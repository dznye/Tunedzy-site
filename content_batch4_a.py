"""Batch 4a (25 October 2026): ten how-to guides. Same shape as content.GUIDES; merged in content.py.

Each page answers one job, says what works without any tool, and names where Tunedzy helps. No invented numbers, reviews or counts.
"""

PHOTO = {}
TOOLS = {}
GUIDES = {}
ORDER = []
GROUP = 'how'


def add(slug, photo, tools, **g):
    GUIDES[slug] = g
    PHOTO[slug] = photo
    TOOLS[slug] = tools
    ORDER.append(slug)


add('how-to-record-a-podcast-on-your-phone', 'booth', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='How to Record a Podcast on Your Phone (Solo and Two Voices)',
    desc='Record a podcast episode on a phone: where to put the phone, how to handle two voices, the settings that matter and the cleanup afterwards.',
    h1='How to Record a Podcast on Your Phone',
    kw='how to record a podcast on your phone',
    lead='A phone can record a podcast that sounds good enough to publish. The room and the distance do most of the work; the app matters less than you think.',
    tldr=['Record in a small, soft room, with the fans and the fridge off.',
          'For two people, put each phone or mic close to its own speaker, not one phone between you.',
          'Record a few seconds of room tone before the episode starts, for cleanup later.',
          'Keep the raw file and clean a copy.'],
    body='''
<h2>The setup that matters most</h2>
<p>Pick the quietest room you have and make it softer: a rug, curtains, a sofa, and clothes on a rail behind you. Sit at a table with the phone on a stand, about a hand&rsquo;s width from your mouth and a little off to the side. A phone lying flat on a table picks up every knock and echo, so lift it.</p>
<h2>Two people on two phones</h2>
<p>One phone in the middle of a table records both voices, but the nearer person is always louder. Two phones, each close to its own speaker, give you two clean tracks. Record each phone on its own and line the two files up afterwards by the clap at the start: clap once, loudly, at the start of both recordings.</p>
<h2>Settings</h2>
<p>Use the highest quality the recorder offers, usually a lossless or high-bit-rate format. Turn on any "do not disturb" mode so a call does not cut into the take, and close background apps that use the microphone.</p>
<h2>Before you hit record</h2>
<p>Record ten seconds of silence with everyone quiet. This room tone is the sound a noise cleaner learns from. Then do a short test and listen back on headphones.</p>
<h2>After the episode</h2>
<p>Keep the raw recordings. Clean a copy with <a href="/tunedzy/clean-up-a-phone-voice-recording">the phone cleanup steps</a>, level the two voices, and export once at a loudness target. <a href="/tunedzy/podcast-sound-professional-on-a-budget">The budget podcast guide</a> covers the rest of the chain.</p>
''',
    vf_title='Clean the episode on your phone',
    vf='<p>Tunedzy Go cleans a recording you make or choose, on the phone, for free. Keep the raw file and export the cleaned copy.</p>',
    faq=[('Can I record two people on one phone?', 'Yes, but the voices will differ in level. Two phones, each close to its speaker, sound more even.'),
         ('What should the room sound like?', 'Quiet and soft. You should hear the voices and very little echo or hum.'),
         ('Do I need a podcast app?', 'No. Any recorder with a good quality setting works. Cleaning and levelling are the steps that make it sound finished.')],
    related=['clean-up-a-phone-voice-recording', 'podcast-sound-professional-on-a-budget', 'how-to-record-a-remote-podcast-guest'])

