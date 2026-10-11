"""Builds the static site for fuidzy.com/vocalforge into this folder (the GitHub repo root).

  python build.py                         pre-launch: informational CTAs, no buy button, no dead links
  python build.py --launched --download-url https://downloads.fuidzy.com/vocalforge/VocalForge-Setup-1.0.0.exe

Output layout (the Worker maps URL -> file):
  vocalforge/index.html                 https://fuidzy.com/vocalforge
  vocalforge/<slug>/index.html          https://fuidzy.com/vocalforge/<slug>
  vocalforge/og.png, favicon.png
  vocalforge-sitemap.xml
"""
import argparse
import html
import json
import shutil
from pathlib import Path

import content as C

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'vocalforge'
ap = argparse.ArgumentParser()
ap.add_argument('--launched', action='store_true')
ap.add_argument('--download-url', default='')
args = ap.parse_args()
LAUNCHED = args.launched and bool(args.download_url)
DOWNLOAD = args.download_url

e = html.escape
CSS = """
:root{--bg:#0b0c0f;--panel:#14161b;--panel2:#1b1e24;--line:#262a31;--text:#ecebe6;--mute:#9aa1ab;--amber:#ffb347;--amber2:#ff8a3c;--teal:#4fd1b5}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:radial-gradient(900px 500px at 75% -5%,#1d160c 0%,transparent 60%),var(--bg);color:var(--text);font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--amber);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1060px;margin:0 auto;padding:0 20px}.narrow{max-width:760px;margin:0 auto;padding:0 20px}
header.top{position:sticky;top:0;z-index:5;background:rgba(11,12,15,.88);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;align-items:center;gap:22px;height:58px}
.logo{display:flex;align-items:center;gap:10px;font-weight:700;color:var(--text);font-size:18px}.logo img{width:28px;height:28px;border-radius:8px}
.logo b{background:linear-gradient(90deg,var(--amber),var(--amber2));-webkit-background-clip:text;background-clip:text;color:transparent}
nav.main{display:flex;gap:20px;margin-left:auto;font-size:15px}nav.main a{color:var(--mute)}nav.main a:hover{color:var(--text);text-decoration:none}
.btn{display:inline-flex;align-items:center;gap:8px;border-radius:12px;padding:12px 22px;font-weight:650;font-size:16px;border:1px solid var(--line);background:var(--panel2);color:var(--text);cursor:pointer}
.btn:hover{text-decoration:none;border-color:#454c56}
.btn.primary{background:linear-gradient(180deg,#ffbe5c,#ff8f3d);color:#1d1204;border-color:transparent;box-shadow:0 10px 30px rgba(255,138,60,.25)}
.btn.primary:hover{filter:brightness(1.06)}
.btn.off{opacity:.65;cursor:default}
.hero{padding:64px 0 30px}.hero h1{font-size:clamp(34px,5.4vw,56px);line-height:1.08;letter-spacing:-.03em;margin:0 0 16px;max-width:840px}
.hero h1 em{font-style:normal;background:linear-gradient(90deg,var(--amber),var(--amber2));-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p.sub{font-size:19px;color:var(--mute);max-width:700px;margin:0 0 26px}
.cta{display:flex;gap:12px;flex-wrap:wrap;align-items:center}.small{font-size:14px;color:var(--mute)}
.badges{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}.badges span{font-size:13px;color:var(--mute);border:1px solid var(--line);border-radius:99px;padding:4px 12px;background:var(--panel)}
section{padding:46px 0}h2{font-size:clamp(24px,3.4vw,32px);letter-spacing:-.02em;margin:0 0 14px;line-height:1.2}h3{margin:0 0 6px;font-size:18px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px}
.card{background:linear-gradient(180deg,var(--panel),#101216);border:1px solid var(--line);border-radius:16px;padding:20px}
.card p{margin:0;color:var(--mute);font-size:15.5px}
.steps{counter-reset:s;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px}
.steps .card::before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:linear-gradient(180deg,var(--amber),var(--amber2));color:#1d1204;font-weight:800;margin-bottom:12px}
.mock{border:1px solid var(--line);border-radius:18px;background:#0e1013;padding:0;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.5);margin-top:34px}
.price{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:center}@media(max-width:760px){.price{grid-template-columns:1fr}}
.price .big{font-size:56px;font-weight:800;letter-spacing:-.03em}.price ul{margin:14px 0;padding-left:20px;color:var(--mute)}
table{width:100%;border-collapse:collapse;font-size:14.5px;margin:18px 0;display:block;overflow-x:auto}th,td{padding:10px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}th{color:var(--mute);font-weight:600;white-space:nowrap}
article h1{font-size:clamp(30px,4.6vw,44px);line-height:1.12;letter-spacing:-.025em;margin:34px 0 14px}article h2{margin-top:36px}
article p,article li{color:#d5d3cc}article ul,article ol{padding-left:22px}article li{margin:6px 0}
.lead{font-size:19px;color:#d9d7d0}.tldr{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--amber);border-radius:12px;padding:6px 20px 8px;margin:22px 0}
.tldr b{display:block;margin:10px 0 2px}.vf{background:linear-gradient(180deg,rgba(255,179,71,.08),transparent);border:1px solid rgba(255,179,71,.3);border-radius:16px;padding:22px;margin:38px 0}
.vf h2{margin-top:0;font-size:22px}.note{font-size:14px;color:var(--mute)}
details{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:10px 0}summary{cursor:pointer;font-weight:600}details p{margin:10px 0 2px;color:var(--mute)}
.crumbs{font-size:14px;color:var(--mute);padding-top:18px}.crumbs a{color:var(--mute)}
.related{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}.related a{display:block;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px;color:var(--text)}.related a:hover{border-color:#454c56;text-decoration:none}
footer{border-top:1px solid var(--line);margin-top:50px;padding:34px 0;color:var(--mute);font-size:14.5px}footer .cols{display:flex;gap:40px;flex-wrap:wrap}footer a{color:var(--mute)}footer h4{margin:0 0 8px;color:var(--text);font-size:14px}
.band{background:linear-gradient(180deg,var(--panel),#101216);border:1px solid var(--line);border-radius:20px;padding:34px;text-align:center}
.herogrid{display:grid;grid-template-columns:1.05fr .95fr;gap:42px;align-items:center}@media(max-width:900px){.herogrid{grid-template-columns:1fr}}
.photo{position:relative;border-radius:26px;overflow:hidden;border:1px solid #ffffff1c;box-shadow:0 40px 90px rgba(0,0,0,.55),0 0 0 8px #ffffff06;background:#111}
.photo img{display:block;width:100%;height:auto}.photo::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 55%,rgba(11,12,15,.55));pointer-events:none}
.heropic{position:relative}.floatmock{position:absolute;left:-26px;bottom:-34px;width:62%;border-radius:16px;overflow:hidden;border:1px solid #ffffff22;box-shadow:0 30px 70px rgba(0,0,0,.6);z-index:2}
@media(max-width:900px){.floatmock{left:10px;bottom:-24px}}.chip{position:absolute;right:14px;top:14px;z-index:2;background:rgba(11,12,15,.72);backdrop-filter:blur(8px);border:1px solid #ffffff22;border-radius:99px;padding:7px 14px;font-size:13px;color:var(--text)}
.chip i{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--teal);margin-right:8px;box-shadow:0 0 0 4px rgba(79,209,181,.18)}
.spot{display:grid;grid-template-columns:.8fr 1.2fr;gap:44px;align-items:center}@media(max-width:860px){.spot{grid-template-columns:1fr}}
.spot ul{padding-left:20px;color:#d5d3cc}.spot li{margin:8px 0}.eyebrow{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--amber);font-weight:700;margin:0 0 10px}
.privband{position:relative;border-radius:26px;overflow:hidden;min-height:340px;display:grid;align-items:center;border:1px solid var(--line)}
.privband img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(.2) brightness(.6)}
.privband::before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(11,12,15,.92) 8%,rgba(11,12,15,.45) 60%,rgba(11,12,15,.15))}
.privband .in{position:relative;z-index:2;padding:46px;max-width:620px}.privband h2{margin-bottom:12px}.privband p{color:#cfcdc6;margin:0 0 10px}
.pcards{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}.pcard{border-radius:20px;overflow:hidden;background:var(--panel);border:1px solid var(--line);transition:transform .2s,border-color .2s}
.pcard:hover{transform:translateY(-3px);border-color:#454c56}.pcard img{display:block;width:100%;height:210px;object-fit:cover}.pcard div{padding:18px 20px 20px}.pcard p{margin:0;color:var(--mute);font-size:15.5px}
.ico{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;background:linear-gradient(180deg,rgba(255,179,71,.18),rgba(255,138,60,.08));border:1px solid rgba(255,179,71,.3);margin-bottom:14px;color:var(--amber)}
.ico svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.banner{margin:20px 0 6px;border-radius:22px;overflow:hidden;border:1px solid var(--line);position:relative}.banner img{display:block;width:100%;height:auto}
.credit{font-size:12.5px;color:var(--faint,#6d747d);margin:6px 2px 0}.credit a{color:var(--mute)}
.related a.th{padding:0;overflow:hidden}.related a.th img{display:block;width:100%;height:120px;object-fit:cover}.related a.th span{display:block;padding:12px 16px}
.gh img{display:block;width:100%;height:150px;object-fit:cover}.guides .related{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
h2.c{text-align:center}.sub2{text-align:center;color:var(--mute);margin:-4px auto 26px;max-width:620px}
.glow{position:absolute;pointer-events:none;width:520px;height:520px;border-radius:50%;filter:blur(80px);opacity:.22;background:radial-gradient(circle,#ff8a3c,transparent 70%);right:-120px;top:-80px}
@media(prefers-reduced-motion:no-preference){.pcard,.card{transition:transform .2s,border-color .2s}.card:hover{transform:translateY(-2px);border-color:#3a4048}}
"""

