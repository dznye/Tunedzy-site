"""Blog posts, batch 23: editing audio well (evergreen). Merged into content_blog.py.
Editing techniques are explained as judgement calls with limits, not rules. Shortcut and menu details are kept general
because they differ between editors. No invented statistics. Funnel: each post ends with a link to Tunedzy Go and to
the matching free tool."""

CLUSTERS = {
    'evergreen-edit': dict(tool='vocal-checker', label='Editing audio well', tool_name='Vocal Checker'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='audio-editing-workflow-for-beginners', cluster='evergreen-edit', kw='audio editing workflow',
    title='Audio Editing Workflow for Beginners: Raw File to Finished Episode',
    desc='An audio editing workflow for beginners: the steps from raw file to finished episode, in the order that prevents rework and keeps the sound clean.',
    h1='Audio Editing Workflow for Beginners: Raw File to Finished Episode',
    answer='A reliable editing workflow runs in a fixed order: back up the raw file, listen through once, fix the faults, cut the structure, clean and level the voices, add music and effects, then check and export. Following the same order every time prevents rework and keeps problems from spreading through the edit.',
    body='''
<p>Beginners often open an editor and start clicking, cutting and processing without a plan. The result is usually a file that takes many hours, sounds uneven and is hard to finish. An editing workflow is a fixed sequence of steps that solves the problems in a sensible order. Each stage prepares the next, so the work moves forward rather than looping back. Once the order is familiar, it becomes automatic, and the edit becomes faster and calmer.</p>
<p>This post sets out a workflow for a typical spoken episode, with notes on how it changes for music and video. It is a starting point, and experienced editors adapt it, but the principle of working in order holds.</p>
<h2>Back up the raw file first</h2>
<p>Before you open the editor, copy the raw recording to a safe place and do not change it. Work on a project file that points to a copy. The raw file is the one thing you cannot replace, and a mistake in an edit can always be undone if the original is safe. This single habit prevents more disasters than any other part of the workflow.</p>
<p>Name the project with the episode and the date, so you can find it later and tell it apart from earlier versions.</p>
<h2>Listen through once</h2>
<p>Play the whole recording straight through, on headphones, without making changes. Note the problems and the strongest moments. Write the times down. The first listen gives you the shape of the episode and a list of tasks, which is far more useful than starting at the beginning and fixing as you go.</p>
<h2>Fix the faults first</h2>
<p>Clicks, dropouts, hum and clipping are faults, and they should be repaired before the structure changes. A fault repaired after a cut can end up on the wrong side of a join. Fix each one at its position in the raw file, then check that the repair sounds natural in context.</p>
<h2>Cut the structure</h2>
<p>Next, shape the episode. Remove the repeats, the tangents that do not serve the story, the long dead air and the false starts. Work on the story rather than the sound at this stage, and keep the natural pauses that help the listener follow. The <a href="/tunedzy/edit-a-podcast-by-its-words">edit by words guide</a> shows a fast way to make these cuts from a transcript.</p>
<h2>Clean and level the voices</h2>
<p>Once the structure is set, clean the voices and balance them. Reduce steady noise gently, then level each speaker so they sit together. Clean after cutting, not before, because processing applied to a long file may behave differently at each join. The <a href="/tunedzy/how-to-level-voices-between-speakers">levelling guide</a> explains the method for two or more speakers.</p>
<h2>Add music and effects</h2>
<p>Add music, intros and effects last, once the voices are settled. Lower the music under speech, and check that every element is licensed for your use. Music can hide problems in the voices, so listen to the speech on its own after adding it, to be sure it is still clear.</p>
<h2>Check the whole episode</h2>
<p>Play the finished episode from start to end, on headphones and on a phone speaker. Check the joins, the levels, the music balance and the ending. Listen for anything that makes you want to turn the volume up or down, since those moments point to the problems a listener will feel.</p>
<h2>Export and keep the master</h2>
<p>Export the file in the format your platform requires, and check its loudness and true peak. Keep the master project and the export together, so you can re-export later for a different platform or a clip.</p>
<h2>Why the order matters</h2>
<p>Each stage depends on the one before. Cleaning before cutting spreads effort over material you will remove. Adding music before levelling the voices hides problems in the speech. Exporting before checking the whole episode means a fault may slip out. Working in order keeps each decision meaningful, and it prevents the endless loop of fixing and re-fixing.</p>
<h2>Adapting the workflow</h2>
<p>For music, the order changes: the structure and arrangement come first, then the balance of parts, then the processing. For video, the cuts follow the picture, so the audio is edited first and the picture is cut to match. The principle of working in a deliberate order still applies, and the best workflow is the one you can repeat.</p>
<h2>Keep a workflow checklist</h2>
<p>Write the steps down as a checklist, and tick them off for each episode. A checklist protects the workflow on busy weeks, when the temptation to skip a step is strongest. Review the list every few months, and add any step that would have caught a problem you missed.</p>
<h2>Limits</h2>
<p>A workflow is a guide, not a rule. Some episodes need a different order, and some editors prefer to work in different ways. The aim is a repeatable process that produces a clean, finished episode. If your process is working, keep it, and change it only when a specific problem shows you why.</p>
<h2>Check the finished file</h2>
<p>A final check before publishing catches the problems that editing hides. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the cutting technique itself, read the <a href="/tunedzy/blog/how-to-cut-a-podcast-from-a-long-recording">long recording guide</a> in this series.</p>
''',
    faq=[('What is the most important first step?', 'Backing up the raw file and never changing it. Everything else can be undone if the original is safe.'),
         ('Should I clean before or after cutting?', 'After cutting, so processing is applied to the material you keep, not the material you remove.'),
         ('Where does music go in the order?', 'Last, once the voices are settled, so it does not hide problems in the speech.'),
         ('Is this workflow the same for music?', 'The order changes for music, with structure and balance first, but working deliberately still applies.')])

add(slug='cutting-audio-on-the-breath', cluster='evergreen-edit', kw='cut audio on breath',
    title='Cutting Audio on the Breath: How to Make Edits That Sound Natural',
    desc='Cutting audio on the breath: why breath points make natural edit points, how to find them and how to keep the rhythm of speech when you join two takes.',
    h1='Cutting Audio on the Breath: How to Make Edits That Sound Natural',
    answer='Cutting on the breath means making an edit at a natural pause, where a speaker takes a breath, so the change sounds like a normal rhythm of speech rather than a jump. Breaths give a natural boundary, and a cut placed there is much harder to hear than one placed in the middle of a word.',
    body='''
<p>A good edit is one the listener does not notice. The most common way to achieve that in spoken audio is to cut on the breath. Speakers breathe at natural points, and a cut that falls at a breath matches the rhythm the listener already expects. A cut in the middle of a word, or in the middle of a sentence without a breath, sounds abrupt, even when the content is perfectly logical.</p>
<p>This post explains why breath points work so well, how to find them, how to make the cut and how to keep the breath sounding human after the join.</p>
<h2>Why breaths make good edit points</h2>
<p>A breath is a natural pause in the flow of speech. The ear accepts a change in sound at a breath, because the change matches what a person does while talking. The listener’s attention also resets slightly at a breath, so a cut there is less likely to break the thread of the sentence.</p>
<p>The effect is strongest when the breath comes before a new thought. A cut at that point feels like a new sentence starting, rather than an edit in the middle of one.</p>
<h2>Find the breaths</h2>
<p>Breaths are easy to miss at normal speed. Zoom in on the waveform near the pause, where the breath appears as a soft, noisy shape. Listen at slower speed to hear the breath clearly, and mark the points you might use. A transcript can help, because it shows where the sentences end, but the breath is the sound you need.</p>
<h2>Make the cut</h2>
<p>Place the cut in the middle of the breath, or just before the sound of the new phrase begins. Avoid cutting into the start of a word, since that can clip the consonant. Make the cut with a very short fade on each side, so the change is smooth. Listen to the join at normal speed, and check that the rhythm of the breath still sounds natural.</p>
<h2>Keep the breath human</h2>
<p>After a cut, the breath may sound too short, too long or too loud, depending on where it was joined. Keep a natural breath at each join. If a breath has been cut in half, the listener may hear the change as a stutter. Adjust the length by a small amount, rather than removing the breath altogether, because a voice with no breath sounds unnatural.</p>
<h2>When there is no breath</h2>
<p>Sometimes the pause you need has no breath in it. In that case, look for a natural pause in the room tone, or a point where the speaker’s energy drops. A short piece of room tone can be used to bridge the change, with a crossfade to hide the join. The <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade guide</a> explains the method.</p>
<h2>Judge by the flow</h2>
<p>After cutting, play the whole passage at normal speed, not just the join. The edit should feel like part of the speech, not a separate sound. If you notice the cut as a cut, try moving it a little, or adjust the breath.</p>
<h2>Common mistakes</h2>
<ul>
<li>Cutting into the start of a word, which clips the consonant.</li>
<li>Removing every breath, so the speaker sounds robotic.</li>
<li>Leaving a breath that is much louder after the join than before it.</li>
<li>Cutting at a pause that has no sense of a new thought.</li>
<li>Judging the cut only on a loud speaker, where the breath may be inaudible.</li>
</ul>
<h2>Practise on a short piece</h2>
<p>A short piece of speech, with several breaths, is the best practice material. Make a few cuts on breath points, then listen to them back to back. The differences will teach you more than any written rule, and the skill grows quickly.</p>
<h2>Limits</h2>
<p>Breath cuts work best for speech with a clear rhythm. Fast speakers, overlapping speech and emotional moments can make breath points hard to find or wrong to use. Judge each cut by ear, and accept that some joins will need a different solution.</p>
<h2>Listen for the breath, not the cut</h2>
<p>A good edit is judged by the breath and the flow. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps you judge the joins. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the breath level itself, read the <a href="/tunedzy/blog/how-to-edit-breaths-in-a-voiceover">breath editing post</a> in this series.</p>
''',
    faq=[('Why do breath cuts sound natural?', 'They match the rhythm of speech, so the listener expects a change at that point.'),
         ('Should I remove breaths at joins?', 'Keep a natural breath at each join. A voice without breath sounds unnatural.'),
         ('What if there is no breath at the cut point?', 'Use a natural pause in the room tone, and crossfade the join.'),
         ('How do I practise?', 'Make a few cuts on breath points in a short passage, then listen to them back to back.')])

add(slug='editing-laughter-and-reactions-in-podcasts', cluster='evergreen-edit', kw='editing laughter in podcast',
    title='Editing Laughter and Reactions in Podcasts Without Losing the Moment',
    desc='Editing laughter and reactions in podcasts: when to keep them, how to shorten long laughs, how to avoid unnatural joins and how to protect the moment.',
    h1='Editing Laughter and Reactions in Podcasts Without Losing the Moment',
    answer='Keep most laughter and reactions, because they show that the conversation is alive. Shorten a laugh that runs too long, and cut any reaction that repeats or distracts, but place the cuts carefully so the moment still feels real. A laugh that is edited too neatly can sound fake, so judge each change by how the moment feels.',
    body='''
<p>Laughter is one of the most human sounds in a podcast, and it is one of the easiest to spoil in editing. A laugh that runs too long can drag the episode, while a laugh that is cut too neatly can sound false. Reactions such as a surprised breath, a sharp intake or a quiet “wow” carry emotion that listeners respond to. The job of the editor is to shorten what drags and protect what makes the conversation feel alive.</p>
<p>This post explains when to keep laughter and reactions, how to shorten them, how to make the joins invisible and how to avoid making the conversation feel scripted.</p>
<h2>Why keep most reactions</h2>
<p>Reactions show that the people in the conversation are listening to each other. They are part of the connection that makes a podcast enjoyable, and they signal that the moment mattered. Removing too many reactions turns a conversation into a series of answers, and listeners can feel the difference even when they cannot name it.</p>
<p>A good rule is to keep the reactions that come from the moment, and to cut only the ones that repeat, drag or distract from the point.</p>
<h2>Shorten a laugh that runs long</h2>
<p>A long laugh can be shortened by cutting part of the sustained middle, keeping the start and the tail. Choose the cut point carefully, usually at a point where the laugh changes shape, so the change sounds like the natural end of the laugh. Keep a little of the release, since a laugh that stops abruptly sounds unnatural.</p>
<h2>Keep the energy at the join</h2>
<p>When you cut a laugh, the energy of the voices must still feel right at the join. If a laugh is cut so the next line starts in the middle of the laugh’s peak, the moment can feel rushed. Leave a short breath or pause after the cut, so the conversation can breathe.</p>
<h2>Protect the moment</h2>
<p>Some laughs are the best parts of an episode, and they should be kept almost untouched. If a laugh captures a real surprise or a shared joke, resist the urge to shorten it. The listener feels the warmth of a moment like that, and editing it heavily can take that warmth away.</p>
<h2>Check the room sound</h2>
<p>Laughter often comes with a change in room sound, because people move, turn or lean. A join in the middle of a laugh can therefore expose a change in the room. Check the room tone on each side of the join, and use a short crossfade or a matched piece of room tone if needed.</p>
<h2>Avoid making it feel scripted</h2>
<p>Overediting a conversation can make it sound scripted, with perfectly timed reactions and no natural overlap. Keep some of the natural overlap between speakers, and keep the pauses that feel human. A conversation that sounds real is more engaging than one that sounds polished.</p>
<h2>A simple approach</h2>
<ol>
<li>Listen to the whole conversation first, and mark the laughs and reactions.</li>
<li>Keep the reactions that come from the moment, and cut only the repeats.</li>
<li>Shorten long laughs at a natural change in shape, keeping the release.</li>
<li>Check the join for room sound and energy, and fix any harsh change.</li>
<li>Listen to the whole episode, and ask whether it still feels alive.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Cutting every laugh short, so the episode feels flat.</li>
<li>Joining a laugh at its peak, which makes the next line feel rushed.</li>
<li>Ignoring the change in room sound at the join.</li>
<li>Keeping a laugh that is loud and distracting for no reason.</li>
<li>Removing all the overlap between speakers, which makes the talk sound scripted.</li>
</ul>
<h2>Limits</h2>
<p>There is no single right amount of laughter to keep. Some shows are light and playful, and others are serious and focused. The guiding question is whether the reaction helps the listener feel the conversation, and the answer depends on the show and the people in it. Discuss sensitive moments with the guests before publishing.</p>
<h2>Keep the consent and the context</h2>
<p>Editing a reaction can change its meaning, so keep the context honest. A laugh that was at a joke should not be made to sound like a laugh at a person. If a moment is sensitive, check with the speaker before publishing, as covered in the <a href="/tunedzy/blog/podcast-guest-consent-what-to-agree-before-recording">consent post</a> in this series.</p>
<h2>Check the result on a phone</h2>
<p>Laughter can sound very different on a phone speaker. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping and level problems in a recording you own, which helps with loud reactions. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the wider editing workflow, read the <a href="/tunedzy/blog/audio-editing-workflow-for-beginners">editing workflow post</a> in this series.</p>
''',
    faq=[('Should I keep the laughs?', 'Keep most of them. Cut only the repeats and the ones that drag or distract.'),
         ('How do I shorten a long laugh?', 'Cut the sustained middle at a natural change, and keep a little of the release.'),
         ('Why does an edited laugh sound fake?', 'The join is too neat, or the energy is wrong at the cut. Leave a breath or pause after the join.'),
         ('Should I check sensitive laughs with the guest?', 'Yes. Editing can change the meaning, so check before publishing if the moment is sensitive.')])

add(slug='shortening-pauses-without-sounding-rushed', cluster='evergreen-edit', kw='shorten pauses in audio',
    title='Shortening Pauses in Audio Without Sounding Rushed',
    desc='Shortening pauses in audio without sounding rushed: which pauses to cut, how much to remove and how to keep the rhythm and the emphasis of speech.',
    h1='Shortening Pauses in Audio Without Sounding Rushed',
    answer='Shorten pauses that drag, such as dead air and long hesitations, but keep the pauses that give emphasis, let a point land or mark a change of thought. Cut in small amounts, and listen for any loss of rhythm. A pause shortened too far makes speech sound rushed, anxious or robotic.',
    body='''
<p>Pauses are one of the first things an editor reaches for when a recording feels slow. Long gaps, hesitations and dead air can make a talk drag, and removing them can tighten the episode noticeably. The risk is that pauses are part of how people think and speak. A pause before a key point gives it weight, and a pause after a joke lets it land. Cut too many, and the speech sounds rushed, anxious or machine-like.</p>
<p>This post explains how to tell the pauses that drag from those that help, how much to remove and how to keep the rhythm and emphasis of the speaker.</p>
<h2>Why pauses matter</h2>
<p>Listeners use pauses to follow the shape of an argument. A pause marks the end of one idea and the start of the next, and it gives the listener a moment to take in what was said. Pauses also carry emotion. A longer silence before an answer can signal thought or weight, and a short one can signal confidence or excitement.</p>
<p>The editor’s job is to decide which pauses serve the speaker and which only fill time.</p>
<h2>Sort the pauses</h2>
<p>Listen through the recording and sort the pauses into groups. Dead air, long gaps caused by a technical problem or a moment of confusion, can usually be cut. Hesitations, where a speaker searches for a word, are often worth shortening slightly. Pauses that give emphasis or mark a change of thought should usually be kept, perhaps reduced only a little.</p>
<h2>Cut in small amounts</h2>
<p>When you shorten a pause, remove a small amount at a time, and listen after each change. A pause cut by a quarter of its length often feels tighter without sounding rushed. Cutting half or more can change the feel of the speech. Work gradually, and stop when the rhythm feels natural.</p>
<h2>Keep the room tone</h2>
<p>A pause is not silent in a real recording. It contains the room tone, the quiet background that every recording has. If you cut a pause too short, the room tone may jump at the join. Keep a little of the room tone on each side, and use a short crossfade to smooth the change. A consistent room tone makes the edit invisible.</p>
<h2>Protect the emphasis</h2>
<p>Pauses around a key word or a surprising point are part of the emphasis. Keep them, even when the surrounding talk is cut. Listeners often remember the moment after a pause, because the pause prepared them to hear it.</p>
<h2>Check the rhythm</h2>
<p>After shortening, listen to a whole section at normal speed. Check whether the speaker still sounds calm and clear, and whether the points still land. A passage that feels tense or breathless may need a few pauses restored. The rhythm should feel like the speaker’s own, not a faster version of it.</p>
<h2>Watch the automatic tools</h2>
<p>Many editors now remove silence automatically, with a threshold for what counts as a pause. Automatic removal is fast, but it cannot tell the difference between dead air and emphasis. Use it as a first pass, then listen to every change and restore the pauses that matter.</p>
<h2>A simple approach</h2>
<ol>
<li>Listen to the whole recording and sort the pauses into groups.</li>
<li>Cut dead air and technical gaps, which usually do not help the listener.</li>
<li>Shorten hesitations slightly, in small steps.</li>
<li>Keep the pauses that give emphasis or mark a change of thought.</li>
<li>Check the rhythm at normal speed, and restore any pause that makes the talk feel rushed.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Cutting every pause, so the speaker sounds anxious.</li>
<li>Removing the pause before a key point.</li>
<li>Joining pauses so the room tone jumps.</li>
<li>Relying on automatic silence removal without listening.</li>
<li>Making the speaker sound faster than they naturally speak.</li>
</ul>
<h2>Limits</h2>
<p>How much to shorten depends on the speaker, the content and the audience. A fast-paced news summary may take many pauses, while a reflective interview may need almost all of them. Judge each recording by how it feels, and keep the speaker’s natural rhythm as the guide.</p>
<h2>Keep the speaker’s voice</h2>
<p>Editing pauses is about keeping the speaker’s voice, not changing it. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For a related technique, read the <a href="/tunedzy/blog/cutting-audio-on-the-breath">breath cutting post</a> in this series.</p>
''',
    faq=[('How much of a pause should I cut?', 'Small amounts at a time. A quarter of the length often tightens the talk without rushing it.'),
         ('Should I remove all silence?', 'No. Keep the pauses that give emphasis or mark a change of thought.'),
         ('Why does my edited talk sound anxious?', 'Too many pauses were cut. Restore the ones that let the points land.'),
         ('Is automatic silence removal safe?', 'Use it as a first pass only, and listen to every change.')])

add(slug='removing-filler-words-carefully', cluster='evergreen-edit', kw='remove filler words audio',
    title='Removing Filler Words Carefully: When to Cut and When to Keep',
    desc='Removing filler words from audio carefully: which fillers to cut, which to keep, how to avoid unnatural joins and how to keep the speaker recognisable.',
    h1='Removing Filler Words Carefully: When to Cut and When to Keep',
    answer='Remove filler words such as um and er where they distract, but keep the ones that give the speech its natural feel. Cut in small amounts, avoid joins that change the rhythm, and make sure the speaker still sounds like themselves. Over-removal makes people sound robotic and rehearsed.',
    body='''
<p>Filler words are the small sounds people make while thinking: um, er, uh, and phrases such as you know. In a transcript they can look like clutter, and many editors remove them to tighten the speech. Used carefully, that removal makes an episode easier to follow. Used heavily, it turns a real person into a polished voice that no longer sounds like the speaker, and listeners often notice the difference even if they cannot say why.</p>
<p>This post explains which fillers to cut, which to keep, how to make the joins invisible and how to keep the speaker recognisable.</p>
<h2>Why fillers are not always a problem</h2>
<p>Fillers signal thought. A short um before an answer can show that the speaker is considering the question, and it makes the answer feel more natural. Removing every filler can make an answer sound as though it was prepared in advance, which may not be what the listener expects from a conversation.</p>
<p>A filler becomes a problem when it is repeated, when it breaks the flow of an important point or when it distracts from the content.</p>
<h2>Sort the fillers</h2>
<p>Listen to the speaker and note the fillers. Group them into three kinds: the ones that distract, such as a long string of ums in a row; the ones that carry thought, such as a short pause with a filler before a key idea; and the ones that are part of the speaker’s style. Cut the first group, keep the second, and decide the third by listening.</p>
<h2>Cut in small amounts</h2>
<p>Remove fillers one at a time, not in batches. After each cut, listen to the sentence at normal speed. A filler removed with a short fade and a matched breath often disappears completely, while a batch of removals can make the speech sound jerky. If a join is noticeable, restore a little of the filler to soften it.</p>
<h2>Keep the breath and the rhythm</h2>
<p>When a filler is cut, the breath around it often needs adjusting. Keep a natural breath at the join, and make sure the rhythm of the sentence still sounds like the speaker. A sentence with its fillers removed can end up too fast, and a little pause restored at the join may fix that.</p>
<h2>Protect the speaker’s voice</h2>
<p>Each speaker has a rhythm and a style. A speaker who uses filler words as part of their conversational voice may sound unlike themselves if every filler is removed. Listeners who know the speaker will notice, and they may feel the episode is less honest. Keep enough of the style that the speaker is still recognisable.</p>
<h2>Check the transcript and the audio</h2>
<p>Automatic transcripts often show fillers clearly, which makes them easy to find. Use the transcript to locate the fillers, but always make the cut in the audio, and listen to the result. A transcript can show a filler as removed while the audio still carries a click or a change in room tone.</p>
<h2>A simple approach</h2>
<ol>
<li>Locate the fillers using the transcript, then confirm them by listening.</li>
<li>Cut the distracting clusters first, such as long strings of ums.</li>
<li>Keep the fillers that carry thought before an important idea.</li>
<li>Make each cut in small steps, with a short fade and a matched breath.</li>
<li>Listen to every edited sentence at normal speed, and restore any join that feels wrong.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Removing every filler, so the speaker sounds rehearsed.</li>
<li>Cutting fillers in batches, which makes the speech jerky.</li>
<li>Ignoring the breath and the rhythm at the join.</li>
<li>Trusting the transcript without listening to the audio.</li>
<li>Removing the speaker’s whole conversational style.</li>
</ul>
<h2>Limits</h2>
<p>How much to cut depends on the format and the audience. A tightly produced show may cut more than a relaxed conversation, and a formal interview may cut more than a casual chat. There is no fixed number of fillers to remove. The aim is clear speech that still sounds like the speaker.</p>
<h2>Fillers and the speaker’s consent</h2>
<p>Editing a speaker’s words, even lightly, should be agreed in advance. Some guests expect a tidy edit, and others want their conversational style kept. Discuss the approach before recording, and confirm it before publishing, as set out in the <a href="/tunedzy/blog/podcast-guest-consent-what-to-agree-before-recording">consent post</a> in this series.</p>
<h2>Check the result</h2>
<p>A final listen on a phone speaker shows whether the speech still flows. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the transcript side of the work, read the <a href="/tunedzy/blog/how-to-make-podcast-show-notes-from-a-transcript">show notes post</a> in this series.</p>
''',
    faq=[('Should I remove all filler words?', 'No. Remove the distracting ones and keep the fillers that carry thought or the speaker’s style.'),
         ('Why does my edit sound jerky?', 'Fillers were cut in batches. Cut one at a time, with a breath and a short fade at each join.'),
         ('Can I trust the transcript to find fillers?', 'Use it to locate them, then make every cut in the audio and listen to the result.'),
         ('Should I tell guests I removed fillers?', 'Agree the editing approach with guests before recording or publishing, especially for interviews.')])

add(slug='editing-music-to-fit-speech', cluster='evergreen-edit', kw='edit music to fit speech',
    title='Editing Music to Fit Speech: Timing Beds, Stings and Endings',
    desc='Editing music to fit speech: timing beds and stings to the words, shaping endings and keeping the music supporting the voice rather than competing with it.',
    h1='Editing Music to Fit Speech: Timing Beds, Stings and Endings',
    answer='Edit music to fit speech by timing beds to the rhythm of the talk, placing stings at the right points and shaping endings so they finish with the speech rather than fighting it. The music should support the voice, and it should change where the speech changes, not run on regardless of the words.',
    body='''
<p>Music in a podcast or video is there to support the speech. It can set a mood, mark a transition or give the listener a moment to breathe. When it is edited well, the listener barely notices it. When it is edited badly, it competes with the voice, arrives at the wrong moment or ends in an awkward place. Fitting music to speech is therefore a matter of timing, level and sensitivity to what the words are doing.</p>
<p>This post covers the three main jobs: timing a bed under speech, placing stings and shaping endings. It assumes the music is licensed for your use, which is a separate check covered in earlier posts in this series.</p>
<h2>Time the bed to the speech</h2>
<p>A bed is music that plays under speech for a longer period. Time it to the rhythm of the talk, so it rises slightly in the pauses and falls back when someone speaks. Ducking can do this automatically, but check the result by ear. The bed should never compete with the consonants or the key words, so keep it well below the voice.</p>
<h2>Place the stings</h2>
<p>A sting is a short musical phrase used to mark a change, such as the start of a segment or a dramatic moment. Place it at the exact point of change, not a moment early or late. A sting that lands on a pause feels deliberate, while one that cuts across a word feels careless. Test the placement with the voice playing, since the sting and the speech can mask each other.</p>
<h2>Shape the endings</h2>
<p>Music endings are where many edits go wrong. A fade out that ends in the middle of a phrase feels unfinished, and a sudden stop feels abrupt. Shape the ending to finish with the speech: let the music fall away as the final sentence lands, or hold a final chord for a beat after the last word. The ending should feel like a decision, not an accident.</p>
<h2>Match the energy</h2>
<p>Music and speech should share a sense of energy. A calm passage with a driving track can feel mismatched, and an excited talk with a slow bed can drag. Choose music that suits the mood of the section, and adjust its level so it fits the energy of the voice.</p>
<h2>Keep it under the voice</h2>
<p>Most music in speech should sit well below the voice, so the words are always clear. A simple test is to listen to the speech alone, then to the speech with the music. The music should add atmosphere without changing how easy the speech is to follow. If you find yourself straining to hear a word, lower the music.</p>
<h2>Check on a phone</h2>
<p>Music often sounds fuller on headphones than on a phone, where the low end is weaker and the voice can be lost. Check the balance on a phone speaker, and listen for any section where the music masks the speech. The <a href="/tunedzy/how-to-duck-music-under-a-voiceover">ducking guide</a> explains the automatic method, and the check on a phone catches what automation misses.</p>
<h2>A simple approach</h2>
<ol>
<li>Choose music that suits the mood and the energy of each section.</li>
<li>Time the bed to the rhythm of the talk, and duck it under speech.</li>
<li>Place each sting at the exact point of change, and test it with the voice.</li>
<li>Shape each ending to finish with the speech.</li>
<li>Check the whole episode on headphones and a phone speaker.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Letting the music run at the same level under every part of the talk.</li>
<li>Placing stings a fraction early or late.</li>
<li>Ending music in the middle of a phrase.</li>
<li>Choosing music whose energy does not suit the section.</li>
<li>Checking the balance only on good headphones.</li>
</ul>
<h2>Limits</h2>
<p>Music editing depends on taste and genre, and there is no single right way to time a sting or shape an ending. Some styles call for a dramatic stop, and others for a long fade. Trust your ear, and use the principles as guides.</p>
<h2>Licence the music first</h2>
<p>Editing music is only half the job. Every track must be licensed for the way it is used, including any edit. The <a href="/tunedzy/blog/podcast-intro-music-rules-and-safe-choices">intro music rules post</a> sets out the basic checks. For the voice side of the balance, the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings.</p>
''',
    faq=[('How far below the voice should the music sit?', 'Well below, so every word stays clear. Lower it further if you strain to hear the speech.'),
         ('Where should a sting go?', 'At the exact point of change, tested with the voice playing.'),
         ('How do I end music well?', 'Let it finish with the final sentence, or hold a final chord briefly. Avoid stopping mid-phrase.'),
         ('Can ducking do all the work?', 'It helps, but check the result by ear and on a phone, since automation can miss details.')])

add(slug='timeline-markers-for-audio-editing', cluster='evergreen-edit', kw='markers in audio editing',
    title='Timeline Markers for Audio Editing: Keeping Your Place in a Project',
    desc='Timeline markers for audio editing: how to use them to mark sections, problems and decisions, and how to keep a long project navigable.',
    h1='Timeline Markers for Audio Editing: Keeping Your Place in a Project',
    answer='Timeline markers label points in a recording so you can find them again quickly. Use them to mark section starts, problems to fix, decisions to revisit and points to check on export. Consistent marker names keep a long project navigable, and they save time at every stage of the edit.',
    body='''
<p>A long audio project can have hundreds of decisions, problems and points to revisit. Without a way to mark them, the editor spends time scrolling and searching, and some issues are forgotten altogether. Timeline markers solve this. A marker is a label attached to a point in the timeline, and used well it turns a long recording into a map that can be navigated in seconds.</p>
<p>This post explains what markers are good for, how to name them, how to use them through the stages of the edit and how to keep them from becoming clutter.</p>
<h2>What markers are for</h2>
<p>Markers can record almost anything you need to find again: the start of a section, a fault that needs repair, a joke to keep, a line that needs checking against the transcript, or a moment to revisit after a break. They are a memory aid, and they let you pass a project to someone else without losing the detail of your work.</p>
<p>Markers also help with export. A marker that says “check loudness here” or “re-check the music bed” reminds you of the final checks.</p>
<h2>Name them consistently</h2>
<p>Use a short, consistent naming pattern, such as a prefix for the type of marker: FIX for a fault, KEEP for a moment to keep, CHECK for a point to verify, and SEC for a section start. A consistent pattern lets you filter or scan for one type, and it makes the list of markers useful rather than a jumble of notes.</p>
<h2>Use markers through the stages</h2>
<p>During the first listen, mark the faults and the strongest moments. During the structural edit, mark the sections and the cut points. During cleaning, mark the places where processing needs checking. During the final review, mark any point that still feels wrong. Each stage adds markers, and each stage removes the ones it has dealt with.</p>
<h2>Keep them tidy</h2>
<p>Markers become useless if there are too many. Remove a marker when its job is done, and review the list at each stage. A project with thirty live markers is easier to work with than one with three hundred stale ones. Treat marker cleanup as part of the workflow.</p>
<h2>Share markers with collaborators</h2>
<p>If a project passes to a collaborator, markers are a clear way to hand over the work. A list of markers with short notes tells the next person where the problems are and why they matter. Many editors can export a marker list, which can be shared as a simple text note.</p>
<h2>Use colour and position carefully</h2>
<p>Some editors allow coloured markers. Use colour for a few clear categories, such as red for faults and green for keepers, and avoid colour for every small note. Place each marker exactly on the point it describes, since a marker a few seconds off can send you to the wrong place.</p>
<h2>A simple workflow</h2>
<ol>
<li>Mark sections and faults during the first listen.</li>
<li>Name markers with a consistent prefix and a short note.</li>
<li>Remove markers as each task is completed.</li>
<li>Add a CHECK marker for each point that needs a final listen.</li>
<li>Clear the list before export, so the final file is clean.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Naming markers inconsistently, so they cannot be scanned.</li>
<li>Leaving completed markers in the project.</li>
<li>Placing a marker a few seconds from the point it describes.</li>
<li>Using too many colours, so the colours mean nothing.</li>
<li>Forgetting to remove markers before exporting the final file.</li>
</ul>
<h2>Limits</h2>
<p>Marker features differ between editors, and some do not offer colours or exportable lists. The principle is the same across editors: a marker is a note attached to a point in time. Use the features your editor offers, and keep the naming and the cleanup habits simple.</p>
<h2>Keep the edit on track</h2>
<p>Markers keep the work organised, and organised work sounds better. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps with the CHECK markers. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the workflow that sets the order of the markers, read the <a href="/tunedzy/blog/audio-editing-workflow-for-beginners">editing workflow post</a> in this series.</p>
''',
    faq=[('What should I mark?', 'Section starts, faults, moments to keep, points to check, and decisions to revisit.'),
         ('How should I name markers?', 'With a short, consistent prefix and a brief note, so they can be scanned and filtered.'),
         ('Should I remove markers before export?', 'Yes. Clear completed markers so the final project is clean and easy to hand over.'),
         ('Do markers affect the audio?', 'No. They are notes on the timeline and are not part of the exported sound.')])

add(slug='audio-editing-shortcuts-explained', cluster='evergreen-edit', kw='audio editing shortcuts',
    title='Audio Editing Shortcuts Explained: Working Faster Without Losing Care',
    desc='Audio editing shortcuts explained: the kinds of keyboard commands that speed up editing, how to learn them in order and how to stay careful while working fast.',
    h1='Audio Editing Shortcuts Explained: Working Faster Without Losing Care',
    answer='Audio editing shortcuts speed up cutting, zooming, playback and navigation. Learn a small set in a fixed order, starting with play and stop, zoom, cut, undo and marker placement. Speed is useful, but careful listening should not be sacrificed for it, because the fastest edit is the one that does not need to be redone.',
    body='''
<p>Editing is repetitive, and a few seconds saved on each action add up to hours over a project. Keyboard shortcuts are the most direct way to save that time. They let the hands stay on the keyboard, while the eyes stay on the waveform and the ears stay on the sound. Learning shortcuts is worth the effort, but it should be done in a sensible order, and speed should never replace careful listening.</p>
<p>This post explains the kinds of shortcuts that matter most, how to learn them gradually and how to stay careful while working quickly. The exact keys differ between editors, so check your own editor’s reference for the specifics.</p>
<h2>Start with playback and navigation</h2>
<p>The first shortcuts to learn are the ones you use most: play and stop, jumping to the start and end, moving forward and back by a set amount, and looping a section. These let you listen the way you need to, without reaching for the mouse. Learn these before anything else, because they are used constantly.</p>
<h2>Learn zoom</h2>
<p>Zooming in and out is essential for precise work. Learn the shortcut for zooming to the selection and for returning to the full view. Zooming to a join or a click is how you make small, accurate changes, so it is worth practising until it feels natural.</p>
<h2>Learn the cut and the selection</h2>
<p>Cutting, copying, pasting and selecting are the core of the edit. Learn the shortcut for splitting a clip at the playhead, for deleting a selection and for selecting the next region. These let you work through a recording quickly, cut by cut.</p>
<h2>Learn undo and redo</h2>
<p>Undo is the most important shortcut of all. Learn it early, and use it freely while experimenting. A fast editor who undoes mistakes quickly makes more careful decisions than one who is afraid to try a change. Make sure you know how far the undo history goes in your editor.</p>
<h2>Learn markers</h2>
<p>Placing a marker with a single key press is one of the most useful habits. As you listen, you can mark problems and keepers without stopping, which speeds up the first listen and the structural edit. The <a href="/tunedzy/blog/timeline-markers-for-audio-editing">markers post</a> in this series explains how to use them well.</p>
<h2>Build the set in order</h2>
<ol>
<li>Learn play, stop and navigation first.</li>
<li>Add zoom, so you can work precisely.</li>
<li>Add cut, select and delete for the structural work.</li>
<li>Add undo and redo, and use them freely.</li>
<li>Add markers, then any other shortcuts you use often.</li>
</ol>
<h2>Stay careful while working fast</h2>
<p>Speed is a means to an end, and the end is a clean, well-judged recording. A fast cut that clips a consonant or leaves a click has to be fixed later, and the time saved disappears. Slow down at the joins, listen to the result at normal speed, and use the shortcuts to make the work smoother rather than rushed.</p>
<h2>Common mistakes</h2>
<ul>
<li>Learning many shortcuts at once, and remembering none.</li>
<li>Using fast cuts without listening to the join.</li>
<li>Being afraid to undo, which leads to over-cautious edits.</li>
<li>Working at a single zoom level throughout.</li>
<li>Relying on shortcuts without checking the final result by ear.</li>
</ul>
<h2>Limits</h2>
<p>Shortcuts differ between editors, and some features have no default key. Check your editor’s reference, and consider customising the keys you use most. The principles are the same across editors, and the speed comes from practice rather than from memorising a long list.</p>
<h2>Check the result carefully</h2>
<p>Speed should not reduce the quality of the final file. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the order in which these actions belong, read the <a href="/tunedzy/blog/audio-editing-workflow-for-beginners">editing workflow post</a> in this series.</p>
''',
    faq=[('Which shortcuts should I learn first?', 'Play, stop and navigation, then zoom, cut and undo.'),
         ('Are shortcuts the same in every editor?', 'No. The keys differ, but the actions are similar. Check your editor’s reference.'),
         ('Does working fast reduce quality?', 'It can, if joins are not listened to. Slow down at the joins and check the result.'),
         ('Should I customise my shortcuts?', 'Yes, for the actions you use most often, once you know the defaults.')])

add(slug='non-destructive-editing-explained', cluster='evergreen-edit', kw='non destructive audio editing',
    title='Non-Destructive Audio Editing Explained: Keeping the Original Intact',
    desc='Non-destructive audio editing explained: how edits can be changed later without damaging the original file, and why this matters for safe, flexible work.',
    h1='Non-Destructive Audio Editing Explained: Keeping the Original Intact',
    answer='Non-destructive editing records changes as instructions that sit on top of the original audio, so the original file is never overwritten and any edit can be changed or removed later. It keeps work flexible and safe, and it lets you revisit decisions without losing the raw material.',
    body='''
<p>Some editing methods change the audio file itself, so each edit permanently alters the recording. Others record the edits as a list of instructions that the software applies when the file is played or exported. The second approach is called non-destructive editing, and it is one of the most important ideas for safe, flexible work. It protects the original, makes experimentation cheap and lets you change decisions after the fact.</p>
<p>This post explains the difference between destructive and non-destructive editing, the advantages of the second approach, its limits and how to work in that way safely.</p>
<h2>What destructive editing means</h2>
<p>In destructive editing, each change is written into the audio file. Cutting a section removes it from the file, and applying an effect alters the sound permanently. The original is lost unless a separate copy was saved. Destructive editing can be fast and simple, but it leaves no easy route back if a decision turns out to be wrong.</p>
<h2>What non-destructive editing means</h2>
<p>In non-destructive editing, the original file stays unchanged, and the software stores the edits as instructions: where to cut, what effect to apply, how loud to make each part. The instructions are applied when the file is played or exported. Changing an instruction changes the result, and the original is always available underneath.</p>
<h2>The advantages</h2>
<ul>
<li>The original is never damaged, so a mistake can always be undone.</li>
<li>Edits can be changed or removed at any stage.</li>
<li>Experiments are cheap, because a trial does not commit the file.</li>
<li>The project can be re-exported for a different platform without losing work.</li>
<li>A collaborator can see and change the decisions, not just the result.</li>
</ul>
<h2>The limits</h2>
<p>Non-destructive editing needs more storage and more processing power, because the software must apply the instructions on the fly. Large projects with many effects can slow down. It also depends on the project file, so the project must be kept safe as well as the audio. A lost project file can mean a lost edit, even when the original audio survives.</p>
<h2>Working safely</h2>
<ol>
<li>Keep the original audio in a separate folder, and never overwrite it.</li>
<li>Save the project file regularly, and keep backups of it.</li>
<li>Export a finished version, and keep it apart from the working project.</li>
<li>Name the project and the exports clearly, with dates and versions.</li>
<li>Clean up old exports and trial versions when the project is complete.</li>
</ol>
<h2>When destructive editing still makes sense</h2>
<p>Some tasks are simpler when applied destructively, such as repairing a click in a single file that will never change. Some editors offer both approaches, and the choice depends on the job. The safe habit is to keep the original, whichever method you use for the change.</p>
<h2>Common mistakes</h2>
<ul>
<li>Overwriting the original file with an edit, and losing it.</li>
<li>Losing the project file, and with it all the edits.</li>
<li>Keeping a huge number of old exports, which fills the storage.</li>
<li>Assuming the export is the same as the project, when it may not be.</li>
<li>Forgetting that a project depends on the original files it points to.</li>
</ul>
<h2>Limits</h2>
<p>The benefits of non-destructive editing depend on good file management. A project with a missing original cannot be rebuilt, and a project with a corrupted file may lose its edits. Treat the project and the originals as a single unit, and back them up together.</p>
<h2>Keep the original safe</h2>
<p>The original is the foundation of any safe edit. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the backup routine that protects both the originals and the project, read the <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup post</a> in this series.</p>
''',
    faq=[('Does non-destructive editing change the original?', 'No. The original stays unchanged, and the edits are applied on top of it.'),
         ('Why would I still edit destructively?', 'Some simple repairs are quicker that way, if the file will never change.'),
         ('What is the biggest risk?', 'Losing the project file, which holds the edits, or the original files it points to.'),
         ('Does it use more storage?', 'Often yes, because the original and the project both need to be kept.')])

add(slug='audio-quality-check-before-publishing', cluster='evergreen-edit', kw='audio quality check before publishing',
    title='Audio Quality Check Before Publishing: A Checklist for Episodes',
    desc='Audio quality check before publishing: a checklist for the finished episode covering levels, clipping, noise, joins, music, metadata and playback on real devices.',
    h1='Audio Quality Check Before Publishing: A Checklist for Episodes',
    answer='Before publishing, check the finished episode on real devices: the levels and loudness of the export, clipping and true peak, noise in the quiet pauses, the joins and music, the metadata and the first and last minute. A short, consistent check catches the mistakes that are easy to miss after many hours of editing.',
    body='''
<p>After hours of editing, the ear is tired, the details blur and the temptation is to publish. A final quality check is the last chance to catch the mistakes that editing hides: a click at a join, a music bed that masks a word, a loudness that does not match the rest of the show, or a title with a typo. A short, consistent check, run the same way for every episode, catches most of these problems before listeners hear them.</p>
<p>This post sets out the checklist, explains each check and suggests how to run it without losing a day. It is written for podcasters and video makers who publish audio regularly.</p>
<h2>Check the export, not the project</h2>
<p>The project may sound fine while the export does not. Check the exported file, the one you will publish. Play it in a media player, not in the editor, so you hear what listeners will hear. A change in format or sample rate can alter the sound in small but noticeable ways.</p>
<h2>Check the levels and loudness</h2>
<p>Measure the loudness and true peak of the exported file, and compare them with your target. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows both figures for a finished file. A file that is far from the target should be re-exported, and a file with a true peak near full scale should be checked for clipping.</p>
<h2>Check for clipping and distortion</h2>
<p>Listen for crackle, harshness or flattened peaks on the loudest sounds. Look at the waveform for flat tops, which show clipping. If you find any, re-export with lower levels or a gentler limiter, rather than publishing a distorted file.</p>
<h2>Check the quiet pauses</h2>
<p>The quiet pauses reveal noise, hum, hiss and any sudden change in room tone. Listen to several pauses on headphones, and turn the volume up slightly to hear the background. A noise that is audible in a pause will be heard by listeners in quiet places, so fix it or accept it deliberately.</p>
<h2>Check the joins</h2>
<p>Play the join points at normal speed. Listen for clicks, level jumps and changes in room sound. A join that is obvious at normal speed will be obvious to listeners, so fix any that stand out.</p>
<h2>Check the music and effects</h2>
<p>Check the music balance under speech, the stings and the endings. Make sure the music never masks a word, and that every element is licensed for the use. A music bed that is too loud on a phone speaker is a common problem, so check the balance there too.</p>
<h2>Check the start and the ending</h2>
<p>The first minute decides whether many listeners stay, and the last minute decides how they feel about the episode. Listen to both carefully. Check the intro level, the first words, the final sentence and the closing music or sign-off.</p>
<h2>Check the metadata</h2>
<p>Check the title, the description, the chapter titles, the cover art and any tags or credits. A wrong name or a missing link is easy to publish and hard to recall. Read the description aloud once, and check every link.</p>
<h2>Listen on real devices</h2>
<p>Finally, listen on the devices your audience uses: a phone speaker, earbuds and, if possible, a car. The episode should be clear and comfortable on each. If something works only on headphones, fix it before publishing.</p>
<h2>A short checklist</h2>
<ol>
<li>Play the exported file, not the project.</li>
<li>Check loudness and true peak against your target.</li>
<li>Listen for clipping, distortion and flattened peaks.</li>
<li>Listen to the quiet pauses for noise and hum.</li>
<li>Play the joins at normal speed.</li>
<li>Check the music balance and the licences.</li>
<li>Listen to the first and last minute.</li>
<li>Read the metadata and check every link.</li>
<li>Listen on a phone speaker and earbuds before publishing.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Publishing from the project rather than the export.</li>
<li>Checking only the first minute and assuming the rest is fine.</li>
<li>Skipping the metadata, and publishing a wrong title or link.</li>
<li>Relying on headphones alone.</li>
<li>Rushing the check because the episode is late.</li>
</ul>
<h2>Limits</h2>
<p>The checklist catches common problems, but it cannot guarantee a perfect episode. Some issues appear only on specific devices, and some are a matter of taste. Use the checklist to remove the obvious mistakes, then trust your judgement about the rest.</p>
<h2>Check the sound one more time</h2>
<p>A final check is a habit that protects the show. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> confirms the loudness and true peak of the finished file, and the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. For the editing steps that come before the check, read the <a href="/tunedzy/blog/audio-editing-workflow-for-beginners">editing workflow post</a> in this series.</p>
''',
    faq=[('Should I check the project or the export?', 'The export, because it is the file listeners will hear.'),
         ('How long should the check take?', 'Around fifteen to thirty minutes, once the habit is set. It saves far more time than it costs.'),
         ('What is the most commonly missed problem?', 'A wrong title, description or link, which is easy to publish and hard to recall.'),
         ('Is headphones-only checking enough?', 'No. Check on a phone speaker and earbuds, since many listeners use them.')])
