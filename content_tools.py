"""Copy for the free in-browser tools (each tool is its own page) and the tools hub.
Honesty rules: the tools run in the visitor's browser, nothing is uploaded; accuracy limits are stated plainly."""

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
    desc='Free vocal quality checker: drop in a recording to see clipping, noise, rumble and level problems with plain-English fixes. Private, in your browser.',
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
    title='Free Music Tools: BPM, Key, Chord Finder & LUFS Meter',
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


# ------------------------------------------------------------------------------------------------- live tools (microphone in the browser)
TOOLS['live-autotune'] = dict(
    title='Live Autotune Recorder: Sing With Autotune Online (Free)',
    desc='Free live autotune in your browser. Turn on your mic, pick a key, hear yourself autotuned in real time and record the take. Private: nothing is uploaded.',
    h1='Live Autotune Recorder: Sing With Autotune Online, Free',
    short='Live Autotune', blurb='Sing with real-time autotune and record the take.', icon='mic', color='pink',
    kind='live', focus='all', tap=False, kw='live autotune online',
    lead=('Turn on your microphone, pick a key, and hear yourself with autotune in real time. Record the take and download it as a WAV. '
          'It runs in your browser with no install and no sign-up, and your voice is never uploaded.'),
    how=['Put on headphones, then click <strong>Turn on microphone</strong> and allow access.',
         'Pick the key of your beat (or let the <a href="/vocalforge/tools/song-key-finder">key finder</a> tell you), then choose Natural, Pop or Hard-tune.',
         'Press <strong>Record</strong>, sing, press <strong>Stop and save</strong>, then play it back or download the WAV.'],
    body='''
<h2>How the live autotune works</h2>
<p>Your microphone goes into a small pitch detector that finds the note you are singing about two hundred times a second. Each time, it picks the nearest note in the scale you chose and shifts your voice there. <strong>Retune speed</strong> sets how fast it moves: instant gives the hard, robotic effect, and slower gives a natural correction. <strong>Strength</strong> sets how much of the correction you hear. The grey line in the picture is what you sang; the pink line is what you hear.</p>
<h2>Which setting should I use?</h2>
<table><tr><th>Preset</th><th>Strength</th><th>Retune speed</th><th>Good for</th></tr>
<tr><td>Natural</td><td>55%</td><td>120 ms</td><td>Gentle polish on ballads and soft vocals</td></tr>
<tr><td>Pop</td><td>80%</td><td>50 ms</td><td>Modern melodic rap and pop</td></tr>
<tr><td>Hard-tune</td><td>100%</td><td>instant</td><td>The T-Pain / trap robotic sound</td></tr></table>
<h2>Set the right key first</h2>
<p>Autotune pulls every note toward the scale you pick, so a wrong key makes things sound worse, not better. If you do not know the key of your beat, drop it into the <a href="/vocalforge/tools/song-key-finder">song key finder</a>. If you are unsure between major and minor, try the relative key it shows.</p>
<h2>Tips for a clean result</h2>
<ul>
<li><strong>Use headphones.</strong> Speakers feed your voice back into the mic and cause howling.</li>
<li><strong>Sing close and steady.</strong> The detector works best on one clear note at a time. Loud background sound confuses it.</li>
<li><strong>Expect a little delay.</strong> A browser adds some latency, which depends on your computer and audio device. A wired headset and Chrome or Edge on desktop give the smallest delay.</li>
<li><strong>Keep the dry take if it matters.</strong> This tool records the autotuned sound. For a final track, record clean and tune it afterwards with better settings.</li>
</ul>
<h2>Browser versus a full studio tool</h2>
<p>This is a fast, free, real-time effect, great for practising, writing and trying ideas. The VocalForge desktop app does the same job offline with higher quality: it analyses the whole take, tunes it to the key of your beat, cleans noise and echo, fits the timing and masters the result.</p>
''',
    faq=[('Is the live autotune free?', 'Yes. No sign-up, no time limit and no watermark.'),
         ('Does it upload my voice?', 'No. The microphone is processed inside your browser and recordings stay on your device until you download them.'),
         ('Why do I hear a delay?', 'Every browser and audio device adds some latency. Use wired headphones, close other audio apps, and use Chrome or Edge on a computer for the lowest delay. Wireless headphones add noticeably more.'),
         ('Can I use a beat with it?', 'Yes. Use the karaoke autotune page: it plays your backing track, sets the key automatically, and records your voice and the mix.'),
         ('Why does it sound robotic?', 'Retune speed is set to instant on Hard-tune. Pick Natural or Pop, lower the strength, or slow the retune speed for a more natural sound.')],
    related=['karaoke-autotune', 'song-key-finder', 'vocal-checker'],
    guide_links=['autotune-for-rap-vocals', 'fix-vocals-recorded-on-phone'],
)

