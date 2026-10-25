/* Tunedzy neural noise suppressor: Xiph RNNoise (a small recurrent network trained on speech and noise) compiled to WebAssembly.
 * It works on 10 ms frames at 48 kHz. Other sample rates are converted in and out with linear interpolation.
 * Parameters:  amount 0..1  (0 = untouched voice, 1 = fully cleaned; the dry path is delayed to match, so mixing is phase-aligned)
 * Port out:    {vad}        voice-activity estimate (0..1), about 10 times a second
 * Latency:     about 29 ms at 48 kHz (the network's own two frames plus render-quantum alignment) */
import './rnnoise-polyfill.js';
import createRNNWasmModuleSync from './rnnoise-sync.js';

const FRAME = 480, RATE = 48000, SCALE = 32768;

class Resampler {                       // streaming linear-interpolation converter; ratio = input samples per output sample
  constructor(ratio) { this.r = ratio; this.phase = 0; this.prev = 0; }
  push(x, n, emit) {
    const r = this.r;
    for (let i = 0; i < n; i++) {
      const v = x[i];
      while (this.phase < 1) { emit(this.prev + (v - this.prev) * this.phase); this.phase += r; }
      this.phase -= 1; this.prev = v;
    }
  }
}

class VFRnnoise extends AudioWorkletProcessor {
  static get parameterDescriptors() { return [{ name: 'amount', defaultValue: 1, minValue: 0, maxValue: 1, automationRate: 'k-rate' }]; }
  constructor() {
    super();
    this.native = Math.abs(sampleRate - RATE) < 1;
    this.m = createRNNWasmModuleSync();
    this.ptr = this.m._malloc(FRAME * 4); this.i32 = this.ptr >> 2;
    this.st = this.m._rnnoise_create();
    this.up = this.native ? null : new Resampler(sampleRate / RATE);
    this.down = this.native ? null : new Resampler(RATE / sampleRate);
    this.acc = new Float32Array(FRAME); this.na = 0;                     // 48 kHz frame being filled
    this.d1 = new Float32Array(FRAME); this.d2 = new Float32Array(FRAME);   // dry history: the network's output lags its input by two frames
    this.fifo = new Float32Array(8192); this.fr = 0; this.fw = 0; this.fn = 0;
    this.prime = this.native ? 448 : Math.ceil(FRAME * sampleRate / RATE) + 96;   // output delay so the FIFO never runs dry (448 = worst-case 128-quantum alignment)
    this.one = new Float32Array(1); this.putFn = y => this._put(y);
    for (let i = 0; i < this.prime; i++) this._put(0);
    this.vad = 0; this.t = 0; this.amt = 1;
  }
  _put(v) { this.fifo[this.fw] = v; this.fw = (this.fw + 1) & 8191; this.fn++; }
  _frame() {
    const m = this.m, h = m.HEAPF32, a = this.acc, o = this.i32, amt = this.amt, d = this.d2;
    if (amt < 0.001) {                                                    // off: the voice passes with the same delay, RNNoise state stays cold
      for (let i = 0; i < FRAME; i++) this._emit48(d[i]);
    } else {
      for (let i = 0; i < FRAME; i++) h[o + i] = a[i] * SCALE;
      this.vad = m._rnnoise_process_frame(this.st, this.ptr, this.ptr);
      // the cleaned frame that comes out belongs to the input of two frames ago, so that is the dry signal it is mixed with
      for (let i = 0; i < FRAME; i++) this._emit48(amt * (h[o + i] / SCALE) + (1 - amt) * d[i]);
    }
    this.d2.set(this.d1); this.d1.set(a);
  }
  _emit48(v) {
    if (this.native) this._put(v); else { this.one[0] = v; this.down.push(this.one, 1, this.putFn); }
  }
  process(inputs, outputs, params) {
    const inp = inputs[0] && inputs[0][0], out = outputs[0] && outputs[0][0];
    if (!out) return true;
    this.amt = params.amount[0];
    const n = out.length;
    if (!inp) { out.fill(0); }
    else {
      const push = v => { this.acc[this.na++] = v; if (this.na === FRAME) { this._frame(); this.na = 0; } };
      if (this.native) { for (let i = 0; i < n; i++) push(inp[i]); } else this.up.push(inp, n, push);
      for (let i = 0; i < n; i++) {
        if (this.fn > 0) { out[i] = this.fifo[this.fr]; this.fr = (this.fr + 1) & 8191; this.fn--; } else out[i] = 0;
      }
    }
    for (let c = 1; c < outputs[0].length; c++) outputs[0][c].set(out);
    this.t += n;
    if (this.t >= sampleRate / 10) { this.t = 0; this.port.postMessage({ vad: this.vad }); }
    return true;
  }
}
registerProcessor('vf-rnnoise', VFRnnoise);
