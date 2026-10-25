"""Cover artwork for blog posts: one generated picture per post, drawn from the post's own slug.

Each cover is an inline SVG built from a seeded random generator, so a rebuild gives the same picture, while
every post gets its own composition. Posts in the same cluster share a colour family.
"""
import hashlib
import math
import random

W, H = 1600, 640

COVER_CSS = (
    '.cover-art{margin:0 0 30px;border-radius:18px;overflow:hidden;border:1px solid var(--line);background:#100b18}'
    '.cover-art svg{display:block;width:100%;height:auto}'
    '.related a.th svg.cover-th{display:block;width:100%;height:130px}'
)


def _seed(text):
    return int(hashlib.sha256(text.encode('utf-8')).hexdigest()[:12], 16)


def cover_svg(slug, cluster, cls='cover-img'):
    rnd = random.Random(_seed(slug))
    hue = (random.Random(_seed('family:' + cluster)).uniform(0, 360) + rnd.uniform(-40, 40)) % 360
    hue2 = (hue + rnd.choice([-60, -35, 35, 60, 120, 180])) % 360
    uid = 'c' + format(_seed(slug + ':id') % 0xFFFFFF, '06x')
    cx = rnd.uniform(0.25, 0.75) * W
    cy = rnd.uniform(0.3, 0.7) * H
    glow = rnd.uniform(0.35, 0.6)

    parts = [
        f'<defs><linearGradient id="{uid}g" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="hsl({hue:.0f},60%,20%)"/>'
        f'<stop offset="1" stop-color="hsl({hue2:.0f},55%,10%)"/></linearGradient>'
        f'<radialGradient id="{uid}r" cx="{cx / W:.3f}" cy="{cy / H:.3f}" r="{glow:.3f}">'
        f'<stop offset="0" stop-color="hsl({hue:.0f},85%,62%)" stop-opacity=".55"/>'
        f'<stop offset="1" stop-color="hsl({hue:.0f},85%,62%)" stop-opacity="0"/></radialGradient></defs>',
        f'<rect width="{W}" height="{H}" fill="url(#{uid}g)"/>',
        f'<rect width="{W}" height="{H}" fill="url(#{uid}r)"/>',
    ]

    for i in range(rnd.randint(3, 6)):
        r = 60 + i * rnd.uniform(60, 120)
        parts.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="none" stroke="#fff" '
                     f'stroke-opacity="{rnd.uniform(0.08, 0.22):.2f}" stroke-width="{rnd.uniform(1.5, 3):.1f}"/>')

    envelope = rnd.uniform(0.3, 0.7)
    for k in range(rnd.randint(3, 5)):
        amp = rnd.uniform(60, 190)
        freq = rnd.uniform(1.5, 7)
        phase = rnd.uniform(0, 2 * math.pi)
        spread = rnd.uniform(0.6, 1.3)
        pts = []
        for x in range(0, W + 1, 8):
            t = x / W
            env = math.exp(-((t - envelope) ** 2) / (2 * (0.18 * spread) ** 2))
            y = cy + amp * env * math.sin(2 * math.pi * freq * t + phase + k * 0.6)
            pts.append(f'{x} {y:.1f}')
        col = hue if k % 2 == 0 else hue2
        parts.append(f'<path d="M{" L".join(pts)}" fill="none" stroke="hsl({col:.0f},80%,72%)" '
                     f'stroke-opacity="{rnd.uniform(0.5, 0.9):.2f}" stroke-width="{rnd.uniform(2, 4.5):.1f}" '
                     f'stroke-linecap="round"/>')

    bars = rnd.randint(30, 52)
    bw = W / bars
    level = rnd.uniform(0.2, 0.5)
    for i in range(bars):
        level = min(0.95, max(0.08, level + rnd.uniform(-0.25, 0.25)))
        bh = level * 150
        parts.append(f'<rect x="{i * bw + bw * 0.2:.1f}" y="{H - 40 - bh:.1f}" width="{bw * 0.6:.1f}" '
                     f'height="{bh:.1f}" rx="4" fill="#fff" fill-opacity=".16"/>')

    if rnd.random() < 0.5:
        parts.append(f'<circle cx="{rnd.uniform(0.1, 0.9) * W:.0f}" cy="{rnd.uniform(0.1, 0.5) * H:.0f}" '
                     f'r="{rnd.uniform(18, 46):.0f}" fill="hsl({hue2:.0f},85%,70%)" fill-opacity=".8"/>')
    else:
        parts.append(f'<rect x="{rnd.uniform(0.1, 0.8) * W:.0f}" y="{rnd.uniform(0.1, 0.4) * H:.0f}" '
                     f'width="{rnd.uniform(40, 90):.0f}" height="{rnd.uniform(40, 90):.0f}" rx="12" '
                     f'transform="rotate({rnd.uniform(-30, 30):.0f})" fill="none" '
                     f'stroke="hsl({hue:.0f},85%,72%)" stroke-width="3" stroke-opacity=".7"/>')

    return (f'<svg class="{cls}" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" '
            f'aria-hidden="true" focusable="false">' + ''.join(parts) + '</svg>')
