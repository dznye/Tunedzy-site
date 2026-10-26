# Tunedzy site

Static pages for https://fuidzy.com/tunedzy, served by the `vocalforge-pages` Cloudflare Worker from this repo's `main` branch
(GitHub repo `dznye/Tunedzy-site`). Procedures are in **RUNBOOK.md**; this file says what is where and why.

**To rebuild the live site:** `python build.py`, then `python tools/check_pages.py`, commit and push. Nothing else is needed.

## What is here

| Path | What it is |
|---|---|
| `build.py` | the generator. `python build.py` builds the live site; `--prelaunch` builds the old pre-launch variant; `--go <folder>` replaces the phone app at `/tunedzy/go/` (without it the existing `tunedzy/go` is kept) |
| `content.py`, `content_seo_how.py`, `content_seo_compare.py` | hub copy, 241 guides and comparisons, policies, prices |
| `content_tools.py` | copy for the 9 free in-browser tools |
| `content_blog.py` + `content_blog_ext_1.py` ... `_30.py` | the blog: 339 posts in 36 clusters (see below) |
| `cover_art.py` | the cover picture of every blog post (see below) |
| `assets/` | `site.css`, the in-browser tool code (`vf-*.js`), `icon.png`, `src/` (photo originals), `indexnow.txt` (the IndexNow key) |
| `tools/` | `check_blog.py`, `check_pages.py`, `crawl_live.py`, `indexnow.py` |
| `seo/` | search notes and `make_keywords.py` (3,181 candidate queries, each mapped to the page that answers it; volumes are not measured) |
| `tunedzy/` | **generated**: every page, `img/`, `go/` (the phone app), the IndexNow key file. Do not edit by hand; `build.py` wipes and rewrites it |
| `tunedzy-sitemap.xml`, `worker-pages.json` | **generated**: the sitemap (599 URLs) and the slug whitelist the Worker serves |

Support address: fuidzy@outlook.com (also the Mac-version request address). Photos are free-licence Pexels / Unsplash, credited in the footer.

## The blog

339 posts: 39 original (`content_blog.py`), 100 added on 2026-10-25 (`ext_1`-`ext_10`), 200 added on 2026-10-26 (`ext_11`-`ext_30`).
Every post after the first 139 is at least 800 words; across all 339 the median is 808 and the longest is 1,054 words. Written to be useful without the app,
each ends with a free tool, the Tunedzy Go page and links to related posts.

One module per cluster. A module defines `CLUSTERS` (one key: `tool`, `label`, `tool_name`), `BLOGS = []` and `add(**kw)`;
`content_blog.py` imports each and merges them in the `for _m in (_ext1, ..., _ext30)` loop at its end.
A post is `add(slug, cluster, kw, title, desc, h1, answer, body, faq)`:

- `title` at most 70 characters; `desc` 60-165; no HTML entities (use real characters such as the typographic apostrophe)
- `answer` plain text (it is the quick-answer box and must not end in a closing tag); `body` HTML with `<h2>` sections; `faq` is a list of `(question, answer)` tuples
- blog links are `/tunedzy/blog/<slug>`, guides `/tunedzy/<guide-slug>`, tools `/tunedzy/tools/<tool>`, the phone app `/tunedzy/go/`
- no invented statistics, prices or reviews; a trend claim names its source or says it is unverified

`python tools/check_blog.py` enforces all of this (and that every internal link points at something real). Run it before every build.

## Cover pictures

`cover_art.py` draws one picture per post as an inline SVG (waveforms, rings and a level meter), seeded from the post's slug, so a rebuild
gives the same picture and every post gets its own. Posts in one cluster share a colour family. They are generated artwork, not photographs.
The cover shows under the quick answer, as a thumbnail on the blog index and on the "Keep reading" cards. The social-share image stays the single `og.png`.

## How it is served

The `vocalforge-pages` Worker (Cloudflare account that owns fuidzy.com; route `fuidzy.com/tunedzy*`) reads from
`https://raw.githubusercontent.com/dznye/Tunedzy-site/main/`:

