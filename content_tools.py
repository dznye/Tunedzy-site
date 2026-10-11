"""Copy for the free in-browser tools (each tool is its own page) and the tools hub.
Honesty rules: the tools run in the visitor's browser, nothing is uploaded; accuracy limits are stated plainly."""

TOOL_ORDER = ['bpm-finder', 'song-key-finder', 'chord-finder', 'lufs-meter', 'vocal-checker']


def delay_table(bpms=(80, 90, 120, 140)):
    rows = ''
    for b in bpms:
        q = 60000 / b
        rows += f'<tr><td>{b}</td><td>{q:.0f} ms</td><td>{q / 2:.0f} ms</td><td>{q * 0.75:.0f} ms</td><td>{q / 4:.0f} ms</td></tr>'
    return ('<table><tr><th>BPM</th><th>1/4 note</th><th>1/8 note</th><th>dotted 1/8</th><th>1/16 note</th></tr>' + rows + '</table>')


TOOLS = {}

TOOLS['bpm-finder'] = dict(
    title='BPM Finder: Detect the Tempo of Any Song (Free)',
    desc='Free BPM finder and tap tempo. Drop in any song or beat and get the BPM in seconds. Private: your file never leaves your browser.',
    h1='Free BPM Finder: Detect the Tempo of Any Song or Beat',
    short='BPM Finder', blurb='Drop in a song or beat, get the tempo. Includes tap tempo.', icon='tempo', color='amber',
    focus='bpm', tap=True, kw='bpm finder',
    lead=('Drop in an MP3, WAV or FLAC and get the BPM in a few seconds. You also get a tap-tempo button for when you want to check by feel. '
          'Everything runs inside your browser, so your unreleased beat is never uploaded.'),
    how=['Drop your song, beat or voice memo into the box (or click it to choose a file).',
         'Wait a few seconds while it listens. Long files are analysed from the middle two and a half minutes.',
         'Read the BPM. If it is half or double what you expected, click the alternative tempo shown under it.'],
    body='''
<h2>How the BPM finder works</h2>
<p>It looks for the moments where the music gets suddenly louder in different frequency bands (kicks, snares, hats, plucked notes), then measures how regularly those moments repeat. The repeat rate that fits best across the whole track is the tempo. After the first guess it fine-tunes in steps of a twentieth of a BPM, which is why you can see numbers like 92.4.</p>
<h2>Why does it sometimes say 70 when I count 140?</h2>
<p>Tempo has a built-in ambiguity: a track at 70 BPM and the same track felt at 140 BPM have identical hits, just counted differently. It is especially common in trap, drill and slow R&amp;B, where the hi-hats run twice as fast as the snare. Both numbers are &ldquo;right&rdquo;; use whichever your DAW project or your collaborator uses. The alternatives are shown right under the main result so you can switch with one click.</p>
<h2>Why BPM matters for vocals</h2>
<ul>
<li><strong>Delay and echo times.</strong> A delay set to a note length stays in time with the beat. The table below shows the milliseconds for common tempos.</li>
<li><strong>Reverb pre-delay and tails.</strong> A tail that decays just before the next beat keeps the vocal clear.</li>
<li><strong>Timing fixes.</strong> Tools that nudge words onto the beat need the right tempo grid first.</li>
<li><strong>Matching takes.</strong> Recording a new verse to a beat you downloaded means the project tempo has to match the beat.</li>
</ul>
''' + delay_table() + '''
<p class="note">Milliseconds = 60,000 divided by BPM, then divided or multiplied for the note length.</p>
<h2>Tips for a more accurate reading</h2>
<ul>
<li>Use the full mix or the beat on its own. A solo acapella has no steady pulse to lock onto.</li>
<li>Songs with tempo changes, live drumming or long drum-free intros will read less confidently. The confidence bar tells you when to double-check with tap tempo.</li>
<li>Tap on the snare or the kick, not on the vocal.</li>
</ul>
''',
    faq=[('How accurate is this BPM finder?',
          'On music with a steady drum pattern it normally matches DAW and DJ software to within a fraction of a BPM, apart from the half-time and double-time ambiguity explained above. On live or free-tempo music it is less certain, and it tells you so.'),
         ('Is my audio uploaded anywhere?',
          'No. The file is decoded and analysed by your own browser. There is no upload step, and you can disconnect from the internet after the page loads and it still works.'),
         ('What is tap tempo?',
          'You tap a button on every beat and it averages the gaps between taps into a BPM. It is the fastest way to check a result by feel.'),
         ('Which file types work?',
          'MP3, WAV, FLAC and OGG work everywhere. M4A works in most browsers.')],
    related=['song-key-finder', 'chord-finder', 'lufs-meter'],
    guide_links=['mix-vocals-on-a-beat', 'autotune-for-rap-vocals'],
)

