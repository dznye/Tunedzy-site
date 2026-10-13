/* Tunedzy free tools: page glue. Decodes the dropped file in the browser, analyses it in a Web Worker, renders the cards.
   Nothing is uploaded: there is no network code in this file. */
(function () {
  'use strict';
  var root = document.getElementById('tool');
  if (!root) return;
  var focus = root.getAttribute('data-focus') || 'all';
  var $ = function (s, r) { return (r || root).querySelector(s); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var drop = $('#drop'), input = $('#file'), prog = $('#prog'), out = $('#results'), demoBtn = $('#demo');
  var supportMail = 'fuidzy@outlook.com', BASE = root.getAttribute('data-base') || '/vocalforge';

  function mmss(t) { t = Math.max(0, Math.round(t)); return Math.floor(t / 60) + ':' + ('0' + (t % 60)).slice(-2); }
  function f1(v) { return (Math.round(v * 10) / 10).toFixed(1); }
  function setProg(msg, p) { prog.hidden = false; $('#progmsg').textContent = msg; $('#progbar').style.width = Math.round(p * 100) + '%'; }

  // ------------------------------------------------------------------ analysis in a worker (falls back to the page thread)
  function analyse(chs, sr, onProg) {
    return new Promise(function (resolve, reject) {
      var core = document.getElementById('vfcore').textContent, w;
      try {
        var src = core + ';self.onmessage=function(e){try{var d=e.data;var r=VFCore.analyzeAll(d.chs,d.sr,{progress:function(m,p){self.postMessage({prog:[m,p]})}});self.postMessage({res:r})}catch(err){self.postMessage({err:String(err&&err.message||err)})}}';
        w = new Worker(URL.createObjectURL(new Blob([src], { type: 'text/javascript' })));
      } catch (e) { w = null; }
      if (!w) { try { resolve(VFCore.analyzeAll(chs, sr, { progress: onProg })); } catch (e2) { reject(e2); } return; }
      w.onmessage = function (m) {
        var d = m.data;
        if (d.prog) onProg(d.prog[0], d.prog[1]); else if (d.res) { w.terminate(); resolve(d.res); } else if (d.err) { w.terminate(); reject(new Error(d.err)); }
      };
      w.onerror = function (e) { w.terminate(); reject(new Error(e.message || 'analysis failed')); };
      w.postMessage({ chs: chs.slice(0, 2), sr: sr }, chs.slice(0, 2).map(function (c) { return c.buffer; }));
    });
  }

  function run(chs, sr, name, seconds) {
    out.hidden = true; out.innerHTML = ''; setProg('Starting', 0.03); root.classList.add('busy');
    return analyse(chs, sr, setProg).then(function (r) {
      r.name = name; render(r); prog.hidden = true; root.classList.remove('busy');
      var t = $('#results'); if (t && t.scrollIntoView && !root.hasAttribute('data-noscroll')) t.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }).catch(function (e) { root.classList.remove('busy'); fail('Something went wrong while analysing this file (' + (e.message || e) + '). Try a WAV or MP3.'); });
  }
  function fail(msg) { prog.hidden = true; out.hidden = false; out.innerHTML = '<div class="tcard bad"><p>' + esc(msg) + '</p></div>'; }

  function handleFile(file) {
    if (!file) return;
    if (file.size > 400 * 1024 * 1024) { fail('That file is very large (over 400 MB). Try an MP3 or a shorter WAV.'); return; }
    setProg('Reading ' + file.name, 0.02); root.classList.add('busy');
    var fr = new FileReader();
    fr.onerror = function () { fail('Could not read that file.'); };
    fr.onload = function () {
      setProg('Decoding audio', 0.06);
      var AC = window.AudioContext || window.webkitAudioContext, ctx = new AC();
      var done = function (buf) {
        var chs = []; for (var c = 0; c < Math.min(2, buf.numberOfChannels); c++) chs.push(new Float32Array(buf.getChannelData(c)));
        try { ctx.close(); } catch (e) {}
        run(chs, buf.sampleRate, file.name, buf.duration);
      };
      var bad = function () { fail('Your browser could not decode that file. MP3, WAV, FLAC, OGG and (on most browsers) M4A work.'); };
      var p = ctx.decodeAudioData(fr.result, done, bad); if (p && p.catch) p.catch(bad);
    };
    fr.readAsArrayBuffer(file);
  }

  // ------------------------------------------------------------------ cards
  function bar(p, cls) { return '<div class="meter ' + (cls || '') + '"><i style="width:' + Math.round(Math.max(0, Math.min(1, p)) * 100) + '%"></i></div>'; }
  function card(id, cls, body) { return '<div class="tcard ' + cls + (focus === id ? ' primary' : '') + '" id="c-' + id + '" data-id="' + id + '">' + body + '</div>'; }

  function bpmCard(r) {
    var t = r.tempo; if (!t) return card('bpm', 'idle', '<h3>Tempo</h3><p>This file is too short to find a steady tempo (needs about 6 seconds of music).</p>');
    var alts = t.alt.map(function (a) { return '<button class="chip" data-bpm="' + a + '" title="Use this tempo instead">' + (Math.abs(a / t.bpm - 2) < 0.02 ? 'double-time ' : Math.abs(a / t.bpm - 0.5) < 0.02 ? 'half-time ' : '') + a + '</button>'; }).join('');
    return card('bpm', 'bpm', '<div class="kicker">Tempo</div><div class="big"><span id="bpmval">' + f1(t.bpm) + '</span><small> BPM</small></div>' +
      bar(t.confidence, 'amber') + '<p class="mute">' + (t.confidence > 0.55 ? 'Steady, clear pulse.' : 'Weaker pulse. Use tap tempo to double-check.') + '</p>' +
      (alts ? '<div class="chips"><span class="mute">Could also be read as</span>' + alts + '</div>' : '') +
      '<p class="mute sm">Rhythm detection often lands on half-time or double-time in rap and trap. Pick whichever matches how you count it.</p>');
  }
  function keyCard(r) {
    var k = r.key; if (!k) return card('key', 'idle', '<h3>Key</h3><p>Not enough pitched music in this file to name a key.</p>');
    var others = k.others.slice(0, 2).map(function (o) { return '<span class="chip ghost">' + esc(o.name) + '</span>'; }).join('');
    return card('key', 'key', '<div class="kicker">Key</div><div class="big">' + esc(k.name) + '</div>' +
      '<div class="chips"><span class="chip solid">Camelot ' + k.camelot + '</span><span class="chip ghost">same notes as ' + esc(k.relative) + '</span></div>' + bar(k.confidence, 'violet') +
      '<p class="mute">' + (k.confidence > 0.5 ? 'Strong match.' : 'Close call between a few keys.') + (others ? ' Next closest:' : '') + '</p><div class="chips">' + others + '</div>' +
      '<p class="mute sm">Set your autotune or your producer\'s scale to this key. If vocals sound off, try the relative key shown above.</p>');
  }
  function chordCard(r) {
    var c = r.chords; if (!c || !c.timeline.length) return card('chords', 'idle', '<h3>Chords</h3><p>No clear chords found (works best on music with guitar, piano, synth or pads).</p>');
    var shown = c.timeline.slice(0, 48).map(function (x) { return '<span class="chord" title="' + mmss(x.t) + '"><b>' + esc(x.chord) + '</b><i>' + (x.deg ? esc(x.deg) : '') + '</i></span>'; }).join('');
    var top = c.top.slice(0, 4).map(function (x) { return '<span class="chip ghost">' + esc(x.chord) + '</span>'; }).join('');
    return card('chords', 'chords', '<div class="kicker">Chords</div>' + (c.loop ? '<div class="big sm2">' + esc(c.loop) + '</div><p class="mute">Most repeated progression</p>' : '') +
      '<div class="chordline">' + shown + '</div><div class="chips"><span class="mute">Most used</span>' + top + '</div>' +
      '<p class="mute sm">Approximate triads (major and minor) every two beats, starting from the first beat found. Great for a starting point; check by ear for 7ths and extended chords.</p>');
  }
  function loudCard(r) {
    var l = r.loudness, k = r.check; if (!l || !isFinite(l.lufs)) return card('loud', 'idle', '<h3>Loudness</h3><p>This file is silent or too short to measure.</p>');
    var rows = [['Spotify', -14], ['YouTube', -14], ['Apple Music', -16]].map(function (p) {
      var g = p[1] - l.lufs, txt = g > 0.4 ? (p[0] === 'YouTube' ? 'left as is (no boost)' : 'turned up ' + f1(g) + ' dB') : g < -0.4 ? 'turned down ' + f1(-g) + ' dB' : 'about right';
      return '<tr><td>' + p[0] + '</td><td>' + p[1] + ' LUFS</td><td>' + txt + '</td></tr>';
    }).join('');
    return card('loud', 'loud', '<div class="kicker">Loudness</div><div class="big">' + f1(l.lufs) + '<small> LUFS</small></div>' +
      '<div class="stats"><div><b>' + f1(k.truePeakDb) + ' dB</b><span>true peak (est.)</span></div><div><b>' + f1(l.lra) + ' LU</b><span>loudness range</span></div><div><b>' + f1(l.shortTermMax) + '</b><span>loudest 3 s</span></div></div>' +
      '<table class="mini"><tr><th>Platform</th><th>Target</th><th>What happens</th></tr>' + rows + '</table>' +
      '<p class="mute sm">Integrated loudness per ITU-R BS.1770 / EBU R128, measured on your file in this browser. Platforms change their targets sometimes, so treat these as a guide.</p>');
  }
  function status(v, good, warn) { return v <= good ? 'ok' : v <= warn ? 'warn' : 'bad'; }
  function checkCard(r) {
    var k = r.check; if (!k) return '';
    var rows = [];
    var peakS = k.peakDb > -0.1 ? 'bad' : k.peakDb > -1 ? 'warn' : 'ok';
    rows.push([k.clipEvents > 0 ? 'bad' : 'ok', 'Clipping', k.clipEvents > 0 ? k.clipEvents + ' clipped spot' + (k.clipEvents > 1 ? 's' : '') + ' found. Clipped peaks sound harsh and are hard to repair.' : 'No clipped peaks found.']);
    rows.push([peakS, 'Peak level', f1(k.peakDb) + ' dBFS. ' + (peakS === 'ok' ? 'Healthy headroom.' : 'Very close to full scale. Leave room for processing and conversion.')]);
    var nS = k.noiseFloorDb > -40 ? 'bad' : k.noiseFloorDb > -50 ? 'warn' : 'ok';
    rows.push([nS, 'Background noise', f1(k.noiseFloorDb) + ' dBFS in the quietest moments' + (k.snr ? ' (' + Math.round(k.snr) + ' dB below the loud parts)' : '') + '. ' +
      (nS === 'ok' ? 'Clean gaps.' : nS === 'warn' ? 'The quiet moments sit fairly high. That can be hiss or room tone, or just a take with no pauses. Listen to a gap between phrases.' : 'A lot of noise or room sound under the voice. Light noise reduction will help.')]);
    var rS = k.spec.rumble > 0.15 ? 'bad' : k.spec.rumble > 0.06 ? 'warn' : 'ok';
    rows.push([rS, 'Low rumble', Math.round(k.spec.rumble * 100) + '% of the energy sits below 80 Hz. ' + (rS === 'ok' ? 'Nothing to fix.' : 'Rumble, handling or desk noise. A high-pass filter around 80 to 100 Hz removes it.')]);
    var lv = k.lufs, lS = (lv === null || !isFinite(lv)) ? 'ok' : (lv < -30 ? 'warn' : lv > -9 ? 'warn' : 'ok');
    rows.push([lS, 'Overall level', (lv !== null && isFinite(lv)) ? f1(lv) + ' LUFS. ' + (lv < -30 ? 'Quiet. Raise the level before processing so noise is not boosted later.' : lv > -9 ? 'Very loud for a solo vocal. Check for clipping and leave room to mix.' : 'A healthy working level.') : 'Could not measure.']);
    var bad = rows.filter(function (x) { return x[0] === 'bad'; }).length, warn = rows.filter(function (x) { return x[0] === 'warn'; }).length;
    var verdict = bad ? 'Needs work before you post' : warn ? 'Nearly there' : 'Looks ready';
    return card('check', 'check ' + (bad ? 'bad' : warn ? 'warn' : 'ok'), '<div class="kicker">Vocal check-up</div><div class="big sm2">' + verdict + '</div>' +
      '<ul class="rows">' + rows.map(function (x) { return '<li class="' + x[0] + '"><i></i><div><b>' + x[1] + '</b><span>' + esc(x[2]) + '</span></div></li>'; }).join('') + '</ul>' +
      '<p class="mute sm">These checks look at the whole file. They are a quick health check, not a replacement for listening.</p>');
  }

  function render(r) {
    var order = { bpm: ['bpm', 'key', 'chords', 'loud', 'check'], key: ['key', 'bpm', 'chords', 'loud', 'check'], chords: ['chords', 'key', 'bpm', 'loud', 'check'],
                  loud: ['loud', 'check', 'bpm', 'key', 'chords'], check: ['check', 'loud', 'bpm', 'key', 'chords'], all: ['bpm', 'key', 'chords', 'loud', 'check'] }[focus] || ['bpm', 'key', 'chords', 'loud', 'check'];
    var make = { bpm: bpmCard, key: keyCard, chords: chordCard, loud: loudCard, check: checkCard };
    var summary = '';
    if (r.tempo) summary += f1(r.tempo.bpm) + ' BPM';
    if (r.key) summary += (summary ? ' | ' : '') + r.key.name + ' (' + r.key.camelot + ')';
    if (r.chords && r.chords.loop) summary += ' | ' + r.chords.loop;
    if (r.loudness && isFinite(r.loudness.lufs)) summary += ' | ' + f1(r.loudness.lufs) + ' LUFS';
    var cta = (r.check && (r.check.clipEvents > 0 || r.check.noiseFloorDb > -55 || r.check.spec.rumble > 0.05))
      ? '<h3>Want that vocal fixed in one pass?</h3><p>Tunedzy removes noise, rumble, clicks and harsh S sounds, repairs clipping, tunes to the key above and masters the result. Free 7-day trial.</p>'
      : '<h3>Make the vocal match this track</h3><p>Tunedzy tunes your vocal to this key and tempo, sets its level against the beat and masters the result. Free 7-day trial.</p>';
    out.hidden = false;
    out.innerHTML = '<div class="resbar"><div><b>' + esc(r.name) + '</b><span>' + mmss(r.seconds) + ' &middot; ' + Math.round(r.sampleRate / 100) / 10 + ' kHz &middot; analysed on your device</span></div>' +
      '<button class="btn small" id="copy" type="button">Copy results</button></div><div class="tgrid">' + order.map(function (id) { return make[id](r); }).join('') + '</div>' +
      '<div class="ctabox">' + cta + '<div class="cta"><a class="btn primary" href="' + BASE + '#try">Try Tunedzy free</a><a class="btn ghost" href="mailto:' + supportMail + '?subject=Tunedzy%20question">Ask us anything</a></div></div>';
    var cp = $('#copy'); if (cp) cp.onclick = function () { try { navigator.clipboard.writeText(summary); cp.textContent = 'Copied'; setTimeout(function () { cp.textContent = 'Copy results'; }, 1600); } catch (e) { cp.textContent = summary; } };
    out.onclick = function (e) {
      var b = e.target.closest ? e.target.closest('[data-bpm]') : null; if (!b) return;
      var v = $('#bpmval'); if (v) v.textContent = f1(parseFloat(b.getAttribute('data-bpm')));
    };
  }

  // ------------------------------------------------------------------ events
  drop.addEventListener('click', function () { input.click(); });
  drop.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); input.click(); } });
  input.addEventListener('change', function () { handleFile(input.files[0]); input.value = ''; });
  ['dragenter', 'dragover'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
  ['dragleave', 'drop'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); }); });
  drop.addEventListener('drop', function (e) { var f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0]; handleFile(f); });
  document.addEventListener('dragover', function (e) { e.preventDefault(); });
  document.addEventListener('drop', function (e) { if (!root.contains(e.target)) e.preventDefault(); });
  if (demoBtn) demoBtn.addEventListener('click', function () { var d = VFCore.demoLoop(44100); run(d.channels, d.sampleRate, 'Demo loop (made in your browser)', d.channels[0].length / d.sampleRate); });

  // ------------------------------------------------------------------ tap tempo
  var tap = $('#tap');
  if (tap) {
    var taps = [], tbpm = $('#tapbpm'), tinfo = $('#tapinfo'), idle;
    var hit = function () {
      var now = performance.now(); if (taps.length && now - taps[taps.length - 1] > 2500) taps = [];
      taps.push(now); taps = taps.slice(-10); clearTimeout(idle); idle = setTimeout(function () { taps = []; }, 2600);
      tap.classList.add('hit'); setTimeout(function () { tap.classList.remove('hit'); }, 90);
      if (taps.length < 2) { tbpm.textContent = '--'; tinfo.textContent = 'Keep tapping on the beat'; return; }
      var iv = []; for (var i = 1; i < taps.length; i++) iv.push(taps[i] - taps[i - 1]); iv.sort(function (a, b) { return a - b; });
      var med = iv[Math.floor(iv.length / 2)], bpm = 60000 / med;
      tbpm.textContent = f1(bpm); tinfo.textContent = taps.length + ' taps. Half-time ' + f1(bpm / 2) + ' / double-time ' + f1(bpm * 2);
    };
    tap.addEventListener('pointerdown', function (e) { e.preventDefault(); hit(); });
    tap.addEventListener('keydown', function (e) { if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); hit(); } });
    $('#tapreset').addEventListener('click', function () { taps = []; tbpm.textContent = '--'; tinfo.textContent = 'Tap the big button on the beat, at least four times'; });
  }
})();
