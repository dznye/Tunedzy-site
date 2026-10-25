"""Batch 5b (25 October 2026): seventeen how-to guides. Same shape as content.GUIDES.

Tunedzy features named here exist in the app: Auto-duck, fades, Match loudness, Key and speed, Export stems, the vocal remover.
Anything else is general, practical advice. No invented numbers, reviews or counts.
"""

PHOTO = {}
TOOLS = {}
GUIDES = {}
ORDER = []
GROUP_OF = {}


def add(slug, photo, tools, **g):
    GUIDES[slug] = g
    PHOTO[slug] = photo
    TOOLS[slug] = tools
    ORDER.append(slug)
    GROUP_OF[slug] = 'how'


add('how-to-duck-music-under-a-voiceover', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='How to Duck Music Under a Voiceover',
    desc='Lower background music automatically while a voice speaks, so the words stay clear: the steps in Tunedzy and in any editor, and how to avoid pumping.',
    h1='How to Duck Music Under a Voiceover',
    kw='how to duck music under voiceover',
    lead='Ducking keeps the music under the voice and brings it back up in the gaps. Set it once and it works through the whole piece.',
    tldr=['Put the voice on one track and the music on another.',
          'Set the amount of reduction first, a few decibels to start.',
          'Slow the recovery so the music does not pump.',
          'Listen to the whole passage, not one phrase.'],
    body='''
<h2>Set up the tracks</h2>
<p>Keep the voice and the music on separate tracks. Clean the voice first, so the ducking reacts to the words and not to noise. Level the music to a sensible starting volume before you duck it.</p>
<h2>In Tunedzy</h2>
<p>In Multitrack, use Auto-duck to lower the music under the voices. It is the setting that does this job. Start with the default, play the passage, then adjust the amount of reduction. If the music pumps, reduce the amount and slow the return.</p>
<h2>In any other editor</h2>
<p>Most editors have a ducking or sidechain option. Use the voice as the trigger for the music track, and set a moderate reduction. If your editor lacks it, draw the volume of the music down by hand at the start and end of each phrase; it takes longer but works.</p>
<h2>Check it</h2>
<p>Play the passage on a phone speaker as well as headphones. The voice should stay clear, and the music should sit under it without disappearing.</p>
<h2>Related</h2>
<p>The <a href="/tunedzy/what-is-ducking">ducking explanation</a> covers the idea, and the <a href="/tunedzy/how-to-add-background-music-to-a-voiceover">background music guide</a> covers the level.</p>
''',
    vf_title='Auto-duck in Multitrack',
    vf='<p>Tunedzy lowers the music under your voices in Multitrack with Auto-duck, and exports the mix at a loudness target.</p>',
    faq=[('How much should the music drop?', 'Usually a few decibels to around ten, depending on the music. Listen and adjust.'),
         ('Why does the music pump?', 'The reduction is too strong or the return too fast. Lower the amount and slow the release.'),
         ('Can I duck more than one track?', 'Yes. Each music or effects track can be ducked under the same voice.')],
    related=['what-is-ducking', 'how-to-add-background-music-to-a-voiceover', 'voice-cleanup-for-podcasters'])

add('how-to-add-fades-to-a-recording', 'desk', ['vocal-checker', 'lufs-meter'],
    title='How to Add Fades to a Recording',
    desc='Add a fade in and a fade out so a recording starts and ends smoothly: the steps, the length of a good fade and when a fade is the wrong choice.',
    h1='How to Add Fades to a Recording',
    kw='how to add fades to a recording',
    lead='A fade is a short, smooth change in level at the start or end of a clip. It removes the abrupt start and stop that make a clip sound cut off.',
    tldr=['Add a short fade in to the start and a fade out to the end.',
          'Keep the fade short for speech, longer for music.',
          'Fades are for the edges; do not use them to hide a bad cut in the middle.',
          'In Multitrack, fades are set by dragging the handles at the start and end of a clip.'],
    body='''
<h2>Why fades matter</h2>
<p>A recording that starts or stops at full level sounds abrupt. A fade in softens the start, and a fade out softens the end, so the piece feels finished rather than chopped off.</p>
<h2>How long</h2>
<p>For speech, a fade of a fraction of a second at the start and a little longer at the end is usually enough. For music, a few seconds is common. Listen to it: the fade should be hard to notice.</p>
<h2>In Tunedzy</h2>
<p>In Multitrack, each clip has fade handles at its start and end. Drag them to set the length of the fade. Play the clip to check the edges.</p>
<h2>When not to fade</h2>
<p>A fade in the middle of speech sounds like a dip. For a cut in the middle, use a short crossfade between the two pieces instead, as the <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade guide</a> explains.</p>
''',
    vf_title='Smooth starts and endings',
    vf='<p>Multitrack in Tunedzy gives each clip fade handles, so you can shape the start and end of a clip directly.</p>',
    faq=[('How long should a fade be?', 'Short for speech, longer for music. Listen rather than measure.'),
         ('Does a fade change the loudness?', 'Only at the edges. The middle of the clip keeps its level.'),
         ('Should every clip have a fade?', 'Clips at the start and end of a piece usually do. Cuts in the middle use crossfades.')],
    related=['how-to-crossfade-two-recordings', 'how-to-trim-silence-from-a-recording', 'how-to-normalize-audio-the-right-way'])