# ---------------------------------------------------------------------------------------------------- photos (free licence, hosted by us)
# name -> (source file, width, height, focus x, focus y, alt text)
PHOTOS = {
    'hero':      ('pexels-8132797.jpg', 1100, 760, .55, .45, 'Singer wearing headphones recording vocals into a studio condenser microphone'),
    'neon':      ('pexels-18259198.jpg', 760, 980, .5, .3, 'Rapper performing into a microphone in front of a neon sign'),
    'neon-wide': ('pexels-18259198.jpg', 1600, 640, .5, .4, 'Rapper performing into a microphone in front of a neon sign'),
    'booth':     ('pexels-8133004.jpg', 900, 600, .55, .38, 'Vocal booth seen through a studio window with a singer in headphones'),
    'booth-wide':('pexels-8133004.jpg', 1600, 640, .55, .36, 'Vocal booth seen through a studio window with a singer in headphones'),
    'mic':       ('unsplash-bG8U3kaZltE.jpg', 900, 600, .5, .55, 'Condenser microphone with a pop filter in a dark studio'),
    'mic-wide':  ('unsplash-bG8U3kaZltE.jpg', 1600, 640, .5, .55, 'Condenser microphone with a pop filter in a dark studio'),
    'desk':      ('unsplash-Q-raIe-gAOo.jpg', 900, 600, .5, .5, 'Headphones resting on a laptop on a wooden desk'),
    'desk-wide': ('unsplash-Q-raIe-gAOo.jpg', 1600, 640, .5, .5, 'Headphones resting on a laptop on a wooden desk'),
    'neon-th':   ('pexels-18259198.jpg', 900, 600, .5, .2, 'Rapper performing into a microphone in front of a neon sign'),
    'hero-wide': ('pexels-8132797.jpg', 1600, 640, .55, .45, 'Singer wearing headphones recording vocals into a studio condenser microphone'),
}
CREDITS = [('Anna Pou', 'Pexels', 'https://www.pexels.com/photo/a-man-singing-in-front-of-the-microphone-8132797/'),
           ('Anna Pou', 'Pexels', 'https://www.pexels.com/photo/a-man-singing-in-the-studio-8133004/'),
           ('Eduardo L\u00f3pez', 'Pexels', 'https://www.pexels.com/photo/man-singing-into-the-mic-18259198/'),
           ('Leo Wieling', 'Unsplash', 'https://unsplash.com/photos/grayscale-photo-of-condenser-microphone-beside-pop-filter-bG8U3kaZltE'),
           ('Project 290', 'Unsplash', 'https://unsplash.com/photos/a-pair-of-headphones-sitting-next-to-a-laptop-Q-raIe-gAOo')]
