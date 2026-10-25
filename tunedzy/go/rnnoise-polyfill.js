/* AudioWorkletGlobalScope has no atob and no self: the RNNoise WebAssembly loader needs both. Loaded before rnnoise-sync.js. */
const B64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
if (typeof globalThis.atob !== 'function') {
  globalThis.atob = function (s) {
    s = String(s).replace(/[\t\n\f\r ]+/g, '');
    s += '=='.slice(2 - (s.length & 3));
    let out = '', i = 0;
    while (i < s.length) {
      const a = B64.indexOf(s.charAt(i++)), b = B64.indexOf(s.charAt(i++)), c = B64.indexOf(s.charAt(i++)), d = B64.indexOf(s.charAt(i++));
      const n = (a << 18) | (b << 12) | ((c & 63) << 6) | (d & 63);
      out += c === 64 ? String.fromCharCode((n >> 16) & 255)
           : d === 64 ? String.fromCharCode((n >> 16) & 255, (n >> 8) & 255)
           : String.fromCharCode((n >> 16) & 255, (n >> 8) & 255, n & 255);
    }
    return out;
  };
}
if (typeof globalThis.self === 'undefined') globalThis.self = { location: { href: '' } };
