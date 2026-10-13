/* Tunedzy free tools: noise-cancelling mic + voice recorder page glue (streaming and recording modes).
   Nothing is uploaded; there is no network code here. */
(function () {
  'use strict';
  var root = document.getElementById('clean');
  if (!root) return;
  var mode = root.getAttribute('data-mode') || 'stream', BASE = root.getAttribute('data-base') || '/tunedzy';
  var $ = function (s) { return root.querySelector(s); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var clean = new VFClean.Clean(); window.__vfClean = clean;
  var NOTES = VFLive.NOTES;
  var st = { key: 0, scale: 'major', preset: 'pop', learned: false, takes: 0, recTimer: null, recStart: 0, pitchT: 0 };
  function toast(msg, bad) { var t = $('#msg'); t.textContent = msg; t.className = 'livemsg' + (bad ? ' bad' : ''); t.hidden = !msg; }
  function mmss(t) { t = Math.max(0, Math.floor(t)); return Math.floor(t / 60) + ':' + ('0' + (t % 60)).slice(-2); }
  function dbw(db) { return Math.max(0, Math.min(100, Math.round((db + 70) / 70 * 100))); }

  // ------------------------------------------------------------------ settings -> engine
  function applyDenoise() {
    var red = +$('#reduce').value, sens = +$('#sens').value / 10; $('#reducev').textContent = red + ' dB'; $('#sensv').textContent = sens.toFixed(1);
    clean.setParams({ reduceDb: red, sens: sens, gateOn: $('#gate').checked });
  }
  var PRESETS = { natural: { a: 0.55, s: 0.12 }, pop: { a: 0.8, s: 0.05 }, hard: { a: 1, s: 0 } };
  function applyTune() { clean.setTune($('#amount').value / 100, $('#speed').value / 1000); $('#amountv').textContent = $('#amount').value + '%'; $('#speedv').textContent = $('#speed').value === '0' ? 'instant' : $('#speed').value + ' ms'; }
  function setPreset(name) {
    st.preset = name; root.querySelectorAll('[data-preset]').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-preset') === name); });
    var p = PRESETS[name]; $('#amount').value = Math.round(p.a * 100); $('#speed').value = Math.round(p.s * 1000); applyTune();
  }
  function applyKey() { clean.setKey(st.key, st.scale); }
  function applyFx() {
    var r = $('#reverb').value, e = $('#echo').value, t = $('#echotime').value, c = $('#chorus').value;
    $('#reverbv').textContent = r + '%'; $('#echov').textContent = e + '%'; $('#echotimev').textContent = t + ' ms'; $('#chorusv').textContent = c + '%';
    clean.setReverb(r / 100); clean.setEcho(e / 100, +t); clean.setChorus(c / 100);
  }
  function applyAll() { applyDenoise(); clean.setPolish($('#polish').checked); clean.setBypass($('#ab').checked); applyKey(); setPreset(st.preset); applyFx(); clean.setAutotune($('#at').checked); }

  // ------------------------------------------------------------------ meters + learn
  clean.onMeter = function (m) {
    $('#inbar').style.width = dbw(m.inDb) + '%'; $('#outbar').style.width = dbw(m.outDb) + '%';
    $('#noisedb').textContent = m.noiseDb > -110 ? m.noiseDb.toFixed(0) + ' dBFS' : 'measuring...';
    if (m.learning) { $('#learnbar').style.width = Math.round(m.progress * 100) + '%'; }
  };
  clean.onLearned = function (m) {
    st.learned = true; $('#learn').disabled = false; $('#learn').textContent = 'Learn again'; $('#learnbar').style.width = '100%';
    $('#learnmsg').innerHTML = 'Learned your room: <b>' + (20 * Math.log10(m.noiseRms)).toFixed(0) + ' dBFS</b> of background noise is now being removed.';
  };
  clean.onPitch = function (m) {
    var now = performance.now(); if (now - st.pitchT < 120) return; st.pitchT = now;
    if (m.f > 0) { var n = VFLive.noteName(m.f); $('#note').textContent = n.name + (m.t ? ' > ' + VFLive.noteName(m.t).name : ''); }
  };
  function learn() {
    var b = $('#learn'); b.disabled = true; b.textContent = 'Stay quiet...'; $('#learnmsg').textContent = 'Stay silent for 3 seconds. Do not speak or type.'; $('#learnbar').style.width = '0%';
    setTimeout(function () { clean.learn(3); }, 500);
  }

  // ------------------------------------------------------------------ output devices (streaming mode)
  async function fillDevices() {
    try {
      var d = await clean.devices(), mic = $('#mic'); var cur = mic.value;
      mic.innerHTML = '<option value="">Default microphone</option>' + d.inputs.map(function (x) { return '<option value="' + esc(x.deviceId) + '">' + esc(x.label || 'Microphone') + '</option>'; }).join('');
      mic.value = cur;
      var os = $('#outsel'); if (os) {
        os.innerHTML = '<option value="">Do not play (just clean and meter)</option><option value="default">Default speakers or headphones (hear yourself)</option>' +
          d.outputs.filter(function (x) { return x.deviceId !== 'default' && x.deviceId !== 'communications'; }).map(function (x) { return '<option value="' + esc(x.deviceId) + '">' + esc(x.label || 'Output') + '</option>'; }).join('');
      }
    } catch (e) {}
  }
  async function chooseOutput() {
    var v = $('#outsel').value, s = $('#outstatus');
    if (v && v !== 'default' && !clean.canChooseOutput()) { s.textContent = 'This browser cannot choose an output device. Use Chrome or Edge on a computer.'; s.className = 'small bad'; return; }
    var ok = await clean.setOutput(v);
    if (!v) { s.textContent = 'Nothing is being played. The clean mic is only metered or recorded.'; s.className = 'small mute'; }
    else if (!ok) { s.textContent = 'Could not use that output device.'; s.className = 'small bad'; }
    else { var label = $('#outsel').selectedOptions[0].textContent; s.innerHTML = 'Sending your clean mic to: <b>' + esc(label) + '</b>'; s.className = 'small ok'; }
  }

  // ------------------------------------------------------------------ recording (voice recorder mode)
  function addTake(res) {
    st.takes++; var html = '<div class="take"><b>Take ' + st.takes + ' <small>' + mmss(res.seconds) + '</small></b>';
    function row(label, blob, name) { var url = URL.createObjectURL(blob); return '<div class="takerow"><span>' + label + '</span><audio controls preload="metadata" src="' + url + '"></audio><a class="btn small" download="' + name + '" href="' + url + '">Download WAV</a></div>'; }
    if (res.clean) html += row('Clean (noise removed)', res.clean, 'tunedzy-take' + st.takes + '-clean.wav');
    if (res.raw) html += row('Original (untouched)', res.raw, 'tunedzy-take' + st.takes + '-original.wav');
    html += '<p class="small mute">Want it studio-ready? <a href="' + BASE + '#pricing">Tunedzy</a> also fixes echo, tunes, levels and masters a take like this on your PC.</p></div>';
    $('#takes').insertAdjacentHTML('afterbegin', html);
  }
  function recToggle() {
    var b = $('#rec');
    if (clean.recording) {
      clearInterval(st.recTimer); var res = clean.stopRecording(); b.textContent = 'Record'; b.classList.remove('live'); $('#timer').textContent = '0:00';
      if (res.clean) addTake(res); else toast('Nothing was recorded.', true); return;
    }
    clean.startRecording(); b.textContent = 'Stop and save'; b.classList.add('live'); st.recStart = performance.now();
    st.recTimer = setInterval(function () { $('#timer').textContent = mmss((performance.now() - st.recStart) / 1000); }, 250);
  }

  // ------------------------------------------------------------------ clean an existing file (record mode)
  function cleanFile(file) {
    if (!file) return; var box = $('#cresult'); box.hidden = false; box.innerHTML = '<p>Reading <b>' + esc(file.name) + '</b>...</p>';
    file.arrayBuffer().then(function (ab) {
      var AC = window.AudioContext || window.webkitAudioContext, tmp = new AC();
      return tmp.decodeAudioData(ab).then(function (buf) { try { tmp.close(); } catch (e) {} return buf; });
    }).then(function (buf) {
      box.innerHTML = '<p>Cleaning <b>' + esc(file.name) + '</b> (' + mmss(buf.duration) + ')...</p>';
      var chs = []; for (var c = 0; c < Math.min(2, buf.numberOfChannels); c++) chs.push(new Float32Array(buf.getChannelData(c)));
      var origBlob = VFClean.wav16n(chs.map(function (x) { return x.slice(); }), buf.sampleRate);
      var opts = { reduceDb: +$('#reduce').value, sens: +$('#sens').value / 10, gateOn: $('#gate').checked };
      var src = document.getElementById('vfdenoise').textContent + ';self.onmessage=function(e){try{var d=e.data,o=[];for(var i=0;i<d.chs.length;i++){o.push(VFDenoise.cleanBuffer(d.chs[i],d.sr,d.opts))}self.postMessage({res:o.map(function(r){return{out:r.out,learned:r.learned,noiseRms:r.noiseRms}})},o.map(function(r){return r.out.buffer}))}catch(err){self.postMessage({err:String(err)})}}';
      var w = new Worker(URL.createObjectURL(new Blob([src], { type: 'text/javascript' })));
      return new Promise(function (resolve, reject) {
        w.onmessage = function (m) { w.terminate(); if (m.data.res) resolve(m.data.res); else reject(new Error(m.data.err)); };
        w.onerror = function (e) { w.terminate(); reject(new Error(e.message || 'failed')); };
        w.postMessage({ chs: chs, sr: buf.sampleRate, opts: opts }, chs.map(function (x) { return x.buffer; }));
      }).then(function (res) {
        var outs = res.map(function (r) { return r.out; });
        if ($('#cnorm').checked) { var pk = 0; outs.forEach(function (o) { for (var i = 0; i < o.length; i += 1) { var a = Math.abs(o[i]); if (a > pk) pk = a; } }); if (pk > 0) { var g = 0.89 / pk; outs.forEach(function (o) { for (var i = 0; i < o.length; i++) o[i] *= g; }); } }
        var cleanBlob = VFClean.wav16n(outs, buf.sampleRate), u1 = URL.createObjectURL(origBlob), u2 = URL.createObjectURL(cleanBlob);
        var base = file.name.replace(/\.[^.]+$/, '');
        box.innerHTML = '<div class="take"><b>' + esc(file.name) + ' <small>' + mmss(buf.duration) + '</small></b>' +
          '<p class="small mute">' + (res[0].learned === true ? 'Learned the background noise from a quiet part of your recording (' + (20 * Math.log10(res[0].noiseRms)).toFixed(0) + ' dBFS) and removed it.' : 'No silent part was found, so the noise was estimated from the whole recording and removed gently. For a stronger result, record 1 to 2 seconds of room tone at the start.') + '</p>' +
          '<div class="takerow"><span>Original</span><audio controls src="' + u1 + '"></audio></div>' +
          '<div class="takerow"><span>Cleaned</span><audio controls src="' + u2 + '"></audio><a class="btn small" download="' + esc(base) + '-clean.wav" href="' + u2 + '">Download WAV</a></div></div>';
      });
    }).catch(function (e) { box.innerHTML = '<p class="livemsg bad">Could not clean that file (' + esc(e.message || e) + '). Try a WAV or MP3.</p>'; });
  }

  // ------------------------------------------------------------------ start
  async function start() {
    var b = $('#start'); b.disabled = true; b.textContent = 'Turning on...';
    try { await clean.open({ deviceId: $('#mic').value || undefined }); }
    catch (e) { b.disabled = false; b.textContent = 'Turn on microphone'; toast(e && e.name === 'NotAllowedError' ? 'The browser blocked the microphone. Click the lock icon in the address bar, allow it, and try again.' : 'Could not start the microphone (' + (e && e.message || e) + ').', true); return; }
    toast(''); b.hidden = true; $('#panel').hidden = false; applyAll(); await fillDevices();
    $('#lat').textContent = 'Estimated delay: about ' + clean.latencyMs() + ' ms';
    if ($('#outsel')) chooseOutput();
  }

  // ------------------------------------------------------------------ events
  var kSel = $('#key'); NOTES.forEach(function (n, i) { var o = document.createElement('option'); o.value = i; o.textContent = n; kSel.appendChild(o); });
  $('#start').onclick = start; $('#learn').onclick = learn;
  ['#reduce', '#sens'].forEach(function (id) { $(id).oninput = applyDenoise; }); $('#gate').onchange = applyDenoise;
  $('#polish').onchange = function () { clean.setPolish(this.checked); }; $('#ab').onchange = function () { clean.setBypass(this.checked); };
  $('#at').onchange = function () { clean.setAutotune(this.checked); };
  $('#key').onchange = function () { st.key = +this.value; applyKey(); }; $('#scale').onchange = function () { st.scale = this.value; applyKey(); };
  root.querySelectorAll('[data-preset]').forEach(function (b) { b.onclick = function () { setPreset(this.getAttribute('data-preset')); if (!$('#at').checked) { $('#at').checked = true; clean.setAutotune(true); } }; });
  $('#amount').oninput = applyTune; $('#speed').oninput = applyTune;
  ['#reverb', '#echo', '#echotime', '#chorus'].forEach(function (id) { $(id).oninput = applyFx; });
  $('#micoff').onclick = function () { if (clean.recording) recToggle(); clean.close(); $('#panel').hidden = true; var b = $('#start'); b.hidden = false; b.disabled = false; b.textContent = 'Turn on microphone'; toast('Microphone off.'); };
  if (mode === 'stream') { $('#outsel').onchange = chooseOutput; $('#monitor').onchange = function () { clean.setMonitor(this.checked); }; }
  if (mode === 'record') {
    $('#rec').onclick = recToggle;
    var drop = $('#cdrop'), inp = $('#cfile');
    drop.onclick = function () { inp.click(); }; drop.onkeydown = function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); inp.click(); } };
    inp.onchange = function () { cleanFile(inp.files[0]); inp.value = ''; };
    ['dragenter', 'dragover'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
    ['dragleave', 'drop'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); }); });
    drop.addEventListener('drop', function (e) { cleanFile(e.dataTransfer && e.dataTransfer.files[0]); });
  }
})();