add('how-to-crossfade-two-recordings', 'desk-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Crossfade Two Recordings',
    desc='Join two pieces of audio so the join cannot be heard: crossfade length, matching the room tone and the steps to check each join.',
    h1='How to Crossfade Two Recordings',
    kw='how to crossfade two recordings',
    lead='A crossfade blends the end of one piece into the start of the next. Done well, the join disappears; done badly, the room sound jumps.',
    tldr=['Overlap the two pieces slightly and fade one out while the other fades in.',
          'Match the room tone on both sides, so the join does not change the sound.',
          'Keep the crossfade short for speech; longer for music.',
          'Listen to every join at normal volume.'],
    body='''
<h2>Why the join matters</h2>
<p>Two recordings made at different times can have different room sound. If you simply butt them together, the change is audible as a click or a sudden shift in the background.</p>
<h2>The method</h2>
<p>Overlap the end of the first piece with the start of the second by a short time. Fade the first out while the second fades in. The overlap should be short for speech, a fraction of a second, so the words are not blurred.</p>
<h2>Match the room</h2>
<p>If the two sides sound different, add a little room tone under the join. A short section of the quiet room tone, faded in and out, smooths the change. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone guide</a> explains how to record it.</p>
<h2>Check the joins</h2>
<p>Play the join several times at normal volume. Listen for a click, a dip, or a change in the background. If you hear it, adjust the overlap or add more room tone.</p>
''',
    vf_title='Join the pieces without a seam',
    vf='<p>Tunedzy&rsquo;s Multitrack lays out clips with fades, so you can overlap two pieces and check the join by ear.</p>',
    faq=[('How long should a crossfade be?', 'Short for speech, longer for music. Listen to the join.'),
         ('Why does the join still click?', 'The fade is too short, or the two sides start at different levels. Fade a little longer and check the level.'),
         ('Can I crossfade a whole edit?', 'You crossfade each join. The rest of the recording is untouched.')],
    related=['how-to-add-fades-to-a-recording', 'how-to-trim-silence-from-a-recording', 'what-is-ducking'])

add('how-to-normalize-audio-the-right-way', 'desk', ['lufs-meter', 'vocal-checker'],
    title='How to Normalize Audio the Right Way',
    desc='What normalising does, the difference between peak and loudness normalising, and how to normalise a recording without clipping or squashing it.',
    h1='How to Normalize Audio the Right Way',
    kw='how to normalize audio',
    lead='Normalising raises a file so its loudest peak reaches a chosen level. It is simple and safe, but peak normalising does not match how loud a recording sounds, so it is not the whole answer.',
    tldr=['Peak normalising sets the highest peak to a level; it does not set loudness.',
          'Loudness normalising matches the average level, which is closer to how we hear.',
          'Normalising to a peak below full scale leaves room for conversion.',
          'Use loudness for the final level, and peak normalising only as a safety step.'],
    body='''
<h2>Peak normalising</h2>
<p>Peak normalising raises the file until its loudest sample reaches a level you choose, often just below full scale. It changes the level by one amount for the whole file. It is simple, but two files normalised to the same peak can sound very different.</p>
<h2>Loudness normalising</h2>
<p>Loudness normalising measures the average level of the file, usually in LUFS, and sets it to a target. That matches how loud the file feels. For speech and music, it is the better choice for the final level.</p>
<h2>A safe order</h2>
<ol>
<li>Clean and repair the file first.</li>
<li>Set the loudness to your target, so the average level is right.</li>
<li>Check the true peak, and lower the level or limit the peaks if it is too high.</li>
</ol>
<h2>In Tunedzy</h2>
<p>Match loudness sets a recording to a loudness target and checks the true peak. The <a href="/tunedzy/how-to-make-audio-louder-without-distortion">louder without distortion guide</a> covers the limits.</p>
''',
    vf_title='Normalise to loudness, check the peak',
    vf='<p>Tunedzy sets a file to a loudness target and checks the true peak, so it is level without clipping.</p>',
    faq=[('Does normalising improve sound?', 'It changes the level only. It does not make a recording better.'),
         ('Is peak normalising bad?', 'Not bad, but it is only a level check. Loudness is the better target for speech.'),
         ('Should I normalise before or after cleanup?', 'After. Clean first, then set the level.')],
    related=['how-to-make-audio-louder-without-distortion', 'loudness-for-youtube-podcasts-and-spotify', 'what-is-lufs'])

