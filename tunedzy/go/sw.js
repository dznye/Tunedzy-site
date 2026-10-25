/* Tunedzy Go service worker: everything is cached on the first visit, so the app opens and works with no connection. The cache name carries a hash of
 * the files (tools/build_go.py), so a new build replaces the old cache by itself. */
const VERSION = '5.0.0-9520be908b';
const CACHE = 'tunedzy-go-' + VERSION;
const FILES = ["./", "index.html", "go.css", "go.js", "dfn-web.js", "manifest.webmanifest", "tz-engine.js", "rnnoise-worklet.js", "rnnoise-polyfill.js", "rnnoise-sync.js", "icon-192.png", "icon-512.png", "icon-maskable.png"];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('tunedzy-go-') && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin) return;
  // the app files are cached when it is installed; the AI runtime and model (22 MB) are cached the first time Studio sound is used
  e.respondWith(caches.match(e.request, {ignoreSearch: true}).then(r => r || fetch(e.request).then(res => { if (res.ok && /\/(vendor|models)\//.test(u.pathname)) { const c = res.clone(); caches.open(CACHE).then(k => k.put(e.request, c)); } return res; })));
});
