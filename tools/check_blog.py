"""Check the blog posts before a build: schema, unique slugs/titles/kw, cluster and tool links, internal links,
entity leaks, title and description lengths, and the 800-word floor for every post outside the first 139.

  python tools/check_blog.py        exits 1 when anything is wrong
"""
import re
import sys
from collections import Counter
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import content as C  # noqa: E402
import content_tools as T  # noqa: E402
import content_blog as B  # noqa: E402

REQUIRED = ('slug', 'cluster', 'kw', 'title', 'desc', 'h1', 'answer', 'body', 'faq')
problems = []
guide_slugs = set(C.GUIDES)
blog_slugs = {b['slug'] for b in B.BLOGS}
policy_slugs = set(getattr(C, 'POLICIES', {}) or {})
static = {'guides', 'pricing', 'blog', 'tools', 'thanks', 'go', 'go/'}
# The first 139 posts (39 original + 100 added on 2026-10-25) were written before the 800-word rule.
LEGACY = {'stream', 'record', 'vocal', 'compare', 'artist', 'music', 'podcast', 'voiceover', 'loudness', 'repair',
          'phone', 'video', 'singing', 'workflow', 'gear', 'ai'}
GUIDE_KWS = {(g.get('kw') or '').lower() for g in C.GUIDES.values()}


def text_of(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return ' '.join(unescape(s).split())


def check_link(where, href):
    if not href.startswith('/tunedzy'):
        return
    path = href[len('/tunedzy'):].lstrip('/').rstrip('/')
    ok = (path in guide_slugs or path in static or path in policy_slugs
          or (path.startswith('tools/') and path[6:] in T.TOOLS)
          or (path.startswith('blog/') and path[5:] in blog_slugs)
          or path.startswith('go'))
    if not ok:
        problems.append(f'{where}: unknown internal link {href}')


for label, counter in (('slug', Counter(b.get('slug') for b in B.BLOGS)),
                       ('title', Counter(b.get('title') for b in B.BLOGS)),
                       ('kw', Counter((b.get('kw') or '').lower() for b in B.BLOGS))):
    for value, n in counter.items():
        if n > 1:
            problems.append(f'duplicate {label}: {value} x{n}')

counts = []
for b in B.BLOGS:
    slug = b.get('slug', '?')
    for key in REQUIRED:
        if not b.get(key):
            problems.append(f'{slug}: missing {key}')
    if b.get('cluster') not in B.CLUSTERS:
        problems.append(f'{slug}: unknown cluster {b.get("cluster")}')
    cl = B.CLUSTERS.get(b.get('cluster'), {})
    if cl and cl.get('tool') not in T.TOOLS:
        problems.append(f'{slug}: cluster tool {cl.get("tool")} not in TOOLS')
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', slug):
        problems.append(f'{slug}: slug not kebab-case')
    if slug in C.GUIDES:
        problems.append(f'{slug}: slug collides with a guide')
    for field in ('title', 'desc', 'h1', 'answer', 'body'):
        val = b.get(field, '')
        if "'''" in val:
            problems.append(f'{slug}: triple quote in {field}')
        if re.search(r'&amp;(?:[a-z]+;|#)|&#\d+;?[a-z]', val):
            problems.append(f'{slug}: suspicious entity in {field}')
    if len(b.get('title', '')) > 70:
        problems.append(f'{slug}: title over 70 chars ({len(b["title"])})')
    if not (60 <= len(b.get('desc', '')) <= 165):
        problems.append(f'{slug}: desc length {len(b.get("desc", ""))} outside 60-165')
    for q, a in b.get('faq', []):
        if not q.strip().endswith('?'):
            problems.append(f'{slug}: faq question without ?: {q}')
    for where, val in (('body', b.get('body', '')), ('answer', b.get('answer', ''))):
        for href in re.findall(r'href="([^"]+)"', val):
            check_link(f'{slug} {where}', href)
    for q, a in b.get('faq', []):
        for href in re.findall(r'href="([^"]+)"', a):
            check_link(f'{slug} faq', href)
    words = len(text_of(b.get('body', '')).split())
    counts.append((words, slug))
    if b.get('cluster') not in LEGACY and words < 800:
        problems.append(f'{slug}: body {words} words, under 800')
    if b.get('cluster') not in LEGACY and '</' in b.get('answer', ''):
        problems.append(f'{slug}: html tag in answer')
    if (b.get('kw') or '').lower() in GUIDE_KWS:
        problems.append(f'{slug}: kw duplicates a guide kw')

counts.sort()
print(f'posts: {len(B.BLOGS)}  clusters: {len(B.CLUSTERS)}  guides: {len(guide_slugs)}')
if counts:
    print(f'words min {counts[0][0]} ({counts[0][1]}), max {counts[-1][0]}, median {counts[len(counts) // 2][0]}')
print('problems:', len(problems))
for p in problems:
    print('  -', p)
sys.exit(1 if problems else 0)