add('how-to-set-the-gain-on-a-microphone', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Set the Gain on a Microphone',
    desc='Set the microphone gain so the voice is strong and clean: the test, the target peak and the mistakes that add noise or clipping.',
    h1='How to Set the Gain on a Microphone',
    kw='how to set gain on microphone',
    lead='Gain is the boost given to the mic signal before it is recorded. Set it right and the voice is strong and clean; set it wrong and you get either noise or clipping.',
    tldr=['Place the mic first, then set the gain.',
          'Ask the speaker to say the loudest words they will use, and set the peaks around -6 dB.',
          'Too little gain adds noise when you raise the level later.',
          'Too much gain clips the loudest words, and clipping cannot be undone.'],
    body='''
<h2>Position first</h2>
<p>Put the mic where it will be during the recording, at the distance and angle you will use. Gain should be set for that position, not for a different one.</p>
<h2>Test the loudest words</h2>
<p>Ask the speaker to say the loudest part of the script at the volume they will use, including any laughs or shouts. Set the gain so those peaks reach around -6 dB on the meter, not the top.</p>
<h2>Too little</h2>
<p>If the level only reaches the bottom of the meter, the voice is weak and the electronics noise is more audible when you raise it later. Move closer or raise the input gain.</p>
<h2>Too much</h2>
<p>If the peaks touch the top of the meter, the loudest words will clip. Lower the gain, or move the mic back a little.</p>
<h2>Check after a minute</h2>
<p>Speakers get louder as they warm up. Check the level again after a minute of real speech, and adjust if the peaks are too close to the top.</p>
''',
    vf_title='Set the level once, then record',
    vf='<p>A recording set at a good gain needs less cleanup. Tunedzy cleans what remains, and checks the peaks on export.</p>',
    faq=[('What peak should I aim for?', 'Around -6 dB is a common target, leaving room for surprises.'),
         ('Should I set the gain on the mic or in the software?', 'Set the input gain on the mic or interface first, then adjust the software only a little.'),
         ('Why does my gain keep changing?', 'The speaker moves, changes distance or gets louder. Check again during the take.')],
    related=['what-is-gain-staging', 'what-is-headroom', 'my-recording-is-too-quiet'])

add('how-to-record-with-a-headset-microphone', 'mic', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='How to Record With a Headset Microphone',
    desc='Get a clear voice from a headset mic: the boom position, the distance, the room and the cleanup that suits a headset recording.',
    h1='How to Record With a Headset Microphone',
    kw='how to record with headset microphone',
    lead='A headset mic is always the same distance from your mouth, which helps. Position the boom correctly, keep the room soft, and a headset gives a clean, consistent voice.',
    tldr=['Place the boom mic a finger-width from the corner of the mouth, slightly to the side.',
          'Keep the headset steady; a moving mic changes the level.',
          'Use a soft room, because a headset still picks up the room.',
          'Check for breath noise and move the boom if you hear it.'],
    body='''
<h2>Position the boom</h2>
<p>Put the mic a finger-width from the corner of your mouth, slightly to the side, so breath hits the side of the capsule rather than the front. A mic in front of the mouth pops; a mic far to the side sounds thin.</p>
<h2>Keep it steady</h2>
<p>Adjust the headband so it stays put when you turn your head. A mic that moves changes the level and the tone during a take.</p>
<h2>The room</h2>
<p>A headset mic is close, so the room matters less than with a desk mic, but it still picks up echo and fan noise. A soft room helps.</p>
<h2>Cleanup</h2>
<p>Use the <a href="/tunedzy/clean-up-a-phone-voice-recording">cleanup steps</a> gently. A close mic usually needs less cleanup than a distant one.</p>
''',
    vf_title='Clean the headset take',
    vf='<p>Tunedzy cleans a headset recording in one pass on your PC. Compare Before and After.</p>',
    faq=[('Is a headset mic good enough for a podcast?', 'Often yes, for a single voice in a quiet room.'),
         ('Why do I hear breath pops?', 'The mic is in front of the mouth. Move it a little to the side.'),
         ('Does the headset cable cause noise?', 'It can rub or pick up handling noise. Keep the cable clear of the mic.')],
    related=['how-to-use-a-lavalier-microphone', 'how-to-record-with-a-usb-microphone', 'what-is-a-pop-filter']
)