GUIDE_PHOTO = {'fix-vocals-recorded-on-phone': 'hero', 'remove-echo-from-vocal-recording': 'mic', 'autotune-for-rap-vocals': 'neon-wide',
               'mix-vocals-on-a-beat': 'desk', 'future-vocal-effect-settings': 'booth', 'vocal-cleanup-software-compared': 'mic'}
SIZES = {}
THUMB = {'neon-wide': 'neon-th'}


def process_photos():
    from PIL import Image
    (OUT / 'img').mkdir(parents=True, exist_ok=True)
    for name, (src, w, h, fx, fy, alt) in PHOTOS.items():
        im = Image.open(ROOT / 'assets' / 'src' / src).convert('RGB')
        sw, sh = im.size
        scale = max(w / sw, h / sh)
        im = im.resize((int(sw * scale) + 1, int(sh * scale) + 1), Image.LANCZOS)
        left = int(min(max(fx * im.width - w / 2, 0), im.width - w))
        top = int(min(max(fy * im.height - h / 2, 0), im.height - h))
        im.crop((left, top, left + w, top + h)).save(OUT / 'img' / f'{name}.webp', 'WEBP', quality=76, method=6)
        SIZES[name] = (w, h)


def img(name, cls='', eager=False, alt=None):
    w, h = SIZES.get(name, PHOTOS[name][1:3])
    a = e(alt if alt is not None else PHOTOS[name][5])
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="{C.BASE}/img/{name}.webp" width="{w}" height="{h}" alt="{a}" {load}{" class=" + chr(34) + cls + chr(34) if cls else ""}>'


