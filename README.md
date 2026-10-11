# VocalForge site

Static pages for https://fuidzy.com/vocalforge, served by the `vocalforge-pages` Cloudflare Worker (same pattern as the SpaceWise pages).

- `content.py` page copy (hub FAQ, guides, policies); `content_tools.py` copy for the free tools and the AI guide
- `build.py` generator (`python build.py`, or `--launched --download-url URL` when the download is live)
- `assets/site.css` design; `assets/vf-core.js` + `assets/vf-ui.js` the in-browser analysers (BPM, key, chords, LUFS, vocal check). They run entirely in the visitor's browser and are inlined into the tool pages
- output: `vocalforge/` (pages + `img/`), `vocalforge-sitemap.xml`, `worker-pages.json` (the slug whitelist the Worker serves)
- photos: free-licence Pexels / Unsplash, credited in the footer (originals in `assets/src/`)
- support address: fuidzy@outlook.com (also the Mac-version request address)
