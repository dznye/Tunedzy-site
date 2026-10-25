# Tunedzy search and funnel

## The funnel

1. **Search (awareness):** a how-to guide answers the question in plain steps, without needing any tool.
2. **Consider (comparison):** an honest comparison or the alternatives hub says where each tool fits, and where Tunedzy is the better choice.
3. **Try (free):** every guide links to Tunedzy Go on the phone (free, nothing uploaded) and to the free browser tools.
4. **Get (decision):** the Windows app and the pricing page (free credits first, then packs or a plan). The thanks page and the download link close the loop.

Every guide ends with: all guides and comparisons, Tunedzy Go, and pricing. The home page shows six guides and a link to the full guides hub at `/tunedzy/guides`.

## What is here

- `content_seo_how.py`: twelve how-to guides.
- `content_seo_compare.py`: five comparisons and the voice-cleaner alternatives hub.
- `content.py`: merges both into the site; `build.py` renders them, adds the guides hub and the funnel links.
- `seo/make_keywords.py` builds `seo/keywords.csv`: 2,925 **candidate** queries, each mapped to the page that answers it. These are generated from combinations, not measured. Their volume column says `unmeasured`.
- `seo/COMMUNITIES.md`: where audio questions are asked, with rules to check first. Nothing has been posted.
- `seo/POST_DRAFTS.md`: three help-first drafts, awaiting approval.

## How a page goes live

1. `python build.py --launched --download-url <installer url> --go <path to dist/go>`
2. Commit and push `main`. The Worker reads pages from GitHub and reads `worker-pages.json` (refreshed by the build) to decide which paths to serve. A new page needs no Worker change.
3. Cached pages can take up to about 15 minutes to update after a push.

## Before you trust the numbers

- The keyword map is not search volume. Measure with Google Search Console after the sitemap is submitted, and sort by impressions and clicks.
- Competitor facts are from public reviews and vendor material on 25 October 2026. Prices and free-tier limits change; the copy points readers to each vendor's page instead of quoting them.
- Do not add reviews, ratings or customer counts. None exist yet.