ICONS = {
    'clean': '<path d="M12 3l1.8 4.6L18.5 9l-4.7 1.4L12 15l-1.8-4.6L5.5 9l4.7-1.4z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
    'tune': '<path d="M4 17c3 0 3-10 6-10s3 10 6 10 2-6 4-6"/>',
    'beat': '<path d="M3 12h3l2-6 4 12 3-9 2 3h4"/>',
    'artist': '<circle cx="12" cy="8" r="3.5"/><path d="M5 20c1-4 4-6 7-6s6 2 7 6"/>',
    'mix': '<path d="M4 6h8M18 6h2M4 12h2M12 12h8M4 18h12M20 18h0"/><circle cx="15" cy="6" r="2"/><circle cx="9" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>',
    'master': '<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-5"/><circle cx="12" cy="17" r="1.2"/>',
}


def ico(key):
    return f'<div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[key]}</svg></div>'


# ---------------------------------------------------------------------------------------------------- pieces
def cta_primary(label_live='Download free trial', where='hero'):
    if LAUNCHED:
        return f'<a class="btn primary" href="{e(DOWNLOAD)}" rel="noopener">{label_live}</a>'
    return '<span class="btn primary off" aria-disabled="true">Windows download launching soon</span>'


def cta_buy():
    if LAUNCHED:
        return f'<a class="btn" href="{e(C.BUY_URL)}" rel="noopener">Buy lifetime license, $29</a>'
    return ''


def breadcrumbs(items):
    lis = ''.join(f'<a href="{e(u)}">{e(n)}</a> / ' for n, u in items[:-1]) + e(items[-1][0])
    ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': C.SITE + u} for i, (n, u) in enumerate(items)]}
    return f'<div class="crumbs">{lis}</div>', ld


def faq_html(faq):
    return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)


def faq_ld(faq):
    strip = lambda s: html.unescape(s.replace('<br>', ' ')).replace('\u2019', "'")
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in faq]}


def software_ld():
    offer = {'@type': 'Offer', 'price': '29.00', 'priceCurrency': 'USD', 'url': C.SITE + C.BASE + '#pricing',
             'availability': 'https://schema.org/InStock' if LAUNCHED else 'https://schema.org/PreOrder'}
    return {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': 'VocalForge', 'applicationCategory': 'MultimediaApplication',
            'operatingSystem': 'Windows 10, Windows 11', 'url': C.SITE + C.BASE, 'image': C.SITE + C.BASE + '/og.png',
            'description': 'Windows app that cleans, tunes, fits to the beat, style-matches and masters rough vocal recordings. Runs offline on your PC.',
            'offers': offer, 'publisher': {'@type': 'Organization', 'name': 'Fuidzy', 'url': C.SITE}}


def layout(*, title, desc, path, body, lds, robots='index,follow', og_type='website'):
    url = C.SITE + path
    nav = ''.join(f'<a href="{e(h)}">{e(n)}</a>' for n, h in C.NAV)
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{e(url)}">
<link rel="icon" href="{C.BASE}/favicon.png">
<meta name="theme-color" content="#0b0c0f">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="VocalForge by Fuidzy"><meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{e(url)}"><meta property="og:image" content="{C.SITE}{C.BASE}/og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{C.SITE}{C.BASE}/og.png">
<style>{CSS}</style>{ld}</head><body>
<header class="top"><div class="wrap"><a class="logo" href="{C.BASE}"><img src="{C.BASE}/favicon.png" alt="" width="28" height="28"><span>Vocal<b>Forge</b></span></a>
<nav class="main" aria-label="Main">{nav}</nav></div></header>
{body}
<footer><div class="wrap"><div class="cols">
<div><h4>VocalForge</h4><a href="{C.BASE}">Overview</a><br><a href="{C.BASE}#pricing">Pricing</a><br><a href="{C.BASE}#faq">FAQ</a></div>
<div><h4>Guides</h4>{''.join(f'<a href="{C.BASE}/{s}">{e(C.GUIDES[s]["h1"].split(":")[0][:44])}</a><br>' for s in C.GUIDE_ORDER[:4])}</div>
<div><h4>Legal</h4><a href="{C.BASE}/privacy">Privacy</a><br><a href="{C.BASE}/terms">Terms</a><br><a href="{C.BASE}/refund-policy">Refunds</a></div>
<div style="max-width:300px"><h4>Fuidzy</h4>VocalForge is a Fuidzy product. It is not affiliated with or endorsed by any artist or plugin company mentioned on this site.</div>
</div><p class="credit" style="margin-top:22px">Photos: {', '.join(f'<a href="{u}" rel="noopener">{n} / {site}</a>' for n, site, u in CREDITS)}. Free to use under the Pexels and Unsplash licenses.</p></div></footer></body></html>'''


MOCK = '''<svg viewBox="0 0 1000 420" role="img" aria-label="Illustration of the VocalForge mix screen: a waveform with painted sections and effect sliders" width="100%" style="display:block"><defs><linearGradient id="a" x1="0" x2="1"><stop offset="0" stop-color="#ffbe5c"/><stop offset="1" stop-color="#ff8f3d"/></linearGradient></defs>
<rect width="1000" height="420" fill="#0e1013"/><rect width="1000" height="40" fill="#121418"/><circle cx="22" cy="20" r="6" fill="#ff6b6b"/><circle cx="42" cy="20" r="6" fill="#ffb347"/><circle cx="62" cy="20" r="6" fill="#4fd1b5"/>
<rect y="40" width="150" height="380" fill="#101216"/><g fill="#1a1d22"><rect x="14" y="62" width="122" height="34" rx="9"/><rect x="14" y="106" width="122" height="34" rx="9"/><rect x="14" y="150" width="122" height="34" rx="9"/><rect x="14" y="194" width="122" height="34" rx="9" fill="#2a2013"/><rect x="14" y="238" width="122" height="34" rx="9"/></g>
<g fill="#ffb347"><rect x="24" y="209" width="40" height="4" rx="2"/></g>
<rect x="170" y="60" width="520" height="220" rx="12" fill="#14161a"/><rect x="250" y="60" width="130" height="220" fill="#ffb347" opacity=".16"/><rect x="480" y="60" width="150" height="220" fill="#9d8cff" opacity=".16"/>
<g fill="#a3abb5">''' + ''.join(f'<rect x="{180 + i * 6}" y="{170 - h}" width="3" height="{2 * h}" rx="1.5"/>' for i, h in enumerate(
    [12, 20, 34, 52, 60, 48, 66, 72, 58, 40, 62, 74, 68, 50, 34, 56, 70, 76, 64, 44, 30, 52, 68, 72, 60, 38, 24, 46, 64, 70, 56, 36, 22, 40, 58, 66, 52, 30, 18, 34, 54, 62, 50, 32, 20, 38, 56, 60, 44, 28, 16, 30, 46, 52, 38, 22, 12, 20, 34, 40, 30, 16, 10, 18, 26, 22, 14, 8, 12, 18, 14, 8, 10, 14, 10, 6, 8, 12, 8, 6, 8, 10, 6, 4])) + '''</g>