add('how-to-use-a-lavalier-microphone', 'desk', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='How to Use a Lavalier Microphone',
    desc='Clip a lav mic on clothing for a clear voice: the clip position, cable handling, rustle and the cleanup that suits a clipped-on mic.',
    h1='How to Use a Lavalier Microphone',
    kw='how to use a lavalier microphone',
    lead='A lavalier, or lav, mic clips to clothing close to the mouth. Clip it in the right place, manage the cable, and it gives a steady voice with the hands free.',
    tldr=['Clip it about 15 to 20 cm below the mouth, on the centre of the chest.',
          'Tuck the cable so it does not rub against clothing.',
          'Test for rustle when you move, and avoid loose or noisy fabric.',
          'Check the level once you are wearing it, as posture changes the distance.'],
    body='''
<h2>Where to clip it</h2>
<p>Clip the mic on the centre of the chest, roughly 15 to 20 cm below the mouth, with the capsule facing up. Too low and the voice sounds dull; too high and it picks up the chin and the room more.</p>
<h2>Cable and rustle</h2>
<p>Tuck the cable under clothing and secure it with a small loop, so it does not rub. Clothing that rustles, such as nylon or loose fabric, is the usual source of noise. Test by moving and turning before you record.</p>
<h2>Level and movement</h2>
<p>Posture changes the distance, so check the level after you have sat in the position for a minute. Keep head movements small, because a turn takes the mic away from the mouth.</p>
<h2>Cleanup</h2>
<p>A lav mic is close, so it needs less cleanup, but it can pick up the body. Clean gently and check for rustle in the file.</p>
''',
    vf_title='Clean the clip-on voice',
    vf='<p>Tunedzy cleans a clip-on recording on your PC. Use Before and After to listen for rustle.</p>',
    faq=[('Where is the best place to clip it?', 'About 15 to 20 cm below the mouth, centred on the chest.'),
         ('Why does my lav sound muffled?', 'It is under clothing or covered. Clip it outside the fabric where possible.'),
         ('Can I use one for a presentation?', 'Yes. It keeps the distance steady and frees your hands.')],
    related=['how-to-record-with-a-headset-microphone', 'my-audio-has-background-hiss', 'what-is-a-shock-mount']
)

add('how-to-record-voice-in-a-car', 'neon', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record Voice in a Car',
    desc='Record a clear voice in a parked car: the engine off, the windows up, the right spot and the road and fan noise to avoid.',
    h1='How to Record Voice in a Car',
    kw='how to record voice in a car',
    lead='A parked car with the engine off and the windows up can be a surprisingly quiet, soft space. Moving, it is not: road and wind noise swamp a voice.',
    tldr=['Park, switch the engine off, and close the windows.',
          'Turn off the fan and any climate system before you record.',
          'Sit in the back seat, where the cabin is quieter than the front, with the mic close.',
          'Record a few seconds of the cabin alone to check the noise first.'],
    body='''
<h2>Choose the right moment</h2>
<p>Park in a quiet place, away from traffic and from a running engine. A car on a quiet street with the engine off is the best case.</p>
<h2>Set the cabin</h2>
<p>Switch the engine and the climate system off, close every window, and turn off any fan. Soft seats and the car&rsquo;s own fabric help absorb reflections.</p>
<h2>Position</h2>
<p>Sit where the cabin is most enclosed. The back seat is often a quieter spot. Keep the mic close to your mouth, and check that the car&rsquo;s structure is not right beside you.</p>
<h2>Check the cabin first</h2>
<p>Record ten seconds of silence and listen on headphones. If you hear a tick from the engine, a fan or traffic, wait or move. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone guide</a> explains why this matters.</p>
<h2>Cleanup</h2>
<p>A car cabin has low rumble and echo. Use a high-pass filter around 80 to 120 Hz and gentle cleanup. The <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup steps</a> apply.</p>
''',
    vf_title='Clean the car recording',
    vf='<p>Tunedzy cleans a car recording on your PC. Check the room tone first, then clean gently.</p>',
    faq=[('Can I record while driving?', 'It is not safe to record while driving. Park first, and follow the laws where you are.'),
         ('Why does the car sound boomy?', 'Low rumble and cabin resonance. A high-pass filter and a closer mic help.'),
         ('Is the back seat better?', 'Often, because it is further from the road noise and the windows.')],
    related=['how-to-set-up-a-quiet-recording-corner-on-a-budget', 'my-audio-has-background-hiss', 'remove-background-noise-from-a-voice-recording']
)