TOOLS['song-key-finder'] = dict(
    title='Song Key Finder: What Key Is This Song In? (Free)',
    desc='Free song key finder. Drop in a song or beat and see its key, the Camelot code and the relative key. Runs in your browser, nothing uploaded.',
    h1='Free Song Key Finder: Find the Key of Any Song or Beat',
    short='Key Finder', blurb='Find the key and Camelot code of any song or beat.', icon='key', color='violet',
    focus='key', tap=False, kw='song key finder',
    lead=('Drop in a song or beat and see what key it is in, with the Camelot code for DJ mixing and the relative key. '
          'Use it to set your autotune, write a topline, or match a vocal to a beat you downloaded. It runs in your browser and nothing is uploaded.'),
    how=['Drop in the full beat or song (a beat with its melody gives the best result).',
         'Read the key and the Camelot code. The &ldquo;same notes as&rdquo; line shows the relative major or minor.',
         'Set your autotune or your keyboard to that key and record.'],
    body='''
<h2>How the key finder works</h2>
<p>It measures how much energy the track has at each of the 12 musical notes over time, ignoring which octave they are in, to build a fingerprint of the notes the music uses most. It then compares that fingerprint to the typical pattern of every major and minor key and shows the best match, plus the runners-up so you can see when it is a close call.</p>
<h2>Relative keys: why &ldquo;C major&rdquo; and &ldquo;A minor&rdquo; are the same notes</h2>
<p>Every major key shares its seven notes with a minor key three semitones down. C major and A minor use exactly the same white keys. A song can feel major or minor depending on which note feels like home, and a detector can only guess from the balance of the notes. If the result is a close call, try the relative key too. For autotune, either one works, because the note set is identical.</p>
<h2>What the Camelot code is for</h2>
<p>DJs label keys on a wheel (1A to 12B) so they can see which songs mix harmonically. Neighbouring numbers, or the same number with the other letter, sound good together. The finder shows the code next to the key so you can sort a crate or a beat folder by it.</p>
<h2>Using the key with your vocal</h2>
<ul>
<li><strong>Autotune:</strong> set the scale to the detected key. Notes outside the scale get pulled to the nearest note inside it. See <a href="/vocalforge/autotune-for-rap-vocals">autotune for rap vocals</a> for settings.</li>
<li><strong>Toplines and ad-libs:</strong> sing or hum notes from the key, and use the <a href="/vocalforge/tools/chord-finder">chord finder</a> to see what chords the beat plays.</li>
<li><strong>Harmonies:</strong> stack thirds and fifths above your lead using the same scale.</li>
</ul>
<h2>When the result can be wrong</h2>
<ul>
<li>Beats that are mostly drums and 808 with no melody give little to work with.</li>
<li>Tracks that change key part-way (modulations) are summarised as one key.</li>
<li>Heavily detuned or atonal sounds, and some blues-style tracks that mix major and minor, are ambiguous by nature.</li>
</ul>
''',
    faq=[('How accurate is the key finder?',
          'On music with a clear melody or chords it usually agrees with other key detectors, including picking the relative key. It is weaker on drum-heavy beats with little melody, and it shows its confidence so you know.'),
         ('Can it find the key of an acapella vocal?',
          'It can give a rough answer from the notes sung, but a full beat or chord part is far more reliable.'),
         ('What if my vocal sounds off after tuning to this key?',
          'Try the relative key, or turn the amount of correction down. If the beat itself changes key, tune each section separately.'),
         ('Is my audio uploaded anywhere?', 'No. Everything runs in your browser.')],
    related=['bpm-finder', 'chord-finder', 'vocal-checker'],
    guide_links=['autotune-for-rap-vocals', 'fix-vocals-recorded-on-phone'],
)