add('how-to-clean-a-song-vocal-recorded-on-a-phone', 'neon', ['song-key-finder', 'bpm-finder', 'vocal-checker'],
    title='How to Clean a Song Vocal Recorded on a Phone',
    desc='Turn a rough phone vocal into something you can use on a song: cleanup first, then key and timing, then level, with the limits of each step.',
    h1='How to Clean a Song Vocal Recorded on a Phone',
    kw='clean song vocal recorded on phone',
    lead='A phone vocal often has room sound, noise and a level that jumps around. Clean it before you tune or mix it, so the later steps work on a clean voice.',
    tldr=['Clean the noise and the room sound first, gently.',
          'Check the key and tempo of the beat, so the vocal can match them.',
          'Level the vocal to sit at a steady volume against the beat.',
          'Tune last, lightly, and listen after each step.'],
    body='''
<h2>Start with the take, not the plugins</h2>
<p>A phone vocal records everything in the room. Clean it first, with gentle settings, because tuning and compression make noise more obvious. Record the vocal dry if you can: no room effects while you record, because you can add reverb later.</p>
<h2>Find the key and the tempo</h2>
<p>Knowing the key lets you tune the vocal to the right scale, and the tempo tells you where the phrases should line up. The <a href="/tunedzy/tools/song-key-finder">song key finder</a> and the <a href="/tunedzy/tools/bpm-finder">BPM finder</a> on this site measure both in your browser.</p>
<h2>Level it against the beat</h2>
<p>Set the vocal so the words sit clearly above the beat without covering it. Check at a low listening level too, where a vocal that is too quiet disappears first.</p>
<h2>Tune lightly</h2>
<p>Tuning works best when it only nudges the notes. Heavy correction sounds robotic. Compare the tuned and untuned takes, and keep the one that sounds like the singer.</p>
<h2>Check the vocal</h2>
<p>The <a href="/tunedzy/tools/vocal-checker">vocal checker</a> looks for noise, clipping and tone problems in a file. Use it before the final mix, not after.</p>
''',
    vf_title='Clean the vocal, then mix it',
    vf='<p>Tunedzy cleans the vocal, lines it up with the beat in Multitrack, and exports the mix at a loudness target. Your beat stays in your own DAW.</p>',
    faq=[('Should I tune a phone vocal at all?', 'A light touch usually helps. Heavy tuning makes a phone vocal sound robotic.'),
         ('Can I use the phone recording in a song?', 'Yes, once it is cleaned and levelled. A clean phone vocal can work well for demos and some releases.'),
         ('Do I need the key of the beat?', 'It helps. Tuning and harmony work best when they match the key of the beat.')],
    related=['record-a-vocal-at-home-for-a-song', 'clean-up-a-phone-voice-recording', 'fix-vocals-recorded-on-phone'])

add('how-to-level-voices-between-speakers', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='How to Level Voices Between Speakers',
    desc='Make two or more speakers sound equally loud: why one voice is always louder, how to level each speaker, and how to check the balance.',
    h1='How to Level Voices Between Speakers',
    kw='level voices between speakers',
    lead='One speaker closer to the mic is always louder. Levelling brings each voice to a similar volume, so the listener does not reach for the volume control between speakers.',
    tldr=['Level each speaker on their own track first, before mixing them together.',
          'Aim for the same perceived loudness, not the same peak level.',
          'Check the balance on headphones and on a phone speaker.',
          'Automatic levelling helps, but a manual pass usually sounds more natural.'],
    body='''
<h2>Why voices differ</h2>
<p>Distance, mic type and how loudly someone speaks all change the level. A quiet, careful speaker and a loud, animated one can sit 10 dB apart in the same room. A listener hears that as one person being far away.</p>
<h2>Level each voice first</h2>
<p>Work on each speaker separately. Set the level of each voice so the words are clear and the volume matches the others. Do this before you mix, because a voice that is right on its own can still sound too loud next to another.</p>
<h2>Use loudness, not peaks</h2>
<p>Peaks tell you about the loudest word, not how loud a speaker sounds. Use the average loudness of each speaker&rsquo;s part (the LUFS value) to compare them. The <a href="/tunedzy/what-is-lufs">LUFS explanation</a> covers the idea.</p>
<h2>Check the balance</h2>
<p>Listen on headphones, then on a phone speaker, because phones make quiet voices vanish. If you have to turn up the volume to hear one speaker, that speaker needs raising.</p>
<h2>Be gentle with automatic levelling</h2>
<p>Automatic levellers can pump the quiet parts up along with the room noise. Use them as a finishing touch and keep the dynamics a speaker naturally has.</p>
''',
    vf_title='Level each voice, then mix',
    vf='<p>Multitrack in Tunedzy gives each speaker a track, so you can level them one by one and export the mix at a loudness target.</p>',
    faq=[('Is it better to level by ear or by number?', 'Both. Use a number to get close, then listen to decide.'),
         ('Why does the host always sound quieter?', 'Usually the host is further from the mic. Move the host&rsquo;s mic closer or raise the host&rsquo;s track.'),
         ('Can I level a recording that is already mixed?', 'Only roughly. Separate tracks give much better control, so record each person separately when you can.')],
    related=['podcast-sound-professional-on-a-budget', 'how-to-record-a-remote-podcast-guest', 'how-to-clean-up-an-interview-recording'])

