"""Check the built blog pages: every post has a page, a title, FAQ markup, no double-escaped entities, and every
internal /tunedzy/ link points at a built file.

  python tools/check_pages.py       run after python build.py; exits 1 when anything is wrong
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import content_blog as B  # noqa: E402

TUNE = ROOT / 'tunedzy'
problems = []
checked = 0
for b in B.BLOGS:
    page = TUNE / 'blog' / b['slug'] / 'index.html'
    if not page.exists():
        problems.append(f'missing page: {b["slug"]}')
        continue
    checked += 1
    html = page.read_text(encoding='utf-8')
    if not re.search(r'<title>[^<]{10,}</title>', html):
        problems.append(f'{b["slug"]}: no title')
    if '&amp;rsquo' in html or '&amp;amp;' in html or '&amp;ldquo' in html:
        problems.append(f'{b["slug"]}: double-escaped entity')
    if html.count('"@type": "Question"') + html.count('"@type":"Question"') == 0 and b.get('faq'):
        problems.append(f'{b["slug"]}: no FAQ schema')
    for href in set(re.findall(r'href="(/tunedzy/[^"#?]*)"', html)):
        path = href[len('/tunedzy/'):].rstrip('/')
        if path == '' or path.startswith('go'):
            continue
        if not any(c.is_file() for c in (TUNE / path / 'index.html', TUNE / (path + '.html'), TUNE / path)):
            problems.append(f'{b["slug"]}: broken link {href}')
print('pages checked:', checked, 'of', len(B.BLOGS))
print('problems:', len(problems))
for p in problems[:40]:
    print('  -', p)
sys.exit(1 if problems else 0)