TOOLS['karaoke-autotune'] = dict(
    title='Online Karaoke With Autotune (Free): Sing Along to Any Song',
    desc='Free online karaoke with live autotune. Add any song or backing track, sing along with autotune on, and record your voice and the mix. Private, in your browser.',
    h1='Online Karaoke With Autotune: Sing Along to Any Track, Free',
    short='Karaoke Autotune', blurb='Sing along to any track with live autotune and record the mix.', icon='karaoke', color='violet',
    kind='karaoke', focus='all', tap=False, kw='online karaoke with autotune',
    lead=('Add a backing track, sing along with live autotune, and record your voice and the mix. '
          'It finds the key of the track for you, can reduce the original vocals, shows the lyrics, and everything stays in your browser.'),
    how=['Add your backing track (an instrumental works best). The key is detected and autotune is set to it.',
         'Put on headphones, click <strong>Turn on microphone</strong>, and paste your lyrics if you want them on screen.',
         'Press <strong>Record</strong>. After a 3-2-1 count the track plays and you sing. Stop to get your voice and the mix as WAV files.'],
    body='''
<h2>How online karaoke with autotune works</h2>
<p>Your backing track plays through the browser and your microphone goes through live autotune that is tuned to the track&rsquo;s key. You hear both in your headphones. When you record, you get two files: your autotuned voice on its own, and your voice mixed with the track, lined up to compensate for the audio delay of your device.</p>
<h2>Using a full song instead of an instrumental</h2>
<p>If you only have the original song, tick <strong>Reduce original vocals</strong>. It removes whatever is mixed in the centre of the stereo picture, which is where the lead vocal usually sits. This works on many songs but not all, and it also takes some bass and snare with it, so it is a quick karaoke trick, not a studio separation. For a clean vocal-free version, VocalForge uses an AI separation model on your own PC.</p>
<h2>Get the best sound</h2>
<ul>
<li><strong>Headphones are essential.</strong> Otherwise the track leaks into your mic and the recording gets messy.</li>
<li><strong>Check the key.</strong> The detected key is shown. If notes feel pulled the wrong way, try the relative major or minor.</li>
<li><strong>Use the sync slider.</strong> If your voice feels slightly early or late against the track in the saved mix, nudge it a few milliseconds and record again.</li>
<li><strong>Balance the mix.</strong> Use the voice and track sliders so you can hear yourself clearly without shouting.</li>
</ul>
<h2>Use music you have the right to use</h2>
<p>Your files never leave your device, but copyright still applies to what you publish. For videos you plan to post, use your own beat, licensed instrumentals or royalty-free music.</p>
<h2>Want a studio version of your take?</h2>
<p>Record here for fun, then run a clean take through the <a href="/vocalforge">VocalForge</a> desktop app: it removes noise and echo, tunes to the key of your beat, fits the timing and masters the result.</p>
''',
    faq=[('Is the karaoke free?', 'Yes. No account, no limits and no watermark.'),
         ('Are my songs or my voice uploaded?', 'No. The track, your microphone and the recordings all stay in your browser unless you download them.'),
         ('Can I sing along to any song?', 'Yes, any audio file your browser can play. Instrumentals work best. For a full song, tick Reduce original vocals.'),
         ('Why is my voice slightly off from the track in the recording?', 'Different devices add different delay. Use the sync slider to nudge the voice earlier or later, and record again.'),
         ('Does it work on a phone?', 'It can, but phones have more audio delay and fewer controls. A computer with wired headphones works best.')],
    related=['live-autotune', 'bpm-finder', 'song-key-finder'],
    guide_links=['autotune-for-rap-vocals', 'mix-vocals-on-a-beat'],
)



