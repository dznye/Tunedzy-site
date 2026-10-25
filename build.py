"""Builds the static site for fuidzy.com/tunedzy into this folder (the GitHub repo root).

  python build.py                         pre-launch: informational CTAs, no dead links
  python build.py --launched --download-url https://downloads.fuidzy.com/tunedzy/Tunedzy-Setup.exe

Output layout (the Worker maps URL -> file):
  tunedzy/index.html                      https://fuidzy.com/tunedzy
  tunedzy/<slug>/index.html               https://fuidzy.com/tunedzy/<slug>
  tunedzy/tools/index.html + tools/<tool>/index.html
  tunedzy/og.png, favicon.png, img/*.webp
  tunedzy-sitemap.xml, worker-pages.json (the slug whitelist the Worker uses)
"""
import argparse
import html
import json
import re
import shutil
from pathlib import Path

import content as C
import content_tools as T
import content_blog as B

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'tunedzy'
ap = argparse.ArgumentParser()
ap.add_argument('--launched', action='store_true')
ap.add_argument('--download-url', default='')
ap.add_argument('--go', default='', help='a built Tunedzy Go folder (python tools/build_go.py in the app repo) to publish at /tunedzy/go/')
args = ap.parse_args()
LAUNCHED = args.launched and bool(args.download_url)
DOWNLOAD = args.download_url

e = html.escape
CSS = (ROOT / 'assets' / 'site.css').read_text(encoding='utf-8')
CORE_JS = (ROOT / 'assets' / 'vf-core.js').read_text(encoding='utf-8')
UI_JS = (ROOT / 'assets' / 'vf-ui.js').read_text(encoding='utf-8')
LIVE_JS = (ROOT / 'assets' / 'vf-live.js').read_text(encoding='utf-8')
LIVE_UI_JS = (ROOT / 'assets' / 'vf-live-ui.js').read_text(encoding='utf-8')
DENOISE_JS = (ROOT / 'assets' / 'vf-denoise.js').read_text(encoding='utf-8')
CLEAN_JS = (ROOT / 'assets' / 'vf-clean.js').read_text(encoding='utf-8')
CLEAN_UI_JS = (ROOT / 'assets' / 'vf-clean-ui.js').read_text(encoding='utf-8')

# ---------------------------------------------------------------------------------------------------- photos (free licence, hosted by us)
# name -> (source file, width, height, focus x, focus y, alt text)
PHOTOS = {
    'hero':      ('pexels-8132797.jpg', 1100, 760, .55, .45, 'Singer wearing headphones recording vocals into a studio condenser microphone'),
    'neon':      ('pexels-18259198.jpg', 760, 980, .5, .3, 'Rapper performing into a microphone in front of a neon sign'),
    'neon-wide': ('pexels-18259198.jpg', 1600, 640, .5, .4, 'Rapper performing into a microphone in front of a neon sign'),
    'booth':     ('pexels-8133004.jpg', 900, 600, .55, .38, 'Vocal booth seen through a studio window with a singer in headphones'),
    'booth-wide': ('pexels-8133004.jpg', 1600, 640, .55, .36, 'Vocal booth seen through a studio window with a singer in headphones'),
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
GUIDE_PHOTO = {'fix-vocals-recorded-on-phone': 'hero', 'ai-vocal-cleanup-explained': 'desk', 'remove-echo-from-vocal-recording': 'mic',
               'autotune-for-rap-vocals': 'neon-wide', 'mix-vocals-on-a-beat': 'desk', 'future-vocal-effect-settings': 'booth',
               'vocal-cleanup-software-compared': 'mic'}
GUIDE_TOOLS = {'fix-vocals-recorded-on-phone': ['vocal-checker', 'bpm-finder'], 'ai-vocal-cleanup-explained': ['vocal-checker', 'song-key-finder'],
               'remove-echo-from-vocal-recording': ['vocal-checker', 'lufs-meter'], 'autotune-for-rap-vocals': ['song-key-finder', 'bpm-finder'],
               'mix-vocals-on-a-beat': ['bpm-finder', 'lufs-meter'], 'future-vocal-effect-settings': ['bpm-finder', 'song-key-finder'],
               'vocal-cleanup-software-compared': ['vocal-checker', 'lufs-meter']}
GUIDE_PHOTO.update(C.GUIDE_PHOTO_EXTRA)
GUIDE_TOOLS.update(C.GUIDE_TOOLS_EXTRA)
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
    'tempo': '<path d="M12 3l5 18H7z"/><path d="M12 15l4-7"/>',
    'key': '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3M14 9l2 2"/>',
    'chords': '<path d="M5 4v16M10 4v16M15 4v16M20 4v16"/><path d="M3 9h18"/>',
    'meter': '<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l3-6"/><path d="M6 17h2M16 17h2"/>',
    'check': '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    'upload': '<path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/>',
    'lock': '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    'mic': '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3M9 21h6"/>',
    'karaoke': '<path d="M9 18V6l10-2v12"/><circle cx="7" cy="18" r="2.5"/><circle cx="17" cy="16" r="2.5"/>',
    'denoise': '<path d="M3 12h2l2-5 3 10 3-14 3 12 2-3h3"/><path d="M4 20L20 4"/>',
    'record': '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.5" fill="currentColor"/>',
}
TOOL_COLOR = {'amber': 'cA', 'violet': 'cV', 'pink': 'cP', 'teal': 'cT', 'blue': 'cB'}


def ico(key, color='cA'):
    return f'<div class="ico {color}"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[key]}</svg></div>'


def svg_icon(key):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[key]}</svg>'


# ---------------------------------------------------------------------------------------------------- decorative shapes
def shapes(kind='hero'):
    dots = ('<svg class="dots {c}" viewBox="0 0 210 140"><defs><pattern id="dp{c}" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.8" fill="#fff"/></pattern></defs>'
            '<rect width="210" height="140" fill="url(#dp{c})"/></svg>')
    bars = '<span class="pbars p1">' + ''.join(f'<i style="height:{h}px"></i>' for h in (30, 62, 40, 84, 52, 70, 36, 78, 46, 58, 26)) + '</span>'
    squig = '<svg class="squig {c}" viewBox="0 0 210 40"><path d="M3 20 C 20 -2, 36 -2, 52 20 S 84 42, 100 20 S 132 -2, 148 20 S 180 42, 207 20"/></svg>'
    if kind == 'hero':
        return ('<div class="shapes" aria-hidden="true"><span class="blob b1 fl1"></span><span class="blob b2 fl2"></span><span class="blob b3"></span>'
                '<span class="ring r1 spin"></span><span class="ring r2 fl3"></span><span class="sq s1 fl2"></span><span class="sq s2 fl1"></span>'
                '<span class="tri t1 fl3"></span><span class="cross x1"></span><span class="cross x2"></span>' + dots.format(c='d1') + squig.format(c='q1') + '</div>')
    if kind == 'soft':
        return ('<div class="shapes" aria-hidden="true"><span class="blob b2 fl2"></span><span class="ring r3 fl3"></span><span class="sq s3 fl1"></span>'
                + dots.format(c='d2') + squig.format(c='q2') + '</div>')
    if kind == 'bars':
        return ('<div class="shapes" aria-hidden="true"><span class="blob b3"></span><span class="ring r2 fl3"></span><span class="sq s1 fl2"></span>' + bars + '</div>')
    return ''


# ---------------------------------------------------------------------------------------------------- shared pieces
def cta_primary():
    if LAUNCHED:
        return f'<a class="btn primary" href="{e(DOWNLOAD)}" rel="noopener">Download free for Windows</a>'
    return f'<a class="btn primary" href="{e(C.LAUNCH_MAIL)}">Email me at launch</a>'


def breadcrumbs(items):
    lis = ''.join(f'<a href="{e(u)}">{e(n)}</a> / ' for n, u in items[:-1]) + e(items[-1][0])
    ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': C.SITE + u} for i, (n, u) in enumerate(items)]}
    return f'<div class="crumbs">{lis}</div>', ld


def faq_html(faq):
    return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)


def faq_ld(faq):
    strip = lambda s: html.unescape(re.sub(r'<[^>]+>', '', s.replace('<br>', ' '))).replace('\u2019', "'")
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in faq]}


