"""Tell Bing, Yandex and other IndexNow engines that pages were added or changed.

  python tools/indexnow.py --changed              pages changed in the last commit (HEAD~1..HEAD)
  python tools/indexnow.py --changed --since REV  pages changed since REV
  python tools/indexnow.py --all                  every URL in tunedzy-sitemap.xml (a new key, or a big change)
  python tools/indexnow.py URL [URL ...]          just those URLs
  add --dry-run to print the URLs without sending

Submit only what is new or changed; repeating the whole site every day is discouraged by IndexNow.

How it works: assets/indexnow.txt holds the key. build.py publishes it as tunedzy/<key>.txt, and the vocalforge-pages
Worker serves that one file (its STATIC map names it). IndexNow fetches https://fuidzy.com/tunedzy/<key>.txt to check
the key, and a key in a folder only covers URLs in that folder, so this script sends /tunedzy/ URLs only.
See RUNBOOK.md for rotating the key.

Answers: 200 accepted; 202 accepted, key check pending; 403 SiteVerificationNotCompleted: wait a few minutes and
retry; 403 UserForbiddedToAccessSite: the key file did not load (404 or wrong text), fix that or rotate the key.
"""
import argparse
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = 'fuidzy.com'
BASE = f'https://{HOST}/tunedzy'
KEY = (ROOT / 'assets' / 'indexnow.txt').read_text(encoding='utf-8').strip()

ap = argparse.ArgumentParser()
ap.add_argument('urls', nargs='*')
ap.add_argument('--changed', action='store_true')
ap.add_argument('--since', default='HEAD~1')
ap.add_argument('--all', action='store_true')
ap.add_argument('--dry-run', action='store_true')
args = ap.parse_args()

urls = list(args.urls)
if args.all:
    urls += re.findall(r'<loc>([^<]+)</loc>', (ROOT / 'tunedzy-sitemap.xml').read_text(encoding='utf-8'))
if args.changed:
    out = subprocess.run(['git', 'diff', '--name-only', f'{args.since}..HEAD', '--', 'tunedzy'], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout.split()
    for f in out:
        m = re.fullmatch(r'tunedzy/(.*?)/?index\.html', f)
        if m and not m.group(1).startswith(('go/', 'img/')):
            urls.append(f'{BASE}/{m.group(1)}'.rstrip('/'))
urls = sorted({u for u in urls if u.startswith(BASE)})
if not urls:
    sys.exit('nothing to submit')
print(f'{len(urls)} URLs')
if args.dry_run:
    print('\n'.join(urls[:20]) + ('\n...' if len(urls) > 20 else ''))
    sys.exit(0)

for i in range(0, len(urls), 10000):
    chunk = urls[i:i + 10000]
    body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': f'{BASE}/{KEY}.txt', 'urlList': chunk}).encode('utf-8')
    req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, method='POST',
                                 headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print(f'{len(chunk)} URLs: HTTP {r.status}')
    except urllib.error.HTTPError as e:
        print(f'{len(chunk)} URLs: HTTP {e.code} {e.read().decode("utf-8", "replace")[:200]}')
        sys.exit(1)