<g fill="#4fd1b5" opacity=".55"><path d="M180 270 C 240 250, 300 262, 360 236 S 480 226, 540 250 S 640 240, 680 224" stroke="#4fd1b5" stroke-width="2" fill="none"/></g>
<g font-family="system-ui,Segoe UI,sans-serif" font-size="13" fill="#868d97"><text x="180" y="300">Hook</text><text x="490" y="300">Ad-libs</text></g>
<g><rect x="710" y="60" width="270" height="340" rx="12" fill="#14161a"/>''' + ''.join(
    f'<text x="728" y="{92 + i * 44}" font-family="system-ui,sans-serif" font-size="13" fill="#9aa1ab">{n}</text><rect x="728" y="{102 + i * 44}" width="234" height="6" rx="3" fill="#22262c"/><rect x="728" y="{102 + i * 44}" width="{w}" height="6" rx="3" fill="url(#a)"/><circle cx="{728 + w}" cy="{105 + i * 44}" r="8" fill="#f4efe6"/>'
    for i, (n, w) in enumerate([('Autotune', 150), ('Reverb', 140), ('Echo', 100), ('Doubles', 170), ('Harmony', 90), ('Vocal level', 120)])) + '''</g>
<rect x="170" y="296" width="520" height="104" rx="12" fill="#14161a"/><circle cx="212" cy="348" r="22" fill="url(#a)"/><path d="M205 338v20l18-10z" fill="#1d1204"/><rect x="250" y="338" width="420" height="20" rx="8" fill="#0e1013"/></svg>'''


# ---------------------------------------------------------------------------------------------------- pages
def hub():
    feats = [
        ('Clean', 'Removes noise, mic pops, harsh S sounds and loud breaths, repairs clipped peaks, evens out levels and dries up room echo.'),
        ('Tune', 'Reads the key from your beat and tunes to it: off, natural, hard-tune, or a style learned from a reference song.'),
        ('Fit to the beat', 'Detects tempo and key, nudges words onto the beat, and sets the vocal level against the music.'),
        ('Sound like an artist', 'Drop in a song you love. VocalForge measures its tuning, tone, space and width and applies a similar treatment to your voice.'),
        ('Mix live', 'Paint hooks, verses and ad-libs on the timeline and give each its own reverb, echo, doubles and harmony. Changes are instant.'),
        ('Master and export', 'Loudness, true-peak and tonal checks with a pass/fail report, then export 24-bit WAV or FLAC.'),
    ]
    who = [
        ('Bedroom rappers and singers', 'Recorded on a phone or USB mic and want the take to sound finished next to the beat.'),
        ('Producers finishing demos', 'Turn a rough artist take into something you can send back or release.'),
        ('Anyone with a vocal that feels &ldquo;off&rdquo;', 'Timing that drifts, words that sound cut, levels that jump: fixed before you post.'),
    ]
    steps = [('Drop in your files', 'Your recording, your beat or song, and optionally a song by an artist whose sound you want.'),
             ('Press Forge it', 'VocalForge cleans, tunes, fits and styles your vocal and maps the song into hooks and verses.'),
             ('Adjust and export', 'Tweak with live sliders or painted sections, check the master, and export WAV or FLAC.')]
    guides = ''.join(f'<a href="{C.BASE}/{s}"><b>{e(C.GUIDES[s]["h1"])}</b><br><span class="small">{e(C.GUIDES[s]["desc"][:105])}&hellip;</span></a>' for s in C.GUIDE_ORDER)
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('VocalForge', C.BASE)])
    price_cta = (f'<a class="btn primary" href="{e(C.BUY_URL)}" rel="noopener">Buy lifetime license, $29</a>' if LAUNCHED
                 else '<span class="btn primary off" aria-disabled="true">Opens at launch</span>')
    status = ('' if LAUNCHED else '<p class="small">VocalForge for Windows is launching soon. The page and price are final; the download opens at launch.</p>')
    feats = [
        ('clean', 'Clean', 'Removes noise, mic pops, harsh S sounds and loud breaths, repairs clipped peaks, evens out levels and dries up room echo.'),
        ('tune', 'Tune', 'Reads the key from your beat and tunes to it: off, natural, hard-tune, or a style learned from a reference song.'),
        ('beat', 'Fit to the beat', 'Detects tempo and key, nudges words onto the beat, and sets the vocal level against the music.'),
        ('artist', 'Sound like an artist', 'Drop in a song you love. VocalForge measures its tuning, tone, space and width and applies a similar treatment to your voice.'),
        ('mix', 'Mix live', 'Paint hooks, verses and ad-libs on the timeline and give each its own reverb, echo, doubles and harmony. Changes are instant.'),
        ('master', 'Master and export', 'Loudness, true-peak and tonal checks with a pass/fail report, then export 24-bit WAV or FLAC.'),
    ]
    who = [('hero', 'Bedroom rappers and singers', 'Recorded on a phone or USB mic and want the take to sound finished next to the beat.'),
           ('booth', 'Producers finishing demos', 'Turn a rough artist take into something you can send back or release.'),
           ('desk', 'Anyone whose vocal feels &ldquo;off&rdquo;', 'Timing that drifts, words that sound cut, levels that jump: fixed before you post.')]
    steps = [('Drop in your files', 'Your recording, your beat or song, and optionally a song by an artist whose sound you want.'),
             ('Press Forge it', 'VocalForge cleans, tunes, fits and styles your vocal and maps the song into hooks and verses.'),
             ('Adjust and export', 'Tweak with live sliders or painted sections, check the master, and export WAV or FLAC.')]
    guides = ''.join(f'<a class="th" href="{C.BASE}/{s}">{img(THUMB.get(GUIDE_PHOTO[s], GUIDE_PHOTO[s]), alt="")}<span><b>{e(C.GUIDES[s]["h1"])}</b><br><span class="small" style="padding:0">{e(C.GUIDES[s]["desc"][:100])}&hellip;</span></span></a>' for s in C.GUIDE_ORDER)
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('VocalForge', C.BASE)])
    price_cta = (f'<a class="btn primary" href="{e(C.BUY_URL)}" rel="noopener">Buy lifetime license, $29</a>' if LAUNCHED
                 else '<span class="btn primary off" aria-disabled="true">Opens at launch</span>')
    status = ('' if LAUNCHED else '<p class="small" style="margin-top:14px">VocalForge for Windows is launching soon. The page and price are final; the download opens at launch.</p>')
    body = f'''<main><div class="wrap" style="position:relative"><div class="glow"></div><div class="hero"><div class="herogrid"><div>