add('how-to-record-a-voicemail-greeting', 'booth-wide', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Record a Voicemail Greeting That Sounds Clear',
    desc='Record a voicemail greeting on a phone that sounds clear and friendly: the room, the distance, the script and the short cleanup it needs.',
    h1='How to Record a Voicemail Greeting',
    kw='how to record voicemail greeting',
    lead='A voicemail greeting is short, but callers judge it in seconds. A quiet room, a steady distance and a clear script give a greeting that sounds professional.',
    tldr=['Record in a quiet, soft room with the fans off.',
          'Hold the phone a hand&rsquo;s width from the mouth, slightly to the side.',
          'Write the script, read it once aloud, and keep it short.',
          'Listen back on a phone speaker, the way callers will hear it.'],
    body='''
<h2>Write it first</h2>
<p>A greeting needs your name or number, a short line of thanks, and what to do next. Read it aloud once with a timer; it should be well under ten seconds for most people.</p>
<h2>Record it</h2>
<p>Use a quiet room and a steady distance. Speak at a slightly slower pace than normal, and smile while you speak, because the voice sounds warmer.</p>
<h2>Clean it</h2>
<p>Use the <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup steps</a> gently. A greeting is short, so clean only what is audible: room noise and clicks.</p>
<h2>Check it</h2>
<p>Play it on a phone speaker at normal volume. If you have to lean in, the level is too low.</p>
''',
    vf_title='Clean the greeting on your phone',
    vf='<p>Tunedzy Go cleans a short recording on your phone for free. Record, clean and check the greeting there.</p>',
    faq=[('How long should a greeting be?', 'Short. Under about ten seconds is a common target.'),
         ('Should I use my phone or a studio mic?', 'Your phone is fine if the room and distance are right.'),
         ('How do I make it sound friendly?', 'Smile while you speak, slow slightly and keep the sentences short.')],
    related=['clean-up-a-phone-voice-recording', 'voice-note-sounds-better-on-an-iphone', 'why-does-my-phone-recording-sound-far-away']
)

add('how-to-make-a-podcast-intro-and-outro', 'mic', ['lufs-meter', 'vocal-checker'],
    title='How to Make a Podcast Intro and Outro That Sounds Professional',
    desc='Record and mix a podcast intro and outro: script length, music under the voice, loudness that matches the episode and the steps to keep them consistent.',
    h1='How to Make a Podcast Intro and Outro',
    kw='how to make podcast intro and outro',
    lead='An intro and outro frame every episode. Keep them short, consistent and at the same loudness as the episode, and they feel like part of the show.',
    tldr=['Keep the intro under about thirty seconds, so listeners reach the content.',
          'Put music under the voice, ducked, rather than competing with it.',
          'Match the loudness of the intro and outro to the episode.',
          'Record the intro and outro once and reuse them.'],
    body='''
<h2>Keep it short</h2>
<p>The intro tells listeners what the show is and who is speaking. Keep it short, and move to the episode quickly. The outro thanks listeners and says where to find the show.</p>
<h2>Music and voice</h2>
<p>If there is music, duck it under the voice so the words stay clear. The <a href="/tunedzy/how-to-duck-music-under-a-voiceover">ducking guide</a> has the steps.</p>
<h2>Match the loudness</h2>
<p>An intro that is much louder or quieter than the episode jolts listeners. Set the intro and outro to the same loudness target as the episode. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the targets.</p>
<h2>Reuse them</h2>
<p>Record the intro and outro once, clean them with the same settings as the episodes, and reuse them. Consistency is what makes a show recognisable.</p>
''',
    vf_title='Frame every episode the same way',
    vf='<p>Tunedzy levels the intro and outro to the same loudness target as the episode, so the show sounds consistent.</p>',
    faq=[('How long should a podcast intro be?', 'Short. Under about thirty seconds is a common target.'),
         ('Do I need music?', 'Not always. A clear voice with a simple sting is enough for many shows.'),
         ('Should the intro be louder than the episode?', 'No. Match it to the episode, so listeners do not reach for the volume control.')],
    related=['podcast-sound-professional-on-a-budget', 'how-to-duck-music-under-a-voiceover', 'voice-cleanup-for-podcasters']
)

