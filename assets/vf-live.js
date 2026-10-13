/* Tunedzy free tools: live autotune + karaoke engine. Runs entirely in the visitor's browser (Web Audio + AudioWorklet).
   Mic -> pitch detection (YIN) -> delay-line pitch shifter -> light studio tone + reverb -> headphones, with recording.
   The same shifter as the Tunedzy desktop app's live monitor. Nothing is uploaded. */
(function (root) {
  'use strict';

  var WORKLETS = [
    '// live autotune: YIN pitch detection (decimated) + two-head delay-line pitch shifter',
    'class LiveTune extends AudioWorkletProcessor {',
    "  static get parameterDescriptors(){ return [{name:'amount', defaultValue:1, minValue:0, maxValue:1}, {name:'speed', defaultValue:.02, minValue:0, maxValue:.3}]; }",
    '  constructor(){ super();',
    '    this.scale = null; this.tonic = 0; this.report = 0;',
    '    this.port.onmessage = e => { this.scale = e.data.scale; this.tonic = e.data.tonic || 0; };',
    '    this.dec = 4; this.N = 512; this.ring = new Float32Array(this.N); this.ri = 0; this.acc = 0; this.accN = 0;',
    '    this.x = new Float32Array(this.N); this.d = new Float32Array(this.N / 2);',
    '    this.ratio = 1; this.target = 1; this.hop = 0;',
    '    this.L = 8192; this.dl = new Float32Array(this.L); this.w = 0; this.win = Math.round(.03 * sampleRate); this.ph = 0;',
    '  }',
    '  detect(){',
    '    const N = this.N, W = N / 2, fs = sampleRate / this.dec, x = this.x, d = this.d;',
    '    let en = 0; for (let i = 0; i < N; i++){ x[i] = this.ring[(this.ri + i) % N]; en += x[i] * x[i]; }',
    '    if (en / N < 2e-6) return 0;',
    '    const lo = Math.floor(fs / 1000), hi = Math.min(W - 2, Math.floor(fs / 70)); let run = 0; d[0] = 1;',
    '    for (let t = 1; t <= hi; t++){ let s = 0; for (let i = 0; i < W; i++){ const v = x[i] - x[i + t]; s += v * v; } run += s; d[t] = run ? s * t / run : 1; }',
    '    for (let t = Math.max(2, lo); t <= hi; t++){',
    '      if (d[t] < .15){ while (t + 1 <= hi && d[t + 1] < d[t]) t++;',
    '        const a = d[t - 1], b = d[t], c = d[t + 1], den = a - 2 * b + c; return fs / (t + (den ? (a - c) / (2 * den) : 0)); }',
    '    }',
    '    return 0;',
    '  }',
    '  snap(f){',
    '    const m = 69 + 12 * Math.log2(f / 440); let best = Math.round(m), bd = 99;',
    '    if (this.scale) for (let n = Math.floor(m) - 2; n <= Math.ceil(m) + 2; n++){',
    '      if (this.scale.includes(((n - this.tonic) % 12 + 12) % 12) && Math.abs(n - m) < bd){ bd = Math.abs(n - m); best = n; } }',
    '    return 440 * Math.pow(2, (best - 69) / 12);',
    '  }',
    '  process(inputs, outputs, params){',
    '    const inp = inputs[0] && inputs[0][0], out = outputs[0][0];',
    '    if (!inp){ out.fill(0); return true; }',
    '    for (let i = 0; i < inp.length; i++){ this.acc += inp[i]; if (++this.accN === this.dec){ this.ring[this.ri] = this.acc / this.dec; this.ri = (this.ri + 1) % this.N; this.acc = 0; this.accN = 0; } }',
    '    if ((this.hop += inp.length) >= 256){ this.hop = 0; const f = this.detect(); this.target = f > 70 && f < 1000 ? this.snap(f) / f : 1;',
    '      if ((this.report++ & 1) === 0) this.port.postMessage({f: f, t: f > 0 ? f * this.target : 0}); }',
    '    const sp = params.speed[0], k = sp <= .001 ? 1 : 1 - Math.exp(-inp.length / sampleRate / sp);',
    '    this.ratio += k * ((1 + (this.target - 1) * params.amount[0]) - this.ratio);',
    '    const L = this.L, W = this.win;',
    '    for (let i = 0; i < inp.length; i++){',
    '      this.dl[this.w] = inp[i];',
    '      this.ph += 1 - this.ratio; if (this.ph >= W) this.ph -= W; if (this.ph < 0) this.ph += W;',
    '      let y = 0;',
    '      for (let h = 0; h < 2; h++){',
    '        let dly = this.ph + h * W / 2; if (dly >= W) dly -= W;',
    '        const g = Math.sin(Math.PI * dly / W); let r = this.w - dly - 2; while (r < 0) r += L;',
    '        const r0 = Math.floor(r), fr = r - r0, s0 = this.dl[r0 % L], s1 = this.dl[(r0 + 1) % L];',
    '        y += g * g * (s0 + (s1 - s0) * fr);',
    '      }',
    '      out[i] = y; this.w = (this.w + 1) % L;',
    '    }',
    '    return true;',
    '  }',
    '}',
    "registerProcessor('live-tune', LiveTune);",
    '// recorder tap: hands raw blocks (all input channels) to the page while recording',
    'class RecTap extends AudioWorkletProcessor {',
    '  constructor(){ super(); this.on = false; this.port.onmessage = e => { this.on = e.data.on; }; }',
    '  process(inputs){ const i = inputs[0]; if (this.on && i && i.length){ this.port.postMessage(i.map(c => c.slice(0))); } return true; }',
    '}',
    "registerProcessor('rec-tap', RecTap);"
  ].join('\n');

  function biq(c, type, f, q, gain) { var n = c.createBiquadFilter(); n.type = type; n.frequency.value = f; if (q != null) n.Q.value = q; if (gain != null) n.gain.value = gain; return n; }
  function makeIR(c, sec) {
    var n = Math.floor(c.sampleRate * sec), b = c.createBuffer(2, n, c.sampleRate);
    for (var ch = 0; ch < 2; ch++) {
      var d = b.getChannelData(ch), e = 0, i;
      for (i = 0; i < n; i++) { d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / n, 2.6); e += d[i] * d[i]; }
      var k = 1 / Math.sqrt(e || 1); for (i = 0; i < n; i++) d[i] *= k;               // unit energy: reverb return stays at the send level
    }
    return b;
  }
  function wav16(chans, sr) {
    var nch = chans.length, n = chans[0].length, b = new ArrayBuffer(44 + n * nch * 2), v = new DataView(b);
    function w(o, s) { for (var i = 0; i < s.length; i++) v.setUint8(o + i, s.charCodeAt(i)); }
    w(0, 'RIFF'); v.setUint32(4, 36 + n * nch * 2, true); w(8, 'WAVE'); w(12, 'fmt '); v.setUint32(16, 16, true); v.setUint16(20, 1, true);
    v.setUint16(22, nch, true); v.setUint32(24, sr, true); v.setUint32(28, sr * nch * 2, true); v.setUint16(32, nch * 2, true); v.setUint16(34, 16, true);
    w(36, 'data'); v.setUint32(40, n * nch * 2, true);
    var o = 44;
    for (var i = 0; i < n; i++) for (var c = 0; c < nch; c++) { var s = Math.max(-1, Math.min(1, chans[c][i])); v.setInt16(o, s < 0 ? s * 32768 : s * 32767, true); o += 2; }
    return new Blob([b], { type: 'audio/wav' });
  }
  function join(chunks, ch) { var n = 0, i; for (i = 0; i < chunks.length; i++) n += chunks[i][ch] ? chunks[i][ch].length : 0; var o = new Float32Array(n), p = 0; for (i = 0; i < chunks.length; i++) { var a = chunks[i][ch]; if (a) { o.set(a, p); p += a.length; } } return o; }

  var SCALES = { major: [0, 2, 4, 5, 7, 9, 11], minor: [0, 2, 3, 5, 7, 8, 10], chromatic: null };

  function Live() {
    this.ctx = null; this.stream = null; this.recording = false; this.vchunks = []; this.mchunks = [];
    this.tuneOn = true; this.reverb = 0.18; this.backing = null; this.src = null; this.startedAt = 0; this.offset = 0; this.playing = false;
    this.onPitch = function () {}; this.nudgeMs = 0;
  }
  // opts.mic (default true) asks for the microphone; opts.source(ctx) is a test hook that supplies an AudioNode instead.
  Live.prototype.open = async function (opts) {
    opts = opts || {};
    if (this.ctx) return;
    var AC = root.AudioContext || root.webkitAudioContext;
    this.ctx = new AC({ latencyHint: 'interactive' });
    var c = this.ctx;
    await c.audioWorklet.addModule(URL.createObjectURL(new Blob([WORKLETS], { type: 'application/javascript' })));
    var input;
    if (opts.source) input = opts.source(c);
    else {
      this.stream = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: false, noiseSuppression: false, autoGainControl: false, channelCount: 1 } });
      input = c.createMediaStreamSource(this.stream);
    }
    var self = this;
    this.meter = c.createAnalyser(); this.meter.fftSize = 1024; input.connect(this.meter);
    var hp0 = biq(c, 'highpass', 80, 0.7); input.connect(hp0);
    this.tune = new AudioWorkletNode(c, 'live-tune', { outputChannelCount: [1] });
    this.tune.port.onmessage = function (e) { self.onPitch(e.data); };
    this.tuned = c.createGain(); this.dry = c.createGain();
    hp0.connect(this.tune); this.tune.connect(this.tuned); hp0.connect(this.dry);
    var pres = biq(c, 'peaking', 5500, 0.7, 2), air = biq(c, 'highshelf', 11000, null, 3);
    var comp = c.createDynamicsCompressor(); comp.threshold.value = -22; comp.ratio.value = 3; comp.attack.value = 0.005; comp.release.value = 0.1;
    this.tuned.connect(pres); this.dry.connect(pres); pres.connect(air).connect(comp);
    this.voice = c.createGain(); comp.connect(this.voice);                         // dry-tone voice
    var conv = c.createConvolver(); conv.normalize = false; conv.buffer = makeIR(c, 0.5);
    this.revSend = c.createGain(); this.revRet = c.createGain(); this.revRet.gain.value = 1;
    comp.connect(this.revSend); this.revSend.connect(biq(c, 'highpass', 300, 0.7)).connect(conv).connect(this.revRet);
    var vb = c.createGain(); this.voice.connect(vb); this.revRet.connect(vb);
    this.voiceBus = c.createDynamicsCompressor(); this.voiceBus.threshold.value = -3; this.voiceBus.knee.value = 0; this.voiceBus.ratio.value = 20; this.voiceBus.attack.value = 0.002; this.voiceBus.release.value = 0.12;
    vb.connect(this.voiceBus);                                                       // safety limiter: no clipped recordings
    // master -> speakers
    this.master = c.createGain(); this.master.channelCount = 2; this.master.channelCountMode = 'explicit';
    this.voiceBus.connect(this.master); this.master.connect(c.destination);
    // backing track path (optional)
    this.backGain = c.createGain(); this.backGain.gain.value = 0.8;
    this.backGain.channelCount = 2; this.backGain.channelCountMode = 'explicit';
    this.direct = c.createGain(); this.reduced = c.createGain(); this.reduced.gain.value = 0;
    this.backIn = c.createGain(); this.backIn.channelCount = 2; this.backIn.channelCountMode = 'explicit';
    this.backIn.connect(this.direct).connect(this.backGain);
    var sp = c.createChannelSplitter(2), sideSum = c.createGain(), bassSum = c.createGain(), mg = c.createChannelMerger(2);
    var lS = c.createGain(), rS = c.createGain(), lB = c.createGain(), rB = c.createGain();
    lS.gain.value = 0.5; rS.gain.value = -0.5; lB.gain.value = 0.5; rB.gain.value = 0.5;
    this.backIn.connect(sp); sp.connect(lS, 0); sp.connect(rS, 1); sp.connect(lB, 0); sp.connect(rB, 1);
    lS.connect(sideSum); rS.connect(sideSum); lB.connect(bassSum); rB.connect(bassSum);
    var sideHp = biq(c, 'highpass', 140, 0.7), bassLp = biq(c, 'lowpass', 140, 0.7);
    sideSum.connect(sideHp); bassSum.connect(bassLp);
    sideHp.connect(mg, 0, 0); sideHp.connect(mg, 0, 1); bassLp.connect(mg, 0, 0); bassLp.connect(mg, 0, 1);
    mg.connect(this.reduced).connect(this.backGain);
    this.backGain.connect(this.master);
    // recorder taps (kept alive through a silent gain)
    var silent = c.createGain(); silent.gain.value = 0; silent.connect(c.destination);
    this.voiceTap = new AudioWorkletNode(c, 'rec-tap', { numberOfInputs: 1, numberOfOutputs: 1, channelCount: 1, channelCountMode: 'explicit' });
    this.voiceBus.connect(this.voiceTap); this.voiceTap.connect(silent);
    this.voiceTap.port.onmessage = function (e) { if (self.recording) self.vchunks.push(e.data); };
    this.mixRec = c.createGain(); this.mixRec.channelCount = 2; this.mixRec.channelCountMode = 'explicit';
    this.voiceBus.connect(this.mixRec);
    this.backDelay = c.createDelay(1.0); this.backGain.connect(this.backDelay); this.backDelay.connect(this.mixRec);
    this.mixTap = new AudioWorkletNode(c, 'rec-tap', { numberOfInputs: 1, numberOfOutputs: 1, channelCount: 2, channelCountMode: 'explicit' });
    var mixLim = c.createDynamicsCompressor(); mixLim.threshold.value = -3; mixLim.knee.value = 0; mixLim.ratio.value = 20; mixLim.attack.value = 0.002; mixLim.release.value = 0.12;
    this.mixRec.connect(mixLim); mixLim.connect(this.mixTap); this.mixTap.connect(silent);
    this.mixTap.port.onmessage = function (e) { if (self.recording) self.mchunks.push(e.data); };
    this.setKey(0, 'major'); this.setTune(0.8, 0.05); this.setReverb(this.reverb); this.setNudge(0); this.apply();
    await c.resume();
  };
  Live.prototype.estLatencyMs = function () { var c = this.ctx; if (!c) return 0; return Math.round(((c.baseLatency || 0.01) + (c.outputLatency || 0.02) + 0.015) * 1000); };
  Live.prototype.apply = function () { this.tuned.gain.value = this.tuneOn ? 1 : 0; this.dry.gain.value = this.tuneOn ? 0 : 1; };
  Live.prototype.setKey = function (tonic, scale) { if (!this.tune) return; this.tune.port.postMessage({ tonic: tonic, scale: SCALES[scale] === undefined ? SCALES.major : SCALES[scale] }); };
  Live.prototype.setTune = function (amount, speed) { if (!this.tune) return; this.tune.parameters.get('amount').value = amount; this.tune.parameters.get('speed').value = speed; };
  Live.prototype.setTuneOn = function (on) { this.tuneOn = !!on; if (this.ctx) this.apply(); };
  Live.prototype.setReverb = function (v) { this.reverb = v; if (this.revSend) this.revSend.gain.value = v; };
  Live.prototype.setVoiceGain = function (v) { if (this.voice) this.voice.gain.value = v; };
  Live.prototype.setBackGain = function (v) { if (this.backGain) this.backGain.gain.value = v; };
  Live.prototype.setReduce = function (on) { if (!this.ctx) return; this.direct.gain.value = on ? 0 : 1; this.reduced.gain.value = on ? 1 : 0; };
  Live.prototype.setNudge = function (ms) { this.nudgeMs = ms; if (this.backDelay) this.backDelay.delayTime.value = Math.max(0, Math.min(0.9, (this.estLatencyMs() + ms) / 1000)); };
  Live.prototype.level = function () { if (!this.meter) return 0; var a = new Float32Array(this.meter.fftSize), m = 0; this.meter.getFloatTimeDomainData(a); for (var i = 0; i < a.length; i++) m = Math.max(m, Math.abs(a[i])); return m; };

  // ---- backing track
  Live.prototype.loadBacking = async function (arrayBuffer) {
    var c = this.ctx; this.stopBacking(); this.offset = 0;
    this.backing = await c.decodeAudioData(arrayBuffer); return this.backing;
  };
  Live.prototype.setBacking = function (buffer) { this.stopBacking(); this.offset = 0; this.backing = buffer; };
  Live.prototype.position = function () { if (!this.backing) return 0; var p = this.playing ? this.offset + (this.ctx.currentTime - this.startedAt) : this.offset; return Math.min(p, this.backing.duration); };
  Live.prototype.play = function (from) {
    if (!this.backing) return; var c = this.ctx; this.stopBacking();
    if (typeof from === 'number') this.offset = Math.max(0, Math.min(from, this.backing.duration - 0.05));
    var s = c.createBufferSource(); s.buffer = this.backing; s.connect(this.backIn);
    var self = this; s.onended = function () { if (self.src === s && self.playing) { self.playing = false; self.offset = 0; self.src = null; if (self.onEnd) self.onEnd(); } };
    s.start(0, this.offset); this.src = s; this.startedAt = c.currentTime; this.playing = true;
  };
  Live.prototype.pause = function () { if (!this.playing) return; this.offset = this.position(); this.stopBacking(true); };
  Live.prototype.stopBacking = function (keepOffset) { if (this.src) { var s = this.src; this.src = null; this.playing = false; s.onended = null; try { s.stop(); } catch (e) {} } this.playing = false; if (!keepOffset) { /* offset kept by caller */ } };

  // ---- recording
  Live.prototype.startRecording = function () { this.vchunks = []; this.mchunks = []; this.recording = true; this.voiceTap.port.postMessage({ on: true }); this.mixTap.port.postMessage({ on: true }); this.recStart = this.ctx.currentTime; };
  Live.prototype.stopRecording = function () {
    this.recording = false; this.voiceTap.port.postMessage({ on: false }); this.mixTap.port.postMessage({ on: false });
    var sr = this.ctx.sampleRate, v = join(this.vchunks, 0), out = { seconds: v.length / sr, voice: v.length ? wav16([v], sr) : null, mix: null };
    if (this.mchunks.length) { var l = join(this.mchunks, 0), r = join(this.mchunks, 1); if (!r.length) r = l; out.mix = wav16([l, r], sr); }
    return out;
  };
  Live.prototype.close = function () { if (this.stream) this.stream.getTracks().forEach(function (t) { t.stop(); }); this.stopBacking(); if (this.ctx) { try { this.ctx.close(); } catch (e) {} } this.ctx = null; this.stream = null; this.tune = null; this.meter = null; this.recording = false; this.playing = false; };

  var NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
  function noteName(f) { var m = 69 + 12 * Math.log2(f / 440), r = Math.round(m); return { name: NOTES[((r % 12) + 12) % 12] + (Math.floor(r / 12) - 1), midi: m, cents: Math.round((m - r) * 100) }; }
  var api = { Live: Live, SCALES: SCALES, noteName: noteName, NOTES: NOTES, wav16: wav16, WORKLETS: WORKLETS, makeIR: makeIR };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.VFLive = api;
})(typeof window !== 'undefined' ? window : globalThis);
