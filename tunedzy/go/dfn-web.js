/* Studio sound in the browser: DeepFilterNet3 (Schroeter et al., MIT or Apache-2.0) with ONNX Runtime Web (MIT). A port of neural.py (see its header for the method):
 * 960-point STFT with a Vorbis window, 32 ERB bands, running normalisation, the three network graphs, the ERB mask and the 5-tap deep filter. The model files are
 * downloaded the first time it is used (about 22 MB) and then kept by the service worker. Nothing is uploaded. Tested against the Python version: tests/go_parity. */
'use strict';
const DFN = (() => {
  const SR = 48000, N = 960, H = 480, NB_ERB = 32, NB_DF = 96, ORDER = 5, LA_DF = 2, LA_CONV = 2, ALPHA = 0.99, BINS = N / 2 + 1, M = 2048;
  const PIECE = 20 * SR, CTX = 2 * SR;
  let sess = null, loading = null, base = './';

  /* ---- a 2048-point complex FFT (radix 2, precomputed twiddles), and a 960-point DFT through it (Bluestein) ---- */
  const cosT = new Float64Array(M / 2), sinT = new Float64Array(M / 2); for (let i = 0; i < M / 2; i++) { cosT[i] = Math.cos(2 * Math.PI * i / M); sinT[i] = -Math.sin(2 * Math.PI * i / M); }
  const rev = new Uint16Array(M); for (let i = 0, j = 0; i < M; i++) { rev[i] = j; let bit = M >> 1; for (; j & bit; bit >>= 1) j ^= bit; j ^= bit; }
  function fft(re, im) {
    for (let i = 0; i < M; i++) { const j = rev[i]; if (i < j) { let t = re[i]; re[i] = re[j]; re[j] = t; t = im[i]; im[i] = im[j]; im[j] = t; } }
    for (let len = 2; len <= M; len <<= 1) { const half = len >> 1, step = M / len;
      for (let i = 0; i < M; i += len) for (let k = 0, w = 0; k < half; k++, w += step) { const a = i + k, b = a + half, xr = re[b] * cosT[w] - im[b] * sinT[w], xi = re[b] * sinT[w] + im[b] * cosT[w]; re[b] = re[a] - xr; im[b] = im[a] - xi; re[a] += xr; im[a] += xi; } }
  }
  const chR = new Float64Array(N), chI = new Float64Array(N);                   // chirp e^{i pi n^2 / N}
  for (let n = 0; n < N; n++) { const a = Math.PI * ((n * n) % (2 * N)) / N; chR[n] = Math.cos(a); chI[n] = Math.sin(a); }
  const bR = new Float64Array(M), bI = new Float64Array(M);
  for (let n = 0; n < N; n++) { bR[n] = chR[n]; bI[n] = chI[n]; if (n) { bR[M - n] = chR[n]; bI[M - n] = chI[n]; } }
  fft(bR, bI);
  const wR = new Float64Array(M), wI = new Float64Array(M);
  /** DFT of the complex signal (xr, xi) of length 960 into (or, oi); only the first `keep` outputs are written. */
  function dft(xr, xi, or, oi, keep) {
    wR.fill(0); wI.fill(0);
    for (let n = 0; n < N; n++) { wR[n] = xr[n] * chR[n] + xi[n] * chI[n]; wI[n] = xi[n] * chR[n] - xr[n] * chI[n]; }          // x[n] * conj(chirp[n])
    fft(wR, wI);
    for (let i = 0; i < M; i++) { const r = wR[i] * bR[i] - wI[i] * bI[i], q = wR[i] * bI[i] + wI[i] * bR[i]; wR[i] = r; wI[i] = -q; }  // multiply by FFT(b); conjugate for the inverse
    fft(wR, wI);
    for (let k = 0; k < keep; k++) { const r = wR[k] / M, q = -wI[k] / M; or[k] = r * chR[k] + q * chI[k]; oi[k] = q * chR[k] - r * chI[k]; }
  }

  const erbWidths = (() => {
    const f2e = f => 9.265 * Math.log1p(f / (24.7 * 9.265)), e2f = e => 24.7 * 9.265 * (Math.exp(e / 9.265) - 1), fw = SR / N, lo = f2e(0), hi = f2e(SR / 2), step = (hi - lo) / NB_ERB, w = [];
    let prev = 0, over = 0; for (let i = 1; i <= NB_ERB; i++) { const fb = Math.round(e2f(lo + i * step) / fw); let n = fb - prev - over; if (n < 2) { over = 2 - n; n = 2; } else over = 0; w.push(n); prev = fb; } w[NB_ERB - 1] += 1; return w;
  })();
  const edges = [0]; erbWidths.forEach(w => edges.push(edges[edges.length - 1] + w));
  const WIN = new Float64Array(N); for (let i = 0; i < N; i++) WIN[i] = Math.sin(0.5 * Math.PI * Math.pow(Math.sin(Math.PI * (i + 0.5) / N), 2));
  const WNORM = 1 / (N * N / (2 * H));

  function stft(x) {                       // -> {re, im: Float32Array(T*BINS), T, total}
    const total = H + x.length + N, T = Math.floor((total - N) / H) + 1, re = new Float32Array(T * BINS), im = new Float32Array(T * BINS), xr = new Float64Array(N), xi = new Float64Array(N), or = new Float64Array(BINS), oi = new Float64Array(BINS);
    for (let t = 0; t < T; t++) {
      for (let i = 0; i < N; i++) { const p = t * H + i - H; xr[i] = (p >= 0 && p < x.length ? x[p] : 0) * WIN[i]; xi[i] = 0; }
      dft(xr, xi, or, oi, BINS); const o = t * BINS; for (let k = 0; k < BINS; k++) { re[o + k] = or[k] * WNORM; im[o + k] = oi[k] * WNORM; }
    }
    return {re, im, T, total};
  }
  function istft(re, im, T, total) {
    const out = new Float32Array(total), xr = new Float64Array(N), xi = new Float64Array(N), or = new Float64Array(N), oi = new Float64Array(N);
    for (let t = 0; t < T; t++) {
      const o = t * BINS;
      for (let k = 0; k < BINS; k++) { xr[k] = re[o + k] / WNORM; xi[k] = -im[o + k] / WNORM; }                          // conj of the half spectrum ...
      for (let k = 1; k < N / 2; k++) { xr[N - k] = xr[k]; xi[N - k] = -xi[k]; }                                          // ... and of its mirror
      dft(xr, xi, or, oi, N);
      const p0 = t * H; for (let i = 0; i < N; i++) out[p0 + i] += or[i] / N * WIN[i];                                     // y = conj(DFT(conj X)) / N, real part
    }
    return out;
  }

  function features(re, im, T) {
    const erb = new Float32Array(T * NB_ERB), spec = new Float32Array(2 * T * NB_DF), st = new Float64Array(NB_ERB), su = new Float64Array(NB_DF);
    for (let b = 0; b < NB_ERB; b++) st[b] = -60 + (-90 + 60) * b / (NB_ERB - 1); for (let f = 0; f < NB_DF; f++) su[f] = 0.001 + (0.0001 - 0.001) * f / (NB_DF - 1);
    for (let t = 0; t < T; t++) {
      const o = t * BINS;
      for (let b = 0; b < NB_ERB; b++) { let p = 0; for (let k = edges[b]; k < edges[b + 1]; k++) p += re[o + k] * re[o + k] + im[o + k] * im[o + k]; const db = 10 * Math.log10(p / erbWidths[b] + 1e-10); st[b] = db * (1 - ALPHA) + st[b] * ALPHA; erb[t * NB_ERB + b] = (db - st[b]) / 40; }
      for (let f = 0; f < NB_DF; f++) { const r = re[o + f], q = im[o + f], mag = Math.sqrt(r * r + q * q); su[f] = mag * (1 - ALPHA) + su[f] * ALPHA; const s = 1 / Math.sqrt(su[f]); spec[t * NB_DF + f] = r * s; spec[T * NB_DF + t * NB_DF + f] = q * s; }
    }
    return {erb, spec};
  }

  async function piece(x) {
    const {re, im, T, total} = stft(x), {erb, spec} = features(re, im, T);
    const fe = new Float32Array(T * NB_ERB); fe.set(erb.subarray(LA_CONV * NB_ERB));                                      // the model looks 2 frames ahead
    const fs = new Float32Array(2 * T * NB_DF); for (let c = 0; c < 2; c++) fs.set(spec.subarray(c * T * NB_DF + LA_CONV * NB_DF, (c + 1) * T * NB_DF), c * T * NB_DF);
    const enc = await sess.enc.run({feat_erb: new ort.Tensor('float32', fe, [1, 1, T, NB_ERB]), feat_spec: new ort.Tensor('float32', fs, [1, 2, T, NB_DF])});
    const mk = await sess.erb.run({emb: enc.emb, e3: enc.e3, e2: enc.e2, e1: enc.e1, e0: enc.e0}), cf = await sess.df.run({emb: enc.emb, c0: enc.c0});
    const m = mk.m.data, coefs = cf.coefs.data, oR = new Float32Array(re.length), oI = new Float32Array(im.length);
    for (let t = 0; t < T; t++) {
      const o = t * BINS;
      for (let b = 0; b < NB_ERB; b++) { const g = m[t * NB_ERB + b]; for (let k = edges[b]; k < edges[b + 1]; k++) { oR[o + k] = re[o + k] * g; oI[o + k] = im[o + k] * g; } }
      for (let f = 0; f < NB_DF; f++) {                                                                                  // deep filtering: 5 complex taps over the neighbouring frames
        let ar = 0, ai = 0;
        for (let k = 0; k < ORDER; k++) { const s = t + k - (ORDER - 1 - LA_DF); if (s < 0 || s >= T) continue; const cr = coefs[(t * NB_DF + f) * 10 + k * 2], ci = coefs[(t * NB_DF + f) * 10 + k * 2 + 1], xr = re[s * BINS + f], xi = im[s * BINS + f]; ar += xr * cr - xi * ci; ai += xr * ci + xi * cr; }
        oR[o + f] = ar; oI[o + f] = ai;
      }
    }
    return istft(oR, oI, T, total).subarray(H, H + x.length);
  }

  /** Load the runtime and the three model files from `from` (a folder URL with vendor/ort/ and models/). */
  async function load(from, onProgress) {
    if (sess) return sess; if (loading) return loading; base = from || './';
    loading = (async () => {
      if (typeof ort === 'undefined') await new Promise((res, rej) => { const s = document.createElement('script'); s.src = base + 'vendor/ort/ort.wasm.min.js'; s.onload = res; s.onerror = () => rej(new Error('Could not load the AI runtime.')); document.head.append(s); });
      ort.env.wasm.wasmPaths = new URL(base + 'vendor/ort/', location.href).href; ort.env.wasm.numThreads = 1; ort.env.logLevel = 'error';
      const files = ['enc', 'erb_dec', 'df_dec'], buf = {}; let got = 0;
      for (const f of files) { const r = await fetch(base + 'models/' + f + '.onnx'); if (!r.ok) throw new Error('Could not load the AI model.'); buf[f] = await r.arrayBuffer(); got++; if (onProgress) onProgress(got / (files.length + 1)); }
      const mk = b => ort.InferenceSession.create(b, {executionProviders: ['wasm'], graphOptimizationLevel: 'all'});
      sess = {enc: await mk(buf.enc), erb: await mk(buf.erb_dec), df: await mk(buf.df_dec)}; if (onProgress) onProgress(1); return sess;
    })().catch(e => { loading = null; throw e; });
    return loading;
  }
  const resample = (x, a, b) => {                                                                                         // windowed-sinc, 16 taps each side: plenty for speech
    if (a === b) return Float32Array.from(x); const ratio = b / a, n = Math.round(x.length * ratio), out = new Float32Array(n), cut = Math.min(1, ratio) * .94, T = 16;
    for (let i = 0; i < n; i++) { const c = i / ratio, i0 = Math.floor(c); let s = 0, wsum = 0; for (let j = i0 - T + 1; j <= i0 + T; j++) { const d = (j - c) * cut, w = d === 0 ? 1 : Math.sin(Math.PI * d) / (Math.PI * d), win = .5 + .5 * Math.cos(Math.PI * (j - c) / T); if (j >= 0 && j < x.length) { s += x[j] * w * win * cut; wsum += w * win * cut; } } out[i] = wsum ? s / wsum : 0; }
    return out;
  };
  /** x: mono Float32Array at any rate. -> the enhanced voice, same rate and length. strength 0..1 mixes with the original. */
  async function enhance(x, sr, strength, onProgress) {
    if (!sess) throw new Error('Load the model first.'); const s = Math.max(0, Math.min(1, strength == null ? 1 : strength)); if (s <= 0 || x.length < sr * .2) return Float32Array.from(x);
    const y48 = sr === SR ? x : resample(x, sr, SR), n = y48.length, out = new Float32Array(n); let done = 0;
    while (done < n) {
      const a = done, b = Math.min(n, done + PIECE), lo = Math.max(0, a - CTX), hi = Math.min(n, b + CTX), r = await piece(y48.subarray(lo, hi));
      out.set(r.subarray(a - lo, a - lo + (b - a)), a); done = b; if (onProgress) onProgress(done / n); await new Promise(res => setTimeout(res, 0));
    }
    let y = sr === SR ? out : resample(out, SR, sr); if (y.length !== x.length) { const z = new Float32Array(x.length); z.set(y.subarray(0, x.length)); y = z; }
    if (s < 1) for (let i = 0; i < y.length; i++) y[i] = s * y[i] + (1 - s) * x[i];
    return y;
  }
  return {load, enhance, ready: () => !!sess, _use: s => { sess = s; }, _internals: {stft, istft, features, erbWidths, dft}};
})();
