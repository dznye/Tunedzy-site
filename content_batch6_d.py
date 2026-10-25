"""Batch 6d (25 October 2026): fifteen how-to guides. Same shape as content.GUIDES. GROUP_OF marks them 'how'.

Tunedzy features named here exist in the app (Perfect it, Repair, Studio sound, Multitrack, the transcript and caption export, Match
loudness, Replace audio in video, the free LUFS and vocal tools). Everything else is general practical advice.
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


add('how-to-convert-audio-to-mp3-without-losing-quality', 'desk', ['lufs-meter', 'vocal-checker'],
    title='How to Convert Audio to MP3 Without Losing Quality',
    desc='Convert a WAV or other audio file to MP3 at a high quality setting, from the master, with the true peak checked. Steps and the settings that matter.',
    h1='How to Convert Audio to MP3 Without Losing Quality',
    kw='how to convert audio to mp3 without losing quality',
    lead='An MP3 is lossy, so some detail is always removed. You can keep the loss small by converting once, from a lossless master, at a high bit rate.',
    tldr=['Convert from the WAV or FLAC master, never from another MP3.',
          'Use a high bit rate, the highest your platform accepts.',
          'Check the true peak of the MP3, because conversion can raise it.',
          'Listen to the MP3 on the device you will use.'],
    body='''
<h2>Start from the master</h2>
<p>Keep the original WAV or FLAC. Each conversion from an MP3 adds loss, so a second MP3 from the first one is worse than a single conversion from the master.</p>
<h2>Set the bit rate</h2>
<p>Choose the highest bit rate the platform accepts. For speech, a high bit rate is very close to the original for most listeners. Check the platform&rsquo;s recommendation before you export.</p>
<h2>Check the peak</h2>
<p>Conversion can raise the peaks. After exporting, check the true peak of the MP3, and lower the level if it is above -1 dBTP. The <a href="/tunedzy/what-is-true-peak-dbtp">true peak explanation</a> covers why.</p>
<h2>Listen on your device</h2>
<p>Play the MP3 on the phone or speaker your listeners will use. If something sounds wrong, export again at a higher bit rate from the master.</p>
''',
    vf_title='Export the MP3 from the master',
    vf='<p>Tunedzy exports MP3 from its master at the bit rate you choose, with the true peak checked.</p>',
    faq=[('Does one conversion lose quality?', 'A little, at a high bit rate it is hard to hear for speech.'),
         ('Can I convert an MP3 to a better MP3?', 'No. That adds loss. Go back to the master.'),
         ('What bit rate should I use?', 'The highest the platform accepts, checked on your device.')],
    related=['my-mp3-sounds-worse-than-my-wav', 'how-to-choose-wav-mp3-or-flac', 'what-is-bitrate'])

add('how-to-compress-an-audio-file-for-email', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='How to Compress an Audio File for Email',
    desc='Make a voice recording small enough to send by email: mono, a moderate bit rate and trimming the silence, with the steps and the trade-offs.',
    h1='How to Compress an Audio File for Email',
    kw='how to compress audio file for email',
    lead='Email services limit attachment size. A voice clip becomes small quickly if you use mono, a moderate bit rate and no dead air at the start and end.',
    tldr=['Convert to mono; a single voice does not need two channels.',
          'Use a moderate bit rate for speech.',
          'Trim the silence at the start and end.',
          'Check the size limit of the service before you send.'],
    body='''
<h2>Check the limit first</h2>
<p>Each email service has an attachment size limit. Check it before you start, so you know how much to reduce.</p>
<h2>Mono and trim</h2>
<p>Convert to mono and trim the dead air. These two steps often halve the size without changing how a voice sounds. The <a href="/tunedzy/how-to-trim-silence-from-a-recording">trimming guide</a> shows how.</p>
<h2>Export a compressed copy</h2>
<p>Export a compressed format from the master at a moderate bit rate. Listen to the copy before you send it. For speech, a moderate setting is usually clear.</p>
<h2>Share a link if it is still large</h2>
<p>For a long file, a file-sharing link often works better than an attachment. Check the sharing terms and who can open the link.</p>
''',
    vf_title='Small copy, same voice',
    vf='<p>Tunedzy exports a mono or compressed copy from the master, and keeps the full file for editing.</p>',
    faq=[('Will the email copy sound worse?', 'At a moderate bit rate, speech is usually clear. Listen before you send.'),
         ('Which format is smallest?', 'A compressed format at a moderate bit rate. WAV is the largest.'),
         ('Should I keep the original?', 'Yes. Send the copy and keep the master.')],
    related=['my-audio-file-is-too-big', 'how-to-choose-wav-mp3-or-flac', 'how-to-trim-silence-from-a-recording'])

add('how-to-clean-up-a-recorded-phone-call', 'desk', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Clean Up a Recorded Phone Call',
    desc='Clean a recorded phone call: the limits of call audio, a gentle cleanup, levelling both voices and what to do about a faint or crackly line.',
    h1='How to Clean Up a Recorded Phone Call',
    kw='how to clean up recorded phone call',
    lead='A phone call is compressed and often quiet. Cleanup can make it clearer, but it cannot rebuild speech that the line dropped. Start gently and level both voices.',
    tldr=['A phone call is compressed; it has less detail than a local recording.',
          'Clean gently, because heavy cleanup thins the call audio.',
          'Level the two voices so both are easy to follow.',
          'Keep the original recording, and say so if the call matters for a story.'],
    body='''
<h2>What the line did</h2>
<p>Phone audio is narrow and compressed. High and low frequencies are removed, and dropouts cut words. Cleanup works on the noise and the level, not the lost sound.</p>
<h2>A gentle cleanup</h2>
<p>Reduce the steady noise, remove clicks, and level the speakers. Keep the setting light, because heavy reduction on call audio sounds thin and watery.</p>
<h2>Levelling</h2>
<p>The caller and the receiver are often at different levels. Bring them together, so the listener does not have to adjust the volume between speakers.</p>
<h2>Keep the original</h2>
<p>Keep the untouched recording. If the call matters for a story, note that it was cleaned, and keep the original for checking.</p>
''',
    vf_title='Clean the call gently',
    vf='<p>Tunedzy cleans the call gently and levels the speakers. Keep the original and compare with Before and After.</p>',
    faq=[('Can a dropped word be restored?', 'No. Cleanup cannot rebuild speech the line lost.'),
         ('Should I record the call locally?', 'Yes, if you can. A local recording is much cleaner.'),
         ('Is it fine to clean a recorded call?', 'Yes, with consent for the recording. Keep the original.')],
    related=['how-to-clean-up-a-zoom-or-video-call-recording', 'recording-consent-before-you-record', 'how-to-level-voices-between-speakers'])

add('how-to-record-a-voice-over-for-a-slideshow', 'booth', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record a Voice-Over for a Slideshow',
    desc='Record a clear voice-over for a slideshow or presentation: the script per slide, the timing, the room and the cleanup that makes it sound finished.',
    h1='How to Record a Voice-Over for a Slideshow',
    kw='how to record voice over for slideshow',
    lead='A slideshow with a clear voice-over explains itself. Write one line per slide, time it, record in a quiet room and keep the voice steady from slide to slide.',
    tldr=['Write one short line for each slide.',
          'Time the lines against the slides before you record.',
          'Record in a quiet room with the mic close and steady.',
          'Clean and level the voice, and align it slide by slide.'],
    body='''
<h2>Script per slide</h2>
<p>Write one or two sentences for each slide, and say only what the slide does not. Read the script aloud and time it, so each line fits its slide.</p>
<h2>Record in sections</h2>
<p>Record one slide at a time, so a stumble is easy to re-record. Keep the mic distance and the level the same across the sections.</p>
<h2>Clean and align</h2>
<p>Clean the voice gently and level it. Place each line on its slide, and leave a short pause before a new slide, so the viewer can see the change.</p>
''',
    vf_title='Clean the narration, slide by slide',
    vf='<p>Tunedzy cleans and levels the narration, so each slide has a clear voice-over.</p>',
    faq=[('How long should each line be?', 'As long as the slide needs and no longer. Time it aloud.'),
         ('Should I record the whole show at once?', 'No. Record in sections, so re-takes are easy.'),
         ('Can I use music under the narration?', 'Yes, if you have the right to use it. Duck it under the voice.')],
    related=['how-to-add-a-voiceover-to-a-screen-recording', 'record-a-voiceover-on-your-phone', 'how-to-add-background-music-to-a-voiceover'])

add('how-to-make-a-podcast-trailer', 'mic', ['clean-streaming-mic', 'lufs-meter'],
    title='How to Make a Podcast Trailer That Sounds Professional',
    desc='Make a short podcast trailer: pick the best moments, write a hook, record the narration, mix the clips and set the loudness for a short listen.',
    h1='How to Make a Podcast Trailer',
    kw='how to make a podcast trailer',
    lead='A trailer is a short, clear promise of the show. Pick the best moments, write a line that hooks the listener, and mix the clips with the narration at a loudness that matches the show.',
    tldr=['Pick two or three of the strongest moments from the show.',
          'Write a short narration that hooks the listener in the first seconds.',
          'Mix the clips with the narration, and duck the music under the voice.',
          'Match the loudness to the show, so the trailer does not jolt the listener.'],
    body='''
<h2>Pick the moments</h2>
<p>Choose two or three clips that make someone want the episode: a surprising line, a laugh, a clear point. Clean them first, so they sit well together.</p>
<h2>Write the hook</h2>
<p>Write a short line that tells the listener what they will get. The first few seconds decide whether they keep listening.</p>
<h2>Mix</h2>
<p>Lay the narration and clips on one timeline. Duck any music under the voice, and keep the transitions short. The <a href="/tunedzy/how-to-duck-music-under-a-voiceover">ducking how-to</a> has the steps.</p>
<h2>Match the loudness</h2>
<p>Set the trailer to the same loudness as the show, so it does not jump when a listener moves from one to the other.</p>
''',
    vf_title='Mix the trailer, match the show',
    vf='<p>Tunedzy mixes the clips and narration, ducks the music, and sets the trailer to the loudness of the show.</p>',
    faq=[('How long should a trailer be?', 'Short. A minute or two is common; shorter is often better.'),
         ('Do I need music?', 'Not always. Music under the narration works if it suits the show.'),
         ('Should it be louder than the show?', 'No. Match the show, so it does not jolt listeners.')],
    related=['how-to-make-a-podcast-intro-and-outro', 'how-to-duck-music-under-a-voiceover', 'loudness-for-youtube-podcasts-and-spotify']
)

add('how-to-record-a-voice-note-for-a-client-brief', 'booth-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record a Voice Note for a Client Brief',
    desc='Record a clear voice note for a client brief or a team handover: the room, the level, a short structure and a file that is easy to share and understand.',
    h1='How to Record a Voice Note for a Client Brief',
    kw='how to record voice note for client brief',
    lead='A voice note is quick, but a brief recorded in a noisy room is hard to use. Record in a quiet spot, structure the brief, and send a file that is easy to play and share.',
    tldr=['Record in a quiet spot, with the phone a hand&rsquo;s width from the mouth.',
          'Structure the brief: goal, audience, deadline, what to avoid.',
          'Keep it short; long notes are harder to act on.',
          'Send a compressed copy with a short written summary.'],
    body='''
<h2>Set up</h2>
<p>A quiet spot with soft surfaces is enough. Hold the phone close and steady, and record a few seconds first to check the level.</p>
<h2>Structure</h2>
<p>Say the goal first, then the audience, the deadline, and what to avoid. A short structure is easier to act on than a long, unstructured note.</p>
<h2>Share it</h2>
<p>Send a compressed copy, and add a short written summary underneath. The <a href="/tunedzy/how-to-compress-an-audio-file-for-email">email compression guide</a> covers the file size.</p>
''',
    vf_title='Clean the brief, send it clear',
    vf='<p>Tunedzy Go cleans a voice note on your phone for free. Send the clean copy with a short summary.</p>',
    faq=[('How long should a voice note be?', 'Short. A minute or two is usually enough for a brief.'),
         ('Should I transcribe it?', 'A short written summary is more useful than a transcript for a brief.'),
         ('Can I clean it on my phone?', 'Yes, with Tunedzy Go, for free.')],
    related=['clean-up-a-phone-voice-recording', 'how-to-compress-an-audio-file-for-email', 'how-to-record-a-voicemail-greeting']
)

add('how-to-make-a-vocal-comp-from-several-takes', 'neon', ['song-key-finder', 'bpm-finder'],
    title='How to Make a Vocal Comp From Several Takes',
    desc='Build one best vocal from several takes by choosing the best phrases from each: the listening order, the joins and the checks that make a comp sound seamless.',
    h1='How to Make a Vocal Comp From Several Takes',
    kw='how to make a vocal comp',
    lead='A comp is one vocal built from the best parts of several takes. Listen to each phrase, choose the strongest, and join them so the listener cannot hear where one take ends and the next begins.',
    tldr=['Record several full takes, and keep them all.',
          'Choose the best phrase from each take, not the best whole take.',
          'Join at natural breaths or pauses, with a short crossfade.',
          'Check the joins at the same level and in the same room tone.'],
    body='''
<h2>Record several takes</h2>
<p>Record the whole song or passage several times. Each take gives you choices, and the best phrases are often spread across different takes.</p>
<h2>Choose the phrases</h2>
<p>Listen to each phrase and mark the best. A comp is made of phrases, not of takes, so keep the parts that sound most alive.</p>
<h2>Join at breaths</h2>
<p>Join at a natural breath or a pause. A join in the middle of a word is hard to hide. A short crossfade at each join keeps the room sound steady. The <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade how-to</a> has the steps.</p>
<h2>Check the joins</h2>
<p>Play the whole vocal through. Listen for a jump in level, tone or room sound at each join, and adjust until none is audible.</p>
''',
    vf_title='Build the best vocal from the takes',
    vf='<p>Tunedzy Multitrack lets you line up the phrases from several takes and check each join by ear.</p>',
    faq=[('How many takes do I need?', 'Several. Enough to have choice for each phrase.'),
         ('Will the joins be audible?', 'Not if they are at breaths or pauses and the room is the same.'),
         ('Should I tune the comp?', 'Tune lightly, after the comp is built.')],
    related=['how-to-crossfade-two-recordings', 'record-a-vocal-at-home-for-a-song', 'vocal-cleanup-for-singers-and-rappers']
)

add('how-to-clean-up-a-speech-recorded-in-a-hall', 'booth-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Clean Up a Speech Recorded in a Hall',
    desc='Clean a speech recorded in a large, echoey hall: the limits of echo removal, a gentle reduction, the level for the loudest moments and the steps that help.',
    h1='How to Clean Up a Speech Recorded in a Hall',
    kw='clean up speech recorded in hall',
    lead='A speech recorded in a big hall picks up echo and crowd noise. Cleanup can reduce both, but it cannot remove a hall completely. A close mic recording helps far more than any cleanup.',
    tldr=['Echo in a big hall is hard to remove completely.',
          'Reduce the crowd noise gently, and keep the speaker natural.',
          'Level the speech so the quiet and loud parts both sit well.',
          'A close mic or a lav recording beats cleanup of a distant one.'],
    body='''
<h2>What the hall does</h2>
<p>A hall adds long reflections and crowd noise. The echo smears the words, and the crowd fills the gaps between them.</p>
<h2>What cleanup can do</h2>
<p>It can reduce the steady crowd and room noise and tidy the level. A de-reverb or echo tool reduces the smear, but cannot remove a large hall. Keep the speech natural.</p>
<h2>Levelling</h2>
<p>Speakers get louder when they are excited. Level the speech so the loud parts do not overwhelm the quiet ones. The <a href="/tunedzy/voice-cleanup-for-public-speakers">public speaker routine</a> covers the set-up.</p>
''',
    vf_title='Reduce the hall, keep the speech',
    vf='<p>Tunedzy reduces the steady room and crowd noise and levels the speech. Compare Before and After.</p>',
    faq=[('Can you remove all the echo?', 'Not completely. Reduce it and keep the speech natural.'),
         ('Is a lav mic better?', 'Yes. A close mic beats cleanup of a distant one.'),
         ('What should I check first?', 'The level on the loud parts, and the echo on the quiet ones.')],
    related=['voice-cleanup-for-public-speakers', 'wedding-speech-recording', 'remove-echo-from-vocal-recording']
)

add('how-to-record-audio-in-a-noisy-office', 'desk-wide', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Record Audio in a Noisy Office',
    desc='Record a clear voice in a noisy office: finding the quietest spot, a close mic, the air conditioning and the cleanup that helps with office noise.',
    h1='How to Record Audio in a Noisy Office',
    kw='how to record audio in noisy office',
    lead='An office has the air conditioning, the keyboards and the people. Find the quietest spot, put the mic close, and clean the steady noise. A small room or a meeting room with the door shut helps most.',
    tldr=['Find the quietest spot: a small room, a corner away from the door, or a booth.',
          'Put the mic close, and speak to it rather than across the room.',
          'Turn off the air conditioning for the take if you can.',
          'Clean the steady office noise gently.'],
    body='''
<h2>Find the quiet spot</h2>
<p>A small meeting room with the door shut is often quiet. A corner away from the door and the printers can work too. Record a few seconds of silence to check the room.</p>
<h2>Mic and distance</h2>
<p>Put the mic close and speak to it, not across the room. A close voice rises above the office hum and the keyboards.</p>
<h2>Clean</h2>
<p>Reduce the steady air conditioning and room noise gently. The <a href="/tunedzy/remove-background-noise-from-a-voice-recording">noise guide</a> covers the method, and the <a href="/tunedzy/how-to-remove-keyboard-and-desk-noise-from-a-recording">keyboard guide</a> covers clicks.</p>
''',
    vf_title='Clean the office noise',
    vf='<p>Tunedzy reduces the steady office noise and levels the voice, on your PC.</p>',
    faq=[('Can I record at my desk?', 'Yes, with the mic close and the keyboard quiet. A quiet room is better.'),
         ('What is the best time to record?', 'When the office is quiet, such as early or late. Air conditioning often runs all day.'),
         ('Should I ask colleagues to be quiet?', 'Yes, for an important take. A short, clear request works.')],
    related=['how-to-reduce-people-talking-in-the-background', 'how-to-set-up-a-quiet-recording-corner-on-a-budget', 'how-to-record-a-meeting-clearly']
)

add('how-to-remove-reverb-from-a-recording', 'booth', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Remove Reverb From a Recording',
    desc='Reduce reverb in a voice recording: what reverb is, how much can be removed, the de-reverb tools and how to avoid a hollow, unnatural voice.',
    h1='How to Remove Reverb From a Recording',
    kw='how to remove reverb from recording',
    lead='Reverb is the room sound that follows the voice. It can be reduced in a file, but removing it fully leaves a hollow, unnatural voice. Reduce it a little, and fix the room for the next take.',
    tldr=['Reverb is the dense wash of room reflections after the voice.',
          'De-reverb tools reduce it; they cannot remove a very live room cleanly.',
          'Too much de-reverb sounds hollow and processed.',
          'Soft furnishings are the lasting fix.'],
    body='''
<h2>What reverb is</h2>
<p>Reverb is the dense wash of reflections that a room adds after each sound. It makes a voice sound far away or hollow, and it is part of how a room feels.</p>
<h2>Reducing it</h2>
<p>A de-reverb tool reduces the wash. Use a light setting and compare with the original. For a very live room, expect a partial reduction, not a removal.</p>
<h2>The lasting fix</h2>
<p>Record in a soft room with rugs, curtains and a closet of clothes. The <a href="/tunedzy/what-is-reverb-vs-echo">reverb and echo explanation</a> covers the difference between the two.</p>
''',
    vf_title='Reduce the wash, keep the voice',
    vf='<p>Tunedzy reduces the room sound in its cleanup. Use Before and After to keep the voice natural.</p>',
    faq=[('Can reverb be removed completely?', 'Not without making the voice hollow. Reduce it, and fix the room next time.'),
         ('Why does my de-reverbed voice sound thin?', 'The setting is too strong. Lower it and listen again.'),
         ('Is reverb the same as echo?', 'No. Echo is a distinct repeat; reverb is a dense wash.')],
    related=['remove-echo-from-vocal-recording', 'what-is-reverb-vs-echo', 'how-to-set-up-a-quiet-recording-corner-on-a-budget']
)

add('how-to-record-a-vlog-voice', 'neon', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record a Clear Voice for a Vlog',
    desc='Record a clear voice for a vlog: a mic close to you while you move, wind and rustle to avoid, the level for a phone and the cleanup that keeps the voice steady.',
    h1='How to Record a Clear Voice for a Vlog',
    kw='how to record voice for vlog',
    lead='A vlog voice moves: you walk, turn and talk to the camera. A close mic that stays with you, a level that holds as you move, and a cleanup for wind and rustle keep the voice clear.',
    tldr=['Use a lav or a small mic close to your mouth, so the distance stays steady.',
          'Avoid rustling clothes and the wind on the mic.',
          'Set the level for the loudest moments, including when you move.',
          'Clean the rustle and the room noise gently.'],
    body='''
<h2>The mic</h2>
<p>A lav mic clipped to your clothes keeps the distance steady while you move. A small mic on a short cable works too. Keep the cable tucked so it does not rub.</p>
<h2>Wind and rustle</h2>
<p>Outdoors, use a foam or furry windshield. Indoors, avoid rustling clothes near the mic. The <a href="/tunedzy/how-to-remove-wind-noise-from-audio">wind guide</a> covers the rumble.</p>
<h2>Level and clean</h2>
<p>Set the level for the loudest moments, then check it while you move. Clean the room noise and rustle gently, and check the loudness for the platform.</p>
''',
    vf_title='A steady voice while you move',
    vf='<p>Tunedzy cleans the vlog voice gently and sets its loudness, so the voice stays clear as you move.</p>',
    faq=[('Do I need a lav mic?', 'A lav keeps the distance steady, which helps while you move.'),
         ('What causes rustle?', 'Clothing and the cable rubbing the mic. Tuck the cable and avoid loose fabric.'),
         ('Can cleanup fix wind?', 'Only some of it. A windshield is the real fix.')],
    related=['how-to-use-a-lavalier-microphone', 'how-to-remove-wind-noise-from-audio', 'record-a-voiceover-on-your-phone']
)

add('how-to-add-captions-to-a-video-from-audio', 'desk', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Add Captions to a Video From Its Audio',
    desc='Make captions for a video from its audio: a clean transcript, checking names and terms, timing the captions and exporting an SRT or VTT file.',
    h1='How to Add Captions to a Video From Its Audio',
    kw='how to add captions to video from audio',
    lead='Captions help viewers who are deaf or hard of hearing, and everyone watching without sound. Make a transcript from the audio, check it against the sound, then export a caption file for the video.',
    tldr=['Start from a clean audio file; a clear recording gives a better transcript.',
          'Check names, terms and numbers against the audio.',
          'Time the captions to the speech, and keep each caption short.',
          'Export SRT or VTT and load it into the video platform.'],
    body='''
<h2>Start with clean audio</h2>
<p>A clean recording gives a better transcript. Clean the voice first with the <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup steps</a>, then transcribe.</p>
<h2>Check the transcript</h2>
<p>A speech model misses names, technical words and quiet speech. Check each one against the audio before you export.</p>
<h2>Export the captions</h2>
<p>Tunedzy exports SRT and VTT caption files from the transcript. Load the file into your video platform, and check the timing on the first few captions. The <a href="/tunedzy/how-to-export-captions-srt-and-vtt">caption export guide</a> has the steps.</p>
''',
    vf_title='Transcribe, check, export captions',
    vf='<p>Tunedzy transcribes the audio on your PC, lets you check the words, and exports SRT or VTT captions.</p>',
    faq=[('Do captions need to be perfect?', 'They should be accurate. Check names and terms before you publish.'),
         ('Which caption format should I use?', 'SRT is widely accepted; VTT is common for the web.'),
         ('Is the audio uploaded for the transcript?', 'In Tunedzy, no. The transcript is made on your PC.')],
    related=['edit-a-podcast-by-its-words', 'tunedzy-transcript-editor', 'audio-cleanup-for-teachers']
)

add('how-to-record-a-voice-on-a-train', 'mic', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record a Voice on a Train',
    desc='Record a clear voice on a train or a bus: the noise to expect, a close mic, a quiet carriage choice and the cleanup that deals with rumble and announcements.',
    h1='How to Record a Voice on a Train',
    kw='how to record voice on train',
    lead='A train is loud: the engine rumbles and the announcements carry. A close mic, a quieter carriage and a clean take make a train recording usable, and a cleanup handles the steady rumble.',
    tldr=['Choose a quieter carriage, away from the engine and the doors.',
          'Keep the mic close and turn your face away from the carriage noise.',
          'Record between announcements, or pause during them.',
          'Clean the rumble with a low cut and the steady noise gently.'],
    body='''
<h2>Pick the carriage</h2>
<p>A carriage away from the engine and the doors is quieter. Quiet times, such as off-peak, help too.</p>
<h2>Mic and position</h2>
<p>Use a close mic or headset and keep it steady. Turn your head slightly away from the carriage noise, so the mic faces you.</p>
<h2>Clean</h2>
<p>A low cut removes much of the engine rumble. The <a href="/tunedzy/what-is-a-high-pass-filter">high-pass guide</a> explains the setting, and the <a href="/tunedzy/remove-background-noise-from-a-voice-recording">noise guide</a> covers the rest.</p>
''',
    vf_title='Clean the rumble, keep the voice',
    vf='<p>Tunedzy cleans the rumble and steady noise on a train recording, on your PC or phone.</p>',
    faq=[('Can I record on a moving train?', 'Yes, with a close mic and a quieter carriage. Expect rumble, and clean it.'),
         ('Why is the announcement in my recording?', 'The speaker is loud. Pause during announcements, or cut them in editing.'),
         ('Is recording on public transport allowed?', 'Check the rules of the operator, and get consent from people you record.')],
    related=['how-to-record-voice-in-a-car', 'how-to-remove-wind-noise-from-audio', 'recording-consent-before-you-record']
)

add('how-to-record-outdoor-interviews', 'neon-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record Outdoor Interviews Without the Noise',
    desc='Record an outdoor interview clearly: a windshield, a lav mic, a quiet spot away from traffic and the cleanup that deals with wind and street noise.',
    h1='How to Record Outdoor Interviews',
    kw='how to record outdoor interviews',
    lead='Outdoor interviews fight wind, traffic and crowds. A windshield, a close mic and a spot out of the wind make most of the difference. Cleanup can handle the rest.',
    tldr=['Use a windshield on the mic; a furry one for strong wind.',
          'Use a lav or a close mic so the distance stays steady.',
          'Choose a spot out of the wind and away from traffic.',
          'Record a few seconds of the place to check the noise first.'],
    body='''
<h2>Wind</h2>
<p>Wind is the biggest problem outdoors. A foam windshield handles a light breeze; a furry one handles stronger wind. Keep the mic out of the wind line, and stand with the wind behind you if you can.</p>
<h2>Traffic and crowds</h2>
<p>Pick a spot away from the road. Record a few seconds of the place to hear the noise, and move if it is too loud. A quiet side street is better than the main road.</p>
<h2>Clean</h2>
<p>A low cut removes much of the wind rumble, and gentle noise reduction handles the rest. The <a href="/tunedzy/how-to-remove-wind-noise-from-audio">wind guide</a> covers the method.</p>
''',
    vf_title='Clean the outdoor interview',
    vf='<p>Tunedzy cleans wind rumble and street noise gently on your PC, with Before and After to compare.</p>',
    faq=[('Is a windshield enough?', 'For a light breeze, yes. For strong wind, a furry windshield works much better.'),
         ('Should I use a lav outdoors?', 'Yes, it keeps the distance steady, with a windshield on the mic.'),
         ('Can I fix a windy recording?', 'Partly. A low cut helps with rumble; distortion from overloading cannot be fixed.')],
    related=['how-to-remove-wind-noise-from-audio', 'how-to-clean-up-an-interview-recording', 'audio-cleanup-for-journalists']
)

add('how-to-check-audio-quality-before-publishing', 'mic-wide', ['lufs-meter', 'vocal-checker'],
    title='How to Check Audio Quality Before You Publish',
    desc='A short checklist for audio quality before you publish: clipping, noise, loudness, true peak, the phone speaker test and the file you will upload.',
    h1='How to Check Audio Quality Before You Publish',
    kw='how to check audio quality before publishing',
    lead='A short check before you publish catches most problems: clipping, noise, loudness, a bad join and a file that will not play on a phone. Five minutes of checking saves a re-upload.',
    tldr=['Check for clipping: flat tops on the waveform and a harsh edge on loud words.',
          'Check the noise between words and in the silent parts.',
          'Measure the loudness and the true peak of the final file.',
          'Listen on a phone speaker and headphones, then upload the file you checked.'],
    body='''
<h2>Clipping and noise</h2>
<p>Scan the waveform for flat tops. Listen to the quiet parts for steady noise, hum and clicks. Fix anything you find before you export.</p>
<h2>Loudness and peak</h2>
<p>Measure the loudness of the whole file and check the true peak. The <a href="/tunedzy/tools/lufs-meter">free LUFS meter</a> on this site measures a file in your browser.</p>
<h2>Listen where people will hear it</h2>
<p>Listen on a phone speaker, headphones and a laptop speaker. Check the start, the end and any join. Upload the same file you checked, not an earlier version.</p>
''',
    vf_title='Check it before it goes out',
    vf='<p>Tunedzy checks the peak and sets the loudness on export. Use the free LUFS meter to check any file.</p>',
    faq=[('How long does the check take?', 'A few minutes for a short file. Long files need the same check, in sections.'),
         ('What is the most common mistake?', 'Uploading an earlier export. Check the file you upload.'),
         ('Do I need special equipment?', 'No. A phone and headphones are enough for most checks.')],
    related=['how-to-export-audio-for-spotify-and-apple-podcasts', 'what-is-true-peak-dbtp', 'my-voice-sounds-different-on-a-phone-speaker']
)