TOOLS['chord-finder'] = dict(
    title='Chord Finder: Find the Chords of Any Song (Free)',
    desc='Free chord finder. Drop in a song and see the chord progression, the repeating loop and Roman numerals. Runs in your browser, nothing uploaded.',
    h1='Free Chord Finder: See the Chords in Any Song or Beat',
    short='Chord Finder', blurb='See the chord progression and the loop it repeats.', icon='chords', color='pink',
    focus='chords', tap=False, kw='chord finder',
    lead=('Drop in a song or beat and see its chord progression, the loop it repeats, and what each chord is in the key (I, IV, vi and so on). '
          'It is built for songwriters and vocalists who want to know what is underneath the beat. Runs in your browser, nothing uploaded.'),
    how=['Drop in a song or a beat with a melody part (piano, guitar, synth, pads or strings).',
         'Read the loop at the top, then the timeline of chords underneath (hover a chord to see when it starts).',
         'Use the loop as a map for your topline, harmonies or ad-libs.'],
    body='''
<h2>How the chord finder works</h2>
<p>It first finds the tempo and key, then splits the track into two-beat slices. For each slice it measures the strength of the 12 notes and picks the major or minor chord whose notes fit best, with a small preference for chords that belong to the song&rsquo;s key. Neighbouring slices with the same chord are merged, and the most repeated sequence is shown as the loop.</p>
<h2>Reading the Roman numerals</h2>
<p>The small label under each chord says where it sits in the key. In a major key, I is home, IV and V are the strong supporting chords, and vi (the relative minor) is the sad one. In a minor key, i is home, with VI, III and VII as the common companions. Many hit songs are built from just four of these in a loop, so seeing the numerals makes the pattern obvious.</p>
<table><tr><th>Loop</th><th>In C major</th><th>Typical feel</th></tr>
<tr><td>vi &ndash; IV &ndash; I &ndash; V</td><td>Am &ndash; F &ndash; C &ndash; G</td><td>emotional, anthemic</td></tr>
<tr><td>I &ndash; V &ndash; vi &ndash; IV</td><td>C &ndash; G &ndash; Am &ndash; F</td><td>bright, pop</td></tr>
<tr><td>i &ndash; VI &ndash; III &ndash; VII</td><td>Am &ndash; F &ndash; C &ndash; G (in A minor)</td><td>dark but uplifting, trap and R&amp;B</td></tr></table>
<h2>What it can and cannot do</h2>
<ul>
<li>It shows <strong>major and minor triads</strong>. Sevenths, ninths, suspended and slash chords are heard as their nearest triad, so check by ear if a chord feels richer than shown.</li>
<li>It works best on <strong>harmonic</strong> parts. Drum-and-808 beats with a sparse melody give fewer clear chords.</li>
<li>Chord timing is placed on a two-beat grid, so quick changes inside a bar are merged.</li>
</ul>
<h2>Using chords with your vocal</h2>
<p>Aim long notes at the chord tones (the root, third and fifth), let passing words sit on other notes of the scale, and end phrases on a chord tone. Pair this with the <a href="/vocalforge/tools/song-key-finder">key finder</a> to set your autotune to the right scale.</p>
''',
    faq=[('Is the chord finder accurate?',
          'It is a good starting point for the main progression, not a transcription. It is strongest on clear chordal music and weakest on busy, distorted or very sparse tracks. The loop is usually right even when a single chord is off.'),
         ('Why does it not show 7th chords?',
          'It reports plain major and minor triads to stay reliable. A Cmaj7 will usually show as C, and an Am7 as Am.'),
         ('Does it work on a vocal-only file?',
          'A solo vocal has only one note at a time, so there is little harmony to read. Use the beat or the full song.'),
         ('Is my audio uploaded anywhere?', 'No. It is analysed entirely in your browser.')],
    related=['song-key-finder', 'bpm-finder', 'vocal-checker'],
    guide_links=['mix-vocals-on-a-beat', 'future-vocal-effect-settings'],
)

