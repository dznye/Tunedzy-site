"""Page content for fuidzy.com/vocalforge. Plain HTML strings; build.py wraps them in the shared template.

Rules every page follows: answer the question first, give real steps, be honest about limits, never invent reviews,
ratings, customer counts or benchmarks, and keep product claims to what VocalForge actually does.
"""

SITE = 'https://fuidzy.com'
BASE = '/vocalforge'
PRODUCT_ID = 'pdt_0NpUhQriM4NqB6qcQZp3d'
BUY_URL = f'https://checkout.dodopayments.com/buy/{PRODUCT_ID}?quantity=1&redirect_url=https%3A%2F%2Ffuidzy.com%2Fvocalforge%2Fthanks'
DATE = '2026-10-13'
SUPPORT_EMAIL = 'fuidzy@outlook.com'
MAC_MAIL = f'mailto:{SUPPORT_EMAIL}?subject=VocalForge%20for%20Mac&body=Hi%2C%20I%27d%20like%20a%20Mac%20version%20of%20VocalForge.'
HELP_MAIL = f'mailto:{SUPPORT_EMAIL}?subject=VocalForge%20support'
LAUNCH_MAIL = f'mailto:{SUPPORT_EMAIL}?subject=Notify%20me%20when%20VocalForge%20launches&body=Please%20email%20me%20when%20the%20VocalForge%20download%20opens.'

NAV = [('Free tools', f'{BASE}/tools'), ('Features', f'{BASE}#features'), ('Guides', f'{BASE}#guides'), ('Pricing', f'{BASE}#pricing'), ('Support', f'{BASE}#support')]

# --------------------------------------------------------------------------------------------- shared FAQ
HUB_FAQ = [
    ('Is VocalForge free?',
     'You can download it and use everything free for 7 days. After the trial it is a one-time $29 for a lifetime license on up to two of your PCs. No subscription. '
     'The tools on this site (BPM finder, key finder, chord finder, LUFS meter and vocal checker) are free forever and run in your browser.'),
    ('Is VocalForge a plugin, a DAW or a standalone app?',
     'It is a standalone vocal workstation: the whole vocal chain (clean, tune, fit to the beat, style, mix and master) in one window, with live sliders and a painted-sections timeline. '
     'It exports 24-bit WAV, FLAC or MP3, and a DAW pack with every stem in sync plus tempo, key and a song map, so you can keep working in FL Studio, Ableton, Logic, Reaper or Pro Tools. It is not a DAW replacement and not a VST/AU plugin yet.'),
    ('Does it need an internet connection?',
     'Your audio is processed on your own PC, so your unreleased songs are not uploaded anywhere. The app checks your license online and '
     'keeps working for up to 60 days without internet after a successful check. The optional AI vocal-separation add-on is a one-time download.'),
    ('What happens when the free trial ends?',
     'You can still open projects and listen. Processing and exporting need a license key.'),
    ('How many computers can I use one license on?',
     'Two. If you get a new PC, deactivate the old one from the License screen to free the slot.'),
    ('Do I need a powerful computer or a GPU?',
     'No. Cleaning, tuning, mixing and mastering run on a normal Windows 10 or 11 PC with 8 GB of RAM or more. A recent NVIDIA graphics card only makes '
     'the optional AI vocal-separation step much faster; without one it still works, just slower.'),
    ('What file types can I use?',
     'WAV, FLAC, MP3 and OGG work out of the box. Exports are 24-bit WAV or FLAC, or MP3 320 kbps for quick sharing. M4A and AAC files work if ffmpeg is installed on your PC.'),
    ('What if my recording is really bad?',
     'VocalForge can repair a lot (noise, clicks, mic pops, harsh S sounds, clipped peaks, level swings, room echo), but it is not magic. A vocal buried in '
     'reverb, heavily distorted, or recorded far from the mic will improve but not become a studio take. Re-recording closer to the mic is always the best fix.'),
    ('Is this AI?',
     'It uses automatic analysis, so it listens to your recording and picks the settings for you, on top of signal processing that runs locally. '
     'An optional AI model (Demucs) handles one job: separating vocals from a full song, for example to study a reference track or pull a vocal out of a beat you downloaded.'),
    ('Can it make me sound like a specific artist?',
     'You can drop in any song by an artist whose sound you like. VocalForge measures how that record was tuned, EQ-ed, spaced and mixed and applies a similar '
     'treatment to your own voice. It changes the processing, not your voice, so you will still sound like you. VocalForge is not affiliated with any artist.'),
    ('Is there a Mac version?',
     'Not yet: Windows 10 and 11 (64-bit) only for now. Want one? Email fuidzy@outlook.com with the subject "VocalForge for Mac". Requests decide what we build next.'),
    ('How do I get help?',
     'Email fuidzy@outlook.com. Include what you were doing and, if you can, a screenshot. We read every message.'),
]