add('how-to-fix-a-crackling-recording', 'booth-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Fix a Crackling Recording',
    desc='Find where a crackle comes from (cable, gain, a loose connection or clipping) and fix what can be fixed, with the steps in order.',
    h1='How to Fix a Crackling Recording',
    kw='fix crackling recording',
    lead='A crackle is a fast, rough noise on top of the voice. It has a few common causes, and the cause decides the fix. Find it before you clean it.',
    tldr=['Crackle from the gain is usually clipping; check the waveform for flat tops.',
          'Crackle from a cable or a connection is intermittent; wiggle the cable to test it.',
          'Dry, dusty crackle on a recording made long ago needs a click repair.',
          'Fix the cause on the next take, then clean the old one.'],
    body='''
<h2>Find the cause</h2>
<p>Play the recording and listen for when the crackle happens. If it happens only on loud words, the input is too hot and the sound is clipping: check the waveform for flat tops. If it happens when you move the cable, the connection is loose. If it is a steady dry crackle everywhere, the recording is probably a worn or dusty source.</p>
<h2>If it is clipping</h2>
<p>Lower the input level and record again if you can. If you cannot, a clipping repair rebuilds some of the peaks. The <a href="/tunedzy/fix-clipped-distorted-audio">clipping guide</a> explains what repair can and cannot do.</p>
<h2>If it is a loose connection</h2>
<p>Check the cable, the plug and the USB port. Replace the cable if it crackles when it bends. A crackle from a connection cannot be fixed in the file once it is in the recording, so the next take matters more than the repair.</p>
<h2>If it is clicks and crackle in the file</h2>
<p>Short clicks and a light dusty crackle can be mended with a click repair. Use the lowest setting that removes them, and listen for dull patches afterwards.</p>
<h2>Check the result</h2>
<p>Listen on headphones after each step. A repair that removes the crackle but leaves the voice dull is too strong.</p>
''',
    vf_title='Mend the clicks, keep the voice',
    vf='<p>Tunedzy&rsquo;s Repair finds clicks and crackle and mends them before the cleanup. Compare Before and After.</p>',
    faq=[('Is crackle always fixable?', 'Clicks and light crackle usually are. Clipping and a failing connection are only partly fixable.'),
         ('Can a crackling USB mic be fixed?', 'Try another cable and port first. If the crackle changes when you move the cable, replace it.'),
         ('Why does my recording crackle only on loud parts?', 'Clipping. Lower the input so the loudest words stay below the top of the meter.')],
    related=['fix-clipped-distorted-audio', 'how-to-remove-keyboard-and-desk-noise-from-a-recording', 'clean-up-a-phone-voice-recording'])

add('how-to-record-audio-for-youtube-videos', 'mic-wide', ['lufs-meter', 'vocal-checker'],
    title='How to Record Audio for YouTube Videos',
    desc='Record a clear voice for a YouTube video: the setup, the mic distance, the levels, and the cleanup and loudness that make it sound finished.',
    h1='How to Record Audio for YouTube Videos',
    kw='how to record audio for youtube videos',
    lead='Viewers forgive a plain picture faster than poor sound. A clear, even voice with a steady level does more for a video than any gear upgrade.',
    tldr=['Record the voice separately from the picture, when you can.',
          'Keep the mic about a hand&rsquo;s width from the mouth, a little off-axis.',
          'Set the level so the loudest words stay well below full scale.',
          'Clean, level and export to a loudness target before you put it into the video.'],
    body='''
<h2>Record the voice on its own</h2>
<p>A separate audio recording is easier to clean than the sound in a camera. Record the voice on a dedicated recorder or a phone while the camera records the picture, then line the two up with a clap at the start.</p>
<h2>Distance and room</h2>
<p>Keep the mic close enough to hear clearly, but far enough that breath pops stay quiet. A soft room matters more than a better mic: a bedroom with a rug and curtains beats a bare room with an expensive mic.</p>
<h2>Level and clipping</h2>
<p>Set the input so the loudest words peak around the middle of the meter, not the top. A video that clips once is far more annoying than a voice that is a little quiet.</p>
<h2>Clean and level</h2>
<p>Use the <a href="/tunedzy/clean-up-a-phone-voice-recording">cleanup steps</a>, then set the level to a loudness target for online video. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the numbers. Check the true peak before you export.</p>
<h2>Put it back into the video</h2>
<p>If the video already has the wrong sound, <a href="/tunedzy/put-clean-audio-back-into-a-video">replace the audio</a> and keep the picture as it is.</p>
''',
    vf_title='Clean the voice for the video',
    vf='<p>Tunedzy cleans the voice, sets the loudness for online video, and can put the cleaned sound back into your video without re-encoding the picture.</p>',
    faq=[('Should I use a mic or the camera sound?', 'A mic close to the mouth is almost always better than a camera microphone far away.'),
         ('Is -14 LUFS the right level for YouTube?', 'It is a common reference. Check YouTube&rsquo;s own guidance for the current rule.'),
         ('Can I fix bad audio in a finished video?', 'Partly: clean the sound and put it back. The picture does not change.')],
    related=['record-a-voiceover-on-your-phone', 'put-clean-audio-back-into-a-video', 'loudness-for-youtube-podcasts-and-spotify'])

