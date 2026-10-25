"""Blog posts, batch 6 of 10: video sound cluster. Merged into content_blog.py.
Each post answers one search first, then explains it in plain steps, admits its limits, and links to a tool or guide.
No invented statistics, reviews, prices or benchmarks."""

CLUSTERS = {
    'video': dict(tool='vocal-checker', label='Video sound', tool_name='Vocal Checker'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='how-to-fix-echo-in-a-talking-head-video', cluster='video', kw='fix echo in talking head video',
    title='How to Fix Echo in a Talking-Head Video',
    desc='Fix echo in a talking-head video: why rooms make video sound hollow, how to set up the space and the mic, and what cleanup can and cannot do.',
    h1='How to Fix Echo in a Talking-Head Video',
    answer='Echo in a talking-head video comes from the room. Move the microphone closer, add soft surfaces behind and beside you, and record in a space with rugs and fabrics. Cleanup can reduce a little echo afterwards, but it cannot make a bare room sound close.',
    body='''
<p>A talking-head video with echo sounds like the speaker is standing in an empty hall. It is one of the most common problems in home video, and it makes viewers trust the sound less than the picture. The fix starts with the room, because no filter can fully remove the reflections that a hard room creates.</p>
<h2>Choose a softer room</h2>
<p>Pick the room with the most soft surfaces: carpet, curtains, sofas, cushions and bookshelves full of books. Bare walls, glass and tiled floors reflect sound. Test the room by clapping once and listening for a ringing tail. The <a href="/tunedzy/how-to-test-your-room-for-echo">clap test guide</a> shows what to listen for.</p>
<h2>Place the microphone close</h2>
<p>Put the microphone as close to the speaker as the frame allows, usually a few tens of centimetres from the mouth, pointing toward the mouth and slightly off-axis. A closer microphone picks up more of the voice and less of the room. A clip-on microphone on the chest is often the simplest way to get a close, dry sound.</p>
<h2>Soften the space behind the speaker</h2>
<p>The sound that comes back from the wall behind the speaker is the main source of echo in many videos. Hang a blanket, put a cushion or a rug in the background, or move the chair away from the wall. A soft backdrop helps both the sound and the picture.</p>
<h2>Clean up what is left</h2>
<p>After recording, reduce background noise gently, and avoid heavy processing that makes the voice watery. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise, rumble and level problems in a recording, which helps you decide what to fix.</p>
<h2>Check on a laptop and a phone</h2>
<p>Play the finished video on a laptop speaker and on a phone, since many viewers use them. If the voice still sounds distant, record again in a softer space, rather than adding more processing.</p>
<h2>Limits</h2>
<p>A very bright room or a large empty space will always sound echoey. Cleanup helps a little. The most useful change is usually a closer microphone and a few soft objects around the speaker.</p>
''',
    faq=[('Can I remove echo completely in editing?', 'Rarely. Editing can reduce some echo, but the best result comes from a softer room and a closer microphone.'),
         ('Does a better camera fix echo?', 'No. Echo is a room and microphone problem, not a camera problem.'),
         ('Where should I put the microphone?', 'As close to the speaker as the frame allows, pointing at the mouth, and slightly off-axis to reduce breath.'),
         ('Is a blanket behind me enough?', 'Often it helps a lot. Add a rug or cushions if the room is still bright.')])

add(slug='how-to-sync-audio-and-video-in-an-editor', cluster='video', kw='how to sync audio and video',
    title='How to Sync Audio and Video in an Editor',
    desc='Sync audio and video in an editor: use a clap or a visual cue, line up the waveform and picture, check the start and end, and avoid drift over long clips.',
    h1='How to Sync Audio and Video in an Editor',
    answer='Sync audio and video by lining up a sharp sound, such as a clap, with the moment the picture shows it. Zoom in on both the waveform and the frame, move the audio until they match, then check the start, middle and end of the clip.',
    body='''
<p>Sync problems are easy to fix when the clip is short, and frustrating when it is long. The key is to create a clear reference point at the start of each recording, then line up the picture and sound against it. Most editors handle this well once you know the steps.</p>
<h2>Create a sync point when you record</h2>
<p>At the start of each recording, clap your hands once in front of the camera, or tap the microphone sharply. The clap gives a sharp sound and a clear visual moment. If you are recording with a separate audio device, do this at the start and, for long takes, at the end too.</p>
<h2>Line up the clap</h2>
<ol>
<li>Zoom in on the waveform until the clap is a clear spike.</li>
<li>Find the frame where the hands first meet in the picture.</li>
<li>Move the audio track so the spike and the frame line up.</li>
<li>Play the start of the clip to check the match.</li>
</ol>
<h2>Check the middle and the end</h2>
<p>A clip can match at the start and drift later, especially if the audio and video were recorded on different devices with slightly different clocks. Check a point in the middle and near the end. If the sound lags more and more, the clocks differ, and you may need to stretch the audio slightly or re-record with a shared clock.</p>
<h2>Use the timeline markers</h2>
<p>Put a marker on the sync point and on any key moment, such as a word that must match a cut. Markers help you check and fix sync after changes, and they make it easier to find the right place again.</p>
<h2>Avoid drift on long clips</h2>
<p>Long takes are more likely to drift. Record in shorter sections where you can, and sync each section separately. Use a single, consistent frame rate for the project, because a mismatch can make a long clip drift.</p>
<h2>Limits</h2>
<p>If the audio was never recorded with a sync point, lining it up by ear is slow and imprecise. Use a clap or a clear sound at the start of every future recording, and keep the sound and picture recording together where possible.</p>
''',
    faq=[('What is the easiest sync point?', 'A sharp clap at the start, lined up with the moment the hands meet on screen.'),
         ('Why does my audio drift later in the clip?', 'The audio and video clocks differ. Check the middle and end, and re-sync or re-record in shorter sections.'),
         ('Should I use a clap or a tap?', 'Either works. A clap gives a clear visual moment as well as a sharp sound.'),
         ('Can I sync automatically?', 'Some editors can, but check the result by listening, because automatic sync can miss a drift.')])

add(slug='how-to-mix-music-under-talking-in-a-video', cluster='video', kw='music under talking in video',
    title='How to Mix Music Under Talking in a Video',
    desc='Mix music under talking in a video: lowering the music so speech stays clear, using ducking, choosing the right track and checking the balance on a phone.',
    h1='How to Mix Music Under Talking in a Video',
    answer='Lower the music so it sits well below the speech, and duck it further when someone talks. Choose music with a steady rhythm and little vocal, keep the level consistent, and check the balance on a phone speaker, since that is where talking gets lost.',
    body='''
<p>Background music can make a video feel warm and finished, but it often hides the speech. The aim is music that supports the talking without competing with it. A good balance is noticed only when it is wrong, so the goal is to make the words easy to follow at all times.</p>
<h2>Choose the right track</h2>
<p>Pick music with a steady rhythm and little or no singing, since lyrics compete with the voice. Choose a track that matches the mood of the video, and check the licence before you publish, as covered in the <a href="/tunedzy/blog/podcast-intro-music-rules-and-safe-choices">intro music post</a>. Quiet, simple tracks are often easier to mix than busy ones.</p>
<h2>Set the level under the speech</h2>
<p>Start with the music well below the voice, then raise it only until you can hear it clearly during pauses. A common mistake is leaving the music too loud because it sounds good on its own. Listen to the whole video with the music, not just the music on its own.</p>
<h2>Duck the music when someone speaks</h2>
<p>Ducking lowers the music automatically while speech is present, and brings it back in the gaps. Use a smooth release, so the change is gentle rather than sudden. The <a href="/tunedzy/how-to-duck-music-under-a-voiceover">ducking guide</a> explains the method step by step.</p>
<h2>Keep the balance steady</h2>
<p>Check the music level at the start, the middle and the end of the video. A track that suddenly rises in a quiet section can distract. Use a fade at the start and end, so the music does not begin or stop abruptly.</p>
<h2>Check on a phone</h2>
<p>Play the final video on a phone speaker and in a noisy place if you can. Speech that is clear on headphones may vanish on a small speaker. If you cannot hear the words easily, lower the music again.</p>
<h2>Limits</h2>
<p>Music can help a video, but it cannot rescue poor speech. If the voice is hard to hear even with the music low, fix the voice recording first, then return to the music balance.</p>
''',
    faq=[('How loud should the music be under talking?', 'Well below the speech. Raise it only enough to hear it clearly during pauses.'),
         ('Should I use music with lyrics?', 'Usually not under speech, because the lyrics compete with the voice.'),
         ('What is ducking?', 'Automatically lowering the music while someone speaks, then bringing it back in the gaps.'),
         ('Can I use any music in my video?', 'Only music you have the right to use. Check the licence before you publish.')])

add(slug='best-microphone-for-talking-head-videos-explained', cluster='video', kw='best mic for talking head video',
    title='What to Look for in a Microphone for Talking-Head Videos',
    desc='What to look for in a microphone for talking-head videos: a close, steady position, clip-on or shotgun options, the connection and how to test before you film.',
    h1='What to Look for in a Microphone for Talking-Head Videos',
    answer='For talking-head video, look for a microphone that can sit close and steady: a clip-on for the chest, or a small desk or boom microphone for a fixed seat. Check the connection your camera or phone needs, then test the setup before filming, rather than buying by the top of a list.',
    body='''
<p>Many people buy a microphone for a talking-head video and then find the sound is still poor. The reason is usually position and room, not the microphone itself. A modest microphone placed well will always beat an expensive one held far away. Start with the way you will film, then choose the microphone that fits.</p>
<h2>Decide how you will sit and move</h2>
<p>If you sit in one place, a desk or boom microphone close to the mouth gives a steady sound. If you move, stand or walk, a clip-on microphone on the chest keeps the distance constant. Choose the option that matches how you film, not the one that looks most professional.</p>
<h2>Check the connection</h2>
<p>Look at what your camera or phone accepts. Some clip-on microphones use a wired plug or a wireless link, and some need an adapter. A microphone that does not connect properly is no use, so check the connector before you buy.</p>
<h2>Consider the pattern</h2>
<p>For a close speaker, a cardioid or similar pattern helps to reject sound from behind and from the sides. A shotgun microphone can help when it is aimed at the speaker from a short distance, but it needs careful placement and is less forgiving in a busy room.</p>
<h2>Test before you film</h2>
<p>Record a short test in the actual room, with the camera and the lighting you will use. Play it back on headphones and on a phone. Check for echo, background noise, rustle and the level. A test takes ten minutes and reveals most problems.</p>
<h2>Protect the sound</h2>
<p>Use a windscreen or pop filter if needed, keep the cable tidy, and make sure clothing does not rub the microphone. Soft furnishings behind you help more than most upgrades. The <a href="/tunedzy/how-to-test-your-room-for-echo">clap test</a> helps you choose the spot.</p>
<h2>Limits</h2>
<p>No single microphone suits every room and every speaker. Test the setup you have, and upgrade only when the test shows a clear gap. The best choice is the one that sounds clear in your own room.</p>
''',
    faq=[('Is a clip-on or a desk microphone better?', 'A clip-on suits moving speakers, and a desk or boom microphone suits a fixed seat.'),
         ('Do I need a shotgun microphone?', 'Not usually. A close, steady microphone often sounds better in a home room.'),
         ('What should I test before filming?', 'Echo, background noise, rustle and level, on headphones and a phone.'),
         ('Does the camera microphone work?', 'It can, but it is usually far from the speaker. A closer microphone almost always sounds better.')])

add(slug='why-is-my-video-audio-out-of-sync-after-export', cluster='video', kw='audio out of sync after export',
    title='Why Is My Video Audio Out of Sync After Export?',
    desc='Why video audio is out of sync after export: frame rate mismatches, variable frame rate, editing settings and how to fix the sync and prevent it next time.',
    h1='Why Is My Video Audio Out of Sync After Export?',
    answer='Audio drifts out of sync after export usually because of a mismatch in frame rate, variable frame rate footage, or a sample-rate conversion in the export settings. Check the project and export frame rates match the source, convert variable footage to constant frame rate, then export a short test.',
    body='''
<p>A video that looks perfect in the editor but drifts after export is one of the most frustrating problems in video work. The sound and picture were correct on the timeline, so the cause is usually a setting that changed during export. The fix is a few checks, and a short test before the full export.</p>
<h2>Check the frame rate</h2>
<p>If the project frame rate does not match the source footage, the editor may stretch or drop frames. The audio stays at its length, so the picture and sound drift apart over time. Match the project frame rate to the footage, and check the export uses the same rate.</p>
<h2>Watch for variable frame rate</h2>
<p>Some phones and cameras record variable frame rate video, which changes speed during the clip. Editors can struggle with it, and the sync can drift. Convert the footage to a constant frame rate before editing, using a transcoder or a re-export.</p>
<h2>Check the sample rate</h2>
<p>If the audio was recorded at one sample rate and exported at another, the editor converts it. A correct conversion does not cause drift, but a faulty one can. Keep the project and export sample rates the same as the recording, where possible.</p>
<h2>Export a short test</h2>
<p>Export a thirty-second section that includes a clap or a clear sound, then check the sync in the exported file, not in the editor. A short test saves time and shows the problem before you export the full video.</p>
<h2>Fix it and prevent it</h2>
<p>If the export has drifted, re-export with corrected settings rather than trying to stretch the audio by hand, which can leave the speech sounding odd. For future projects, record a sync point, keep the frame rate constant, and check a short export before the final one.</p>
<h2>Limits</h2>
<p>Drift can have several causes, and some are in the source footage. If the drift remains after the settings are correct, check the original file, and consider re-recording the affected section.</p>
''',
    faq=[('What is variable frame rate?', 'Footage where the frame rate changes during the clip. Editors can struggle with it, so convert it to constant frame rate.'),
         ('Why is the sync fine at the start and off at the end?', 'A frame rate or clock mismatch is accumulating. Check the frame rate and the source footage.'),
         ('Should I stretch the audio to fix it?', 'Only as a last resort. Re-exporting with correct settings is cleaner.'),
         ('How do I check the export quickly?', 'Export a short section with a clap or sharp sound, then check the sync in the exported file.')])

add(slug='audio-for-short-videos-what-matters-most', cluster='video', kw='audio for short videos',
    title='Audio for Short Videos: What Matters Most',
    desc='Audio for short videos: what matters most for social clips, how to keep speech clear in the first seconds, music and levels, and what to check on a phone.',
    h1='Audio for Short Videos: What Matters Most',
    answer='For short videos, the first few seconds of speech matter most. Keep the voice clear and close, set the music well below it, keep the level steady, and check the result on a phone speaker, since most viewers listen that way.',
    body='''
<p>A short video is often watched with the sound on, on a small speaker, in a busy place. The audio has to work quickly. If the first words are hard to hear, viewers scroll on, however strong the picture. Good short-form audio is simple, clear and consistent.</p>
<h2>Make the first seconds clear</h2>
<p>Viewers decide in the first few seconds. Start with the clearest speech you have, and keep any background music low at the start. A clean, close voice at the opening is more important than any effect.</p>
<h2>Keep the voice close and dry</h2>
<p>A close microphone and a soft room keep the voice clear on a small speaker. Echo and distance make speech hard to follow, and a short clip has no time to recover. Record close, and use a clip-on microphone if you move.</p>
<h2>Balance the music</h2>
<p>Music helps a short video feel polished, but it should sit under the voice. Choose a steady track with little vocal, and duck it under speech, as covered in the <a href="/tunedzy/blog/how-to-mix-music-under-talking-in-a-video">music under talking post</a>. Trending sounds are a licensing question, so check the terms of the platform and the track.</p>
<h2>Keep the level steady</h2>
<p>Short clips jump between shots and sound sources, which makes levels feel uneven. Match the speech level across clips, and avoid making the clip so loud that the peaks clip on a phone. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can show the loudness of the finished file.</p>
<h2>Check on a phone</h2>
<p>Play the clip on a phone speaker, with the volume at a normal level. Ask yourself whether the words are clear without headphones. If not, lower the music, bring the voice forward, or re-record the opening line.</p>
<h2>Limits</h2>
<p>Platforms change their playback and their features, so check the current guidance from the platform you use. The steps above stay useful, even when the features move.</p>
''',
    faq=[('What matters most in a short video?', 'Clear speech in the first few seconds, with music kept under it.'),
         ('Should I always use music?', 'Not always. Some clips work better with clear speech and no music.'),
         ('How do I check it quickly?', 'Play the clip on a phone speaker at a normal volume and see whether the words are easy to follow.'),
         ('Does the platform change the audio?', 'Platforms may adjust playback levels or re-encode the file. Check the result on the platform after you upload.')])

add(slug='how-to-record-narration-for-a-screen-recording', cluster='video', kw='record narration for screen recording',
    title='How to Record Narration for a Screen Recording',
    desc='Record narration for a screen recording: prepare the script, set up a quiet microphone, record in sections and sync the voice to the on-screen actions.',
    h1='How to Record Narration for a Screen Recording',
    answer='Write a short script that matches the steps on screen, record the narration in a quiet room with the microphone close, and record each section separately. Sync the voice to the actions after recording, and leave a little pause before each new step so the viewer can follow.',
    body='''
<p>A screen recording with clear narration is easy to follow, and it saves viewers from guessing what you clicked. The narration does most of the teaching, so it needs to be clear and steady. Planning the steps and recording in sections make the job much easier.</p>
<h2>Write the steps first</h2>
<p>Make a list of the actions on screen, then write one or two short sentences for each. Keep the sentences plain, and say what the viewer will see before they see it. A written list also helps you time the narration against the screen.</p>
<h2>Record in a quiet room</h2>
<p>Choose a soft room with no fans or traffic. Place the microphone close, with a pop filter, and keep the distance steady. Turn off notifications on the computer, because a chime can ruin a take. The <a href="/tunedzy/blog/how-to-record-voice-over-for-youtube-videos">YouTube voice-over post</a> covers the same setup in more detail.</p>
<h2>Record in sections</h2>
<p>Record each step as a separate take, with a short pause between. If you make a mistake, re-record only that step. Sections also make the edit faster, because you can place each one next to the screen action it describes.</p>
<h2>Sync the voice to the screen</h2>
<p>Place each narration clip beside the action it describes. Leave a short pause before a new click or a new screen, so the viewer has time to look. If the narration is faster than the action, slow the action down or add a pause before the next step.</p>
<h2>Check the sound on a phone</h2>
<p>Many viewers listen on a phone or a laptop speaker. Play the finished recording on one, and check that the narration is clear and the music, if any, is under the voice. Fix any steps that are hard to hear before you publish.</p>
<h2>Limits</h2>
<p>A narration cannot replace clear on-screen text for complex steps. Use both, and keep the narration short enough that the viewer is not overloaded.</p>
''',
    faq=[('Should I write a full script?', 'A list of steps with a sentence each usually works better than a long script.'),
         ('How do I avoid the narration sounding rushed?', 'Leave short pauses before each new step, and speak to one viewer.'),
         ('What if I make a mistake mid-step?', 'Re-record that step only, then place the new take beside the action.'),
         ('Do I need a special microphone?', 'Not necessarily. A close microphone in a quiet room is more important than the model.')])

add(slug='how-to-remove-traffic-noise-from-a-video', cluster='video', kw='remove traffic noise from video',
    title='How to Remove Traffic Noise From a Video Recording',
    desc='Remove traffic noise from a video recording: why road noise is hard to remove, how to move, time and place the mic, and how to clean what remains gently.',
    h1='How to Remove Traffic Noise From a Video Recording',
    answer='Traffic noise is a low rumble with bursts of horns and engines, and it is hard to remove once it covers the voice. Move indoors or away from the road, record at a quieter time, and place the microphone close to the speaker. Clean what remains gently, and re-record the sections the noise has covered.',
    body='''
<p>Traffic is one of the most common reasons a good video sounds poor. The rumble of cars is low and steady, and the bursts of horns and engines are sharp. Both overlap the voice, so cleaning them afterwards can make the speech sound thin. The best approach is to avoid the noise at the source.</p>
<h2>Move away from the road</h2>
<p>Record in a room on the far side of the building, away from the road. Close the windows and doors, and turn off fans or air conditioning. Even a short distance from a busy road can make a large difference, especially for the low rumble.</p>
<h2>Choose the time</h2>
<p>Record early in the morning, late at night or on a quiet day, when traffic is lighter. A few minutes of quiet beats hours of cleanup. Plan the shoot around the time when the road is calmest.</p>
<h2>Place the microphone close</h2>
<p>A close microphone captures more of the voice and less of the road. Use a clip-on for the chest, or a desk microphone close to the mouth. Keep the distance steady, so the voice does not drop under the noise when you move.</p>
<h2>Clean what remains gently</h2>
<p>A high-pass filter can reduce low rumble without changing the voice much, if the cutoff is set carefully. Use noise reduction lightly, and listen for the watery sound that heavy cleanup causes. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from an existing recording.</p>
<h2>Re-record where the noise covers the voice</h2>
<p>If a horn or engine covers a word, no filter can restore it. Re-record that line, rather than repairing it. A short clean take is better than a long repaired one.</p>
<h2>Limits</h2>
<p>Traffic noise in a city is hard to remove completely. Plan the location and the time, and treat cleanup as a way to tidy the recording, not a rescue.</p>
''',
    faq=[('Can a filter remove all traffic noise?', 'Rarely. It reduces the rumble, but bursts of horns can cover the voice.'),
         ('Is a windscreen useful against traffic?', 'It helps with wind, not with the sound of traffic. Distance and timing help more.'),
         ('What time is quietest for outdoor shoots?', 'Early morning, late at night or on a quiet day. Test the location first.'),
         ('Should I use noise reduction on the whole video?', 'Use it lightly, and only on sections that need it, to avoid a watery sound.')])

add(slug='how-to-keep-audio-levels-consistent-across-video-clips', cluster='video', kw='consistent audio across video clips',
    title='How to Keep Audio Levels Consistent Across Video Clips',
    desc='Keep audio levels consistent across video clips: matching speech levels, using gain changes and a loudness target, and checking the sequence as a whole.',
    h1='How to Keep Audio Levels Consistent Across Video Clips',
    answer='Match the speech level of each clip to a common target, using gain changes rather than heavy processing. Check the sequence as a whole, not one clip at a time, and listen for jumps at each cut. A loudness target for the final export keeps the whole video consistent.',
    body='''
<p>A video made of several clips can sound patchy, with some shots quiet and others loud. Viewers notice these jumps and reach for the volume control. The fix is to bring every clip to a similar level before you export, so the sequence sounds like one recording.</p>
<h2>Set a target before you start</h2>
<p>Choose a level for speech, such as a comfortable loudness that works on a phone and a laptop. Use it as the reference for every clip. Writing the target down helps you return to it across a long project.</p>
<h2>Match each clip by ear</h2>
<p>Play each clip in turn, and adjust its gain until the speech sits at the target. Use small changes, and listen to the whole clip, not only the loudest word. Check the quietest clips first, since they are the ones most likely to be missed.</p>
<h2>Check the cuts</h2>
<p>Play the sequence through, paying attention to each cut. A jump in level or room sound at a cut is more noticeable than a small difference across a clip. If the room tone changes, a short crossfade can smooth the join, as covered in the <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade guide</a>.</p>
<h2>Set a loudness target for the export</h2>
<p>Once the clips match, measure the loudness of the whole export, and compare it with your target. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains common targets for online video. Adjust the whole mix, not each clip again.</p>
<h2>Limits</h2>
<p>Clips recorded in very different places will never match perfectly. Try to record the main clips in the same room and at the same distance. Consistency is easier to achieve at the start of a shoot than at the end.</p>
''',
    faq=[('Should I use a compressor on every clip?', 'Use it lightly, if at all. Gain changes usually keep the voice more natural.'),
         ('Why does one clip sound louder at the cut?', 'Its level or room sound differs. Match the level, then check the join.'),
         ('Should I normalise each clip to the same peak?', 'Peak matching is not enough. Match the speech level by ear and check the loudness of the whole export.'),
         ('What is the easiest fix for a patchy video?', 'Match each clip by ear to the same speech level, then check the cuts.')])

add(slug='why-does-my-video-sound-muffled', cluster='video', kw='why does my video sound muffled',
    title='Why Does My Video Sound Muffled and How to Fix It',
    desc='Why a video sounds muffled: a covered or distant microphone, a soft room, heavy processing or a lowpass setting, and how to fix each one.',
    h1='Why Does My Video Sound Muffled and How to Fix It',
    answer='A video sounds muffled when the high frequencies are lost, usually because the microphone is covered or far away, the room absorbs too much, or heavy processing removes the top end. Check the microphone, move closer, and look at the processing before you blame the room.',
    body='''
<p>Muffled sound is different from echo or noise. The voice sounds dull, as if it is coming through a blanket. The words are harder to follow, and the video feels less professional. Muffled audio has a few common causes, and the fix depends on which one you have.</p>
<h2>Check the microphone</h2>
<p>A microphone covered by a hand, a case, a cloth or a scarf loses the high frequencies. A microphone pointed away from the speaker does too. Make sure the microphone is uncovered and aimed at the mouth, then record a short test.</p>
<h2>Move closer</h2>
<p>A microphone far from the speaker picks up more of the room and less of the bright, clear sound of the voice. Move closer, and keep the distance steady. A close microphone usually fixes a muffled sound more than any setting.</p>
<h2>Look at the room</h2>
<p>A very soft room with heavy fabrics can absorb the high frequencies, and the voice can sound dull. Keep some natural brightness in the room, and avoid stacking soft materials right against the microphone.</p>
<h2>Check the processing</h2>
<p>A low-pass filter, heavy noise reduction or an aggressive enhancement setting can remove the top end of the voice. If the muffled sound appeared after processing, undo the step and compare. A light touch keeps the voice clear.</p>
<h2>Restore clarity carefully</h2>
<p>If the voice is only a little dull, a gentle high-shelf boost can restore some clarity. Boost in small steps, and listen for harshness. The <a href="/tunedzy/blog/how-to-make-a-harsh-voice-recording-sound-warmer">harsh voice post</a> covers the opposite problem and the balance between the two.</p>
<h2>Limits</h2>
<p>If the voice was recorded far away or behind a barrier, the clarity is gone, and no boost will bring it back. Re-record in a closer position, and treat the fix as a short-term improvement.</p>
''',
    faq=[('Is a muffled video always a microphone problem?', 'Often it is distance, covering or processing. Check those before blaming the room.'),
         ('Can I boost the top end to fix it?', 'A little, in small steps. Too much boost makes the voice harsh.'),
         ('Does the camera microphone cause muffled sound?', 'It can, when it is far away. A close microphone usually helps most.'),
         ('Should I turn off noise reduction?', 'Test it. If the sound got duller after processing, reduce or remove the step.')])