- a path is a page only if its slug is in `worker-pages.json` (the build rewrites it; the Worker re-reads it every 5 minutes), so **a new page needs no Worker change**
- `/tunedzy/img/*.webp`, `/tunedzy/go/*` and three named files (`og.png`, `favicon.png`, the IndexNow key) are served as static files; anything else under `/tunedzy/` falls through to a 404
- `/tunedzy-sitemap.xml` is served from the repo root; `/vocalforge*` 301-redirects to `/tunedzy*`
- short links (`fuidzy.com/bpm-finder` and others) are the Worker's `ALIAS` map plus one exact route per alias on the zone
- pages are cached about 10 minutes by the Worker and longer at the edge, so a push can take up to about 15 minutes to show

Downloads: `downloads.fuidzy.com/tunedzy/<file>` is the `vocalforge-downloads` Worker over the `dznye/Tunedzy-downloads` release `downloads`.
`downloads.fuidzy.com/tunedzy/Tunedzy-Setup.exe` is the stable link the site uses: the `tunedzy-verify` Worker answers 302 to the installer named in the published `manifest.json`,
so a new release needs no site change. `tunedzy-verify` also signs the weekly licence lease (secret `LEASE_KEY`); do not redeploy it casually.

## Search

- **Google Search Console** (domain property `fuidzy.com`) and **Bing Webmaster Tools** (`https://fuidzy.com/`): eight sitemaps are submitted in both (listed in RUNBOOK.md). `tunedzy-sitemap.xml` is the one this repo owns.
- **IndexNow:** key `assets/indexnow.txt`, published as `/tunedzy/<key>.txt`. It covers `/tunedzy/` URLs only; `tools/indexnow.py` sends them. The 598 `/tunedzy/` URLs were accepted on 2026-10-26.
- Nothing about rankings is measured yet; read Search Console and Bing after a few weeks.

## Short tool links
`fuidzy.com/bpm-finder`, `/key-finder`, `/song-key-finder`, `/chord-finder`, `/lufs-meter`, `/vocal-checker`, `/live-autotune`, `/autotune-online`, `/karaoke-autotune`, `/online-karaoke`,
`/noise-remover`, `/voice-recorder`, `/noise-cancelling-mic`, `/clean-streaming-mic` 301-redirect to the real tool pages under `/tunedzy/tools/`.

## Live tools
`assets/vf-live.js` (Web Audio engine: YIN pitch detection + delay-line shifter in an AudioWorklet, limiter, reverb, recording taps) and `assets/vf-live-ui.js` power `/tools/live-autotune` and `/tools/karaoke-autotune`.
Same shifter as the desktop app's live monitor. Tested with a synthetic mic (override `navigator.mediaDevices.getUserMedia`). All tool code runs in the visitor's browser; nothing is uploaded.

## Known limits (2026-10-26)

- Streamdzy (1,138 URLs), the `/blog/` pages and a few root pages on fuidzy.com are listed in the sitemaps but are built elsewhere (not in this repo or on this machine), so they have no IndexNow key file; they rely on their sitemaps.
- `sitemap-all.xml` (Worker `fuidzy-sitemap-all`) is an old hard-coded list with only 29 Tunedzy URLs. `robots.txt` and `sitemap-index.xml` point at `tunedzy-sitemap.xml`, which is authoritative.
- `tunedzy-verify` still fetches the manifest through the old repo name `dznye/vocalforge-downloads` (works through GitHub's rename redirect). The two other Workers were switched to the new names on 2026-10-26.
- The 139 oldest posts predate the 800-word rule; the shortest, `why-finish-a-vocal-in-one-app-instead-of-many-plugins`, is 107 words.
- Cover pictures are generated artwork. Real photos would need sourcing and credits.
- Not done by the owner yet (from the app handoff): a real purchase test, reading the draft privacy/terms/refund pages, signing the Windows installer.