add('how-to-add-a-voiceover-to-a-screen-recording', 'desk', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Add a Voiceover to a Screen Recording',
    desc='Record a clean voiceover for a screen recording or tutorial: timing, the script, the room, and a voice that sits well over the on-screen sound.',
    h1='How to Add a Voiceover to a Screen Recording',
    kw='how to add voiceover to screen recording',
    lead='A screen recording with a clear voice explains itself. Record the voice to match the screen, keep the room quiet, and leave room for the on-screen sound.',
    tldr=['Write or outline the script, then record the voice against the screen.',
          'Record the voice in a quiet room with the screen&rsquo;s own sound off.',
          'Leave a short pause before each new step so the viewer can see what changed.',
          'Clean the voice and balance it under any music.'],
    body='''
<h2>Script the steps</h2>
<p>A short outline with one line per step is enough. Read it aloud once with a timer to see how long each step takes. Speak to the screen: name the thing the viewer should look at, then say what it does.</p>
<h2>Record the voice</h2>
<p>Record the voice in a quiet room, away from the computer fan. Mute notifications and other audio so the recording is clean. Record step by step, one take per section, so you can replace a single bad line without re-recording the whole tutorial.</p>
<h2>Line it up with the screen</h2>
<p>Place each section of the voice against the matching part of the screen recording. Leave a short gap before a new step, so the viewer sees the change before the voice explains it.</p>
<h2>Balance it</h2>
<p>If the screen has sound or music, lower it under the voice, not the other way round. Check the balance on a laptop speaker, which is what many viewers will hear.</p>
<h2>Clean and export</h2>
<p>Clean the voice gently, then export the mix at a loudness target for online video.</p>
''',
    vf_title='Clean the voice under the screen',
    vf='<p>Tunedzy cleans the voiceover and balances it with music in Multitrack, then exports at a loudness target.</p>',
    faq=[('Should I record the voice first or after the screen?', 'Record the voice against the finished screen recording, so the timing matches the actions.'),
         ('How do I stop the computer fan being picked up?', 'Turn the fan down, or record with the laptop on a stand away from the mic.'),
         ('Is there a free way to do this?', 'Yes. Any recorder for the voice and any free editor for the mix will do the job.')],
    related=['record-a-voiceover-on-your-phone', 'how-to-record-audio-for-youtube-videos', 'remove-background-noise-from-a-voice-recording'])

