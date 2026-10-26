# Tunedzy site: runbook

Everything here was checked on 2026-10-26. Commands run from this repo's root.

## Before every push

```bash
python tools/check_blog.py                 # posts: schema, links, lengths. Must say "problems: 0"
python build.py                            # builds the live site; a bare run reproduces what is deployed
python tools/check_pages.py                # built pages: titles, FAQ markup, internal links. Must say "problems: 0"
git status                                 # only intended files changed
```

Never hand-edit `tunedzy/`, `tunedzy-sitemap.xml` or `worker-pages.json`; `build.py` rewrites them.
`build.py` keeps the existing `tunedzy/go/` (the phone app) unless you pass `--go <folder>`.

## Add posts

1. Copy the header of the newest module (`content_blog_ext_30.py`) to `content_blog_ext_31.py`: a `CLUSTERS` dict with one new key (`tool` must be a slug in `content_tools.TOOLS`, plus `label` and `tool_name`), `BLOGS = []`, `add(**kw)`.
2. Write posts (rules in README.md). Aim for 800+ words, real internal links, no invented numbers.
3. In `content_blog.py` add `import content_blog_ext_31 as _ext31  # noqa: E402` and add `_ext31` to the `for _m in (...)` tuple.
4. Run the three commands above, commit, push.
5. After about 15 minutes: `python tools/crawl_live.py` (every sitemap URL must answer 200), then `python tools/indexnow.py --changed`.
   Google re-reads `tunedzy-sitemap.xml` by itself; no resubmit is needed.

## Release a new Windows build (the site follows by itself)

Follow "Release flow" in the app repo's `HANDOFF.md`. The site's download button is `downloads.fuidzy.com/tunedzy/Tunedzy-Setup.exe`,
and the `tunedzy-verify` Worker redirects it to the installer named in the release's `manifest.json`, so upload the installer, then the manifest last. No site rebuild is needed.
Never delete old release files.

## Refresh the phone app on the site

In the app repo: `python tools/build_go.py` (writes `dist/go`), then here `python build.py --go ../Tunedzy/dist/go`, check `git status`, commit, push.
(`dist/` is git-ignored in the app repo, so `dist/go` exists only on the machine that built it; the copy in this repo's `tunedzy/go/` is the one that is live.)

## Roll back

- Site: `git revert <commit>` and push, then wait about 15 minutes. The Worker reads `main` from GitHub, nothing else holds a copy.
- A Worker: Cloudflare dashboard, Workers and Pages, the Worker, Deployments, roll back to a previous version.

## The Workers

All in the Cloudflare account that owns the `fuidzy.com` zone (Free plan, 100,000 requests a day shared by every site on it).

| Worker | Routes | Source of truth | Notes |
|---|---|---|---|
| `vocalforge-pages` | `fuidzy.com/tunedzy*`, `/vocalforge*`, the short links | GitHub raw `dznye/Tunedzy-site` `main` (set 2026-10-26) | no bindings. Static files are the `STATIC` map: `og.png`, `favicon.png`, the IndexNow key file |
| `vocalforge-downloads` | `downloads.fuidzy.com/*` | GitHub release `dznye/Tunedzy-downloads` tag `downloads` (set 2026-10-26) | no bindings. Serves any file in the release, with range requests |
| `tunedzy-verify` | `downloads.fuidzy.com/tunedzy/Tunedzy-Setup.exe`, `/tunedzy/verify` (and the `/vocalforge/` twins) | manifest URL still uses `dznye/vocalforge-downloads` (GitHub redirect) | **holds the secret `LEASE_KEY`**. If you edit it in the dashboard the secret is kept. If you upload it through the API, send `"keep_bindings": ["secret_text"]` or the licence lease stops working |

Editing a Worker: Cloudflare dashboard, Workers and Pages, the Worker, Edit code, deploy. Or the API (`PUT /accounts/<id>/workers/scripts/<name>` with multipart `metadata` + the module).
Read the current source first (`GET .../content/v2`), change one line, check `bindings` in `.../settings` is empty before re-uploading, and test a few URLs straight after.

## Search consoles and IndexNow

Sitemaps submitted in Google Search Console and Bing Webmaster Tools on 2026-10-26 (all read successfully):
`sitemap.xml`, `sitemap-index.xml`, `sitemap-all.xml`, `blog-guides-sitemap.xml`, `spacewise-sitemap.xml`, `tunedzy-sitemap.xml`, `streamdzy-sitemap.xml`, `vocalforge-sitemap.xml` (a 301 to the Tunedzy one).
`robots.txt` lists six of them.

IndexNow: `tools/indexnow.py --changed` (last commit), `--since REV`, `--all`, or give URLs. Only `/tunedzy/` URLs are accepted for this key.

### Rotate the IndexNow key
Do this if IndexNow answers 403 `UserForbiddedToAccessSite` and the key URL really serves the key, or if the key leaks into something it should not.

1. `python -c "import secrets; print(secrets.token_hex(16))"` and put the result in `assets/indexnow.txt`.
2. `python build.py` (writes `tunedzy/<newkey>.txt`, removes the old one), commit, push.
3. In `vocalforge-pages` change the file name in the `STATIC` map from the old key to the new one and deploy.
4. `curl https://fuidzy.com/tunedzy/<newkey>.txt` must return the key as `text/plain`. **Do not call IndexNow before this works**: a key whose file returned 404 at the first check can be refused afterwards.
5. `python tools/indexnow.py --all`. `SiteVerificationNotCompleted` means wait a few minutes and retry.

## Monthly check (about 10 minutes)

1. `python tools/crawl_live.py`: every URL 200.
2. Google Search Console, Sitemaps: all eight "Success"; Pages: indexed count rising toward 599 for `/tunedzy/`. Bing, Sitemaps: all "Succeeded", none with errors.
3. `curl -I https://downloads.fuidzy.com/tunedzy/Tunedzy-Setup.exe` gives 302 to the versioned installer, and that answers 200.
4. Cloudflare dashboard: Workers requests well under 100,000 a day; the zone is Active. The domain `fuidzy.com` is registered until 2027-09-06 with auto-renew on.
5. Read what people search for in Search Console and write posts for the gaps (see "Add posts").

## When something looks wrong

| Symptom | Likely cause | What to do |
|---|---|---|
| New page 404 | push not live yet, or the slug is missing from `worker-pages.json` | wait 15 minutes; check the build ran and the push landed |
| Page shows "Temporarily unavailable" (503) | GitHub raw or the release was unreachable | usually clears in a minute; check githubstatus.com |
| Whole site 404 under `/tunedzy/` | the Worker route or the Worker was removed or broken | Workers, `vocalforge-pages`, Deployments, roll back |
| A build deleted the phone app | `--go` given an empty folder | `git checkout -- tunedzy/go` |
| Site looks like the pre-launch variant | built with `--prelaunch` | `python build.py` |
| IndexNow 403 `SiteVerificationNotCompleted` | the key check is still running | wait, retry |
| IndexNow 403 `UserForbiddedToAccessSite` | the key file does not load as exactly the key | fix the file or rotate the key |

## Not done, and why

- IndexNow for Streamdzy, the root `/blog/` pages and other fuidzy.com pages: they are built in other repos that are not on this machine; add a key file there.
- A real purchase test, the privacy/terms/refund review, code-signing the Windows installer and opening the Mac build on a Mac: owner steps listed in the app repo's `HANDOFF.md`.
- Search results are not measured yet.
