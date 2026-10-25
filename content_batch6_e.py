"""Batch 6e (25 October 2026): fifteen how-to guides, the second half of the thirty. Same shape as content.GUIDES. GROUP_OF marks 'how'.

Tunedzy features named here exist in the app (the transcript and caption export, Multitrack and fades, Replace audio in video, the free
tools). Everything else is general practical advice.
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


add('how-to-make-a-podcast-episode-checklist', 'desk', ['lufs-meter', 'vocal-checker'],
    title='Podcast Episode Checklist: From Recording to Publish',
    desc='A podcast episode checklist from recording to publishing: the room and levels, the cleanup, the edit, the loudness and the upload check.',
    h1='Podcast Episode Checklist',
    kw='podcast episode checklist',
    lead='A repeatable checklist keeps every episode sounding like the show. Work through the recording, the cleanup, the edit, the loudness and the upload in order.',
    tldr=['Before recording: the room, the mics, the levels and a room-tone sample.',
          'After recording: clean each voice, then level the speakers.',
          'Edit by the words, cut the distractions and check every join.',
          'Before upload: measure the loudness, check the true peak and listen on a phone.'],
    body='''
<h2>Before recording</h2>
<p>Check the room, the mics and the distance. Record a few seconds of room tone. Set the level on the loudest speaker, not the quietest.</p>
<h2>After recording</h2>
<p>Save the originals. Clean each voice on its own, then level the speakers together. The <a href="/tunedzy/voice-cleanup-for-podcasters">podcaster routine</a> explains the order.</p>
<h2>Edit</h2>
<p>Edit by the words, cut the ums and the long pauses, and check each join. Keep the natural breaths.</p>
<h2>Before upload</h2>
<p>Measure the loudness and check the true peak. Listen on a phone speaker and headphones. Upload the file you checked. The <a href="/tunedzy/how-to-check-audio-quality-before-publishing">quality check guide</a> has the detail.</p>
''',
    vf_title='Run the checklist in one pass',
    vf='<p>Tunedzy cleans, levels, edits by words and exports the episode at a loudness target, with the true peak checked.</p>',
    faq=[('How long does the checklist take?', 'It depends on the episode. A routine makes it faster each time.'),
         ('What is the most skipped step?', 'Listening on a phone speaker before upload.'),
         ('Should the checklist change for each show?', 'The steps stay. The targets may change with the platform.')],
    related=['how-to-check-audio-quality-before-publishing', 'podcast-sound-professional-on-a-budget', 'voice-cleanup-for-podcasters'])

add('how-to-export-captions-srt-and-vtt', 'desk-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Export Captions as SRT and VTT',
    desc='Export captions from a transcript as SRT or VTT files: the format differences, checking the timing and loading the file into a video platform.',
    h1='How to Export Captions as SRT and VTT',
    kw='how to export captions srt vtt',
    lead='SRT and VTT are the two common caption files. They hold the text and the times for each caption. Export from a checked transcript, then check the timing on the video.',
    tldr=['SRT is widely accepted and simple.',
          'VTT is common for the web and supports a little styling.',
          'Check the transcript before export: names and terms matter.',
          'Check the first few captions in the video platform.'],
    body='''
<h2>SRT and VTT</h2>
<p>SRT is a plain text file with numbered captions and times. VTT is similar, with a header and a few more options. Most video platforms accept both.</p>
<h2>Check the transcript first</h2>
<p>Correct names, technical words and numbers before you export. A wrong name in a caption is hard to forget.</p>
<h2>Export and load</h2>
<p>Export the file from Tunedzy, then load it into your video platform. Check the timing on the first few captions, and on any fast speech. The <a href="/tunedzy/how-to-add-captions-to-a-video-from-audio">captions from audio guide</a> covers the full steps.</p>
''',
    vf_title='Export captions from a checked transcript',
    vf='<p>Tunedzy exports SRT and VTT from the transcript you have checked, on your PC.</p>',
    faq=[('Which should I use, SRT or VTT?', 'SRT is the most widely accepted. VTT works well on the web.'),
         ('Why are my captions out of time?', 'The file was exported from a different version of the audio. Export again from the final edit.'),
         ('Can I edit the file afterwards?', 'Yes, it is plain text. Check the timing after any edit.')],
    related=['how-to-add-captions-to-a-video-from-audio', 'tunedzy-transcript-editor', 'edit-a-podcast-by-its-words'])

add('how-to-name-and-organise-audio-files', 'desk', ['vocal-checker', 'lufs-meter'],
    title='How to Name and Organise Audio Files for a Project',
    desc='A simple system for naming and organising audio files: a folder per project, dated names, masters and copies kept apart, and a note of the settings.',
    h1='How to Name and Organise Audio Files',
    kw='how to name and organise audio files',
    lead='A clear file system saves hours on a project. Name files by date and content, keep masters apart from copies, and write down the settings for each session.',
    tldr=['One folder per project, with sub-folders for originals, edits and exports.',
          'Name files with the date, the episode or session, and the version.',
          'Keep the masters separate, and never overwrite an original.',
          'Write the settings for each session in a short note.'],
    body='''
<h2>Folders</h2>
<p>Make one folder per project. Inside it, keep originals, edits and exports in separate sub-folders, so you always know which file is which.</p>
<h2>Names</h2>
<p>Put the date first, then the episode or session, then the version. For example, a dated name with the episode number and the word master. Consistent names sort well and are easy to search.</p>
<h2>Masters and copies</h2>
<p>Keep the masters as they were recorded, and make copies for editing and sharing. Never overwrite an original. The <a href="/tunedzy/how-to-choose-wav-mp3-or-flac">format guide</a> explains which file to keep.</p>
<h2>Notes</h2>
<p>Write the mic, the distance, the level and the room for each session. Those notes make the next session match.</p>
''',
    vf_title='A system that finds files',
    vf='<p>Tunedzy keeps your projects and exports in separate places; name each export by its episode and version.</p>',
    faq=[('Should the date go first?', 'Yes, for sorting. A date first keeps the files in order.'),
         ('How many versions should I keep?', 'Keep the master and the exports you shared. Delete drafts you no longer need.'),
         ('Should I name files with spaces?', 'Avoid unusual characters. Use hyphens or underscores for safety.')],
    related=['how-to-back-up-your-recordings', 'how-to-choose-wav-mp3-or-flac', 'how-to-make-a-podcast-episode-checklist'])

add('how-to-back-up-your-recordings', 'desk-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Back Up Your Recordings',
    desc='A simple backup plan for recordings: two copies in two places, a check that the backup opens, and how to keep the masters safe for years.',
    h1='How to Back Up Your Recordings',
    kw='how to back up recordings',
    lead='A recording you cannot find or open is lost. Keep two copies in two places, check that the backup opens, and back up the masters first.',
    tldr=['Keep at least two copies, in two different places.',
          'Back up the masters before the exports.',
          'Check that a backup opens, from time to time.',
          'Label the backups with the date, so you know which is latest.'],
    body='''
<h2>Two copies, two places</h2>
<p>One copy on your computer and one somewhere else, such as an external drive or a cloud folder. Two places protect against a broken drive and a lost laptop.</p>
<h2>Masters first</h2>
<p>Back up the original recordings and the masters before the exports. You can make exports again from a master, but not the other way round.</p>
<h2>Check the backup</h2>
<p>Open a file from the backup every few months. A backup that does not open is not a backup.</p>
<h2>Keep it tidy</h2>
<p>Use the folder system from <a href="/tunedzy/how-to-name-and-organise-audio-files">the naming guide</a>, so the backup is easy to find.</p>
''',
    vf_title='Keep the masters safe',
    vf='<p>Keep your Tunedzy masters and exports in a folder you back up, and check one backup opens.</p>',
    faq=[('How often should I back up?', 'After each session or episode, and check the backup now and then.'),
         ('Is a cloud folder enough?', 'Two places is safer: a cloud folder and a drive you control.'),
         ('What if I lose a file?', 'Restore from the backup. If there is no backup, the file is gone.')],
    related=['how-to-name-and-organise-audio-files', 'how-to-choose-wav-mp3-or-flac', 'how-to-check-audio-quality-before-publishing'])

add('how-to-turn-a-voice-memo-into-a-song-idea', 'neon', ['song-key-finder', 'bpm-finder'],
    title='How to Turn a Voice Memo Into a Song Idea',
    desc='Turn a rough voice memo into a song idea: find the key and tempo, clean the melody, record it properly and build a demo from the best phrase.',
    h1='How to Turn a Voice Memo Into a Song Idea',
    kw='how to turn voice memo into song',
    lead='A voice memo often holds a good melody buried in noise. Find its key and tempo, clean the phrase, record it clearly, and build a demo around the part that works.',
    tldr=['Find the key and tempo of the melody, using the tools on this site.',
          'Clean the memo gently so the melody is clear.',
          'Record the melody again with a clean take, in a quiet room.',
          'Build a simple demo around the phrase that works best.'],
    body='''
<h2>Find the key and tempo</h2>
<p>Sing or play the melody and check where it sits. The <a href="/tunedzy/tools/song-key-finder">song key finder</a> and the <a href="/tunedzy/tools/bpm-finder">BPM finder</a> help you measure the memo, and a rough reading is enough to start.</p>
<h2>Clean the memo</h2>
<p>Use the <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup steps</a> gently, so the melody stays clear. Keep the original memo, as the rough feel is part of the idea.</p>
<h2>Record it again</h2>
<p>Record the melody in a quiet room with a clean take, and sing the words you have. A clean take makes it easier to judge the idea.</p>
<h2>Build the demo</h2>
<p>Build a short demo around the phrase that works best. The <a href="/tunedzy/musicians-making-demos">demo guide</a> covers the rest.</p>
''',
    vf_title='Clean the idea, then build the demo',
    vf='<p>Tunedzy cleans the memo gently and sets its level, so the melody is clear enough to build on.</p>',
    faq=[('Do I need the key to write a song?', 'It helps to know it, so the melody and the beat fit together.'),
         ('Should I clean the memo or record again?', 'Both: clean the memo to hear it, then record a clean take.'),
         ('Is a phone memo good enough for an idea?', 'Yes. The idea matters more than the quality of the first recording.')],
    related=['musicians-making-demos', 'record-a-vocal-at-home-for-a-song', 'how-to-clean-a-song-vocal-recorded-on-a-phone'])

add('how-to-record-a-spoken-word-poem', 'booth', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record a Spoken Word Poem',
    desc='Record a spoken word poem with emotion and clarity: the room, the mic distance, the pace and the cleanup that keeps the performance alive.',
    h1='How to Record a Spoken Word Poem',
    kw='how to record spoken word poem',
    lead='A spoken word poem lives in its performance: the pace, the breath and the force of the lines. Record close and dry, keep the pauses, and clean only what gets in the way.',
    tldr=['Record close and dry, in a soft room.',
          'Keep the pauses and breaths that carry the rhythm.',
          'Record several passes, and keep the most alive one.',
          'Clean the noise gently, and never over-process the performance.'],
    body='''
<h2>Set up</h2>
<p>A close mic in a soft room keeps the voice intimate and dry. Stand or sit at a steady distance, and keep it the same for every pass.</p>
<h2>Keep the performance</h2>
<p>The pauses and the breath are part of the poem. Keep them. Cutting every breath makes a performance feel rushed and unreal.</p>
<h2>Several passes</h2>
<p>Record the poem several times. The most alive pass is often not the most careful one. Keep the passes, and choose later.</p>
<h2>Clean lightly</h2>
<p>Clean the room noise and any clicks gently. Over-processing flattens the force of a performance. The <a href="/tunedzy/how-to-remove-breath-noise-from-a-voice-recording">breath guide</a> explains how far to go.</p>
''',
    vf_title='Clean the noise, keep the performance',
    vf='<p>Tunedzy cleans the room noise gently and levels the performance, keeping the breaths and pauses.</p>',
    faq=[('Should I keep the breaths?', 'Yes, most of them. They carry the rhythm.'),
         ('How many passes should I record?', 'Several. Pick the most alive one later.'),
         ('Can I add music?', 'Yes, if you have the right to use it. Duck it under the voice.')],
    related=['how-to-remove-breath-noise-from-a-voice-recording', 'record-a-vocal-at-home-for-a-song', 'how-to-make-a-voice-sound-close-and-intimate']
)

add('how-to-write-a-podcast-script-that-sounds-natural', 'desk-wide', ['clean-streaming-mic', 'vocal-checker'],
    title='How to Write a Podcast Script That Sounds Natural',
    desc='Write a podcast script that sounds like speech, not reading: short sentences, a conversational outline and the points to read aloud before you record.',
    h1='How to Write a Podcast Script That Sounds Natural',
    kw='how to write podcast script sounds natural',
    lead='A script that reads well on paper can sound stiff when spoken. Write short sentences, plan the points rather than the words, and read it aloud before you record.',
    tldr=['Write the points and the order, not every word.',
          'Use short sentences and words you would say aloud.',
          'Read the script aloud and mark where you stumble.',
          'Leave room for natural speech, and keep the pauses.'],
    body='''
<h2>Plan the points</h2>
<p>Write the points in order, with a short note for each. A talking outline sounds more natural than a script read word for word.</p>
<h2>Write for the ear</h2>
<p>Use short sentences and words you would say in conversation. Long sentences with clauses are hard to follow when heard.</p>
<h2>Read it aloud</h2>
<p>Read the script aloud before you record. Mark the lines you stumble on and rewrite them. A line that trips your tongue will trip the listener.</p>
<h2>Keep the room for speech</h2>
<p>Leave space for the natural pauses and asides. A podcast that sounds spoken is easier to listen to than one that sounds read.</p>
''',
    vf_title='Plan it, then record it clean',
    vf='<p>Tunedzy cleans and edits the recording by its words, so the natural speech you planned comes through.</p>',
    faq=[('Should I write the whole script?', 'Write the points and the key lines. A full script can sound stiff.'),
         ('How long should sentences be?', 'Short enough to say in one breath, usually.'),
         ('Can I edit the speech afterwards?', 'Yes, by the transcript. Keep the speech natural.')],
    related=['edit-a-podcast-by-its-words', 'podcast-sound-professional-on-a-budget', 'how-to-make-a-podcast-episode-checklist']
)

add('how-to-record-a-live-q-and-a', 'mic-wide', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='How to Record a Live Q and A Session Clearly',
    desc='Record a live Q and A with a clear voice for the host and the audience: the microphones, the levels, the room and the cleanup for a replay.',
    h1='How to Record a Live Q and A',
    kw='how to record a live q and a',
    lead='A Q and A has two voices: the host and the people asking. Give the host a close mic, pass a mic or a clear recording to the questions, and clean the replay gently.',
    tldr=['A close mic for the host, and a clear way to capture each question.',
          'Repeat each question into the mic if you cannot capture the audience.',
          'Set the levels for the host and the questions, so both are clear.',
          'Clean the replay gently and level the voices.'],
    body='''
<h2>The host</h2>
<p>A close mic keeps the host clear. A headset or a lav is steady, and a desk mic works if the host stays at it.</p>
<h2>The questions</h2>
<p>Pass a mic to people who ask questions, or ask them to speak close to a mic. If that is not possible, the host repeats each question clearly. The replay then makes sense.</p>
<h2>Levels and replay</h2>
<p>Set the levels for the host and the questions, so neither is too quiet. Clean the replay gently, and level the voices together. The <a href="/tunedzy/how-to-level-voices-between-speakers">levelling guide</a> shows the steps.</p>
''',
    vf_title='Clear questions, clean replay',
    vf='<p>Tunedzy cleans the replay gently and levels the host and the questions together.</p>',
    faq=[('Do I need a mic for the audience?', 'Not always. Repeating each question into the mic works well.'),
         ('How do I keep the levels even?', 'Set each mic separately, and check the balance during a test.'),
         ('Can I share the replay?', 'Check the rights and consent of the people who spoke.')],
    related=['how-to-record-a-remote-podcast-guest', 'how-to-level-voices-between-speakers', 'how-to-record-a-meeting-clearly']
)

add('how-to-test-your-microphone', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Test Your Microphone Before You Record',
    desc='A quick microphone test before a recording: the levels, the noise, the pops and the placement, in about five minutes with headphones.',
    h1='How to Test Your Microphone',
    kw='how to test your microphone',
    lead='A five-minute test catches most microphone problems before a recording. Check the level, the noise, the pops and the placement, and listen on headphones.',
    tldr=['Record a short phrase at your normal volume and check the peaks.',
          'Record ten seconds of silence and listen for noise, hum and clicks.',
          'Say a few words with p and b sounds, and check for pops.',
          'Move the mic and listen to how the sound changes.'],
    body='''
<h2>Level</h2>
<p>Record a phrase at normal volume. The peaks should sit well below the top of the meter. If they touch it, move back or lower the gain.</p>
<h2>Noise</h2>
<p>Record silence. Listen for hiss, hum, fan noise and clicks. Turn off the things you can, and check again.</p>
<h2>Pops and placement</h2>
<p>Say words with p and b. If you hear a thump, add a pop filter or move slightly to the side. Move the mic and listen to the change.</p>
<h2>Check it on headphones</h2>
<p>Listen on headphones, because small noises are easier to hear there. Keep the test short, and go ahead once it sounds right.</p>
''',
    vf_title='Test it before you record',
    vf='<p>Tunedzy checks the peaks and cleans what remains, but the test before the take still matters most.</p>',
    faq=[('How long should the test take?', 'About five minutes.'),
         ('What if the test shows noise?', 'Fix the room or the cable before the take, not after.'),
         ('Should I test every session?', 'Yes, a quick check each time keeps the sound consistent.')],
    related=['how-to-set-the-gain-on-a-microphone', 'my-audio-has-background-hiss', 'how-to-test-your-room-for-echo']
)

add('how-to-test-your-room-for-echo', 'booth-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Test Your Room for Echo',
    desc='A simple clap test to hear the echo in your recording room, and what to change once you know: the soft surfaces that cut it down most.',
    h1='How to Test Your Room for Echo',
    kw='how to test room for echo',
    lead='A clap test tells you how much echo your room has. Clap once and listen for the tail. A long, ringing tail means a hard room; a short tail means a soft one.',
    tldr=['Clap once, clearly, and listen to the tail of the sound.',
          'A long ringing tail means echo; a short one means the room is soft.',
          'Try the test in a few spots, and pick the one with the shortest tail.',
          'Add soft surfaces behind and beside the mic, and test again.'],
    body='''
<h2>The clap test</h2>
<p>Stand where you will record, and clap once. Record the clap, or listen to it live, and hear how long the sound lasts. A clean room has a short tail; a hard room rings.</p>
<h2>Try spots</h2>
<p>Try a few spots: a corner, a wardrobe, the middle of the room. Pick the one where the tail is shortest.</p>
<h2>Soften</h2>
<p>Put rugs, curtains, cushions and clothes on the hard surfaces behind and beside the mic. Clap again. The <a href="/tunedzy/what-is-reverb-vs-echo">reverb and echo explanation</a> covers what you are hearing.</p>
''',
    vf_title='Soften the room, then record',
    vf='<p>A soft room cuts echo at the source. Tunedzy can reduce what remains in the file.</p>',
    faq=[('Is a clap test accurate?', 'It is a practical guide, not a measurement. It shows whether a room is soft or hard.'),
         ('Where is the best spot?', 'Often a corner with soft things around, or a wardrobe of clothes.'),
         ('Should I buy acoustic panels?', 'Only after soft furnishings. They often do most of the work.')],
    related=['how-to-set-up-a-quiet-recording-corner-on-a-budget', 'remove-echo-from-vocal-recording', 'how-to-test-your-microphone']
)

add('how-to-record-a-voice-in-a-bedroom', 'booth', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record a Voice in a Bedroom',
    desc='Record a clear voice in a bedroom: picking the spot, softening the room with what you have, the fan and the street, and a cleanup that suits a bedroom.',
    h1='How to Record a Voice in a Bedroom',
    kw='how to record voice in bedroom',
    lead='A bedroom is one of the best home booths: it has soft furniture and a bed to absorb sound. Pick the spot, soften the walls behind you, and switch off the noise.',
    tldr=['Pick the spot with the most soft surfaces: the bed, the wardrobe, the curtains.',
          'Record facing into the soft side of the room, not the bare wall.',
          'Switch off the fan, the air conditioning and the phone notifications.',
          'Check the room tone and clean the rest gently.'],
    body='''
<h2>Pick the spot</h2>
<p>A bedroom with a bed, a wardrobe and curtains is already soft. Record in the part of the room with the most fabric, and face into it.</p>
<h2>Soften what you have</h2>
<p>Hang a blanket behind the mic, or drape a towel over a hard surface. The <a href="/tunedzy/how-to-test-your-room-for-echo">clap test</a> shows whether it helps.</p>
<h2>Switch off the noise</h2>
<p>Turn off the fan, the air conditioning and the notifications. Close the window if the street is loud.</p>
<h2>Clean</h2>
<p>Check the room tone and clean the steady noise gently. The <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup steps</a> apply to a bedroom recording too.</p>
''',
    vf_title='Record in the softest corner',
    vf='<p>Tunedzy cleans the bedroom recording on your PC, with Before and After to check it.</p>',
    faq=[('Is a bedroom good enough for a podcast?', 'Yes. A soft bedroom is a practical home booth for many people.'),
         ('What about the bed creaking?', 'Move still during the take, and keep the mic away from the frame.'),
         ('Should I record with the door open?', 'Shut it to reduce the house noise.')],
    related=['how-to-set-up-a-quiet-recording-corner-on-a-budget', 'how-to-test-your-room-for-echo', 'record-a-voiceover-on-your-phone']
)

add('how-to-set-levels-for-a-livestream', 'mic-wide', ['clean-streaming-mic', 'vocal-checker'],
    title='How to Set Levels for a Livestream',
    desc='Set microphone and stream levels for a livestream so the voice is clear and steady: the input, the peaks, the game audio balance and a test before you go live.',
    h1='How to Set Levels for a Livestream',
    kw='how to set levels for livestream',
    lead='A livestream has the voice, the game or the music, and the alerts. Set the voice first, keep it steady, balance the rest under it, and test the mix before you go live.',
    tldr=['Set the microphone input so the loudest words peak around -6 dB.',
          'Balance the game or music under the voice, not at the same level.',
          'Test a short clip, recorded back, before going live.',
          'Keep the level steady during the stream, and check it now and then.'],
    body='''
<h2>The voice first</h2>
<p>Set the microphone input so your loudest words peak well below the top of the meter. Speak as you will on stream, and check the peaks.</p>
<h2>The game or music</h2>
<p>Balance the game or music under the voice, so the words are always the clearest sound. Lower the game audio if you have to strain to hear the voice.</p>
<h2>Test</h2>
<p>Record a short test, play it back, and listen on headphones and a speaker. Go live only when the voice is clear and steady. The <a href="/tunedzy/voice-cleanup-for-streamers">streamer routine</a> covers the mic and the cleanup.</p>
''',
    vf_title='Set the voice, balance the rest',
    vf='<p>Tunedzy Live Studio cleans the microphone live on Windows, so the voice stays clear under the game.</p>',
    faq=[('How loud should the game be?', 'Under the voice. Listen during the test and adjust.'),
         ('Why does my voice drop out?', 'The gain changed or the mic moved. Check the setup before you go live.'),
         ('Do I need to check during the stream?', 'Yes, now and then, especially when the game changes.')],
    related=['voice-cleanup-for-streamers', 'tunedzy-live-studio', 'best-virtual-audio-mixer-for-streamers']
)

add('how-to-add-sound-effects-to-a-voiceover', 'neon', ['vocal-checker', 'lufs-meter'],
    title='How to Add Sound Effects to a Voiceover',
    desc='Add sound effects to a voiceover without hiding the words: choosing effects you have the right to use, timing them to the speech and balancing them under the voice.',
    h1='How to Add Sound Effects to a Voiceover',
    kw='how to add sound effects to voiceover',
    lead='Sound effects add texture to a voiceover, but they must not hide the words. Choose effects you have the right to use, time them to the speech, and balance them below the voice.',
    tldr=['Use effects you have the right to use, from your own recordings or licensed libraries.',
          'Time the effects to a word or a pause, not in the middle of speech.',
          'Keep effects below the voice, and duck them under speech.',
          'Use only a few effects; too many distract the listener.'],
    body='''
<h2>Rights first</h2>
<p>Use effects from your own recordings or from a library you have a licence for. Check the licence before you publish.</p>
<h2>Timing</h2>
<p>Place the effect at a word or in a pause. An effect that lands on top of a key word makes it hard to hear.</p>
<h2>Balance</h2>
<p>Keep effects below the voice, and duck them under speech where they overlap. The <a href="/tunedzy/what-is-ducking">ducking explanation</a> covers the method.</p>
<h2>Restraint</h2>
<p>A few well-placed effects are better than many. Remove any effect that the listener notices more than the voice.</p>
''',
    vf_title='Effects under the voice',
    vf='<p>Tunedzy Multitrack lets you place effects on their own track and duck them under the voice.</p>',
    faq=[('Where do I find effects?', 'Your own recordings, or a library with a licence you have.'),
         ('How loud should an effect be?', 'Below the voice. Listen on a phone speaker.'),
         ('Can I use an effect from a film?', 'Only with the rights. Check first.')],
    related=['how-to-add-background-music-to-a-voiceover', 'how-to-duck-music-under-a-voiceover', 'tunedzy-multitrack']
)

add('how-to-make-a-voiceover-sound-natural', 'booth-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Make a Voiceover Sound Natural',
    desc='Make a voiceover sound like a person talking, not a reading: pace, pauses, emphasis and a light cleanup that keeps the voice human.',
    h1='How to Make a Voiceover Sound Natural',
    kw='how to make voiceover sound natural',
    lead='A natural voiceover sounds like someone talking to the listener. Pace, pauses and a little emphasis do most of the work; the cleanup should stay out of the way.',
    tldr=['Speak to one listener, as if talking to a friend.',
          'Keep the pace steady, with pauses where a person would breathe.',
          'Emphasise the key words, not every word.',
          'Clean lightly, so the voice does not sound processed.'],
    body='''
<h2>Speak to one person</h2>
<p>Picture one listener and talk to them. A voice aimed at a crowd sounds like a speech; a voice aimed at one person sounds warm.</p>
<h2>Pace and pauses</h2>
<p>Keep the pace steady, and pause at the ends of thoughts. A short breath before a new idea makes the voice feel human.</p>
<h2>Emphasis</h2>
<p>Stress the key words and let the rest run. Stressing every word flattens the rhythm.</p>
<h2>Clean lightly</h2>
<p>Clean the noise and clicks gently. Over-processing makes a voice sound artificial, which listeners notice quickly. The <a href="/tunedzy/does-ai-cleanup-change-your-voice">AI cleanup and your voice guide</a> covers the balance.</p>
''',
    vf_title='Natural voice, light cleanup',
    vf='<p>Tunedzy cleans the noise and levels the voice lightly, so the performance stays natural.</p>',
    faq=[('Should I read from a script?', 'A script is fine. Practise it aloud until it sounds like talking.'),
         ('What makes a voice sound robotic?', 'Flat pace, no pauses and heavy processing. Fix the pace first.'),
         ('Does cleanup make a voice unnatural?', 'Heavy cleanup can. Keep it light and compare with the original.')],
    related=['my-voice-sounds-robotic-after-cleanup', 'how-to-write-a-podcast-script-that-sounds-natural', 'record-a-voiceover-on-your-phone']
)

add('how-to-fix-a-cut-in-the-middle-of-a-word', 'desk', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Fix a Cut in the Middle of a Word',
    desc='Fix an audible cut in the middle of a word after editing: the join point, a crossfade, matching the room tone and the checks that make it seamless.',
    h1='How to Fix a Cut in the Middle of a Word',
    kw='how to fix cut in middle of word audio',
    lead='A cut in the middle of a word sounds wrong because the sound stops or jumps. Move the join to a pause or a breath, use a short crossfade, and match the room tone.',
    tldr=['Move the join to a pause or a breath, if you can.',
          'Use a short crossfade so the sound blends into the next part.',
          'Match the room tone on both sides of the join.',
          'Listen at normal volume, and check the join more than once.'],
    body='''
<h2>Find the cause</h2>
<p>A word that is cut sounds clipped or jumps. The join may be in the middle of a vowel or a consonant, where the sound is still moving.</p>
<h2>Move the join</h2>
<p>If you can, move the cut to a pause or a breath, where the sound is already quiet. Moving the join is better than any repair.</p>
<h2>Crossfade and room tone</h2>
<p>Use a short crossfade at the join, and add a little room tone under it if the background changes. The <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade how-to</a> has the steps.</p>
<h2>Check it</h2>
<p>Play the join several times at normal volume, on headphones and a speaker. Fix it until it is not audible.</p>
''',
    vf_title='Move the join, blend the sound',
    vf='<p>Tunedzy Multitrack lets you move a join and blend it with a short fade, then check it by ear.</p>',
    faq=[('Can a cut in a word always be hidden?', 'Usually, if the join is moved to a pause or the crossfade is right.'),
         ('How long should the crossfade be?', 'Short. Listen to the join rather than measure it.'),
         ('What if the room tone changes?', 'Add a little room tone under the join to match it.')],
    related=['how-to-crossfade-two-recordings', 'what-is-crossfade', 'edit-a-podcast-by-its-words']
)