# --------------------------------------------------------------------------------------------- guides
GUIDES = {}

GUIDES['fix-vocals-recorded-on-phone'] = dict(
    title='Make Phone Vocals Sound Professional: Manual + AI Fixes',
    desc='Recorded vocals on your phone? Clean, tune and mix them step by step so they sit on a beat, plus how AI vocal cleanup can automate the boring parts.',
    h1='How to Make Vocals Recorded on a Phone Sound Professional',
    kw='phone vocals sound professional',
    lead=('A phone can capture a usable vocal. What makes it sound amateur is usually the room, the distance to the mic, and what happens after: '
          'no cleanup, no tuning, and no balance against the beat. Fix those four things in the right order and a phone take can sit next to a studio one.'),
    tldr=['Record close to the phone (a hand-width or two), in a small soft room, with headphones on.',
          'Clean first (high-pass, light noise reduction, de-ess), then tune, then compress, then add space last.',
          'Level the vocal against the beat by ear and by meter, and check it in mono.',
          'Export WAV and keep the dry take: you will want to redo the mix later.'],
    body='''
<h2>1. Record it right (this does 70% of the work)</h2>
<p>Everything after this step is repair. The closer you get to a clean, dry source, the less repair you need.</p>
<ul>
<li><strong>Pick the deadest room you have.</strong> A closet full of clothes beats a bathroom every time. Hard walls create the reflections that later sound like &ldquo;room&rdquo;.</li>
<li><strong>Stay close.</strong> Sing a hand-width or two from the phone, slightly off-axis to soften P and B pops, and keep the distance steady.</li>
<li><strong>Use headphones.</strong> If the beat plays from a speaker, it ends up in your take, and no tool removes it cleanly.</li>
<li><strong>Turn off noise suppression and auto-gain</strong> in your recording app, and record lossless (WAV) if the app allows it.</li>
<li><strong>Aim for peaks around &minus;12 to &minus;6 dB.</strong> Clipped peaks are very hard to repair; a quiet-but-clean take is easy to turn up.</li>
<li><strong>Record several takes.</strong> A passing car ruins one, not all of them.</li>
</ul>
<h2>2. Clean it before you do anything creative</h2>
<p>Order matters, because every effect after this point amplifies whatever problems are still in the vocal.</p>
<ol>
<li><strong>High-pass around 80&ndash;100&nbsp;Hz</strong> to remove rumble and handling noise that phones pick up.</li>
<li><strong>Light noise reduction.</strong> Learn the noise from a quiet gap and remove only as much as needed. If the voice starts to sound papery or watery, you went too far.</li>
<li><strong>Fix clicks, pops and breaths.</strong> Soften plosives, turn loud breaths down (not out), and trim silence.</li>
<li><strong>De-ess.</strong> Phone mics tend to exaggerate &ldquo;s&rdquo; sounds around 5&ndash;9&nbsp;kHz. Reduce them only when they spike.</li>
<li><strong>Deal with the room.</strong> If you hear echo between words, use a de-reverb tool, but expect to reduce it, not erase it.</li>
</ol>
<h2>3. Tune and tighten the performance</h2>
<p>Pitch and timing are what separate &ldquo;demo&rdquo; from &ldquo;record&rdquo;. Find your beat&rsquo;s key and set pitch correction to it. For a natural result use a slower retune speed and a moderate amount; for the modern rap and melodic sound push retune speed to its fastest. Then nudge words that fall behind the beat so syllables land on the grid.</p>
<h2>4. Make it sit in the beat</h2>
<ul>
<li><strong>Level:</strong> raise the vocal until every word is clear, then back off a hair. Compare against a finished record in the same genre.</li>
<li><strong>EQ:</strong> cut boxiness around 200&ndash;500&nbsp;Hz, add presence around 3&ndash;5&nbsp;kHz, add a little air above 10&nbsp;kHz.</li>
<li><strong>Compression:</strong> gentle and steady. Phone takes already have a raised noise floor; heavy compression raises it more.</li>
<li><strong>Space last:</strong> reverb and a tempo-synced delay on sends, with the low end filtered out of both so they do not muddy the beat.</li>
<li><strong>Check in mono</strong> and at low volume. If the words disappear, the vocal is fighting the beat.</li>
</ul>
<h2>5. Export, and keep the dry take</h2>
<p>Bounce a 24-bit WAV for the finished vocal and also keep the clean, untreated version. Treat the dry file as your master copy: if you change the beat or the style later you can redo the mix instead of re-recording.</p>
''',
    vf_title='Skip the manual chain: do steps 2&ndash;5 in one pass',
    vf='''<p>VocalForge runs this whole order for you. Drop in the phone recording and your beat and it removes noise, pops and harsh S sounds, repairs clipped peaks, dries up room echo, tunes to your beat&rsquo;s key, nudges words onto the beat, sets the vocal level against the music, and masters the result, then lets you adjust it live. Everything runs on your PC.</p>''',
    faq=[('Can a phone recording really sound professional?',
          'It can sound clean and competitive, especially for rap and melodic tracks that rely on processing. It will not have the detail of a good condenser mic, but good technique and cleanup close most of the gap.'),
         ('Should I use the voice-memo app or a recording app?',
          'Use any app that lets you record uncompressed (WAV) and turn off noise suppression and auto-gain. Voice memos are fine on iPhone if you set the quality to lossless.'),
         ('What is the biggest mistake with phone vocals?',
          'Recording in a hard-walled room or too far from the phone. Echo and distance cannot be fully fixed afterwards.')],
    ai=('Can AI fix phone vocals automatically?', '<p>Partly, and that is useful. &ldquo;AI vocal cleanup&rdquo; tools listen to your recording and choose the settings for you: how much noise to remove, where the harsh S sounds are, which key to tune to. That removes the guesswork, which is where most beginners go wrong. The repair itself is mostly classic signal processing, with AI models doing the heavy lifting in a few places, such as splitting a voice from music.</p><p>Whatever you use, the order in this guide still applies, and a closer, drier recording beats any AI. If you want the automatic route, VocalForge&rsquo;s analysis picks the settings and its optional AI add-on handles vocal separation.</p>'),
    related=['remove-echo-from-vocal-recording', 'mix-vocals-on-a-beat', 'autotune-for-rap-vocals'],
)

