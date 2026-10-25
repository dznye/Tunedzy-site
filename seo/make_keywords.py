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
LIVE = set(C.GUIDE_ORDER) | {'guides', 'pricing'} | {'blog/' + b['slug'] for b in B.BLOGS} | {'tools/' + s for s in T.TOOL_ORDER}

PROBLEMS = {  # problem -> the guide that answers it
    'background noise': 'remove-background-noise-from-a-voice-recording',
    'room echo': 'remove-echo-from-vocal-recording',
    'hum': 'remove-hum-from-audio',
    'hiss': 'remove-background-noise-from-a-voice-recording',
    'fan noise': 'remove-background-noise-from-a-voice-recording',
    'traffic noise': 'remove-background-noise-from-a-voice-recording',
    'keyboard noise': 'how-to-remove-keyboard-and-desk-noise-from-a-recording',
    'wind noise': 'how-to-remove-wind-noise-from-audio',
    'rumble': 'remove-background-noise-from-a-voice-recording',
    'clipping': 'fix-clipped-distorted-audio',
    'distortion': 'fix-clipped-distorted-audio',
    'muffled': 'fix-a-muffled-voice-recording',
    'clicks': 'clean-up-a-phone-voice-recording',
    'crackle': 'clean-up-a-phone-voice-recording',
    'mic pops': 'blog/remove-mic-pops-plosives',
    'breath noise': 'how-to-remove-breath-noise-from-a-voice-recording',
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
    'obs stream mic': 'blog/remove-background-noise-from-mic-obs',
    'discord voice': 'blog/virtual-audio-cable-setup-obs-discord-zoom',
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

RESEARCH_QUERIES = {  # query (from the research in seo/RESEARCH.md) -> the page that answers it
    'what is a noise gate': 'what-is-a-noise-gate',
    'what is a noise gate in audio': 'what-is-a-noise-gate',
    'what is lufs': 'what-is-lufs',
    'what is lufs in audio': 'what-is-lufs',
    'what is true peak dbtp': 'what-is-true-peak-dbtp',
    'what is dbtp': 'what-is-true-peak-dbtp',
    'what is an equalizer eq': 'what-is-an-equalizer',
    'what is a high pass filter': 'what-is-a-high-pass-filter',
    'how to remove breath noise from voice recording': 'how-to-remove-breath-noise-from-a-voice-recording',
    'how to remove echo from phone voice recording': 'remove-echo-from-vocal-recording',
    'clean up zoom recording audio': 'how-to-clean-up-a-zoom-or-video-call-recording',
    'how to clean up zoom recording': 'how-to-clean-up-a-zoom-or-video-call-recording',
    'how to remove keyboard noise from recording': 'how-to-remove-keyboard-and-desk-noise-from-a-recording',
    'how to make audio louder without distortion': 'how-to-make-audio-louder-without-distortion',
    'export audio for spotify': 'how-to-export-audio-for-spotify-and-apple-podcasts',
    'export audio for apple podcasts': 'how-to-export-audio-for-spotify-and-apple-podcasts',
    'how to make voice sound warmer': 'how-to-make-a-voice-sound-warmer',
    'isolate voice from background music': 'how-to-isolate-a-voice-from-background-music',
    'record voice on laptop microphone': 'how-to-record-a-voice-on-a-laptop-microphone',
    'record remote podcast guest': 'how-to-record-a-remote-podcast-guest',
    'clean up interview recording': 'how-to-clean-up-an-interview-recording',
    'remove wind noise from audio': 'how-to-remove-wind-noise-from-audio',
    'remove plosives from voice recording': 'blog/remove-mic-pops-plosives',
    'how to remove plosives mic pops': 'blog/remove-mic-pops-plosives',
    'clean up audio for podcast': 'podcast-sound-professional-on-a-budget',
    'how to remove ums from audio': 'edit-a-podcast-by-its-words',
    'how to make a podcast sound better': 'podcast-sound-professional-on-a-budget',
    'phone voiceover sounds professional': 'record-a-voiceover-on-your-phone',
    'what lufs for podcast': 'loudness-for-youtube-podcasts-and-spotify',
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
    for q, path in RESEARCH_QUERIES.items():
        add(q, 'informational' if q.startswith(('what', 'how')) else 'commercial', 'awareness' if q.startswith(('what', 'how')) else 'consideration', path, 'research')
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
