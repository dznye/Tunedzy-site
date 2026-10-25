"""Blog posts, batch 22: levels, metering and dynamics for home work (evergreen). Merged into content_blog.py.
Each post explains one concept, its practical use and its limits. Settings are described in general terms because
menus differ between apps. No invented statistics. Funnel: each post ends with a link to Tunedzy Go and to the
matching free tool."""

CLUSTERS = {
    'evergreen-levels': dict(tool='lufs-meter', label='Levels and metering explained', tool_name='LUFS Meter'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='gain-staging-explained-for-home-studios', cluster='evergreen-levels', kw='gain staging explained',
    title='Gain Staging Explained for Home Studios: Setting Levels Step by Step',
    desc='Gain staging explained for home studios: how to set levels at each stage of the chain, keep headroom and avoid noise and distortion from the start.',
    h1='Gain Staging Explained for Home Studios: Setting Levels Step by Step',
    answer='Gain staging means setting the level at each stage of the signal chain so that every stage has enough signal to be clean and enough headroom to avoid distortion. Start at the microphone, set the interface gain with a test, then check levels through each plug-in or effect. Good gain staging removes many problems before they start.',
    body='''
<p>Gain staging is the discipline of managing level through the whole signal chain, from the microphone to the final file. Each stage of the chain has its own limits: too little level and the noise becomes obvious, too much and the signal distorts or clips. A home studio can sound excellent with modest equipment if the gain is staged well, and it can sound poor with expensive equipment if the levels are wrong at any point.</p>
<p>This post explains the principle, walks through the stages in order and gives a simple routine for setting levels that keeps the signal clean from the start.</p>
<h2>What gain staging means</h2>
<p>Every device in the chain takes an input, changes it and passes an output to the next device. Each device has a range where it works best. Gain staging keeps the signal inside that range at every point. The microphone produces a small signal, the preamp boosts it, the interface converts it, the software processes it and the export prepares it for delivery. A problem at any stage travels to the next one.</p>
<p>The goal is not the loudest possible signal at each point. It is a signal that is strong enough to be clean and low enough to leave headroom for surprises.</p>
<h2>Start at the microphone</h2>
<p>The first decision is the distance and the position of the microphone. A close, steady position gives a strong signal for the same gain, which means less boost is needed and less noise is added. Before touching any gain control, set the microphone where it will stay for the session, and mark the position if you can.</p>
<h2>Set the interface gain</h2>
<p>Set the interface gain with the speaker talking at normal volume, and watch the meter. Aim for the loudest words to reach the upper part of the meter without touching the top. Leave room for sudden loud sounds, such as a laugh or a plosive pop. Record a short test and listen on headphones before you commit, since a level that looks right on the meter may still sound harsh or quiet.</p>
<h2>Check the software</h2>
<p>Most recording software has its own input and output levels. Check that the track level is not clipping, and that the level inside the project is similar to what the interface delivers. A software fader set very high can cause clipping even when the interface is fine, so keep the track faders near their default position and make adjustments at the source where possible.</p>
<h2>Check each effect</h2>
<p>Effects such as compressors, equalisers and limiters change the level as well as the tone. Check the meter after each effect, and make sure the signal leaving the effect is not clipping. A compressor with makeup gain can push a signal over the top, so adjust the makeup gain to restore the level without distortion.</p>
<h2>Leave headroom for the final mix</h2>
<p>Each track should leave room below the top of the meter, so the mix has space to combine. A mix made of many tracks that each peak near the top will clip when they are summed. Aim for each track to peak comfortably below the top, and set the final level with the master fader, not by pushing each track.</p>
<h2>The export is the last stage</h2>
<p>The export is the final stage of the chain, and it deserves a check. Measure the true peak and the loudness of the exported file, not only the project, since the export can add its own changes. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can show both figures for a finished file.</p>
<h2>A routine that keeps levels clean</h2>
<ol>
<li>Set the microphone position, and mark it.</li>
<li>Set the interface gain with a test at normal speaking volume.</li>
<li>Check the track level in the software, keeping the faders near their default.</li>
<li>Check the level after each effect, and adjust makeup gain.</li>
<li>Leave headroom in the mix, and check the export at the end.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Setting the gain too low, then boosting the noise later.</li>
<li>Letting one stage clip, which cannot be repaired downstream.</li>
<li>Pushing every track to the top, so the mix clips.</li>
<li>Judging the level only by the meter, without listening.</li>
<li>Ignoring the level change caused by an effect.</li>
</ul>
<h2>Why it pays off</h2>
<p>Good gain staging makes every later decision easier. The noise floor stays low, the effects behave predictably, and the mix has room to breathe. Many home studio problems that seem to need expensive fixes are really gain staging problems, and they disappear when the levels are set properly at the start.</p>
<h2>Limits</h2>
<p>Gain staging principles apply broadly, but the specific controls differ between interfaces, plug-ins and software. Some devices behave differently at different levels, and some effects are designed to be driven hard. Learn the principle, then check how your own equipment responds with a test.</p>
<h2>Check the level at every stage</h2>
<p>Gain staging is easiest with a reliable meter at each stage. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the loudness and true peak of the finished file, and the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. For the basics that come first, read the <a href="/tunedzy/blog/what-is-gain-in-recording">gain post</a> in this series.</p>
''',
    faq=[('Where should I start when setting levels?', 'At the microphone, with the distance and position, then the interface gain.'),
         ('Why does my mix clip when every track is fine?', 'The tracks add together. Leave headroom on each track and set the final level at the master.'),
         ('Should I push the faders to the top?', 'No. Keep them near their default and adjust at the source where possible.'),
         ('What does makeup gain do?', 'It restores the level after compression. Check that it does not push the signal into clipping.')])

add(slug='limiting-vs-clipping-explained', cluster='evergreen-levels', kw='limiting vs clipping',
    title='Limiting vs Clipping: What Each One Does to Your Sound',
    desc='Limiting vs clipping explained: why clipping damages the sound, how a limiter controls peaks gently and how to tell which problem you have.',
    h1='Limiting vs Clipping: What Each One Does to Your Sound',
    answer='Clipping happens when a signal goes above the maximum a system can handle, and the peaks are cut off, which adds harsh distortion. Limiting is a controlled process that reduces peaks before they reach the maximum, so the level is held without a harsh break. Limiting can prevent clipping, but heavy limiting flattens the sound.',
    body='''
<p>Limiting and clipping are often mentioned together, and beginners sometimes treat them as the same thing. They are not. Clipping is damage that happens when a signal exceeds the maximum the system can carry. Limiting is a deliberate process that reduces the peaks of a signal before they reach that maximum. One is an accident and the other is a tool, and understanding the difference helps you choose the right response to a loud sound.</p>
<p>This post explains what happens in each case, why clipping sounds harsh, how a limiter controls peaks and when limiting goes too far.</p>
<h2>What clipping is</h2>
<p>In digital audio, there is a maximum level that the system can store. When a signal rises above that level, the top of the wave is cut flat. The flattened peaks add new frequencies that were not in the original sound, which the ear hears as a harsh, crackly or distorted tone. Clipping cannot be fully undone, because the information above the maximum was never stored.</p>
<p>Clipping can happen at several points in the chain: at the input, inside a plug-in, or at the export. Any stage that is pushed too hard can clip, and the damage is usually obvious on headphones.</p>
<h2>What limiting is</h2>
<p>A limiter watches the signal and reduces its gain whenever the level would exceed a set ceiling. The reduction happens quickly and smoothly, so the peak is held at the ceiling rather than being cut off abruptly. The result is a louder, more controlled signal, with the peaks tamed before they can distort.</p>
<p>A good limiter works in very short moments, and it recovers gradually afterwards. The speed of those actions decides whether the result sounds natural or squashed.</p>
<h2>Why clipping sounds harsh</h2>
<p>A clipped waveform has sharp corners, and sharp corners contain high-frequency content that the original sound did not have. The ear hears that content as roughness, grit or crackle. The harshness is most noticeable on loud, sustained sounds, such as a voice shouting or a cymbal crash, and on sounds that repeat quickly.</p>
<h2>Why limiting can also harm</h2>
<p>Limiting that is too strong removes the natural dynamics of the sound. The louder parts are held down, the quieter parts are raised, and the whole signal feels flat and tiring. This is the squashed sound that many listeners dislike. A little limiting is often invisible, but heavy limiting is obvious, especially in music with a wide dynamic range.</p>
<h2>How to tell which problem you have</h2>
<ol>
<li>Listen for crackle, grit or harsh edges on the loudest sounds. That suggests clipping.</li>
<li>Listen for a flat, tiring sound with little contrast between loud and quiet. That suggests heavy limiting.</li>
<li>Check the meter for flat tops on the waveform, which show clipping.</li>
<li>Check the gain reduction on the limiter, which shows how hard it is working.</li>
<li>Compare with the original at the same level, to hear which change has occurred.</li>
</ol>
<h2>The right response</h2>
<p>If clipping has already happened, the best response is usually to re-record or re-export with lower levels, since the damage cannot be fully repaired. If the signal is hot but unclipped, a light limiter can hold the peaks and protect the rest of the chain. Set the ceiling a little below full scale, and use only enough gain reduction to catch the loudest moments.</p>
<h2>Practical limits</h2>
<p>Limiters are powerful, and they can be misused as a loudness button. Use them to control peaks, not to make the whole recording louder. If you find yourself using heavy gain reduction, the level needs to be set lower earlier in the chain, or the mix needs more dynamic control.</p>
<h2>Limiting in a mix and on a master</h2>
<p>A limiter does different work on a single voice, on a mix and on a master. On a voice, it catches the loudest words so the level can be raised without clipping. On a mix, it can control the sum of several tracks, catching peaks that appear only when the parts combine. On a master, it sets the final ceiling for delivery, and it is the stage where clipping most often appears if the earlier levels were too hot.</p>
<p>The key is to set the ceiling at the stage that needs it. A limiter on every track can build up gain reduction everywhere, and the sound becomes uniformly flat. Place the limiter where a peak problem actually occurs, and check the gain reduction it shows.</p>
<p>When a mix sounds dull after limiting, remove the limiter from one stage at a time and listen again. The stage that restores life is usually the one that was working too hard.</p>
<h2>Limits</h2>
<p>The behaviour of limiters varies widely between products, and the settings that suit one may not suit another. The principles above apply broadly, but judge each limiter by ear, on the material you are working on.</p>
<h2>Check the peaks in the final file</h2>
<p>Peaks are easiest to check in the finished file. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the true peak alongside the loudness, which helps you spot clipping that a sample meter can miss. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping in a recording you own. For the level basics, read the <a href="/tunedzy/blog/limiter-settings-for-voice-explained">limiter settings post</a> in this series.</p>
''',
    faq=[('Can I fix a clipped recording?', 'Not fully. The information above the maximum was lost. Re-record or re-export with lower levels.'),
         ('Does a limiter prevent clipping?', 'Yes, if it is set to catch the peaks before the maximum. It cannot fix a signal that has already clipped.'),
         ('Why does my limited mix sound flat?', 'The limiting is too heavy. Reduce the gain reduction and set the level lower earlier in the chain.'),
         ('Where should the limiter ceiling sit?', 'A little below full scale, leaving headroom for the export and playback.')])

add(slug='parallel-compression-explained', cluster='evergreen-levels', kw='parallel compression',
    title='Parallel Compression Explained: Punch Without Squashing the Sound',
    desc='Parallel compression explained: how blending a heavily compressed copy with the original adds weight and punch without losing the natural dynamics.',
    h1='Parallel Compression Explained: Punch Without Squashing the Sound',
    answer='Parallel compression blends a heavily compressed copy of a sound with the original, adding weight and punch while keeping the natural dynamics of the uncompressed signal. It is useful for voices and drums that need more body without losing their life. Blend the compressed copy quietly, and listen to the balance between the two.',
    body='''
<p>Compression reduces the gap between loud and quiet, which can make a sound feel bigger and more solid. Heavy compression, however, can flatten the life out of a performance. Parallel compression is a way to get the weight of heavy compression without losing the contrast of the original. The technique blends a strongly compressed copy with the untouched sound, so the result has both body and dynamics.</p>
<p>This post explains the principle, how to set up a parallel path, how to blend it and the mistakes that make the effect sound unnatural.</p>
<h2>The basic idea</h2>
<p>You create two versions of the same sound: the original, which is left alone, and a copy that is compressed heavily. Then you blend the compressed copy under the original. The compressed version fills in the quieter moments and adds sustain, while the original keeps the peaks and the natural feel. The combination can sound powerful without the squashed quality of simply compressing the whole signal.</p>
<h2>Why it works</h2>
<p>Heavy compression brings up the quiet parts and holds down the loud ones. Blended under the original, the compressed copy adds those raised quiet details, and the original keeps the transients that give a sound its attack. The ear hears the blend as fuller and more present, rather than as a single heavily processed sound.</p>
<h2>How to set it up</h2>
<ol>
<li>Duplicate the track, or send the track to an auxiliary channel.</li>
<li>Apply heavy compression to the copy, with a high ratio and a fast attack.</li>
<li>Set the makeup gain on the copy so its level matches the original.</li>
<li>Blend the compressed copy under the original, using its fader or send level.</li>
<li>Listen to the balance, and reduce the copy until the effect is felt rather than heard.</li>
</ol>
<h2>Where it suits a voice</h2>
<p>For a voice, parallel compression can add presence and body to a thin or quiet performance, while keeping the natural breath and expression. It is useful when a singer or a speaker is delivering with a soft, intimate tone that needs a little more weight. Keep the compressed copy quiet, so it adds fullness without making the voice sound pumped.</p>
<h2>Where it suits drums</h2>
<p>Drums often benefit most, because the heavy compressed copy can add sustain and punch while the original keeps the attack. Blended carefully, it makes a kit sound bigger without losing its life. Watch the balance, since too much of the compressed copy can make the drums sound smeared.</p>
<h2>Common mistakes</h2>
<ul>
<li>Blending the compressed copy too loudly, so the effect dominates.</li>
<li>Forgetting to match the level, so the copy seems louder for the wrong reason.</li>
<li>Using a slow attack on the copy, which removes the punch.</li>
<li>Stacking more compression on the original, which defeats the purpose.</li>
<li>Judging the effect only soloed, rather than in the mix.</li>
</ul>
<h2>Check the result</h2>
<p>Compare the blended sound with the original, at the same level, with the copy switched on and off. The blend should sound fuller, with the natural dynamics intact. If you notice the effect as a separate sound, reduce the copy. Check the final result on headphones and a phone, since small speakers can reveal a smeared low end.</p>
<h2>A little goes a long way</h2>
<p>Parallel compression is one of the most effective tools for adding weight, and it is easy to overdo. A small blend, felt rather than heard, is usually the goal. Keep the original as the star, and let the compressed copy support it.</p>
<h2>Choosing the compressor for the copy</h2>
<p>The compressor on the parallel copy does not have to be the same as the one you would use on the original. Many producers choose a compressor with a fast, aggressive character for the copy, because it creates the dense, sustained sound that makes the blend work. The original can then be left with a gentler setting, or none at all, so its transients remain intact.</p>
<p>Try two or three compressors on the copy, and listen to which one adds the most useful weight. Some add warmth, others add bite. The right one depends on the sound you need, and the blend will reveal the difference quickly.</p>
<p>Keep the settings of the copy saved, so you can recall the exact sound when you need it again on a similar track.</p>
<h2>Limits</h2>
<p>Parallel compression is not a fix for a poor recording. It adds body to a sound that already has clarity, and it cannot restore detail that was never captured. Some sounds do not benefit at all, and simpler processing may serve them better.</p>
<h2>Listen in context</h2>
<p>Parallel effects are easiest to judge in the full mix. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can check the loudness of the final file after blending, so the extra weight does not push the level too far. For the basic compressor settings, read the <a href="/tunedzy/blog/what-does-a-compressor-do">compressor post</a> in this series.</p>
''',
    faq=[('What is parallel compression?', 'Blending a heavily compressed copy with the original to add weight without losing dynamics.'),
         ('Does it work on voices?', 'Yes, for adding presence and body, if the compressed copy is kept quiet.'),
         ('Why does my blend sound smeared?', 'The copy is too loud or its attack is too slow. Reduce the level and speed up the attack.'),
         ('Is it the same as heavy compression?', 'No. The original dynamics are kept, which is the point of the technique.')])

add(slug='fade-in-and-fade-out-explained', cluster='evergreen-levels', kw='fade in and fade out audio',
    title='Fade In and Fade Out Explained: How to Start and End Audio Smoothly',
    desc='Fade in and fade out explained: when to use them, the curve shapes that suit speech and music and how to avoid the clicks that abrupt starts and endings cause.',
    h1='Fade In and Fade Out Explained: How to Start and End Audio Smoothly',
    answer='A fade in gradually raises the level at the start of a clip, and a fade out gradually lowers it at the end. They prevent abrupt starts and endings, which can sound like clicks or pops. Use short fades for speech and longer ones for music, and choose a curve that suits the sound.',
    body='''
<p>A sudden start or a sudden stop in a recording can jar the listener, and sometimes it creates an audible click. Fades solve that problem by changing the level smoothly over a short time. They are one of the simplest tools in audio editing, and they are also one of the most often used badly. A fade that is too long, too short or the wrong shape can spoil a clip that would otherwise be fine.</p>
<p>This post explains what fades do, when to use them, the shapes that suit speech and music and the common mistakes to avoid.</p>
<h2>What a fade does</h2>
<p>A fade changes the level of a sound over time. A fade in starts from silence and rises to the full level. A fade out starts at the full level and falls to silence. The change is gradual, so the listener does not hear a sudden edge. A fade also helps the sound blend into what comes before or after it.</p>
<h2>Why clicks happen</h2>
<p>A digital audio clip that starts or ends in the middle of a wave can produce a click, because the sudden jump in level is heard as a sharp sound. A short fade removes the jump, since the level changes gradually across a few milliseconds. This is why even a very short fade is often enough to remove a click at an edit point.</p>
<h2>Fades for speech</h2>
<p>For speech, short fades are usually best. A few milliseconds at the start and end prevent clicks without cutting off the first or last sound. Be careful not to fade out the final word, because a long fade can make the speaker sound as if they trailed off. Check the end of each clip by listening, and adjust the fade so the last word is complete.</p>
<h2>Fades for music</h2>
<p>Music often benefits from longer fades, especially at the end of a track or a section. A fade out of several seconds can bring a song to a natural finish, while an abrupt stop can feel unfinished. The length should suit the tempo and the feel of the piece, and the fade should be shaped so it does not sound like a volume change.</p>
<h2>Fade curves</h2>
<p>Fades can follow different curves. A linear fade changes the level at a steady rate, which can sound like a sudden drop near the end. An exponential or logarithmic fade follows the way the ear perceives loudness, and it often sounds more natural. Many editors offer several curve shapes, so try a few and listen to the result.</p>
<h2>Common mistakes</h2>
<ul>
<li>Fading out the last word of speech, which makes it sound unfinished.</li>
<li>Using a fade that is too long for a short clip.</li>
<li>Leaving a click at an edit point, because no fade was applied.</li>
<li>Choosing a linear curve when a smoother one would suit the sound better.</li>
<li>Fading a clip that has a strong natural ending, which removes the impact.</li>
</ul>
<h2>Crossfades are different</h2>
<p>A crossfade is a fade out of one clip and a fade in of the next, overlapping in time. It is used to join two clips smoothly, and it is covered in the <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade guide</a>. A simple fade in or out is for the start and end of a single clip.</p>
<h2>Check the edges</h2>
<p>After adding fades, play the start and end of each clip several times, on headphones and on a phone. Listen for clicks, for cut-off words and for any sudden change in the room sound. Adjust the length and curve until the edges feel natural.</p>
<h2>Fades in music production</h2>
<p>In a song, fades are often used at the start and end of the whole track, and sometimes inside it, to move between sections or to bring in a new element. A fade in can introduce a sound gradually, so it does not interrupt the groove. A fade out can end a track without a sudden stop, but it should not hide an ending that the arrangement has built toward.</p>
<p>Fades inside a track can be used to create a dropout or a breath, where the level drops for a moment and rises again. Test these carefully, because a fade that is too slow can blur the timing of the beat.</p>
<p>When you make a fade in a music project, check it against the tempo. A fade that lasts a whole number of bars often feels more natural than one that ends between beats.</p>
<h2>Limits</h2>
<p>Fades are a finishing tool, and they cannot repair a clip that starts or ends badly in the performance. Some sounds, such as a deliberate stop or a sharp ending, should not be faded at all. Trust your ear, and keep the fade as short as the job allows.</p>
<h2>Listen to the edges</h2>
<p>The edges of a file are where listeners form their first and last impressions. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can check the loudness of the finished file, and the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping and level problems in a recording you own. For the editing side, read the <a href="/tunedzy/blog/how-to-fix-clicks-and-pops-in-an-audio-recording">clicks and pops post</a> in this series.</p>
''',
    faq=[('How long should a speech fade be?', 'A few milliseconds at the edges, enough to prevent clicks without cutting off words.'),
         ('Why does my track end abruptly?', 'It was cut without a fade. Add a fade out of a few seconds for music.'),
         ('Which fade curve should I use?', 'Try a few. A logarithmic or exponential curve often sounds more natural than a linear one.'),
         ('Is a fade the same as a crossfade?', 'No. A fade covers the start or end of a clip, while a crossfade joins two clips.')])

add(slug='vu-meter-vs-peak-meter', cluster='evergreen-levels', kw='vu meter vs peak meter',
    title='VU Meter vs Peak Meter: Which One Should You Watch?',
    desc='VU meter vs peak meter explained: how each one reads level, why they show different numbers and which one to watch for recording and mixing.',
    h1='VU Meter vs Peak Meter: Which One Should You Watch?',
    answer='A VU meter shows an average level, reacting slowly to match how loud a sound seems, while a peak meter shows the single loudest moment, reacting quickly. Watch the peak meter to avoid clipping, and use the VU-style average to judge how loud a passage feels. Use both together, because each answers a different question.',
    body='''
<p>Level meters come in several designs, and two of the most common are the VU meter and the peak meter. They look similar, but they show different things. A VU meter shows an average level, while a peak meter shows the loudest moment. Beginners who watch the wrong one can set levels that clip or that sound too quiet, so it is worth understanding what each meter measures.</p>
<p>This post explains how each meter works, why they disagree, which one to watch for each job and how to use them together.</p>
<h2>What a VU meter shows</h2>
<p>A VU meter is designed to show something close to the loudness a listener perceives. It reacts slowly, averaging the level over a fraction of a second, so the needle does not jump with every spike. That makes it useful for judging how loud a passage feels, but it can hide short, sharp peaks that will clip.</p>
<p>Many digital meters offer a VU-style display alongside a peak display, and the VU-style reading is often shown as an average level.</p>
<h2>What a peak meter shows</h2>
<p>A peak meter reacts quickly to the loudest moment in the signal. It shows the highest level reached, and it is the meter to watch for clipping. A peak meter can look busy on speech, because the peaks appear and disappear with every word, but the reading is essential for avoiding distortion.</p>
<h2>Why they disagree</h2>
<p>A speech signal has short, loud peaks and a lower average. The peak meter shows the peaks, which can be well above the average, and the VU meter shows the average, which sits lower. Both readings are correct, and they answer different questions. A speech recording can show peaks near the top on the peak meter while the average sits comfortably in the middle.</p>
<h2>Which to watch for each job</h2>
<ul>
<li><strong>Recording:</strong> watch the peak meter, to keep the loudest words clear of clipping.</li>
<li><strong>Judging how loud a passage feels:</strong> watch the average, to match levels between sections.</li>
<li><strong>Mixing:</strong> use both, with the average for balance and the peaks for headroom.</li>
<li><strong>Final checks:</strong> use a loudness reading and a true-peak reading on the export.</li>
</ul>
<h2>A simple way to use both</h2>
<ol>
<li>During recording, keep the peaks comfortably below the top.</li>
<li>During editing, match the average level of each section.</li>
<li>Listen to every change, since neither meter replaces the ear.</li>
<li>After export, check the loudness and true peak of the final file.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Setting the level by the average alone, and clipping on the peaks.</li>
<li>Watching only the peaks, and making a quiet recording that feels weak.</li>
<li>Expecting a VU meter to show clipping, which it may not reveal.</li>
<li>Comparing readings across different meter types without knowing which is which.</li>
</ul>
<h2>Reading both meters in a session</h2>
<p>During a recording session, the two meters can tell you different and useful things. The peak meter warns you when a loud word is about to clip. The average meter tells you whether the performance feels consistent from one take to the next. Watching both as you record lets you keep the peaks safe and the feel steady, without chasing every change in the peak meter.</p>
<p>A practical habit is to run the first few takes with both meters in view, noting where the average sits for a verse and a chorus. Later takes can then be compared with those reference points, which makes it easier to notice when a singer or speaker has drifted.</p>
<h2>Meters in editing</h2>
<p>In editing, the average meter helps you match the level of one section to another, while the peak meter confirms that no edit has pushed a moment into clipping. A section that looks correct on the average can still hide a loud spike, and a section that looks quiet on the peaks may feel too low in the average. Use both, and listen to the join between sections before making a final decision.</p>
<p>Make a note of the average level of a section that sounds right, and use it as a target for the rest of the edit. A reference point is more useful than an abstract number. Write the reference beside the section it came from, so you can see the context when you return to the edit.</p>
<h2>Limits</h2>
<p>Meters differ widely in how they calculate and display level, and the names are used inconsistently across products. Check what each meter in your software measures before comparing readings, and do not assume that two meters labelled the same will agree.</p>
<h2>Check the peaks in the final file</h2>
<p>The finished file is where level matters most. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the loudness and true peak of an export, and the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping and level problems in a recording you own. For the decibel scale behind all these readings, read the <a href="/tunedzy/blog/decibels-explained-for-recording">decibels post</a> in this series.</p>
''',
    faq=[('Which meter prevents clipping?', 'The peak meter, because it shows the loudest moment.'),
         ('Why does the average look lower than the peaks?', 'Speech has short, loud peaks and a quieter average. Both readings are correct.'),
         ('Should I trust a VU meter for clipping?', 'Not on its own. Use a peak reading to check for clipping.'),
         ('Do I need both meters?', 'Ideally yes, since each answers a different question about the level.')])

add(slug='loudness-after-noise-reduction', cluster='evergreen-levels', kw='loudness after cleanup',
    title='Why Loudness Changes After Noise Reduction and How to Fix It',
    desc='Why loudness changes after noise reduction: how cleanup lowers the level, how to restore it without raising the noise and how to check the final loudness.',
    h1='Why Loudness Changes After Noise Reduction and How to Fix It',
    answer='Noise reduction often lowers the overall loudness of a recording, because it removes sound along with the noise. Restoring the level by raising the whole file also raises any remaining noise. Restore loudness with gentle gain and light levelling after cleanup, then check the final loudness against your target.',
    body='''
<p>Many people are surprised when a recording gets quieter after noise reduction. The reason is simple: the reduction removes sound, and some of that sound is part of the voice. The file sounds cleaner, but it may now be below the level you need. Restoring the level is important, but it has to be done carefully, or the noise that was removed will return with the voice.</p>
<p>This post explains why loudness drops, how to restore it without bringing the noise back and how to check the result against a target.</p>
<h2>Why the level drops</h2>
<p>A noise reducer lowers the signal in the parts it judges to be noise, and some of that signal is quiet speech or breath. The total energy of the recording goes down, which the meter shows as a drop in loudness. The drop is often a few decibels, and it can be larger with strong settings.</p>
<p>The reduction also changes the balance of the signal. Quiet passages may lose more than loud ones, so the difference between them can change.</p>
<h2>Why you should not just turn it up</h2>
<p>Raising the whole file restores the level, but it also raises the noise that remains. A file that was quiet and clean can become loud and hissy in the same move. The noise floor rises with the voice, so the background may become more distracting than before the cleanup.</p>
<h2>Restore the level carefully</h2>
<ol>
<li>Check the loudness of the cleaned file against your target, and note the gap.</li>
<li>Apply a gentle gain change to close most of the gap, not all of it.</li>
<li>Use light levelling to bring the quiet passages up, rather than raising everything.</li>
<li>Check the noise in the quiet pauses after each change.</li>
<li>Stop when the level is close to the target and the background stays low.</li>
</ol>
<h2>Use levelling rather than gain alone</h2>
<p>A levelling process raises quiet passages and lowers loud ones, which can reach the target without lifting the noise in the quietest pauses. It is gentler than a single gain change, and it keeps the balance more natural. Apply it with a light touch, so the voice keeps its expression.</p>
<h2>Check the final loudness</h2>
<p>After restoring the level, measure the loudness of the final file, not only the project. Check the true peak too, since a gain change can push peaks into clipping. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows both figures for the export, so you can confirm the file meets your target.</p>
<h2>Listen to the background</h2>
<p>Once the level is restored, listen to the quiet pauses on headphones. If the noise has risen, reduce the restoration gain or apply the noise reduction more gently. A slightly lower level with a clean background is usually better than a louder file with audible hiss.</p>
<h2>Common mistakes</h2>
<ul>
<li>Restoring the level with a large gain change that lifts the noise.</li>
<li>Applying heavy noise reduction, then raising the level to compensate.</li>
<li>Checking loudness on the project rather than the export.</li>
<li>Forgetting to check the true peak after a gain change.</li>
<li>Ignoring the change in balance between quiet and loud passages.</li>
</ul>
<h2>Plan the level before cleaning</h2>
<p>A good habit is to check the level before any noise reduction, and to set a target for the cleaned file in advance. If the original is far below the target, consider whether the recording can be re-made at a closer distance, rather than relying on cleanup and gain to bridge the gap. A recording that starts at the right level needs much less restoration, and it keeps the voice more natural.</p>
<p>Record the level before and after each cleanup stage, in your project notes. The record shows how much each stage affects the loudness, and it helps you decide how much restoration is reasonable for future recordings.</p>
<p>When a client or a collaborator asks for a specific loudness, explain the trade-off. A higher target may require more cleanup, and more cleanup can cost naturalness. A clear discussion at the start avoids disappointment at the end. Agree the target and the trade-off in writing, so the expectation is clear to everyone. Revisit the agreement if the delivery format changes, since a different platform may ask for a different target.</p>
<h2>Limits</h2>
<p>There is a limit to how much the level can be restored without audible noise. If the cleanup was very strong, the recording may simply be quieter than your target, and the best choice is to accept a slightly lower level. Targets are guides, and a clean, natural sound matters more than hitting a number exactly.</p>
<h2>Check the result</h2>
<p>A reliable meter confirms the level after cleanup. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the loudness and true peak of the final file, and the <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own. For the balance between cleanup and natural sound, read the <a href="/tunedzy/blog/how-much-noise-reduction-is-too-much">noise reduction limits post</a> in this series.</p>
''',
    faq=[('Why is my cleaned file quieter?', 'Noise reduction removes some sound along with the noise, which lowers the overall level.'),
         ('Can I just raise the level?', 'It raises the noise too. Use gentle gain and levelling, then check the background.'),
         ('What target should I aim for?', 'Your platform or project target, but accept a slightly lower level if the cleanup was strong.'),
         ('Should I check loudness before or after export?', 'After. The export can change the level, so measure the final file.')])

add(slug='loudness-units-vs-decibels', cluster='evergreen-levels', kw='loudness units vs decibels',
    title='Loudness Units vs Decibels: Why Two Scales Are Used',
    desc='Loudness units vs decibels explained: how LU and dB relate, why loudness uses a perception-based scale and how to read the numbers on a loudness meter.',
    h1='Loudness Units vs Decibels: Why Two Scales Are Used',
    answer='Decibels measure the level of a signal relative to a reference, while loudness units measure how loud a sound is perceived to be, using a model of human hearing. Loudness is measured in LUFS and LU, which are related to decibels but weighted for perception. Use decibels for setting levels and loudness units for matching how loud a file sounds.',
    body='''
<p>Audio meters show two kinds of unit that look similar and mean different things. Decibels measure the level of a signal against a reference. Loudness units measure how loud a sound is perceived to be, using a model of how the ear responds to different frequencies. Confusing them leads to mistakes, such as setting a level by the wrong meter or judging a file by a number that does not describe what the listener hears.</p>
<p>This post explains the difference between the two, why loudness uses its own scale and how to use both when you set levels and check a finished file.</p>
<h2>What decibels measure</h2>
<p>A decibel is a ratio on a logarithmic scale. In recording, the level is usually shown in dBFS, which compares the signal with the maximum the system can store. Decibels describe how strong the signal is at a particular point, which is ideal for setting gain and avoiding clipping. They do not account for how the ear hears different frequencies.</p>
<h2>What loudness units measure</h2>
<p>Loudness units, written as LU, and the loudness scale LUFS, measure perceived loudness. The measurement applies a weighting that reflects how sensitive the ear is at different frequencies, and it averages the result over time. Two signals with the same peak level can have very different loudness, and the loudness scale reflects that difference.</p>
<h2>How they relate</h2>
<p>Loudness is measured from the same digital signal as the decibel level, but it adds the perceptual weighting and the averaging. So a loudness reading is always in relation to the level of the signal, but it is not the same number. A file can have a peak at minus three decibels and a loudness far lower or higher, depending on its content.</p>
<h2>Which to use for what</h2>
<ul>
<li><strong>Setting gain and avoiding clipping:</strong> use decibels, watching the peak meter.</li>
<li><strong>Matching how loud a file sounds:</strong> use loudness, against a target.</li>
<li><strong>Checking platform delivery:</strong> use loudness and true peak together.</li>
<li><strong>Comparing mixes:</strong> use loudness to match levels, and listen to confirm.</li>
</ul>
<h2>Reading a loudness meter</h2>
<p>A loudness meter usually shows an integrated value for the whole file, a short-term value for recent sound and a momentary value for the last fraction of a second. The integrated figure is the one most often matched to a target. The true peak, shown separately, tells you whether the file will clip on playback.</p>
<h2>Common confusions</h2>
<p>A beginner may see minus 14 on a loudness meter and think the file is too quiet, because it looks like a small negative number. Loudness targets are usually negative numbers below full scale, and a higher number is louder, not quieter. Another confusion is treating a loudness reading as a peak reading. They answer different questions.</p>
<h2>Why the numbers feel backwards</h2>
<p>Many beginners find loudness numbers counterintuitive, because a larger number on a level meter usually means louder, while many loudness targets are negative. A target of minus fourteen is louder than minus twenty, even though the number is smaller. The easiest way to avoid confusion is to say the target in full, such as minus fourteen LUFS integrated, and to remember that the scale is measured from full scale downward.</p>
<p>Write the target at the top of your project notes, with the standard it refers to. A clear label removes most of the confusion, especially when you return to a project after a break.</p>
<p>When you share a file with a collaborator, state its loudness and the standard used. A bare number without a unit is easy to misread, and a misread target can lead to a file that is too quiet or too loud for its destination.</p>
<h2>Reading a file you did not make</h2>
<p>When you receive a file from someone else, check its loudness and true peak before you edit it. A file that arrives very quiet may have been mixed for a different purpose, and raising it may bring up noise and room tone. A file that arrives very loud may already be limited, and reducing it may not restore the dynamics that were lost. Measure first, then decide what changes are sensible.</p>
<p>Ask the sender what the file is for and what loudness it was intended to reach. A short exchange at the start saves rework, and it makes the final delivery easier to agree.</p>
<h2>Limits</h2>
<p>Loudness standards and the targets used by platforms change over time, so check the current guidance from the platform you publish to. The principles here apply broadly, but the specific numbers belong to the standard in use.</p>
<h2>Check both on the export</h2>
<p>Checking both kinds of reading on the export gives the most reliable result. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the loudness and true peak of a finished file, and the <a href="/tunedzy/blog/how-to-read-a-lufs-meter">LUFS meter guide</a> explains how to read the readings. For the decibel basics, see the <a href="/tunedzy/blog/decibels-explained-for-recording">decibels post</a> in this series.</p>
''',
    faq=[('Are loudness units the same as decibels?', 'No. Loudness units weight the level for how the ear hears, while decibels measure the signal itself.'),
         ('Is a loudness reading of minus 14 quiet?', 'Not necessarily. Loudness targets are negative numbers, and the value describes the target level, not a fault.'),
         ('Which one prevents clipping?', 'The peak reading, in decibels or true peak. Loudness does not show clipping.'),
         ('Which should I match between files?', 'Loudness, so that files sound similarly loud when played one after another.')])

add(slug='why-recording-level-drifts-in-long-sessions', cluster='evergreen-levels', kw='why recording level drifts',
    title='Why Recording Levels Drift in Long Sessions and How to Stop It',
    desc='Why recording levels drift in long sessions: the causes of drift, how to keep the voice steady across an hour, and how to correct drift without damaging the sound.',
    h1='Why Recording Levels Drift in Long Sessions and How to Stop It',
    answer='Levels drift in long sessions because the speaker moves, tires or changes posture, and the room and equipment can also shift. Keep the microphone position fixed, check the level during breaks, and correct drift with gentle gain changes in editing. A steady setup and a short check every so often prevent most of the problem.',
    body='''
<p>A recording that starts well can drift during a long session. The voice grows quieter, or louder, or thinner, and the change is gradual enough that the speaker does not notice. By the end of an hour the sound may be very different from the start. Drift is common, and it is largely preventable with a steady setup and a few simple habits.</p>
<p>This post explains the causes of drift, how to keep a session steady, how to correct drift in editing and when a re-record is the better answer.</p>
<h2>Why levels drift</h2>
<p>Speakers move. They lean back in the chair, turn toward a guest, or shift their weight, and each movement changes the distance to the microphone. Voices also change as the session goes on: the speaker may relax and speak more softly, or tire and lose energy. The room can change too, as the heating comes on, a door opens or a fan starts.</p>
<p>Each change is small, but the cumulative effect can be large. A distance change of a few centimetres can shift the level by several decibels.</p>
<h2>Fix the microphone position</h2>
<p>The most effective fix is a fixed microphone position. Use a stand or boom arm that holds the microphone steady, and mark the position of the speaker’s seat and head. Ask the speaker to stay in the marked position, and remind them during breaks. A fixed setup makes most drift disappear before it starts.</p>
<h2>Check during breaks</h2>
<p>Pause the session every twenty or thirty minutes, and check the level with a short test. Ask the speaker to read a sentence, and compare the level with the start of the session. If the level has moved, adjust the microphone position or the gain before continuing. A short check is much cheaper than discovering drift at the edit.</p>
<h2>Watch the energy</h2>
<p>A speaker who tires may speak more softly and flatly, which lowers the level and thins the voice. Build breaks into the session, and encourage water and short pauses. A rested speaker produces a more consistent performance, and it is easier to keep the level steady.</p>
<h2>Correct drift in editing</h2>
<p>Drift that has already happened can be corrected with gentle gain changes. Split the recording into sections, and level each one to match the start. Use small changes, and check the joins by listening. Avoid lifting the quiet passages so far that the room noise rises with them, and consider light noise reduction on the sections that were quiet.</p>
<h2>When to re-record</h2>
<p>If the drift is large, or if the voice has changed in tone as well as level, correction may not be enough. Re-recording the affected section, with the microphone reset, is often faster and gives a more natural result. Keep the good sections, and replace only the parts that have drifted.</p>
<h2>A simple routine</h2>
<ol>
<li>Mark the microphone and seat positions before the session.</li>
<li>Record a short test at the start, and note the level.</li>
<li>Check the level at each break, and adjust the position if needed.</li>
<li>Build in rest and water for the speaker.</li>
<li>Level the sections in editing, and re-record any section that has changed in tone.</li>
</ol>
<h2>Plan the session in blocks</h2>
<p>A long session is easier to keep steady when it is split into blocks, each with its own setup check. Plan three or four blocks of about twenty minutes, with a short reset between them. At the start of each block, confirm the microphone position, run a short test and note the level. The block structure gives natural points to correct drift, and it stops a small change from growing unnoticed across the whole session.</p>
<p>Keep the blocks consistent from session to session. If the same structure is used each time, the sound of the finished episodes will be more alike, and the editing will follow a familiar pattern. When the blocks look the same across sessions, a change in one of them stands out at once, which makes the drift easier to catch and correct early in the work. Keep the block notes with the session files, so the next session can start from the same structure. Note any block that needed correction, and the reason for it.</p>
<h2>Limits</h2>
<p>Some drift is natural, because voices change with energy and emotion. The aim is to keep the sound consistent enough that listeners do not notice the change, not to remove every variation. A performance with natural dynamics is better than one that has been levelled into flatness.</p>
<h2>Check the level across the session</h2>
<p>A steady check across the session shows whether drift is happening. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps you spot drift in a test. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the loudness of the finished file. For the setup that prevents drift, read the <a href="/tunedzy/blog/how-to-keep-a-podcast-sounding-the-same-every-episode">consistent sound post</a> in this series.</p>
''',
    faq=[('What causes most level drift?', 'Movement of the speaker, which changes the distance to the microphone.'),
         ('How often should I check the level?', 'Every twenty or thirty minutes, and at each break.'),
         ('Can I fix drift in editing?', 'Partly, with gentle gain changes. A large drift may need a re-record.'),
         ('Does the room change the level?', 'Yes, slightly, as heating and doors change the room. Check during the session.')])

add(slug='headphone-volume-and-hearing-safety', cluster='evergreen-levels', kw='headphone volume safe for hearing',
    title='Headphone Volume and Hearing Safety for Audio Work',
    desc='Headphone volume and hearing safety for audio work: how long exposure adds up, how to set a safe level for mixing and recording and what to do if hearing changes.',
    h1='Headphone Volume and Hearing Safety for Audio Work',
    answer='Long exposure to loud sound can damage hearing, and audio work often means hours of listening. Keep headphone levels moderate, take regular breaks, and check your hearing if you notice ringing, muffling or changes that last. A quiet listening level is also more accurate for making decisions about balance and tone.',
    body='''
<p>Audio work involves a great deal of listening, and much of it happens on headphones at close range. A level that feels comfortable for a few minutes can still add up to harm over a long session, and the damage to hearing is often gradual and hard to notice. Protecting your hearing is part of protecting your work, because a fatigued ear makes poor decisions about balance and tone.</p>
<p>This post explains how exposure adds up, how to set a safe level for mixing and recording, how to take breaks and what to do if your hearing changes.</p>
<h2>How exposure adds up</h2>
<p>Hearing damage depends on both the level and the duration of exposure. A higher level causes damage more quickly, and a longer session adds more exposure. The damage can build over many sessions, and it is not always reversible. Many people do not notice the early changes, because the ear adapts to a loud level and makes it feel normal.</p>
<p>Headphones are particularly close to the ear, so a moderate-looking level can be significant. Check your listening level with a meter if your software offers one.</p>
<h2>Set a sensible level</h2>
<p>A common approach is to mix and record at a moderate level, where speech is clear and comfortable without strain. Many professionals work quietly most of the time, and turn up only briefly to check a specific detail. If you find yourself turning up to hear the mix, the mix may need adjusting rather than more volume.</p>
<h2>Why quieter is more accurate</h2>
<p>A moderate level also gives better judgement. At high volume, the ear emphasises the bass and changes the balance of tone, and it tires quickly. A quieter level reveals the true balance of the mix, and it lets you judge the voice and the detail more clearly. Mixing at a lower level is good practice as well as protection.</p>
<h2>Take regular breaks</h2>
<p>Step away from the headphones at regular intervals, especially during long sessions. A break of a few minutes every hour gives the ear time to recover, and it helps you come back with fresh judgement. Many people find that a break makes problems easier to hear when they return.</p>
<h2>Use speakers for checking</h2>
<p>Speakers can be used for a large part of the checking, at a moderate level, with the room providing a more natural sound. Headphones are still valuable, especially for detail, but a mix of speakers and headphones at low to moderate levels is kinder to the ear.</p>
<h2>Watch for warning signs</h2>
<p>Ringing in the ears, a muffled sound after a session, or a sense of fullness that lasts after you stop listening are warning signs. So is any change in hearing that persists for more than a short time. If you notice these, reduce your listening level and rest your ears. If the changes continue, see a doctor or an audiologist.</p>
<h2>A simple routine</h2>
<ol>
<li>Set a moderate level, where speech is clear and comfortable.</li>
<li>Check the mix on speakers at a low to moderate level, when you can.</li>
<li>Take a short break every hour in long sessions.</li>
<li>Turn up only briefly, to check a specific detail.</li>
<li>Seek advice if you notice ringing, muffling or lasting changes in your hearing.</li>
</ol>
<h2>Build a listening habit that protects you</h2>
<p>A simple habit protects both your ears and your judgement: decide the listening level before you start, and write it on a note near the desk. Keep the volume at that level for the whole session, and check the mix at a second, lower level during the final decisions. The lower level exposes balance problems that a loud level hides, and it keeps the ears fresh. Give the ears a few minutes of silence between checks, and the next decision will be clearer. Silence is not wasted time; it is part of the work. Plan that silence into the session, rather than leaving it to chance, and treat it as a deliberate part of the routine.</p>
<p>Consider a rule for the end of the session as well. When the ears feel tired, stop mixing and do the administrative work instead. Tired ears make decisions that you may regret the next day.</p>
<h2>Limits</h2>
<p>General guidance cannot replace a professional assessment of hearing. Hearing needs differ between people, and some are more sensitive than others. If you have concerns about your hearing, speak to a doctor or an audiologist, and treat any lasting change as a reason to seek advice.</p>
<h2>Keep the listening level sensible</h2>
<p>Good decisions come from a comfortable level. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> helps check the loudness of a finished file, so you do not need to turn the volume up to judge it. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. For the balance between checking and comfort, read the <a href="/tunedzy/blog/what-loudness-should-a-voice-over-be">voice-over loudness post</a> in this series.</p>
''',
    faq=[('What level is safe for headphones?', 'Moderate, where speech is clear and comfortable. If you have to turn up to hear, the mix may need adjusting.'),
         ('Why should I mix quietly?', 'It gives more accurate judgement of balance and tone, and it protects your hearing.'),
         ('How often should I take breaks?', 'A few minutes every hour in long sessions is a good habit.'),
         ('What if my ears ring after a session?', 'Reduce the level and rest. If the ringing or muffling lasts, see a doctor or audiologist.')])

add(slug='how-to-match-levels-between-clips', cluster='evergreen-levels', kw='match levels between clips',
    title='How to Match Levels Between Clips and Recordings',
    desc='How to match levels between clips and recordings: setting a shared reference, matching by ear and by meter, and checking the join so each clip sits together.',
    h1='How to Match Levels Between Clips and Recordings',
    answer='Match levels between clips by choosing a shared reference, setting each clip to that reference by ear and by meter, and then checking the joins. Use the average level for balance and the peaks for safety. A final check of the whole sequence catches the differences that a single clip hides.',
    body='''
<p>When several clips or recordings are put together, their levels rarely agree. One interview is quiet, another is loud, and a voice-over recorded on a different day sits lower again. Viewers and listeners notice these jumps, and they reach for the volume control each time. Matching levels is therefore one of the most useful jobs in finishing a project, and it is a skill that improves with practice.</p>
<p>This post explains how to choose a reference, how to match each clip by ear and by meter, how to check the joins and how to keep the matching consistent for future work.</p>
<h2>Choose a shared reference</h2>
<p>Start by choosing a reference level that the whole project will use. A good reference is the level of the cleanest, most typical clip, because it shows how the speech should sound in the finished work. Play that clip at a comfortable listening level, and note its average level and its peaks. Those numbers become the target for every other clip.</p>
<p>Writing the reference in the project notes is essential. A reference that exists only in memory will drift over a long project, and the later clips will not match the earlier ones.</p>
<h2>Match by ear first</h2>
<p>Listening is the best guide, because meters can disagree with what the ear hears. Play each clip in turn, comparing it with the reference, and adjust its gain until the speech sits at the same apparent level. Listen to the whole clip, not just a loud word, and pay attention to the quiet passages. A clip that sounds even but is quiet overall may need more gain than a clip that has a loud word.</p>
<h2>Confirm with the meter</h2>
<p>Once the clips sound matched, confirm the averages on a meter. A large difference in the average level points to a clip that needs a small correction, even if the ear was satisfied. Use the peak meter to check that the adjustment has not pushed any word into clipping. Small corrections are usually enough, and large ones are a sign that the source differs too much.</p>
<h2>Check the joins</h2>
<p>A level match can still sound wrong at the join if the room tone differs. Play each join at normal speed, and listen for a change in background sound, not only in volume. A short crossfade or a matched piece of room tone can smooth the change. The <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade guide</a> explains the method.</p>
<h2>Check the whole sequence</h2>
<p>After matching each clip, play the whole sequence from start to finish, without stopping. Problems that are invisible in a single clip can become obvious in the flow of the project. Note any clip that stands out, and return to it for a small adjustment.</p>
<h2>Keep the matching consistent</h2>
<p>Use the same reference for future projects, so each series sounds like one show. Record the reference level in your template, and check new recordings against it before editing. A consistent reference saves time on every project, and it is one of the simplest ways to make your work sound professional.</p>
<h2>Working with clips from different sources</h2>
<p>Clips that come from different sources need more care than clips from the same session. A clip from a phone, a clip from a studio microphone and a clip from a laptop may all be well made, but they will carry different tonal character and different noise. Matching the level is only the first step. Listen for differences in brightness and warmth, and consider a light, matched EQ on the clip that differs most, so the sequence sounds like one voice in one place. Save the EQ settings with the clip, so the match can be repeated if the clip is re-exported later. Keep the settings close to the reference note, so the match is easy to find when the project is revisited months later.</p>
<p>When the sources differ a great deal, it can help to place the most distinctive clip where the change will feel intentional, such as at the start of a new section. A deliberate change of place is easier for listeners to accept than an unexplained one in the middle of a conversation.</p>
<h2>Limits</h2>
<p>Matching levels cannot fix recordings that differ in tone, distance or room. A clip recorded far from the microphone will not match a close one, however carefully the level is set. In those cases, the better fix is to re-record, or to accept that the difference exists and place the clips where it will be least noticed.</p>
<h2>Check the result</h2>
<p>A final check on the whole project confirms that the levels match. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the loudness and true peak of the finished file, and the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping and level problems in a recording you own. For a related technique, read the <a href="/tunedzy/blog/how-to-keep-audio-levels-consistent-across-video-clips">video clip levels post</a> in this series.</p>
''',
    faq=[('What should I use as the reference?', 'The cleanest, most typical clip in the project, measured for average level and peaks.'),
         ('Should I match by ear or by meter?', 'Both. The ear decides, and the meter confirms the average and checks the peaks.'),
         ('Why do matched clips still sound different?', 'Their tone, distance or room differs. Matching levels cannot fix those differences.'),
         ('How do I keep matching consistent over time?', 'Record the reference in your template, and check every new recording against it.')])