GUIDES['remove-echo-from-vocal-recording'] = dict(
    title='Remove Echo From Vocals: AI De-Reverb & Manual Tips',
    desc='Roomy vocal? Learn what reduces echo and reverb, how AI de-reverb compares with manual fixes, how to avoid watery artifacts, and when to re-record.',
    h1='How to Remove Echo and Room Reverb From a Vocal Recording',
    kw='remove echo from vocal recording',
    lead=('Echo and noise are two different problems. Noise sits underneath the voice (hiss, fans, traffic). Echo is the voice itself bouncing back from the walls. '
          'That is why a noise-reduction tool will not fix a roomy vocal, and why you can reduce echo but rarely erase it.'),
    tldr=['Reduce, do not erase: heavy de-reverb makes vocals sound thin, watery or &ldquo;underwater&rdquo;.',
          'Order: gate or noise-reduce, then de-reverb, then EQ, then compress, then add your own (good) reverb.',
          'Recording closer to the mic in a soft room beats any plugin.',
          'Add a short, dark reverb on a send afterwards so the vocal does not sound sterile.'],
    body='''
<h2>First, work out which problem you have</h2>
<ul>
<li><strong>Noise:</strong> constant sound under and between words: hiss, hum, a fan, an air conditioner. It stays when you stop singing.</li>
<li><strong>Room echo (reverb):</strong> the tail you hear after each word that dies away. It is the voice, delayed and smeared, so it overlaps the next words.</li>
</ul>
<p>Noise reduction learns a steady sound and subtracts it. Echo is not steady (it follows your voice), so it needs a different kind of tool: a de-reverb that estimates the late reflections and turns them down.</p>
<h2>How to reduce echo, step by step</h2>
<ol>
<li><strong>Start from the original file.</strong> Do not process an MP3 export if you still have the WAV.</li>
<li><strong>Remove noise first.</strong> Clean steady noise lightly so the de-reverb is not fooled by it.</li>
<li><strong>Apply de-reverb gently.</strong> Increase the amount until the tail between words is quieter, then stop. If consonants get soft or the voice sounds hollow, back off.</li>
<li><strong>Re-balance with EQ.</strong> De-reverb can leave the vocal slightly thin; a small boost around 150&ndash;250&nbsp;Hz and a cut around 300&ndash;500&nbsp;Hz usually restores body.</li>
<li><strong>Compress after, not before.</strong> Compression lifts quiet tails, so compressing a roomy vocal makes the echo louder.</li>
<li><strong>Add a short, dark reverb or delay</strong> of your own on a send. A treated vocal with a believable space sounds better than a totally dry, over-processed one.</li>
</ol>
<h2>The thing no plugin fixes</h2>
<p>If you recorded in a bathroom, a kitchen or an empty room, the reflections are mixed into the voice at similar loudness to the words. Heavy removal will damage the vocal. Re-record in a closet, under a duvet, or with blankets hung around the mic, even if it feels silly. It takes ten minutes and saves hours.</p>
<h2>Free versus paid tools</h2>
<p>Free editors have noise reduction and gates that help with hiss and some tails but cannot do true de-reverb. Dedicated tools (iZotope RX, sonible prime:vocal, LALAL.AI&rsquo;s echo remover and others) do the heavy lifting, and are worth it for important recordings. Whatever you use, compare before and after at the same loudness, and watch for artifacts.</p>
''',
    vf_title='Echo removal built into the finish',
    vf='''<p>VocalForge measures how roomy your recording is and dries it up automatically, scaled to the room (a closet-quality take is left alone; a bedroom echo gets treated), then continues with tuning, levelling and mastering. It is classic signal processing that runs on your PC. It reduces echo noticeably; for a very roomy recording it will improve it, but a re-record is still the real fix.</p>''',
    faq=[('Can you completely remove echo from a vocal?',
          'Not cleanly. You can reduce it a lot on moderate rooms; very roomy recordings can only be improved. Heavy removal causes watery or thin artifacts.'),
         ('Why does my vocal sound thin after removing reverb?',
          'De-reverb removes some of the body along with the tail. Restore it with a gentle EQ boost in the low-mids and add your own short reverb after.'),
         ('Is noise reduction the same as removing echo?',
          'No. Noise reduction removes steady background sounds. Echo follows your voice, so it needs de-reverb.')],
    ai=('Does AI echo removal work better?', '<p>AI and machine-learning de-reverb models can sound cleaner than old gate-and-EQ tricks, especially on speech, but they can also introduce their own artifacts: a thin, phasey or &ldquo;underwater&rdquo; tone when pushed hard. The rule is the same as for manual tools: reduce the room, do not try to erase it, then put a pleasant reverb back.</p><p>Free online &ldquo;AI echo remover&rdquo; sites are fine for experiments, but they mean uploading your audio. If the song is unreleased, a tool that runs on your own PC keeps it private.</p>'),
    related=['fix-vocals-recorded-on-phone', 'mix-vocals-on-a-beat', 'vocal-cleanup-software-compared'],
)

