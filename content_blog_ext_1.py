"""Blog posts, batch 1 of 10: podcast cluster. Merged into content_blog.py.
Each post answers one search first, then explains it in plain steps, admits its limits, and links to a tool or guide.
No invented statistics, reviews, prices or benchmarks."""

CLUSTERS = {
    'podcast': dict(tool='lufs-meter', label='Podcast sound and editing', tool_name='LUFS Meter'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='podcast-episode-length-how-long-should-a-podcast-be', cluster='podcast', kw='how long should a podcast episode be',
    title='How Long Should a Podcast Episode Be? A Practical Answer',
    desc='How long a podcast episode should be depends on the show, the listener and the platform. How to choose a length, test it and stop padding.',
    h1='How Long Should a Podcast Episode Be?',
    answer='There is no single right length. Choose the length the material needs, then check your own listening data. Many shows find that tighter episodes keep more listeners to the end.',
    body='''
<p>Every podcaster asks this, usually after a first episode that ran long and felt slow. The honest answer is that the right length is the one your material needs and your listeners will finish. A tight twenty minutes can hold attention better than a loose hour, and a deep interview can justify ninety minutes if every section earns its place.</p>
<h2>Start from the points, not the clock</h2>
<p>Before you record, write down the three to five things the episode must say. Put them in order and give each one a rough time. If the whole plan fits in twenty-five minutes, a forty-minute recording will almost certainly feel padded, however good the guest is. Length follows the plan, not the other way round.</p>
<h2>Read your own drop-off data</h2>
<p>Hosting platforms show where people stop listening. If most listeners leave in the first five minutes, the intro is too long or too slow. If they drop in the middle of a segment, that segment is the problem. Use your own numbers to decide, rather than a rule you read once. Compare episodes on similar topics, because a tutorial and a conversation behave differently.</p>
<h2>Match the length to the format</h2>
<ul>
<li><strong>Solo commentary</strong> often works best shorter, because one voice for a long time tires people quickly.</li>
<li><strong>Interviews</strong> follow the guest&rsquo;s story. Cut the warm-up chat and the long goodbye, which rarely matter to anyone else.</li>
<li><strong>Narrative shows</strong> can run longer when each chapter moves the story forward.</li>
<li><strong>Quick updates</strong> should stay short and predictable, so people know the show is worth a few minutes.</li>
</ul>
<h2>Cut for pace, then check again</h2>
<p>Padding is anything that repeats a point, waits for a laugh that does not come, or restates the show&rsquo;s theme. The fastest way to find it is to read the transcript and cut repeats first, then tangents. The <a href="/tunedzy/edit-a-podcast-by-its-words">edit by words guide</a> shows how to do this without losing the flow.</p>
<h2>Keep a range, not a rule</h2>
<p>Listeners build habits around roughly what to expect. Choose a range you can keep, such as twenty to thirty minutes, and aim inside it. A show that is usually the same length is easier to fit into a commute, and easier for you to plan. Going well outside the range now and then is fine when the material calls for it.</p>
<h2>Limits of this advice</h2>
<p>Length is one signal among many. Sound quality, a clear topic and a strong first minute matter more than the exact number of minutes. If you are not sure, publish one shorter and one longer episode, then compare the listen-through rates after a few weeks.</p>
''',
    faq=[('Is there a standard podcast length?', 'No. Lengths vary widely by genre and format. Choose what the material needs, then check your own listening data.'),
         ('Are short episodes worse for podcasts?', 'Not necessarily. A tight twelve-minute episode can hold attention better than a loose hour.'),
         ('Should every episode be the same length?', 'A similar range helps people build a habit, but the exact length can change with the topic.'),
         ('What if my guest talks for a long time?', 'Edit for the story. Keep the parts that answer your questions and cut the rest, even if it was good conversation.')])

add(slug='how-to-start-a-podcast-with-a-phone-and-no-budget', cluster='podcast', kw='how to start a podcast with a phone',
    title='How to Start a Podcast With Just Your Phone',
    desc='Start a podcast with a phone and no budget: the room, the mic position, the recording app, the first clean episode and the tools that finish it.',
    h1='How to Start a Podcast With Just Your Phone',
    answer='You can start a podcast with a phone if the room is quiet and the phone is close to your mouth. Record in a soft room, clean the file gently, and focus on the first five episodes before you buy anything.',
    body='''
<p>Most phone podcasts that sound poor do so because of the room, not the phone. A modern phone records speech clearly from a short distance. The problems are echo, fans, traffic and a voice that moves around. Fix those, and a phone is enough to start a show that people can listen to all the way through.</p>
<h2>Choose the room before anything else</h2>
<p>Pick the quietest spot you have, with soft surfaces around you. A bedroom with a bed, curtains and a rug is often better than a kitchen with hard tiles. A wardrobe full of clothes makes a surprisingly good booth. Turn off fans and air conditioning, and switch the phone to do-not-disturb. Record a few seconds of silence to hear what the room adds. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone post</a> explains why that silence matters.</p>
<h2>Hold the phone the same way every time</h2>
<p>Keep the phone about a hand&rsquo;s width from your mouth, slightly to one side so breath does not hit the microphone. Use the same distance for each episode. Stand the phone on a few books or a small stand so the desk does not thump or rattle. Consistent distance matters more than a perfect distance.</p>
<h2>Use one recording app and one setting</h2>
<p>Choose a recording app that saves a high-quality file, and use the same setting for every episode. Record in one format, such as WAV or a high-bit-rate AAC, and avoid compressed voice-note modes if your app offers them. Check the first thirty seconds of each take before you carry on, so you catch a problem early.</p>
<h2>Clean the file gently</h2>
<p>After recording, clean the file lightly to remove room noise and clicks. Heavy processing makes a voice sound thin and watery, so keep the change small and listen on headphones. The <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup guide</a> walks through the steps in order.</p>
<h2>Publish the first five, then improve</h2>
<p>Your first episodes will not be perfect, and that is normal. Publish them anyway, then change one thing at a time: the distance, the room, the level, the amount of cleanup. Buy equipment only when you know which problem it solves. A small USB microphone is a sensible second step, once the room and habits are right.</p>
<h2>What a phone cannot do</h2>
<p>A phone struggles in noisy streets, in large echoey halls and with several people talking at once. For a panel or a live event, a dedicated recorder or a few microphones will do better. Be honest with listeners about where you record, and keep the show&rsquo;s sound consistent.</p>
''',
    faq=[('Do I need a microphone to start?', 'No. A phone close to your mouth in a quiet room is enough to start. A microphone helps later, once your habits are set.'),
         ('Which phone app should I use?', 'Any recorder that saves a high-quality file. Cleaning the file afterwards changes the result more than the app does.'),
         ('How long before my podcast sounds good?', 'It improves with each episode as you learn the room and your voice. Keep the setup the same so you can hear the progress.'),
         ('Can I record a guest on a phone too?', 'Yes, but each person should record their own side if possible, in a quiet room with the phone at a steady distance.')])

add(slug='podcast-intro-music-rules-and-safe-choices', cluster='podcast', kw='podcast intro music rights',
    title='Podcast Intro Music: Rights, Safe Choices and Mistakes',
    desc='Podcast intro music needs the right to use it. What to check before you use a track, safe choices for a show and the mistakes that get episodes taken down.',
    h1='Podcast Intro Music: Rights and Safe Choices',
    answer='A podcast intro needs music you have the right to use. Check the licence before you publish, and prefer music you made, music you commissioned, or a library whose licence covers podcasts.',
    body='''
<p>A short intro feels harmless, which is why so many shows get it wrong. Music is protected by copyright, and a recording that plays a commercial track to an audience is a public use. A takedown or a claim can remove an episode, and sometimes the whole feed. Getting the rights right takes a few minutes and saves a lot of trouble later.</p>
<h2>Why a short clip still counts</h2>
<p>Many people believe a few seconds are fine, or that a credit makes it legal. Neither is a safe assumption. Playing a track to yourself is different from publishing it to an audience, and a credit does not replace permission. If you do not own the rights, you need a licence that says you may use the track in this way.</p>
<h2>Three safe ways to get intro music</h2>
<ul>
<li><strong>Make it yourself.</strong> A simple phrase on a piano, a few synth notes or a sung hook that you wrote is yours to use.</li>
<li><strong>Commission it.</strong> Agree the rights in writing before the work starts, including how long you may use it and where it can appear.</li>
<li><strong>Use a licensed library.</strong> Check that the licence covers podcasts, the way you publish and any monetised use.</li>
</ul>
<h2>Read the licence, not the label</h2>
<p>A track described as &ldquo;free&rdquo; can still carry terms. Some require a credit, some limit commercial use, and some restrict how the music can be edited or used in an advert. Save a copy of the licence and the download receipt with the episode files, so you can show them if a question comes up.</p>
<h2>Keep the intro short and the voice clear</h2>
<p>Whatever the source, keep the intro brief so listeners reach the content. If the music plays under your opening words, lower it so the voice stays clear. The <a href="/tunedzy/how-to-duck-music-under-a-voiceover">ducking guide</a> shows how to lower music automatically under speech.</p>
<h2>If a claim arrives</h2>
<p>Respond with your licence or proof of ownership. If you cannot resolve it quickly, remove the track and replace it, and keep the original episode files as they were. This is general guidance, not legal advice. For anything with money, contracts or a dispute, speak to a professional who knows your country&rsquo;s rules.</p>
''',
    faq=[('Can I use a song from the radio as my intro?', 'Not without permission from the rights holders. Use music you have a licence for.'),
         ('Is royalty-free music always safe?', 'Only if the licence covers podcasts and your use. Read the terms, since royalty-free can still have limits.'),
         ('Should I credit the musician?', 'Often yes, and some licences require it. Check the terms for each track.'),
         ('Can I use a short sound effect instead?', 'The same rules apply. Check the licence for each sound, including short ones.')])

add(slug='how-to-cut-a-podcast-from-a-long-recording', cluster='podcast', kw='how to cut a long podcast recording',
    title='How to Cut a Podcast Episode From a Long Recording',
    desc='Turn a long recording into a tight podcast episode: mark the best moments, cut by the transcript, keep the natural pauses and check every join.',
    h1='How to Cut a Podcast Episode From a Long Recording',
    answer='Cut a long recording in three passes: mark the best moments, cut the repeats and tangents, then tidy the joins. Work from the transcript where you can, and keep the original recording untouched.',
    body='''
<p>An hour of conversation can become a twenty-minute episode, but only if you cut with a plan. Random cutting leaves awkward joins and loses the thread. A three-pass method keeps the story intact, and it gets faster the more episodes you do.</p>
<h2>Before you start: save the original</h2>
<p>Copy the full recording to a separate folder and do not touch it again. Work on a project that points to the copy. If you later want a longer version, a clip for social media or a re-cut after feedback, the original is still there. This one habit saves you from re-recording.</p>
<h2>Pass one: mark the moments that matter</h2>
<p>Listen once at normal speed and mark the parts you would keep if you had to choose three minutes. Look for a clear point, a good story, an answer that lands, a laugh that feels real. Ignore the rest for now. You are looking for the spine of the episode, which is usually shorter than you expect.</p>
<h2>Pass two: cut by the words</h2>
<p>Open the transcript and cut the repeats, tangents, false starts and dead air. Editing by text is faster than the waveform, and you can read the flow of the conversation as it will sound. The <a href="/tunedzy/edit-a-podcast-by-its-words">edit by words guide</a> explains how to do this in the Tunedzy transcript editor, including how to check each cut by ear.</p>
<h2>Pass three: tidy the joins</h2>
<p>Every cut is a join, and a join is where listeners notice the edit. Play each one at normal volume and at full speed. If the room tone jumps, add a short crossfade or a little room tone under the join. Remove a breath or a click only where it is distracting, because a natural breath keeps the voice human. The <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade guide</a> has the steps.</p>
<h2>Keep the natural pauses</h2>
<p>Pauses are part of how people think and talk. Remove the long dead air that drags, but keep short pauses before an important point or after a joke. A conversation with every gap removed sounds rushed and robotic.</p>
<h2>Check the finished episode</h2>
<p>Play the episode from start to end, on headphones and on a phone speaker. Check that the story still makes sense without the cut material, that the speakers sound like themselves, and that nothing repeats. Note the length of the final episode, then compare it with your plan.</p>
<h2>Limits</h2>
<p>Heavy cutting can change the meaning of an answer, so keep the context around every quote. If you are editing someone else&rsquo;s words, agree the approach first. Good editing is mostly removing what does not help the listener, not making the guest sound better than they were.</p>
''',
    faq=[('How long does cutting take?', 'It depends on the length and the material. A one-hour recording can take a few hours the first time and less as you get faster.'),
         ('Should I cut before or after cleaning?', 'Clean first, then cut. Cutting first can leave the noise changing at each join.'),
         ('Can I cut by the transcript?', 'Yes, with a transcript editor such as the one in Tunedzy. Always check each cut by ear before you publish.'),
         ('Will listeners notice the cuts?', 'Only if the joins are rough. Matched room tone and natural pauses make most cuts hard to hear.')])

add(slug='podcast-audio-mistakes-that-make-listeners-leave', cluster='podcast', kw='podcast audio mistakes',
    title='Podcast Audio Mistakes That Make Listeners Leave',
    desc='The audio mistakes that drive listeners away: uneven levels, echo, background noise, clipped speech and a loud intro. How to spot and fix each one.',
    h1='Podcast Audio Mistakes That Make Listeners Leave',
    answer='The audio mistakes that lose listeners most are uneven levels, an echoey room, steady background noise, clipped speech and a loud intro. Each one is easy to check and fix before you publish.',
    body='''
<p>Listeners forgive a lot in a podcast: a plain cover, a slow start, a host who talks too much. What they rarely forgive is sound that tires them out. Audio problems make people reach for the volume control, then turn it down again, and many simply stop. The mistakes below are the ones that show up most often in the first minutes of a show.</p>
<h2>Uneven levels between voices</h2>
<p>If one speaker is much quieter than the other, listeners keep adjusting the volume. Then the loud parts become painful. Level each voice before you mix, and check the difference by listening, not only by eye. The <a href="/tunedzy/how-to-level-voices-between-speakers">levelling guide</a> shows the steps for two or more speakers.</p>
<h2>An echoey room</h2>
<p>Hard walls make a voice sound distant and hollow. Rugs, curtains, cushions and a wardrobe of clothes absorb reflections far better than most filters can remove them later. Test the room by clapping once and listening for a ringing tail. The <a href="/tunedzy/how-to-test-your-room-for-echo">clap test guide</a> helps you choose a spot that sounds dry and close.</p>
<h2>Steady background noise</h2>
<p>A fan, a fridge, a computer or traffic under the voice is tiring over an hour, even when listeners do not name it. Turn off what you can, record at a quieter time of day, and reduce what remains gently. Over-cleaning makes the voice thin, so aim for the noise to fade into the background rather than vanish.</p>
<h2>Clipped speech</h2>
<p>Peaks that touch the top of the meter sound harsh and distorted, and digital clipping cannot be fully undone. Record with the loudest peaks well below full scale, and check the waveform after each take. A quick re-record is cheaper than a repair.</p>
<h2>A loud intro</h2>
<p>Many listeners set their volume once, at the start of an episode. If the intro is loud, the speech that follows sounds quiet, and they turn up or down. Match the intro to the episode&rsquo;s loudness, and keep music under the voice. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the common targets.</p>
<h2>Checking before you publish</h2>
<p>Listen to the full episode on headphones and on a phone speaker, because many people use the second. Check the loudness of the exported file and its true peak, not only the project. Ask one person who has not heard the episode to tell you where their attention moved. Their answer is more useful than any meter.</p>
''',
    faq=[('Which mistake matters most?', 'Uneven levels and background noise are noticed most. Start with those.'),
         ('Do listeners notice a quiet room?', 'Most do not name it, but they notice a noisy or echoey one, and they feel tired listening to it.'),
         ('How do I check for these before publishing?', 'Listen on headphones and a phone speaker, then check the loudness and peaks of the exported file.'),
         ('Can editing fix everything?', 'No. Editing helps, but a clean recording in a good room is always easier to finish well.')])

add(slug='how-to-keep-a-podcast-sounding-the-same-every-episode', cluster='podcast', kw='podcast consistent sound',
    title='How to Keep a Podcast Sounding the Same Every Episode',
    desc='A podcast that sounds consistent feels trustworthy. How to keep the room, the mic, the levels and the cleanup the same across episodes, with a simple template.',
    h1='How to Keep a Podcast Sounding the Same Every Episode',
    answer='Keep the same room, the same mic position, the same level and the same cleanup settings for every episode. Write them down as a template, and compare the first minute of each new episode with the last.',
    body='''
<p>Listeners rarely name the reasons they like a show, but they notice when the sound changes. A new room, a louder microphone or a different cleanup setting makes an episode feel like it came from another show. Consistency builds trust without anyone saying so, and it makes your own editing faster because you know what to expect.</p>
<h2>Why sameness is a feature</h2>
<p>People listen to podcasts in cars, kitchens and on walks. They choose a show partly for its familiar sound. When an episode suddenly has more echo or sits much quieter, the listener has to adjust, and some will not bother. Keeping the sound steady is a small kindness to the audience.</p>
<h2>Write a session template</h2>
<p>For each episode, record the microphone, the distance, the room, the recording level and the cleanup settings you used. A short note in the project folder is enough. The next session should start from that template, not from memory. Over time the note becomes the show&rsquo;s sound design, written down.</p>
<h2>Fix the room and the mic position</h2>
<p>Mark the microphone position on the desk with tape. Record in the same spot, and at a similar time of day if traffic, heating or neighbours change the room. If the room has to change, record a short test and compare it with the last episode before you commit to a full recording.</p>
<h2>Use the same loudness target</h2>
<p>Set every episode to the same loudness target, so the show sits at a similar level from one episode to the next. Listeners who switch between shows will hear the difference. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the common targets and why one number is not right for every platform.</p>
<h2>Compare the first minute</h2>
<p>Before you publish, play the first minute of the new episode straight after the last one. If the room tone, the level or the brightness differs, adjust and check again. Two minutes of comparison prevents most of the drift that happens over a season.</p>
<h2>Where consistency can go wrong</h2>
<p>A show that never changes can feel stale. Keep the sound steady, but let the content move. If you change equipment on purpose, do it at the start of a season and note the date, so listeners and future you understand why the sound changed.</p>
''',
    faq=[('What if my room changes?', 'Record a short test, compare it with the last episode, then adjust the cleanup and write the change into the template.'),
         ('Do I need the same microphone?', 'The same microphone helps, but the same position and room matter as much.'),
         ('How do I keep the cleanup the same?', 'Save the settings you used and reuse them, adjusting only when a recording needs it.'),
         ('Should I tell listeners about a change?', 'Yes, briefly, if the sound changes on purpose. A short note in the episode description is enough.')])

add(slug='how-to-make-podcast-show-notes-from-a-transcript', cluster='podcast', kw='podcast show notes from transcript',
    title='How to Make Podcast Show Notes From a Transcript',
    desc='Turn a podcast transcript into useful show notes: a summary, timestamps, links and quotes. How to do it quickly, and what to check before you publish.',
    h1='How to Make Podcast Show Notes From a Transcript',
    answer='Show notes come from the transcript: write a short summary, add timestamps for the main topics, list the links and people mentioned, and pull one or two quotes. Check every name and link before you publish.',
    body='''
<p>Good show notes help people decide to press play, find the part they want and share the episode. They also help search engines understand what an episode covers. A transcript makes writing them much faster, provided you clean it first and check the facts that matter.</p>
<h2>Start with a clean transcript</h2>
<p>A speech-to-text transcript gets most words right and some names and technical terms wrong. Read it once and fix every name, brand and term. Remove the ums and the repeated words that add nothing. A clean transcript turns the notes into a quick job rather than a rewrite.</p>
<h2>Write a short summary first</h2>
<p>Write two or three sentences that say what the episode covers and who it is for. Listeners decide in a few seconds, so put the most useful point first. Avoid describing the show itself. Say what the listener will learn or hear.</p>
<h2>Add timestamps for the main topics</h2>
<p>Find the main topics in the transcript and note the time each one starts. Use short labels, such as &ldquo;why the first draft failed&rdquo;, rather than long sentences. Timestamps help listeners jump to what they came for, and they are easy to read off a transcript editor.</p>
<h2>List the links and people</h2>
<p>Note every book, tool, product and person mentioned, with a public link where one exists. Check that each link opens before you publish. If a guest has asked not to be linked or named, respect that and leave the link out.</p>
<h2>Pick one or two quotes</h2>
<p>A short quote makes the notes feel alive. Quote exactly, keep it short, and check it against the audio, because transcripts can mishear a word. A quote that makes sense on its own works best.</p>
<h2>Re-use the same transcript</h2>
<p>The transcript can also make captions and a text version of the episode. The <a href="/tunedzy/how-to-export-captions-srt-and-vtt">caption export guide</a> shows the common file formats, which makes the transcript useful well beyond the show notes.</p>
<h2>Limits</h2>
<p>Automatic transcripts can be wrong, especially with accents, crosstalk and specialist words. Always check the facts in the notes against the episode. Do not publish a claim you have not confirmed in the audio.</p>
''',
    faq=[('Can a transcript be used as show notes directly?', 'Only after cleaning. Speech tools miss names and terms, and show notes need a short summary that a transcript does not give.'),
         ('How long should show notes be?', 'Short enough to scan. A summary, timestamps and links are usually enough.'),
         ('Is the transcript private?', 'Check the privacy settings of any tool you use. Some services send audio to their servers, so read what each one does with your files.'),
         ('Do I need timestamps for every topic?', 'Not for every line. Mark the main topics so listeners can jump to what they want.')])

add(slug='how-to-record-a-solo-podcast-without-sounding-flat', cluster='podcast', kw='solo podcast sound',
    title='How to Record a Solo Podcast Without Sounding Flat',
    desc='A solo podcast can sound flat or monotone. How to use pace, pauses, a close mic and light processing to keep a single voice lively and easy to follow.',
    h1='How to Record a Solo Podcast Without Sounding Flat',
    answer='A solo voice sounds flat when the pace is even, the room is dead and the microphone is far away. Vary the pace, use pauses on purpose, keep the mic close and steady, and keep the processing light.',
    body='''
<p>A solo podcast has nowhere to hide. There is no guest to carry the energy and no second voice to break up the rhythm. Listeners hear one person for thirty minutes, so the delivery and the sound have to hold their attention. The good news is that most of the fix is planning and habit, not expensive equipment.</p>
<h2>Plan the emphasis before you record</h2>
<p>Write the episode as points, and mark which ones matter most. Speak faster on simple points and slower on the ones you want people to remember. A steady pace all the way through wears listeners down, even when the content is strong. Rehearse the key sentence once, out loud, to hear where the weight falls.</p>
<h2>Use pauses on purpose</h2>
<p>A short pause before a key point lets listeners catch up. After a joke or a surprising fact, a half-second of silence helps it land. Do not fill every gap with words. Silence is part of the rhythm, and an uninterrupted monologue can feel like a lecture. Cut only the long pauses that drag.</p>
<h2>Keep the microphone close and steady</h2>
<p>A close microphone gives intimacy and presence, which suits a solo voice. Keep the distance the same from take to take, and use a pop filter so breath does not thump. If you lean back or turn your head, the sound changes, so set up a chair and a desk that keep you still.</p>
<h2>Avoid a dead room</h2>
<p>A completely dead room can sound unnatural and tiring. Aim for a soft room with a little natural warmth, rather than an airless booth. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone post</a> explains why a little room sound helps the voice feel real.</p>
<h2>Process lightly</h2>
<p>Heavy compression and high levels flatten a solo voice and make the breaths sound loud. Use gentle cleanup and a moderate level, then compare the processed file with the original on headphones. If the voice sounds smaller, you have done too much.</p>
<h2>Record in short sections</h2>
<p>Record each section separately, with a short pause between. If one section goes wrong, you can re-record just that part without losing the whole episode. Short takes also help your energy, because each one is a fresh start.</p>
<h2>Limits</h2>
<p>A solo show takes more planning than an interview, and it is easy to ramble. Good preparation matters more than any equipment. If the voice still sounds flat after the changes, record a few minutes and listen back to find where your energy drops.</p>
''',
    faq=[('Is a solo podcast harder to make interesting?', 'It takes more planning. Pace, pauses and a clear structure carry it, rather than a guest.'),
         ('Should I use music between segments?', 'Only with the rights to the music, and keep it well under the voice. The intro music post explains the rights.'),
         ('How do I stop sounding monotone?', 'Plan the emphasis, speak to one listener, and record key sections a few times to choose the best take.'),
         ('Can I use a script?', 'A short outline works better than a full script for most solo shows, because a script can sound read.')])

add(slug='podcast-guest-consent-what-to-agree-before-recording', cluster='podcast', kw='podcast guest consent',
    title='Podcast Guest Consent: What to Agree Before You Record',
    desc='Agree the basics with a podcast guest before recording: consent to record, how the episode will be used, editing rights and what happens to the files.',
    h1='Podcast Guest Consent: What to Agree Before You Record',
    answer='Before you record a guest, agree in writing that the conversation is recorded, how the episode will be published, what edits are allowed and what happens to the files. Recording rules vary, so check them where you and the guest are.',
    body='''
<p>Most guests are happy to talk on a show, and most problems come from something nobody said out loud. A guest may assume the episode will never be clipped, or that they can review every word, or that the recording will be deleted after publication. A short, clear agreement before you press record prevents those disagreements and protects both of you.</p>
<h2>Consent to record</h2>
<p>Tell the guest that you are recording, and get their agreement before the recording starts. It is good practice to repeat the agreement at the beginning of the recording, so it is captured. Some places require everyone in the conversation to agree. Check the rules for where you and the guest each are, because they can differ.</p>
<h2>How the episode will be used</h2>
<p>Say where the episode will be published, and whether it may be clipped, shortened or reused. A guest should know if the conversation will appear in a trailer, on social media, in a paid course or in a video. Be specific, because &ldquo;the podcast&rdquo; can mean more than one thing.</p>
<h2>Editing rights</h2>
<p>Agree what edits you will make. Removing ums, cutting tangents and fixing a stumble are normal and expected. Changing what was said is not. Decide whether the guest will hear the edit before it goes out, and how long they have to respond. Write this down so there is no surprise later.</p>
<h2>What happens to the files</h2>
<p>Agree how long you keep the raw recordings and who can access them. If you share the files with an editor or a transcription service, say so. Keep the agreement with the episode files, so you can show it if a question comes up.</p>
<h2>Keep it simple</h2>
<p>A short written email is often enough for a casual show. For a paid collaboration, a licence or anything with money involved, use a proper written agreement and ask a professional to check it. This section is general guidance, not legal advice.</p>
<h2>If a guest changes their mind</h2>
<p>Re-read what you agreed. Respond politely, and be willing to remove a section if the agreement allows it or the guest asks in good faith. Handling a request calmly and quickly keeps the relationship good, and makes future guests more confident about working with you.</p>
''',
    faq=[('Do I need a written agreement?', 'A written note is a good habit and shows what was agreed. Check whether your situation needs more.'),
         ('Can I record without telling the guest?', 'Not in many places, and it damages trust. Always tell the guest and get agreement first.'),
         ('What if the guest changes their mind after the episode?', 'Check what you agreed, respond politely, and handle the request according to your agreement.'),
         ('Should I record the consent itself?', 'Often yes. A short spoken confirmation at the start is a simple record of what was agreed.')])

add(slug='podcast-export-settings-for-hosts-explained', cluster='podcast', kw='podcast export settings',
    title='Podcast Export Settings Explained for Hosts',
    desc='The podcast export settings that matter: format, sample rate, bit rate, mono or stereo, loudness and true peak, with what to choose for speech.',
    h1='Podcast Export Settings Explained for Hosts',
    answer='For a speech podcast, keep a lossless master, then export an MP3 at a high bit rate, mono or stereo as your host recommends. Set the loudness to your target, check the true peak of the exported file, and keep the master for re-exports.',
    body='''
<p>Export settings look technical, but for a speech podcast only a few choices matter. Get them right once, write them down, and you will not think about them again. Get them wrong and you may upload a file that is too quiet, too loud or much bigger than it needs to be.</p>
<h2>Keep a master, then export the copy</h2>
<p>Keep a lossless WAV or FLAC master of the finished episode. Use it for every later export: the MP3 for your host, a shorter clip, or a version for another platform. Exporting the MP3 from the master avoids repeated compression, which slowly reduces quality if you re-encode a compressed file.</p>
<h2>Sample rate and bit depth</h2>
<p>44.1 kHz and 48 kHz are both fine for speech. Keep the rate you recorded at, to avoid a conversion step that adds nothing. A 24-bit master is a sensible choice, and 16 bits is usually enough for the final file. Do not raise the rate above the recording, because it adds size without adding detail.</p>
<h2>Bit rate for the MP3</h2>
<p>Use the highest bit rate your host accepts for the MP3, within a size that listeners can download comfortably. For speech, a high bit rate sounds very close to the master on most devices. Check what your host recommends, because the best setting is the one the host keeps intact.</p>
<h2>Mono or stereo</h2>
<p>Most speech podcasts are mono, since a single voice or a conversation gains little from stereo. Mono files are smaller. Use stereo only if your mix uses it, for example for music with a stereo intro or a deliberate effect.</p>
<h2>Loudness and true peak</h2>
<p>Set the loudness of the exported file to your target, and check the true peak of the export rather than the project. The true peak shows the level between samples, which is where clipping can hide. The <a href="/tunedzy/how-to-export-audio-for-spotify-and-apple-podcasts">export guide</a> covers the steps for the main podcast platforms in more detail.</p>
<h2>Check the file that goes up</h2>
<p>After export, open the MP3 in a player and listen to the start, a middle section and the end. Confirm the file is the one you intended, with the right name, length and cover art, before you upload it. Some hosts re-encode the file, so check the final version on the platform too.</p>
<h2>Limits</h2>
<p>Platforms change their recommendations, so treat any number as a starting point and confirm the current guidance from your host. The steps above stay the same even when the numbers change.</p>
''',
    faq=[('Which setting matters most?', 'The loudness and true peak of the exported file, then the bit rate for the MP3.'),
         ('Should I export stereo for a podcast?', 'Only if your mix needs it. Most speech shows are mono.'),
         ('Do hosts change the file?', 'Some re-encode it. Upload the checked export, then listen to the version on the platform too.'),
         ('What should I keep after export?', 'Keep the master, the project file and a note of the export settings, so you can repeat the result.')])
