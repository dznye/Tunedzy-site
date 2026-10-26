"""Fetch every URL in the live sitemap and report anything that is not a 200.

  python tools/crawl_live.py                  https://fuidzy.com/tunedzy-sitemap.xml
  python tools/crawl_live.py --sitemap URL    another sitemap
  python tools/crawl_live.py --workers 8      parallel requests (default 6; keep it modest, the site runs on the free plan)

Exits 1 when any URL fails. Takes about a minute for ~600 URLs.
"""
import argparse
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ap = argparse.ArgumentParser()
ap.add_argument('--sitemap', default='https://fuidzy.com/tunedzy-sitemap.xml')
ap.add_argument('--workers', type=int, default=6)
args = ap.parse_args()


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'tunedzy-crawl/1'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b''
    except Exception as e:  # noqa: BLE001 - report any network failure as a failed URL
        return str(e)[:60], b''


status, xml = get(args.sitemap)
if status != 200:
    sys.exit(f'sitemap not readable: {status}')
urls = re.findall(r'<loc>([^<]+)</loc>', xml.decode('utf-8'))
print(f'{len(urls)} URLs in {args.sitemap}')
bad = []
with ThreadPoolExecutor(args.workers) as ex:
    for url, (code, _) in zip(urls, ex.map(get, urls)):
        if code != 200:
            bad.append((code, url))
print('not 200:', len(bad))
for code, url in bad[:40]:
    print(' ', code, url)
sys.exit(1 if bad else 0)