<p class="eyebrow">Vocal finishing for Windows</p>
<h1>Make rough vocals sound <em>finished</em>, without a studio.</h1>
<p class="sub">VocalForge cleans noisy phone and bedroom recordings, tunes them to your beat&rsquo;s key, locks the flow, matches the sound of the artist you&rsquo;re going for, and masters the result. On your own PC, <strong>$29 once</strong>.</p>
<div class="cta">{cta_primary()}<a class="btn" href="#features">See what it does</a></div>{status}
<div class="badges"><span>Offline processing</span><span>Your songs stay on your PC</span><span>24-bit WAV / FLAC</span><span>7-day free trial</span><span>No subscription</span></div></div>
<div class="heropic"><div class="photo">{img('hero', eager=True)}</div><div class="chip"><i></i>Rough take in, finished vocal out</div><div class="floatmock">{MOCK}</div></div></div></div></div>
<section id="features"><div class="wrap"><p class="eyebrow" style="text-align:center">What it does</p><h2 class="c">One pass from rough take to finished track</h2><p class="sub2">Everything you would normally chain by hand, in the right order.</p>
<div class="grid">{''.join(f'<div class="card">{ico(k)}<h3>{n}</h3><p>{d}</p></div>' for k, n, d in feats)}</div></div></section>
<section><div class="wrap"><div class="spot"><div class="photo" style="max-width:420px;margin:0 auto">{img('neon')}</div><div>
<p class="eyebrow">Sound like the records you love</p><h2>Drop in a song. Get that treatment on your voice.</h2>
<p style="color:#d5d3cc">Pick any track by an artist whose sound you want. VocalForge separates the vocal and measures how it was tuned, brightened, spaced, doubled and compressed, then applies a similar treatment to <em>your</em> recording.</p>
<ul><li>Learns the autotune style: natural, modern or hard-snapped</li><li>Matches tone, reverb size, width and how tight the flow sits on the beat</li><li>Keeps your voice yours: it changes the processing, not who you are</li><li>Saves each style so you can reuse it on the next song</li></ul>
<p class="note">Not affiliated with or endorsed by any artist. Artist names are used only to describe styles of processing.</p></div></div></div></section>
<section><div class="wrap"><div class="privband">{img('mic-wide', alt='')}<div class="in"><p class="eyebrow">Private by design</p><h2>Your unreleased songs never leave your PC.</h2>
<p>VocalForge processes everything locally. No uploads, no per-minute limits, no watermarks. The only internet use is the license check and the optional AI add-on download.</p></div></div></div></section>
<section><div class="wrap"><p class="eyebrow" style="text-align:center">How it works</p><h2 class="c">Three steps</h2><div class="steps" style="margin-top:22px">{''.join(f'<div class="card"><h3>{n}</h3><p>{d}</p></div>' for n, d in steps)}</div></div></section>
<section><div class="wrap"><p class="eyebrow" style="text-align:center">Who it&rsquo;s for</p><h2 class="c">Made for people who record in real rooms</h2><div class="pcards" style="margin-top:22px">{''.join(f'<div class="pcard">{img(k)}<div><h3>{n}</h3><p>{d}</p></div></div>' for k, n, d in who)}</div>
<p class="note" style="margin-top:18px">Honest limits: VocalForge is a finishing tool, not a DAW or a VST plugin (yet), and it is Windows-only for now. It can improve a rough recording a lot, but it can&rsquo;t turn a vocal buried in echo or heavy distortion into a studio take. Re-recording closer to the mic is always the best fix.</p></div></section>
<section id="guides" class="guides"><div class="wrap"><p class="eyebrow" style="text-align:center">Free guides</p><h2 class="c">Get better vocals today</h2><p class="sub2">Practical, and useful with or without VocalForge.</p><div class="related">{guides}</div></div></section>
<section id="pricing"><div class="wrap"><div class="band"><div class="price"><div style="text-align:left"><div class="small">Lifetime license</div><div class="big">$29</div><div class="small">one-time payment, USD</div></div>
<div style="text-align:left"><ul><li>VocalForge for Windows 10 / 11</li><li>Use on up to 2 of your PCs</li><li>7-day free trial, everything unlocked</li><li>No subscription</li><li>Your audio never leaves your PC</li></ul><div class="cta">{price_cta}</div></div></div></div></div></section>
<section id="faq"><div class="narrow"><h2>Questions</h2>{faq_html(C.HUB_FAQ)}</div></section></main>'''
    title = 'VocalForge: Vocal Cleanup, Autotune & Mastering Software'
    desc = 'Turn rough phone or bedroom vocals into finished tracks. VocalForge cleans, tunes, fits to your beat and masters, offline on Windows. $29 once, 7-day trial.'
    return layout(title=title, desc=desc, path=C.BASE, body=body, lds=[software_ld(), faq_ld(C.HUB_FAQ), crumbs_ld])


def guide(slug):
    g = C.GUIDES[slug]
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('VocalForge', C.BASE), (g['h1'], f'{C.BASE}/{slug}')])
    rel = ''.join(f'<a class="th" href="{C.BASE}/{r}">{img(THUMB.get(GUIDE_PHOTO[r], GUIDE_PHOTO[r]), alt="")}<span><b>{e(C.GUIDES[r]["h1"])}</b></span></a>' for r in g['related'])
    pk = GUIDE_PHOTO[slug]
    banner = f'<div class="banner">{img(pk if pk.endswith("wide") else (pk + "-wide" if pk + "-wide" in PHOTOS else pk), eager=True)}</div>'
    tl = ''.join(f'<li>{t}</li>' for t in g['tldr'])
    action = (f'<p><a class="btn primary" href="{e(DOWNLOAD)}" rel="noopener">Download the free trial</a></p>' if LAUNCHED
              else f'<p><a class="btn" href="{C.BASE}">See what VocalForge does</a></p>')
    article_ld = {'@context': 'https://schema.org', '@type': 'Article', 'headline': g['h1'], 'description': g['desc'], 'datePublished': C.DATE, 'dateModified': C.DATE,
                  'image': C.SITE + C.BASE + '/og.png', 'mainEntityOfPage': C.SITE + f'{C.BASE}/{slug}',
                  'author': {'@type': 'Organization', 'name': 'Fuidzy'}, 'publisher': {'@type': 'Organization', 'name': 'Fuidzy', 'url': C.SITE}}
    body = f'''<main><div class="narrow"><article>{crumbs_html}<h1>{g['h1']}</h1><p class="note">Updated October 2026</p><p class="lead">{g['lead']}</p>{banner}