add('how-to-reduce-people-talking-in-the-background', 'booth', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Reduce People Talking in the Background of a Recording',
    desc='Reduce background chatter in a voice recording: what can be done with a gate and EQ, what cannot, and how to record so it does not happen.',
    h1='How to Reduce People Talking in the Background',
    kw='reduce background talking in recording',
    lead='Other people talking in the background is one of the hardest things to remove, because it sounds like speech. Reduce it, do not expect it to vanish, and record so it cannot get in.',
    tldr=['Background speech is hard to separate from your voice, because it sounds like speech.',
          'A gate can quieten it between your phrases; it will not remove it under them.',
          'Moving the mic closer to you is the most effective fix.',
          'Ask the people to be quiet, or record in another room.'],
    body='''
<h2>Why it is hard</h2>
<p>Noise removal works best on sounds that do not change. Other people talking changes all the time and has the same frequency range as your voice. A tool that removes it can remove parts of your voice too.</p>
<h2>What helps in the file</h2>
<p>A gate set just above the room noise quietens background speech between your phrases. A little less high-end on the background can soften it, but the balance has to stay natural. Expect a reduction, not a removal.</p>
<h2>What helps on the day</h2>
<p>Move the mic closer to you so your voice is louder than the room. Record in another room, or ask people to pause during the take. A close mic with a quiet room beats any cleanup.</p>
<h2>Know when to re-record</h2>
<p>If the background speech is as loud as your voice, cleanup will leave you with a muffled, odd sound. A short re-take of that section is quicker and sounds better.</p>
''',
    vf_title='Reduce the chatter, keep your voice',
    vf='<p>Tunedzy&rsquo;s cleanup reduces steady room noise. For speech in the background, use Before and After and expect a reduction, not a removal.</p>',
    faq=[('Can AI remove people talking in the background?', 'It can reduce it, but not always without affecting the voice. Check the result carefully.'),
         ('Is it better to re-record?', 'Usually, if the background speech is loud. A short re-take sounds better than heavy cleanup.'),
         ('What about a noisy café?', 'Record somewhere quieter, or with the mic very close to your mouth.')],
    related=['remove-background-noise-from-a-voice-recording', 'what-is-a-noise-gate', 'clean-up-a-phone-voice-recording'])

add('how-to-record-an-audiobook-at-home', 'booth-wide', ['voice-recorder-noise-cancellation', 'lufs-meter'],
    title='How to Record an Audiobook at Home',
    desc='Record an audiobook narration at home: the room, the mic, consistent sound, levels for audiobook platforms and cleanup that keeps long sessions consistent.',
    h1='How to Record an Audiobook at Home',
    kw='record audiobook at home',
    lead='An audiobook is hours of speech that must sound the same from the first chapter to the last. The room, the mic and the level must stay fixed for the whole project.',
    tldr=['Build a booth or use a closet of clothes; the room must stay the same for the whole book.',
          'Keep the mic distance and the level fixed, and note the settings for each session.',
          'Record in short sessions, and re-record a whole chapter if the sound changes.',
          'Clean every chapter the same way, then check the loudness against the platform rules.'],
    body='''
<h2>Keep the room the same</h2>
<p>Consistency is the main job. Record every session in the same spot, at the same time of day if you can, with the same fans off. A change of room shows up as a change of sound between chapters.</p>
<h2>Keep the mic and the level fixed</h2>
<p>Mark the mic position on the desk and write down the level for each session. Speak at a steady volume and take a breath between sentences rather than rushing.</p>
<h2>Record in short sessions</h2>
<p>Short sessions keep your voice fresh and make the sound more even. Stop when your voice tires, and do not carry a tired voice into the next chapter.</p>
<h2>Clean and check</h2>
<p>Clean each chapter with the same settings. Then check the loudness against the platform you publish on, because audiobook platforms have their own rules. The <a href="/tunedzy/blog/what-loudness-should-a-voice-over-be">voice-over loudness guide</a> covers the common targets.</p>
''',
    vf_title='Clean every chapter the same way',
    vf='<p>Tunedzy applies the same cleanup and loudness target to every file, so chapters match. Check each platform&rsquo;s rules before you upload.</p>',
    faq=[('Do I need a professional booth?', 'No. A small room with soft furnishings is a practical start for many narrators.'),
         ('How do I keep the sound the same across months?', 'Note the mic position, distance and level, and record in the same room.'),
         ('Who sets the loudness rules?', 'Each audiobook platform sets its own. Check their current guidance before you upload.')],
    related=['record-a-voiceover-on-your-phone', 'podcast-sound-professional-on-a-budget', 'loudness-for-youtube-podcasts-and-spotify'])