add('how-to-add-background-music-to-a-voiceover', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='How to Add Background Music to a Voiceover',
    desc='Put music under a voiceover so it adds mood without hiding the words: choosing the music, levels, ducking and the checks before you export.',
    h1='How to Add Background Music to a Voiceover',
    kw='how to add background music to voiceover',
    lead='Background music adds mood, but it must stay under the words. Choose music that suits the voice, set it low, duck it under speech, and check it on a small speaker.',
    tldr=['Choose music with a steady, simple texture that does not fight the voice.',
          'Set the music well below the voice before you duck it.',
          'Duck the music under the speech, so it returns in the gaps.',
          'Check the balance on a phone speaker, where many listeners will hear it.'],
    body='''
<h2>Choose the music</h2>
<p>Pick music without a strong vocal in the same range, and with a steady feel rather than sudden changes. Music that changes a lot pulls attention away from the words.</p>
<h2>Set the level</h2>
<p>Start the music low, well below the voice, then bring it up only as far as you can hear it under the words. A background that you can hear clearly on the first listen is usually too loud.</p>
<h2>Duck it</h2>
<p>Duck the music under the speech, so it lifts in the pauses. The <a href="/tunedzy/what-is-ducking">ducking explanation</a> describes how it behaves.</p>
<h2>Check it</h2>
<p>Listen on headphones and on a small speaker. Make sure the words are clear, and the music is there without being in the way.</p>
''',
    vf_title='Music under the words',
    vf='<p>Tunedzy&rsquo;s Multitrack lets you duck music under a voice and export the mix at a loudness target.</p>',
    faq=[('How loud should the music be?', 'Low enough that the words are clearly the focus. Listen on a phone speaker.'),
         ('Can I use any music?', 'Only music you have the right to use. Check the licence before you publish.'),
         ('Why does the music cover the voice?', 'It is too loud or not ducked. Lower it and duck it under the speech.')],
    related=['how-to-duck-music-under-a-voiceover', 'record-a-voiceover-on-your-phone', 'how-to-make-a-podcast-intro-and-outro']
)

add('how-to-export-stems-for-a-daw', 'mic-wide', ['song-key-finder', 'bpm-finder'],
    title='How to Export Stems for Your DAW',
    desc='Export each track of a mix as its own file, so you can finish the voice in your DAW: the steps, the naming and the sync that keeps the tracks lined up.',
    h1='How to Export Stems for Your DAW',
    kw='how to export stems for daw',
    lead='A stem is one track exported on its own. Export stems when a DAW needs the voice and the music as separate files, lined up on the same start time.',
    tldr=['Export one file per track, all starting at the same time.',
          'Name each file clearly, so the DAW shows what each one is.',
          'Keep the sample rate the same for all stems.',
          'Check the stems line up by importing them together.'],
    body='''
<h2>Why stems</h2>
<p>A DAW may be the best place to finish music, while Tunedzy is best for the voice. Exporting stems lets you move the voice into your DAW with its timing intact.</p>
<h2>How in Tunedzy</h2>
<p>Use Export in Multitrack, and choose the stems option, which exports one file per track. Each file starts at the same time, so they stay in sync.</p>
<h2>Naming and format</h2>
<p>Name each file after its track, such as lead vocal or music bed. Keep one sample rate across all stems, so the DAW does not have to convert them. WAV is the usual choice for stems.</p>
<h2>Check the sync</h2>
<p>Import all the stems into the DAW at the same time. Play the start and a join. If they drift, check the start time of each file.</p>
''',
    vf_title='Export the voice for your DAW',
    vf='<p>Tunedzy exports stems from Multitrack, one file per track, so the voice finishes cleanly in your DAW.</p>',
    faq=[('Why export stems instead of one mix?', 'So you can change the balance and effects in your DAW.'),
         ('Which format should stems be?', 'WAV is common, at the same sample rate for all stems.'),
         ('Will the stems be in sync?', 'They start at the same time. Check by importing them together.')],
    related=['tunedzy-vs-garageband', 'how-to-choose-wav-mp3-or-flac', 'how-to-isolate-a-voice-from-background-music']
)

add('how-to-change-speed-without-changing-pitch', 'neon-wide', ['song-key-finder', 'bpm-finder', 'chord-finder'],
    title='How to Change Speed Without Changing Pitch',
    desc='Speed up or slow down a recording without the voice going high or low: what time-stretching is, the limits and the steps in Tunedzy.',
    h1='How to Change Speed Without Changing Pitch',
    kw='how to change speed without changing pitch',
    lead='Changing speed alone also changes pitch: a faster file sounds higher. Time-stretching changes the speed and keeps the pitch, within limits.',
    tldr=['Simple speed changes also change the pitch, the way a tape does.',
          'Time-stretching changes the speed and keeps the pitch, with some artifacts.',
          'Small changes sound natural; large changes sound smeared.',
          'Keep the original, and listen for warble on sustained notes.'],
    body='''
<h2>Speed and pitch are linked</h2>
<p>When you play a recording faster, the pitch rises. When you slow it, the pitch falls. That is how tape works. To change speed without the pitch moving, the audio has to be time-stretched.</p>
<h2>What time-stretching does</h2>
<p>It analyses the sound and rebuilds it at a new length. Small changes are very hard to notice. Large changes can smear consonants or add a warble on long vowels.</p>
<h2>In Tunedzy</h2>
<p>The key and speed tool changes the key or the speed of a clip. Use it for small changes, check the result on sustained notes, and keep the original.</p>
<h2>Keep the change small</h2>
<p>A few percent changes almost always sound natural. If you need a large change, consider re-recording at the right pace.</p>
''',
    vf_title='Change the speed, keep the pitch',
    vf='<p>Key and speed in Tunedzy changes the speed or key of a clip. Keep changes small and listen for artifacts.</p>',
    faq=[('Will the voice sound robotic?', 'Small changes usually do not. Large changes can add artifacts.'),
         ('Can I change key and speed together?', 'Yes, with the same tool. Check the result each time.'),
         ('Why does my slowed voice sound smeared?', 'The change is too large for time-stretching. Use a smaller change.')],
    related=['how-to-change-the-key-of-a-vocal', 'how-to-clean-a-song-vocal-recorded-on-a-phone', 'vocal-cleanup-for-singers-and-rappers']
)

