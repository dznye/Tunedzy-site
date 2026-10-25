"""Blog posts, batch 21: vocal technique and recording for singers (evergreen). Merged into content_blog.py.
Technique is described in general terms; voice health points defer to a doctor or voice teacher.
No invented statistics. Funnel: each post ends with a link to Tunedzy Go and to the matching free tool."""

CLUSTERS = {
    'evergreen-music-vocals': dict(tool='karaoke-autotune', label='Vocal technique at home', tool_name='Karaoke Autotune'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='pitch-correction-explained-for-singers', cluster='evergreen-music-vocals', kw='how does pitch correction work',
    title='How Pitch Correction Works and What It Means for Singers',
    desc='How pitch correction works for singers: what the tools detect and move, the audible side effects, and how to use correction without losing your own voice.',
    h1='How Pitch Correction Works and What It Means for Singers',
    answer='Pitch correction detects the pitch of each note in a vocal and moves it toward a target note, usually in a set scale. It can make small errors inaudible, but heavy settings leave artefacts and a robotic sound. Singers get the most from it by learning to sing in tune first, then using correction lightly as a finishing tool.',
    body='''
<p>Pitch correction has become part of almost every commercial vocal, and many singers wonder what it actually does. The short answer is that it listens to the pitch of each note, decides where that note should be, and shifts it there. The longer answer involves choices about speed, scale and strength, and each choice changes how the voice sounds. Understanding the process helps you use correction with judgement rather than as a default.</p>
<p>This post explains how pitch detection works in plain terms, what the common settings mean, the artefacts to listen for and how a singer can use correction without losing the character of their voice.</p>
<h2>What the tool listens for</h2>
<p>A pitch correction tool analyses the voice to find its fundamental frequency, the main pitch of each note. It then compares that pitch with a target, which may be a chromatic scale, a key or a set of notes chosen by the user. The tool works best on clear, single notes, and it struggles with breathy sounds, vibrato and fast runs, because the pitch is changing as it listens.</p>
<p>Detection is the first place where errors can enter. A tool that misreads a note will move it to the wrong target, which is why a clean recording gives better results.</p>
<h2>What it does to the note</h2>
<p>Once the target is chosen, the tool shifts the note toward it. The speed of that shift is one of the most important settings. A fast shift, sometimes called an instant correction, gives the robotic effect that many listeners associate with heavy correction. A slow shift preserves more of the natural movement of the voice, and it is far less noticeable.</p>
<p>The tool may also change the formants, the resonances that give a voice its character. Some tools preserve formants, and some do not. Without formant preservation, a correction can make a voice sound thinner or more like a different singer.</p>
<h2>Settings that matter</h2>
<ul>
<li><strong>Scale or key:</strong> the set of notes the tool is allowed to move to. Choosing the correct key stops the tool from moving a correct note to a wrong one.</li>
<li><strong>Speed:</strong> how quickly the correction happens. Slower is more natural.</li>
<li><strong>Strength:</strong> how much of the error is corrected. Partial correction often sounds better than full correction.</li>
<li><strong>Formant handling:</strong> whether the character of the voice is kept during the shift.</li>
<li><strong>Vibrato handling:</strong> whether natural vibrato is kept or flattened.</li>
</ul>
<h2>Artefacts to listen for</h2>
<p>The most common artefacts are a robotic tone on sustained notes, a warbling or chirping sound during slides, a thinning of the voice and a loss of vibrato. Each one tells you something about the settings. A robotic sound usually means the speed is too fast or the strength too high. A warble often means the detection is struggling with a fast change.</p>
<h2>Singing in tune first</h2>
<p>Correction is a finishing tool, not a substitute for good pitch. A singer who depends on it may find that their live pitch suffers, and that their ear does not develop. Practise with a reference note, record yourself, and listen back to hear where you drift. Once the pitch is secure, correction can tidy the remaining small errors without changing the sound.</p>
<h2>A light approach</h2>
<ol>
<li>Choose the correct key before you start.</li>
<li>Set a slow speed and partial strength.</li>
<li>Keep formants and natural vibrato where the tool allows it.</li>
<li>Correct only the notes that are clearly off, not every small wobble.</li>
<li>Listen on headphones and a phone, and compare with the uncorrected take.</li>
</ol>
<h2>Correction in performance and in the studio</h2>
<p>Correction used live is a different matter from correction used in the studio. A live singer who hears a corrected version in their monitors can drift toward the correction, relying on it rather than on their own ear. In the studio, the singer can listen back, judge the result and decide where help is needed. For that reason, many singers keep correction out of the live monitors and use it only on recordings they have reviewed.</p>
<p>If you do use correction on stage, practise without it first, so the pitch comes from your ear and the tool is a safety net rather than a crutch.</p>
<p>Some singers also find that correction changes how they breathe and place notes. After a long period of heavy correction, a return to unprocessed singing can feel exposed. That is a sign to practise the unprocessed voice more, not a reason to avoid it.</p>
<h2>Limits</h2>
<p>Pitch correction tools differ in their methods, and their results depend on the voice and the recording. The principles above apply broadly, but no setting suits every singer. Some styles call for a very obvious effect, and that is a choice rather than a fault. Judge the result by how it serves the song.</p>
<h2>Check the key before you correct</h2>
<p>The correct key is the first setting to get right. The <a href="/tunedzy/tools/song-key-finder">Song Key Finder</a> reports the key of a song, and the <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets singers practise with live autotune and record the mix. For a related guide on singing in tune without correction, read the <a href="/tunedzy/blog/how-to-practise-singing-in-tune-at-home">practice post</a> in this series.</p>
''',
    faq=[('Does pitch correction always sound robotic?', 'Not if it is set slowly and partially. Heavy settings cause the robotic effect.'),
         ('Why does my voice sound thin after correction?', 'The formants may not be preserved. Choose a setting that keeps the character of the voice.'),
         ('Should I learn to sing in tune first?', 'Yes. Correction works best as a finishing tool on a voice that is already close.'),
         ('What key should I choose?', 'The key of the song or the key you are singing in. Check it before you start.')])

add(slug='how-to-record-harmonies-at-home', cluster='evergreen-music-vocals', kw='how to record harmonies at home',
    title='How to Record Harmonies at Home: A Practical Guide',
    desc='How to record harmonies at home: choosing the harmony part, recording each line separately, keeping the pitch and timing together and balancing the stack.',
    h1='How to Record Harmonies at Home: A Practical Guide',
    answer='Record harmonies by building them one line at a time: start with a clear lead, then record each harmony part separately, listening to the lead as you go. Keep the parts balanced and the timing tight, and use a simple reference to keep the pitch steady across the stack.',
    body='''
<p>Harmonies make a vocal sound full and emotional, and they are within reach for a singer working alone. The method is simple: record a lead, then add the other parts one at a time, each matched to the lead. The difficulty is in the detail, because harmonies depend on tight pitch and timing, and small errors become obvious when the parts are stacked together.</p>
<p>This guide covers choosing the harmony, recording each line, keeping the pitch and timing steady and balancing the final stack. It is written for singers who want to produce harmony parts at home.</p>
<h2>Start with a clear lead</h2>
<p>Every harmony begins with a lead that is clean, in tune and in time. Record the lead first, with the best performance you can manage, and check it closely before adding anything. A weak lead makes every harmony harder, because the other parts must match its mistakes or fight them.</p>
<p>Keep the lead as the reference for the whole session. Listen to it on headphones each time you record a harmony, so you always know where the melody sits.</p>
<h2>Choose the harmony</h2>
<p>The most common harmony is a third above or below the lead, because it blends closely. A fifth adds width, and an octave doubles the lead without changing the colour much. Find the harmony that suits the song by singing the lead with the other note, and listening to how the two sit together. The choice depends on the chords, so check the key before you choose.</p>
<p>Start simple. Two parts are easier to get right than four, and a good two-part harmony often sounds more moving than a crowded stack.</p>
<h2>Record each line separately</h2>
<p>Record each harmony part on its own track, listening to the lead and any parts already recorded. Use headphones so the recording does not bleed into the microphone. Sing the part slowly the first time, to learn the notes, then at performance speed. Record several takes, and choose the best section by section.</p>
<h2>Keep the pitch steady</h2>
<p>Harmony pitch is more demanding than melody pitch, because the notes must sit at precise intervals. A reference note helps. Play the harmony note on a keyboard or a tuning app before each take, and sing it to match. Check each take by listening to the two parts together, and listen for the point where the harmony sounds slightly rough, since that usually means one part is out of tune.</p>
<h2>Keep the timing tight</h2>
<p>Harmony parts must start and end together, especially on consonants and short notes. Count the phrase in your head, and line up the attacks with the lead. A harmony that comes in a fraction late can sound loose even when the pitch is right. Use the waveform to check the start of each phrase, and move any part that is clearly out of line.</p>
<h2>Balance the stack</h2>
<p>Harmony parts should sit slightly below the lead, so the melody stays clear. Set each track’s level so the lead leads, and the harmonies add colour. Panning the harmonies gently to the sides can add width, but keep the lead in the centre. Check the balance on a phone speaker, where harmonies can disappear if they are too quiet.</p>
<h2>Listen as a whole</h2>
<p>Once the stack is built, listen to it from start to finish, without stopping. Harmony problems are often clearer in the flow of the song than in short sections. Make a note of any moment that feels wrong, then go back to that part and record a fix.</p>
<h2>Use the lead as a guide for timbre</h2>
<p>Harmony parts sound best when their tone matches the lead. A bright lead with a dark harmony can sound like two different singers, even when the notes are right. Listen for the colour of the voice as well as the pitch, and adjust the way you sing the harmony: brighter or darker, more or less breathy. A harmony that blends in tone will sit inside the lead, rather than sitting beside it.</p>
<p>Record a short test of the lead and the harmony together, then listen with your eyes closed. If the harmony draws attention to itself, adjust the tone before recording the rest of the parts.</p>
<h2>Limits</h2>
<p>Harmony recording takes patience, and it is easy to fall into endless retakes. Set a time limit for each part, and accept that a live performance will always differ from a stacked studio version. The aim is a pleasing, honest harmony, not a perfect choir.</p>
<h2>Keep the harmony clean</h2>
<p>A clean recording of each part makes the stack easier to balance. The <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets you sing along with live autotune and record the mix, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the wider vocal chain, read the <a href="/tunedzy/blog/how-to-double-track-vocals-and-ad-libs">double-tracking post</a> in this series.</p>
''',
    faq=[('Should I start with two parts or four?', 'Two parts. They are easier to get right and often sound better.'),
         ('Which harmony interval is easiest?', 'A third is common because it blends closely. Choose by how the chords sit.'),
         ('Why do my harmonies sound rough?', 'One part is slightly out of tune or out of time. Check each part against the lead.'),
         ('Do I need a second person to sing?', 'No. You can record each part yourself, one track at a time.')])

add(slug='vocal-comping-explained', cluster='evergreen-music-vocals', kw='vocal comping',
    title='Vocal Comping Explained: Building One Great Take From Many',
    desc='Vocal comping explained: how a singer or producer builds one great vocal from several takes, the choices involved and how to keep the performance feeling whole.',
    h1='Vocal Comping Explained: Building One Great Take From Many',
    answer='Comping is the process of combining the best sections of several vocal takes into one finished performance. It lets you keep the strongest phrases from each take. Good comping keeps the breath, the energy and the continuity of the performance, and it avoids joins that a listener can hear.',
    body='''
<p>Most finished vocals are not a single take. The singer records several passes of a song, and the producer or the singer picks the best section from each, joining them into one complete performance. This process is called comping, short for composite, and it is one of the most important skills in vocal recording. A well-comped vocal can sound like one continuous, inspired performance, even when it was built from many takes.</p>
<p>This post explains the process, the choices involved, the common mistakes and how to keep the vocal feeling alive.</p>
<h2>Why comp at all</h2>
<p>No singer delivers every phrase perfectly in one take. One take may have the best chorus but a weak verse, while another has a strong bridge with a flat note at the end. Comping lets you use the strongest moment from each, so the final vocal is better than any single take. It also reduces the pressure on a singer to get everything right in one go.</p>
<p>The aim is not to remove all the variation between takes. It is to choose the variation that serves the song.</p>
<h2>Prepare the takes</h2>
<p>Name each take clearly, with its number and the section it covers, and keep the takes lined up on the same timeline. Listen through every take before you start, and make notes on the strongest moments. A quick survey saves hours later, because you will know which takes to listen to closely for each section.</p>
<h2>Choose section by section</h2>
<p>Work through the song in sections: verse, chorus, bridge and so on. For each section, compare the takes and choose the one with the best feel, the cleanest pitch and the most natural breath. Sometimes the best option is a single phrase from one take, and sometimes a whole section from another. Judge the performance first, and the detail second.</p>
<h2>Keep the breath and the energy</h2>
<p>Breaths are part of the performance, and they must sit naturally between phrases. A join that cuts a breath short can make the vocal sound robotic. When you join two takes, keep a natural breath at the join, even if it comes from a different take. Listen for the energy as well: a join that changes the intensity of the delivery is obvious, even when the pitch matches.</p>
<h2>Make the joins invisible</h2>
<p>A good join is one the listener never notices. Cut on a consonant or a pause, not in the middle of a vowel. Match the level and the room tone on each side. A short crossfade can smooth the change. Listen to each join at normal speed and at a slower speed, to check for clicks, level jumps and any change in tone.</p>
<h2>Watch the pitch and timing</h2>
<p>If the takes differ in pitch or timing, a join can show it. Check the pitch of each phrase before joining, and align the timing carefully. A small pitch difference between takes is often hidden by the natural movement of the voice, but a large difference will stand out. Correct only what is needed, and keep the correction light.</p>
<h2>Keep the performance whole</h2>
<p>A vocal built from many takes can sound stitched together if the emotional arc is lost. Listen to the whole comped vocal from start to finish. Ask whether the energy builds in the right places, whether the chorus lands and whether the ending feels earned. If not, revisit the choices and aim for a more continuous performance.</p>
<h2>Common mistakes</h2>
<ul>
<li>Joining takes at every small error, which makes the vocal sound chopped.</li>
<li>Ignoring the breath and the energy when choosing sections.</li>
<li>Matching the pitch but not the tone or the room.</li>
<li>Comping too many takes, so the vocal loses its sense of one performance.</li>
<li>Forgetting to listen to the whole vocal after the joins are made.</li>
</ul>
<h2>Document the choices</h2>
<p>When a vocal is built from many takes, the choices are easy to forget. Keep a simple record of which take each section came from, and any corrections or edits made. The record makes it possible to rebuild the vocal if a client asks for a change, and it helps when a second person needs to continue the work. A comped vocal without a record is hard to revisit, and it can end up being rebuilt from scratch.</p>
<p>Save the composite as a separate version, and keep the original takes untouched. If a later change is worse, you can return to the earlier composite rather than comping the whole song again.</p>
<h2>Limits</h2>
<p>Comping is a craft, and it takes practice to hear joins that others will miss. Some styles accept more visible joins than others, and some performances are best left as single takes. The aim is a vocal that serves the song, not a perfect composite.</p>
<h2>Start with a clean set of takes</h2>
<p>Clean takes make comping easier. The <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets you sing along with live autotune and record the mix, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the editing side of the same work, read the <a href="/tunedzy/blog/how-to-sync-audio-and-video-in-an-editor">sync post</a> in this series, which covers aligning files on a timeline.</p>
''',
    faq=[('How many takes should I record?', 'Enough to find strong sections, usually several per section. Too many can make the choice harder.'),
         ('Should I keep the breaths from different takes?', 'Keep a natural breath at each join, even if it comes from another take.'),
         ('Can a comped vocal sound live?', 'Yes, if the energy and the breath are kept together and the joins are invisible.'),
         ('Do I need expensive software to comp?', 'No. Most editing software can align, cut and crossfade the takes.')])

add(slug='vibrato-explained-for-singers', cluster='evergreen-music-vocals', kw='what is vibrato',
    title='What Is Vibrato? A Plain Explanation for Singers',
    desc='What is vibrato? A plain explanation for singers: what the regular pitch and volume movement is, how it develops, why it is not a fault and how to practise it.',
    h1='What Is Vibrato? A Plain Explanation for Singers',
    answer='Vibrato is a regular, gentle variation in pitch and volume on a sustained note. It usually sits at about five to seven cycles per second and adds warmth and expression. It develops naturally with relaxed breath and support, and it should not be forced. A steady, unforced vibrato is a sign of a healthy voice, not a flaw to remove.',
    body='''
<p>Vibrato is one of the most recognisable features of a singing voice, and it is often misunderstood. Some singers try to create it with effort, others try to remove it because they think it is a fault, and listeners sometimes hear it as a sign of skill without knowing why. In reality, vibrato is a natural pattern of small pitch and volume changes, and it develops most easily when the voice is relaxed and supported.</p>
<p>This post explains what vibrato is, how it develops, why a steady vibrato is a healthy sign and how to practise it safely.</p>
<h2>What vibrato is</h2>
<p>Vibrato is a regular oscillation in pitch, and usually in loudness too, on a sustained note. The pitch rises and falls slightly around the centre of the note, several times each second. In a healthy voice, the rate is fairly steady and the depth is small, so the note still sounds clear and centred. The effect adds warmth and expression, and it is a major part of the sound of many singing styles.</p>
<p>The rate is commonly described as around five to seven cycles per second in a trained voice. Individual voices vary, and the exact rate matters less than whether the movement is smooth and relaxed.</p>
<h2>How it develops</h2>
<p>Vibrato usually develops with practice, as the voice finds its balance of breath, support and resonance. Many singers notice it appearing after months or years of relaxed singing, rather than through deliberate effort. It is a result of a free, stable voice, not a technique to be forced onto a note.</p>
<p>Some singers have a naturally fast or slow vibrato, and some have very little. A vibrato that is not yet developed is not a problem in itself.</p>
<h2>Why a steady vibrato is healthy</h2>
<p>A steady vibrato suggests that the voice is free of excessive tension, and that the breath is supporting the sound evenly. A wobble, by contrast, is usually a sign of effort or unsteady support, and it can sound uncontrolled. Working to make the vibrato steady and relaxed is more useful than trying to make it bigger or smaller.</p>
<p>Listen for the difference between a relaxed vibrato and a forced one. The relaxed version sounds easy and warm. The forced version often sounds tight, pushed or wavering.</p>
<h2>Trying to force it</h2>
<p>Forcing vibrato, by pulsing the breath or pushing the throat, can strain the voice and create the very wobble that singers want to avoid. If you find yourself working hard to create the movement, stop and return to relaxed breath and simple sustained notes. A teacher can help you find the difference, and can check that the voice is healthy.</p>
<h2>Practising safely</h2>
<ol>
<li>Warm up gently, with breath and simple sustained notes.</li>
<li>Sing a comfortable note at a moderate volume, and let it sit.</li>
<li>Listen for a smooth, even movement rather than a push.</li>
<li>Stop if the note feels tight, sore or effortful.</li>
<li>Record the note, and compare later takes to notice progress.</li>
</ol>
<h2>When to ask for help</h2>
<p>If vibrato is very wide, very fast or very uneven, or if the voice feels strained, ask a voice teacher to listen. Persistent hoarseness, pain or a sudden change in the voice should be checked by a doctor. Healthy singing should feel free and comfortable.</p>
<h2>Vibrato on recordings</h2>
<p>Pitch correction tools can flatten vibrato or make it sound unnatural. If you use correction, check that the natural movement survives, and keep the vibrato in the final take. A recording that keeps the vibrato sounds warmer and more human than one that has been flattened.</p>
<h2>Vibrato across genres</h2>
<p>Different styles use vibrato differently. Classical singing often favours a steady, even movement with a controlled depth. Popular and soul singing may use a wider or more expressive vibrato, sometimes with a slight delay before it starts. Folk and country singers often prefer very little vibrato, letting the plain tone carry the emotion. None of these is right or wrong; each suits its music.</p>
<p>Listen to singers in the style you want to sing, and notice when the vibrato starts, how wide it is and when it stops. Imitating the placement of the vibrato, rather than its exact sound, is often the most useful step.</p>
<h2>Limits</h2>
<p>Vibrato varies by style, voice type and individual. Some styles use very little, and some use a great deal. The description here is general. For specific technique, a qualified teacher is the best guide, and voice health should always come first.</p>
<h2>Listen and record</h2>
<p>Recording a sustained note is one of the best ways to hear your vibrato. The <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets you sing along with live autotune and record the mix, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the warm-up that prepares the voice, read the <a href="/tunedzy/blog/how-to-warm-up-your-voice-before-singing">warm-up post</a> in this series.</p>
''',
    faq=[('Is vibrato a sign of good singing?', 'A steady, relaxed vibrato is a healthy sign. A wobble or a forced vibrato is worth checking.'),
         ('Can I learn to add vibrato?', 'It develops with relaxed singing. Forcing it can strain the voice, so work with a teacher.'),
         ('Should I remove my vibrato for recordings?', 'Not usually. Natural vibrato keeps the sound warm, so keep it when you can.'),
         ('When should I see a doctor?', 'If the voice is hoarse for more than a few days, painful, or changes suddenly.')])

add(slug='falsetto-vs-head-voice-explained', cluster='evergreen-music-vocals', kw='falsetto vs head voice',
    title='Falsetto vs Head Voice: What Singers Need to Know',
    desc='Falsetto vs head voice explained for singers: how the two registers differ, why the terms are often confused and how to find and blend them safely.',
    h1='Falsetto vs Head Voice: What Singers Need to Know',
    answer='Falsetto and head voice are different high registers. Falsetto is lighter and airier, with less of the vocal folds closing fully, while head voice is a fuller, resonant high register. The terms are often confused in popular use, and singers benefit from learning to tell them apart by feel and sound before blending them.',
    body='''
<p>Singers often use the words falsetto and head voice as if they meant the same thing. They do not, and the confusion can make practice harder. Both describe ways of singing above the comfortable middle of the voice, and both are used widely across styles. Understanding how they differ helps you find each one, blend them smoothly and avoid strain when you move between them.</p>
<p>This post explains the difference in simple terms, how each feels, why the labels vary and how to practise safely. It is general information, and a voice teacher can help with specific technique.</p>
<h2>What falsetto is</h2>
<p>Falsetto is a light, airy register in which the vocal folds stretch and vibrate with a gap, so less air is blocked and more air escapes with the sound. The result is a soft, pure tone with less volume and less carrying power than a full voice. Many singers use falsetto for the highest notes, for a gentle quality, or for stylistic effect.</p>
<p>The sound is often described as breathy, flute-like or ethereal. Listeners recognise it quickly, because it has a distinct character.</p>
<h2>What head voice is</h2>
<p>Head voice is a resonant high register, in which the vocal folds are stretched but still close fully, and the sound is supported by the breath and the resonance of the head and upper chest. It is usually fuller than falsetto, with more presence and volume. Many singers find head voice to be the most natural way to reach the upper middle range.</p>
<p>Head voice is often described as feeling light but connected, with a sense of resonance in the head rather than in the chest.</p>
<h2>Why the terms are confused</h2>
<p>The terms are used differently in different traditions, and some teachers use them interchangeably. Popular music often uses falsetto for any high, light sound, and some singers describe a full high note as falsetto even when it is head voice. The result is that a singer who reads one source may have a different understanding from one who reads another.</p>
<p>The best guide is the sound and the feel, rather than the label alone.</p>
<h2>How to tell them apart</h2>
<ul>
<li>Falsetto is lighter, airier and softer, with less carrying power.</li>
<li>Head voice is fuller and more resonant, with more support and volume.</li>
<li>Falsetto often feels breathy at the start of a note, while head voice feels connected.</li>
<li>Head voice usually sits closer to the chest voice in quality, with a smooth transition.</li>
</ul>
<h2>Blending the two</h2>
<p>Many singers want to move smoothly between their chest voice, their head voice and their falsetto. A smooth blend comes from relaxed support and gradual practice, rather than sudden changes. Practise slides between notes at a gentle volume, and listen for the point where the sound changes. Aim for a transition that is hardly noticeable.</p>
<h2>Practising safely</h2>
<ol>
<li>Warm up thoroughly before attempting high notes.</li>
<li>Start with gentle slides in the upper range, at a moderate volume.</li>
<li>Stop if the sound feels tight, pinched or painful.</li>
<li>Record the practice, and compare it over several weeks.</li>
<li>Work with a teacher if the transition feels rough or uncomfortable.</li>
</ol>
<h2>Teachers and the labels</h2>
<p>Voice teachers use the terms in different ways, and a good teacher will explain what they mean by each one. Some teachers describe registers by how the vocal folds behave, others by how the sound feels, and others by the resonance. A student who asks which term a teacher uses, and what it means for their practice, will get more from the lesson than one who simply adopts a label.</p>
<p>When you work on the transition between registers, record your practice and listen back. The recording shows whether the change is smooth, and it gives a teacher something concrete to discuss.</p>
<p>Be cautious with online descriptions that promise a quick route to a new register. Many of them describe a result without explaining how the voice reaches it, and an effort to force a register can cause strain. A slow, gradual approach with a teacher is safer and usually more successful over time, even though it can feel slower at first. Progress is often easiest to see on recordings made over several weeks, so keep the first recording as a reference point.</p>
<h2>Limits</h2>
<p>The labels are useful, but they are not fixed categories, and many voices blend the two in ways that defy neat description. The aim is a voice that moves smoothly and comfortably, whatever the label. A voice teacher can help you find your own balance.</p>
<h2>Record to hear the difference</h2>
<p>Recording yourself is one of the best ways to hear the registers. The <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets you sing along with live autotune and record the mix, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the high-note technique in more detail, read the <a href="/tunedzy/blog/how-to-sing-high-notes-without-straining">high notes post</a> in this series.</p>
''',
    faq=[('Is falsetto the same as head voice?', 'No. Falsetto is lighter and airier, while head voice is fuller and more resonant.'),
         ('Why do people use the terms differently?', 'Traditions and genres vary. Use the sound and the feel as your guide.'),
         ('How do I blend registers?', 'Practise gentle slides at moderate volume, with relaxed support and a teacher if needed.'),
         ('Should a high note ever hurt?', 'No. Pain or strain means stop, rest and seek advice.')])

add(slug='karaoke-party-sound-setup', cluster='evergreen-music-vocals', kw='karaoke party speakers setup',
    title='How to Set Up Sound for a Karaoke Party at Home',
    desc='How to set up sound for a karaoke party at home: speaker placement, microphone levels, backing tracks, feedback control and a simple checklist before guests arrive.',
    h1='How to Set Up Sound for a Karaoke Party at Home',
    answer='A good home karaoke setup places the speakers to cover the room evenly, keeps the microphone levels steady and the backing track balanced below the singer, and prevents feedback with careful placement. Test with a real song before guests arrive, and keep a spare microphone and cable ready.',
    body='''
<p>A karaoke party is one of the most fun things to host at home, and sound is the difference between a good night and an awkward one. Speakers that are too quiet leave the room flat, speakers that are too loud spoil conversation, and a microphone that feeds back ruins the mood for everyone. A little planning, done before guests arrive, makes the sound work in the room and for the singers.</p>
<p>This guide covers speaker placement, microphone levels, backing tracks, feedback control and a simple checklist. It is written for a typical home, not a venue.</p>
<h2>Place the speakers well</h2>
<p>Place the speakers so the sound reaches the whole room without a dead spot near the singer. Avoid placing them directly behind the singer, where the microphone will pick up the sound and feed back. A speaker on each side of the room, pointing into it, usually spreads the sound evenly. Test by walking the room with a song playing, and note where the sound is thin.</p>
<p>Keep speakers off the floor if you can, and away from corners that boom. A little height helps the sound reach the back of the room.</p>
<h2>Set the microphone level</h2>
<p>Set the microphone level with a singer at normal volume and the backing playing. Aim for the voice to sit clearly above the backing, with the loudest sounds well below distortion. A singer who shouts or whispers will change the level, so keep a rule of thumb for guests: hold the microphone a hand’s width away, and sing at the volume of a normal conversation.</p>
<p>Use a limiter if the equipment has one, to catch the loudest moments and protect the speakers.</p>
<h2>Balance the backing track</h2>
<p>The backing track should support the singer, not compete with them. Set the backing level so the vocal sits clearly on top, but the song still feels full. Test with a few songs at different tempos, since the balance may change between them.</p>
<h2>Control the feedback</h2>
<p>Feedback is the howl that appears when a microphone picks up its own speaker sound. It is caused by the microphone being too close to a speaker, or by the level being too high. Keep speakers in front of the singer and away from the microphone, lower the gain if feedback begins, and move the microphone slightly if needed. A quick test before the party, with the room set as it will be, prevents most problems.</p>
<h2>Check the cables and power</h2>
<p>Use cables that are firmly connected, and tape any that might be tripped over. Keep power leads away from audio cables to reduce hum. If the setup uses a laptop or a phone for the backing, keep it charged and on mains power, and turn off notifications that could interrupt a song.</p>
<h2>Have a backup</h2>
<p>Keep a spare microphone, a spare cable and a second backing source ready. A cable that fails in the middle of a song is the most common disaster. A quick check at the start of the evening and a note of the setup make a repair faster if something goes wrong.</p>
<h2>A checklist before guests arrive</h2>
<ol>
<li>Place the speakers to cover the room, away from the singer.</li>
<li>Test each microphone with a real song at normal volume.</li>
<li>Set the backing level so the voice sits clearly on top.</li>
<li>Test for feedback at the volume you plan to use.</li>
<li>Check cables, power and the spare equipment.</li>
</ol>
<h2>Keep the party moving</h2>
<p>A karaoke night depends on pace as much as on sound. Keep a simple running order, so there is always a next singer ready. Mix duets, group songs and solo performances, and let the more confident singers go first to set the tone. A short break between songs gives people time to choose and keeps the energy up without a long wait.</p>
<p>Keep a list of requests on a visible board or a shared note, so guests can add songs without interrupting the current singer. Check the backing tracks for each request before the party, so nothing stops the evening halfway through.</p>
<p>Plan a short break about halfway through the evening, so the speakers and the amplifier have time to cool, and the guests can refresh their drinks. A quieter moment in the middle can also reset the room for the stronger performances that follow.</p>
<h2>Limits</h2>
<p>Home sound systems have limits, and the room will shape the result more than any equipment. Keep the volume at a level that suits the neighbours and the people in the room, and adjust through the evening as the crowd grows. A karaoke night is about fun, not a perfect sound.</p>
<h2>Prepare the backing and the voices</h2>
<p>Good backing tracks and clear voices make the night. The <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets you sing along with live autotune and record the mix, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For making your own backing track, read the <a href="/tunedzy/blog/how-to-make-a-karaoke-backing-track-at-home">karaoke track post</a> in this series.</p>
''',
    faq=[('Why does the microphone squeal?', 'Feedback from a microphone too close to a speaker or set too loud. Move the speakers and lower the gain.'),
         ('Where should the speakers go?', 'Around the room, facing into it, and away from the singer and the microphone.'),
         ('How loud should the backing be?', 'Loud enough to hear the song, with the vocal clearly on top.'),
         ('What should I bring as a backup?', 'A spare microphone, a spare cable and a second backing source.')])

add(slug='flow-and-timing-for-rap-recording', cluster='evergreen-music-vocals', kw='rap timing recording',
    title='Flow and Timing for Rap Recording: Getting the Pocket Right',
    desc='Flow and timing for rap recording: how a rapper finds the pocket, how to keep the rhythm tight across takes and how to check the timing on a recording.',
    h1='Flow and Timing for Rap Recording: Getting the Pocket Right',
    answer='In rap, flow is how the words sit against the beat, and the pocket is the place where the rhythm feels right. Keep the timing tight by rehearsing to the beat, marking the stressed syllables, and checking each take against the grid. Small timing differences can change the feel, so listen closely as well as looking at the waveform.',
    body='''
<p>Flow is what makes a rap feel alive, and the pocket is the sweet spot where the words sit comfortably against the beat. A good rapper can place a line so it feels effortless, even when the rhythm is complex. Recording that feel is about rehearsal, attention to timing and honest checking. The difference between a line that lands and one that drags can be a few milliseconds.</p>
<p>This post explains how to find the pocket, how to keep the timing steady across takes and how to check the result on a recording.</p>
<h2>What the pocket is</h2>
<p>The pocket is the relationship between the words and the beat that makes the rhythm feel natural. A line can sit slightly before the beat, on it or slightly after, and each position creates a different feel. Laid-back flows sit a little behind, while urgent ones push ahead. The pocket is a choice, and consistency within a verse makes it work.</p>
<p>Finding the pocket starts with listening. Play the beat on loop, and tap your foot or your hand on the beat. Then speak the line along with it, and notice where the stressed syllables fall.</p>
<h2>Rehearse to the beat</h2>
<p>Rehearse each verse with the beat playing, until the timing is automatic. Speak the words first, without performing, so the rhythm is clear. Then add the energy and the delivery. Rehearsal is what turns a good idea into a reliable performance, and it reduces the number of takes you need.</p>
<h2>Mark the stresses</h2>
<p>Write the stressed syllables on the lyric sheet, and mark where each line lands on the beat. The marks become a map for the recording. A line with many syllables may need to be sung quickly, while a short line can be held. Marking the stresses helps you keep the same placement across takes, which is what makes the verse feel consistent.</p>
<h2>Keep the timing tight across takes</h2>
<p>Each take should land on the same points. Listen to a take against the beat, and note where it drifts. A verse that starts on the beat and ends behind it may need to be re-recorded in sections. Recording in short sections makes it easier to keep the timing locked, and to fix one line without losing the rest.</p>
<h2>Check the timing on the waveform</h2>
<p>The waveform shows where each syllable starts, and a grid view shows whether the words land on the beat. Use both to check the timing, but listen first. A waveform can look aligned while the feel is off, and a small visual gap can sound perfectly natural if the flow is right. Trust your ear, and use the picture to confirm.</p>
<h2>Keep the breath in the flow</h2>
<p>Breaths are part of the rhythm in rap, and they must sit where the phrase allows. Mark the breaths on the lyric sheet, and keep them short and quiet. A breath taken in the wrong place can break the flow, while a well-placed one adds punch.</p>
<h2>Edit with care</h2>
<p>If you edit a timing problem, do it gently. Move a syllable only when the feel requires it, and check the result against the rest of the verse. Over-editing a rap makes the flow sound machine-like, which listeners often notice even if they cannot name it.</p>
<h2>A simple checklist</h2>
<ol>
<li>Rehearse each verse with the beat until the timing is automatic.</li>
<li>Mark the stressed syllables and the breaths on the lyric sheet.</li>
<li>Record in short sections, and listen against the beat after each take.</li>
<li>Check the timing on the waveform, but decide by ear.</li>
<li>Edit only where the feel needs it, and listen to the whole verse after each change.</li>
</ol>
<h2>Flow across the whole verse</h2>
<p>A verse should have a shape, with a beginning, a build and a landing. Thinking about the flow as a whole, rather than line by line, helps the rapper decide where to lean forward and where to hold back. A verse that is delivered at a single energy level can become monotonous, while one that varies its placement keeps the listener engaged. Mark the lines that carry the most weight, and give them the strongest placement.</p>
<p>Listen to the verse played back at a slower speed as well. Problems that are hidden at full speed, such as a syllable that sits in the wrong place, become clear, and you can fix them before recording the final take.</p>
<h2>Limits</h2>
<p>Flow is a personal style, and the pocket is different for every rapper and every beat. The principles here are guidelines, not rules. Some of the most effective flows break the expected timing on purpose, and that is a choice to make with intent.</p>
<h2>Start with the beat and a clean take</h2>
<p>Good timing starts with the beat and a clean recording. The <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets you sing along with live autotune and record the mix, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the bpm side of the work, read the <a href="/tunedzy/blog/how-to-find-the-bpm-of-a-song">tempo post</a> in this series.</p>
''',
    faq=[('What is the pocket in rap?', 'The place where the words sit comfortably against the beat, which creates the feel of the flow.'),
         ('Should I always land on the beat?', 'Not always. Laid-back and urgent flows sit in different places, and both can work.'),
         ('How do I keep timing across takes?', 'Rehearse to the beat, mark the stresses, and record in short sections.'),
         ('Can I fix timing with editing?', 'A little, gently. Over-editing makes the flow sound machine-like.')])

add(slug='recording-a-choir-at-home', cluster='evergreen-music-vocals', kw='record choir at home',
    title='How to Record a Choir at Home: Practical Steps for Small Groups',
    desc='How to record a choir at home: arranging singers, placing microphones, balancing the sections, managing room sound and keeping the performance together.',
    h1='How to Record a Choir at Home: Practical Steps for Small Groups',
    answer='Recording a small choir at home is possible with careful planning. Arrange the singers so each section can hear the others, use one or two microphones at a steady distance, balance the sections by ear, and treat the room to reduce echo. Record several complete passes, then choose the best.',
    body='''
<p>A choir sounds rich because many voices blend, and recording that blend at home is a challenge. The sound must be balanced across sections, the room must not swamp the voices, and the singers must stay together without a studio engineer. A small group can make a good recording with careful planning, a simple microphone arrangement and patience with the take.</p>
<p>This post covers the arrangement of singers, the microphone choices, the balance between sections, the room, the performance and the editing. It is written for small home groups and for singers recording together for the first time.</p>
<h2>Arrange the singers</h2>
<p>Place the singers so each section can hear the others, usually in a semicircle or in rows facing the microphone. Keep the altos and basses close together so they blend, and keep the sopranos slightly forward if the room is reflective. A conductor or a lead singer should be visible to everyone. Test a few arrangements before recording, and listen to which one gives the best blend.</p>
<p>Leave enough space between singers so they can breathe and move without touching each other or the microphone stands.</p>
<h2>Choose the microphones</h2>
<p>A stereo pair or a single good microphone placed a few metres from the group usually captures a choir best. The distance captures the blend, while a microphone too close picks up individual voices unevenly. Test the position by listening through headphones while someone walks around the group, and choose the spot where the sound feels full and balanced.</p>
<p>If you have only one microphone, place it high and centred, angled down toward the group, and check the balance by listening.</p>
<h2>Balance the sections</h2>
<p>Sections often need to be balanced by ear. A loud soprano section may cover the altos, and a quiet bass section may disappear. Ask the singers to adjust their volume during a test, so the blend feels right in the room. If the balance is still off, move the singers rather than relying on the microphone to fix it.</p>
<h2>Treat the room</h2>
<p>Hard rooms make choirs sound harsh and echoey. Soft furnishings, rugs, curtains and blankets on the walls reduce reflections and make the blend cleaner. Test the room with a short recording of the group singing, and listen for echo and any harsh peaks. A room that sounds good to the ear may still reflect a lot, so trust the recording.</p>
<h2>Warm up together</h2>
<p>A short group warm-up helps the choir blend, tune and breathe together. Start with breath and gentle humming, then move to simple scales that the whole group can sing. A group that warms up together usually sounds more unified in the first take.</p>
<h2>Record several complete passes</h2>
<p>Record each song several times from start to finish, rather than stopping for mistakes. A complete pass gives the best sense of the performance, and it lets you choose the strongest pass or the best sections from several. Keep the same microphone position and level for every pass, so the passes can be combined later if needed.</p>
<h2>Edit with restraint</h2>
<p>Choir recordings can be edited, but heavy editing removes the life of the performance. Fix clear problems, such as a wrong entry or a loud cough, and keep the natural blend. Compare any edit with the original at the same level, and listen for changes in the room sound at the joins.</p>
<h2>A simple checklist</h2>
<ol>
<li>Arrange the singers so each section can hear the others.</li>
<li>Position one or two microphones at a steady distance from the group.</li>
<li>Balance the sections by listening, and adjust the positions if needed.</li>
<li>Treat the room with soft furnishings and test it.</li>
<li>Record several complete passes, and choose the best.</li>
</ol>
<h2>Plan the rehearsal around the recording</h2>
<p>A rehearsal that sounds good in the room may record differently, because microphones hear differently from ears. Before the recording session, rehearse with the microphone in place, and listen back to a short passage. Ask the singers to move a little, as they would in a real performance, and note any section where the sound changes. A rehearsal planned around the recording saves time on the day, because the problems have already been found.</p>
<p>Agree a simple cue for starting and stopping, so the group begins together and the takes are clean at the start and end.</p>
<h2>Limits</h2>
<p>A home choir recording will not match a professional recording, and the room will always shape the sound. The aim is a warm, honest recording that captures the group well. Keep the expectations realistic, and enjoy the process of making music together.</p>
<h2>Start with a clean recording of the group</h2>
<p>A clean group recording makes editing easier. The <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets you sing along with live autotune and record the mix, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the room side of the work, read the <a href="/tunedzy/how-to-test-your-room-for-echo">room test guide</a>.</p>
''',
    faq=[('How many microphones do I need?', 'One or two, placed a few metres from the group, is usually enough for a home choir.'),
         ('Where should the singers stand?', 'In a semicircle or rows that let each section hear the others, with the altos and basses close together.'),
         ('How do I balance the sections?', 'By listening in the room, and moving singers rather than relying on the microphone alone.'),
         ('Should I edit a choir recording?', 'Lightly. Fix clear problems and keep the natural blend.')])

add(slug='cooling-down-your-voice-after-singing', cluster='evergreen-music-vocals', kw='cool down voice after singing',
    title='How to Cool Down Your Voice After Singing or Recording',
    desc='How to cool down your voice after singing or recording: gentle exercises, hydration, rest and the signs that mean you should stop and seek advice.',
    h1='How to Cool Down Your Voice After Singing or Recording',
    answer='Cool down after singing or a long recording session with gentle humming, lip trills and a slow return to speaking. Drink water, rest the voice and avoid shouting or clearing the throat hard. If hoarseness, pain or a change in the voice lasts more than a few days, see a doctor or a voice specialist.',
    body='''
<p>Singing and long recording sessions ask a lot of the voice, and the way you finish matters as much as the way you start. A proper cool-down helps the voice return to rest, reduces the tiredness of a long day and makes the next session easier. It is a simple habit, and most singers who skip it notice the cost sooner or later.</p>
<p>This post covers gentle cool-down exercises, hydration and rest, the habits that protect the voice and the signs that mean you should stop and seek advice. It is general information and does not replace medical or voice-specialist advice.</p>
<h2>Why cool down</h2>
<p>A voice that has been working hard is warm and sometimes slightly swollen, and it benefits from a gradual return to rest. Stopping abruptly after a loud or long session can leave the voice feeling tired, tight or hoarse the next day. A cool-down is a gentle transition, not an extra workout.</p>
<p>It also gives you a moment to notice how the voice feels, which is useful information for the next session.</p>
<h2>Gentle exercises</h2>
<p>Begin with lip trills or humming on a gentle, comfortable note, moving slowly down the range. Follow with a few descending sirens, keeping the volume soft. Finish with a slow, quiet hum that fades to silence. Each exercise should feel easy. If anything hurts or strains, stop.</p>
<h2>Hydration</h2>
<p>Drink water before, during and after a session. Sipping regularly keeps the vocal folds comfortable, and it is more helpful than a large amount at once. Avoid relying on caffeine or alcohol to get through a session, since both can dry the throat. Warm drinks without much sugar are often soothing after singing.</p>
<h2>Rest</h2>
<p>Give the voice a real rest after a long session. Avoid talking loudly, shouting or whispering for long periods, since whispering can strain the voice as much as speaking. If you can, plan a quiet period after a busy recording day, especially before another demanding session.</p>
<h2>Habits to avoid</h2>
<ul>
<li>Clearing the throat hard, which can irritate the vocal folds.</li>
<li>Shouting over music or a crowd to be heard.</li>
<li>Singing through hoarseness or pain.</li>
<li>Relying on lozenges to mask a tired voice.</li>
<li>Skipping the cool-down after a long, loud session.</li>
</ul>
<h2>Watch the warning signs</h2>
<p>Hoarseness that lasts more than a few days, pain when speaking or singing, a sudden change in pitch or range, or a feeling of a lump in the throat should be checked by a doctor. Bleeding, difficulty breathing or swallowing, and a voice that disappears completely are reasons to seek urgent advice. Do not wait for these signs to get worse.</p>
<h2>A simple routine</h2>
<ol>
<li>Finish with a few gentle lip trills or humming.</li>
<li>Follow with a slow, quiet descending siren.</li>
<li>Drink water and rest the voice for a short period.</li>
<li>Note how the voice feels for the next session.</li>
<li>Seek advice if any warning sign lasts more than a few days.</li>
</ol>
<h2>Build the routine into the day</h2>
<p>A cool-down works best when it is part of the day, not an afterthought at the end of a session. Plan a few minutes of gentle exercises, a glass of water and a short rest into the schedule. If a session runs late, protect the cool-down rather than cutting it, because a long, loud day is when the voice most needs it.</p>
<p>Notice how the voice feels the next morning. A voice that is clear and comfortable suggests the routine is working. A voice that is tired or hoarse suggests that the day was too demanding, and the next session should be shorter or quieter.</p>
<h2>When the routine is not enough</h2>
<p>A cool-down is a simple, supportive habit, but it cannot repair a voice that is already damaged. If the voice remains hoarse, rough or painful after rest and gentle exercises, the routine has done what it can, and a professional should look at the voice. Voice clinicians and speech and language therapists work with singers and speakers, and a referral from a doctor can often be arranged.</p>
<p>Keep a simple diary for a week or two, noting how the voice felt each day and what you did. The diary gives a clinician useful information, and it shows you which habits help and which make the voice worse.</p>
<h2>Limits</h2>
<p>Everyone’s voice is different, and general advice cannot replace a personal assessment. A voice teacher can help with technique, and a doctor or voice specialist can check the health of the voice when needed. Treat the cool-down as a supportive habit, not as a cure for an existing problem.</p>
<h2>Keep the voice healthy for the next session</h2>
<p>A healthy voice makes better recordings. The <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets you sing along with live autotune and record the mix, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the warm-up before singing, read the <a href="/tunedzy/blog/how-to-warm-up-your-voice-before-singing">warm-up post</a> in this series.</p>
''',
    faq=[('How long should a cool-down take?', 'A few minutes of gentle exercises and a rest. It is short, but it helps.'),
         ('Is whispering good for a tired voice?', 'No. Whispering can strain the voice as much as speaking, so rest in silence instead.'),
         ('Should I drink milk or tea?', 'Warm drinks without much sugar are often soothing. Water is the most important.'),
         ('When should I see a doctor?', 'If hoarseness lasts more than a few days, or pain, bleeding or breathing problems appear.')])

add(slug='singing-with-a-cold-what-to-do', cluster='evergreen-music-vocals', kw='singing with a cold',
    title='Singing With a Cold: What to Do and What to Avoid',
    desc='Singing with a cold: when to rest, how to adjust your singing, what to avoid and the warning signs that mean you should see a doctor before singing again.',
    h1='Singing With a Cold: What to Do and What to Avoid',
    answer='Singing with a cold is risky, because a sore, swollen throat can be strained further. Rest the voice if you can, drink plenty of water and avoid forcing high or loud notes. If your voice feels painful, changed or hoarse for more than a few days, see a doctor before singing again.',
    body='''
<p>A cold and a singing schedule often clash. A recording session is booked, a performance is coming, and the voice is hoarse or blocked. Many singers push through, and many regret it. A cold affects the throat and the vocal folds, and singing through it can strain the voice and slow recovery. The decision to sing or rest depends on how you feel, and the aim is to protect the voice for the long term.</p>
<p>This post explains how a cold affects the voice, when to rest, how to adjust if you must sing and when to seek advice. It is general information and does not replace medical advice.</p>
<h2>How a cold affects the voice</h2>
<p>A cold causes inflammation and mucus in the nose and throat, and the vocal folds can become swollen, dry or coated. A swollen fold vibrates less efficiently, which makes the voice hoarse, weak or unstable. Singing with swollen folds can cause further irritation, so the voice takes longer to recover.</p>
<p>The effect differs from person to person. Some singers feel only a little change, while others lose much of their range.</p>
<h2>When to rest</h2>
<p>Rest is the safest choice when the voice is hoarse, breaks easily, feels painful or does not respond normally. A fever, a painful throat, or a heavy cold with a blocked voice are reasons to stop singing. If a performance is booked, speak to the organiser early, and consider a substitute or a lighter arrangement rather than risking the voice.</p>
<h2>If you must sing</h2>
<p>If you have to sing, keep the sessions short, sing softly and avoid the highest and loudest notes. Choose songs that sit in your comfortable middle range, and transpose them down if needed. Warm up very gently, and stop at the first sign of strain. Drink water between songs, and avoid cold drinks, which can tighten the throat.</p>
<h2>What to avoid</h2>
<ul>
<li>Shouting, belting or pushing high notes.</li>
<li>Clearing the throat hard between songs.</li>
<li>Taking strong decongestants or cough medicines without advice, since some can dry the throat.</li>
<li>Singing for long periods without rest.</li>
<li>Recording a full session while the voice is still unwell.</li>
</ul>
<h2>Helpful habits</h2>
<p>Steam and warm drinks can soothe a dry throat, and plenty of water keeps the folds comfortable. Gentle humming and rest help the voice recover. Good sleep and avoiding smoke and alcohol also support recovery, because they dry and irritate the throat.</p>
<h2>When to see a doctor</h2>
<p>See a doctor if the voice is hoarse for more than a few days, if you cough up blood, if you have difficulty breathing or swallowing, if you have a high fever, or if the voice changes suddenly. A voice that has not recovered after a cold should be checked, because persistent changes need assessment.</p>
<h2>Plan for the next session</h2>
<p>After a cold, return to singing gradually. Start with gentle warm-ups, then sing for short periods, and build up as the voice feels normal. Record a short check, and compare it with an earlier recording to see whether the voice has returned to its usual sound.</p>
<h2>Tell the people who depend on you</h2>
<p>If a cold will affect a recording, a session or a performance, tell the people involved early. A producer, a band or a client would rather move a date than receive a strained or unreliable performance. Explain plainly what you can and cannot do, and suggest a realistic alternative, such as a shorter session or a later date.</p>
<p>Being honest about the voice is part of professional care. It protects the performance, the relationship and your long-term ability to sing.</p>
<h2>Recovery and the return to singing</h2>
<p>Coming back after a cold needs patience. The voice may feel normal in speech while still being fragile for singing, because singing asks more of the folds. Start with gentle humming and simple sustained notes in the middle of your range, and only then add the phrases and the higher notes. Stop if you feel any strain, and return to the earlier stage the next day.</p>
<p>Record a short check each day during the return, and compare it with an earlier recording of your normal voice. When the sound and the effort feel the same as before the cold, you can usually resume your full schedule, but keep the first few sessions shorter than usual.</p>
<h2>Limits</h2>
<p>Advice on singing with a cold is general, and every case is different. A doctor or a voice specialist can assess the voice properly, and a voice teacher can advise on technique. When in doubt, rest and get checked.</p>
<h2>Protect the voice for the recording</h2>
<p>A rested voice records better. The <a href="/tunedzy/tools/karaoke-autotune">Karaoke Autotune</a> tool lets you sing along with live autotune and record the mix, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For recovery after a session, read the <a href="/tunedzy/blog/cooling-down-your-voice-after-singing">cool-down post</a> in this series.</p>
''',
    faq=[('Can I record with a cold?', 'It is better to wait. A cold voice may strain and record poorly, and recovery is slower.'),
         ('Should I take medicine to sing?', 'Ask a doctor or pharmacist first. Some medicines dry the throat or affect the voice.'),
         ('How long before I sing normally again?', 'It depends on the cold. Return gradually once the voice feels normal and comfortable.'),
         ('When is a cold voice an emergency?', 'Coughing up blood, breathing or swallowing difficulty, or a sudden voice change needs urgent medical advice.')])
