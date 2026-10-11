/* VocalForge free tools: live noise-cancelling mic pipeline (browser only, nothing uploaded).
   mic -> noise suppression (learns your room) -> optional voice polish -> chosen output device (e.g. a virtual cable for OBS/Discord/Zoom) + recorder. */
(function (root) {
  'use strict';

  var TAP = [
    'class CleanTap extends AudioWorkletProcessor {',
    '  constructor(){ super(); this.on = false; this.port.onmessage = e => { this.on = e.data.on; }; }',
    '  process(inputs){ const i = inputs[0] && inputs[0][0]; if (this.on && i) this.port.postMessage(i.slice(0)); return true; }',
    '}',
    "registerProcessor('clean-tap', CleanTap);"
  ].join('\n');

  function wav16(x, sr) {
    var n = x.length, b = new ArrayBuffer(44 + n * 2), v = new DataView(b);
    function w(o, s) { for (var i = 0; i < s.length; i++) v.setUint8(o + i, s.charCodeAt(i)); }
    w(0, 'RIFF'); v.setUint32(4, 36 + n * 2, true); w(8, 'WAVE'); w(12, 'fmt '); v.setUint32(16, 16, true); v.setUint16(20, 1, true);
    v.setUint16(22, 1, true); v.setUint32(24, sr, true); v.setUint32(28, sr * 2, true); v.setUint16(32, 2, true); v.setUint16(34, 16, true);
    w(36, 'data'); v.setUint32(40, n * 2, true);
    for (var i = 0, o = 44; i < n; i++, o += 2) { var s = Math.max(-1, Math.min(1, x[i])); v.setInt16(o, s < 0 ? s * 32768 : s * 32767, true); }
    return new Blob([b], { type: 'audio/wav' });
  }
  function wav16n(chs, sr) {
    var nch = chs.length, n = chs[0].length, b = new ArrayBuffer(44 + n * nch * 2), v = new DataView(b);
    function w(o, s) { for (var i = 0; i < s.length; i++) v.setUint8(o + i, s.charCodeAt(i)); }
    w(0, 'RIFF'); v.setUint32(4, 36 + n * nch * 2, true); w(8, 'WAVE'); w(12, 'fmt '); v.setUint32(16, 16, true); v.setUint16(20, 1, true);
    v.setUint16(22, nch, true); v.setUint32(24, sr, true); v.setUint32(28, sr * nch * 2, true); v.setUint16(32, nch * 2, true); v.setUint16(34, 16, true);
    w(36, 'data'); v.setUint32(40, n * nch * 2, true);
    for (var i = 0, o = 44; i < n; i++) for (var c = 0; c < nch; c++, o += 2) { var s = Math.max(-1, Math.min(1, chs[c][i])); v.setInt16(o, s < 0 ? s * 32768 : s * 32767, true); }
    return new Blob([b], { type: 'audio/wav' });
  }
  function join(chunks) { var n = 0, i; for (i = 0; i < chunks.length; i++) n += chunks[i].length; var o = new Float32Array(n), p = 0; for (i = 0; i < chunks.length; i++) { o.set(chunks[i], p); p += chunks[i].length; } return o; }
  function biq(c, type, f, q, gain) { var n = c.createBiquadFilter(); n.type = type; n.frequency.value = f; if (q != null) n.Q.value = q; if (gain != null) n.gain.value = gain; return n; }

  function Clean() {
    this.ctx = null; this.stream = null; this.recording = false; this.cchunks = []; this.rchunks = [];
    this.onMeter = function () {}; this.onLearned = function () {}; this.onPitch = function () {}; this.polishOn = false; this.profile = null; this.tuneOn = false;
  }
  Clean.prototype.devices = async function () {
    var all = await navigator.mediaDevices.enumerateDevices();
    return { inputs: all.filter(function (d) { return d.kind === 'audioinput'; }), outputs: all.filter(function (d) { return d.kind === 'audiooutput'; }) };
  };
  // opts.deviceId: chosen microphone. opts.source(ctx): test hook supplying an AudioNode instead of the microphone.
  Clean.prototype.open = async function (opts) {
    opts = opts || {};
    var AC = root.AudioContext || root.webkitAudioContext, self = this;
    this.ctx = new AC({ latencyHint: 'interactive' });
    var c = this.ctx;
    await c.audioWorklet.addModule(URL.createObjectURL(new Blob([VFDenoise.workletSource() + '\n' + TAP + '\n' + VFLive.WORKLETS], { type: 'application/javascript' })));
    var input;
    if (opts.source) input = opts.source(c);
    else {
      var audio = { echoCancellation: false, noiseSuppression: false, autoGainControl: false, channelCount: 1 };
      if (opts.deviceId) audio.deviceId = { exact: opts.deviceId };
      this.stream = await navigator.mediaDevices.getUserMedia({ audio: audio });
      input = c.createMediaStreamSource(this.stream);
    }
    this.dn = new AudioWorkletNode(c, 'vf-denoise', { outputChannelCount: [1] });
    this.dn.port.onmessage = function (e) {
      var m = e.data;
      if (m.learned) { self.profile = m.profile; self.onLearned(m); } else self.onMeter(m);
    };
    input.connect(this.dn);
    // optional autotune (the same shifter as the VocalForge live monitor); off = straight through
    this.tune = new AudioWorkletNode(c, 'live-tune', { outputChannelCount: [1] });
    this.tune.port.onmessage = function (e) { self.onPitch(e.data); };
    this.tuned = c.createGain(); this.dry = c.createGain(); this.pre = c.createGain();
    this.dn.connect(this.tune); this.tune.connect(this.tuned); this.dn.connect(this.dry); this.tuned.connect(this.pre); this.dry.connect(this.pre);
    this.tuned.gain.value = 0; this.dry.gain.value = 1;
    // voice polish (optional): high-pass, a little presence, gentle compression
    this.hp = biq(c, 'highpass', 20, 0.7); this.pres = biq(c, 'peaking', 3500, 0.8, 0); this.comp = c.createDynamicsCompressor();
    this.comp.threshold.value = -26; this.comp.ratio.value = 1; this.comp.attack.value = 0.006; this.comp.release.value = 0.16; this.comp.knee.value = 12;
    this.pre.connect(this.hp); this.hp.connect(this.pres); this.pres.connect(this.comp);
    // effects: reverb, echo, doubler (each a send added to the dry voice)
    this.fx = c.createGain(); this.comp.connect(this.fx);
    var conv = c.createConvolver(); conv.normalize = false; conv.buffer = VFLive.makeIR(c, 0.9);
    this.revSend = c.createGain(); this.revSend.gain.value = 0; this.comp.connect(this.revSend); this.revSend.connect(biq(c, 'highpass', 250, 0.7)).connect(conv).connect(this.fx);
    this.echoSend = c.createGain(); this.echoSend.gain.value = 0; this.echoDel = c.createDelay(1.5); this.echoDel.delayTime.value = 0.28;
    var fb = c.createGain(), lp = biq(c, 'lowpass', 3200, 0.7); fb.gain.value = 0.38;
    this.comp.connect(this.echoSend); this.echoSend.connect(this.echoDel); this.echoDel.connect(lp); lp.connect(fb); fb.connect(this.echoDel); lp.connect(this.fx);
    this.chorusSend = c.createGain(); this.chorusSend.gain.value = 0;
    [[0.017, 0.31, 0.0022], [0.026, 0.47, 0.0030]].forEach(function (cfg) {
      var d = c.createDelay(0.1); d.delayTime.value = cfg[0]; var lfo = c.createOscillator(); lfo.frequency.value = cfg[1]; var depth = c.createGain(); depth.gain.value = cfg[2];
      lfo.connect(depth).connect(d.delayTime); lfo.start(); self.comp.connect(self.chorusSend); self.chorusSend.connect(d); d.connect(self.fx);
    });
    this.out = c.createGain(); this.fx.connect(this.out);
    // output to a chosen device through a media element; monitor through the default output
    this.dest = c.createMediaStreamDestination(); this.out.connect(this.dest);
    this.el = new Audio(); this.el.srcObject = this.dest.stream; this.el.muted = true; this.el.autoplay = true; this.el.play().catch(function () {});
    this.mon = c.createGain(); this.mon.gain.value = 0; this.out.connect(this.mon); this.mon.connect(c.destination);
    // recorder taps: cleaned output and the untouched mic
    var silent = c.createGain(); silent.gain.value = 0; silent.connect(c.destination);
    this.cTap = new AudioWorkletNode(c, 'clean-tap'); this.out.connect(this.cTap); this.cTap.connect(silent);
    this.rTap = new AudioWorkletNode(c, 'clean-tap'); input.connect(this.rTap); this.rTap.connect(silent);
    this.cTap.port.onmessage = function (e) { if (self.recording) self.cchunks.push(e.data); };
    this.rTap.port.onmessage = function (e) { if (self.recording) self.rchunks.push(e.data); };
    await c.resume();
  };
  Clean.prototype.learn = function (seconds) { this.dn.port.postMessage({ cmd: 'learn', seconds: seconds || 3 }); };
  Clean.prototype.clearProfile = function () { this.profile = null; this.dn.port.postMessage({ cmd: 'clear' }); };
  Clean.prototype.setParams = function (p) { this.dn.port.postMessage({ cmd: 'params', p: p }); };
  Clean.prototype.setBypass = function (on) { this.setParams({ bypass: !!on }); };
  Clean.prototype.setPolish = function (on) {
    this.polishOn = !!on; var t = this.ctx.currentTime;
    this.hp.frequency.setTargetAtTime(on ? 85 : 20, t, 0.02); this.pres.gain.setTargetAtTime(on ? 2.5 : 0, t, 0.02); this.comp.ratio.setTargetAtTime(on ? 2.5 : 1, t, 0.02);
    this.out.gain.setTargetAtTime(on ? 1.25 : 1, t, 0.02);
  };
  Clean.prototype.setAutotune = function (on) { this.tuneOn = !!on; var t = this.ctx.currentTime; this.tuned.gain.setTargetAtTime(on ? 1 : 0, t, 0.01); this.dry.gain.setTargetAtTime(on ? 0 : 1, t, 0.01); };
  Clean.prototype.setKey = function (tonic, scale) { var SC = VFLive.SCALES; this.tune.port.postMessage({ tonic: tonic, scale: SC[scale] === undefined ? SC.major : SC[scale] }); };
  Clean.prototype.setTune = function (amount, speed) { this.tune.parameters.get('amount').value = amount; this.tune.parameters.get('speed').value = speed; };
  Clean.prototype.setReverb = function (v) { this.revSend.gain.setTargetAtTime(v * 0.9, this.ctx.currentTime, 0.02); };
  Clean.prototype.setEcho = function (v, ms) { this.echoSend.gain.setTargetAtTime(v * 0.8, this.ctx.currentTime, 0.02); if (ms) this.echoDel.delayTime.setTargetAtTime(ms / 1000, this.ctx.currentTime, 0.05); };
  Clean.prototype.setChorus = function (v) { this.chorusSend.gain.setTargetAtTime(v * 0.7, this.ctx.currentTime, 0.02); };
  Clean.prototype.setMonitor = function (on) { if (this.mon) this.mon.gain.setTargetAtTime(on ? 1 : 0, this.ctx.currentTime, 0.02); };
  // deviceId: '' = silent (just meters/recording), 'default' = default output, or a device id
  Clean.prototype.setOutput = async function (deviceId) {
    if (!this.el) return false;
    if (!deviceId) { this.el.muted = true; return true; }
    if (deviceId !== 'default' && typeof this.el.setSinkId === 'function') { try { await this.el.setSinkId(deviceId); } catch (e) { return false; } }
    else if (deviceId !== 'default') return false;
    this.el.muted = false; try { await this.el.play(); } catch (e) {} return true;
  };
  Clean.prototype.canChooseOutput = function () { return typeof Audio !== 'undefined' && typeof Audio.prototype.setSinkId === 'function'; };
  Clean.prototype.startRecording = function () { this.cchunks = []; this.rchunks = []; this.recording = true; this.cTap.port.postMessage({ on: true }); this.rTap.port.postMessage({ on: true }); };
  Clean.prototype.stopRecording = function () {
    this.recording = false; this.cTap.port.postMessage({ on: false }); this.rTap.port.postMessage({ on: false });
    var sr = this.ctx.sampleRate, c = join(this.cchunks), r = join(this.rchunks);
    // the cleaned signal runs about 11 ms behind the raw one: trim so both files start together
    var lag = 512; if (c.length > lag) c = c.subarray(lag);
    return { seconds: c.length / sr, clean: c.length ? wav16(c, sr) : null, raw: r.length ? wav16(r, sr) : null };
  };
  Clean.prototype.latencyMs = function () { var c = this.ctx; return c ? Math.round(512 / c.sampleRate * 1000 + ((c.baseLatency || 0.01) + (c.outputLatency || 0.02)) * 1000) : 0; };
  Clean.prototype.close = function () { if (this.stream) this.stream.getTracks().forEach(function (t) { t.stop(); }); if (this.el) { this.el.pause(); this.el.srcObject = null; } if (this.ctx) { try { this.ctx.close(); } catch (e) {} } this.ctx = null; this.stream = null; this.recording = false; };

  var api = { Clean: Clean, wav16: wav16, wav16n: wav16n };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.VFClean = api;
})(typeof window !== 'undefined' ? window : globalThis);
