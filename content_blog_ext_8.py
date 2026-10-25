"""Blog posts, batch 8 of 10: recording workflow cluster. Merged into content_blog.py.
Each post answers one search first, then explains it in plain steps, admits its limits, and links to a tool or guide.
No invented statistics, reviews, prices or benchmarks."""

CLUSTERS = {
    'workflow': dict(tool='vocal-checker', label='Recording workflow', tool_name='Vocal Checker'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='how-to-name-audio-files-for-a-project', cluster='workflow', kw='how to name audio files',
    title='How to Name Audio Files So You Can Find Them Later',
    desc='How to name audio files so you can find them later: a simple pattern with date, project, take and version, and the mistakes that make files impossible to search.',
    h1='How to Name Audio Files So You Can Find Them Later',
    answer='Use one consistent pattern for every file, such as date, project, what it is, take number and version. Put the most important part first, avoid spaces and symbols, and keep the same order across the whole project.',
    body='''
<p>A folder of files called final, final2 and new-mix-v3 is a common sign of a project that will be hard to finish. Good names cost a few seconds each time you save, and they save hours when you come back to a project later or hand it to someone else. The rules are simple, and the discipline is what matters.</p>
<h2>Choose one pattern and keep it</h2>
<p>Decide on a pattern once, and write it down. A useful one is date, project, content, take, version, for example 2026-10-25_episode12_intro_take03_v2. Use the same order in every file, so you can scan a list and read the story of the project at a glance.</p>
<h2>Put the date first</h2>
<p>Starting with the date in year-month-day form keeps files in order when sorted by name. It also tells you at once which file is newest, without opening it.</p>
<h2>Keep names short and clean</h2>
<ul>
<li>Use letters, numbers, dashes and underscores.</li>
<li>Avoid spaces, which can break some tools and scripts.</li>
<li>Avoid symbols such as slashes, question marks and brackets.</li>
<li>Keep names under about fifty characters, so they show in full.</li>
</ul>
<h2>Number the takes and versions</h2>
<p>Use take numbers for raw recordings, and version numbers for edits, such as v1, v2 and v3. Never overwrite a version. Save a new file, so you can go back if a change is worse. The <a href="/tunedzy/blog/how-to-version-audio-projects">project versions post</a> covers how to keep the history tidy.</p>
<h2>Use the same names across tools</h2>
<p>Name the raw files, the project file and the export with the same base name, so you can match them at a glance. An export called episode12_final should come from a project called episode12, not from a file called mix_new.</p>
<h2>Limits</h2>
<p>A naming pattern only works if you use it every time. Set up a template for new projects, and check the names before you archive. A small amount of consistency beats a perfect scheme you rarely follow.</p>
''',
    faq=[('Why put the date first?', 'It sorts files in order by name and shows the newest one without opening it.'),
         ('Should I use spaces in file names?', 'Better not. Underscores or dashes work better with most tools and scripts.'),
         ('What about files I have already named badly?', 'Rename the active ones in a batch, and keep a note of the old names for anything archived.'),
         ('Does the naming matter for a small project?', 'Yes. Small projects grow, and good names make the change easy to manage.')])

add(slug='how-to-back-up-audio-recordings', cluster='workflow', kw='how to back up audio recordings',
    title='How to Back Up Audio Recordings Properly',
    desc='How to back up audio recordings properly: the 3-2-1 idea, what to copy and when, how to check a backup works and how to protect files from loss.',
    h1='How to Back Up Audio Recordings Properly',
    answer='Keep at least three copies of every important recording, on two different kinds of storage, with one copy somewhere else. Back up the raw files as soon as you record them, and check that a backup opens before you rely on it.',
    body='''
<p>An audio recording exists only as long as its files do. A failed drive, a deleted folder or a corrupted file can take a whole episode or a finished song with it. Backups are dull until the day you need one, and then they are the most important thing you own. A simple routine protects almost every project.</p>
<h2>Use the 3-2-1 idea</h2>
<p>Keep three copies of important files: the original, one backup on a second device, and one copy in a different place, such as an external drive stored away from your computer or an online service you trust. Two kinds of storage protects against a single type of failure.</p>
<h2>Back up the raw files first</h2>
<p>Copy the raw recordings as soon as you finish a session, before any editing. The raw files are the ones you cannot replace. Edits can be redone, but a lost recording of an interview or a performance cannot. Keep the raw files in a separate folder that you do not change.</p>
<h2>Back up the project as well</h2>
<p>A project file on its own is not enough, and raw files without the project may be hard to rebuild. Save the project file and any settings with the raw files, so you can re-open the work in the same state.</p>
<h2>Check that a backup works</h2>
<p>Every few months, open a backup file, play it, and check the length. A backup you have never opened may be corrupted. Write a short note of the date and what you checked, so the routine stays on track.</p>
<h2>Plan for the cloud carefully</h2>
<p>Online storage is useful for a copy off-site, but check where the files are stored, who can access them and how long they are kept. For unpublished interviews or client work, check that the terms suit your agreements. This is general guidance, not legal advice.</p>
<h2>Limits</h2>
<p>A backup routine protects you only if you keep it. Set a reminder after each session, and treat backups as part of the recording, not a task for later.</p>
''',
    faq=[('How many copies do I need?', 'At least three of anything important: the original and two backups, on different kinds of storage.'),
         ('What should I back up first?', 'The raw recordings, since they cannot be recreated.'),
         ('Is one external drive enough?', 'Not on its own. Add a second copy in a different place.'),
         ('How often should I check my backups?', 'Every few months, by opening a file and playing it.')])

add(slug='recording-checklist-for-audio-sessions', cluster='workflow', kw='recording checklist for audio',
    title='A Recording Checklist for Audio Sessions',
    desc='A recording checklist for audio sessions: what to check before, during and after a recording, so you catch problems early and finish each session with usable files.',
    h1='A Recording Checklist for Audio Sessions',
    answer='Use a short checklist before, during and after each session: check the room, the microphone, the levels and the storage before you start; monitor the first minute during the session; and back up and name the files as soon as you finish. A checklist catches the problems that are easy to miss.',
    body='''
<p>Most recording problems are predictable. The microphone was moved, the battery was low, the room was not quiet, or the file did not save. A short checklist prevents them, and it makes every session feel less stressful. The best checklist is short enough to use every time.</p>
<h2>Before you start</h2>
<ul>
<li>Check the room: fans, traffic, notifications and doors.</li>
<li>Check the microphone position and the cable.</li>
<li>Record a short test and listen on headphones.</li>
<li>Check the level, with peaks well below the top.</li>
<li>Check the battery, the storage and the backup device.</li>
</ul>
<h2>During the session</h2>
<ul>
<li>Listen to the first minute, then check again after a short break.</li>
<li>Note the take numbers and any problems, with the time.</li>
<li>Keep the distance and the seat the same.</li>
<li>Check that the file is still saving every so often.</li>
</ul>
<h2>After the session</h2>
<ul>
<li>Stop the recording properly, and check that the file saved.</li>
<li>Name the files using your pattern.</li>
<li>Copy the raw files to a backup, as covered in the <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup post</a>.</li>
<li>Write a short note of what worked and what to change next time.</li>
</ul>
<h2>Make it your own</h2>
<p>Print the checklist, or keep it on your phone, and tick each item as you go. Adjust it for your setup. A podcast host, a voice-over artist and a musician will each need different items, but the pattern stays the same.</p>
<h2>Limits</h2>
<p>A checklist cannot catch everything. Some problems only show on playback, and a fresh pair of ears helps. Use the checklist to remove the obvious mistakes, then listen carefully to the finished files.</p>
''',
    faq=[('How long should the checklist be?', 'Short enough to use every time. Ten to fifteen items is usually plenty.'),
         ('Should I check the level during a long session?', 'Yes, with a glance at the meter and a short listen after each break.'),
         ('What is the most common mistake?', 'Forgetting to check that the file is saving, or moving the microphone during a take.'),
         ('Do I need a checklist for a short voice note?', 'Less of one. Check the room and the level, and back up the file.')])

add(slug='when-to-stop-editing-an-audio-file', cluster='workflow', kw='when to stop editing audio',
    title='When to Stop Editing an Audio File',
    desc='When to stop editing an audio file: the signs that a project is finished, how to avoid endless tweaking, and a simple way to decide and export.',
    h1='When to Stop Editing an Audio File',
    answer='Stop editing when the file sounds clear, balanced and consistent on the devices your listeners use, and when further changes are small enough that a listener would not notice. Set a time limit and a final check, then export, and move on to the next project.',
    body='''
<p>Editing can go on forever. Every listen reveals something to change, and small tweaks start to feel like progress. The skill is recognising when the file is good enough for its purpose, then stopping before the work starts to make it worse. Most audio is damaged by overediting.</p>
<h2>Know what finished means</h2>
<p>Decide what the file needs to do before you start. A podcast needs clear speech and a steady level. A song needs balance and impact. When the file does those things, it is finished, even if you can think of small improvements.</p>
<h2>Set a time limit</h2>
<p>Give the edit a fixed time, such as two hours for an episode, and stop when it runs out. A time limit forces decisions. It also prevents a single tiny problem from taking the whole day.</p>
<h2>Do a final check</h2>
<ol>
<li>Play the file from start to end on headphones.</li>
<li>Play it on a phone speaker, at a normal volume.</li>
<li>Check the loudness and the true peak of the export, as covered in the <a href="/tunedzy/blog/what-is-true-peak-in-audio-and-why-it-matters">true peak post</a> if you need it.</li>
<li>Note only the problems that a listener would notice.</li>
</ol>
<h2>Fix the big things, leave the small ones</h2>
<p>If a problem is audible to a typical listener, fix it. If it is only audible when you listen very closely, leave it. A listener cannot hear the difference between two very similar edits, and the time is better spent on the next project.</p>
<h2>Limits</h2>
<p>Some files deserve more time, such as a final mix for a client or an audiobook chapter. Even then, plan the stopping point in advance. The best audio is finished, not perfect, and finished audio gets heard.</p>
''',
    faq=[('How do I know when I am done?', 'When the file sounds clear and balanced on the devices your listeners use, and the changes left are too small to notice.'),
         ('Should I keep editing after I export?', 'Export a version, then make a new one if you find a real problem. Avoid endless small changes.'),
         ('What if I cannot stop listening for flaws?', 'Take a break, then listen again the next day. A fresh ear hears the real problems.'),
         ('How much time should an edit take?', 'It depends on the length and the project. Set a limit before you start.')])

add(slug='how-to-review-your-own-audio-recording', cluster='workflow', kw='how to review your own recording',
    title='How to Review Your Own Audio Recording Honestly',
    desc='How to review your own audio recording honestly: listen as a listener, separate performance from sound, use a checklist and get useful feedback.',
    h1='How to Review Your Own Audio Recording Honestly',
    answer='Listen to the recording as a listener would, on the device they use, without stopping to fix things. Judge the performance and the sound separately, use a short checklist, and wait a day before the final review. Ask one trusted person for feedback on one specific question.',
    body='''
<p>Hearing your own voice is uncomfortable for most people, and it is easy to judge a recording harshly, or to ignore problems because you know what you meant. An honest review needs a method, so that you notice what a listener would hear and learn something useful for the next session.</p>
<h2>Listen as a listener</h2>
<p>Play the whole recording straight through, without stopping. Listen as if you were a stranger who found the episode or the video. Note where your attention drifts, where you feel bored or tired, and where you are drawn in. Those moments show the real problems.</p>
<h2>Separate the performance from the sound</h2>
<p>Judge the performance first: pace, energy, clarity of ideas and emotion. Then judge the sound: noise, level, echo and balance. Mixing the two makes it hard to see what to change. A great performance on a poor sound needs a different fix from a weak performance on a clean sound.</p>
<h2>Use a short checklist</h2>
<ul>
<li>Did the opening hold my attention?</li>
<li>Was the voice clear on a phone speaker?</li>
<li>Were there any distracting noises or clicks?</li>
<li>Did the level stay steady?</li>
<li>Would I listen to the end?</li>
</ul>
<h2>Wait before you judge</h2>
<p>Review the recording the next day if you can. Fresh ears are more honest, and the sharpest criticism often fades. Write down three things that worked and three to improve, then plan the next session around them.</p>
<h2>Get one useful piece of feedback</h2>
<p>Ask a trusted person one specific question, such as &ldquo;was the first minute clear?&rdquo; A broad question like &ldquo;what do you think?&rdquo; often gets politeness. A focused question gets an answer you can use.</p>
<h2>Limits</h2>
<p>Self-review will not catch everything, and it can drift into harsh self-criticism. Keep the focus on what to change next time, and remember that every recording is practice for the next one.</p>
''',
    faq=[('Why does my voice sound bad to me?', 'Most people hear their own voice differently from listeners. Judge the content and the clarity, not only the sound of your voice.'),
         ('How soon should I review a recording?', 'Wait a day if you can, so you hear it with fresher ears.'),
         ('Should I review on headphones or speakers?', 'Both. Headphones show detail, and a phone speaker shows what most listeners hear.'),
         ('Who should I ask for feedback?', 'Someone who will be honest, and who you can ask a focused question.')])

add(slug='how-to-batch-process-audio-files', cluster='workflow', kw='batch process audio files',
    title='How to Batch Process Audio Files Without Losing Control',
    desc='How to batch process audio files without losing control: when batch work helps, how to test settings on one file and review each output.',
    h1='How to Batch Process Audio Files Without Losing Control',
    answer='Batch processing applies the same steps to many files at once, which saves time on repetitive jobs such as export, level and format changes. Test the settings on one file first, run the batch on a copy, and review a sample of the outputs before you publish any of them.',
    body='''
<p>Batch processing is useful when you have many files that need the same change, such as exporting a series of episodes at one loudness, or converting a folder of recordings to one format. It saves hours. The risk is that a wrong setting is applied to every file, and nobody notices until the damage is done. Control is the difference between a timesaver and a mistake.</p>
<h2>Use batch work for the right jobs</h2>
<p>Batch steps suit repetitive, predictable changes: format conversion, a fixed gain change, a standard export. They do not suit creative decisions, such as cutting the best take or matching a voice. Keep the editing manual, and batch the final steps.</p>
<h2>Test on one file first</h2>
<p>Run the settings on a single, typical file, and listen to the output. Check the level, the peaks and the quality. Only when that file is right should you move on to the batch. Testing takes minutes and prevents hours of rework.</p>
<h2>Work on copies</h2>
<p>Run the batch on copies of the files, not the originals. Keep the raw recordings untouched, so you can run the batch again with different settings. This is the same discipline as the <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup routine</a>.</p>
<h2>Review a sample of the outputs</h2>
<p>Do not trust the batch blindly. Listen to the first file, a file from the middle and the last file. Check the loudness of the export with the <a href="/tunedzy/tools/lufs-meter">LUFS meter</a>, and look for clipping or silence where there should be speech.</p>
<h2>Name the outputs clearly</h2>
<p>Use a naming pattern that shows the batch, such as a suffix for the export settings. Clear names make it easy to find the right files and to tell the batches apart later.</p>
<h2>Limits</h2>
<p>Batch processing can hide problems across many files, and some tools behave differently with unusual input. Check the outputs, keep the originals, and be ready to run the job again if a setting turns out to be wrong.</p>
''',
    faq=[('What is batch processing?', 'Applying the same steps to many files at once, such as exporting or converting a folder.'),
         ('Should I batch the editing too?', 'Usually not. Creative editing needs to be done by hand, file by file.'),
         ('How do I know the batch worked?', 'Listen to a sample of outputs and check their loudness, peaks and content.'),
         ('What if I applied the wrong setting?', 'Re-run the batch on the copies, with the correct setting, since you kept the originals.')])

add(slug='how-to-version-audio-projects', cluster='workflow', kw='audio project versions',
    title='How to Version Audio Projects Without Losing Track',
    desc='How to version audio projects without losing track: when to save a new version, how to label versions clearly and how to keep the history without filling your drive.',
    h1='How to Version Audio Projects Without Losing Track',
    answer='Save a new version at each major change, label it with a number and a short note, and never overwrite the previous version. Keep the last few versions and the final export, and archive the rest. Clear versioning lets you go back when a change turns out to be wrong.',
    body='''
<p>Audio projects change a lot, and it is easy to lose a good version when a later change goes wrong. Versioning means saving the project at key points, so you can return to any earlier state. It is one of the simplest habits in audio work and one of the most useful.</p>
<h2>Save at major changes</h2>
<p>Save a new version when you make a significant change: a new edit of the structure, a big level change or a new mix. Do not save a new version for every small tweak, or the history becomes noise. A version should mean something you might want back.</p>
<h2>Label the versions clearly</h2>
<p>Use a number and a short note, such as v3_levelled or v4_music_under. The note tells you what changed without opening the file. Keep the labels consistent across the project, and follow the same pattern as your <a href="/tunedzy/blog/how-to-name-audio-files-for-a-project">file naming</a>.</p>
<h2>Never overwrite a version</h2>
<p>Save a new file rather than replacing the old one. An overwritten version is gone, and you may need it later. If the file is too large to keep many copies, archive the older ones to external storage, rather than deleting them.</p>
<h2>Keep the useful history</h2>
<p>Keep the last few versions in an active folder, the final export and the raw recordings. Archive the rest, and write a short note at the top of the project about what each version did. A clean history helps you finish faster.</p>
<h2>Check the export matches the version</h2>
<p>Before you publish, check that the export came from the version you intended. Use the version label in the export name, so there is no confusion later.</p>
<h2>Limits</h2>
<p>Versioning uses storage space, and very long projects need a plan. Keep the number of active versions small, and archive the rest. The aim is to be able to go back, not to keep every file forever.</p>
''',
    faq=[('How often should I save a version?', 'At major changes, not every small tweak. A version should be something you might want back.'),
         ('Should I keep every version?', 'Keep the recent ones and the final export. Archive older versions to save space.'),
         ('Is saving over the old file ever safe?', 'Rarely. Save a new file, so you can go back if a change is worse.'),
         ('How do I know which version I published?', 'Put the version label in the export name, and note it in the project.')])

add(slug='how-to-share-raw-audio-files-with-a-remote-guest', cluster='workflow', kw='share audio files with remote guest',
    title='How to Share Raw Audio Files With a Remote Guest',
    desc='How to share raw audio files with a remote guest: what to send, how to export a simple copy, a safe transfer and how to confirm it arrived.',
    h1='How to Share Raw Audio Files With a Remote Guest',
    answer='Share a copy of the recording, not the original, and say clearly what it is for. Export a standard format such as WAV or MP3 at the recording quality, use a transfer method you trust, and check with the guest that the file opened correctly before you delete anything.',
    body='''
<p>Sometimes a guest or a collaborator needs a copy of a recording to check it, to clip it for promotion or to add their own edit. Sharing raw audio is simple, but it needs care. You want the file to arrive intact, with a clear purpose, and without exposing more than you intended.</p>
<h2>Decide what you are sharing</h2>
<p>Share the recording the guest needs, not every file in the project. A full project can contain material you never intended to share. Export a copy of the relevant section, and keep the original and the project with you.</p>
<h2>Export a simple copy</h2>
<p>Export a WAV or a high-quality MP3 at the recording quality, and name it clearly. Avoid heavy compression, and do not send a file that has been processed in a way the guest does not expect. Say what the file is, and whether it is a rough or a near-final version.</p>
<h2>Choose a transfer method you trust</h2>
<p>Use a file transfer service or a shared folder that you have checked, rather than an unknown link. Set an expiry date if the service allows it, and remove the copy when the work is finished. Do not send private recordings through public channels.</p>
<h2>Check it arrived</h2>
<p>Ask the guest to confirm that the file opened and sounds right. Wait for that confirmation before you delete anything, and keep your own copy until the project is complete.</p>
<h2>Agree how it will be used</h2>
<p>Make sure the guest knows what the file can be used for, and whether it can be shared further. The <a href="/tunedzy/blog/podcast-guest-consent-what-to-agree-before-recording">guest consent post</a> covers what to agree before recording, including how files are used.</p>
<h2>Limits</h2>
<p>A shared file is outside your control once it leaves. Share only what is needed, and assume the copy may last longer than you expect. This is general guidance, not legal advice.</p>
''',
    faq=[('Should I send the original recording?', 'Usually send a copy, and keep the original yourself.'),
         ('What format should I send?', 'WAV or a high-quality MP3, at the recording quality, with a clear name.'),
         ('How do I make sure it arrived?', 'Ask the guest to confirm it opened and sounded right, then keep your copy until the work is done.'),
         ('Can the guest share the file with others?', 'Only if you agreed. Make the terms clear before you send it.')])

add(slug='how-to-keep-track-of-takes-in-a-recording-session', cluster='workflow', kw='keep track of takes in recording',
    title='How to Keep Track of Takes in a Recording Session',
    desc='How to keep track of takes in a recording session: a simple take log, naming and marking good takes, and how to find the best version quickly during editing.',
    h1='How to Keep Track of Takes in a Recording Session',
    answer='Keep a simple take log with the take number, the time, a line of the script and a short note about how it went. Mark your favourite takes as you record, and name each file with its take number, so you can find the best version quickly during editing.',
    body='''
<p>A session with many takes can turn into a pile of files, and the best take is lost. Without a record, editing becomes a search through every file. A take log takes a few seconds per take, and it makes the edit much faster and less stressful.</p>
<h2>Keep a simple take log</h2>
<p>Write the take number, the time, the line or section, and a short note. A note such as &ldquo;good energy, breath at end&rdquo; is enough to decide later. Use a notebook or a text file next to the recording, and keep it simple.</p>
<h2>Mark the good takes</h2>
<p>When you hear a take that works, mark it in the log, and in the file name if you can. A marker in the file or the recorder is also useful. Do not wait until the end of the session, because the good moments are easy to forget.</p>
<h2>Name each take clearly</h2>
<p>Include the take number and the section in the file name, such as intro_take04. Consistent names let you find any take by a quick search. The <a href="/tunedzy/blog/how-to-name-audio-files-for-a-project">file naming post</a> covers the full pattern.</p>
<h2>Keep the performance notes</h2>
<p>Note the problems too, such as a loud breath, a stumble or a noise outside. These notes help you decide which take to use, and they guide the next take. Write them as you go, while the detail is fresh.</p>
<h2>Use the log in the edit</h2>
<p>When you edit, start with the marked takes. Compare the best two or three against each other, rather than scanning every file. The log turns a long search into a short comparison.</p>
<h2>Limits</h2>
<p>A take log adds a small step to each session, and it is easy to skip when things are going well. Keep it simple enough to use every time, and it will pay off in the edit.</p>
''',
    faq=[('How detailed should the log be?', 'Short. A take number, a time, the section and a one-line note is enough.'),
         ('Should I mark takes on the recorder?', 'If your recorder allows it, yes. A marker helps, but the log is the main record.'),
         ('What if I forget to log a take?', 'Listen to the takes in order during the edit, and note the good ones then.'),
         ('How many takes should I keep?', 'Keep all of them until the edit is finished, then archive the ones you did not use.')])

add(slug='working-with-an-audio-editor-remotely', cluster='workflow', kw='working with an audio editor remotely',
    title='Working With an Audio Editor Remotely: A Practical Guide',
    desc='Working with an audio editor remotely: what to send, how to brief the edit clearly, how to give feedback on timestamps and how to agree on revisions.',
    h1='Working With an Audio Editor Remotely: A Practical Guide',
    answer='Send the raw files, a clear brief and a reference episode, then agree the number of revision rounds before you start. Give feedback with timestamps and one change per note, and keep the project files and notes in one shared place so nothing is lost between rounds.',
    body='''
<p>Remote editing is common for podcasts, voice-overs and video, and it works well when both sides are clear about what is needed. Most problems come from a vague brief, feedback that is hard to act on, or files scattered across several places. A little structure keeps the work moving.</p>
<h2>Send a clear brief</h2>
<p>Write what the episode or piece is for, how long it should be, who the listeners are and what the tone should feel like. Include one reference example that you like, and one that you do not. A short brief saves several rounds of revision.</p>
<h2>Send organised files</h2>
<p>Send the raw recordings, with clear names and a note of which take to use where you know it. Include the script or the shot list, and the agreed music, with its licence. Share everything in one folder, rather than several emails.</p>
<h2>Agree the revision rounds</h2>
<p>Agree how many rounds of revisions are included, and what counts as a revision. A round is one set of notes, given together. Agree a deadline for each round, so the work does not drift.</p>
<h2>Give feedback that is easy to act on</h2>
<ul>
<li>Use timestamps, such as 04:32, for each note.</li>
<li>Write one change per note, and say what you want, not only what you dislike.</li>
<li>Group related notes together, and send them in one message.</li>
</ul>
<h2>Keep one shared place</h2>
<p>Keep the project file, the exports and the notes in one shared folder, with the version labels. Check that both sides are looking at the same version before you give feedback. The <a href="/tunedzy/blog/how-to-version-audio-projects">versioning post</a> covers how to label the exports.</p>
<h2>Limits</h2>
<p>Remote work depends on the connection and on clear communication. Build in time for delays, and check the final export on your own devices before you approve it.</p>
''',
    faq=[('What should I send an editor first?', 'A clear brief, the raw files, the script and a reference example.'),
         ('How do I give feedback that is easy to use?', 'Use timestamps, one change per note, and group related notes together.'),
         ('How many revisions should I agree?', 'Agree a number before you start, so the work has a clear end.'),
         ('Where should files live?', 'In one shared folder with clear version labels, so both sides see the same version.')])