<div class="tldr"><b>The short version</b><ul>{tl}</ul></div>{g['body']}
<div class="vf"><h2>{g['vf_title']}</h2>{g['vf']}{action}</div>
<h2>Frequently asked questions</h2>{faq_html(g['faq'])}
<h2>Keep going</h2><div class="related">{rel}</div></article></div></main>'''
    return layout(title=g['title'], desc=g['desc'], path=f'{C.BASE}/{slug}', body=body, lds=[article_ld, faq_ld(g['faq']), crumbs_ld], og_type='article')


def policy(slug):
    p = C.POLICIES[slug]
    body = f'<main><div class="narrow"><article><h1>{p["h1"]}</h1>{p["body"]}</article></div></main>'
    return layout(title=p['title'], desc=p['desc'], path=f'{C.BASE}/{slug}', body=body, lds=[])


def thanks():
    body = '''<main><div class="narrow"><article><h1>Thank you for buying VocalForge</h1>
<p class="lead">Your license key is on its way to the email you used at checkout. It usually arrives within a minute.</p>
<h2>Get started</h2><ol><li>Install VocalForge for Windows (the download link is in your receipt email and on <a href="/vocalforge">the VocalForge page</a>).</li>
<li>Open VocalForge and click the <strong>License</strong> button at the top.</li><li>Paste your key and press <strong>Activate</strong>. One key works on up to 2 of your PCs.</li></ol>
<p>Didn&rsquo;t get the email? Check spam, then contact us from fuidzy.com.</p></article></div></main>'''
    return layout(title='Thanks for buying VocalForge', desc='Your VocalForge license key and next steps.', path=f'{C.BASE}/thanks', body=body, lds=[], robots='noindex,nofollow')


# ---------------------------------------------------------------------------------------------------- write everything
def write(rel, text):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')


def og():
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), (11, 12, 15))
    d = ImageDraw.Draw(img)
    for y in range(H):                                       # soft warm glow top-right
        for x in range(0, W, 4):
            dist = ((x - 950) ** 2 + (y + 40) ** 2) ** .5
            k = max(0, 1 - dist / 700)
            if k:
                d.rectangle([x, y, x + 3, y], fill=(int(11 + 60 * k), int(12 + 38 * k), int(15 + 8 * k)))
    bold = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 74)
    reg = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 34)
    small = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 30)
    icon = Image.open(ROOT / 'assets' / 'icon.png').convert('RGBA').resize((92, 92))
    img.paste(icon, (70, 70), icon)
    d.text((180, 84), 'VocalForge', font=small, fill=(236, 235, 230))
    d.text((70, 215), 'Make rough vocals', font=bold, fill=(236, 235, 230))
    d.text((70, 300), 'sound finished.', font=bold, fill=(255, 179, 71))
    d.text((70, 430), 'Clean, tune, fit to your beat and master,', font=reg, fill=(154, 161, 171))
    d.text((70, 475), 'offline on Windows. $29 once.', font=reg, fill=(154, 161, 171))
    for i, h in enumerate([30, 54, 86, 64, 100, 70, 44, 78, 50, 28]):          # waveform bars
        x = 800 + i * 36
        d.rounded_rectangle([x, 330 - h, x + 18, 330 + h], radius=9, fill=(255, 179 - i * 4, 71 - i * 2))
    img.save(OUT / 'og.png', optimize=True)


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True)
    process_photos()
    shutil.copy2(ROOT / 'assets' / 'icon.png', OUT / 'favicon.png')
    og()
    write('index.html', hub())
    for s in C.GUIDE_ORDER:
        write(f'{s}/index.html', guide(s))
    for s in C.POLICIES:
        write(f'{s}/index.html', policy(s))
    write('thanks/index.html', thanks())
    urls = [(C.BASE, '1.0')] + [(f'{C.BASE}/{s}', '0.8') for s in C.GUIDE_ORDER] + [(f'{C.BASE}/{s}', '0.3') for s in C.POLICIES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        f'  <url><loc>{C.SITE}{u}</loc><lastmod>{C.DATE}</lastmod><priority>{p}</priority></url>\n' for u, p in urls) + '</urlset>\n'
    (ROOT / 'vocalforge-sitemap.xml').write_text(sm, encoding='utf-8')
    pages = 1 + len(C.GUIDE_ORDER) + len(C.POLICIES) + 1
    print(f'built {pages} pages ({"LAUNCHED" if LAUNCHED else "pre-launch"}) -> {OUT}')


if __name__ == '__main__':
    main()
