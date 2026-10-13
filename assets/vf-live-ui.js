/* Tunedzy free tools: live autotune + karaoke page glue. Nothing is uploaded; there is no network code here. */
(function () {
  'use strict';
  var root = document.getElementById('live');
  if (!root) return;
  var mode = root.getAttribute('data-mode') || 'tune', BASE = root.getAttribute('data-base') || '/tunedzy';
  var $ = function (s) { return root.querySelector(s); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var live = new VFLive.Live(); window.__vfLive = live;
  var NOTES = VFLive.NOTES;
  var state = { key: 0, scale: 'major', preset: 'pop', tuneOn: true, takes: 0, pitch: [], recTimer: null, recStart: 0 };

  function mmss(t) { t = Math.max(0, Math.floor(t)); return Math.floor(t / 60) + ':' + ('0' + (t % 60)).slice(-2); }
  function toast(msg, bad) { var t = $('#msg'); t.textContent = msg; t.className = 'livemsg' + (bad ? ' bad' : ''); t.hidden = !msg; }

  // ------------------------------------------------------------------ analysis (karaoke: set the key from the backing track)
  function analyse(buf) {
    return new Promise(function (resolve, reject) {
      var chs = []; for (var c = 0; c < Math.min(2, buf.numberOfChannels); c++) chs.push(new Float32Array(buf.getChannelData(c)));
      var w;
      try {
        var src = document.getElementById('vfcore').textContent + ';self.onmessage=function(e){try{var d=e.data;self.postMessage({res:VFCore.analyzeAll(d.chs,d.sr,{})})}catch(err){self.postMessage({err:String(err)})}}';
        w = new Worker(URL.createObjectURL(new Blob([src], { type: 'text/javascript' })));
      } catch (e) { try { resolve(VFCore.analyzeAll(chs, buf.sampleRate, {})); } catch (e2) { reject(e2); } return; }
      w.onmessage = function (m) { w.terminate(); if (m.data.res) resolve(m.data.res); else reject(new Error(m.data.err)); };
      w.onerror = function (e) { w.terminate(); reject(new Error(e.message || 'analysis failed')); };
      w.postMessage({ chs: chs, sr: buf.sampleRate }, chs.map(function (x) { return x.buffer; }));
    });
  }

  // ------------------------------------------------------------------ controls
  function applyKey() { live.setKey(state.key, state.scale); drawKeyLabel(); }
  function drawKeyLabel() { var k = $('#keylabel'); if (k) k.textContent = state.scale === 'chromatic' ? 'Every note (chromatic)' : NOTES[state.key] + ' ' + state.scale; }
  var PRESETS = { natural: { a: 0.55, s: 0.12 }, pop: { a: 0.8, s: 0.05 }, hard: { a: 1, s: 0 }, off: null };
  function setPreset(name) {
    state.preset = name; var p = PRESETS[name];
    root.querySelectorAll('[data-preset]').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-preset') === name); });
    if (!p) { state.tuneOn = false; live.setTuneOn(false); return; }
    state.tuneOn = true; live.setTuneOn(true);
    $('#amount').value = Math.round(p.a * 100); $('#speed').value = Math.round(p.s * 1000); applyTune();
  }
  function applyTune() { var a = $('#amount').value / 100, s = $('#speed').value / 1000; live.setTune(a, s); $('#amountv').textContent = $('#amount').value + '%'; $('#speedv').textContent = $('#speed').value === '0' ? 'instant' : $('#speed').value + ' ms'; }

  // ------------------------------------------------------------------ pitch picture
  var cv = $('#pcv'), g = cv.getContext('2d'), midiCenter = 60;
  live.onPitch = function (m) {
    var now = performance.now(); state.pitch.push({ t: now, f: m.f, g: m.t });
    while (state.pitch.length && now - state.pitch[0].t > 6000) state.pitch.shift();
    if (m.f > 0) { var n = VFLive.noteName(m.f); $('#note').textContent = n.name; $('#cents').textContent = (n.cents > 0 ? '+' : '') + n.cents + ' cents' + (state.tuneOn && m.t ? ' > ' + VFLive.noteName(m.t).name : ''); }
  };
  var drawing = false;
  function draw() {
    if (!live.ctx) { drawing = false; return; }
    var W = cv.width, H = cv.height, now = performance.now(); g.clearRect(0, 0, W, H);
    var mids = state.pitch.filter(function (p) { return p.f > 0; }).map(function (p) { return 69 + 12 * Math.log2(p.f / 440); });
    if (mids.length) { mids.sort(function (a, b) { return a - b; }); var med = mids[Math.floor(mids.length / 2)]; midiCenter += (med - midiCenter) * 0.05; }
    var lo = midiCenter - 9, hi = midiCenter + 9, y = function (m) { return H - (m - lo) / (hi - lo) * H; };
    var sc = VFLive.SCALES[state.scale];
    g.font = '11px system-ui'; g.textBaseline = 'middle';
    for (var n = Math.floor(lo); n <= Math.ceil(hi); n++) {
      var inScale = !sc || sc.indexOf(((n - state.key) % 12 + 12) % 12) >= 0; if (!inScale) continue;
      g.strokeStyle = (((n - state.key) % 12 + 12) % 12 === 0) ? 'rgba(255,179,71,.55)' : 'rgba(255,255,255,.12)'; g.lineWidth = 1;
      g.beginPath(); g.moveTo(34, y(n)); g.lineTo(W, y(n)); g.stroke(); g.fillStyle = 'rgba(255,255,255,.55)'; g.fillText(NOTES[((n % 12) + 12) % 12], 4, y(n));
    }
    function trace(key, color, w) {
      g.strokeStyle = color; g.lineWidth = w; g.beginPath(); var started = false;
      state.pitch.forEach(function (p) { var f = p[key]; if (!(f > 0)) { started = false; return; } var x = 40 + (W - 40) * (1 - (now - p.t) / 6000), yy = y(69 + 12 * Math.log2(f / 440)); if (!started) { g.moveTo(x, yy); started = true; } else g.lineTo(x, yy); });
      g.stroke();
    }
    trace('f', 'rgba(255,255,255,.55)', 2); if (state.tuneOn) trace('g', '#ff6a2b', 3);
    var l = live.level(); $('#lvl').style.width = Math.min(100, Math.round(l * 140)) + '%'; $('#lvl').className = l > 0.95 ? 'hot' : '';
    requestAnimationFrame(draw);
  }

  // ------------------------------------------------------------------ recording + takes
  function addTake(res) {
    state.takes++;
    var html = '<div class="take"><b>Take ' + state.takes + ' <small>' + mmss(res.seconds) + '</small></b>';
    function row(label, blob, name) { var url = URL.createObjectURL(blob); return '<div class="takerow"><span>' + label + '</span><audio controls preload="metadata" src="' + url + '"></audio><a class="btn small" download="' + name + '" href="' + url + '">Download WAV</a></div>'; }
    if (res.voice) html += row('Your voice (autotuned)', res.voice, 'tunedzy-take' + state.takes + '-voice.wav');
    if (res.mix && mode === 'karaoke' && backingBuf) html += row('Voice + backing track', res.mix, 'tunedzy-take' + state.takes + '-mix.wav');
    html += '<p class="small mute">Want it studio-clean? <a href="' + BASE + '#pricing">Tunedzy</a> cleans, tunes and masters a take like this in one pass.</p></div>';
    var box = $('#takes'); box.insertAdjacentHTML('afterbegin', html);
  }
  function timerOn() { state.recStart = performance.now(); state.recTimer = setInterval(function () { $('#timer').textContent = mmss((performance.now() - state.recStart) / 1000); }, 250); }
  async function record() {
    var btn = $('#rec');
    if (live.recording) { stopRec(); return; }
    btn.disabled = true;
    if (mode === 'karaoke' && live.backing) {
      for (var i = 3; i >= 1; i--) { $('#timer').textContent = 'Starting in ' + i; await new Promise(function (r) { setTimeout(r, 900); }); }
      live.play(0); $('#play').textContent = 'Pause';
    }
    live.startRecording(); btn.disabled = false; btn.textContent = 'Stop and save'; btn.classList.add('live'); timerOn(); root.classList.add('rec');
    if (mode === 'karaoke') startLyrics();
  }
  function stopRec() {
    var btn = $('#rec'); clearInterval(state.recTimer); var res = live.stopRecording();
    if (mode === 'karaoke') { live.pause(); $('#play').textContent = 'Play'; stopLyrics(); }
    btn.textContent = 'Record'; btn.classList.remove('live'); root.classList.remove('rec'); $('#timer').textContent = '0:00';
    if (res.voice) addTake(res); else toast('Nothing was recorded. Sing something first.', true);
  }

  // ------------------------------------------------------------------ karaoke bits
  var lyricTimer = null;
  function startLyrics() { stopLyrics(); var v = $('#lyrview'); if (!v || v.hidden) return; var sp = function () { return $('#lyrspeed').value / 10; }; v.scrollTop = 0; lyricTimer = setInterval(function () { v.scrollTop += sp() / 4; }, 250); }
  function stopLyrics() { clearInterval(lyricTimer); lyricTimer = null; }
  async function loadFile(file) {
    if (!file) return; var info = $('#backinfo'); info.hidden = false; info.innerHTML = 'Loading <b>' + esc(file.name) + '</b>...';
    try {
      var ab = await file.arrayBuffer(), AC = window.AudioContext || window.webkitAudioContext, tmp = new AC();
      var buf = await tmp.decodeAudioData(ab); try { tmp.close(); } catch (e) {}
      useBacking(buf, file.name);
    } catch (e) { info.innerHTML = 'That file could not be decoded. Try an MP3 or WAV.'; }
  }
  var backingBuf = null;
  async function useBacking(buf, name) {
    backingBuf = buf; var info = $('#backinfo'); info.hidden = false;
    info.innerHTML = '<b>' + esc(name) + '</b> &middot; ' + mmss(buf.duration) + ' &middot; finding its key...';
    $('#seek').max = Math.floor(buf.duration); $('#dur').textContent = mmss(buf.duration);
    if (live.ctx) live.setBacking(buf);
    try {
      var r = await analyse(buf);
      if (r.key) {
        state.key = r.key.tonic; state.scale = r.key.mode; $('#key').value = state.key; $('#scale').value = state.scale; if (live.ctx) applyKey(); else drawKeyLabel();
        info.innerHTML = '<b>' + esc(name) + '</b> &middot; ' + mmss(buf.duration) + ' &middot; key <b>' + esc(r.key.name) + '</b>' + (r.tempo ? ' &middot; ' + Math.round(r.tempo.bpm) + ' BPM' : '') + ' <span class="mute">(autotune set to this key; change it below if it sounds off)</span>';
      } else info.innerHTML = '<b>' + esc(name) + '</b> &middot; ' + mmss(buf.duration) + ' &middot; could not find a clear key, pick one below.';
    } catch (e) { info.innerHTML = '<b>' + esc(name) + '</b> &middot; ' + mmss(buf.duration) + ' &middot; loaded.'; }
    $('#transport').hidden = false;
  }
  var ticking = false;
  function seekTick() {
    if (!live.ctx) { ticking = false; return; } if (live.backing) { var p = live.position(); if (!$('#seek').matches(':active')) $('#seek').value = Math.floor(p); $('#pos').textContent = mmss(p); } requestAnimationFrame(function () { setTimeout(seekTick, 250); }); }

  // ------------------------------------------------------------------ start
  async function start() {
    var b = $('#start'); b.disabled = true; b.textContent = 'Turning on...';
    try { await live.open({}); }
    catch (e) { b.disabled = false; b.textContent = 'Turn on microphone'; toast(e && e.name === 'NotAllowedError' ? 'The browser blocked the microphone. Click the lock icon in the address bar, allow the microphone, and try again.' : 'Could not start the microphone (' + (e && e.message || e) + '). Check that a microphone is connected and that no other app is using it.', true); return; }
    toast(''); b.hidden = true; $('#panel').hidden = false; $('#lat').textContent = 'Estimated delay: about ' + live.estLatencyMs() + ' ms. Use headphones to avoid feedback.';
    applyKey(); setPreset(state.preset); live.setReverb($('#reverb').value / 100); if (backingBuf) live.setBacking(backingBuf);
    live.onEnd = function () { if (live.recording) stopRec(); else $('#play').textContent = 'Play'; };
    if (!drawing) { drawing = true; requestAnimationFrame(draw); } if (mode === 'karaoke' && !ticking) { ticking = true; seekTick(); }
  }

  // ------------------------------------------------------------------ events
  var kSel = $('#key'); NOTES.forEach(function (n, i) { var o = document.createElement('option'); o.value = i; o.textContent = n; kSel.appendChild(o); });
  $('#start').onclick = start;
  $('#key').onchange = function () { state.key = +this.value; applyKey(); };
  $('#scale').onchange = function () { state.scale = this.value; applyKey(); };
  root.querySelectorAll('[data-preset]').forEach(function (b) { b.onclick = function () { setPreset(this.getAttribute('data-preset')); }; });
  $('#amount').oninput = applyTune; $('#speed').oninput = applyTune;
  $('#reverb').oninput = function () { live.setReverb(this.value / 100); $('#reverbv').textContent = this.value + '%'; };
  $('#rec').onclick = record;
  $('#micoff').onclick = function () {
    if (live.recording) stopRec();
    live.close(); state.pitch = []; $('#panel').hidden = true; $('#note').textContent = '--';
    var b = $('#start'); b.hidden = false; b.disabled = false; b.textContent = 'Turn on microphone'; toast('Microphone off. Nothing is being recorded.');
  };
  if (mode === 'karaoke') {
    var drop = $('#kdrop'), inp = $('#kfile');
    drop.onclick = function () { inp.click(); };
    drop.onkeydown = function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); inp.click(); } };
    inp.onchange = function () { loadFile(inp.files[0]); inp.value = ''; };
    ['dragenter', 'dragover'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
    ['dragleave', 'drop'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); }); });
    drop.addEventListener('drop', function (e) { loadFile(e.dataTransfer && e.dataTransfer.files[0]); });
    $('#kdemo').onclick = function () { var d = VFCore.demoLoop(44100), AC = window.AudioContext || window.webkitAudioContext, c = new AC(), b = c.createBuffer(1, d.channels[0].length, d.sampleRate); b.getChannelData(0).set(d.channels[0]); try { c.close(); } catch (e) {} useBacking(b, 'Demo loop (made in your browser)'); };
    $('#play').onclick = function () { if (!live.ctx) { toast('Turn on the microphone first.', true); return; } if (live.playing) { live.pause(); this.textContent = 'Play'; } else { live.play(+$('#seek').value); this.textContent = 'Pause'; } };
    $('#stop').onclick = function () {
      if (!live.ctx) return;
      if (live.recording) stopRec();
      live.pause(); live.offset = 0; $('#seek').value = 0; $('#pos').textContent = '0:00'; $('#play').textContent = 'Play'; stopLyrics();
    };
    $('#restart').onclick = function () { if (!live.ctx) return; live.play(0); $('#play').textContent = 'Pause'; };
    $('#seek').oninput = function () { if (live.playing) live.play(+this.value); else live.offset = +this.value; };
    $('#bvol').oninput = function () { live.setBackGain(this.value / 100); };
    $('#vvol').oninput = function () { live.setVoiceGain(this.value / 100); };
    $('#reduce').onchange = function () { live.setReduce(this.checked); };
    $('#nudge').oninput = function () { live.setNudge(+this.value); $('#nudgev').textContent = (this.value > 0 ? '+' : '') + this.value + ' ms'; };
    $('#showlyr').onchange = function () { var v = $('#lyrview'); v.hidden = !this.checked; v.textContent = $('#lyr').value || 'Paste your lyrics above, then tick "Show lyrics".'; };
    $('#lyr').oninput = function () { if (!$('#lyrview').hidden) $('#lyrview').textContent = this.value; };
    $('#lyrsize').oninput = function () { $('#lyrview').style.fontSize = this.value + 'px'; };
  }
  drawKeyLabel();
})();