TOOLS['lufs-meter'] = dict(
    title='LUFS Meter: Check Your Song\'s Loudness (Free Online)',
    desc='Free online LUFS meter. Drop in a mix or master and see integrated LUFS, true peak and loudness range, and what Spotify, YouTube and Apple Music would do to it.',
    h1='Free LUFS Meter: Check How Loud Your Song Is',
    short='LUFS Meter', blurb='Integrated LUFS, true peak and streaming targets.', icon='meter', color='teal',
    focus='loud', tap=False, kw='lufs meter',
    lead=('Drop in your mix or master and see its integrated loudness in LUFS, its estimated true peak and loudness range, '
          'plus what Spotify, YouTube and Apple Music would do to it. Measured with the standard ITU-R BS.1770 method, in your browser, with no upload.'),
    how=['Drop in your exported mix or master (WAV or FLAC is best; MP3 is fine for a quick check).',
         'Read the LUFS number. Compare it with the platform table underneath.',
         'If you are far off, adjust the level or limiter in your DAW, export again and re-check.'],
    body='''
<h2>What LUFS means</h2>
<p>LUFS (Loudness Units relative to Full Scale) is a measure of how loud a track <em>sounds</em>, not just how high its peaks are. It weights frequencies the way human hearing does and averages over the whole track, ignoring silence. Streaming services use it to level songs against each other so you do not have to reach for the volume knob between tracks.</p>
<h2>Streaming loudness targets</h2>
<table><tr><th>Platform</th><th>Approx. target</th><th>Behaviour</th></tr>
<tr><td>Spotify</td><td>&minus;14 LUFS (default setting)</td><td>Turns loud tracks down; can turn quiet tracks up</td></tr>
<tr><td>YouTube</td><td>about &minus;14 LUFS</td><td>Turns loud tracks down; does not boost quiet ones</td></tr>
<tr><td>Apple Music (Sound Check)</td><td>&minus;16 LUFS</td><td>Adjusts both ways when Sound Check is on</td></tr>
<tr><td>Tidal</td><td>about &minus;14 LUFS</td><td>Normalises when the setting is on</td></tr></table>
<p class="note">Platforms change their settings from time to time, and listeners can switch normalisation off. Treat these as a guide and check the platform&rsquo;s current documentation.</p>
<h2>Do I have to master to &minus;14?</h2>
<p>No. If your master is louder than the target, the platform simply lowers it, so being much louder gains nothing and costs dynamics. If you want the best result, finish with a true peak a little under 0 dBFS (many engineers use &minus;1 dBTP) so converted MP3 or AAC versions do not clip, and keep the loudness in the &minus;14 to &minus;9 LUFS range your genre expects.</p>
<h2>True peak and loudness range</h2>
<ul>
<li><strong>True peak</strong> estimates the height of the waveform between samples, which can be higher than the sample peaks and is what causes clipping after lossy encoding. The figure here is an estimate from 4x oversampling.</li>
<li><strong>Loudness range (LRA)</strong> shows how much the loudness moves between quiet and loud sections. Dense, modern pop and rap often sit at 3&ndash;6 LU.</li>
</ul>
<h2>Measuring a vocal on its own</h2>
<p>Vocals are not mastered to streaming targets by themselves, but the number is still useful: a vocal that measures far below the beat&rsquo;s section loudness usually needs more level or compression. The <a href="/vocalforge/tools/vocal-checker">vocal checker</a> looks at the other health signs.</p>
''',
    faq=[('Is this the same as the loudness meters in mastering software?',
          'It follows the same ITU-R BS.1770 / EBU R128 method: K-weighting, 400 ms blocks and the standard two-stage gate. Results typically agree with professional meters to within about a tenth of a dB. The true peak is an estimate.'),
         ('What LUFS should my song be?',
          'Streaming services normalise to around &minus;14 LUFS, but many loud genres are mastered hotter (about &minus;9 to &minus;7) and the platform turns them down. Master for how it sounds, and make sure the true peak is safe.'),
         ('Does the format matter?',
          'Measure your WAV or FLAC master if you can. An MP3 can read slightly differently from the file it came from.'),
         ('Is my audio uploaded anywhere?', 'No. The measurement runs in your browser.')],
    related=['vocal-checker', 'bpm-finder', 'song-key-finder'],
    guide_links=['mix-vocals-on-a-beat', 'vocal-cleanup-software-compared'],
)