add('how-to-change-the-key-of-a-vocal', 'neon', ['song-key-finder', 'chord-finder', 'bpm-finder'],
    title='How to Change the Key of a Vocal',
    desc='Move a vocal into a different key so it suits a singer or a beat: finding the current key, choosing the new one and checking the result.',
    h1='How to Change the Key of a Vocal',
    kw='how to change key of vocal',
    lead='Changing the key moves a whole vocal up or down in pitch, so it suits a singer or a beat. Work out the current key, choose the new one, and check the result carefully.',
    tldr=['Find the current key of the vocal and the beat.',
          'Move the vocal by a small number of semitones, not a large jump.',
          'Check the result on the highest and lowest notes.',
          'Changing key changes the timbre a little, so listen to the whole song.'],
    body='''
<h2>Find the keys</h2>
<p>Use the <a href="/tunedzy/tools/song-key-finder">song key finder</a> on the beat, and sing or play the vocal&rsquo;s range to see where it sits. Knowing both keys tells you how far to move.</p>
<h2>Move by semitones</h2>
<p>Move the vocal by a small number of semitones. A few semitones usually sound natural; a large move can make a voice sound like someone else.</p>
<h2>Check the extremes</h2>
<p>Check the highest and lowest notes. A key change that makes the top note strained or the bottom note too weak is the wrong key.</p>
<h2>In Tunedzy</h2>
<p>The key and speed tool moves a clip by semitones. Change in small steps, and play the whole song after each change.</p>
''',
    vf_title='Move the vocal, check the range',
    vf='<p>Key and speed in Tunedzy moves a vocal by semitones. Check the highest and lowest notes after each move.</p>',
    faq=[('How many semitones is a good move?', 'Usually a few. Check the singer&rsquo;s range rather than a number.'),
         ('Does changing key change the voice?', 'A little. Large changes can alter the character of the voice.'),
         ('Should I change the beat or the vocal?', 'Usually the vocal, because beats are harder to move cleanly.')],
    related=['how-to-change-speed-without-changing-pitch', 'how-to-clean-a-song-vocal-recorded-on-a-phone', 'vocal-cleanup-for-singers-and-rappers']
)

add('how-to-make-a-karaoke-track-from-a-song', 'desk', ['karaoke-autotune', 'song-key-finder'],
    title='How to Make a Karaoke Track From a Song',
    desc='Remove the vocal from a song you have the right to use, to make a karaoke or practice track: the method, the limits and the rights check.',
    h1='How to Make a Karaoke Track From a Song',
    kw='how to make karaoke track from song',
    lead='A karaoke track is the song without its lead vocal. Separation can make one for practice, but it is never perfect, and it is only right to do with music you have the right to use.',
    tldr=['Use only music you own or have the right to use.',
          'Separation removes most of the vocal, with some bleed left in.',
          'Clean the result gently, and listen for artifacts on the vocal parts.',
          'For practice at home, a reasonable result is enough.'],
    body='''
<h2>Check the rights first</h2>
<p>A karaoke track made from a commercial song can be a copyright issue, even for personal use. Use your own recordings, music you have a licence for, or a track the artist has released for this purpose.</p>
<h2>How it works</h2>
<p>A separation model splits the song into a vocal and an instrumental. The instrumental is what you sing over. Expect some vocal bleed, and some artifacts where the vocal was removed.</p>
<h2>In Tunedzy</h2>
<p>Tunedzy has a vocal remover and a stem mixer. The <a href="/tunedzy/how-to-isolate-a-voice-from-background-music">voice isolation guide</a> covers the same method and its limits. Karaoke Autotune on this site is a live tool for singing along.</p>
<h2>Listen critically</h2>
<p>Check the instrumental for holes where the vocal was, and for any hiss on the cymbals. A short practice loop is more useful than a perfect track.</p>
''',
    vf_title='Practice, with the right music',
    vf='<p>Tunedzy separates a vocal on your PC. Use it only with music you have the right to use.</p>',
    faq=[('Is a karaoke track from a commercial song legal?', 'It depends on the rights and the use. Check the rules and the licence before you make or share one.'),
         ('Why does the instrumental sound watery?', 'Separation leaves artifacts. Use a gentle clean and listen for holes.'),
         ('Can I sing on top of it?', 'Yes, for practice. Sharing a recording publicly raises the rights question again.')],
    related=['how-to-isolate-a-voice-from-background-music', 'vocal-cleanup-for-singers-and-rappers']
)

