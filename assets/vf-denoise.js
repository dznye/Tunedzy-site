/* Tunedzy free tools: noise suppression that learns YOUR background noise. Runs in the visitor's browser (AudioWorklet) or offline on a file.
   Method: short-time Fourier transform (512 samples, 75% overlap), noise spectrum learned from a few seconds of room tone (or tracked
   automatically), Wiener-style gain with time and frequency smoothing, then an optional noise gate set from the learned noise level.
   Best on steady noise (fans, hiss, AC, hum, PC noise). It cannot remove voices or keyboard clatter. Nothing is uploaded. */
(function (root) {
  'use strict';

  // ---------- radix-2 complex FFT (in place). Kept as a plain function so its source can be copied into the AudioWorklet.
  function fftInPlace(re, im) {
    var n = re.length, i, j, k, m, t;
    for (i = 1, j = 0; i < n; i++) {
      var bit = n >> 1;
      for (; j & bit; bit >>= 1) j ^= bit;
      j ^= bit;
      if (i < j) { t = re[i]; re[i] = re[j]; re[j] = t; t = im[i]; im[i] = im[j]; im[j] = t; }
    }
    for (var len = 2; len <= n; len <<= 1) {
      var ang = -2 * Math.PI / len, wr = Math.cos(ang), wi = Math.sin(ang), half = len >> 1;
      for (i = 0; i < n; i += len) {
        var cr = 1, ci = 0;
        for (k = 0; k < half; k++) {
          var a = i + k, b = a + half;
          var xr = re[b] * cr - im[b] * ci, xi = re[b] * ci + im[b] * cr;
          re[b] = re[a] - xr; im[b] = im[a] - xi; re[a] += xr; im[a] += xi;
          m = cr * wr - ci * wi; ci = cr * wi + ci * wr; cr = m;
        }
      }
    }
  }

  class Denoiser {
    constructor(sr, N, hop) {
      this.sr = sr; this.N = N || 512; this.hop = hop || 128;
      var n = this.N, h = this.hop;
      this.win = new Float32Array(n); var ws = 0;
      for (var i = 0; i < n; i++) { this.win[i] = 0.5 - 0.5 * Math.cos(2 * Math.PI * (i + 0.5) / n); ws += this.win[i] * this.win[i]; }
      this.norm = h / ws;                                         // overlap-add normalisation for the window pair
      this.winPow = ws;
      this.inRing = new Float32Array(n); this.inPos = 0; this.cnt = 0;
      this.acc = new Float32Array(n); this.fifo = new Float32Array(n * 4); this.fh = 0; this.ft = 0; this.fn = 0;
      this.re = new Float32Array(n); this.im = new Float32Array(n);
      var K = n / 2 + 1; this.K = K;
      this.P = new Float32Array(K); this.G = new Float32Array(K).fill(1); this.Gs = new Float32Array(K).fill(1);
      this.noise = new Float32Array(K); this.hasProfile = false;
      this.ps = new Float32Array(K); this.nmin = new Float32Array(K).fill(1e-3); this.navg = new Float32Array(K); this.warm = 0;   // automatic tracker
      this.learning = false; this.learnFrames = 0; this.learnAcc = new Float64Array(K); this.learnCount = 0; this.onLearn = null;
      this.reduceDb = 18; this.sens = 1.6; this.gateOn = true; this.gateOffsetDb = 6; this.polish = false;
      this.gateG = 1; this.env = 0; this.bypass = false; this.vad = 1; this.autoSens = 0.65;
      this.inE = 0; this.outE = 0; this.meterN = 0; this.noiseRms = 0;
    }
    setParams(p) { for (var k in p) if (p[k] !== undefined) this[k] = p[k]; }
    startLearn(seconds) { this.learning = true; this.learnFrames = Math.max(8, Math.round(seconds * this.sr / this.hop)); this.learnAcc.fill(0); this.learnCount = 0; }
    setProfile(arr) { this.noise.set(arr); this.hasProfile = true; this._updNoiseRms(); }
    clearProfile() { this.hasProfile = false; }
    _updNoiseRms() { var s = 0, K = this.K; for (var k = 0; k < K; k++) s += this.noise[k] * (k === 0 || k === K - 1 ? 1 : 2); this.noiseRms = Math.sqrt(s / (this.N * this.winPow)); }

    _frame() {
      var n = this.N, K = this.K, re = this.re, im = this.im, w = this.win, i, k;
      for (i = 0; i < n; i++) { re[i] = this.inRing[(this.inPos + i) % n] * w[i]; im[i] = 0; }
      fftInPlace(re, im);
      var P = this.P, noise = this.noise;
      for (k = 0; k < K; k++) P[k] = re[k] * re[k] + im[k] * im[k];
      if (this.learning) {
        for (k = 0; k < K; k++) this.learnAcc[k] += P[k];
        this.learnCount++;
        if (this.learnCount >= this.learnFrames) {
          for (k = 0; k < K; k++) noise[k] = this.learnAcc[k] / this.learnCount;
          this.hasProfile = true; this.learning = false; this._updNoiseRms(); if (this.onLearn) this.onLearn(this.noiseRms);
        }
      }
      var est = noise;
      if (!this.hasProfile) {                                       // automatic: average the bins that look like noise (near the tracked quiet floor)
        var ps = this.ps, nm = this.nmin, na = this.navg; this.warm++;
        for (k = 0; k < K; k++) {
          ps[k] = 0.85 * ps[k] + 0.15 * P[k];
          nm[k] = ps[k] < nm[k] ? ps[k] : nm[k] + (ps[k] - nm[k]) * 0.0004;
          if (this.warm < 24) na[k] += 0.2 * (P[k] - na[k]);       // first frames: assume mostly noise so the estimate starts sensible
          else if (P[k] < 4 * nm[k] + 1e-12) na[k] += 0.03 * (P[k] - na[k]);
          this.noise[k] = na[k] * 1.12;
        }
        est = this.noise; if (this.warm % 16 === 0) this._updNoiseRms();
      }
      var gmin = Math.pow(10, -this.reduceDb / 20), a = this.hasProfile ? this.sens : this.sens * this.autoSens, G = this.G, Gs = this.Gs, g;
      for (k = 0; k < K; k++) { var p = P[k] + 1e-12; g = 1 - a * est[k] / p; g = g > gmin * gmin ? Math.sqrt(g) : gmin; G[k] = g; }
      // frame-level voice check: a frame no louder than the learned noise is room tone, so it gets the full reduction
      var lo = Math.max(1, Math.round(100 * n / this.sr)), hi = Math.min(K - 1, Math.round(5000 * n / this.sr)), sp = 1e-12, se = 1e-12;
      for (k = lo; k <= hi; k++) { sp += P[k]; se += est[k]; }
      var ratio = sp / se, v = (ratio - 1.5) / 2.0; v = v < 0 ? 0 : v > 1 ? 1 : v;
      this.vad += (v > this.vad ? 0.7 : 0.06) * (v - this.vad);
      var vg = gmin + (1 - gmin) * this.vad;
      for (k = 0; k < K; k++) G[k] *= vg;
      for (k = 0; k < K; k++) {                                     // smooth across frequency, then in time (fast open, slower close)
        var l = G[k > 0 ? k - 1 : 0], r = G[k < K - 1 ? k + 1 : K - 1], f = 0.25 * l + 0.5 * G[k] + 0.25 * r;
        var b = f > Gs[k] ? 0.75 : 0.22; Gs[k] += b * (f - Gs[k]);
      }
      for (k = 0; k < K; k++) { var gg = this.bypass ? 1 : Gs[k]; re[k] *= gg; im[k] *= gg; if (k > 0 && k < K - 1) { re[n - k] *= gg; im[n - k] *= gg; } }
      for (i = 0; i < n; i++) im[i] = -im[i];                       // inverse FFT via conjugate trick
      fftInPlace(re, im);
      var acc = this.acc, nrm = this.norm / n;
      for (i = 0; i < n; i++) acc[i] += re[i] * nrm * w[i];
      var fifo = this.fifo, fl = fifo.length;
      for (i = 0; i < this.hop; i++) { fifo[this.ft] = acc[i]; this.ft = (this.ft + 1) % fl; this.fn++; }
      acc.copyWithin(0, this.hop); acc.fill(0, n - this.hop);
    }

    // inp/out: Float32Array of the same length (any length). out is written in place; out may be the same array as inp.
    process(inp, out) {
      var n = this.N, hop = this.hop, L = inp.length, i, ie = 0, oe = 0;
      for (i = 0; i < L; i++) {
        var x = inp[i]; ie += x * x;
        this.inRing[this.inPos] = x; this.inPos = (this.inPos + 1) % n;
        if (++this.cnt === hop) { this.cnt = 0; this._frame(); }
        var y = 0; if (this.fn > 0) { y = this.fifo[this.fh]; this.fh = (this.fh + 1) % this.fifo.length; this.fn--; }
        // gate, set from the learned noise level
        if (this.gateOn && this.noiseRms > 0) {
          var thr = this.noiseRms * Math.pow(10, this.gateOffsetDb / 20), ay = y < 0 ? -y : y;
          this.env += (ay > this.env ? 0.03 : 0.0004) * (ay - this.env);
          var target = this.env > thr * 0.5 ? 1 : 0.06;
          this.gateG += (target > this.gateG ? 0.004 : 0.00045) * (target - this.gateG); y *= this.bypass ? 1 : this.gateG;
        }
        out[i] = y; oe += y * y;
      }
      this.inE += ie; this.outE += oe; this.meterN += L;
    }
    meter() { var n = this.meterN || 1, r = { inDb: 10 * Math.log10(this.inE / n + 1e-12), outDb: 10 * Math.log10(this.outE / n + 1e-12), noiseDb: this.noiseRms > 0 ? 20 * Math.log10(this.noiseRms) : -120 }; this.inE = this.outE = this.meterN = 0; return r; }
  }

  // ---------- AudioWorklet source: fftInPlace + Denoiser + a processor
  function workletSource() {
    return fftInPlace.toString() + '\n' + Denoiser.toString() + '\n' + [
      'class VFDenoiseProc extends AudioWorkletProcessor {',
      '  constructor(){ super(); this.d = new Denoiser(sampleRate, 512, 128); this.t = 0;',
      '    this.d.onLearn = (rms) => this.port.postMessage({learned: true, noiseRms: rms, profile: Array.from(this.d.noise)});',
      '    this.port.onmessage = (e) => { const m = e.data;',
      '      if (m.cmd === "learn") this.d.startLearn(m.seconds || 3);',
      '      else if (m.cmd === "params") this.d.setParams(m.p);',
      '      else if (m.cmd === "profile") this.d.setProfile(m.profile);',
      '      else if (m.cmd === "clear") this.d.clearProfile(); }; }',
      '  process(inputs, outputs){ const i = inputs[0] && inputs[0][0], o = outputs[0][0]; if (!i){ if (o) o.fill(0); return true; }',
      '    this.d.process(i, o); this.t += i.length; if (this.t >= sampleRate * 0.06){ this.t = 0; const m = this.d.meter(); m.learning = this.d.learning; m.progress = this.d.learning ? this.d.learnCount / this.d.learnFrames : 0; this.port.postMessage(m); }',
      '    for (let c = 1; c < outputs[0].length; c++) outputs[0][c].set(o); return true; }',
      '}',
      "registerProcessor('vf-denoise', VFDenoiseProc);"
    ].join('\n');
  }

  // ---------- offline: clean a whole recording. profile (optional) = noise power spectrum; otherwise learn from the quietest second.
  // The quietest half-second of the file, if the file really has a steady quiet floor: several windows share (nearly) the same lowest level.
  // Continuous speech has no such floor, so null is returned and the caller tracks the noise automatically instead.
  function quietestSecond(x, sr) {
    var w = Math.min(x.length, Math.round(sr * 0.5)), step = Math.round(sr * 0.05), i, wins = [];
    for (var s = 0; s + w <= x.length; s += step) {
      var e = 0; for (i = s; i < s + w; i += 4) e += x[i] * x[i];
      wins.push({ s: s, e: e / (w / 4) });
    }
    if (wins.length < 8) return null;
    var best = wins[0]; wins.forEach(function (q) { if (q.e > 1e-10 && (best.e <= 1e-10 || q.e < best.e)) best = q; });
    if (best.e <= 1e-10) return null;
    var near = 0, sorted = wins.map(function (q) { return q.e; }).sort(function (a, b) { return a - b; }), median = sorted[sorted.length >> 1], top = sorted[sorted.length - 1];
    wins.forEach(function (q) { if (q.e <= best.e * 1.6) near++; });
    var stable = near >= Math.max(4, Math.round(wins.length * 0.04)) && top > best.e * 2.5;     // a steady floor with louder material above it
    var clearlyQuieter = best.e < median * 0.15;                                                // or at least 8 dB under the typical level
    if (!stable && !clearlyQuieter) return null;
    return x.subarray(best.s, Math.min(x.length, best.s + w));
  }
  function cleanBuffer(x, sr, opts) {
    opts = opts || {};
    var d = new Denoiser(sr, 512, 128);
    d.setParams({ reduceDb: opts.reduceDb != null ? opts.reduceDb : 18, sens: opts.sens != null ? opts.sens : 1.6, gateOn: opts.gateOn !== false, gateOffsetDb: opts.gateOffsetDb != null ? opts.gateOffsetDb : 6 });
    var learned = false;
    if (opts.profile) { d.setProfile(opts.profile); learned = true; }
    else if (!opts.auto) {
      var q = quietestSecond(x, sr);
      if (q) {
        var tmp = new Denoiser(sr, 512, 128), pad = new Float32Array(q.length), o = new Float32Array(q.length);
        pad.set(q); tmp.startLearn(Math.max(0.25, q.length / sr * 0.8));
        for (var r = 0; r < 6 && tmp.learning; r++) tmp.process(pad, o);
        if (tmp.hasProfile) { d.setProfile(tmp.noise); learned = true; }
      }
    }
    if (!learned) {                                                 // no real silence: track the noise over the whole file, average it into one steady profile
      var tr = new Denoiser(sr, 512, 128), sink = new Float32Array(x.length), mean = new Float32Array(tr.K), cnt = 0, step = 8192;
      tr.setParams({ gateOn: false });
      for (var o2 = 0; o2 < x.length; o2 += step) {
        var seg = x.subarray(o2, Math.min(x.length, o2 + step)); tr.process(seg, sink.subarray(o2, o2 + seg.length));
        if (tr.warm > 200) { for (var k = 0; k < tr.K; k++) mean[k] += tr.noise[k]; cnt++; }
      }
      if (cnt) { for (var k2 = 0; k2 < mean.length; k2++) mean[k2] /= cnt; var sc = opts.trackScale != null ? opts.trackScale : 0.5; for (var k3 = 0; k3 < mean.length; k3++) mean[k3] *= sc; d.setProfile(mean); learned = 'tracked';
      d.setParams({ reduceDb: Math.min(d.reduceDb, 12), sens: Math.min(d.sens, 1.0) }); }          // gentle: without real silence the estimate is less certain
    }
    var out = new Float32Array(x.length), padIn = new Float32Array(x.length + d.N), padOut = new Float32Array(x.length + d.N);
    padIn.set(x); d.process(padIn, padOut);                         // flush: the output lags the input by N-1 samples
    var lag = d.N - 1; for (var i = 0; i < x.length; i++) out[i] = padOut[i + lag];
    return { out: out, noiseRms: d.noiseRms, learned: learned };
  }

  var api = { Denoiser: Denoiser, fftInPlace: fftInPlace, workletSource: workletSource, cleanBuffer: cleanBuffer, quietestSecond: quietestSecond };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.VFDenoise = api;
})(typeof window !== 'undefined' ? window : globalThis);
