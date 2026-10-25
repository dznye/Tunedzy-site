# Search research: audio questions, competitors and gaps (25 October 2026)

What this is: a read of public search results and vendor and review pages, to decide which pages to write. It is not search-volume data.
Measure real demand in Google Search Console after the sitemap is submitted, and re-run this research each quarter.

Method and limits: the search tool returned general web results and few Reddit or forum threads, so community demand is inferred
from the kinds of questions that came up, not counted. Many results were vendor blogs. Prices and free-tier limits change, so the
pages do not quote them.

## What people ask (questions that came up repeatedly)

- How to clean up a phone voice recording; how to remove background noise from voice. ([Lalal.ai guide](https://www.lalal.ai/blog/clean-up-voice/), [Cleanvoice guide](https://cleanvoice.ai/blog/background-noise-removal/))
- How to remove breath noise from a voiceover; the gate trick; breath tools. ([Waves](https://waves.com/how-to-debreath-vocals-without-manual-editing), [WP Fastest Cache](https://www.wpfastestcache.com/blog/how-to-remove-breath-and-mouth-sounds-from-voice-overs/))
- How to remove plosives and mic pops; pop filter placement; high-pass fixes. ([CrumplePop](https://crumplepop.com/how-to-remove-plosives-from-vocals/), [iZotope](https://www.izotope.com/en/learn/removing-plosives-from-a-voice-recording.html))
- How to remove echo from a phone recording; limits of echo removal. ([Cleanvoice](https://cleanvoice.ai/blog/how-to-remove-echo-from-audio/), [Audacity forum](https://forum.audacityteam.org/t/echo/62238))
- How to clean up a Zoom or phone call recording; separate local tracks are the best case. ([iZotope](https://www.izotope.com/en/learn/how-to-clean-up-audio-from-a-phone-recording1.html), [Cleanvoice](https://cleanvoice.ai/blog/how-to-edit-zoom-recording/))
- What a noise gate is, and its controls. ([Lalal.ai](https://www.lalal.ai/blog/what-is-a-noise-gate/), [Violet Recording](https://violetrecording.com/what-is-a-noise-gate/))
- What true peak (dBTP) is, and why -1 dBTP. ([Production Expert](https://www.production-expert.com/production-expert-1/loudness-vs-true-peak-a-beginners-guide?format=amp))
- Voiceovers on TikTok: room, distance from the mouth, levels. ([Podcastle](https://podcastle.ai/blog/how-to-do-a-voice-over-on-tiktok), [Later](https://later.com/resources/videos/how-to-add-a-voiceover-on-tiktok))
- Free audio editors: Audacity noise reduction, GarageBand on Apple devices, DaVinci Resolve Fairlight for dialogue. ([PodFeet](https://www.podfeet.com/blog/how-to-remove-noise-with-audacity/))

## Competitor landscape (what each one is, in its own terms)

- **Adobe Podcast Enhance Speech:** a one-click browser speech enhancer with a free tier. Third-party reviews describe daily limits; Adobe's own page is the reference. ([TechRadar](https://www.techradar.com/computing/artificial-intelligence/i-tried-adobes-free-ai-podcast-enhancer-and-i-cant-believe-how-good-it-makes-even-bad-recordings-sound), [Gaurav Tiwari review](https://gauravtiwari.org/adobe-podcast-review/))
- **Dolby On:** a phone recorder with processing as you record, presets, and a live-stream option on iOS. ([iMore](https://www.imore.com/apps/the-dolby-on-app-is-my-new-favorite-way-to-record-audio-on-the-go), [App Store](https://apps.apple.com/app/id1443964192))
- **Descript:** transcript-based audio and video editing with filler removal, cloud-based, on paid plans. Price comparisons come mostly from a competing transcription vendor, so check Descript's own page. ([Sonix review](https://sonix.ai/resources/?p=3512))
- **Auphonic:** a post-production service with an adaptive leveller, loudness targets and a true-peak limiter. Its official help is the reliable source. ([Auphonic help](https://us.auphonic.com/help/algorithms/singletrack.html))
- **Audacity:** free, manual noise reduction from a noise profile. ([Creative Live lesson](https://site.creativelive.com/class/audio-recording-101-record-voice-audio-for-video-production-tomas-george/lessons/how-to-use-the-noise-reduction-effect-in-audacity))
- **Plugins for breath and plosive repair** (Waves DeBreath, iZotope RX, CrumplePop): the plugin vendors describe their own tools; the core techniques are the same across them.

## Gaps this site can fill (and the pages written for them)

| Gap in the results | Why it matters | Page |
|---|---|---|
| Breath noise has no plain manual guide for a voiceover | Voiceover and podcast searchers | how-to-remove-breath-noise-from-a-voice-recording |
| Keyboard and desk clicks get generic noise advice | Streamers, podcasters | how-to-remove-keyboard-and-desk-noise-from-a-recording |
| Wind noise on location | Outdoor creators | how-to-remove-wind-noise-from-audio |
| Call recordings: what cleanup can and cannot fix | Zoom and Teams users | how-to-clean-up-a-zoom-or-video-call-recording |
| Remote podcast guests: local backup and level matching | Podcasters | how-to-record-a-remote-podcast-guest |
| Interview cleanup that keeps the speaker natural | Interviewers, journalists | how-to-clean-up-an-interview-recording |
| Making audio louder without distortion | Anyone with a quiet file | how-to-make-audio-louder-without-distortion |
| Export settings for Spotify and Apple Podcasts | Publishers | how-to-export-audio-for-spotify-and-apple-podcasts |
| Warmth in a thin voice, without mud | Vocalists, voiceover | how-to-make-a-voice-sound-warmer |
| Isolating a voice from music (with the rights caveat) | Creators, remixers | how-to-isolate-a-voice-from-background-music |
| Laptop mic recording | Students, remote workers | how-to-record-a-voice-on-a-laptop-microphone |
| Plain definitions: noise gate, LUFS, true peak, EQ, high-pass filter | Searchers who meet the term first | the glossary pages |

## What to measure next

1. Search Console impressions and clicks by page, after the sitemap is submitted.
2. Which keyword clusters in `seo/keywords.csv` get impressions, then write pages for the top ones.
3. Which pages lead to Tunedzy Go or a download. Cut the pages that get traffic and no clicks onward.
4. Re-check the competitor pages every quarter: prices, free tiers and features change.