GUIDES['autotune-for-rap-vocals'] = dict(
    title='Autotune for Rap Vocals: Settings & AI Autotune Tips',
    desc='Use autotune on rap and melodic vocals: key, retune speed, natural versus hard-tune, what "AI autotune" really means, free options and mistakes.',
    h1='Autotune for Rap and Melodic Vocals: Settings That Work',
    kw='autotune for rap vocals',
    lead=('The &ldquo;autotune sound&rdquo; is not one setting. It is two choices: which notes the voice is allowed to hit (the key and scale), and how fast it is pulled onto them (retune speed). '
          'Get the key right and everything else is taste.'),
    tldr=['Find your beat&rsquo;s key and scale first. Wrong key = wrong notes, no matter how good the singing is.',
          'Retune speed is the whole sound: slow (&gt;40&nbsp;ms) is natural, around 10&nbsp;ms is modern, 0 is the hard robotic snap.',
          'Tune a clean, dry vocal before reverb and delay, never after.',
          'Rap flow needs timing help too: tune does not fix words that land off the beat.'],
    body='''
<h2>Step 1: find the key</h2>
<p>Pitch correction needs to know which notes are &ldquo;right&rdquo;. Ask the producer, look at the project file, or detect it from the beat. Choose the scale (major or minor); if you are unsure, a chromatic setting corrects to the nearest semitone but gives you less of the melodic character.</p>
<h2>Step 2: choose the retune speed</h2>
<ul>
<li><strong>Natural (slow, around 40&ndash;100&nbsp;ms):</strong> invisible correction. Good for singing and for rap you want to stay human.</li>
<li><strong>Modern (about 10&ndash;30&nbsp;ms):</strong> you hear it on held notes but it still sounds like a person. The sweet spot for many melodic rap and R&amp;B records.</li>
<li><strong>Hard (0&ndash;5&nbsp;ms):</strong> the snapped, stepped, robotic effect. Every glide becomes a staircase. It is a sound, not a correction.</li>
</ul>
<h2>Step 3: tune a clean vocal, in the right place in the chain</h2>
<p>Clean up noise and clicks first, then tune, then compress, then add saturation, reverb and delay. Tuning after reverb makes the tail warble; tuning a noisy take makes the tuner misread the pitch.</p>
<h2>Step 4: fix timing, not just pitch</h2>
<p>Many rap takes sound &ldquo;off&rdquo; because syllables drift from the grid rather than because the notes are wrong. Nudge words onto the beat, especially on repeated patterns and ends of lines, and keep the correction small enough to keep the swing.</p>
<h2>Free and online options</h2>
<p>Browser-based tuners (Audimee&rsquo;s free tier, Rys Up&rsquo;s tool, BandLab&rsquo;s AutoPitch and similar) are fine for trying the sound on a short clip. Check each one&rsquo;s limits, watermarks and what they do with your uploaded audio before sending unreleased music. Most online tools get you to a usable melodic sound; they do not match the speed and control of dedicated pitch software.</p>
<h2>Common mistakes</h2>
<ul>
<li>Setting the wrong key, then blaming the tuner.</li>
<li>Using the hard setting on a vocal that was sung out of tune by more than a semitone: the tuner picks the wrong note.</li>
<li>Tuning a vocal with bleed from the beat in it.</li>
<li>Over-tuning every word, which flattens the emotion. Leave some natural movement in long notes.</li>
</ul>
''',
    vf_title='Key detection and tuning without fiddling',
    vf='''<p>VocalForge reads the key and tempo from your beat, tunes your take to it with a style you choose (off, natural, a style learned from a reference song, or hard), keeps the natural movement in long notes if you want it, and nudges words onto the beat. You can also paint a section so one line gets hard-tune while the rest stays natural.</p>''',
    faq=[('What retune speed is best for rap?',
          'It depends on the sound you want. Slower for natural, around 10&ndash;30&nbsp;ms for a modern melodic sound, and 0 for the hard robotic effect.'),
         ('Do I have to know the key of my beat?',
          'Yes for the best result. If you do not know it, detect it from the instrumental, or use a chromatic setting as a fallback.'),
         ('Is there a free autotune that works for rap?',
          'Several online tools and free plugins can give a basic melodic effect. Check limits and privacy; they are fine for experiments but may not hold up for a release.')],
    ai=('Autotune versus &ldquo;AI autotune&rdquo;: what is the difference?', '<p>Classic autotune is pitch correction: detect the note you sang and move it to the nearest note of a scale. It is not generative AI. When people search for &ldquo;AI autotune&rdquo; they usually mean one of two things: pitch correction that picks the key and settings for you automatically, or voice-conversion tools that replace your voice with another one.</p><p>For rap and melodic vocals, automatic key detection plus fast, key-locked pitch correction is what gives the modern sound. Use the free <a href="/vocalforge/tools/song-key-finder">song key finder</a> to get the key from your beat, then set it in your tuner.</p>'),
    related=['future-vocal-effect-settings', 'mix-vocals-on-a-beat', 'fix-vocals-recorded-on-phone'],
)