# ------------------------------------------------------------------------------------------------- noise-cancelling mic tools
TOOLS['clean-streaming-mic'] = dict(
    title='Noise Cancelling Mic Online for Streaming (Free, Live)',
    desc='Free live noise cancelling for your mic. Learns your room noise, cleans it in real time and feeds OBS, Discord or Zoom. Private, in your browser.',
    h1='Clean Streaming Mic: Live Noise Cancellation for OBS, Discord and Zoom',
    short='Clean Streaming Mic', blurb='Learn your room noise, remove it live and feed OBS, Discord or Zoom.', icon='denoise', color='teal',
    kind='stream', focus='all', tap=False, kw='noise cancelling mic for streaming',
    lead=('Turn on your mic, let it learn the background noise in your room, and it removes that noise in real time. '
          'Add autotune, reverb, echo or a doubler if you like, then send the clean mic to OBS, Discord, Zoom or Teams. It runs in your browser and your voice is never uploaded.'),
    how=['Click <strong>Turn on microphone</strong>, then <strong>Learn my room noise</strong> and stay silent for 3 seconds.',
         'Adjust <strong>Noise removal</strong> until the background is gone but your voice still sounds natural. Tick <strong>Hear original</strong> to compare.',
         'Pick an <strong>output device</strong> (a virtual cable) and choose that cable as the microphone in OBS, Discord or Zoom.'],
    body=r"""
<h2>How the noise cancelling works</h2>
<p>Most mic noise is steady: a PC fan, an air conditioner, a hiss, a hum. When you press <strong>Learn my room noise</strong>, the tool listens to three seconds of that room tone and remembers its sound at every pitch. While you talk, it turns down only the parts of the sound that match that noise, and it closes a gentle gate between words. It adapts to <em>your</em> room, which is why it can beat a generic filter.</p>
<h2>Connect it to OBS, Discord, Zoom or Teams</h2>
<p>A web page cannot create a new microphone by itself, so the clean sound needs a path into your other apps. There are two easy ways:</p>
<ol>
<li><strong>A virtual audio cable (works with every app).</strong> Install a free one: <em>VB-Cable</em> on Windows or <em>BlackHole</em> on Mac. In this page, set <strong>Send clean mic to</strong> the cable&rsquo;s input (&ldquo;CABLE Input&rdquo;). In OBS, Discord, Zoom or Teams, choose the cable&rsquo;s output (&ldquo;CABLE Output&rdquo;) as your microphone.</li>
<li><strong>OBS only, no install:</strong> in OBS (version 28 or newer on Windows 10/11) add an <em>Application Audio Capture</em> source and pick your browser window. It captures the browser&rsquo;s audio, which includes this page. Mute other tabs so only this page plays.</li>
</ol>
<p>Keep this tab open while you stream. Choosing an output device works in Chrome and Edge on a computer.</p>
<h2>Good starting settings</h2>
<table><tr><th>Noise</th><th>Reduction</th><th>Sensitivity</th><th>Notes</th></tr>
<tr><td>Light hiss or hum</td><td>12&ndash;15 dB</td><td>1.3</td><td>Sounds most natural</td></tr>
<tr><td>PC fan or air conditioner</td><td>18 dB</td><td>1.6</td><td>The default; keep the gate on</td></tr>
<tr><td>Loud steady noise</td><td>24&ndash;30 dB</td><td>2.0&ndash;3.0</td><td>Voice may sound slightly thinner</td></tr></table>
<h2>Autotune and effects for streamers</h2>
<p>The same page can add real-time <strong>autotune</strong> (pick the key and a Natural, Pop or Hard-tune style), <strong>reverb</strong>, <strong>echo</strong> and a <strong>doubler</strong>. They run after the noise removal, so you add effects to a clean voice. Voice polish adds a gentle high-pass, a touch of presence and light compression.</p>
<h2>What it cannot do</h2>
<ul>
<li>It cannot remove <strong>other voices</strong>, music or a TV, because those sound like speech.</li>
<li>Sudden sounds such as <strong>keyboard clatter</strong> and mouse clicks are only reduced, not removed.</li>
<li>If you use it with headphones, set the output so you do not hear yourself twice.</li>
</ul>
<p>For recordings that must be perfect, the VocalForge desktop app also removes echo, clicks and mouth noise and masters the result.</p>
""",
    faq=[('Is the noise cancelling free?', 'Yes. No account, no time limit and no watermark.'),
         ('Does it upload my voice?', 'No. Your microphone is processed inside your browser, and nothing is sent to a server.'),
         ('How do I use it in Discord, Zoom or OBS?', 'Install a free virtual audio cable (VB-Cable on Windows, BlackHole on Mac), send this page&rsquo;s output to the cable, and choose the cable as the microphone in your app. In OBS you can alternatively use Application Audio Capture on your browser.'),
         ('What kind of noise does it remove?', 'Steady noise: fans, air conditioning, hiss and hum. It cannot remove other people talking or music.'),
         ('Will it add delay?', 'About 11 milliseconds from the noise removal, plus your browser and audio device. That is small enough for streaming and calls.')],
    related=['voice-recorder-noise-cancellation', 'live-autotune', 'vocal-checker'],
    guide_links=['fix-vocals-recorded-on-phone', 'remove-echo-from-vocal-recording'],
)