TOOLS['vocal-checker'] = dict(
    title='Vocal Quality Checker: Is Your Vocal Ready to Post?',
    desc='Free vocal quality checker. Drop in a vocal recording and see clipping, background noise, rumble and level problems, with plain-English fixes. Private, in your browser.',
    h1='Free Vocal Quality Checker: Is Your Recording Ready to Post?',
    short='Vocal Checker', blurb='Spot clipping, noise, rumble and level problems.', icon='check', color='blue',
    focus='check', tap=False, kw='vocal quality checker',
    lead=('Drop in a vocal recording and get a quick health check: clipping, background noise, low rumble and level problems, each with a plain-English fix. '
          'It is the same kind of analysis VocalForge runs before it cleans a take, and it runs in your browser so your recording stays private.'),
    how=['Drop in your vocal take (an acapella, voice memo or phone recording works best).',
         'Read the verdict and the five checks. Green is fine, amber is worth a look, red is worth fixing.',
         'Fix what is flagged (the tips below), or let VocalForge fix it for you in one pass.'],
    body='''
<h2>What the checker looks for</h2>
<table><tr><th>Check</th><th>What it means</th><th>How to fix it</th></tr>
<tr><td>Clipping</td><td>Runs of samples stuck at full scale. They sound harsh or crunchy.</td><td>Re-record quieter (peaks around &minus;12 to &minus;6 dB). Small clips can be repaired with a declip tool.</td></tr>
<tr><td>Peak level</td><td>How close the loudest moment is to the digital ceiling.</td><td>Leave a few dB of headroom before processing.</td></tr>
<tr><td>Background noise</td><td>How quiet the quietest moments are. Hiss, fans, traffic and room tone live here. A take with no pauses reads as noisier than it is.</td><td>Record in a quiet, soft room. Light noise reduction, not heavy.</td></tr>
<tr><td>Low rumble</td><td>Energy below 80 Hz, which a voice does not need. Handling noise and desk thumps.</td><td>High-pass filter around 80 to 100 Hz.</td></tr>
<tr><td>Overall level</td><td>How loud the take is on the LUFS scale. Very quiet takes bring noise up when you boost them.</td><td>Record a little louder, peaks around &minus;12 to &minus;6 dB, and avoid heavy gain later.</td></tr></table>
<h2>What it cannot hear</h2>
<p>It does not judge pitch, timing, tone or performance, and it cannot reliably measure room echo. Those need your ears, or a full processing chain. Use the checker as a seatbelt check before you spend time mixing.</p>
<h2>The usual order of fixes</h2>
<ol>
<li>Fix the source if you can: closer mic, softer room, headphones on.</li>
<li>High-pass and gentle noise reduction.</li>
<li>De-ess, tune and compress.</li>
<li>Add space (reverb and delay) last.</li>
</ol>
<p>The full walkthrough is in <a href="/vocalforge/fix-vocals-recorded-on-phone">how to make phone vocals sound professional</a>, and if the recording is roomy, see <a href="/vocalforge/remove-echo-from-vocal-recording">how to remove echo from a vocal</a>.</p>
''',
    faq=[('Is this vocal checker AI?',
          'No. It uses standard audio measurements (level, noise floor, spectrum, clipping detection), which is why it is fast and private. VocalForge adds automatic analysis and an optional AI model for separating vocals from songs.'),
         ('Why does my clean take show a warning?',
          'Thresholds are deliberately cautious. Treat amber as &ldquo;take a look&rdquo;. If the recording sounds good to you, trust your ears.'),
         ('Can it check a full song?',
          'Yes, but the noise and level checks are written for a solo vocal. For a finished song, the LUFS meter is more useful.'),
         ('Is my audio uploaded anywhere?', 'No. Your file is analysed in your browser and never sent to a server.')],
    related=['lufs-meter', 'bpm-finder', 'song-key-finder'],
    guide_links=['fix-vocals-recorded-on-phone', 'remove-echo-from-vocal-recording'],
)

HUB = dict(
    title='Free Music Tools: BPM Finder, Key Finder, Chord Finder, LUFS Meter',
    desc='Free in-browser music tools: find the BPM, key and chords of any song, measure LUFS loudness, and check a vocal recording. Private: nothing is uploaded.',
    h1='Free Music Tools That Run in Your Browser',
    lead=('Drop in a song, beat or vocal and see its tempo, key, chords, loudness and vocal health in seconds. '
          'No sign-up, no upload: your audio is analysed on your own device.'),
    faq=[('Are these tools really free?', 'Yes. No sign-up, no limits and no watermarks. They are free forever.'),
         ('Do you keep my audio?', 'No. Files are decoded and analysed by your own browser. Nothing is sent to our servers.'),
         ('Why is it free?', 'These are the same kinds of checks VocalForge runs before it fixes a vocal. If they are useful, the Windows app does the fixing for you, with a free 7-day trial.'),
         ('Which browsers work?', 'Current Chrome, Edge, Firefox and Safari. Very old browsers may not support the audio features.')],
)

