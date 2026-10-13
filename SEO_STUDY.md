# Tunedzy SEO study (US, October 2026)

**Honest caveat:** real Google search volumes need Keyword Planner / Ahrefs / Semrush (logged-in tools), so the keyword
priorities below come from *who ranks and what the results look like*, not from volume numbers. Section 6 is how to add the numbers.

## 1. What the search results look like

| Query family | Who ranks | What that tells us |
|---|---|---|
| "make phone vocals sound professional" | MusicTech, iZotope blog, Splice, emastered, Soundtrap | Long how-to guides from plugin/DAW brands. Beatable with a *more specific, step-by-step* guide that names the order of operations. |
| "free online autotune (for rap)" | Audimee, Rys Up, BandLab, producelikeapro lists | Tool pages + "best free" roundups. People want to *try something now*; free tiers dominate. |
| "remove echo / room reverb from vocal" | LALAL.AI, Rys Up, stemsplit, Soundtrap, Sound On Sound (prime:vocal review) | Mix of AI online tools and tutorials. Intent: fix this file today. |
| "mix vocals on a beat / make vocals sit" | producelikeapro, Violet Recording, MasteringBOX, iZotope, headlinerhub | Pure education, beginner level. High intent for anyone with a 2-track beat (our exact user). |
| "sound like Future / The Weeknd vocal chain" | Rys Up (preset seller), Soundcy, Music Guy Mixing, Antares blog | Artist-style queries are common and answered by preset sellers. Entity-driven; very relevant to our "match an artist" feature. |
| "best vocal cleanup / autotune software" | listicles, vendor pages | Comparison intent, buying stage. |

## 2. The gap we can own

Nobody pairs these four things: **(a) a Windows desktop app, (b) one-time low price, (c) offline/private (unreleased songs stay on the PC), (d) match the style of a reference song.**
Online tools can't claim (c); plugins can't claim "finished in one pass"; subscriptions (Auto-Tune $30/mo, LANDR) can't claim (b).
Positioning line used on the page: *"Make rough vocals sound finished, without a studio. $29 once."*

## 3. Page plan (live)

| URL | Primary query | Search intent | Funnel |
|---|---|---|---|
| `/vocalforge` | vocal cleanup / autotune / mastering software, Tunedzy | commercial + brand | convert |
| `/vocalforge/fix-vocals-recorded-on-phone` | make phone vocals sound professional | informational, problem-aware | top |
| `/vocalforge/remove-echo-from-vocal-recording` | remove echo from vocal recording | informational, fix-it-now | top/mid |
| `/vocalforge/autotune-for-rap-vocals` | autotune for rap vocals, free online autotune | informational + tool-seeking | mid |
| `/vocalforge/mix-vocals-on-a-beat` | how to mix vocals on a beat | informational, beginner | top |
| `/vocalforge/future-vocal-effect-settings` | Future vocal effect settings | artist/entity style | mid |
| `/vocalforge/vocal-cleanup-software-compared` | best vocal cleanup software, Nectar alternative | commercial investigation | bottom |
| `/vocalforge/thanks`, `privacy`, `terms`, `refund-policy` | n/a | trust / post-purchase (thanks is noindex) | |

All guides lead with the answer, give real steps and numbers, admit limits, and end with a soft product tie-in, which is what the ranking pages do.

## 4. On-page checklist (done)

- Unique `<title>` (<= 60 chars) and meta description (<= 160) per page; one H1 matching the primary query; clean H2 outline.
- Canonical URLs (no trailing slash; trailing-slash URLs 301 to canonical); OG + Twitter cards with a 1200x630 image.
- JSON-LD: `SoftwareApplication` + `Offer` ($29 USD) on the hub, `FAQPage` on hub and every guide, `Article` on guides, `BreadcrumbList` everywhere.
  No fake ratings or reviews anywhere (that risks a manual action). `availability` is `PreOrder` until launch, `InStock` after.
- Speed: zero JavaScript, inline CSS, WebP photos 20-110 KB with explicit width/height (no layout shift), lazy-loaded below the fold, hero preloaded via `fetchpriority`.
- Internal links: hub -> all guides (with thumbnails); every guide -> hub + three related guides; footer on every page.
- Sitemap: `/vocalforge-sitemap.xml` and merged into `fuidzy.com/sitemap-all.xml`.
- Trust: policy pages, "not affiliated with any artist or plugin company", honest-limits section, photo credits.

## 5. Next content (ordered by how directly it matches the product)

1. `how-to-sound-like-the-weeknd-vocals` / `-drake-` / `-travis-scott-` (artist-style cluster; same template as the Future page)
2. `vocal-chain-for-rap-in-order` (the full chain: gate, de-ess, tune, comp, sat, reverb, delay)
3. `fix-clipped-vocal-recording` and `remove-mic-pops-plosives` and `how-to-de-ess-vocals`
4. `ai-voice-cover-vocals-sound-robotic` (fixing split words / timing on AI-voice vocals: a fresh, low-competition topic)
5. `how-loud-should-vocals-be-on-a-beat` and `what-lufs-for-spotify-and-youtube`
6. `autotune-settings-key-and-scale-finder` (a free "find the key of my beat" explainer; link-bait)
7. Alternatives pages: `nectar-alternative`, `auto-tune-alternative-one-time-price`, `prime-vocal-alternative`
8. A real before/after audio sample page (embed two short clips): the strongest conversion asset once you have permission-cleared audio.

## 6. Adding the volume numbers (about an hour)

1. Google Ads account (no spend needed) -> Keyword Planner -> *Get search volume*, location United States, paste the queries from section 3 and 5.
   Volumes show as ranges; sort by volume and by low competition.
2. Google Trends: compare "autotune", "vocal mastering", "vocal cleanup" for the last 12 months (US).
3. Re-order section 5 by volume x (1 - difficulty). Move the top 3 up.

## 7. Measuring it

- Google Search Console: add `fuidzy.com`, submit `https://fuidzy.com/sitemap-all.xml`, request indexing for the hub + 6 guides.
- Watch: impressions and average position per page, queries that get impressions but few clicks (rewrite those titles), pages stuck at position 11-20 (add depth/links).
- Conversion: Dodo dashboard (test vs live), plus UTM links from ads/social so you can see which source buys.
- Backlinks (the real ranking lever for a new page): post the guides where bedroom artists are (r/makinghiphop, r/WeAreTheMusicMakers, r/musicproduction: read each sub's self-promo rules first), YouTube walkthroughs, and producer/beatmaker communities.

## 8. Launch flip (done 2026-10-11)

The site was flipped with `python build.py --launched --download-url https://downloads.fuidzy.com/vocalforge/VocalForge-Setup-1.0.0.exe`. The notes below describe how.

The page is in **pre-launch** mode: no buy button, download shows "launching soon", schema says `PreOrder`.
When the installer is hosted and tested: `python build.py --launched --download-url <installer url>`, commit, push. The Worker
caches pages for ~10 minutes, so it updates by itself.