TOOLS['voice-recorder-noise-cancellation'] = dict(
    title='Voice Recorder With Noise Cancellation (Free, Online)',
    desc='Free online voice recorder with noise cancellation. Record voice-overs and content with live noise removal, or clean an existing recording. Private, in your browser.',
    h1='Online Voice Recorder With Noise Cancellation for Content and Voice-Overs',
    short='Noise-Free Voice Recorder', blurb='Record voice-overs with live noise removal, or clean an existing file.', icon='record', color='blue',
    kind='record', focus='all', tap=False, kw='voice recorder with noise cancellation',
    lead=('Record voice-overs, YouTube and TikTok narration, podcasts and voice notes with live noise cancellation, and download a clean WAV. '
          'You can also drop in an existing recording to remove its background noise. Autotune and effects are optional, and nothing is uploaded.'),
    how=['Click <strong>Turn on microphone</strong>, press <strong>Learn my room noise</strong> and stay quiet for 3 seconds.',
         'Press <strong>Record</strong>, speak, then <strong>Stop and save</strong>. You get a clean WAV and an untouched original.',
         'Or skip the mic: drop a recording into <strong>Clean an existing recording</strong> and download the cleaned file.'],
    body=r"""
<h2>Record clean audio without a studio</h2>
<p>Most home recordings are ruined by steady background noise: a fan, a hiss, a hum from the computer. This recorder learns the noise in your room from a few seconds of silence and removes it while you record, so the file you download is already clean. You also get the <strong>original</strong> untouched take, in case you want to process it differently later.</p>
<h2>Clean a recording you already have</h2>
<p>Drop a voice note, a phone video&rsquo;s audio or a podcast take into <strong>Clean an existing recording</strong>. The tool looks for the quietest part of the file to learn the noise from. If the recording has no real silence, it tracks the noise level automatically instead. Then it removes the noise and gives you a before-and-after player and a WAV download. Tick <em>Normalize</em> to bring the level up for voice-overs.</p>
<h2>Autotune and effects for content</h2>
<p>Optional real-time <strong>autotune</strong>, <strong>reverb</strong>, <strong>echo</strong> and a <strong>doubler</strong> run after the noise removal, so effects are added to a clean voice. Use headphones when monitoring, and leave effects off for plain voice-overs.</p>
<h2>Tips for the cleanest result</h2>
<ul>
<li><strong>Record in a soft room.</strong> Curtains, a sofa or a wardrobe full of clothes beat a bare room. Noise removal cannot take echo out.</li>
<li><strong>Stay 10 to 20 cm from the mic</strong> and speak across it, not into it.</li>
<li><strong>Turn off the loudest noise:</strong> fan, air conditioning, notifications.</li>
<li><strong>Use the gentlest setting that works.</strong> Heavy reduction can make a voice sound thin or watery. Tick <em>Hear original</em> to compare.</li>
</ul>
<h2>What it cannot do</h2>
<p>It cannot remove other voices, music, or sudden sounds like clicks and coughs, and it cannot remove room echo. For that, the <a href="/vocalforge">VocalForge desktop app</a> adds echo reduction, click and mouth-noise repair, levelling and mastering.</p>
""",
    faq=[('Is the voice recorder free?', 'Yes. No account, no limit on length, and no watermark.'),
         ('Does it upload my recording?', 'No. Recording, noise removal and downloads all happen in your browser.'),
         ('Can I clean a recording I already made?', 'Yes. Drop it into the &ldquo;Clean an existing recording&rdquo; box. It works on MP3, WAV, FLAC and OGG files and gives you a cleaned WAV.'),
         ('What file do I get?', 'A 16-bit WAV. You also get the original untouched recording from the live recorder.'),
         ('Why does my voice sound thin?', 'The reduction is too strong. Lower the Reduction slider or the Sensitivity, and compare with Hear original.')],
    related=['clean-streaming-mic', 'live-autotune', 'vocal-checker'],
    guide_links=['fix-vocals-recorded-on-phone', 'remove-echo-from-vocal-recording'],
)

TOOL_ORDER = ['live-autotune', 'karaoke-autotune', 'clean-streaming-mic', 'voice-recorder-noise-cancellation', 'bpm-finder', 'song-key-finder', 'chord-finder', 'lufs-meter', 'vocal-checker']