GUIDES['mix-vocals-on-a-beat'] = dict(
    title='How to Mix Vocals on a Beat (+ AI Auto-Mix Option)',
    desc='Mix a vocal on a stereo beat step by step: level, EQ, compression, reverb, delay and ducking, plus where AI auto-mixing helps and where it does not.',
    h1='How to Mix Vocals on a Beat So They Sit in the Mix',
    kw='mix vocals on a beat',
    lead=('Most vocals get buried because they compete with the beat for the same frequencies, not because the fader is too low. '
          'Make room first, then level, then polish. Here is the order that works on a finished two-track beat.'),
    tldr=['Start with the beat lower than you think and the dry vocal clearly audible.',
          'High-pass the vocal, cut mud, add presence, and gently carve the beat where the vocal lives.',
          'Compress for control, then ride the level; add reverb and delay on sends with the lows filtered out.',
          'Check in mono, at low volume, and against a finished record.'],
    body='''
<h2>1. Make room before you add plugins</h2>
<p>Pull the beat down so its loudest parts peak around &minus;6&nbsp;dB, leaving headroom. Bring the dry vocal up until every word is clear but not shouting.</p>
<h2>2. Edit the performance</h2>
<p>Trim dead space, turn down loud breaths, align doubles and ad-libs, and tune. Process the performance you actually want, not the one you hope to fix later.</p>
<h2>3. EQ to avoid the pile-up</h2>
<ul>
<li><strong>High-pass at 80&ndash;120&nbsp;Hz</strong> so the vocal does not fight the kick and bass.</li>
<li><strong>Cut boxiness</strong> around 200&ndash;500&nbsp;Hz.</li>
<li><strong>Add presence</strong> around 3&ndash;5&nbsp;kHz so words cut through.</li>
<li><strong>Add a little air</strong> above 10&nbsp;kHz.</li>
<li><strong>Carve the beat</strong> gently (1&ndash;3&nbsp;dB) between 2 and 4&nbsp;kHz while the vocal is singing. A sidechained or automated dip works well.</li>
</ul>
<h2>4. Compress, then ride the level</h2>
<p>Gentle compression does most of the evening-out; use level automation for the rest, easing down a verse and lifting a hook. Avoid squashing: you want some dynamics left.</p>
<h2>5. Add depth with sends</h2>
<p>Put reverb and a tempo-synced delay on sends, high-pass them around 300&nbsp;Hz, and keep delay feedback low (a few repeats). Duck the reverb while the vocal is singing so words stay clear, and let it bloom in the gaps.</p>
<h2>6. Check it properly</h2>
<ul>
<li><strong>Mono:</strong> does the vocal still hold up when the stereo image collapses?</li>
<li><strong>Low volume and phone speakers:</strong> can you still hear every word?</li>
<li><strong>Reference:</strong> A/B against a finished record in the same genre at the same loudness.</li>
<li><strong>Loudness and peaks:</strong> aim for a sensible loudness and keep true peaks below &minus;1&nbsp;dBTP so streaming encoders do not distort it.</li>
</ul>
''',
    vf_title='The balance step, automated',
    vf='''<p>VocalForge sets the vocal level against your beat (using your reference song&rsquo;s balance if you give it one, or the typical balance of finished records), ducks the beat gently under the voice, adds ducked reverb and tempo-synced echo, then masters the mix and runs a pass/fail check on loudness, true peak, punch, low-end mono and tonal balance. Paint hooks and verses on the timeline to give each section its own space and width.</p>''',
    faq=[('How loud should the vocal be on a beat?',
          'Loud enough that every word is clear without sitting on top of the beat. Compare against a finished record in your genre at matching loudness rather than trusting the fader.'),
         ('Why does my vocal sound separate from the beat?',
          'Usually too much reverb or too bright without matching compression and EQ. Gentle compression, a touch of shared reverb, and carving space in the beat help them blend.'),
         ('What loudness should I master to?',
          'Streaming services normalise around &minus;14 LUFS, but many hip-hop and pop releases are mastered louder. Keep true peaks below &minus;1&nbsp;dBTP either way.')],
    ai=('Where AI auto-mixing helps (and where it does not)', '<p>Automatic mixing tools are good at starting points: a sensible vocal level against the beat, a first EQ and a first compression setting. They are less good at taste, such as how bright, how wet or how forward the vocal should sit for your song. Treat the AI result as a first draft and finish by ear, in mono and at low volume.</p><p>Use the free <a href="/vocalforge/tools/lufs-meter">LUFS meter</a> to check your final loudness and the <a href="/vocalforge/tools/vocal-checker">vocal checker</a> to catch clipping and noise before you export.</p>'),
    related=['fix-vocals-recorded-on-phone', 'future-vocal-effect-settings', 'vocal-cleanup-software-compared'],
)