add('how-to-record-a-lecture-or-tutorial-voice', 'desk-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Record a Lecture or Tutorial Voice',
    desc='Record a clear voice for lectures, courses and tutorials: a quiet room, a steady level, pacing and the cleanup that keeps long recordings consistent.',
    h1='How to Record a Lecture or Tutorial Voice',
    kw='record lecture voice at home',
    lead='A lecture or course needs a voice that stays clear for an hour or more. Set the room and the level once, speak steadily, and clean the recording gently.',
    tldr=['Record in a quiet room, with the air conditioning off for the take.',
          'Set the level once and keep the mic distance the same.',
          'Pace yourself: a steady speaking speed is easier to follow than a fast one.',
          'Cut the long pauses and repeated words, but keep the breath between ideas.'],
    body='''
<h2>The room and the mic</h2>
<p>Lectures are long, so a quiet room matters more than a fancy mic. Turn off the air conditioning or the fan for the take. Put the mic on a stand at a steady distance, so the voice does not move in and out of focus.</p>
<h2>Level and pace</h2>
<p>Set the level before you start, and check it after the first five minutes. Speak a little more slowly than in conversation. Listeners follow a steady pace much more easily than a fast one.</p>
<h2>Record in parts</h2>
<p>Record in sections rather than in one long take. A section is easy to re-record if you stumble, and it keeps the sound even across the lecture.</p>
<h2>Cleanup</h2>
<p>Use the <a href="/tunedzy/clean-up-a-phone-voice-recording">cleanup steps</a> gently. Then cut the long pauses and repeated words in the transcript, leaving the short breaths between ideas. The <a href="/tunedzy/edit-a-podcast-by-its-words">edit-by-words guide</a> shows how.</p>
''',
    vf_title='Clean and edit the lecture',
    vf='<p>Tunedzy cleans the recording, transcribes it on your PC, and lets you cut words and pauses before you export captions.</p>',
    faq=[('Should I use a lapel mic or a desk mic?', 'A lapel mic keeps the distance steady. A desk mic on a stand is also good if you keep still.'),
         ('How long can a lecture recording be?', 'Long recordings take more memory. Record in sections so each file is manageable.'),
         ('Can I add captions?', 'Yes. A transcript made on your PC exports as captions. Check the wording before you publish.')],
    related=['edit-a-podcast-by-its-words', 'clean-up-a-phone-voice-recording', 'how-to-record-an-audiobook-at-home'])

add('how-to-clean-audio-from-a-smartphone-video', 'neon-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Clean Audio From a Smartphone Video',
    desc='Clean the sound of a phone video: pull out the audio, clean it, check it and put it back without touching the picture.',
    h1='How to Clean Audio From a Smartphone Video',
    kw='clean audio from smartphone video',
    lead='A phone video has its sound built in, and the phone&rsquo;s microphone is often far from the speaker. You can clean the sound on its own and put it back, keeping the picture as it is.',
    tldr=['Separate the audio from the picture, clean it, then put it back.',
          'The picture is copied, not re-encoded, so its quality does not drop.',
          'Phone videos often have wind, room echo and clipping; check each.',
          'Keep the original video in case you want the old sound back.'],
    body='''
<h2>Why clean the sound on its own</h2>
<p>Cleaning a video directly can change the picture if the tool re-encodes it. Separating the sound lets you clean the voice and leave the picture alone.</p>
<h2>What to check first</h2>
<p>Listen for wind on the mic, room echo, hum from the lights or a charger, and clipping on loud moments. Each has a different fix. The <a href="/tunedzy/how-to-remove-wind-noise-from-audio">wind guide</a> and the <a href="/tunedzy/remove-hum-from-audio">hum guide</a> cover two of them.</p>
<h2>Clean and check</h2>
<p>Clean the sound gently, then listen to the whole clip, not only the speech. A cleanup that sounds good on talking can make music sound thin.</p>
<h2>Put it back</h2>
<p>Replace the sound in the video with the cleaned version. Check the start, the end and any cut. The <a href="/tunedzy/put-clean-audio-back-into-a-video">replace audio guide</a> has the steps.</p>
''',
    vf_title='Clean the video sound, keep the picture',
    vf='<p>Tunedzy replaces the sound of an MP4 or MOV with a cleaned version and copies the picture as it is.</p>',
    faq=[('Will my video get worse?', 'No. The picture is copied, not re-encoded. Only the sound changes.'),
         ('Can I clean the sound from a phone video on my phone?', 'Tunedzy Go cleans a recording or audio file on your phone. Replacing the sound in a video is a Windows app step for now.'),
         ('What if the video has no sound?', 'There is nothing to clean. Record a voice separately and add it to the video.')],
    related=['put-clean-audio-back-into-a-video', 'how-to-remove-wind-noise-from-audio', 'record-a-voiceover-on-your-phone'])
