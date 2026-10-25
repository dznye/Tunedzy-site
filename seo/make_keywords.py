"""Builds seo/keywords.csv: candidate search queries for Tunedzy's audio pages, each mapped to the page that answers it.

  python seo/make_keywords.py

IMPORTANT: these rows are candidate queries made from combinations of problems, sources and intents. They are NOT measured search
volumes (the volume column says so). Measure real demand after launch (Google Search Console, Google Keyword Planner or a keyword tool)
and sort by what people actually search. One page answers many rows; do not write a page per row.
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import content as C  # noqa: E402
import content_blog as B  # noqa: E402
import content_tools as T  # noqa: E402

OUT = Path(__file__).resolve().parent / 'keywords.csv'
LIVE = set(C.GUIDE_ORDER) | {'guides', 'pricing'} | {b['slug'] for b in B.BLOGS} | {'tools/' + s for s in T.TOOL_ORDER}

PROBLEMS = {  # problem -> the guide that answers it
    'background noise': 'remove-background-noise-from-a-voice-recording',
    'room echo': 'remove-echo-from-vocal-recording',
    'hum': 'remove-hum-from-audio',
    'hiss': 'remove-background-noise-from-a-voice-recording',
    'fan noise': 'remove-background-noise-from-a-voice-recording',
    'traffic noise': 'remove-background-noise-from-a-voice-recording',
    'keyboard noise': 'remove-background-noise-from-a-voice-recording',
    'wind noise': 'remove-background-noise-from-a-voice-recording',
    'rumble': 'remove-background-noise-from-a-voice-recording',
    'clipping': 'fix-clipped-distorted-audio',
    'distortion': 'fix-clipped-distorted-audio',
    'muffled': 'fix-a-muffled-voice-recording',
    'clicks': 'clean-up-a-phone-voice-recording',
    'crackle': 'clean-up-a-phone-voice-recording',
    'mic pops': 'clean-up-a-phone-voice-recording',
    'breath noise': 'clean-up-a-phone-voice-recording',
    'sibilance': 'fix-a-muffled-voice-recording',
    'low volume': 'loudness-for-youtube-podcasts-and-spotify',
    'uneven volume': 'loudness-for-youtube-podcasts-and-spotify',
    'dead air': 'edit-a-podcast-by-its-words',
    'filler words': 'edit-a-podcast-by-its-words',
    'robotic voice': 'remove-background-noise-from-a-voice-recording',
}
SOURCES = {  # source -> the page that answers it best when the problem is about that source
    'phone voice recording': None,
    'voice memo': 'voice-note-sounds-better-on-an-iphone',
    'iphone recording': 'voice-note-sounds-better-on-an-iphone',
    'android recording': None,
    'voiceover': 'record-a-voiceover-on-your-phone',
    'tiktok voiceover': 'record-a-voiceover-on-your-phone',
    'reels voiceover': 'record-a-voiceover-on-your-phone',
    'youtube short audio': 'record-a-voiceover-on-your-phone',
    'video audio': 'put-clean-audio-back-into-a-video',
    'mp4 audio': 'put-clean-audio-back-into-a-video',
    'mov audio': 'put-clean-audio-back-into-a-video',
    'song vocal': 'record-a-vocal-at-home-for-a-song',
    'home vocal': 'record-a-vocal-at-home-for-a-song',
    'podcast episode': 'podcast-sound-professional-on-a-budget',
    'interview recording': 'edit-a-podcast-by-its-words',
    'zoom recording': None,
    'obs stream mic': 'remove-background-noise-from-mic-obs',
    'discord voice': 'virtual-audio-cable-setup-obs-discord-zoom',
    'webcam mic': None,
    'usb mic': 'podcast-sound-professional-on-a-budget',
    'laptop mic': None,
}
INTENTS = [  # template, intent, stage (awareness = how-to, consideration = compare, decision = get it)
    ('how to remove {p} from {s}', 'informational', 'awareness'),
    ('fix {p} in {s}', 'informational', 'awareness'),
    ('how to get rid of {p} in {s}', 'informational', 'awareness'),
    ('best free {p} remover for {s}', 'commercial', 'consideration'),
    ('{s} {p} fix online free', 'transactional', 'decision'),
    ('{p} removal app for {s}', 'transactional', 'decision'),
]
COMPETITORS = {  # name -> the comparison page (None: the alternatives hub)
    'adobe podcast enhance speech': 'tunedzy-vs-adobe-podcast-enhance',
    'dolby on': 'tunedzy-vs-dolby-on',
    'descript': 'tunedzy-vs-descript',
    'audacity': 'tunedzy-vs-audacity',
    'auphonic': 'tunedzy-vs-auphonic',
    'cleanvoice': 'voice-cleaner-alternatives',
    'tunedzy': 'voice-cleaner-alternatives',
}
COMPARE_TEMPLATES = ['{t} alternative', '{t} vs tunedzy', 'is {t} free', '{t} review', '{t} for podcasts', '{t} for voice recording']
LOUDNESS = ['youtube', 'spotify', 'podcast', 'apple podcasts', 'tiktok', 'instagram reels', 'soundcloud', 'audiobook', 'broadcast']
HOWTO = ['make {s} sound professional', 'record {s} at home', 'clean {s} on phone', 'improve {s} sound quality']
TOOL_QUERIES = {  # query -> tool page slug
    'free lufs meter': 'lufs-meter', 'free vocal checker': 'vocal-checker', 'free bpm finder': 'bpm-finder',
    'free song key finder': 'song-key-finder', 'free chord finder': 'chord-finder', 'free live autotune': 'live-autotune',
    'free karaoke autotune': 'karaoke-autotune', 'clean streaming mic': 'clean-streaming-mic',
    'voice recorder noise cancellation': 'voice-recorder-noise-cancellation',
}


def main():
    rows, seen = [], set()

    def add(q, intent, stage, path, cluster):
        q = ' '.join(q.lower().split())
        if q in seen:
            return
        seen.add(q)
        rows.append(dict(query=q, cluster=cluster, intent=intent, stage=stage, page='/tunedzy/' + path,
                         page_status='live' if path in LIVE else 'planned', volume='unmeasured'))

    for p, page in PROBLEMS.items():
        for s, spage in SOURCES.items():
            target = spage or page
            for tpl, intent, stage in INTENTS:
                add(tpl.format(p=p, s=s), intent, stage, target, 'problem: ' + p)
    for name, page in COMPETITORS.items():
        for tpl in COMPARE_TEMPLATES:
            add(tpl.format(t=name), 'commercial' if ('alternative' in tpl or 'vs' in tpl) else 'informational', 'consideration', page, 'compare: ' + name)
    for pl in LOUDNESS:
        add(f'lufs for {pl}', 'informational', 'awareness', 'loudness-for-youtube-podcasts-and-spotify', 'loudness')
        add(f'{pl} loudness target', 'informational', 'awareness', 'loudness-for-youtube-podcasts-and-spotify', 'loudness')
    for s, spage in SOURCES.items():
        for tpl in HOWTO:
            add(tpl.format(s=s), 'informational', 'awareness', spage or 'clean-up-a-phone-voice-recording', 'how to: ' + s)
    for q, slug in TOOL_QUERIES.items():
        add(q, 'transactional', 'decision', 'tools/' + slug, 'free tool')
    rows.sort(key=lambda r: (r['stage'], r['cluster'], r['query']))
    with OUT.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    live = sum(1 for r in rows if r['page_status'] == 'live')
    print(f'{len(rows)} candidate queries -> {OUT} ({live} answered by a live page, {len(rows) - live} planned)')


if __name__ == '__main__':
    main()