def software_ld():
    offer = {'@type': 'AggregateOffer', 'lowPrice': '0', 'highPrice': C.PRICES['year']['usd'], 'priceCurrency': 'USD', 'offerCount': 7, 'url': C.SITE + C.BASE + '/pricing',
             'description': 'Free to start (30 credits in the first month, about 12 a month after). Credit packs from $0.99, plans from $1.99 a month.',
             'availability': 'https://schema.org/InStock' if LAUNCHED else 'https://schema.org/PreOrder'}
    return {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': 'Tunedzy', 'applicationCategory': 'MultimediaApplication',
            'applicationSubCategory': 'Audio studio for voice, podcasts, streams and songs',
            'operatingSystem': 'Windows 10, Windows 11', 'url': C.SITE + C.BASE, 'image': C.SITE + C.BASE + '/og.png',
            'description': 'Audio studio for Windows that turns rough voice recordings into studio sound, with a multitrack editor, editing by transcript, mastering and live voice cleaning. Runs on your PC; nothing is uploaded. Free credits every month.',
            'offers': offer, 'publisher': {'@type': 'Organization', 'name': 'Fuidzy', 'url': C.SITE, 'email': C.SUPPORT_EMAIL}}


def webapp_ld(slug, name, desc):
    return {'@context': 'https://schema.org', '@type': 'WebApplication', 'name': name, 'url': f'{C.SITE}{C.BASE}/tools/{slug}' if slug else f'{C.SITE}{C.BASE}/tools',
            'applicationCategory': 'MultimediaApplication', 'operatingSystem': 'Any (web browser)', 'description': desc, 'isAccessibleForFree': True,
            'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}, 'publisher': {'@type': 'Organization', 'name': 'Fuidzy', 'url': C.SITE}}


def layout(*, title, desc, path, body, lds, robots='index,follow', og_type='website', scripts=''):
    url = C.SITE + path
    nav = ''.join(f'<a href="{e(h)}">{e(n)}</a>' for n, h in C.NAV)
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    tools_f = ''.join(f'<a href="{C.BASE}/tools/{s}">{e(T.TOOLS[s]["short"])}</a><br>' for s in T.TOOL_ORDER)
    guides_f = ''.join(f'<a href="{C.BASE}/{s}">{e(C.GUIDES[s]["h1"].split(":")[0][:46])}</a><br>' for s in C.GUIDE_ORDER[:5])
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{e(url)}">
<link rel="icon" href="{C.BASE}/favicon.png">
<meta name="theme-color" content="#140a14">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="Tunedzy by Fuidzy"><meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{e(url)}"><meta property="og:image" content="{C.SITE}{C.BASE}/og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{C.SITE}{C.BASE}/og.png">
<style>{CSS}</style>{ld}</head><body>
<header class="top"><div class="wrap"><a class="logo" href="{C.BASE}"><img src="{C.BASE}/favicon.png" alt="" width="30" height="30"><span>Tuned<b>zy</b></span></a>
<nav class="main" aria-label="Main">{nav}</nav><a class="hbtn" href="{C.BASE}#pricing">{'Download free' if LAUNCHED else 'Free'}</a></div></header>
{body}
<footer><div class="wrap"><div class="cols">
<div><h4>Tunedzy</h4><a href="{C.BASE}">Overview</a><br><a href="{C.BASE}#features">Features</a><br><a href="{C.GO_URL}">Tunedzy Go (phone)</a><br><a href="{C.BASE}/pricing">Pricing and credits</a><br><a href="{C.BASE}#faq">FAQ</a></div>
<div><h4>Free tools</h4>{tools_f}</div>
<div><h4>Guides</h4>{guides_f}<a href="{C.BASE}/blog">All audio guides</a></div>
<div><h4>More apps by Fuidzy</h4><a href="https://fuidzy.com/">Fuidzy planner</a><br><a href="https://fuidzy.com/deep-clean-pc-or-mac-storage">SpaceWise: clean up PC storage</a><br><a href="https://tradzy.net/" rel="noopener">Tradzy</a><br><a href="https://dznye.github.io/Androidzy/" rel="noopener">Androidzy</a></div>
<div><h4>Support</h4><a href="{e(C.HELP_MAIL)}">{C.SUPPORT_EMAIL}</a><br><a href="{e(C.MAC_MAIL)}">Request a Mac version</a><br><a href="{C.BASE}/privacy">Privacy</a><br><a href="{C.BASE}/terms">Terms</a><br><a href="{C.BASE}/refund-policy">Refunds</a></div>
</div><p class="credit" style="margin-top:26px">Tunedzy is a Fuidzy product. It is not affiliated with or endorsed by any artist or plugin company mentioned on this site.</p>
<p class="credit">Photos: {', '.join(f'<a href="{u}" rel="noopener">{n} / {site}</a>' for n, site, u in CREDITS)}. Free to use under the Pexels and Unsplash licenses.</p></div></footer>{scripts}</body></html>'''


def tool_scripts():
    return f'<script id="vfcore">{CORE_JS}</script><script>{UI_JS}</script>'


def tool_widget(focus='all', tap=False, noscroll=False):
    tapbox = ''
    if tap:
        tapbox = ('<div class="tapbox"><button id="tap" type="button" aria-label="Tap on every beat">TAP</button><div class="tapout"><b id="tapbpm">--</b>'
                  '<span id="tapinfo">Tap the big button on the beat, at least four times</span><br><button class="btn small ghost" id="tapreset" type="button" style="margin-top:10px">Reset</button></div></div>')
    return (f'<div class="tool" id="tool" data-focus="{focus}" data-base="{C.BASE}"{" data-noscroll" if noscroll else ""}><div class="inner">'
            f'<div class="drop" id="drop" tabindex="0" role="button" aria-label="Choose or drop an audio file"><div class="ic">{svg_icon("upload")}</div>'
            '<b>Drop a song, beat or vocal here</b><span>or click to choose a file &middot; MP3, WAV, FLAC, OGG</span></div>'
            f'<input type="file" id="file" accept="audio/*,.mp3,.wav,.flac,.ogg,.m4a,.aac" hidden>'
            f'<div class="toolrow"><span class="priv">{svg_icon("lock")}Stays on your device. Nothing is uploaded.</span>'
            '<button class="btn small" id="demo" type="button">Try a demo loop</button></div>'
            '<div class="prog" id="prog" hidden><div class="t" id="progmsg">Starting</div><div class="tr"><i id="progbar"></i></div></div>'
            f'<div id="results" hidden aria-live="polite"></div>{tapbox}</div></div>')


def live_scripts(kind):
    core = f'<script id="vfcore">{CORE_JS}</script>' if kind == 'karaoke' else ''
    return f'{core}<script>{LIVE_JS}</script><script>{LIVE_UI_JS}</script>'


def live_widget(kind):
    karaoke = kind == 'karaoke'
    load = ''
    if karaoke:
        load = (f'<div class="drop small" id="kdrop" tabindex="0" role="button" aria-label="Choose a backing track"><div class="ic">{svg_icon("upload")}</div>'
                '<b>Add your backing track</b><span>MP3, WAV, FLAC or OGG &middot; an instrumental works best &middot; the key is found for you</span></div>'
                '<input type="file" id="kfile" accept="audio/*,.mp3,.wav,.flac,.ogg,.m4a" hidden>'
                f'<div class="toolrow"><span class="priv">{svg_icon("lock")}Your files and your voice stay on your device.</span><button class="btn small" id="kdemo" type="button">Try a demo backing</button></div>'
                '<div class="backinfo" id="backinfo" hidden></div>')
    transport = ''
    lyrics = ''
    if karaoke:
        transport = ('<div class="cbox" style="margin-top:16px"><h3>Backing track</h3><div id="transport" hidden>'
                     '<div class="fl"><button class="btn small" id="play" type="button">Play</button><button class="btn small" id="stop" type="button">Stop</button><button class="btn small" id="restart" type="button">Restart</button>'
                     '<span class="v" id="pos">0:00</span><input type="range" id="seek" min="0" max="100" value="0"><span class="v" id="dur">0:00</span></div>'
                     '<div class="fl"><label for="bvol">Track volume</label><input type="range" id="bvol" min="0" max="150" value="80"></div>'
                     '<div class="fl"><label for="vvol">Your voice</label><input type="range" id="vvol" min="0" max="200" value="100"></div>'
                     '<div class="fl"><label><input type="checkbox" id="reduce"> Reduce original vocals</label><span class="v" style="text-align:left;min-width:0">for full songs: removes the centre vocal (and some bass)</span></div>'
                     '<div class="fl"><label for="nudge">Recording sync</label><input type="range" id="nudge" min="-150" max="150" value="0"><output class="v" id="nudgev">0 ms</output></div></div>'
                     '<p class="small mute" id="notrack">Add a backing track above to play along. You can also just sing and record without one.</p></div>')
        lyrics = ('<div class="cbox" style="margin-top:16px"><h3>Lyrics</h3><textarea id="lyr" placeholder="Paste your lyrics here"></textarea>'
                  '<div class="fl" style="margin-top:10px"><label><input type="checkbox" id="showlyr"> Show lyrics</label><label for="lyrsize" style="min-width:0">Size</label><input type="range" id="lyrsize" min="18" max="56" value="28">'
                  '<label for="lyrspeed" style="min-width:0">Auto-scroll</label><input type="range" id="lyrspeed" min="0" max="30" value="8"></div><div id="lyrview" hidden></div></div>')
    return (f'<div class="live" id="live" data-mode="{kind if karaoke else "tune"}" data-base="{C.BASE}"><div class="inner">{load}'
            '<div class="startrow"><button class="btn primary" id="start" type="button">Turn on microphone</button>'
            '<span class="small">Wear headphones so the music and your voice do not feed back into the mic.</span></div>'
            '<div class="livemsg" id="msg" hidden></div>'
            '<div class="livepanel" id="panel" hidden>'
            '<div class="pitchbox"><canvas id="pcv" width="900" height="210"></canvas><div class="pitchread"><b id="note">--</b><span id="cents">sing a note</span></div></div>'
            '<div class="lvlbar" title="Mic level"><i id="lvl"></i></div>'
            '<div class="ctrlgrid" style="margin-top:16px"><div class="cbox"><h3>Autotune</h3>'
            '<div class="fl"><label for="key">Key</label><select id="key"></select><select id="scale"><option value="major">major</option><option value="minor">minor</option><option value="chromatic">every note</option></select><span class="small mute" id="keylabel"></span></div>'
            '<div class="presets"><button type="button" data-preset="natural">Natural</button><button type="button" data-preset="pop">Pop</button><button type="button" data-preset="hard">Hard-tune</button><button type="button" data-preset="off">Off (compare)</button></div>'
            '<div class="fl"><label for="amount">Strength</label><input type="range" id="amount" min="0" max="100" value="80"><output class="v" id="amountv">80%</output></div>'
            '<div class="fl"><label for="speed">Retune speed</label><input type="range" id="speed" min="0" max="250" value="50"><output class="v" id="speedv">50 ms</output></div>'
            '<div class="fl"><label for="reverb">Reverb</label><input type="range" id="reverb" min="0" max="60" value="18"><output class="v" id="reverbv">18%</output></div></div>'
            f'<div>{transport if karaoke else ""}'
            '<div class="warnrow">Tip: this is a real-time browser effect with a small delay. For a final, studio-clean vocal, record dry and tune it afterwards in Tunedzy.</div></div></div>'
            f'{lyrics}'
            '<div class="recrow"><button id="rec" type="button">Record</button><span id="timer">0:00</span><button class="btn small ghost" id="micoff" type="button">Turn off microphone</button><span class="small mute" id="lat"></span></div>'
            '<div id="takes"></div></div></div></div>')


def clean_scripts():
    return (f'<script id="vfdenoise">{DENOISE_JS}</script><script>{LIVE_JS}</script><script>{CLEAN_JS}</script><script>{CLEAN_UI_JS}</script>')


def _slider(id_, label, lo, hi, val, out):
    return f'<div class="fl"><label for="{id_}">{label}</label><input type="range" id="{id_}" min="{lo}" max="{hi}" value="{val}"><output class="v" id="{id_}v">{out}</output></div>'


def clean_widget(kind):
    stream = kind == 'stream'
    noise = ('<div class="cbox" style="margin-top:16px"><h3>Noise removal</h3>' + _slider('reduce', 'Reduction', 6, 30, 18, '18 dB') + _slider('sens', 'Sensitivity', 10, 30, 16, '1.6') +
             '<div class="fl"><label><input type="checkbox" id="gate" checked> Close the gate between words</label></div>'
             '<p class="small mute" style="margin:0">Higher reduction removes more noise but can thin the voice. Sensitivity makes it hunt noise harder.</p></div>')
    panel_top = ('<div class="meters"><div class="mrow"><span>Before</span><div class="lvlbar"><i id="inbar"></i></div></div>'
                 '<div class="mrow"><span>After</span><div class="lvlbar"><i id="outbar" style="background:linear-gradient(90deg,var(--teal),var(--blue))"></i></div></div>'
                 '<div class="mrow"><span>Room noise</span><b id="noisedb" class="small">measuring...</b></div></div>'
                 '<div class="learnrow"><button class="btn primary" id="learn" type="button">Learn my room noise</button><div class="lvlbar grow"><i id="learnbar"></i></div></div>'
                 '<p class="small mute" id="learnmsg">Stay silent for 3 seconds so it can hear your room. Until you do, it tracks the noise automatically.</p>'
                 '<div class="fl" style="margin-top:6px"><label><input type="checkbox" id="ab"> Hear original (compare)</label><label><input type="checkbox" id="polish"> Voice polish</label></div>')
    autotune = ('<div class="cbox"><h3>Autotune</h3><div class="fl"><label><input type="checkbox" id="at"> Autotune on</label><span class="small mute" id="note">--</span></div>'
                '<div class="fl"><label for="key">Key</label><select id="key"></select><select id="scale"><option value="major">major</option><option value="minor">minor</option><option value="chromatic">every note</option></select></div>'
                '<div class="presets"><button type="button" data-preset="natural">Natural</button><button type="button" data-preset="pop">Pop</button><button type="button" data-preset="hard">Hard-tune</button></div>'
                + _slider('amount', 'Strength', 0, 100, 80, '80%') + _slider('speed', 'Retune speed', 0, 250, 50, '50 ms') + '</div>')
    effects = ('<div class="cbox"><h3>Effects</h3>' + _slider('reverb', 'Reverb', 0, 80, 0, '0%') + _slider('echo', 'Echo', 0, 80, 0, '0%') + _slider('echotime', 'Echo time', 80, 700, 280, '280 ms')
               + _slider('chorus', 'Doubler', 0, 100, 0, '0%') + '<p class="small mute" style="margin:0">Effects are added after the noise removal, so they sit on a clean voice.</p></div>')
    if stream:
        extra = ('<div class="cbox" style="margin-top:16px"><h3>Send clean mic to</h3><div class="fl"><label for="outsel" style="min-width:0">Output</label><select id="outsel" style="flex:1;min-width:200px"></select></div>'
                 '<div class="fl"><label><input type="checkbox" id="monitor"> Also play in my headphones (monitor)</label></div>'
                 '<p class="small mute" id="outstatus">Choose a virtual cable (for example &ldquo;CABLE Input&rdquo;), then pick the matching &ldquo;CABLE Output&rdquo; as your microphone in OBS, Discord or Zoom.</p></div>')
    else:
        extra = ('<div class="recrow"><button id="rec" type="button">Record</button><span id="timer">0:00</span></div><div id="takes"></div>')
    panel = (f'<div class="livepanel" id="panel" hidden>{panel_top}<div class="ctrlgrid" style="margin-top:16px">{autotune}{effects}</div>{extra}'
             '<div class="recrow"><button class="btn small ghost" id="micoff" type="button">Turn off microphone</button><span class="small mute" id="lat"></span></div></div>')
    filebox = ''
    if not stream:
        filebox = (f'<div class="cbox" style="margin-top:16px"><h3>Clean an existing recording</h3><div class="drop small" id="cdrop" tabindex="0" role="button" aria-label="Choose a recording to clean">'
                   f'<div class="ic">{svg_icon("upload")}</div><b>Drop a recording here</b><span>MP3, WAV, FLAC or OGG &middot; the noise settings above are used</span></div>'
                   '<input type="file" id="cfile" accept="audio/*,.mp3,.wav,.flac,.ogg,.m4a" hidden>'
                   '<div class="fl" style="margin-top:12px"><label><input type="checkbox" id="cnorm" checked> Normalize the level</label></div><div id="cresult" hidden></div></div>')
    return (f'<div class="live" id="clean" data-mode="{kind}" data-base="{C.BASE}"><div class="inner">'
            '<div class="startrow"><select id="mic" aria-label="Microphone" style="min-width:200px"><option value="">Default microphone</option></select><button class="btn primary" id="start" type="button">Turn on microphone</button>'
            '<span class="small">Use headphones if you hear yourself, to avoid feedback.</span></div><div class="livemsg" id="msg" hidden></div>'
            f'{noise}{panel}{filebox}</div></div>')


# ---------------------------------------------------------------------------------------------------- rack mock (hero)
def rack():
    mods = [('CLEAN', 'var(--amber)', .72), ('TUNE', 'var(--pink)', .88), ('FIT', 'var(--teal)', .56), ('STYLE', 'var(--violet)', .66), ('MIX', 'var(--blue)', .8), ('MASTER', 'var(--orange)', .92)]
    hs = [10, 18, 30, 46, 54, 44, 60, 66, 52, 36, 56, 68, 62, 46, 30, 50, 64, 70, 58, 40, 26, 46, 62, 66, 54, 34, 22, 42, 58, 64, 50, 32, 20, 36, 52, 60, 46, 28, 16, 30, 48, 56, 42, 26]
    wave = ''.join(f'<rect x="{10 + i * 7.2:.1f}" y="{70 - h}" width="3.6" height="{2 * h}" rx="1.8" fill="url(#rg)"/>' for i, h in enumerate(hs))
    wavesvg = ('<svg viewBox="0 0 332 140" aria-hidden="true"><defs><linearGradient id="rg" x1="0" x2="1"><stop offset="0" stop-color="#ffb347"/><stop offset=".55" stop-color="#ff7a3d"/><stop offset="1" stop-color="#ff6a2b"/></linearGradient></defs>'
               '<rect x="8" y="4" width="92" height="132" rx="10" fill="#ffb347" opacity=".12"/><rect x="200" y="4" width="76" height="132" rx="10" fill="#ff6a2b" opacity=".18"/>'
               '<text x="14" y="130" font-size="10" fill="#a9a5c4" font-family="system-ui">Hook</text><text x="206" y="130" font-size="10" fill="#a9a5c4" font-family="system-ui">Ad-libs</text>'
               + wave + '</svg>')
    mh = ''.join('<div class="mod" style="--c:%s;--v:%s"><span class="mn">%s</span><span class="knob"></span><span class="leds">%s</span></div>' % (
        c, v, n, ''.join('<i class="on"></i>' if k < round(v * 8) else '<i></i>' for k in range(8))) for n, c, v in mods)
    return ('<div class="rackwrap"><div class="rack" role="img" aria-label="Tunedzy vocal workstation: a waveform with painted sections and six processing modules called Clean, Tune, Fit, Style, Mix and Master">'
            '<div class="rackbar"><span class="dts"><i></i><i></i><i></i></span><b>Tunedzy</b><em>Vocal Workstation</em></div>'
            f'<div class="rwave">{wavesvg}</div><div class="mods">{mh}</div></div>'
            '<div class="fchip fc1"><i></i>92 BPM &middot; A minor</div><div class="fchip fc2"><i></i>Noise &minus;62 dB</div>'
            '<div class="fchip fc3"><i></i>&minus;14.0 LUFS</div><div class="fchip fc4"><i></i>True peak &minus;1.1 dB</div>'
            '<p class="rcap">Example session</p></div>')


# ---------------------------------------------------------------------------------------------------- pages
def plan_card(key, hot=False):
    pr = C.PRICES[key]
    per = f'<small> {pr["per"]}</small>' if pr.get('per') else '<small> once</small>'
    return f'<div class="plan{" hot" if hot else ""}"><span class="tag">{e(pr["label"])}</span><div class="pr">${pr["usd"]}{per}</div><ul><li>{e(pr["note"])}</li></ul></div>'


def pricing_summary():
    return f'''<section id="pricing">{shapes('hero')}<div class="wrap"><p class="eyebrow c">Pricing</p><h2 class="c">Free to start. <span class="grad">Pay only for more.</span></h2><p class="sub2">Everything is free to look at. Using it takes a credit, and a credit covers 24 hours of Tunedzy and Streamdzy. No watermark, no per-export fees.</p>
<div class="pricegrid three"><div class="plan hot"><span class="tag">Free credits</span><div class="pr">$0</div><ul><li>At least 30 credits in your first month</li><li>About 12 free credits a month after that</li><li>Invite friends and you both get credits</li><li>Tunedzy Go on your phone is always free</li></ul><div class="cta">{cta_primary()}</div></div>
<div class="plan"><span class="tag">Credit packs</span><div class="pr">$0.99<small> for 8</small></div><ul><li>20 credits for $2.49</li><li>Credits never expire</li><li>Your first pack counts double</li></ul><div class="cta"><a class="btn" href="{C.BASE}/pricing">See all prices</a></div></div>
<div class="plan"><span class="tag">No counting</span><div class="pr">$1.99<small> a month</small></div><ul><li>$8.99 for 6 months, $13.99 a year</li><li>Or unlimited for 30 days for $0.99 (once)</li><li>The same account works in Streamdzy</li></ul><div class="cta"><a class="btn" href="{C.BASE}/pricing">See all prices</a></div></div></div></div></section>'''


PRICING_FAQ = [
    ('What is a credit?', 'A credit pays for 24 hours of use of both Tunedzy and Streamdzy. The first time you use the app in a day it takes one credit, and then everything is open until the 24 hours end, however little or much you do. Looking around costs nothing.'),
    ('What do I get for free?', 'Your first month gives at least 30 credits: you start with a pass of 14 to 30, and if you run out, another arrives a day later (up to three) until the month has paid 30 in all. After that you get a monthly pass of 2 to 12 credits, and if you still run out, a small weekly pass of 1 to 3 credits seven days later (at most three a month). Someone who uses the app every day receives about 43 credits in the first 50 days.'),
    ('How is it the same as Streamdzy?', 'It is one Fuidzy account. Make a login (a name and a PIN) in either app and sign in with it in the other: the credits, the passes and the 24-hour window are shared. One PC gets one welcome month across both apps.'),
    ('Do credits expire?', 'Credits you buy never expire. Free passes belong to the month they are given. Plans last for the period you paid for.'),
    ('Do I need an account to try it?', 'No. An anonymous account is made in the background the first time a credit is needed. You need a login to buy, to invite friends and to use your credits on another PC (up to five).'),
    ('I have an old lifetime key.', 'It still unlocks everything, forever, with no credits. It is no longer sold.'),
    ('What if I cannot reach the internet?', 'If the credit server cannot be reached and it never said you were out of credits, your work goes on. A bad connection never stops you.'),
    ('Can I get a refund?', 'Yes, within 30 days of a purchase. See the <a href="/tunedzy/refund-policy">refund policy</a>.'),
    ('Who takes the payment?', 'Dodo Payments. We never see your card details.'),
]


def pricing_page():
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('Tunedzy', C.BASE), ('Pricing', f'{C.BASE}/pricing')])
    every = ''.join(f'<li>{e(x)}</li>' for x in C.EVERYTHING)
    how = ''.join(f'<li>{e(x)}</li>' for x in C.HOW_CREDITS)
    body = f'''<main><div class="hero" style="padding:0 0 30px">{shapes('hero')}<div class="wrap">{crumbs_html}<div class="toolhead"><h1>Free to start. <em class="grad">Pay only for more.</em></h1>
<p class="lead">Everything in Tunedzy is free to look at. Using it takes a credit, and a credit covers 24 hours. You get free credits every month, and you can buy more, or take a plan with no counting. Tunedzy and Streamdzy share one account and one pool of credits.</p></div></div></div>
<section style="padding-top:10px"><div class="wrap"><div class="pricegrid three"><div class="plan hot"><span class="tag">Free credits</span><div class="pr">$0</div><ul><li>At least 30 credits in your first month</li><li>About 12 free credits a month after that</li><li>Invite friends: 7 to 20 credits each, for both of you</li><li>Tunedzy Go on your phone is always free</li></ul><div class="cta">{cta_primary()}</div></div>
{plan_card('first30')}{plan_card('pack8')}{plan_card('pack20')}{plan_card('monthly')}{plan_card('half')}{plan_card('year')}</div>
<p class="note c" style="margin-top:18px">Prices in US dollars. Taxes may be added at checkout. You buy in the app (Credits screen), so the credits land on your account at once.</p></div></section>
<section class="alt"><div class="narrow"><h2>How credits work</h2><ol>{how}</ol>
<h2>Everything is included</h2><p>There is no feature that costs extra. A credit opens all of this:</p><ul>{every}</ul>
<p class="note">Looking at the Credits screen costs nothing, and neither does Tunedzy Go or any free tool on this site. The numbers above are the ones the account server really uses; the server owns the rules, so what you see in the app is always right.</p></div></section>
<section><div class="narrow"><h2>Questions about credits</h2>{faq_html(PRICING_FAQ)}</div></section></main>'''
    return layout(title='Tunedzy Pricing: Free Credits Every Month, Packs from $0.99', desc='Tunedzy is free to look at. A credit covers 24 hours. 30 free credits in your first month, about 12 a month after, packs from $0.99 and plans from $1.99 a month.',
                  path=f'{C.BASE}/pricing', body=body, lds=[faq_ld(PRICING_FAQ), crumbs_ld, software_ld()])


def hub():
    feats = [
        ('clean', 'cA', 'STUDIO SOUND', 'Noise, hum, clicks, clipping and room sound out of any voice recording, with one tap. A small AI model on your own PC keeps the voice natural.'),
        ('mix', 'cB', 'MULTITRACK STUDIO', 'Record and arrange tracks for voices, music and effects. Fades, volume lines, pan, EQ and compression on every track, auto-duck, undo and saved projects.'),
        ('record', 'cV', 'EDIT BY WORDS', 'Write out what was said on your PC, then delete words to cut the audio. Remove ums and long pauses in one click. Captions (SRT, VTT) and chapters come out too.'),
        ('upload', 'cP', 'VIDEO TOO', 'A phone video with bad sound? Fix the sound and put it back into the video. MP4 and MOV in.'),
        ('meter', 'cT', 'LOUDNESS AND MASTERING', 'Match every voice to the same loudness, aim for podcast, YouTube, audiobook or broadcast, and get a pass or fail report on loudness, true peak and tone.'),
        ('tune', 'cO', 'TUNE AND VOCAL TOOLS', 'Autotune in your key, a style learned from a reference song, vocal remover and stems, and key and speed changes.'),
    ]
    new2 = [
        ('mic', 'cA', 'AI NOISE CLEANUP', 'A small neural model removes fans, keyboards and hiss around your words, on top of the learned-room filter. Runs on your own PC.'),
        ('record', 'cV', 'PROFILES FOR EVERY SITUATION', 'Streaming, gaming, calls, podcast, voice-over, radio, ASMR and singing, plus a correction for the mic you actually have.'),
        ('upload', 'cB', 'OBS WITHOUT A CABLE', 'Add one browser source and your cleaned voice appears in the OBS mixer. Discord and Zoom still use a free virtual cable.'),
        ('mix', 'cO', 'CONTROL IT YOUR WAY', 'Hotkeys, Stream Deck buttons and scripts, and an AI-assistant connection (MCP) that can measure, master and change your files.'),
        ('meter', 'cT', 'EFFECTS YOU HEAR AS YOU MOVE THEM', 'Play any file through the live chain, or hear a key and speed change while you drag. Settings apply by themselves; nothing to wait for.'),
        ('karaoke', 'cP', 'VOCAL REMOVER &amp; STEM MIXER', 'Acapella, karaoke and stems from any song, then your own mix with faders, solo and mute. Quick edit trims, cuts and fades with a spectrogram.'),
    ]
    who = [('hero', 'Singers and rappers', 'Recorded on a phone or USB mic and want it to sound finished next to the beat.'),
           ('booth', 'Podcasters and interviewers', 'Several voices into one balanced mix, ums removed, loudness set, captions and chapters out.'),
           ('desk', 'Streamers and video makers', 'A clean, broadcast-sounding voice live, and a phone video with its sound put right.')]
    steps = [('Record or drop in a file', 'Record in Tunedzy or on your phone, or bring any recording or video, however bad.'),
             ('Press Perfect it', 'It repairs clipping, clicks and hum, takes out noise and room sound, levels the voice and sets the tone.'),
             ('Edit, mix and export', 'Cut by words, add tracks and music, check the loudness, and export WAV, FLAC or MP3 (or the video).')]
    tool_cards = ''.join(f'<a class="card {TOOL_COLOR[T.TOOLS[s]["color"]]}" href="{C.BASE}/tools/{s}">{ico(T.TOOLS[s]["icon"], TOOL_COLOR[T.TOOLS[s]["color"]])}<h3>{e(T.TOOLS[s]["short"])}</h3><p>{e(T.TOOLS[s]["blurb"])}</p></a>' for s in T.TOOL_ORDER)
    guides = ''.join(f'<a class="th" href="{C.BASE}/{s}">{img(THUMB.get(GUIDE_PHOTO[s], GUIDE_PHOTO[s]), alt="")}<span><b>{e(C.GUIDES[s]["h1"])}</b><br><span class="small">{e(C.GUIDES[s]["desc"][:96])}&hellip;</span></span></a>' for s in C.GUIDE_ORDER[:6]) + f'<a class="th" href="{C.BASE}/guides"><span><b>All guides and comparisons</b><br><span class="small">How-tos, honest comparisons and alternatives.</span></span></a>'
    status = '' if LAUNCHED else '<p class="small" style="margin-top:14px">Windows download opens at launch. Email us and we will let you know the day it does.</p>'
    body = f'''<main>
<div class="hero">{shapes('hero')}<div class="wrap"><div class="herogrid"><div>
<div class="pill"><i></i>New: Tunedzy 5 &middot; Free credits every month &middot; Windows and phone</div>
<h1>Bad recording in. <em class="grad">Studio sound out.</em></h1>
<p class="sub">The audio studio for voices, podcasts, streams and songs. Record, clean, edit by words, mix and master in one app that runs on your own PC, and fix a take on your phone with Tunedzy Go. Everything except making beats.</p>
<div class="cta">{cta_primary()}<a class="btn" href="{C.GO_URL}">Open Tunedzy Go on your phone</a></div>{status}
<div class="trust"><span>30 free credits in your first month</span><span>Then about 12 free a month</span><span>Nothing is uploaded</span></div></div>
{rack()}</div></div></div>
<section id="try" style="padding-top:40px">{shapes('soft')}<div class="wrap"><p class="eyebrow c">Try it right now</p><h2 class="c">Drop a track. See what it&rsquo;s made of.</h2>
<p class="sub2">Free BPM, key, chords and loudness in seconds, right in your browser. Nothing is uploaded.</p>
<div style="max-width:880px;margin:0 auto">{tool_widget('all')}</div>
<div class="tcards" style="margin-top:30px">{tool_cards}</div></div></section>
<section id="features" class="alt">{shapes('bars')}<div class="wrap"><p class="eyebrow c">The studio</p><h2 class="c">Record it. Fix it. Edit it. Finish it.</h2><p class="sub2">What you would do across a recorder, a noise plugin, an editor, a mixer and a mastering tool, in one window, with live control.</p>
<div class="grid">{''.join(f'<div class="card {c}">{ico(k, c)}<h3>{n}</h3><p>{d}</p></div>' for k, c, n, d in feats)}</div></div></section>
<section id="go"><div class="wrap"><div class="spot"><div class="report"><div class="rh"><b>Tunedzy Go</b><span>on your phone</span></div>
<div class="row"><i></i>Record audio or video<span>or pick a file</span></div><div class="row"><i></i>Studio sound (AI)<span>on the phone</span></div><div class="row"><i></i>Before and after<span>tap to compare</span></div>
<div class="row"><i></i>Share or save<span>audio or video</span></div><div class="row"><i></i>After the first visit<span>works offline</span></div><p class="rn">Free. A web app: nothing to install from a store.</p></div>
<div><p class="eyebrow">Tunedzy Go</p><h2>Fix it right where you <span class="grad">recorded it.</span></h2>
<p style="color:#f0dfd8">Open it in your phone&rsquo;s browser and add it to your home screen. Record a voice note or a video, or pick one from your phone, and it comes back sounding like a studio: noise and room sound taken out, the level evened out, the tone set. Your recording never leaves the phone.</p>
<ul><li>Free, with no sign-up</li><li>Same voice engine as the desktop app</li><li>Works without a connection after the first visit (Studio sound downloads a 22 MB model once)</li></ul>
<div class="cta"><a class="btn primary" href="{C.GO_URL}">Open Tunedzy Go</a></div></div></div></div></section>
<section id="new" class="alt">{shapes('soft')}<div class="wrap"><p class="eyebrow c">For streamers and creators</p><h2 class="c">From your mic to the master. <span class="grad">One app.</span></h2><p class="sub2">The tools creators search for most, built in and running on your own PC.</p>
<div class="grid">{''.join(f'<div class="card {c}">{ico(k, c)}<h3>{n}</h3><p>{d}</p></div>' for k, c, n, d in new2)}</div></div></section>
<section><div class="wrap"><div class="spot"><div><p class="eyebrow">Studio-ready checks</p><h2>Know it&rsquo;s ready <span class="grad">before you post.</span></h2>
<p style="color:#f0dfd8">Every export comes with a pass/fail report so you are not guessing: loudness, true peak, tone balance, noise, clipping and more. Fix what&rsquo;s flagged with one slider, then export 24-bit WAV or FLAC for your DAW, your distributor or your socials.</p>
<ul><li>Works next to any DAW: export a finished vocal and drop it in</li><li>Live sliders and XY pads, with changes you hear instantly</li><li>Your original take is never overwritten</li></ul></div>
<div class="report"><div class="rh"><b>Studio-ready report</b><span>All checks pass</span></div>
<div class="row"><i></i>Loudness<span>&minus;14.0 LUFS</span></div><div class="row"><i></i>True peak<span>&minus;1.1 dBTP</span></div><div class="row"><i></i>Noise floor<span>&minus;62 dB</span></div>
<div class="row"><i></i>Clipping<span>none</span></div><div class="row"><i></i>Tonal balance<span>in range</span></div><div class="row"><i></i>Vocal vs beat<span>balanced</span></div><p class="rn">Example report. Real numbers depend on your track.</p></div></div></div></section>
<section class="alt">{shapes('soft')}<div class="wrap"><div class="spot"><div class="photo" style="max-width:430px;margin:0 auto">{img('neon')}</div><div>
<p class="eyebrow">Sound like the records you love</p><h2>Drop in a song. <span class="grad">Get that treatment on your voice.</span></h2>
<p style="color:#f0dfd8">Pick any track by an artist whose sound you want. Tunedzy measures how that vocal was tuned, brightened, spaced, doubled and compressed, then applies a similar treatment to <em>your</em> recording.</p>
<ul><li>Learns the autotune style: natural, modern or hard-snapped</li><li>Matches tone, reverb size, width and how tight the flow sits on the beat</li><li>Keeps your voice yours: it changes the processing, not who you are</li><li>Saves each style so you can reuse it on the next song</li></ul>
<p class="note">Not affiliated with or endorsed by any artist. Artist names are used only to describe styles of processing.</p></div></div></div></section>
<section><div class="wrap"><div class="band">{img('mic-wide', alt='')}<div class="in"><p class="eyebrow">Private by design</p><h2>Your unreleased songs <span class="grad">never leave your PC.</span></h2>
<p>Tunedzy processes everything locally. No uploads, no per-minute limits, no watermarks. The only internet use is counting your credits, updates, and the optional AI model downloads. Tunedzy Go and the free tools on this site work the same way, inside your browser.</p></div></div></div></section>
<section class="alt">{shapes('bars')}<div class="wrap"><p class="eyebrow c">How it works</p><h2 class="c">Three steps</h2><div class="steps" style="margin-top:26px">{''.join(f'<div class="card {c}"><h3>{n}</h3><p>{d}</p></div>' for (n, d), c in zip(steps, ('cA', 'cP', 'cV')))}</div></div></section>
<section><div class="wrap"><p class="eyebrow c">Who it&rsquo;s for</p><h2 class="c">Made for people who record in real rooms</h2><div class="pcards" style="margin-top:26px">{''.join(f'<div class="pcard">{img(k)}<div><h3>{n}</h3><p>{d}</p></div></div>' for k, n, d in who)}</div>
<p class="note" style="margin-top:20px">Honest limits: Tunedzy replaces a DAW for recording, cleaning, editing, mixing and mastering voices, podcasts, streams and vocal songs, but it is not for making beats (no step sequencer, virtual instruments or MIDI composing) and it does not host VST or AU plugins. The DAW pack hands your stems to any DAW. The app to download today is for Windows; Mac and Linux builds are being prepared, and Tunedzy Go runs in any phone or computer browser. Using it as a microphone in Discord, Zoom or games needs a free virtual cable such as VB-Cable (OBS can take it directly, no cable). It can improve a rough recording a lot, but it can&rsquo;t turn a voice buried in echo or heavy distortion into a studio take. Re-recording closer to the mic is always the best fix.</p></div></section>
<section id="guides" class="guides alt">{shapes('soft')}<div class="wrap"><p class="eyebrow c">Free guides</p><h2 class="c">Get better vocals today</h2><p class="sub2">Practical, and useful with or without Tunedzy.</p><div class="related">{guides}</div></div></section>
{pricing_summary()}
<section id="support" class="alt"><div class="wrap"><div class="supportband">{shapes('soft')}<div style="position:relative"><p class="eyebrow">Real people</p><h2>Stuck? Want a Mac version? <span class="grad">Just email us.</span></h2>
<p>Questions, bugs, feature ideas or a Mac request: send a note and we will get back to you. Requests decide what we build next.</p><div class="cta"><a class="btn primary" href="{e(C.HELP_MAIL)}">Email support</a><a class="btn" href="{e(C.MAC_MAIL)}">Request a Mac version</a></div></div>
<div style="position:relative"><div class="mailbig"><a href="{e(C.HELP_MAIL)}">{C.SUPPORT_EMAIL}</a></div><p class="small" style="margin-top:8px">Include what you were doing and a screenshot if you can.</p></div></div></div></section>
<section id="faq"><div class="narrow"><h2 class="c">Questions</h2>{faq_html(C.HUB_FAQ)}</div></section></main>'''
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('Tunedzy', C.BASE)])
    title = 'Tunedzy: Studio Sound for Any Recording, Multitrack Editor and Phone App'
    desc = 'Turn a bad recording into studio sound. AI voice cleanup, multitrack editing, edit by transcript, mastering and a free phone app. Private: nothing is uploaded. Free credits every month.'
    return layout(title=title, desc=desc, path=C.BASE, body=body,
                  lds=[software_ld(), faq_ld(C.HUB_FAQ), crumbs_ld, webapp_ld('', 'Tunedzy free music tools', 'Free BPM, key, chord and loudness finder that runs in your browser.')], scripts=tool_scripts())


def tools_hub():
    t = T.HUB
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('Tunedzy', C.BASE), ('Free tools', f'{C.BASE}/tools')])
    cards = ''.join(f'<a class="card {TOOL_COLOR[T.TOOLS[s]["color"]]}" href="{C.BASE}/tools/{s}">{ico(T.TOOLS[s]["icon"], TOOL_COLOR[T.TOOLS[s]["color"]])}<h3>{e(T.TOOLS[s]["short"])}</h3><p>{e(T.TOOLS[s]["blurb"])}</p></a>' for s in T.TOOL_ORDER)
    body = f'''<main><div class="hero" style="padding:0 0 30px">{shapes('hero')}<div class="wrap">{crumbs_html}<div class="toolhead"><h1>Free music tools that <em class="grad">run in your browser</em></h1><p class="lead">{t['lead']}</p></div>
<div style="max-width:900px">{tool_widget('all')}</div></div></div>
<section style="padding-top:20px">{shapes('soft')}<div class="wrap"><h2 class="c">Pick a tool</h2><p class="sub2">Each one is also available on its own page, with tips and a guide.</p><div class="tcards">{cards}</div></div></section>
<section class="alt"><div class="narrow"><h2>What these tools are for</h2><p>When you record a vocal over a beat, the first questions are always the same: how fast is the beat, what key is it in, what chords are under it, and is my vocal clean and loud enough? These tools answer them in seconds so you can set your project tempo, your autotune scale and your levels before you start mixing.</p>
<p>They are the same kinds of checks <a href="{C.BASE}">Tunedzy</a> runs automatically before it cleans, tunes and masters a rough vocal for you, and your first month comes with free credits.</p></div></section>
<section><div class="narrow"><h2>Questions</h2>{faq_html(t['faq'])}</div></section></main>'''
    return layout(title=t['title'], desc=t['desc'], path=f'{C.BASE}/tools', body=body,
                  lds=[webapp_ld('', 'Tunedzy free music tools', t['desc']), faq_ld(t['faq']), crumbs_ld], scripts=tool_scripts())


def tool_page(slug):
    t = T.TOOLS[slug]
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('Tunedzy', C.BASE), ('Free tools', f'{C.BASE}/tools'), (t['short'], f'{C.BASE}/tools/{slug}')])
    how = ''.join(f'<div>{h}</div>' for h in t['how'])
    rel = ''.join(f'<a class="card {TOOL_COLOR[T.TOOLS[r]["color"]]}" href="{C.BASE}/tools/{r}" style="padding:18px">{ico(T.TOOLS[r]["icon"], TOOL_COLOR[T.TOOLS[r]["color"]])}<h3>{e(T.TOOLS[r]["short"])}</h3><p>{e(T.TOOLS[r]["blurb"])}</p></a>' for r in t['related'])
    gl = ''.join(f'<a href="{C.BASE}/{g}"><b>{e(C.GUIDES[g]["h1"])}</b></a>' for g in t['guide_links'])
    arts = [x for x in B.BLOGS if B.CLUSTERS[x['cluster']]['tool'] == slug]
    articles = ('<h2>Guides for this tool</h2><div class="related">' + ''.join(f'<a href="{C.BASE}/blog/{x["slug"]}"><b>{e(x["h1"])}</b><br><span class="small">{e(x["desc"][:110])}&hellip;</span></a>' for x in arts) + '</div>') if arts else ''
    kind = t.get('kind')
    if kind in ('live', 'karaoke'):
        widget, scripts = live_widget(kind), live_scripts(kind)
    elif kind in ('stream', 'record'):
        widget, scripts = clean_widget(kind), clean_scripts()
    else:
        widget, scripts = tool_widget(t['focus'], tap=t['tap']), tool_scripts()
    action = (f'<a class="btn primary" href="{e(DOWNLOAD)}" rel="noopener">Download Tunedzy</a>' if LAUNCHED
              else f'<a class="btn primary" href="{C.BASE}">See Tunedzy</a>')
    body = f'''<main><div class="hero" style="padding:0 0 30px">{shapes('soft')}<div class="wrap">{crumbs_html}<div class="toolhead"><h1>{t['h1']}</h1><p class="lead">{t['lead']}</p></div>
<div style="max-width:900px">{widget}</div><div class="howto" style="max-width:900px">{how}</div></div></div>
<div class="narrow"><article>{t['body']}
<div class="vf"><h2>Like this? Let Tunedzy do the fixing.</h2><p>These tools tell you what is going on. Tunedzy acts on it: it cleans, tunes to your beat&rsquo;s key, fits the flow, matches an artist&rsquo;s style and masters the result on your own PC. Your first month comes with free credits.</p><div class="cta">{action}<a class="btn" href="{e(C.HELP_MAIL)}">Ask us a question</a></div></div>
<h2>Frequently asked questions</h2>{faq_html(t['faq'])}
{articles}<h2>More free tools</h2><div class="tcards">{rel}</div>
<h2>Related guides</h2><div class="related">{gl}</div></article></div></main>'''
    return layout(title=t['title'], desc=t['desc'], path=f'{C.BASE}/tools/{slug}', body=body,
                  lds=[webapp_ld(slug, t['short'], t['desc']), faq_ld(t['faq']), crumbs_ld], scripts=scripts)


def guide(slug):
    g = C.GUIDES[slug]
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('Tunedzy', C.BASE), (g['h1'], f'{C.BASE}/{slug}')])
    rel = ''.join(f'<a class="th" href="{C.BASE}/{r}">{img(THUMB.get(GUIDE_PHOTO[r], GUIDE_PHOTO[r]), alt="")}<span><b>{e(C.GUIDES[r]["h1"])}</b></span></a>' for r in g['related'])
    tools = ''.join(f'<a href="{C.BASE}/tools/{s}"><b>{e(T.TOOLS[s]["short"])}</b><br><span class="small">{e(T.TOOLS[s]["blurb"])}</span></a>' for s in GUIDE_TOOLS[slug])
    pk = GUIDE_PHOTO[slug]
    banner = f'<div class="banner">{img(pk if pk.endswith("wide") else (pk + "-wide" if pk + "-wide" in PHOTOS else pk), eager=True)}</div>'
    tl = ''.join(f'<li>{t}</li>' for t in g['tldr'])
    ai = g.get('ai')
    ai_html = f'<div class="aibox"><h2>{ai[0]}</h2>{ai[1]}</div>' if ai else ''
    buy = (f'<a class="btn primary" href="{e(DOWNLOAD)}" rel="noopener">Download Tunedzy</a>' if LAUNCHED else f'<a class="btn primary" href="{C.BASE}/pricing">See pricing</a>')
    action = f'<p>{buy} <a class="btn" href="{C.GO_URL}">Try it on your phone, free</a></p>'
    article_ld = {'@context': 'https://schema.org', '@type': 'Article', 'headline': g['h1'], 'description': g['desc'], 'datePublished': C.DATE, 'dateModified': C.DATE,
                  'image': C.SITE + C.BASE + '/og.png', 'mainEntityOfPage': C.SITE + f'{C.BASE}/{slug}',
                  'author': {'@type': 'Organization', 'name': 'Fuidzy'}, 'publisher': {'@type': 'Organization', 'name': 'Fuidzy', 'url': C.SITE}}
    body = f'''<main><div class="hero" style="padding:0 0 10px">{shapes('soft')}<div class="narrow"><article>{crumbs_html}<h1>{g['h1']}</h1><p class="note">Updated October 2026</p><p class="lead">{g['lead']}</p>{banner}</article></div></div>
<div class="narrow"><article><div class="tldr"><b>The short version</b><ul>{tl}</ul></div>{g['body'].replace('<table>', '<div class="tablewrap"><table>').replace('</table>', '</table></div>')}{ai_html}
<div class="vf"><h2>{g['vf_title']}</h2>{g['vf']}{action}</div>
<h2>Free tools for this</h2><div class="related">{tools}</div>
<h2>Frequently asked questions</h2>{faq_html(g['faq'])}
<h2>Keep going</h2><div class="related">{rel}</div><p><a href="{C.BASE}/guides">All guides and comparisons</a> &middot; <a href="{C.GO_URL}">Tunedzy Go on your phone</a> &middot; <a href="{C.BASE}/pricing">Pricing</a></p></article></div></main>'''
    return layout(title=g['title'], desc=g['desc'], path=f'{C.BASE}/{slug}', body=body, lds=[article_ld, faq_ld(g['faq']), crumbs_ld], og_type='article')


def guides_hub():
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('Tunedzy', C.BASE), ('Guides', f'{C.BASE}/guides')])

    def cards(slugs):
        return ''.join(f'<a class="th" href="{C.BASE}/{s}">{img(THUMB.get(GUIDE_PHOTO[s], GUIDE_PHOTO[s]), alt="")}<span><b>{e(C.GUIDES[s]["h1"])}</b><br><span class="small">{e(C.GUIDES[s]["desc"][:110])}&hellip;</span></span></a>' for s in slugs)
    how = [s for s in C.GUIDE_ORDER if s not in C.COMPARE_SLUGS]
    body = (f'<main><div class="hero" style="padding:0 0 10px">{shapes("soft")}<div class="wrap">{crumbs_html}<div class="toolhead"><h1>Audio guides, comparisons and how-tos</h1>'
            '<p class="lead">Practical steps for cleaning a voice, fixing a recording and getting a finished sound, on a phone or a PC. Each guide says what works without any tool, and where Tunedzy helps.</p></div></div></div>'
            f'<section><div class="wrap"><h2>How to</h2><div class="related">{cards(how)}</div></div></section>'
            f'<section class="alt"><div class="wrap"><h2>Compare</h2><p class="sub2" style="text-align:left;margin:0 0 18px">Honest comparisons: where each tool is the better choice, and the cases where Tunedzy is.</p><div class="related">{cards(C.COMPARE_SLUGS)}</div></div></section>'
            f'<section><div class="narrow"><h2>Free and on your phone</h2><p>Tunedzy Go cleans a recording on your phone for free. The free tools on this site (LUFS meter, vocal checker, key and BPM finders) run in your browser. <a href="{C.GO_URL}">Open Tunedzy Go</a> &middot; <a href="{C.BASE}/tools">All free tools</a> &middot; <a href="{C.BASE}/pricing">Pricing</a></p></div></section></main>')
    return layout(title='Audio Guides and Comparisons: Clean Voice, Noise, Loudness', desc='Free audio guides: clean a phone voice recording, remove noise and hum, fix clipping, set loudness, and honest comparisons of voice cleaners.', path=f'{C.BASE}/guides', body=body, lds=[crumbs_ld])


# ---------------------------------------------------------------------------------------------------- blog (SEO articles for the tools)
def blog_by_slug():
    return {b['slug']: b for b in B.BLOGS}


def blog_related(b):
    same = [x for x in B.BLOGS if x['cluster'] == b['cluster']]
    i = same.index(b)
    rel = [same[(i + k) % len(same)] for k in (1, 2, 3)]
    return [r for r in rel if r is not b]


def blog_page(b):
    cl = B.CLUSTERS[b['cluster']]
    tool = T.TOOLS[cl['tool']]
    path = f"{C.BASE}/blog/{b['slug']}"
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('Tunedzy', C.BASE), ('Blog', f'{C.BASE}/blog'), (b['h1'], path)])
    rel = ''.join(f'<a href="{C.BASE}/blog/{r["slug"]}"><b>{e(r["h1"])}</b><br><span class="small">{e(r["desc"][:110])}&hellip;</span></a>' for r in blog_related(b))
    article_ld = {'@context': 'https://schema.org', '@type': 'Article', 'headline': b['h1'], 'description': b['desc'], 'datePublished': C.DATE, 'dateModified': C.DATE,
                  'image': C.SITE + C.BASE + '/og.png', 'mainEntityOfPage': C.SITE + path, 'keywords': b['kw'],
                  'author': {'@type': 'Organization', 'name': 'Fuidzy'}, 'publisher': {'@type': 'Organization', 'name': 'Fuidzy', 'url': C.SITE}}
    action = (f'<a class="btn" href="{e(DOWNLOAD)}" rel="noopener">Get the Tunedzy app</a>' if LAUNCHED else f'<a class="btn" href="{C.BASE}">See Tunedzy</a>')
    body = f'''<main><div class="hero" style="padding:0 0 10px">{shapes('soft')}<div class="narrow"><article>{crumbs_html}<h1>{b['h1']}</h1><p class="note">Updated October 2026 &middot; {e(cl['label'])}</p>
<div class="tldr"><b>Quick answer</b><p style="margin:6px 0 10px">{b['answer']}</p></div></article></div></div>
<div class="narrow"><article>{b['body']}
<div class="vf"><h2>Try it free: {e(tool['short'])}</h2><p>{e(tool['blurb'])} Runs in your browser, nothing is uploaded.</p><div class="cta"><a class="btn primary" href="{C.BASE}/tools/{cl['tool']}">Open the free tool</a>{action}</div></div>
<h2>Frequently asked questions</h2>{faq_html(b['faq'])}
<h2>Keep reading</h2><div class="related">{rel}</div></article></div></main>'''
    return layout(title=b['title'], desc=b['desc'], path=path, body=body, lds=[article_ld, faq_ld(b['faq']), crumbs_ld], og_type='article')


def blog_index():
    crumbs_html, crumbs_ld = breadcrumbs([('Fuidzy', '/'), ('Tunedzy', C.BASE), ('Blog', f'{C.BASE}/blog')])
    secs = ''
    for key, cl in B.CLUSTERS.items():
        items = [x for x in B.BLOGS if x['cluster'] == key]
        cards = ''.join(f'<a href="{C.BASE}/blog/{x["slug"]}"><b>{e(x["h1"])}</b><br><span class="small">{e(x["desc"][:120])}&hellip;</span></a>' for x in items)
        secs += f'<section style="padding:26px 0"><div class="wrap"><h2>{e(cl["label"])}</h2><p class="sub2" style="text-align:left;margin:0 0 18px">Free tool: <a href="{C.BASE}/tools/{cl["tool"]}">{e(cl["tool_name"])}</a></p><div class="related">{cards}</div></div></section>'
    body = (f'<main><div class="hero" style="padding:0 0 10px">{shapes("soft")}<div class="wrap">{crumbs_html}<div class="toolhead"><h1>Audio Guides: Clean Mics, Noise Removal and Recording</h1>'
            '<p class="lead">Practical, step-by-step guides for streamers, creators and voice-over artists: remove background noise, set up your mic, and record clean audio. Each guide links to a free tool that runs in your browser.</p></div></div></div>' + secs + '</main>')
    desc = 'Step-by-step audio guides for streamers and creators: remove mic noise in OBS, set up a virtual audio cable, record clean voice-overs and set the right loudness.'
    return layout(title='Audio Guides: Mic Noise, Streaming and Voice Recording', desc=desc, path=f'{C.BASE}/blog', body=body, lds=[crumbs_ld])


def policy(slug):
    p = C.POLICIES[slug]
    body = f'<main><div class="narrow"><article><h1>{p["h1"]}</h1>{p["body"]}</article></div></main>'
    return layout(title=p['title'], desc=p['desc'], path=f'{C.BASE}/{slug}', body=body, lds=[])


def thanks():
    body = f'''<main><div class="narrow"><article><h1>Thank you</h1>
<p class="lead">Your credits or plan are added to your Fuidzy account as soon as the payment clears, usually within a minute.</p>
<h2>See them in the app</h2><ol><li>Open Tunedzy (or Streamdzy: the account and the credits are shared).</li><li>Open <strong>Credits</strong>. If the new credits are not there yet, wait a moment and open it again.</li></ol>
<p>Bought a pack or a plan with a different login than the one in the app? Sign in with the same login in the app first. Questions or a refund: <a href="{e(C.HELP_MAIL)}">{C.SUPPORT_EMAIL}</a>.</p></article></div></main>'''
    return layout(title='Thanks: your credits are on the way', desc='Where to find your Tunedzy credits after a purchase.', path=f'{C.BASE}/thanks', body=body, lds=[], robots='noindex,nofollow')


# ---------------------------------------------------------------------------------------------------- write everything
def write(rel, text):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')


def og():
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1200, 630
    img_ = Image.new('RGB', (W, H), (20, 10, 20))
    d = ImageDraw.Draw(img_, 'RGBA')
    for cx, cy, r, col in ((980, 80, 420, (255, 122, 61)), (140, 120, 380, (232, 93, 31)), (700, 700, 340, (255, 193, 94))):
        for k in range(r, 0, -8):
            a = int(46 * (1 - k / r) ** 1.6)
            d.ellipse([cx - k, cy - k, cx + k, cy + k], fill=col + (a,))
    d.ellipse([860, 60, 1160, 360], outline=(255, 179, 71, 110), width=3)
    d.rounded_rectangle([90, 470, 190, 570], radius=26, outline=(255, 255, 255, 60), width=2)
    def font(name, size):                       # Segoe UI on Windows; DejaVu Sans elsewhere (Linux build machines)
        for f in (f'C:/Windows/Fonts/{name}.ttf', '/usr/share/fonts/truetype/dejavu/' + ('DejaVuSans-Bold.ttf' if name.endswith('b') else 'DejaVuSans.ttf')):
            try:
                return ImageFont.truetype(f, size)
            except OSError:
                pass
        return ImageFont.load_default()
    bold, reg, small = font('segoeuib', 78), font('segoeui', 34), font('segoeuib', 30)
    icon = Image.open(ROOT / 'assets' / 'icon.png').convert('RGBA').resize((92, 92))
    img_.paste(icon, (70, 62), icon)
    d.text((180, 78), 'Tunedzy 5', font=small, fill=(243, 233, 226))
    d.text((70, 200), 'Rough vocal in.', font=bold, fill=(243, 233, 226))
    d.text((70, 292), 'Finished track out.', font=bold, fill=(255, 150, 120))
    d.text((70, 430), 'Vocal workstation for Windows.', font=reg, fill=(212, 190, 186))
    d.text((70, 476), 'Free credits every month.', font=reg, fill=(212, 190, 186))
    for i, h in enumerate([30, 54, 86, 64, 100, 70, 44, 78, 50, 28]):
        x = 800 + i * 36
        d.rounded_rectangle([x, 450 - h, x + 18, 450 + h], radius=9, fill=(255, 193 - i * 12, 94 - i * 2))
    img_.save(OUT / 'og.png', optimize=True)


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True)
    process_photos()
    shutil.copy2(ROOT / 'assets' / 'icon.png', OUT / 'favicon.png')
    og()
    write('index.html', hub())
    for s in C.GUIDE_ORDER:
        write(f'{s}/index.html', guide(s))
    write('tools/index.html', tools_hub())
    for s in T.TOOL_ORDER:
        write(f'tools/{s}/index.html', tool_page(s))
    for s in C.POLICIES:
        write(f'{s}/index.html', policy(s))
    write('blog/index.html', blog_index())
    for b in B.BLOGS:
        write(f"blog/{b['slug']}/index.html", blog_page(b))
    write('thanks/index.html', thanks())
    write('pricing/index.html', pricing_page())
    write('guides/index.html', guides_hub())
    if args.go:
        shutil.copytree(args.go, OUT / 'go')
    urls = ([(C.BASE, '1.0'), (f'{C.BASE}/pricing', '0.9'), (C.BASE + '/go/', '0.8'), (f'{C.BASE}/tools', '0.9')] + [(f'{C.BASE}/tools/{s}', '0.9') for s in T.TOOL_ORDER]
            + [(f'{C.BASE}/blog', '0.7')] + [(f"{C.BASE}/blog/{b['slug']}", '0.7') for b in B.BLOGS]
            + [(f'{C.BASE}/{s}', '0.8') for s in C.GUIDE_ORDER] + [(f'{C.BASE}/guides', '0.9'), (f'{C.BASE}/pricing', '0.9')] + [(f'{C.BASE}/{s}', '0.3') for s in C.POLICIES])
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        f'  <url><loc>{C.SITE}{u}</loc><lastmod>{C.DATE}</lastmod><priority>{p}</priority></url>\n' for u, p in urls) + '</urlset>\n'
    (ROOT / 'tunedzy-sitemap.xml').write_text(sm, encoding='utf-8')
    slugs = list(C.GUIDE_ORDER) + ['guides', 'tools'] + [f'tools/{s}' for s in T.TOOL_ORDER] + ['blog'] + [f"blog/{b['slug']}" for b in B.BLOGS] + ['thanks', 'pricing'] + list(C.POLICIES)
    (ROOT / 'worker-pages.json').write_text(json.dumps(slugs), encoding='utf-8')
    print(f'built {len(urls) + 1} pages ({"LAUNCHED" if LAUNCHED else "pre-launch"}) -> {OUT}')


if __name__ == '__main__':
    main()