GUIDES['future-vocal-effect-settings'] = dict(
    title='Future Vocal Effect Settings + AI Style Matching',
    desc='Get a Future-style melodic trap vocal: key-locked autotune, light saturation, dark reverb and tempo delay, plus AI style matching from a reference song.',
    h1='How to Get a Future-Style Vocal: Autotune, Reverb and Delay Settings',
    kw='future vocal effect',
    lead=('The melodic-trap vocal sound is a short chain: heavy pitch correction on a dry vocal, a touch of saturation, then a big dark reverb and a tempo delay on sends. '
          'These are starting points, not a secret recipe. Nobody outside the studio has the exact settings, so finish by ear.'),
    tldr=['Tune first, to the beat&rsquo;s key, with a fast retune speed (0&ndash;10&nbsp;ms) for the stepped sound.',
          'Add light saturation, then compress; build width with a few doubles.',
          'Use a long, dark reverb on a send, high-passed, and a quarter-note delay with low feedback.',
          'Duck the effects under the vocal so the words stay clear.'],
    body='''
<h2>The chain, in order</h2>
<ol>
<li><strong>Clean the vocal.</strong> Remove noise, pops and harsh S sounds. Pitch correction reads a dirty vocal badly.</li>
<li><strong>Pitch correction, locked to the key.</strong> For the stepped, robotic snap use a retune speed of 0&ndash;10&nbsp;ms. Some records use a slightly slower setting so the pitch bends audibly; try both.</li>
<li><strong>Saturation.</strong> A little tape or tube drive adds weight and glue. Keep it subtle or run it on a parallel return.</li>
<li><strong>Compression.</strong> Gentle and steady so quiet words stay present.</li>
<li><strong>Doubles and stack.</strong> Two or three tuned copies, panned, slightly detuned and timed a few milliseconds apart, make a vocal wide and thick.</li>
<li><strong>Reverb on a send.</strong> A long, dark hall or plate, high-passed around 300&nbsp;Hz so the beat stays tight. The reverb is audible, not hidden.</li>
<li><strong>Delay on a send.</strong> A tempo-synced quarter or dotted-eighth, 20&ndash;35% feedback, and feed it into the reverb so repeats melt into the tail.</li>
<li><strong>Duck the effects.</strong> Lower the reverb and delay while the vocal sings; let them bloom between lines.</li>
</ol>
<h2>What really creates the sound</h2>
<p>Three things matter more than any plugin: the key is right, the take is clean, and the effects are balanced against the beat rather than stacked on top of it. Copying settings from a preset pack without checking the key is the most common reason it does not sound right.</p>
<h2>Make it yours</h2>
<p>Use these numbers as a starting point, then adjust the retune speed, the reverb size and how much of the delay you hear. The goal is a vocal that suits your voice and your beat, not an imitation.</p>
<p class="note">VocalForge is not affiliated with or endorsed by any artist. Artist names are used only to describe a style of vocal processing.</p>
''',
    vf_title='Match a style from a song instead of copying settings',
    vf='''<p>Drop a song by an artist whose sound you like into VocalForge. It separates the vocal, measures how it was tuned, brightened, spaced, doubled and compressed, and applies a similar treatment to your recording: a style, not a copy. You can then adjust every part live. Your voice stays your own.</p>''',
    faq=[('What retune speed gives the Future sound?',
          'A very fast setting, around 0&ndash;10&nbsp;ms, gives the stepped robotic effect. Some records sound slightly slower; try both against your beat.'),
         ('Do I need Auto-Tune for this sound?',
          'No. The effect comes from fast, key-locked pitch correction, which several tools can do. The key and the clean vocal matter more than the brand.'),
         ('Why does my version sound thin?',
          'Usually a single vocal with no doubles, no saturation and too little reverb. Add a few detuned doubles, light saturation and a long dark reverb on a send.')],
    ai=('Presets versus AI style matching', '<p>Preset packs give you someone else&rsquo;s settings for someone else&rsquo;s voice. Style matching works the other way round: you point a tool at a finished record, it measures how that vocal was tuned, equalised, spaced and compressed, and applies a similar treatment to your recording. That is the idea behind VocalForge&rsquo;s &ldquo;sound like an artist&rdquo; feature. It changes the processing, not your voice, and it is not affiliated with any artist.</p>'),
    related=['autotune-for-rap-vocals', 'mix-vocals-on-a-beat', 'fix-vocals-recorded-on-phone'],
)

