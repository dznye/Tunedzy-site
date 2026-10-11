/* VocalForge free tools: audio analysis that runs entirely in the visitor's browser (nothing is uploaded).
   Pure functions on Float32Array so the same code is tested in Node. */
(function (root) {
  'use strict';

  // ---------------------------------------------------------------- basics
  function fft(re, im) {                      // in-place radix-2
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
  function hann(n) { var w = new Float32Array(n); for (var i = 0; i < n; i++) w[i] = 0.5 - 0.5 * Math.cos(2 * Math.PI * i / n); return w; }

  function mixMono(chs) {
    if (chs.length === 1) return chs[0];
    var n = chs[0].length, out = new Float32Array(n), c = chs.length;
    for (var i = 0; i < n; i++) { var s = 0; for (var k = 0; k < c; k++) s += chs[k][i]; out[i] = s / c; }
    return out;
  }
  function decimate(x, sr, target) {          // box-average decimation (cheap low-pass), returns {x, sr}
    var f = Math.max(1, Math.floor(sr / target));
    if (f === 1) return { x: x, sr: sr };
    var n = Math.floor(x.length / f), out = new Float32Array(n);
    for (var i = 0; i < n; i++) { var s = 0, o = i * f; for (var k = 0; k < f; k++) s += x[o + k]; out[i] = s / f; }
    return { x: out, sr: sr / f };
  }
  function window_(x, sr, maxSec) {           // take up to maxSec from the middle of the file
    var max = Math.floor(maxSec * sr);
    if (x.length <= max) return x;
    var start = Math.floor((x.length - max) / 2);
    return x.subarray(start, start + max);
  }
  function percentile(arr, p) {
    var a = Array.prototype.slice.call(arr).sort(function (u, v) { return u - v; });
    if (!a.length) return 0;
    return a[Math.min(a.length - 1, Math.max(0, Math.round(p * (a.length - 1))))];
  }
  var db = function (v) { return 20 * Math.log10(Math.max(v, 1e-10)); };

  // ---------------------------------------------------------------- tempo
  function onsetEnvelope(x, sr) {
    var N = 1024, hop = 128, w = hann(N), bins = N / 2, nF = Math.max(0, Math.floor((x.length - N) / hop));
    var re = new Float32Array(N), im = new Float32Array(N), prev = new Float32Array(bins), env = new Float32Array(nF);
    var top = Math.min(bins, Math.floor(6000 / (sr / N)));
    for (var f = 0; f < nF; f++) {
      var o = f * hop;
      for (var i = 0; i < N; i++) { re[i] = x[o + i] * w[i]; im[i] = 0; }
      fft(re, im);
      var flux = 0;
      for (var b = 1; b < top; b++) {
        var m = Math.log(1 + 100 * Math.sqrt(re[b] * re[b] + im[b] * im[b]) / N * 2);
        var d = m - prev[b]; if (d > 0) flux += d; prev[b] = m;
      }
      env[f] = flux;
    }
    var fps = sr / hop, win = Math.max(3, Math.round(fps * 0.4)), out = new Float32Array(nF), run = 0;
    for (var t = 0; t < nF; t++) {              // subtract moving average, half-wave rectify
      run += env[t]; if (t >= win) run -= env[t - win];
      var mean = run / Math.min(t + 1, win), v = env[t] - mean;
      out[t] = v > 0 ? v : 0;
    }
    return { env: out, fps: fps };
  }

  function autocorr(env, maxLag) {
    var n = env.length, ac = new Float32Array(maxLag + 2), mean = 0, i, l;
    for (i = 0; i < n; i++) mean += env[i]; mean /= n;
    var e = new Float32Array(n); for (i = 0; i < n; i++) e[i] = env[i] - mean;
    for (l = 0; l <= maxLag + 1; l++) { var s = 0; for (i = l; i < n; i++) s += e[i] * e[i - l]; ac[l] = s / (n - l); }
    var z = ac[0] || 1; for (l = 0; l < ac.length; l++) ac[l] /= z;
    return ac;
  }
  function acAt(ac, lag) {                    // linear interpolation
    var i = Math.floor(lag), fr = lag - i;
    if (i + 1 >= ac.length || i < 0) return 0;
    return ac[i] * (1 - fr) + ac[i + 1] * fr;
  }
  function tempoScore(ac, fps, bpm) {
    var L = fps * 60 / bpm, s = 0, w = 0, mult = [1, 2, 3, 4];
    for (var k = 0; k < mult.length; k++) { if (L * mult[k] < ac.length - 2) { s += acAt(ac, L * mult[k]) / Math.sqrt(mult[k]); w += 1 / Math.sqrt(mult[k]); } }
    return w ? s / w : 0;
  }
  function estimateTempo(x, sr) {
    var o = onsetEnvelope(x, sr), fps = o.fps;
    if (o.env.length < fps * 6) return null;
    var maxLag = Math.ceil(fps * 60 / 55 * 4) + 4, ac = autocorr(o.env, maxLag), cand = [], bpm;
    for (bpm = 60; bpm <= 200; bpm += 0.5) {
      var prior = Math.exp(-0.5 * Math.pow(Math.log2(bpm / 112) / 0.85, 2));
      cand.push({ bpm: bpm, raw: tempoScore(ac, fps, bpm), score: tempoScore(ac, fps, bpm) * (0.55 + 0.45 * prior) });
    }
    var best = cand[0], i;
    for (i = 1; i < cand.length; i++) if (cand[i].score > best.score) best = cand[i];
    var fine = best, b;                        // refine in 0.05 steps
    for (b = best.bpm - 1.5; b <= best.bpm + 1.5; b += 0.05) { var sc = tempoScore(ac, fps, b); if (sc > fine.raw) fine = { bpm: b, raw: sc }; }
    var tempo = Math.round(fine.bpm * 10) / 10;
    // downbeat grid phase: the offset (in frames) whose comb sum is largest
    var period = fps * 60 / fine.bpm, bestPh = 0, bestV = -1, ph;
    for (ph = 0; ph < period; ph += 0.5) { var v = 0, p = ph, cnt = 0; while (p < o.env.length - 1) { v += o.env[Math.round(p)]; p += period; cnt++; } v /= cnt; if (v > bestV) { bestV = v; bestPh = ph; } }
    // confidence: how much the peak stands out from the rest of the tempogram
    var raws = cand.map(function (c) { return c.raw; }), med = percentile(raws, 0.5), top = fine.raw;
    var conf = Math.max(0, Math.min(1, (top - med) / (Math.abs(top) + 0.2)));
    var alt = [];
    [[0.5, 'half'], [2, 'double'], [4 / 3, 'x4/3'], [0.75, 'x3/4'], [1.5, 'x3/2'], [2 / 3, 'x2/3']].forEach(function (m) {
      var t2 = tempo * m[0]; if (t2 < 55 || t2 > 200) return;
      var sc2 = tempoScore(ac, fps, t2); if (m[1].charAt(0) === 'x' && sc2 < fine.raw * 0.8) return;
      alt.push(Math.round(t2 * 10) / 10);
    });
    return { bpm: tempo, alt: alt, confidence: conf, beatOffsetSec: bestPh / fps };
  }

  // ---------------------------------------------------------------- key + chords
  var NOTES_MAJ = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B'];
  var NOTES_MIN = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B'];
  var CAM_MAJ = [8, 3, 10, 5, 12, 7, 2, 9, 4, 11, 6, 1];
  var KK_MAJ = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88];
  var KK_MIN = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17];

  function chromaFrames(x, sr, N, hop) {
    var w = hann(N), re = new Float32Array(N), im = new Float32Array(N), frames = [], bw = sr / N;
    var lo = Math.ceil(65 / bw), hi = Math.min(N / 2 - 1, Math.floor(2000 / bw));
    var pcOf = new Int8Array(hi + 1), wt = new Float32Array(hi + 1);
    for (var b = lo; b <= hi; b++) {
      var midi = 69 + 12 * Math.log2((b * bw) / 440), r = Math.round(midi), dist = Math.abs(midi - r);
      pcOf[b] = ((r % 12) + 12) % 12; wt[b] = Math.max(0, Math.cos(dist * Math.PI)) ;   // 1 on a note, 0 halfway between
    }
    for (var o = 0; o + N <= x.length; o += hop) {
      for (var i = 0; i < N; i++) { re[i] = x[o + i] * w[i]; im[i] = 0; }
      fft(re, im);
      var ch = new Float32Array(12), tot = 0;
      for (b = lo; b <= hi; b++) { var mag = Math.sqrt(re[b] * re[b] + im[b] * im[b]); var v = Math.sqrt(mag) * wt[b] * (1 / (1 + b * bw / 1500)); ch[pcOf[b]] += v; tot += v; }
      if (tot > 1e-6) for (var k = 0; k < 12; k++) ch[k] /= tot;
      frames.push({ t: o / sr, ch: ch, ok: tot > 1e-6 });
    }
    return frames;
  }
  function pearson(a, b) {
    var n = a.length, ma = 0, mb = 0, i; for (i = 0; i < n; i++) { ma += a[i]; mb += b[i]; } ma /= n; mb /= n;
    var s = 0, va = 0, vb = 0; for (i = 0; i < n; i++) { var da = a[i] - ma, db_ = b[i] - mb; s += da * db_; va += da * da; vb += db_ * db_; }
    return s / Math.sqrt((va * vb) || 1);
  }
  function estimateKey(frames) {
    var sum = new Float32Array(12), n = 0;
    frames.forEach(function (f) { if (f.ok) { for (var k = 0; k < 12; k++) sum[k] += f.ch[k]; n++; } });
    if (n < 4) return null;
    var res = [];
    for (var tonic = 0; tonic < 12; tonic++) {
      var maj = [], min = [];
      for (var k = 0; k < 12; k++) { maj.push(KK_MAJ[(k - tonic + 12) % 12]); min.push(KK_MIN[(k - tonic + 12) % 12]); }
      res.push({ tonic: tonic, mode: 'major', r: pearson(sum, maj) });
      res.push({ tonic: tonic, mode: 'minor', r: pearson(sum, min) });
    }
    res.sort(function (a, b) { return b.r - a.r; });
    function label(k) { return k.mode === 'major' ? NOTES_MAJ[k.tonic] + ' major' : NOTES_MIN[k.tonic] + ' minor'; }
    function camelot(k) { return k.mode === 'major' ? CAM_MAJ[k.tonic] + 'B' : CAM_MAJ[(k.tonic + 3) % 12] + 'A'; }
    function relative(k) { return k.mode === 'major' ? { tonic: (k.tonic + 9) % 12, mode: 'minor' } : { tonic: (k.tonic + 3) % 12, mode: 'major' }; }
    var best = res[0], rel = relative(best);
    var distinct = res.filter(function (k) { return !(k.tonic === rel.tonic && k.mode === rel.mode) && !(k === best); });
    var second = distinct[0];
    return { tonic: best.tonic, mode: best.mode, name: label(best), camelot: camelot(best), relative: label(rel), r: best.r,
             confidence: Math.max(0, Math.min(1, (best.r - second.r) * 8 + (best.r - 0.5))),
             others: distinct.slice(0, 3).map(function (k) { return { name: label(k), r: k.r }; }), profile: Array.prototype.slice.call(sum) };
  }

  var TRIADS = (function () {
    var t = [];
    for (var root = 0; root < 12; root++) {
      var maj = new Float32Array(12), min = new Float32Array(12);
      maj[root] = 1; maj[(root + 4) % 12] = 0.9; maj[(root + 7) % 12] = 0.95;
      min[root] = 1; min[(root + 3) % 12] = 0.9; min[(root + 7) % 12] = 0.95;
      t.push({ root: root, q: '', v: maj }); t.push({ root: root, q: 'm', v: min });
    }
    return t;
  })();
  function cosine(a, b) { var s = 0, na = 0, nb = 0; for (var i = 0; i < 12; i++) { s += a[i] * b[i]; na += a[i] * a[i]; nb += b[i] * b[i]; } return s / Math.sqrt((na * nb) || 1); }
  function degreeLabel(ch, key) {
    var iv = (ch.root - key.tonic + 12) % 12, maj = { 0: 'I', 2: 'ii', 4: 'iii', 5: 'IV', 7: 'V', 9: 'vi' }, min = { 0: 'i', 3: 'III', 5: 'iv', 7: 'v', 8: 'VI', 10: 'VII' };
    var tbl = key.mode === 'major' ? maj : min, s = tbl[iv];
    if (!s) return '';
    var isMin = s === s.toLowerCase(); return ((ch.q === 'm') === isMin) ? s : '';
  }
  function inKey(ch, key) {
    var iv = (ch.root - key.tonic + 12) % 12;
    var tbl = key.mode === 'major' ? { 0: '', 2: 'm', 4: 'm', 5: '', 7: '', 9: 'm' } : { 0: 'm', 3: '', 5: 'm', 7: 'm', 8: '', 10: '' };
    return tbl[iv] !== undefined && tbl[iv] === ch.q;
  }
  function estimateChords(x, sr, tempo, key) {
    var N = 4096, hop = 1024, frames = chromaFrames(x, sr, N, hop);
    if (frames.length < 8 || !tempo || !key) return null;
    var beat = 60 / tempo.bpm, seg = beat * 2, dur = x.length / sr;
    function run(off) {
      var out = [], total = 0, t;
      for (t = off; t + seg * 0.5 < dur; t += seg) {
        var ch = new Float32Array(12), n = 0;
        for (var fi = 0; fi < frames.length; fi++) { var f = frames[fi], c = f.t + N / sr / 2; if (f.ok && c >= t && c < t + seg) { for (var k = 0; k < 12; k++) ch[k] += f.ch[k]; n++; } }
        if (!n) continue;
        var best = null, bestS = -1;
        TRIADS.forEach(function (tr) { var sc = cosine(ch, tr.v) * (inKey(tr, key) ? 1 : 0.86); if (sc > bestS) { bestS = sc; best = tr; } });
        out.push({ t: t, root: best.root, q: best.q, score: bestS, chord: NOTES_MAJ[best.root] + best.q }); total += bestS;
      }
      return { out: out, avg: out.length ? total / out.length : 0 };
    }
    var bestRun = null, o0 = tempo.beatOffsetSec % seg;
    for (var j = 0; j < 4; j++) { var r = run((o0 + j * beat / 2) % seg); if (!bestRun || r.avg > bestRun.avg + 0.005) bestRun = r; }
    var out = bestRun.out;
    for (var i = 1; i < out.length - 1; i++) if (out[i - 1].chord === out[i + 1].chord && out[i].chord !== out[i - 1].chord && out[i].score < 0.82) { out[i].chord = out[i - 1].chord; out[i].root = out[i - 1].root; out[i].q = out[i - 1].q; }
    var merged = [];
    out.forEach(function (c) {
      var last = merged[merged.length - 1];
      if (last && last.chord === c.chord) last.len += seg; else merged.push({ t: c.t, chord: c.chord, root: c.root, q: c.q, deg: degreeLabel(c, key), len: seg });
    });
    var counts = {}; out.forEach(function (c) { counts[c.chord] = (counts[c.chord] || 0) + 1; });
    var top = Object.keys(counts).sort(function (u, v) { return counts[v] - counts[u]; }).slice(0, 6).map(function (c) { return { chord: c, n: counts[c] }; });
    var seq = merged.map(function (c) { return c.chord; }), loops = {}, first = {}, L;
    for (L = 2; L <= 4; L++) for (i = 0; i + L <= seq.length; i++) {
      var sl = seq.slice(i, i + L); if (new Set(sl).size < 2) continue;
      var k2 = sl.join(' '); loops[k2] = (loops[k2] || 0) + L; if (first[k2] === undefined) first[k2] = i;
    }
    var loop = Object.keys(loops).sort(function (u, v) { return (loops[v] - loops[u]) || (first[u] - first[v]); })[0] || '';
    return { timeline: merged, top: top, loop: loop, segment: seg };
  }

  // ---------------------------------------------------------------- loudness (ITU-R BS.1770 / EBU R128)
  function biquad(b, a, x) {
    var y = new Float64Array(x.length), x1 = 0, x2 = 0, y1 = 0, y2 = 0;
    for (var i = 0; i < x.length; i++) {
      var xi = x[i], yi = b[0] * xi + b[1] * x1 + b[2] * x2 - a[1] * y1 - a[2] * y2;
      y[i] = yi; x2 = x1; x1 = xi; y2 = y1; y1 = yi;
    }
    return y;
  }
  function kCoefs(fs) {
    var G = 3.999843853973347, f0 = 1681.974450955533, Q = 0.7071752369554196;
    var A = Math.pow(10, G / 40), w0 = 2 * Math.PI * f0 / fs, al = Math.sin(w0) / (2 * Q), c = Math.cos(w0), sA = 2 * Math.sqrt(A) * al;
    var a0 = (A + 1) - (A - 1) * c + sA;
    var s1 = { b: [A * ((A + 1) + (A - 1) * c + sA) / a0, -2 * A * ((A - 1) + (A + 1) * c) / a0, A * ((A + 1) + (A - 1) * c - sA) / a0],
               a: [1, 2 * ((A - 1) - (A + 1) * c) / a0, ((A + 1) - (A - 1) * c - sA) / a0] };
    var f1 = 38.13547087602444, Q1 = 0.5003270373238773, w1 = 2 * Math.PI * f1 / fs, al1 = Math.sin(w1) / (2 * Q1), c1 = Math.cos(w1), a01 = 1 + al1;
    var s2 = { b: [(1 + c1) / 2 / a01, -(1 + c1) / a01, (1 + c1) / 2 / a01], a: [1, -2 * c1 / a01, (1 - al1) / a01] };
    return [s1, s2];
  }
  function measureLoudness(chs, sr) {
    var co = kCoefs(sr), filt = chs.map(function (c) { var y = c; co.forEach(function (s) { y = biquad(s.b, s.a, y); }); return y; });
    var blk = Math.round(0.4 * sr), step = Math.round(0.1 * sr), n = chs[0].length, ms = [];
    for (var s = 0; s + blk <= n; s += step) {
      var tot = 0; for (var c = 0; c < filt.length; c++) { var acc = 0, f = filt[c]; for (var i = s; i < s + blk; i++) acc += f[i] * f[i]; tot += acc / blk; }
      ms.push(tot);
    }
    var lk = function (z) { return -0.691 + 10 * Math.log10(Math.max(z, 1e-12)); };
    if (!ms.length) return null;
    var abs = ms.filter(function (z) { return lk(z) > -70; });
    if (!abs.length) return { lufs: -Infinity, momentaryMax: -Infinity, shortTermMax: -Infinity, lra: 0 };
    var mean = abs.reduce(function (a, b) { return a + b; }, 0) / abs.length, rel = lk(mean) - 10;
    var gated = ms.filter(function (z) { return lk(z) > -70 && lk(z) > rel; });
    var integ = lk(gated.reduce(function (a, b) { return a + b; }, 0) / gated.length);
    var mMax = lk(Math.max.apply(null, ms));
    var st = [], w = 30;                       // short-term = 3 s = 30 steps of 100 ms (mean of block powers)
    for (var j = 0; j + w <= ms.length; j += 5) { var q = 0; for (var u = j; u < j + w; u++) q += ms[u]; st.push(lk(q / w)); }
    var stg = st.filter(function (v) { return v > -70; }), lra = 0;
    if (stg.length > 4) { var m2 = stg.map(function (v) { return Math.pow(10, v / 10); }).reduce(function (a, b) { return a + b; }, 0) / stg.length; var g2 = stg.filter(function (v) { return v > 10 * Math.log10(m2) - 20; }); if (g2.length > 2) lra = percentile(g2, 0.95) - percentile(g2, 0.10); }
    return { lufs: integ, momentaryMax: mMax, shortTermMax: st.length ? Math.max.apply(null, st) : integ, lra: lra };
  }
  function peaks(chs) {
    var pk = 0, clipRuns = 0, i, c, run;
    chs.forEach(function (x) {
      run = 0;
      for (i = 0; i < x.length; i++) {
        var a = Math.abs(x[i]); if (a > pk) pk = a;
        if (a >= 0.995) { run++; if (run === 3) clipRuns++; } else run = 0;
      }
    });
    // true peak estimate: 4x linear-phase sinc interpolation around the loudest samples
    var tp = pk, thr = pk * 0.7;
    chs.forEach(function (x) {
      for (i = 8; i < x.length - 8; i++) {
        if (Math.abs(x[i]) < thr) continue;
        for (var ph = 1; ph < 4; ph++) {
          var t = ph / 4, s = 0;
          for (var k = -7; k <= 8; k++) { var d = k - t, sinc = Math.abs(d) < 1e-9 ? 1 : Math.sin(Math.PI * d) / (Math.PI * d), win = 0.5 + 0.5 * Math.cos(Math.PI * d / 8.5); s += x[i + k] * sinc * win; }
          if (Math.abs(s) > tp) tp = Math.abs(s);
        }
      }
    });
    return { samplePeak: pk, truePeak: tp, clipRuns: clipRuns };
  }

  // ---------------------------------------------------------------- vocal check-up
  function frameLevels(x, sr) {
    var f = Math.round(sr * 0.02), n = Math.floor(x.length / f), out = [];
    for (var i = 0; i < n; i++) { var s = 0, o = i * f; for (var k = 0; k < f; k++) s += x[o + k] * x[o + k]; out.push(db(Math.sqrt(s / f))); }
    return out;
  }
  function spectrumBands(x, sr) {
    var N = 4096, w = hann(N), re = new Float32Array(N), im = new Float32Array(N), acc = new Float64Array(N / 2), cnt = 0, bw = sr / N;
    var step = Math.max(N, Math.floor(x.length / 120));
    for (var o = 0; o + N <= x.length; o += step) {
      for (var i = 0; i < N; i++) { re[i] = x[o + i] * w[i]; im[i] = 0; }
      fft(re, im); for (var b = 1; b < N / 2; b++) acc[b] += re[b] * re[b] + im[b] * im[b]; cnt++;
    }
    function band(lo, hi) { var s = 0; for (var b = Math.ceil(lo / bw); b <= Math.min(N / 2 - 1, Math.floor(hi / bw)); b++) s += acc[b]; return s; }
    var total = band(20, sr / 2 - 1) || 1;
    return { rumble: band(20, 80) / total, low: band(80, 300) / total, mid: band(300, 3000) / total, presence: band(3000, 8000) / total, air: band(8000, sr / 2 - 1) / total, sibRatio: band(5000, 9500) / (band(500, 5000) || 1) };
  }
  function checkVocal(chs, sr, lu) {
    var mono = mixMono(chs), lv = frameLevels(mono, sr).filter(function (v) { return v > -90; });
    var pk = peaks(chs), res = {}, loud = percentile(lv, 0.9), floor = percentile(lv, 0.05);
    res.peakDb = db(pk.samplePeak); res.truePeakDb = db(pk.truePeak); res.clipEvents = pk.clipRuns;
    res.loudDb = loud; res.noiseFloorDb = floor; res.snr = loud - floor; res.lufs = lu ? lu.lufs : null;
    var spec = spectrumBands(mono, sr); res.spec = spec;
    var silent = lv.filter(function (v) { return v < floor + 6; }).length / (lv.length || 1); res.quietShare = silent;
    return res;
  }

  // ---------------------------------------------------------------- one call for everything
  function analyzeAll(chs, sr, opts) {
    opts = opts || {}; var prog = opts.progress || function () {};
    var mono = mixMono(chs), seconds = mono.length / sr, r = { seconds: seconds, sampleRate: sr };
    var d = decimate(window_(mono, sr, 150), sr, 12000);
    prog('Finding the tempo', 0.15); r.tempo = estimateTempo(d.x, d.sr);
    prog('Listening for the key', 0.5); var frames = chromaFrames(d.x, d.sr, 8192, 4096); r.key = estimateKey(frames);
    prog('Reading the chords', 0.7); r.chords = estimateChords(d.x, d.sr, r.tempo, r.key);
    prog('Measuring loudness', 0.85); r.loudness = measureLoudness(chs, sr);
    r.check = checkVocal(chs, sr, r.loudness);
    prog('Done', 1);
    return r;
  }

  // ---------------------------------------------------------------- demo loop (synthesised, no copyright)
  function demoLoop(sr) {
    sr = sr || 44100; var bpm = 92, beat = 60 / bpm, bars = 16, dur = bars * 4 * beat, n = Math.floor(dur * sr), x = new Float32Array(n);
    var prog = [[9, 'min'], [5, 'maj'], [0, 'maj'], [7, 'maj']];   // Am F C G
    var sem = function (m) { return 440 * Math.pow(2, (m - 69) / 12); };
    for (var bar = 0; bar < bars; bar++) {
      var ch = prog[bar % 4], root = 48 + ((ch[0] + 12 - 0) % 12), tri = ch[1] === 'min' ? [0, 3, 7] : [0, 4, 7], t0 = bar * 4 * beat;
      tri.forEach(function (iv) {
        var f = sem(root + iv + 12), s = Math.floor(t0 * sr), len = Math.floor(4 * beat * sr);
        for (var i = 0; i < len && s + i < n; i++) { var tt = i / sr, env = Math.min(1, tt * 20) * Math.exp(-tt * 0.5); x[s + i] += 0.07 * env * (Math.sin(2 * Math.PI * f * tt) + 0.4 * Math.sin(4 * Math.PI * f * tt) + 0.2 * Math.sin(6 * Math.PI * f * tt)); }
      });
      var bf = sem(root - 12), bs = Math.floor(t0 * sr), bl = Math.floor(4 * beat * sr);
      for (var j = 0; j < bl && bs + j < n; j++) { var q = j / sr; x[bs + j] += 0.18 * Math.sin(2 * Math.PI * bf * q) * Math.exp(-(q % beat) * 2.5); }
      for (var b = 0; b < 4; b++) {
        var st = Math.floor((t0 + b * beat) * sr);
        if (b % 2 === 0) for (var i2 = 0; i2 < 9000 && st + i2 < n; i2++) { var u = i2 / sr; x[st + i2] += 0.55 * Math.sin(2 * Math.PI * (48 + 90 * Math.exp(-u * 40)) * u) * Math.exp(-u * 14); }
        else for (var i3 = 0; i3 < 7000 && st + i3 < n; i3++) { var v = i3 / sr; x[st + i3] += 0.3 * (Math.random() * 2 - 1) * Math.exp(-v * 22); }
        for (var h = 0; h < 2; h++) { var hs = Math.floor((t0 + b * beat + h * beat / 2) * sr); for (var i4 = 0; i4 < 1800 && hs + i4 < n; i4++) x[hs + i4] += 0.08 * (Math.random() * 2 - 1) * Math.exp(-(i4 / sr) * 90); }
      }
    }
    return { channels: [x], sampleRate: sr };
  }

  var api = { fft: fft, mixMono: mixMono, decimate: decimate, estimateTempo: estimateTempo, chromaFrames: chromaFrames, estimateKey: estimateKey,
              estimateChords: estimateChords, measureLoudness: measureLoudness, peaks: peaks, checkVocal: checkVocal, analyzeAll: analyzeAll, demoLoop: demoLoop };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.VFCore = api;
})(typeof window !== 'undefined' ? window : globalThis);