add('how-to-record-voice-lines-for-a-game', 'hero', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record Voice Lines for a Game',
    desc='Record consistent voice lines for a game or an animation: the room, the script, the naming, the levels and the cleanup that keeps every line matching.',
    h1='How to Record Voice Lines for a Game',
    kw='how to record voice lines for a game',
    lead='Game voice lines are many short clips that must match. Keep the room and the mic position fixed, name every file clearly, and clean every line with the same settings.',
    tldr=['Fix the room, mic and distance for the whole project.',
          'Record every line with the same level and the same settings.',
          'Name files clearly, by character, scene and line number.',
          'Clean each line gently, and check the loudness across the set.'],
    body='''
<h2>Fix the setup</h2>
<p>Every line must sound like the same room and the same person. Record the whole project in the same place, with the same mic and the same distance. Write the settings down before the first session.</p>
<h2>Script and naming</h2>
<p>Keep a script with a line ID for each clip. Name the files by character, scene and line, so the game engine and the editors can find them.</p>
<h2>Levels</h2>
<p>Set the level once, and check it at the start of each session. Lines that are much louder or quieter than the rest stand out in a game.</p>
<h2>Clean and check</h2>
<p>Clean every line with the same settings, then check the loudness across a set of lines together. The <a href="/tunedzy/how-to-record-an-audiobook-at-home">audiobook guide</a> uses the same consistency principle.</p>
''',
    vf_title='Clean the whole set consistently',
    vf='<p>Tunedzy applies the same cleanup and loudness target to every line, so the set matches.</p>',
    faq=[('How do I keep lines consistent across months?', 'Note the mic, distance and level, and record in the same room.'),
         ('Should I process each line the same way?', 'Yes. Use the same settings for every line in the project.'),
         ('What loudness do games use?', 'It varies by engine and platform. Check the target your engine or publisher asks for.')],
    related=['how-to-record-an-audiobook-at-home', 'voice-cleanup-for-voice-actors', 'how-to-set-the-gain-on-a-microphone']
)

add('how-to-record-a-meeting-clearly', 'desk-wide', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Record a Meeting Clearly',
    desc='Record a meeting so everyone can be heard afterwards: where to place the recorder, what to tell people first, and how to clean and transcribe the result.',
    h1='How to Record a Meeting Clearly',
    kw='how to record a meeting clearly',
    lead='A meeting recording is only useful if you can hear everyone. Place the recorder in the middle, keep the room quiet, and tell people you are recording before you start.',
    tldr=['Tell everyone you are recording, and get their agreement.',
          'Place the recorder in the middle of the table, closer to the quieter speakers.',
          'Turn off the fans and the air conditioning for the meeting.',
          'Clean the file, then transcribe it for notes.'],
    body='''
<h2>Ask first</h2>
<p>Before you record, tell everyone that you will record and why. Check the rules where you are, because some places need everyone to agree. The <a href="/tunedzy/recording-consent-before-you-record">consent guide</a> covers the basics.</p>
<h2>Place the recorder</h2>
<p>Put the recorder in the middle of the table, and closer to the quieter speakers. A recorder at one end favours the people near it. Keep it away from paper, cups and anything that rattles.</p>
<h2>The room</h2>
<p>Turn off the fans and air conditioning if you can. Close the door to reduce the corridor noise. Soft furniture and curtains help a meeting room sound clear.</p>
<h2>Afterwards</h2>
<p>Clean the file gently, and transcribe it for notes. Check any names and figures against the audio before you share them.</p>
''',
    vf_title='Clean the meeting, transcribe the notes',
    vf='<p>Tunedzy cleans a meeting recording and transcribes it on your PC, so the notes stay on your device.</p>',
    faq=[('Do I need a special recorder?', 'A phone on the table works for a small meeting. A dedicated recorder helps larger ones.'),
         ('Can I use the transcript as minutes?', 'Use it as a draft. Check the wording, names and decisions before you share it.'),
         ('What if people talk over each other?', 'Overlapping speech is hard to separate. Ask people to speak one at a time.')],
    related=['how-to-clean-up-a-zoom-or-video-call-recording', 'recording-consent-before-you-record', 'edit-a-podcast-by-its-words']
)