GUIDES['vocal-cleanup-software-compared'] = dict(
    title='Best AI Vocal Cleanup & Autotune Software (2026)',
    desc='Compare AI vocal cleanup, pitch and finishing tools: prices, what each does and who it is for, from plugins to one-click apps. Updated October 2026.',
    h1='Vocal Cleanup, Tuning and Finishing Software Compared',
    kw='vocal cleanup software',
    lead=('The right tool depends on the job. Some fix one problem very well (pitch, noise), some are full mixing plugins, and some finish a whole track. '
          'Here is how they differ, with the list prices we found in October 2026. Check each vendor&rsquo;s site for today&rsquo;s price.'),
    tldr=['Plugins give you deep control inside a DAW; they need you to know what to do.',
          'One-click and online tools are faster but narrower, and online tools mean uploading your audio.',
          'VocalForge is a Windows app for the finishing step: clean, tune, fit to the beat, match a style and master, one-time $29.'],
    body='''
<table>
<thead><tr><th>Tool</th><th>Typical price (US)</th><th>Best at</th><th>Where it falls short for this job</th></tr></thead>
<tbody>
<tr><td><strong>VocalForge</strong></td><td>$29 one-time, 7-day trial</td><td>Finishing a rough vocal on a beat: clean, tune, level, style-match, master</td><td>Not a DAW or plugin (yet); Windows only; less manual depth than Melodyne</td></tr>
<tr><td>iZotope Nectar 4 (Elements / Standard / Advanced)</td><td>about $55 / $199 / $299</td><td>Full vocal-chain plugin with an assistant</td><td>Needs a DAW and some mixing knowledge</td></tr>
<tr><td>Celemony Melodyne 5 Essential</td><td>about $99 list (often discounted)</td><td>Precise pitch and timing editing</td><td>Editing only: no cleanup, levelling or mastering</td></tr>
<tr><td>Antares Auto-Tune Unlimited</td><td>$30 per month or $300 per year for new subscribers</td><td>Industry-standard pitch correction and the classic effect</td><td>Subscription; pitch-focused</td></tr>
<tr><td>sonible prime:vocal</td><td>about $99&ndash;$179</td><td>Making home and phone vocals sound treated, with room reduction</td><td>A plugin: you still tune, mix and master elsewhere</td></tr>
<tr><td>LANDR Studio</td><td>roughly $8&ndash;$16 per month</td><td>Online mastering and distribution</td><td>Mastering-focused; online upload</td></tr>
<tr><td>Free online tuners (Audimee free tier, Rys Up, BandLab AutoPitch)</td><td>Free, with limits</td><td>Trying the effect on a short clip</td><td>Limits, watermarks and uploads of unreleased audio; less control</td></tr>
</tbody></table>
<p class="note">Prices are list prices reported by vendors and retailers in 2026 and change often, especially with sales. Treat them as a guide.</p>
<h2>How to choose</h2>
<ul>
<li><strong>You mix in a DAW and want precise control:</strong> a plugin suite (Nectar, prime:vocal) or Melodyne for pitch.</li>
<li><strong>You just need your track to sound finished and sit on the beat:</strong> a finishing app like VocalForge saves the most time.</li>
<li><strong>You are experimenting:</strong> free online tools are fine; keep unreleased audio in mind.</li>
<li><strong>You only need mastering:</strong> an online mastering service.</li>
</ul>
<h2>Where VocalForge fits</h2>
<p>VocalForge is built for the moment between &ldquo;I recorded it&rdquo; and &ldquo;I can post it&rdquo;: a rough phone or bedroom take, a beat, and not enough time or experience to build a vocal chain. It runs locally, so your unreleased songs stay on your PC. If you already live in a DAW and love your plugins, you may only want it for quick drafts, reference matching and the final loudness and quality check.</p>
''',
    vf_title='Try it on your own track',
    vf='''<p>The best comparison is your own recording. Download the free trial, run a rough take through it, and A/B the result against what you have now. Seven days, everything unlocked.</p>''',
    faq=[('What is the cheapest way to get good vocals?',
          'Record well first. Then a free editor plus a couple of stock plugins can do a lot; a one-time finishing app like VocalForge is the low-cost way to automate the rest.'),
         ('Do I need a plugin or a standalone app?',
          'If you work inside a DAW and want hands-on control, plugins. If you want a finished result quickly, a standalone finishing app is faster.'),
         ('Is VocalForge better than Auto-Tune?',
          'They do different jobs. Auto-Tune is a specialist pitch tool; VocalForge handles cleanup, tuning, levelling, style-matching and mastering together, with less manual control.')],
    ai=('Where AI fits in this list', '<p>&ldquo;AI&rdquo; appears on almost every product page now, but it covers very different things: automatic setting selection, learned noise and reverb removal, vocal separation, and generative voice tools. When you compare, ask what the AI actually does, whether it runs on your PC or in the cloud, and what happens to your audio.</p>'),
    related=['fix-vocals-recorded-on-phone', 'autotune-for-rap-vocals', 'remove-echo-from-vocal-recording'],
)

