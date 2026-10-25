/* Tunedzy Go: studio sound on a phone. Record audio or video, or pick a file; the same voice engine as the desktop app's Perfect it (noise, level, tone, loudness)
 * runs in this page. Nothing is uploaded: no server sees the recording. Built on tz-engine.js (generated from the app's own source by tools/build_web_tools.py). */
'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const Stream = TZ.Stream;
  const S = {ai: true, mode: 'audio', preset: 'auto', level: 'balanced', rec: null, cur: null, ab: 'after', playing: false, busy: false, items: []};
  const SCENE = {auto: null, voice: 'natural', podcast: 'podcast', vlog: 'stream', music: 'singing', bad: 'fix'};
  const TARGET = {auto: -16, voice: -16, podcast: -16, vlog: -14, music: -14, bad: -16};
  const fmt = t => Math.floor(t / 60) + ':' + String(Math.floor(t % 60)).padStart(2, '0');
  const toast = (m, ms = 4000) => { const t = $('toast'); t.textContent = m; t.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => { t.hidden = true; }, ms); };
  const show = id => { document.querySelectorAll('.screen').forEach(s => s.classList.toggle('on', s.id === id)); window.scrollTo(0, 0); };

  /* ---------- the little database: your recent results stay on this phone ---------- */
  const DB = {
    open: () => DB.p || (DB.p = new Promise((res, rej) => { const r = indexedDB.open('tunedzy-go', 1); r.onupgradeneeded = () => r.result.createObjectStore('clips', {keyPath: 'id'}); r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error); })),
    async all() { try { const d = await DB.open(); return await new Promise(res => { const q = d.transaction('clips').objectStore('clips').getAll(); q.onsuccess = () => res((q.result || []).sort((a, b) => b.created - a.created)); q.onerror = () => res([]); }); } catch (e) { return []; } },
    async put(item) { try { const d = await DB.open(); await new Promise((res, rej) => { const t = d.transaction('clips', 'readwrite'); t.objectStore('clips').put(item); t.oncomplete = res; t.onerror = () => rej(t.error); }); } catch (e) { /* private mode: it just will not be remembered */ } },
    async del(id) { try { const d = await DB.open(); d.transaction('clips', 'readwrite').objectStore('clips').delete(id); } catch (e) { /* nothing */ } },
  };

  /* ---------- level meter and recording ---------- */
  const REC_WORKLET = `class GoRec extends AudioWorkletProcessor{constructor(){super();this.b=[];this.n=0}process(i){const x=i[0]&&i[0][0];if(x){this.b.push(x.slice());this.n+=x.length;if(this.n>=4096){const o=new Float32Array(this.n);let p=0;for(const c of this.b){o.set(c,p);p+=c.length}this.port.postMessage(o,[o.buffer]);this.b=[];this.n=0}}return true}}registerProcessor('go-rec',GoRec);`;
  let meterRaf = 0;
  function drawMeter(an) {
    const cv = $('meter'), g = cv.getContext('2d'), buf = new Float32Array(an.fftSize), hist = []; cancelAnimationFrame(meterRaf);
    const f = () => {
      an.getFloatTimeDomainData(buf); let p = 0; for (let i = 0; i < buf.length; i++) { const v = Math.abs(buf[i]); if (v > p) p = v; } hist.push(p); if (hist.length > 90) hist.shift();
      g.clearRect(0, 0, cv.width, cv.height); const w = cv.width / 90; g.fillStyle = 'rgba(255,255,255,.85)';
      hist.forEach((v, i) => { const h = Math.max(3, Math.min(1, v * 2.2) * cv.height * .9); g.fillRect(i * w + 1, cv.height / 2 - h / 2, w - 2, h); });
      meterRaf = requestAnimationFrame(f);
    };
    f();
  }
  async function startRecording() {
    if (S.rec) return;
    const video = S.mode === 'video';
    let stream;
    try { stream = await navigator.mediaDevices.getUserMedia({audio: {echoCancellation: false, noiseSuppression: false, autoGainControl: false, channelCount: 1}, video: video ? {facingMode: 'user', width: {ideal: 1280}, height: {ideal: 720}} : false}); }
    catch (e) { toast(e.name === 'NotAllowedError' ? 'Allow the microphone' + (video ? ' and camera' : '') + ' in your browser to record.' : 'Could not open the microphone: ' + e.message, 7000); return; }
    const AC = window.AudioContext || window.webkitAudioContext, ctx = new AC();
    const rec = {stream, ctx, t0: performance.now(), chunks: [], n: 0, video, mime: ''};
    const src = ctx.createMediaStreamSource(stream), an = ctx.createAnalyser(); an.fftSize = 1024; src.connect(an);
    if (video) {
      $('preview').srcObject = new MediaStream(stream.getVideoTracks()); $('preview').hidden = false; $('preview').play().catch(() => {});
      // the sound is cleaned live (the same chain as the desktop Live Studio) and that cleaned sound is what is recorded with the picture
      try {
        await Stream.start({test: c => c.createMediaStreamSource(new MediaStream(stream.getAudioTracks()))}); Stream.set(Object.assign({}, TZ.STREAM_PRESETS[SCENE[S.preset] || 'stream'].cfg, {mute: false, bypass: false}));
        const dest = Stream.ctx.createMediaStreamDestination(); Stream.n.final.connect(dest); rec.live = true;
        const out = new MediaStream([...stream.getVideoTracks(), ...dest.stream.getAudioTracks()]), types = ['video/mp4;codecs=avc1.42E01E,mp4a.40.2', 'video/mp4', 'video/webm;codecs=vp9,opus', 'video/webm;codecs=vp8,opus', 'video/webm'];
        rec.mime = types.find(t => window.MediaRecorder && MediaRecorder.isTypeSupported(t)) || '';
        rec.mr = new MediaRecorder(out, rec.mime ? {mimeType: rec.mime, videoBitsPerSecond: 4e6, audioBitsPerSecond: 192000} : {}); rec.mr.ondataavailable = e => { if (e.data.size) rec.chunks.push(e.data); }; rec.mr.start(1000);
      } catch (e) { toast('Could not start the live clean-up: ' + e.message, 7000); stopStream(rec); return; }
    } else {
      await ctx.audioWorklet.addModule(URL.createObjectURL(new Blob([REC_WORKLET], {type: 'application/javascript'})));
      const node = new AudioWorkletNode(ctx, 'go-rec', {numberOfInputs: 1, numberOfOutputs: 1, channelCount: 1, channelCountMode: 'explicit', outputChannelCount: [1]}), mute = ctx.createGain(); mute.gain.value = 0;
      src.connect(node); node.connect(mute).connect(ctx.destination); node.port.onmessage = m => { rec.chunks.push(m.data); rec.n += m.data.length; }; rec.node = node;
    }
    S.rec = rec; document.body.classList.add('recording'); $('recBtn').classList.add('on'); $('recBtn').setAttribute('aria-label', 'Stop recording'); $('recHint').textContent = video ? 'Recording with live clean sound. Tap to stop.' : 'Recording. Tap to stop.';
    drawMeter(an); rec.timer = setInterval(() => { $('timer').textContent = fmt((performance.now() - rec.t0) / 1000); }, 250);
    try { if (navigator.wakeLock) rec.lock = await navigator.wakeLock.request('screen'); } catch (e) { /* not available */ }
  }
  function stopStream(rec) { try { rec.stream.getTracks().forEach(t => t.stop()); } catch (e) { /* closed */ } try { rec.ctx.close(); } catch (e) { /* closed */ } try { if (rec.live) Stream.stop(); } catch (e) { /* stopped */ } try { rec.lock && rec.lock.release(); } catch (e) { /* none */ } }
  async function stopRecording() {
    const rec = S.rec; if (!rec) return; S.rec = null; clearInterval(rec.timer); cancelAnimationFrame(meterRaf);
    document.body.classList.remove('recording'); $('recBtn').classList.remove('on'); $('recBtn').setAttribute('aria-label', 'Start recording'); $('recHint').textContent = 'Tap to record. Nothing leaves your phone.'; $('preview').hidden = true; $('preview').srcObject = null; $('timer').textContent = '0:00';
    const secs = (performance.now() - rec.t0) / 1000, sr = rec.ctx.sampleRate;
    if (rec.video) {
      await new Promise(res => { rec.mr.onstop = res; try { rec.mr.stop(); } catch (e) { res(); } }); stopStream(rec);
      if (secs < .5 || !rec.chunks.length) return toast('That was too short.');
      const type = rec.mime.split(';')[0] || 'video/webm', blob = new Blob(rec.chunks, {type}), ext = type.includes('mp4') ? 'mp4' : 'webm';
      return finishVideo(blob, ext, secs);
    }
    stopStream(rec); const x = new Float32Array(rec.n); let p = 0; rec.chunks.forEach(c => { x.set(c, p); p += c.length; });
    if (x.length < sr * .8) return toast('That was too short: record at least a second.');
    return process({x, sr, name: 'Recording ' + new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'}), source: 'recorded'});
  }

  /* ---------- the same voice engine as the desktop app ---------- */
  function removeDc(x) { let m = 0; for (let i = 0; i < x.length; i++) m += x[i]; m /= x.length; if (Math.abs(m) < 1e-4) return x; const o = new Float32Array(x.length); for (let i = 0; i < x.length; i++) o[i] = x[i] - m; return o; }
  /** A lookahead limiter: the loudest sample never passes `ceil` (dBFS), with a 2 ms look-ahead and a 60 ms release, so nothing clips. */
  function limit(x, sr, ceilDb) {
    const ceil = Math.pow(10, ceilDb / 20), look = Math.max(1, Math.round(sr * .002)), rel = Math.exp(-1 / (sr * .06)), out = new Float32Array(x.length), need = new Float32Array(x.length);
    for (let i = 0; i < x.length; i++) { const a = Math.abs(x[i]); need[i] = a > ceil ? ceil / a : 1; }
    let g = 1; const dq = [];                                                  // sliding minimum of `need` over the look-ahead window
    for (let i = 0; i < x.length + look; i++) {
      if (i < x.length) { while (dq.length && need[dq[dq.length - 1]] >= need[i]) dq.pop(); dq.push(i); }
      while (dq.length && dq[0] <= i - look - 1) dq.shift();
      const j = i - look; if (j < 0) continue; const tgt = need[dq[0]]; g = tgt < g ? tgt : g * rel + tgt * (1 - rel); out[j] = x[j] * Math.min(1, g);
    }
    return out;
  }
  const stereoBuf = (x, sr) => { const b = new AudioBuffer({length: x.length, numberOfChannels: 2, sampleRate: sr}); b.copyToChannel(x, 0); b.copyToChannel(x, 1); return b; };
  async function finish(x, sr, lufs) {
    const l = await TZ.msLoudness(stereoBuf(x, sr)); let y = x;
    if (isFinite(l) && l > -70) { const k = Math.pow(10, Math.max(-12, Math.min(30, lufs - l)) / 20); y = new Float32Array(x.length); for (let i = 0; i < x.length; i++) y[i] = x[i] * k; }
    y = limit(y, sr, -1.5); return {out: y, lufsIn: l, lufsOut: await TZ.msLoudness(stereoBuf(y, sr))};
  }
  async function enhance(x, sr, o, step) {
    step('Listening to it…', 6);
    const before = TZ.micCheckup(x, sr); if (!before) throw new Error('That is too short to improve: it needs a few seconds of speech.');
    x = removeDc(x);
    let studio = false;
    if (o.ai) {                                                                  // Studio sound: the neural network takes the noise and the room out first
      try {
        if (!DFN.ready()) { step('Getting Studio sound ready (one time, about 22 MB)…', 8); await DFN.load('./', p => step('Getting Studio sound ready…', 8 + p * 12)); }
        step('Studio sound: taking out the noise and the room…', 22);
        const strength = {gentle: .6, balanced: .85, max: 1}[o.level] || .85, y = await DFN.enhance(x, sr, strength, p => step('Studio sound: taking out the noise and the room…', 22 + p * 40)); x = y; studio = true;
      } catch (e) { console.warn('Studio sound is not available here:', e); toast('Studio sound (AI) did not start on this device, so the standard clean-up was used.', 6000); }
    }
    const plan = TZ.perfectPlan(before, o.level, SCENE[o.preset] || undefined, studio);
    step('Evening out the level, shaping the tone…', studio ? 66 : 22);
    const r = await TZ.streamRenderOffline(x, sr, plan.cfg);
    step('Setting the loudness…', 88);
    const fin = await finish(r.out.length > x.length ? r.out.slice(0, x.length) : r.out, sr, o.target);
    return {x, out: fin.out, sr, before, after: TZ.micCheckup(fin.out, sr), did: plan.did, lufsIn: await TZ.msLoudness(stereoBuf(x, sr)), lufsOut: fin.lufsOut};
  }
  const ring = (p, t) => { $('ringV').style.strokeDashoffset = String(276.5 * (1 - p / 100)); $('ringT').textContent = Math.round(p) + '%'; if (t) $('workStep').textContent = t; };
  async function process(src) {
    if (S.busy) return; S.busy = true; show('work'); $('workTitle').textContent = 'Making it sound like a studio…'; ring(2, 'Starting…');
    try {
      const r = await enhance(src.x, src.sr, {level: S.level, preset: S.preset, target: TARGET[S.preset], ai: S.ai}, (t, p) => ring(p, t));
      ring(100, 'Done'); const id = String(Date.now()), item = {id, name: src.name, created: Date.now(), seconds: r.out.length / r.sr, sr: r.sr, kind: 'audio', preset: S.preset,
        before: new Blob([TZ.wavPcm([r.x], r.sr, 16)], {type: 'audio/wav'}), after: new Blob([TZ.wavPcm([r.out], r.sr, 16)], {type: 'audio/wav'}), stats: {lufsIn: r.lufsIn, lufsOut: r.lufsOut, noiseIn: r.before.noiseDb, noiseOut: r.after ? r.after.noiseDb : null, scoreIn: r.before.score, scoreOut: r.after ? r.after.score : null}, did: r.did};
      src.item = item; await DB.put(item); S.cur = Object.assign({}, item, {src}); showResult(S.cur);
    } catch (e) { toast('That did not work: ' + (e.message || e), 9000); show('home'); }
    S.busy = false;
  }
  async function finishVideo(blob, ext, secs) {
    const id = String(Date.now()), name = 'Video ' + new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'}), item = {id, name, created: Date.now(), seconds: secs, kind: 'video', ext, after: blob, did: ['Recorded with live studio sound: noise removed, level evened out, tone shaped while you filmed']};
    await DB.put(item); S.cur = item; showResult(item);
  }
  async function importFile(file) {
    if (S.busy) return; const isVideo = /^video\//.test(file.type) || /\.(mp4|mov|m4v|webm|3gp)$/i.test(file.name);
    S.busy = false; show('work'); ring(2, 'Reading the file…'); $('workTitle').textContent = isVideo ? 'Cleaning the sound of your video…' : 'Making it sound like a studio…';
    try { const d = await TZ.decodeToMono(file, 48000); S.busy = false; await process({x: d.x, sr: d.sr, name: file.name.replace(/\.[^.]+$/, ''), source: isVideo ? 'video' : 'file'}); }
    catch (e) { S.busy = false; toast('Could not open that file: ' + (e.message || 'unknown format') + '. Try a WAV, MP3 or M4A, or a video from your camera roll.', 9000); show('home'); }
  }

  /* ---------- the result ---------- */
  let au = null;
  function wave(canvas, x) {
    const g = canvas.getContext('2d'), W = canvas.width, H = canvas.height, step = Math.max(1, Math.floor(x.length / W)); g.clearRect(0, 0, W, H); g.fillStyle = '#ff8a3d';
    for (let i = 0; i < W; i++) { let m = 0; for (let j = i * step; j < Math.min(x.length, (i + 1) * step); j += 8) { const v = Math.abs(x[j]); if (v > m) m = v; } const h = Math.max(2, m * H * .92); g.fillRect(i, (H - h) / 2, 1, h); }
  }
  async function showResult(it) {
    show('result'); $('resName').textContent = it.name; S.ab = 'after'; setAB('after');
    const isVideo = it.kind === 'video'; $('resVideo').hidden = !isVideo; $('resWave').hidden = isVideo; $('abSeg').style.display = isVideo ? 'none' : ''; $('lvlSeg').style.display = isVideo ? 'none' : '';
    const afterUrl = URL.createObjectURL(it.after); S.urls = {after: afterUrl};
    if (au) { au.forEach(a => a.pause()); } au = null; $('playBtn').classList.remove('on');
    if (isVideo) { $('resVideo').src = afterUrl; $('playBtn').parentElement.style.display = 'none'; }
    else {
      $('playBtn').parentElement.style.display = ''; S.urls.before = URL.createObjectURL(it.before);
      const a1 = new Audio(S.urls.before), a2 = new Audio(afterUrl); const diff = (it.stats.lufsOut || -16) - (it.stats.lufsIn || -20); a1.volume = Math.min(1, Math.pow(10, Math.min(0, diff) / 20)); a2.volume = Math.min(1, Math.pow(10, Math.min(0, -diff) / 20));   // the louder one is turned down: a fair comparison
      [a1, a2].forEach(a => { a.onended = () => { S.playing = false; $('playBtn').classList.remove('on'); }; }); au = [a1, a2];
      try { const ab = await it.after.arrayBuffer(), d = await new OfflineAudioContext(1, 1, it.sr).decodeAudioData(ab); wave($('resWave'), d.getChannelData(0)); } catch (e) { /* no picture */ }
    }
    const s = it.stats || {}, f1 = v => (v == null || !isFinite(v)) ? '–' : Math.round(v);
    $('stats').replaceChildren(...(isVideo ? [] : [['Noise', f1(s.noiseIn) + ' → ' + f1(s.noiseOut) + ' dB'], ['Loudness', f1(s.lufsIn) + ' → ' + f1(s.lufsOut) + ' LUFS'], ['Sound score', f1(s.scoreIn) + ' → ' + f1(s.scoreOut)]].map(([k, v]) => { const d = document.createElement('div'); d.className = 'stat'; d.innerHTML = '<small></small><b></b>'; d.firstChild.textContent = k; d.lastChild.textContent = v; return d; })));
    $('did').replaceChildren(...(it.did || []).map(t => { const li = document.createElement('li'); li.textContent = t; return li; }));
    const ext = isVideo ? it.ext : 'wav'; $('dlBtn').href = afterUrl; $('dlBtn').download = it.name.replace(/[^\w .()-]/g, '_') + (isVideo ? '' : ' (studio sound)') + '.' + ext; $('dlBtn').textContent = 'Download';
  }
  function setAB(k) { S.ab = k; document.querySelectorAll('#abSeg button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.v === k))); }
  function togglePlay() {
    if (!au) return; const [a1, a2] = au, cur = S.ab === 'before' ? a1 : a2, other = cur === a1 ? a2 : a1;
    if (!cur.paused) { cur.pause(); other.pause(); S.playing = false; $('playBtn').classList.remove('on'); return; }
    other.pause(); cur.play(); S.playing = true; $('playBtn').classList.add('on');
  }
  function swapAB(k) { setAB(k); if (!au) return; const [a1, a2] = au, was = S.ab === 'before' ? a2 : a1, now = S.ab === 'before' ? a1 : a2, t = was.currentTime, playing = !was.paused; was.pause(); now.currentTime = t; if (playing) now.play(); }
  async function share() {
    const it = S.cur; if (!it) return; const isVideo = it.kind === 'video', name = it.name.replace(/[^\w .()-]/g, '_') + (isVideo ? '' : ' (studio sound)') + '.' + (isVideo ? it.ext : 'wav');
    const file = new File([it.after], name, {type: it.after.type || (isVideo ? 'video/mp4' : 'audio/wav')});
    if (navigator.canShare && navigator.canShare({files: [file]})) { try { await navigator.share({files: [file], title: it.name}); return; } catch (e) { if (e.name === 'AbortError') return; } }
    $('dlBtn').click();
  }
  async function reprocess(level) {
    if (!S.cur || !S.cur.src || S.busy) return; S.level = level; document.querySelectorAll('#lvlSeg button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.v === level)));
    await process(S.cur.src);
  }

  /* ---------- recent ---------- */
  async function renderRecent() {
    S.items = await DB.all(); const box = $('recent'); box.replaceChildren();
    S.items.slice(0, 12).forEach(it => {
      const row = document.createElement('div'); row.className = 'item'; const d = document.createElement('div'); d.innerHTML = '<b></b><small></small>'; d.firstChild.textContent = it.name; d.lastChild.textContent = `${it.kind === 'video' ? 'Video' : 'Audio'} · ${fmt(it.seconds || 0)} · ${new Date(it.created).toLocaleDateString()}`;
      const open = document.createElement('button'); open.className = 'chip'; open.textContent = 'Open'; open.onclick = () => { S.cur = it; showResult(it); };
      const del = document.createElement('button'); del.className = 'chip ghost'; del.textContent = 'Delete'; del.onclick = async () => { await DB.del(it.id); renderRecent(); };
      row.append(d, open, del); box.append(row);
    });
  }

  /* ---------- wiring ---------- */
  function init() {
    $('recBtn').onclick = () => S.rec ? stopRecording() : startRecording();
    $('pickBtn').onclick = () => $('fileIn').click(); $('fileIn').onchange = () => { const f = $('fileIn').files[0]; $('fileIn').value = ''; if (f) importFile(f); };
    $('modeSeg').onclick = e => { const v = e.target.dataset.v; if (!v || S.rec) return; S.mode = v; document.querySelectorAll('#modeSeg button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.v === v))); $('recHint').textContent = v === 'video' ? 'Film with live studio sound. Nothing leaves your phone.' : 'Tap to record. Nothing leaves your phone.'; };
    $('aiBox').onchange = () => { S.ai = $('aiBox').checked; };
    $('presetRow').onclick = e => { const v = e.target.dataset.p; if (!v) return; S.preset = v; document.querySelectorAll('#presetRow .chip').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.p === v))); };
    $('abSeg').onclick = e => { const v = e.target.dataset.v; if (v) swapAB(v); }; $('playBtn').onclick = togglePlay;
    $('lvlSeg').onclick = e => { const v = e.target.dataset.v; if (v) reprocess(v); };
    $('shareBtn').onclick = share; $('againBtn').onclick = () => { if (au) au.forEach(a => a.pause()); $('resVideo').pause(); show('home'); renderRecent(); };
    renderRecent();
    let deferred = null; addEventListener('beforeinstallprompt', e => { e.preventDefault(); deferred = e; $('installBtn').hidden = false; });
    $('installBtn').onclick = async () => { if (deferred) { deferred.prompt(); deferred = null; $('installBtn').hidden = true; } };
    if (/iPhone|iPad/.test(navigator.userAgent) && !navigator.standalone) { $('installBtn').hidden = false; $('installBtn').onclick = () => toast('Tap the Share button, then "Add to Home Screen".', 7000); }
    if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost')) navigator.serviceWorker.register('sw.js').catch(() => {});
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) { $('recBtn').disabled = true; $('recHint').textContent = 'Recording needs a secure page (https). You can still choose a recording.'; }
  }
  window.TZGo = {S, enhance, limit, removeDc, importFile, process, DB};
  init();
})();
