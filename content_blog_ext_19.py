"""Blog posts, batch 19: audio basics for beginners (evergreen). Merged into content_blog.py.
Evergreen explanations of standard audio concepts. Settings are described generally because menus differ between
apps and versions. No invented statistics. Funnel: each post ends with a link to Tunedzy Go and to the matching free tool."""

CLUSTERS = {
    'evergreen-beginner': dict(tool='vocal-checker', label='Audio basics for beginners', tool_name='Vocal Checker'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='audio-basics-for-complete-beginners', cluster='evergreen-beginner', kw='audio basics for beginners',
    title='Audio Basics for Complete Beginners: The Terms That Matter Most',
    desc='Audio basics for complete beginners: the handful of terms that matter most, from gain and level to sample rate, loudness and monitoring, explained plainly.',
    h1='Audio Basics for Complete Beginners: The Terms That Matter Most',
    answer='Most beginner audio problems come from a few ideas: gain and level, distance to the microphone, room sound, sample rate and bit depth, loudness, and monitoring. Learn those first, and the rest of the vocabulary becomes much easier. You do not need to understand every term to make a clean recording.',
    body='''
<p>Audio has a large vocabulary, and beginners often feel that they must learn all of it before they can record a decent voice. In practice, a small set of ideas explains most of what goes right and wrong. If you understand gain, distance, room sound, sample rate, loudness and monitoring, you can make clean recordings and fix the common problems. The rest of the terms are useful, but they can wait.</p>
<p>This post introduces those core ideas in plain language, in the order a beginner is likely to meet them. Each one has its own deeper post in this series, linked where it helps.</p>
<h2>Level and gain</h2>
<p>Level is how loud a signal is at a given point in the chain. Gain is the amount the signal is boosted before it is recorded. Setting the gain is one of the first decisions in any recording. Too little gain and the voice is quiet, so you must raise it later and bring the noise up with it. Too much gain and the loudest moments clip, which sounds harsh and cannot be fully repaired.</p>
<p>Set the gain with a test. Speak at your normal volume and watch the meter. The loudest words should peak comfortably below the top, with room to spare for a sudden shout or a laugh.</p>
<h2>Distance to the microphone</h2>
<p>Distance changes the sound more than almost any setting. A microphone close to the mouth captures the voice clearly and picks up less of the room. Moving back makes the voice thinner and the room more noticeable. A hand’s width or two is a sensible starting point for most voices, held steady for the whole recording. Mark the position if you can.</p>
<h2>Room sound</h2>
<p>Every room has a sound, made of reflections from the walls, the floor and the ceiling. A bare room with hard surfaces makes an echo, and a soft room makes the voice feel close. You cannot remove room sound completely after recording, so treat the room as part of the setup. Soft furnishings, rugs and curtains are the simplest and cheapest improvements.</p>
<h2>Noise</h2>
<p>Noise is any sound that is not the voice you want. Some noise is steady, such as a fan or a hum. Some is sudden, such as a door or a car. Steady noise is easier to reduce after recording, but the best fix is to switch off the source. Record a few seconds of silence before each session, so you know what the room sounds like with nobody speaking.</p>
<h2>Sample rate and bit depth</h2>
<p>A digital recording stores the sound as a series of measurements. The sample rate is how many measurements are taken each second, and the bit depth is how precise each measurement is. For speech, a common sample rate such as 44.1 or 48 kilohertz is fine, and a 24-bit recording gives plenty of room for editing. Keep the rate you recorded at, rather than converting without reason.</p>
<h2>Loudness</h2>
<p>Loudness is how loud the recording sounds to a listener, measured over time. It is different from the peak, which is only the single loudest moment. Platforms and broadcasters use loudness to match the level of different programmes. A beginner can aim for a steady, comfortable level and check the final file with a loudness meter before publishing.</p>
<h2>Monitoring</h2>
<p>Monitoring is listening to what you record, on headphones or speakers, while you work. Good monitoring tells you what the recording really sounds like, which is why many beginners are surprised by a playback on another device. Listen on headphones while recording and on a phone speaker after, since most people hear recordings that way.</p>
<h2>Learning order</h2>
<ol>
<li>Learn gain and level first, and set them with a test before each session.</li>
<li>Learn distance and room, since they shape the sound more than most settings.</li>
<li>Learn noise, so you can recognise and reduce it.</li>
<li>Learn loudness and monitoring, so the final file sounds right on real devices.</li>
<li>Learn sample rate and bit depth last, and keep the rate you recorded at.</li>
</ol>
<h2>Common beginner mistakes</h2>
<ul>
<li>Recording too quietly and then boosting the noise to compensate.</li>
<li>Letting the voice clip, which cannot be undone.</li>
<li>Recording far from the microphone in a bare room.</li>
<li>Judging a recording only on the headphones or the studio speakers used to make it.</li>
<li>Processing heavily before listening to the raw recording.</li>
</ul>
<h2>Where to go next</h2>
<p>Once these basics feel familiar, the rest of the vocabulary makes more sense. The <a href="/tunedzy/blog/what-is-gain-in-recording">gain post</a> goes deeper into level, and the <a href="/tunedzy/blog/decibels-explained-for-recording">decibels post</a> explains the numbers you will see on meters. Each concept builds on the one before.</p>
<h2>Limits</h2>
<p>These basics are a starting point, not a complete course. Equipment, software and recording goals differ, and each adds its own terms. The principles above apply widely, but a specialist field may need specialist knowledge. Keep practising with your own voice and room, because that is where the learning sticks.</p>
<h2>Practise with a clean test</h2>
<p>A simple test recording is the best teacher. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps you see the basics in your own file. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the wider picture of how to start, read the <a href="/tunedzy/blog/how-to-start-a-podcast-with-a-phone-and-no-budget">phone podcast guide</a> in this series.</p>
''',
    faq=[('Do I need to learn every audio term?', 'No. Learn gain, distance, room, noise, loudness and monitoring first, and the rest can wait.'),
         ('What is the most important beginner setting?', 'The gain, set with a test so the voice peaks well below the top of the meter.'),
         ('Is a good microphone the first thing to buy?', 'Usually not. Position and room matter more than the microphone for most beginners.'),
         ('How long does it take to learn the basics?', 'A few weeks of regular test recordings and listening, with notes on what changed.')])

add(slug='sample-rate-vs-bit-depth-explained', cluster='evergreen-beginner', kw='sample rate vs bit depth',
    title='Sample Rate vs Bit Depth Explained: What Each One Does',
    desc='Sample rate vs bit depth explained: what each number means for a recording, why 44.1 or 48 kilohertz is fine for speech and when a 24-bit file helps.',
    h1='Sample Rate vs Bit Depth Explained: What Each One Does',
    answer='Sample rate is how many times per second the sound is measured, and bit depth is how precisely each measurement is stored. For speech, 44.1 or 48 kilohertz is enough, and 24-bit gives plenty of room for editing. Keep the settings your recording was made at, and avoid converting without a reason.',
    body='''
<p>Two numbers appear in almost every audio file, and beginners often mix them up. The sample rate and the bit depth both describe how a digital recording is stored, but they measure different things. Understanding the difference helps you choose settings with confidence, and it stops you from doing unnecessary conversions that add no quality.</p>
<p>This post explains each number with an analogy, shows what they mean for speech and music, and sets out the simple rules most creators need. The aim is not technical depth but a clear decision.</p>
<h2>What sample rate means</h2>
<p>Sound is a continuous wave, and a digital recording captures it by taking a series of measurements, called samples. The sample rate is how many of those measurements are taken each second. A rate of 44,100 samples per second means the wave is measured 44,100 times every second. A higher rate can capture higher frequencies, which is why the rate matters for the range of sound a recording holds.</p>
<p>Think of it like taking photographs of a moving object. More frames per second show faster movement more accurately. The sample rate sets how fast the sound can be followed.</p>
<h2>What bit depth means</h2>
<p>Each sample is a number, and the bit depth is the number of bits used to store it. More bits allow a finer range of values, so the difference between a quiet sound and a slightly louder one can be captured more precisely. A 16-bit recording has 65,536 possible values for each sample, and a 24-bit recording has far more.</p>
<p>In everyday terms, bit depth sets the dynamic range and the amount of room you have to work with. A 24-bit recording leaves more space below the quiet parts and above the loud ones, which helps when you edit or change the level.</p>
<h2>Which matters more for speech</h2>
<p>For speech, the sample rate of 44.1 or 48 kilohertz is more than enough to capture the voice clearly. Higher rates capture frequencies that the human voice does not produce in a useful way for most listeners. Bit depth matters more during recording and editing, because it gives you headroom to work with, so 24-bit is a sensible choice for a master.</p>
<p>The final delivery is often 16-bit or a compressed format, because that is what many platforms accept. The master can stay at 24-bit, and you can export a smaller version for delivery.</p>
<h2>Which matters more for music</h2>
<p>Music often has more high-frequency content, such as cymbals and some synthesisers, so a higher sample rate is sometimes chosen. Many producers record at 48 kilohertz or higher, and some use higher rates for specific processing. The bit depth matters for the same reason as with speech: headroom during mixing. A 24-bit master is common, with delivery formats chosen for each platform.</p>
<h2>Keep the rate you recorded at</h2>
<p>Changing the sample rate after recording is called resampling, and it adds a conversion step. Each conversion can change the sound slightly, so avoid it unless a platform or a collaborator requires it. Keep the rate at which you recorded, and change it only in the final export if needed.</p>
<h2>A simple rule</h2>
<ol>
<li>Record at 44.1 or 48 kilohertz, and keep that rate through the project.</li>
<li>Record and edit at 24-bit for headroom.</li>
<li>Export a delivery file in the format the platform requires.</li>
<li>Keep the 24-bit master so you can re-export later.</li>
<li>Avoid converting between rates without a reason.</li>
</ol>
<h2>Common confusions</h2>
<p>Many beginners think a higher number always means better sound. That is not true for speech, where the difference between 44.1 and 96 kilohertz is hard to hear on most devices. Another confusion is between bit depth and loudness. Bit depth does not make a recording louder; it changes how finely the level is stored.</p>
<h2>Where the rate matters in editing</h2>
<p>Editing software works on the sample rate of the project, and the rate you choose at the start affects how the file behaves during processing. A plug-in that resamples internally may add a small conversion step, which is why keeping the project and the recording at the same rate is a good habit. If you mix material recorded at different rates, convert it once, deliberately, at the start of the project, rather than letting each track convert on its own.</p>
<p>When a collaborator sends a file at a different rate, check it before you begin. Mismatched rates are a common cause of pitch shifts and crackles that look like a fault in the recording but are really a setup problem.</p>
<h2>Limits</h2>
<p>These rules describe common practice, and the best choices depend on the project, the platform and the equipment. Some specialist work uses higher rates for specific reasons. For most speech and everyday music, the rules above will serve well.</p>
<h2>Check the file you export</h2>
<p>After export, check the file in a player and on a phone to confirm it is what you intended. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the basics that come before this, read the <a href="/tunedzy/blog/audio-basics-for-complete-beginners">beginner basics post</a> in this series.</p>
''',
    faq=[('Is 44.1 kilohertz good enough?', 'Yes, for most speech and many music jobs. 48 kilohertz is also common and fine.'),
         ('Is 24-bit better than 16-bit?', 'For a master that will be edited, yes, because it gives more headroom. Delivery files are often 16-bit.'),
         ('Should I record at the highest rate?', 'Not usually. A higher rate adds file size without a clear benefit for speech.'),
         ('Does bit depth make my recording louder?', 'No. It changes how finely the level is stored, not how loud it sounds.')])

add(slug='what-is-gain-in-recording', cluster='evergreen-beginner', kw='what is gain in recording',
    title='What Is Gain in Recording and How to Set It Right',
    desc='What is gain in recording and how to set it right: gain versus volume, finding the right level and avoiding noise and clipping.',
    h1='What Is Gain in Recording and How to Set It Right',
    answer='Gain is the amount a microphone signal is boosted before it is recorded. Set it so the loudest words peak comfortably below the top of the meter, with room for surprises. Too little gain forces you to boost noise later, and too much clips the voice in a way that cannot be undone.',
    body='''
<p>Gain is one of the first controls a recordist touches, and one of the most misunderstood. Many beginners treat it as a volume knob for the listener, and then wonder why the recording is noisy or distorted. Gain is not the volume of the final file. It is the amount the signal is boosted at the start of the chain, which decides how much of the microphone’s signal reaches the recording.</p>
<p>This post explains the difference between gain and volume, how gain affects noise and distortion, and a simple way to set it correctly for speech and music.</p>
<h2>Gain is not volume</h2>
<p>Volume is what you hear when you play a recording, and you can change it at any time. Gain is applied during recording, and it decides how strong the signal is when it is stored. Once a signal has clipped, turning the volume down does not restore the lost detail. That is why gain must be set before you press record, not fixed later.</p>
<p>Think of gain as the size of the sample you collect. If the sample is too small, you must enlarge it later, which enlarges any flaws too. If it is too big, the top is cut off.</p>
<h2>Too little gain</h2>
<p>A recording with too little gain is quiet, and the beginner often raises the level during editing. Raising a quiet recording also raises its background noise, hiss and room sound. The result is a recording that sounds thin and noisy, even though the voice itself was fine. The fix is to record with more gain, closer to the microphone, rather than relying on boosting later.</p>
<h2>Too much gain</h2>
<p>A recording with too much gain clips when the loudest words exceed the maximum the system can store. Clipping sounds harsh, crackly and distorted, and no software can fully restore the peaks that were cut off. The safe approach is to leave room for sudden loud sounds, such as a laugh, a shout or a plosive pop, which can push the peaks higher than normal speech.</p>
<h2>A simple way to set it</h2>
<ol>
<li>Position the microphone at the distance you will use.</li>
<li>Ask the speaker to talk at their loudest normal volume, or to speak the loudest line of the script.</li>
<li>Raise the gain until the peaks reach the upper part of the meter, but stay well below the top.</li>
<li>Record a short test and listen on headphones.</li>
<li>Lock the setting, and check it at the start of each session.</li>
</ol>
<h2>Gain and the microphone</h2>
<p>Different microphones give different signal levels, and some need more gain than others. A dynamic microphone usually needs more gain than a condenser, which is one reason a dynamic can sound quieter at the same setting. Check the level for each microphone you use, rather than assuming the same setting will work.</p>
<h2>Gain and noise</h2>
<p>Every recording has some noise from the electronics, and more gain brings that noise up along with the voice. The aim is to set the gain high enough that the voice sits well above the noise floor, but not so high that the peaks clip. A close microphone helps, because it gives a stronger signal for the same gain.</p>
<h2>Gain on a phone</h2>
<p>Phones set gain automatically in many recording apps, which can make the first attempt sound fine and the next one different. Some apps raise or lower the level on their own as you speak, so a quiet passage may be boosted and a loud one held back. Check whether your app has an automatic level control, and if it does, test whether you prefer it or a fixed setting. A fixed level gives a steadier sound across a long recording.</p>
<p>When you record on a phone, keep the phone at a steady distance and set the level with a short test first. The automatic behaviour is only a substitute for a steady setup, not a replacement for one.</p>
<p>A practical habit is to note the gain setting next to each session in your project notes, along with the microphone and the distance. When a later recording sounds different, the notes show whether the gain changed, the position moved or the room was different. Over time, the notes become a reliable template, and the first test of each session takes less time.</p>
<h2>Limits</h2>
<p>Gain settings vary between interfaces, microphones and recording software, and the controls may be labelled differently. The principle is the same across all of them. Learn the principle, then find the control on your own equipment.</p>
<h2>Set the level with a clean test</h2>
<p>A short test recording shows you whether the gain is right. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps you judge a test. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the wider basics, read the <a href="/tunedzy/blog/audio-basics-for-complete-beginners">beginner basics post</a> in this series.</p>
''',
    faq=[('Is gain the same as volume?', 'No. Gain is applied during recording, while volume is how loud you hear the file.'),
         ('Can I fix a quiet recording by turning up the volume?', 'You can make it louder, but you also raise the noise. Record at a better gain next time.'),
         ('What if my recording clips?', 'Clipping cannot be fully repaired. Re-record with lower gain, leaving room for sudden peaks.'),
         ('Where should the peaks sit?', 'Comfortably below the top of the meter, with room for surprises such as laughs or pops.')])

add(slug='what-is-a-preamp', cluster='evergreen-beginner', kw='what is a preamp',
    title='What Is a Preamp? A Plain Explanation for Beginners',
    desc='What is a preamp? A plain explanation for beginners: what a microphone preamp does, why microphones need one, how it affects noise and how to choose one.',
    h1='What Is a Preamp? A Plain Explanation for Beginners',
    answer='A preamp, short for preamplifier, boosts the weak signal from a microphone to a level that can be recorded. Microphones produce very small signals, so a preamp is essential for most microphones. Built-in preamps in interfaces and phones do this job, and their quality affects how clean the recording sounds.',
    body='''
<p>The word preamp appears in almost every discussion of recording equipment, and beginners often do not know what it does. The short answer is that a microphone produces a very weak signal, and a preamp boosts it to a level that the recording system can use. Without a preamp, most microphones would be almost silent. The preamp is part of the signal chain that decides how clean the recording sounds.</p>
<p>This post explains what a preamp does, why it matters for noise, where preamps appear in common setups and what to check when choosing one. The explanation is general, and specific devices vary.</p>
<h2>What a preamp does</h2>
<p>A microphone converts sound into an electrical signal, and that signal is very small, often much smaller than a line-level signal from a music player. A preamp amplifies the microphone signal to a useful level, without changing its character more than necessary. The gain control on an interface usually sets how much the preamp boosts the signal.</p>
<p>Think of the preamp as the first amplifier in the chain. Every later stage works on what the preamp provides, so its quality affects everything that follows.</p>
<h2>Why microphones need one</h2>
<p>Different microphones produce different signal strengths. Dynamic microphones usually need more boost than condensers, and some need a great deal. Condenser microphones need power as well as a preamp, which is why phantom power is often supplied by the same device. Without a preamp, a microphone is simply too quiet to record cleanly.</p>
<p>The amount of boost needed is one reason a microphone can sound noisy at high gain. The preamp is the source of most of the electrical noise in a basic setup.</p>
<h2>Where preamps appear</h2>
<p>Preamps are built into many devices. An audio interface has preamps for each input. A mixer has them for each channel. A phone has a preamp for its built-in microphone, and a USB microphone contains its own. Standalone preamps are also sold, usually for people who want a particular sound or who need more quality than their interface offers.</p>
<h2>Noise and quality</h2>
<p>A good preamp adds very little noise, so the voice sits clearly above the noise floor even at high gain. A weaker preamp can add hiss, especially at high gain, which is most noticeable in quiet passages. The difference is often small with modern equipment, but it is real, and it matters more for quiet sources.</p>
<h2>Do you need a separate preamp?</h2>
<p>Most beginners do not need a separate preamp. A decent interface or a USB microphone will give a clean result for speech. A standalone preamp becomes worth considering when you have a specific microphone that needs more quality, when you want a particular character, or when your interface’s preamps are limiting your work. Test your current setup before you spend money.</p>
<h2>What to check when choosing</h2>
<ul>
<li>Enough gain for the microphones you own, especially dynamic microphones.</li>
<li>Low noise at the gain you will use most often.</li>
<li>The number of inputs you need, now and in the near future.</li>
<li>Phantom power, if you use condenser microphones.</li>
<li>A clear gain control, so the setting is repeatable.</li>
</ul>
<h2>Preamps in phones and laptops</h2>
<p>A phone or laptop has a preamp for its built-in microphone, and the quality of that preamp varies between devices. Many modern devices produce clean speech at close range, which is why a phone can be a useful recorder. The limit is usually the distance and the room rather than the preamp itself, so a steady, close position still matters most.</p>
<p>When you connect an external microphone to a phone or laptop, check whether the input provides enough gain. A microphone that sounds quiet on a computer may simply need a stronger preamp, which is one reason an interface is sometimes worth buying.</p>
<p>When you compare two preamps or two interfaces, use the same microphone, the same distance and the same room, and record the same passage with each. Listen on headphones at the same playback level. Differences in noise are easiest to hear in the quiet pauses, so listen there first. A short, controlled comparison tells you far more than any written specification. Keep the result with your notes, so the comparison is available when you next consider a purchase.</p>
<h2>Limits</h2>
<p>Preamp quality is one factor among many. The microphone position, the room and the recording level often matter more to the final sound. Claims about the character of particular preamps are subjective, and the best choice is the one that sounds right for your voice in your room.</p>
<h2>Start with the basics</h2>
<p>Before you think about preamps, get the gain and distance right. The <a href="/tunedzy/blog/what-is-gain-in-recording">gain post</a> explains the setting. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the wider basics, read the <a href="/tunedzy/blog/audio-basics-for-complete-beginners">beginner basics post</a>.</p>
''',
    faq=[('Does every microphone need a preamp?', 'Almost every microphone needs one, either built in or separate, to reach a usable level.'),
         ('Is a built-in preamp good enough?', 'For most speech recording, yes. Test it with your microphone and room.'),
         ('Can a preamp make my voice sound better?', 'It can add character and reduce noise, but position and room matter more for most beginners.'),
         ('Do phones have preamps?', 'Yes. The built-in microphone and the phone’s electronics handle the same job.')])

add(slug='microphone-frequency-response-explained', cluster='evergreen-beginner', kw='microphone frequency response',
    title='Microphone Frequency Response: What the Chart Really Tells You',
    desc='Microphone frequency response explained: what the chart shows, why a flat response is not always best for voice, and how to use the chart when choosing a microphone.',
    h1='Microphone Frequency Response Explained: What the Chart Really Tells You',
    answer='A microphone frequency response chart shows how sensitive the microphone is across the range of sound, from low to high frequencies. A flat chart is not always the best choice for voice, because some microphones are shaped on purpose to flatter speech. Use the chart as one guide, and judge the microphone on how your own voice sounds.',
    body='''
<p>Almost every microphone comes with a frequency response chart, a line that shows how sensitive the microphone is at different pitches. Beginners often take that chart as the measure of quality, and they assume a flat line is always best. The chart is useful, but it does not tell the whole story. It shows what the microphone picks up, not how a particular voice will sound in a particular room.</p>
<p>This post explains what the chart shows, how to read it, why a flat response is not always the goal for voice, and how to use the chart when choosing a microphone.</p>
<h2>What the chart shows</h2>
<p>A frequency response chart plots the microphone’s sensitivity, usually in decibels, against frequency, from the lowest bass to the highest treble. A line that stays level across the range indicates an even response. Peaks in the line show frequencies the microphone emphasises, and dips show frequencies it reduces. The chart is usually measured under controlled conditions, often on a test bench rather than in a real room.</p>
<p>The result tells you how the microphone responds to different pitches, which is useful information. It does not describe the room, the distance or the voice.</p>
<h2>Why flat is not always the goal</h2>
<p>A perfectly flat microphone captures sound accurately, which is valuable for measurement and for recording instruments that must be heard exactly. For speech, many people prefer a microphone that adds a little warmth in the low middle range, or a slight presence boost in the upper middle, which makes the voice clear and close. Some microphones are designed with that kind of shaping, and it can suit a voice well.</p>
<p>A flat chart can also make a bright or harsh voice sound harsher, while a shaped response may flatter it. The chart cannot tell you which will suit your voice best.</p>
<h2>Proximity and distance</h2>
<p>Many directional microphones change their low-frequency response when you move closer, an effect called proximity. The bass rises as the microphone gets nearer to the mouth, which can make a voice boomy. The chart often shows the response at a fixed distance, so the sound you hear will change with your position. Keep the distance steady, and test the sound at the distance you will use.</p>
<h2>Polar pattern</h2>
<p>The chart may come with a polar pattern, which shows how the microphone responds to sound from different directions. A cardioid pattern rejects sound from behind, which helps reduce room noise and echo. That pattern is often more important for home recording than a small difference in the frequency line.</p>
<h2>How to use the chart</h2>
<ol>
<li>Look at the overall shape, and note any strong peaks or dips.</li>
<li>Check the polar pattern, especially for recording in an untreated room.</li>
<li>Read the note about distance, if the chart is measured at a fixed distance.</li>
<li>Compare two or three microphones with similar charts, and listen to them.</li>
<li>Choose on your own voice, in your room, at your distance.</li>
</ol>
<h2>What the chart cannot tell you</h2>
<p>The chart cannot tell you how the microphone will feel to use, whether it handles plosives well, how it reacts to a particular voice or how it sounds in your room. It also cannot tell you about noise, sensitivity or durability. Those factors often matter as much as the frequency line, and they can only be judged by listening and using the microphone.</p>
<h2>Reading two charts side by side</h2>
<p>A useful exercise is to lay two charts side by side and compare the shapes, not the single line. Look at where each microphone rises and falls in the speech range, and ask which shape suits the voice you record most. A rise in the upper middle may add presence to a soft voice but harshness to a bright one. Keep a note of the comparison, so you can recall why you chose a microphone when the question comes up again.</p>
<p>Remember that the chart is measured on a test rig, and your room will add its own shape. The difference between two microphones may be smaller in a real room than the charts suggest, or it may be larger if one microphone is much more sensitive to reflections.</p>
<h2>Limits</h2>
<p>Frequency response charts vary in how they are measured, and claims based on them can be misleading. Use the chart as one piece of evidence, and do not treat it as a ranking of quality. The best microphone is the one that suits your voice and your room.</p>
<h2>Test the microphone you own</h2>
<p>A simple test recording reveals how your microphone and voice work together. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps you judge a test. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For how to choose a microphone for home voice work, read the <a href="/tunedzy/blog/what-microphone-to-use-for-voice-over-at-home">microphone guide</a> in this series.</p>
''',
    faq=[('Is a flat response always best?', 'Not for voice. Some shaping can flatter speech, depending on the voice and the room.'),
         ('Why does my voice sound boomy up close?', 'Proximity boosts the bass on some microphones. Move slightly back or adjust the distance.'),
         ('Should I trust the chart?', 'Use it as one guide. Listen to the microphone with your own voice before deciding.'),
         ('What is the most useful part of the chart?', 'The overall shape and the note about distance and polar pattern.')])

add(slug='decibels-explained-for-recording', cluster='evergreen-beginner', kw='decibels for beginners',
    title='Decibels Explained for Recording: The Numbers on Every Meter',
    desc='Decibels explained for recording: what dB means, why the scale is logarithmic, what dBFS and dB headroom mean and how to read the numbers on a meter.',
    h1='Decibels Explained for Recording: The Numbers on Every Meter',
    answer='A decibel is a logarithmic unit that compares one level with another. In recording, dBFS measures level relative to the digital maximum, where zero is the top and quieter levels are negative numbers. Learn that the scale is logarithmic and that zero dBFS is the clipping point, and most meters become easy to read.',
    body='''
<p>Every meter in a recording setup shows numbers in decibels, usually written as dB, and the scale can look confusing. Beginners see negative numbers, read them as a sign of trouble and wonder why the meter reads minus something when the recording seems fine. The scale is not complicated once you understand two ideas: it is relative, and it is logarithmic. This post explains both, with the common recording terms.</p>
<p>The aim is to make the numbers on your meter meaningful, so you can set levels with confidence rather than guessing.</p>
<h2>What a decibel is</h2>
<p>A decibel is a way of comparing two levels. It is not an absolute amount, but a ratio expressed on a logarithmic scale. A change of a few decibels is a noticeable change in level, while a change of many decibels is large. Because the scale is logarithmic, equal steps in decibels represent equal ratios, which matches how the ear perceives loudness roughly.</p>
<p>That is why the numbers do not add up in the way beginners expect. Doubling the power is about three decibels, and halving it is about minus three.</p>
<h2>dBFS: the digital scale</h2>
<p>Most recording software shows levels in dBFS, which means decibels relative to full scale. Full scale is the maximum level the digital system can store. Zero dBFS is the top, and any level above it is clipping and cannot be stored. All normal levels are therefore negative numbers, such as minus 12 or minus 18, which simply means they sit below the maximum.</p>
<p>The negative numbers are not a sign of a problem. They are the normal place for speech to sit, with headroom below zero for sudden peaks.</p>
<h2>Headroom in decibels</h2>
<p>Headroom is the distance between your loudest peaks and zero dBFS. If the peaks reach minus 6, you have six decibels of headroom. A few decibels is a sensible margin for speech, and it protects the recording from sudden loud sounds. The <a href="/tunedzy/blog/how-much-headroom-to-leave-in-audio">headroom post</a> explains how much to leave for different material.</p>
<h2>Peak and average</h2>
<p>A peak meter shows the single loudest moment, while an average or loudness meter shows the level over a period. Speech has large peaks and a lower average, so the two readings can differ a lot. Set your recording level by watching the peaks, to avoid clipping, and check loudness on the final file, to match a target.</p>
<h2>Decibels in everyday terms</h2>
<p>A difference of about three decibels is just noticeable to most listeners, and a difference of about ten decibels is widely heard as roughly twice as loud. These are rules of thumb, not exact laws, and they depend on frequency and context. Use them as a guide to how much a change will matter.</p>
<h2>Reading a typical meter</h2>
<ol>
<li>Find zero dBFS, the top of the meter, where clipping starts.</li>
<li>Watch the peaks of speech, and keep them comfortably below zero.</li>
<li>Check the average level, if your meter shows it, for the overall balance.</li>
<li>Look at the noise floor, the level of the quiet parts, to judge the room.</li>
<li>Use a loudness meter on the final file to check against your target.</li>
</ol>
<h2>Common confusions</h2>
<p>Many beginners think minus numbers mean the recording is too quiet. They do not. A recording at minus 18 is normal. Another confusion is between peak and loudness. A peak can be high while the loudness is modest, which is why both readings are useful.</p>
<h2>Decibels on a phone</h2>
<p>Phone recording apps often show levels on a simpler scale, with coloured bars or a single bar that rises and falls. The principle is the same as a digital meter, with the top of the scale marking the point of clipping. Learn where the top sits on your app, and keep the voice well below it, even if the app does not show the numbers you expect.</p>
<p>When a phone app does show decibels, compare its readings with a desktop meter using the same recording. A difference between the two usually reflects the way each one averages the signal, not a fault in the recording.</p>
<p>When you read a meter during a session, look at the peaks and the quiet parts together. The peaks tell you about clipping, and the quiet parts tell you about the noise floor. A healthy recording has peaks that stay clear of the top and a quiet floor that stays well below the voice. If either drifts over the session, check the distance and the room before adjusting the gain.</p>
<h2>Limits</h2>
<p>Meters differ in how they measure, and some show peak, some RMS and some loudness. Check which measure your meter uses before comparing readings across programs. The principles above apply to most setups.</p>
<h2>Set the level, then listen</h2>
<p>A meter is a guide, and your ears make the final decision. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the loudness of a finished file. For the level basics, read the <a href="/tunedzy/blog/what-is-gain-in-recording">gain post</a> in this series.</p>
''',
    faq=[('Why are my levels negative numbers?', 'Because they sit below the digital maximum, which is zero dBFS. Negative numbers are normal.'),
         ('What does zero dBFS mean?', 'It is the maximum level the system can store. Anything above it clips.'),
         ('How much headroom should I leave?', 'A few decibels for speech is a sensible margin, more for loud or processed material.'),
         ('Is a peak meter enough?', 'For avoiding clipping, yes. For overall loudness, check a loudness reading on the final file.')])

add(slug='what-is-audio-latency', cluster='evergreen-beginner', kw='audio latency explained',
    title='Audio Latency Explained: Why Your Voice Comes Back Late',
    desc='Audio latency explained: what causes the delay between speaking and hearing yourself, why it matters for monitoring and how to reduce it.',
    h1='Audio Latency Explained: Why Your Voice Comes Back Late',
    answer='Latency is the delay between a sound going into a system and coming back out. It comes from the time the computer and the interface need to process the audio. Latency makes monitoring feel strange and makes singing or playing hard. Reduce it with a smaller buffer size and a suitable driver, and monitor the microphone directly where possible.',
    body='''
<p>Many beginners notice an odd effect when they record: they speak into the microphone and hear their own voice a moment later in the headphones. The delay is called latency, and it can make the recording experience strange, tiring or impossible for singers and instrumentalists. The good news is that latency has clear causes, and most of them can be reduced with a few settings and habits.</p>
<p>This post explains where latency comes from, why it matters for different kinds of work, how to reduce it and when a delay is simply part of the process.</p>
<h2>What causes latency</h2>
<p>Latency is the time it takes for a sound to travel through the system: from the microphone into the interface, into the computer, through the software and back out to the headphones. Each step takes a small amount of time, and the total is the delay you hear. The computer needs time to collect audio into blocks before it processes them, and that collection is one of the largest causes of delay.</p>
<p>Latency is not caused by the distance the sound travels, which is negligible. It comes from the processing time of the system.</p>
<h2>Why it matters</h2>
<p>For speech, a small delay is annoying but often manageable. For singing and playing, a delay makes it hard to stay in time, because the voice or the instrument seems to lag behind what you hear. Many singers find that even a few milliseconds of delay is distracting, and the effect can make the performance feel out of sync.</p>
<p>Latency can also affect editing and overdubbing, where a recording must line up with existing material. Compensation tools exist for that, but it is simpler to avoid the problem during recording.</p>
<h2>Buffer size and latency</h2>
<p>The buffer size is the amount of audio the computer collects before processing it. A smaller buffer gives lower latency, but it demands more from the computer, and it can cause crackles if the system cannot keep up. A larger buffer is more stable, but it adds delay. The usual approach is to use the smallest buffer that runs without crackles, and to increase it only when the system needs it.</p>
<p>Your audio driver also affects latency. Dedicated drivers from the interface maker are usually better than general drivers, because they are designed for low delay.</p>
<h2>Direct monitoring</h2>
<p>Many interfaces offer direct monitoring, which sends the microphone signal straight to the headphones without passing through the computer. That removes most of the latency from monitoring. The recording still goes through the computer, but you hear the live voice without the delay. Direct monitoring is one of the most useful features for singers and speakers.</p>
<p>When you use direct monitoring, remember that you are hearing the input, not the recording. Any effects added in the software may not be heard during monitoring.</p>
<h2>Reducing latency in practice</h2>
<ol>
<li>Use the interface’s dedicated driver, and keep it updated.</li>
<li>Choose the smallest buffer size that runs without crackles.</li>
<li>Close programs you do not need, to give the computer more room.</li>
<li>Use direct monitoring for speech and singing where your interface offers it.</li>
<li>Test the delay with a short recording, and listen to how it feels.</li>
</ol>
<h2>When a delay is normal</h2>
<p>Some delay is unavoidable, especially with network connections, video calls and some streaming setups. A call or stream may add seconds of delay, which is a property of the network and the platform rather than the audio setup. Know which kind of delay you are dealing with before trying to fix it.</p>
<h2>Latency in video calls</h2>
<p>Video calls add their own delay, which comes from the network, the server and the software on each side. Speakers on a call often hear each other a fraction of a second late, and that delay can make conversation feel awkward. Keep the audio path short, use headphones to avoid echo and speak with a small pause between turns. None of these reduce the network delay itself, but they make the conversation easier to manage.</p>
<p>If the delay becomes a problem during a recorded call, record locally on each side. A local recording is not affected by the network, and the two tracks can be aligned later.</p>
<p>A simple check for latency is to clap once and listen for the echo in your headphones. If you hear a faint second clap, the monitoring path is adding delay. Try the same test with direct monitoring turned on, and compare. The difference is often clear enough to decide the setting in a few seconds, without any measurement.</p>
<h2>Limits</h2>
<p>Settings and menus for latency differ between interfaces, computers and software, and the exact steps change. The principles are stable: smaller buffers reduce delay, and direct monitoring removes most of it. Check the documentation for your own setup.</p>
<h2>Test the setup before a session</h2>
<p>A short test shows whether the delay is acceptable. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the wider setup, read the <a href="/tunedzy/blog/audio-basics-for-complete-beginners">beginner basics post</a> in this series.</p>
''',
    faq=[('Why do I hear myself late?', 'The system takes time to process the audio. Use direct monitoring or a smaller buffer.'),
         ('Is a smaller buffer always better?', 'Only if the system can keep up. Too small a buffer causes crackles.'),
         ('Does latency affect recordings?', 'The recording is usually aligned, but it can make performing harder. Direct monitoring helps.'),
         ('Do video calls have latency?', 'Yes, from the network and the platform. That delay is different from interface latency.')])

add(slug='mono-vs-stereo-recording-explained', cluster='evergreen-beginner', kw='mono vs stereo recording',
    title='Mono vs Stereo Recording: Which Should You Use and Why',
    desc='Mono vs stereo recording explained: what each one captures, why most speech works in mono, when stereo helps and how to check the result.',
    h1='Mono vs Stereo Recording: Which Should You Use and Why',
    answer='Mono records one channel, and stereo records two, giving a sense of left and right. Most speech works well in mono, because a single voice has no stereo image to keep. Use stereo when the position of sound matters, such as with instruments, ambience or a deliberately spatial mix, and check that the mono version still works.',
    body='''
<p>Choosing between mono and stereo is one of the first decisions in a recording, and many beginners pick stereo because it sounds more professional. The right choice depends on what you are recording. A single voice rarely benefits from stereo, while a room, a band or a spatial piece can gain a great deal. Understanding the difference helps you choose the format that serves the sound, not the one that simply sounds impressive.</p>
<p>This post explains what each format captures, why mono is often the right choice for speech, when stereo adds value and how to check that a recording works in both.</p>
<h2>What mono means</h2>
<p>A mono recording has one channel. Everything in the recording comes from a single point in the sound field, and the playback system sends the same signal to both speakers or both ears. For a single voice, that is natural, because a person speaking has one sound source. A mono file is also smaller, and it is easier to listen to on any device.</p>
<p>Mono has no sense of left and right. That is not a weakness for speech. It is simply the right description of a single source.</p>
<h2>What stereo means</h2>
<p>A stereo recording has two channels, usually left and right, and it can place sounds at different points between them. A drum kit can be spread across the stereo field, a guitar can sit on one side, and a room can feel wide. Stereo gives a sense of space and of separate sources, which helps when the recording contains more than one source.</p>
<p>Stereo also doubles the file size and requires a stereo microphone or two microphones placed carefully, which adds cost and complexity.</p>
<h2>When mono is the right choice</h2>
<ul>
<li>Speech from one person or a single voice-over.</li>
<li>Interviews and podcasts, where each voice is one source.</li>
<li>Recordings for phones and mono speakers, where stereo would add nothing.</li>
<li>Any recording where the position of sound does not carry meaning.</li>
</ul>
<h2>When stereo helps</h2>
<ul>
<li>Recordings of instruments that benefit from a spread across the field.</li>
<li>Field recordings and room ambience, where the sense of space is part of the sound.</li>
<li>Music mixes, where separate parts sit at different positions.</li>
<li>Spatial or immersive work that depends on position.</li>
</ul>
<h2>Check both versions</h2>
<p>If you record in stereo, check that the mix also works in mono. Some sounds can cancel out when the channels are summed to mono, and a voice or a bass can thin away. Listen to the mono sum on a phone speaker, which is often mono, and fix any element that disappears. A mix that works in both is more robust.</p>
<h2>A stereo microphone or two microphones</h2>
<p>Recording in stereo can use a single stereo microphone, or two microphones placed in a pattern. The placement affects the image and the phase relationship between the channels. Beginners should start simply, with one microphone for speech, and move to stereo only when the source needs it.</p>
<h2>Mono on a phone speaker</h2>
<p>Most phone speakers play a mono sum, so a stereo recording is heard as mono in many situations. A speech recording made in stereo therefore loses nothing on a phone, but it also gains nothing. A music mix made in stereo should be checked in mono first, because elements that depend on the difference between the channels may thin out or disappear. Checking in mono is one of the simplest ways to catch problems that a stereo monitor hides.</p>
<p>For a voice recorded in mono, the phone check is simpler: the voice is the same on every device, so the level and the clarity are all that need attention.</p>
<p>A common error is recording in stereo out of habit and then discovering that the two channels are almost identical. If the left and right tracks match, the file is effectively mono and only doubles the size. Check the channels on a meter before a long session, and switch to mono if the stereo image is not doing any work. Mono files are also easier to send to collaborators and to publish on platforms that expect one channel.</p>
<h2>Limits</h2>
<p>The choice between mono and stereo depends on the material and the listening context. Some producers record a voice in stereo for effect, and some mix mono sources into a stereo field. The rules above are a starting point, not a fixed law. Test the result on the devices your listeners use.</p>
<h2>Start simple and check the result</h2>
<p>For most speech, a clean mono recording is the strongest choice. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the basics that come before this, read the <a href="/tunedzy/blog/audio-basics-for-complete-beginners">beginner basics post</a>. For a wider stereo technique, see the <a href="/tunedzy/blog/making-a-stereo-mix-sound-wider">stereo width post</a>.</p>
''',
    faq=[('Should I record speech in stereo?', 'Usually not. A single voice is one source, and mono is simpler and smaller.'),
         ('Does mono sound worse?', 'Not for speech. The voice is one source, and mono often sounds more solid on small speakers.'),
         ('How do I check a stereo mix?', 'Sum it to mono and listen for elements that thin out or disappear.'),
         ('Can I convert stereo to mono?', 'Yes. Check the result, because summing can cancel some sounds.')])

add(slug='what-does-a-compressor-do', cluster='evergreen-beginner', kw='what does a compressor do',
    title='What Does a Compressor Do? A Beginner’s Explanation',
    desc='What does a compressor do? A beginner explanation: how compression reduces the gap between loud and quiet, the main controls and how to use it gently on speech.',
    h1='What Does a Compressor Do? A Beginner Explanation',
    answer='A compressor reduces the gap between the loudest and quietest parts of a sound. When the signal rises above a threshold, the compressor turns it down by a set ratio. On speech it can even out the level and keep quiet words audible, but used too hard it makes the voice sound flat and lifeless.',
    body='''
<p>Compression is one of the most common tools in audio, and one of the most misunderstood. Beginners often use it as a way to make everything louder, and then find that the voice sounds flat, tiring or squashed. A compressor is better understood as a tool for controlling the gap between loud and quiet, which can make speech easier to hear, but only when it is used with restraint.</p>
<p>This post explains what a compressor does, the main controls, the common settings for speech and the mistakes to avoid. It is a beginner guide, and the principles apply across many compressors.</p>
<h2>The basic job</h2>
<p>A compressor watches the level of the signal. When the level rises above a set threshold, the compressor reduces the gain by an amount set by the ratio. The louder the signal above the threshold, the more it is reduced. The result is that loud parts are turned down, and the overall range becomes narrower. Quiet parts are not changed, so they can be raised later with gain.</p>
<p>Think of it as a hand on a volume knob that gently pulls down the loudest moments, so the rest can be turned up without the peaks clipping.</p>
<h2>The main controls</h2>
<ul>
<li><strong>Threshold:</strong> the level above which compression starts.</li>
<li><strong>Ratio:</strong> how much the signal is reduced above the threshold. A ratio of 2 to 1 is gentle, and higher ratios are firmer.</li>
<li><strong>Attack:</strong> how quickly the compressor reacts when the level rises.</li>
<li><strong>Release:</strong> how quickly it recovers when the level falls.</li>
<li><strong>Makeup gain:</strong> a boost to restore the overall level after compression.</li>
</ul>
<h2>Why speech uses compression</h2>
<p>Speech has large differences between loud and quiet words, and listeners may need to adjust the volume to hear the quiet ones. A gentle compressor can reduce those differences so the voice is easier to follow on a phone or in a car. The effect is strongest on speakers who vary their volume a lot.</p>
<p>The aim is a natural, steady voice, not a squashed one. A small amount of compression often does more good than a large amount.</p>
<h2>Settings for speech</h2>
<ol>
<li>Start with a gentle ratio, around 2 to 1 or 3 to 1.</li>
<li>Set the threshold so that the compressor works on the loudest words, reducing only a few decibels.</li>
<li>Use a medium attack, slow enough to keep the start of words, and a release that lets the voice breathe.</li>
<li>Add makeup gain to restore the level, and compare with the original.</li>
<li>Listen for pumping and flatness, and reduce the amount if you hear them.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Using a high ratio and a low threshold, which squashes the voice.</li>
<li>Setting an attack so fast that the start of words is lost.</li>
<li>Setting a release so fast that the level pumps with each word.</li>
<li>Judging the compression only by how loud it makes the file.</li>
<li>Using compression to fix problems that should be solved by distance or gain.</li>
</ul>
<h2>Compression and loudness</h2>
<p>Compression can make a file sound louder, but it also reduces the dynamic range, which can make it feel tired. A recording that is compressed heavily to hit a loudness target may sound worse than one that is lightly compressed and then levelled. Use compression for the shape of the voice, and check the final loudness separately.</p>
<h2>Compression on a voice you already like</h2>
<p>If a recording already sounds good, compression should barely change it. A useful test is to set the compressor so it only touches the loudest words, reduce the amount until the change is hard to hear, and then compare the two versions. If you cannot tell them apart on headphones and a phone, the compressor is doing its job quietly. If the voice has become smaller or tighter, the setting has gone too far.</p>
<p>Keep a copy of the uncompressed version. Compression is easy to add later, but hard to remove once the voice has been squeezed and the original detail has been lost.</p>
<p>Attack and release are easier to understand by listening than by reading about them. Set a fast attack on a spoken phrase and listen for the start of each word being softened. Then slow the attack and listen again, until the consonants feel present. Repeat with the release, and notice how a quick release makes the voice seem to breathe between words, while a slow one smooths the whole phrase.</p>
<h2>Limits</h2>
<p>Compressors differ in their character, and the same settings will sound different on different units. Use the principles above as a starting point, and adjust by ear. Compression is a matter of taste and of the material, and the best setting is the one that makes the voice clear and natural.</p>
<h2>Listen before and after</h2>
<p>The clearest way to learn compression is to listen to a voice with and without it, at the same level. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can show the loudness of the final file, and the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. For the wider level basics, read the <a href="/tunedzy/blog/what-is-dynamic-range-in-speech-audio">dynamic range post</a> in this series.</p>
''',
    faq=[('Does a compressor make my voice louder?', 'It reduces the loud parts, which lets the level be raised. It is not a loudness button.'),
         ('What ratio should I use for speech?', 'A gentle ratio, around 2 to 1 or 3 to 1, is a sensible start for most voices.'),
         ('Why does my voice sound flat?', 'The compression is too strong, or the ratio is too high. Reduce the amount and listen.'),
         ('Should I compress while recording?', 'Usually it is safer to record without heavy compression, and apply gentle compression afterwards.')])

add(slug='what-is-eq-and-how-to-use-it-gently', cluster='evergreen-beginner', kw='what is eq in audio',
    title='What Is EQ in Audio and How to Use It Gently',
    desc='What is EQ in audio and how to use it gently: boosting and cutting frequencies, the common problem areas in speech and a simple way to make small changes.',
    h1='What Is EQ in Audio and How to Use It Gently',
    answer='EQ, short for equalisation, boosts or cuts the level of particular frequencies. It shapes the tone of a sound. For speech, small cuts can reduce muddiness or harshness, and small boosts can add clarity or warmth. Use EQ gently, make one change at a time, and check it against the original.',
    body='''
<p>Equalisation, usually called EQ, is one of the most used tools in audio. It changes the balance of frequencies in a sound, making it brighter, darker, warmer or thinner. Beginners often reach for EQ to fix every problem, and they end up with a voice that sounds artificial. Used gently, with a clear purpose, EQ is a powerful way to shape a voice. Used heavily, it damages the sound.</p>
<p>This post explains what EQ does, the frequency areas that matter most for speech, a simple way to find problems and the restraint that keeps the voice natural.</p>
<h2>The basic idea</h2>
<p>Every sound is made of many frequencies, from the deep bass to the high treble. EQ lets you raise or lower the level of a band of those frequencies. A boost makes that band louder, and a cut makes it quieter. The range of frequencies affected depends on the filter, and the width of the band depends on its setting.</p>
<p>The effect is a change in tone. A voice can sound fuller, thinner, closer or more distant, depending on which bands are changed.</p>
<h2>Areas that matter for speech</h2>
<ul>
<li><strong>Low end, below about 100 hertz:</strong> rumble and handling noise, often best cut gently with a high-pass filter.</li>
<li><strong>Low middle, roughly 150 to 300 hertz:</strong> warmth or boxiness, depending on the voice.</li>
<li><strong>Middle, roughly 1 to 3 kilohertz:</strong> clarity and presence, which help words stand out.</li>
<li><strong>Upper middle, roughly 3 to 6 kilohertz:</strong> harshness or edge, where a cut can help a bright voice.</li>
<li><strong>High, above about 8 kilohertz:</strong> air and breath, which can add openness when lifted gently.</li>
</ul>
<h2>A simple way to find problems</h2>
<ol>
<li>Boost a narrow band by a few decibels, and sweep it across the range.</li>
<li>Listen for the band that sounds most unpleasant, such as a honk, a harsh edge or a boom.</li>
<li>Cut that band by a small amount, and compare with the original.</li>
<li>Repeat for any other problem you hear, changing one thing at a time.</li>
<li>Check the voice on headphones and a phone speaker.</li>
</ol>
<h2>High-pass filtering</h2>
<p>A high-pass filter removes the lowest frequencies, which often carry rumble, handling noise and room boom. For most speech, a gentle high-pass filter in the lower range is a safe first step. Set it high enough to remove the rumble, but low enough that the warmth of the voice remains.</p>
<h2>Common mistakes</h2>
<ul>
<li>Boosting too many bands, which makes the sound artificial.</li>
<li>Using wide, strong boosts instead of small, narrow changes.</li>
<li>Cutting the high frequencies too far, which makes the voice dull.</li>
<li>Judging the EQ only on loud headphones, which can exaggerate the effect.</li>
<li>Trying to fix a recording problem that should be solved by distance or room.</li>
</ul>
<h2>Gentle is the rule</h2>
<p>A few decibels of change is often enough. If you need more, look for the cause of the problem first. A voice that is too thin may be recorded too far away. A voice that is harsh may be too close to a bright microphone. EQ can help, but it works best on a good recording.</p>
<h2>Using EQ on a phone recording</h2>
<p>A phone recording often needs less EQ than beginners expect, because the phone&rsquo;s own processing may already shape the sound. Start by listening to the raw file on headphones, and identify the one problem that bothers you most, such as rumble, boxiness or harshness. Fix that first, then listen again before adding anything else. Each extra change adds another layer that can make the voice sound unnatural.</p>
<p>If a phone recording is thin, the cause is usually distance or room. EQ can add some warmth, but it cannot replace a closer position. Record again closer if you can, and keep the EQ as a finishing touch.</p>
<p>Sweeping is the fastest way to find a problem band. Boost a narrow band by a few decibels, move it slowly across the range, and stop where the voice sounds most unpleasant. Then cut that band slightly, and check whether the voice regains its clarity. A narrow cut removes the problem with the least damage to the rest of the sound, which is why it usually beats a broad, gentle change. Write down the frequency you cut, so the same problem can be found quickly in the next recording.</p>
<h2>Limits</h2>
<p>The frequencies given here are approximate, and they vary between voices. The right EQ for one voice may be wrong for another. Use the ranges as starting points, and adjust by ear. Some problems, such as a noisy room, cannot be solved by EQ at all.</p>
<h2>Check every change by ear</h2>
<p>Listening decides EQ, not the curve on the screen. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the tone problems in voices, read the <a href="/tunedzy/blog/how-to-fix-a-tinny-voice-recording">tinny voice post</a> and the <a href="/tunedzy/blog/how-to-make-a-harsh-voice-recording-sound-warmer">harsh voice post</a> in this series.</p>
''',
    faq=[('What is the first EQ move for speech?', 'A gentle high-pass filter to remove rumble and handling noise.'),
         ('How much should I boost or cut?', 'A few decibels is usually enough. Make small changes and compare with the original.'),
         ('Can EQ fix a far-away voice?', 'Only partly. Distance changes the sound in ways EQ cannot fully restore.'),
         ('Should I EQ before or after cleaning?', 'Usually clean first, so the EQ shapes the clean signal rather than the noise.')])