# ------------------------------------------------------------------------------------------------- one more guide (AI wording for search)
AI_GUIDE = dict(
    title='AI Vocal Cleanup: What It Can (and Can\'t) Fix',
    desc='What AI vocal cleanup really does, which problems it fixes well, which it does not, and how to get studio-sounding vocals from a phone or bedroom recording.',
    h1='AI Vocal Cleanup: What It Can and Can\'t Fix',
    kw='ai vocal cleanup',
    lead=('&ldquo;AI vocal cleanup&rdquo; covers everything from one-click noise removal to tools that tune, balance and master a rough take for you. '
          'Some of it is genuinely useful, some of it is marketing. Here is what it can fix, where it falls short, and how to use it without losing your sound.'),
    tldr=['AI is best at the boring, measurable jobs: noise, clicks, level, key detection, loudness.',
          'It is weaker at taste, and at rescuing a recording with heavy echo or distortion.',
          'Check where your audio goes: online AI tools usually upload it, desktop tools can keep it on your PC.',
          'Always keep the original take and compare before and after.'],
    body='''
<h2>What &ldquo;AI&rdquo; usually means in vocal tools</h2>
<ul>
<li><strong>Automatic analysis.</strong> The tool listens to your take and picks settings: how much noise to remove, where the harsh S sounds are, what key to tune to, how loud to set the vocal against a beat.</li>
<li><strong>Learned noise and reverb removal.</strong> Models trained on lots of audio separate speech or singing from background noise and room sound.</li>
<li><strong>Source separation.</strong> A model splits a full song into vocals, drums, bass and other, handy for studying a reference or pulling a vocal out of a beat.</li>
<li><strong>Generative voice tools.</strong> These replace or imitate a voice. That is a different thing from cleaning up your own recording.</li>
</ul>
<h2>What it fixes well</h2>
<ul>
<li>Steady background noise, hum and hiss</li>
<li>Level differences between phrases</li>
<li>Harsh S sounds and mouth clicks</li>
<li>Finding the key and tempo of a beat (try the free <a href="/vocalforge/tools/song-key-finder">key finder</a> and <a href="/vocalforge/tools/bpm-finder">BPM finder</a>)</li>
<li>Loudness and peak checks (see the <a href="/vocalforge/tools/lufs-meter">LUFS meter</a>)</li>
</ul>
<h2>Where it struggles</h2>
<ul>
<li><strong>Heavy room echo.</strong> Strong de-reverb leaves a thin, watery tone. Treat it as reduction, not removal.</li>
<li><strong>Clipping and distortion.</strong> Small clips can be repaired; heavily distorted takes cannot be rebuilt.</li>
<li><strong>Taste.</strong> How bright, wet or forward a vocal should be is a creative choice. Use AI for the first draft and finish by ear.</li>
<li><strong>Performance.</strong> No tool fixes a flat note delivered with no confidence. Tuning helps, a better take helps more.</li>
</ul>
<h2>Privacy: where does your audio go?</h2>
<p>Many free AI vocal tools run on a server, so your recording is uploaded. That is fine for a throwaway test and risky for an unreleased song. Tools that run on your own PC, like VocalForge, keep the audio local. Always check the privacy page of any online tool before uploading something you care about.</p>
<h2>A sensible workflow</h2>
<ol>
<li>Run the free <a href="/vocalforge/tools/vocal-checker">vocal checker</a> to see what is actually wrong.</li>
<li>Fix the source if you can (closer mic, softer room).</li>
<li>Let an automatic tool clean, tune and balance the take.</li>
<li>Compare to the original, adjust by ear, and export a 24-bit WAV.</li>
<li>Check loudness with the <a href="/vocalforge/tools/lufs-meter">LUFS meter</a> before you upload.</li>
</ol>
''',
    vf_title='AI-assisted cleanup that stays on your PC',
    vf='''<p>VocalForge analyses your recording, picks the settings, cleans, tunes to your beat&rsquo;s key, fits the flow, matches an artist&rsquo;s style if you give it a reference, and masters the result. It runs on your own PC, and the optional AI model handles vocal separation. Free 7-day trial.</p>''',
    faq=[('Is AI vocal cleanup better than manual cleanup?',
          'It is faster and more consistent for routine problems, and a skilled engineer still wins on taste and difficult recordings. Many people use the automatic result as a first draft.'),
         ('Can AI make a bad vocal sound studio quality?',
          'It can make a rough take much cleaner and more even. It cannot fully remove heavy echo, distortion or a poor performance. Recording closer to the mic in a soft room is still the biggest improvement.'),
         ('Is it safe to upload my unreleased vocal to an online AI tool?',
          'Check the tool\'s privacy policy. If you would rather not upload at all, use software that processes audio on your own computer.')],
    ai=None,
    related=['fix-vocals-recorded-on-phone', 'remove-echo-from-vocal-recording', 'vocal-cleanup-software-compared'],
)