GUIDE_ORDER = ['fix-vocals-recorded-on-phone', 'remove-echo-from-vocal-recording', 'autotune-for-rap-vocals', 'mix-vocals-on-a-beat',
               'future-vocal-effect-settings', 'vocal-cleanup-software-compared']

# --------------------------------------------------------------------------------------------- policy pages (drafts for the owner to review)
POLICIES = {
    'privacy': dict(title='VocalForge Privacy Policy', desc='How VocalForge handles your audio, license and usage data.', h1='Privacy Policy',
                    body='''
<p class="note">Draft for review by the product owner before launch.</p>
<h2>Your audio stays on your computer</h2>
<p>VocalForge processes your recordings, beats and reference songs on your own PC. They are not uploaded to our servers.</p>
<h2>What does use the internet</h2>
<ul>
<li><strong>License checks.</strong> The app contacts our payment provider, Dodo Payments, to activate and validate your license key. This involves your license key and your computer&rsquo;s name.</li>
<li><strong>Downloads.</strong> The installer, updates and the optional AI add-on are downloaded from our own servers.</li>
<li><strong>Payments.</strong> Purchases are handled by Dodo Payments. We do not see or store your card details.</li>
</ul>
<h2>Contact</h2><p>Questions about privacy: use the contact option on fuidzy.com.</p>'''),
    'terms': dict(title='VocalForge Terms of Use', desc='Terms for using VocalForge software and its license.', h1='Terms of Use',
                  body='''
<p class="note">Draft for review by the product owner before launch.</p>
<h2>License</h2>
<p>A VocalForge license is for one person and may be activated on up to two of that person&rsquo;s computers. It is a personal, non-transferable license to use the software. You may not resell, redistribute or reverse-engineer it.</p>
<h2>Your content</h2>
<p>You keep all rights to the audio you create. You are responsible for having the rights to any recordings, beats or reference songs you process with VocalForge.</p>
<h2>No warranty</h2>
<p>The software is provided as is. Audio results depend on the quality of the source recordings, and we do not guarantee a particular outcome.</p>'''),
    'refund-policy': dict(title='VocalForge Refund Policy', desc='How refunds work for VocalForge purchases.', h1='Refund Policy',
                          body='''
<p class="note">Draft for review by the product owner before launch.</p>
<p>VocalForge includes a 7-day free trial so you can try it on your own recordings before you buy. If you buy and it does not work for you, contact us within 30 days of purchase and we will refund you.</p>
<p>Refunds are issued to the original payment method through our payment provider.</p>'''),
}


# --------------------------------------------------------------------------------------------- tools + extra guide
import content_tools as T  # noqa: E402

GUIDES['ai-vocal-cleanup-explained'] = T.AI_GUIDE
GUIDE_ORDER.insert(1, 'ai-vocal-cleanup-explained')
