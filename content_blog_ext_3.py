"""Blog posts, batch 3 of 10: loudness and levels cluster. Merged into content_blog.py.
Each post answers one search first, then explains it in plain steps, admits its limits, and links to a tool or guide.
No invented statistics, reviews, prices or benchmarks."""

CLUSTERS = {
    'loudness': dict(tool='lufs-meter', label='Loudness and levels', tool_name='LUFS Meter'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='lufs-vs-rms-vs-peak-explained', cluster='loudness', kw='lufs vs rms vs peak',
    title='LUFS vs RMS vs Peak: What Each Meter Tells You',
    desc='LUFS, RMS and peak measure different things. What each one shows, why LUFS matches how loud speech sounds, and which to watch when you export.',
    h1='LUFS vs RMS vs Peak: What Each Meter Tells You',
    answer='Peak shows the highest single moment, RMS shows the average level over a short window, and LUFS gives a loudness figure that tracks how loud the audio sounds to people. For speech, use LUFS for the overall level and peak to check for clipping.',
    body='''
<p>Three numbers appear on almost every audio meter, and they are easy to mix up. Each one answers a different question. Knowing which question you are asking stops you chasing the wrong number, such as turning a voice up because the peak looks low when the loudness is already fine.</p>
<h2>Peak: the highest moment</h2>
<p>Peak meters show the highest single sample or moment in the file. They tell you how close you are to clipping, which is the point where the sound distorts. A peak that touches the top of the meter is a warning. Peak is useful for safety, but it does not tell you how loud the file sounds. A single loud consonant can set the peak while the rest of the voice is quiet.</p>
<h2>RMS: the average level</h2>
<p>RMS measures the average level over a short window, roughly the energy of the sound over time. It is closer to how loud a sound feels than peak is, but it does not account for how people hear different frequencies. Many older meters and some tools use RMS, which is why readings from different software can disagree.</p>
<h2>LUFS: loudness as people hear it</h2>
<p>LUFS, short for loudness units relative to full scale, is a measure based on how the ear responds to different frequencies. It gives a single figure for a whole file, called integrated loudness, and it can also show the loudness over short windows. Platforms and broadcasters use it to match the level of different programmes, which makes it the most useful number for speech and music.</p>
<h2>Which one to watch</h2>
<ul>
<li><strong>For the level of a finished file,</strong> check LUFS against your target.</li>
<li><strong>For clipping,</strong> check the true peak, which is covered in its own post.</li>
<li><strong>For a quick check while recording,</strong> watch the peaks, so the voice never reaches the top.</li>
</ul>
<h2>Use the right meter for the job</h2>
<p>The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the loudness of a file in the units most platforms use. Use it at the end of a project, after cleaning and levelling, rather than at the start. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains which target suits which platform.</p>
<h2>Limits</h2>
<p>No single number describes everything. Two files with the same LUFS can sound different if one is very dynamic and the other is squeezed. Listen as well as look. The meter tells you the level; your ears tell you whether the balance is right.</p>
''',
    faq=[('Which meter should I trust most?', 'For the overall level of a finished file, LUFS. For clipping, the true peak. For a quick check while recording, the peak.'),
         ('Why do two meters show different numbers?', 'They measure different things, or use different windows and weighting. Check which measure each one uses.'),
         ('Is RMS out of date?', 'No. It is still useful as a simple average, but LUFS is the better guide to how loud speech sounds.'),
         ('Should I aim for a specific peak level?', 'Keep the peaks below full scale with some room to spare, and use LUFS for the target loudness.')])

add(slug='what-is-true-peak-in-audio-and-why-it-matters', cluster='loudness', kw='what is true peak in audio',
    title='What Is True Peak in Audio and Why It Matters',
    desc='True peak shows the level between samples, where clipping can hide. What true peak means, why a sample peak can look safe when it is not, and how to check it.',
    h1='What Is True Peak in Audio and Why It Matters',
    answer='True peak is the highest level the audio reaches when it is turned back into a smooth wave, including the moments between the stored samples. A file can look safe on a sample peak meter and still clip after conversion, so check the true peak of the exported file.',
    body='''
<p>Digital audio stores a series of samples, which are measurements taken at regular points in time. A simple peak meter reads those samples. But the sound that comes out of a speaker is a smooth wave, and that wave can rise higher between the samples. When it does, the output can clip even though the meter never reached the top.</p>
<h2>Why sample peaks can mislead</h2>
<p>Imagine two samples that are both just below full scale. The wave between them can rise above full scale, and a converter or a lossy encoder can overshoot. The result is a distorted sound that the sample meter did not show. This happens most with loud, dense mixes, and it can also happen after conversion to MP3 or AAC.</p>
<h2>What true peak measures</h2>
<p>True peak estimates the highest level of the reconstructed wave, including the moments between samples. It is measured in dBTP, which is a dB figure relative to full scale. A true peak below zero means the file should not clip in normal playback, though the exact margin you want depends on the format and the platform.</p>
<h2>How to check it</h2>
<ol>
<li>Export the file in the format you will publish.</li>
<li>Open the exported file in a meter that shows true peak.</li>
<li>Check the highest true peak across the whole file, not only the section you were working on.</li>
<li>If it is over your limit, lower the level or limit the peaks, then export again.</li>
</ol>
<h2>Leave headroom</h2>
<p>Headroom is the gap between the loudest moment and full scale. A small margin, such as a few decibels for speech, protects the sound when it is converted or played on a device that adds its own processing. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can show the true peak of a finished file alongside its loudness.</p>
<h2>Limits</h2>
<p>True peak is an estimate. Different tools calculate it in slightly different ways, and some platforms apply their own processing on playback. Use it as a safety check, and listen to the final file on a phone and on headphones before you publish.</p>
''',
    faq=[('Why does my file clip after export when the meter looked fine?', 'The sample meter misses the peaks between samples. Check the true peak of the exported file.'),
         ('What does dBTP mean?', 'It is the true peak level in decibels relative to full scale. A value below zero means no peak reaches full scale.'),
         ('Do I need to check true peak for speech?', 'Yes, if the voice is loud or heavily processed. It is a quick check that prevents distortion.'),
         ('Can a limiter fix true peak?', 'A limiter can reduce peaks, but use it lightly, or the speech will sound squashed.')])

add(slug='why-is-my-video-quieter-on-youtube', cluster='loudness', kw='why is my video quieter on youtube',
    title='Why Is My Video Quieter on YouTube Than Other Videos?',
    desc='Why a video sounds quieter than others on YouTube: how platforms adjust playback loudness, what level your upload should be, and how to check it before you publish.',
    h1='Why Is My Video Quieter on YouTube Than Other Videos?',
    answer='Platforms adjust playback loudness, and many turn down very loud files without turning up quiet ones. If your video sounds quieter than others, the audio was probably mixed low or with a low peak level. Check the loudness of your export and raise it to a sensible target.',
    body='''
<p>Viewers often notice that one video sounds much quieter than the next, even at the same volume setting. The cause is usually the audio itself. Playback systems adjust levels, but they do not perform miracles. A quiet mix stays quiet unless the level was set well in the first place.</p>
<h2>What platforms do to your audio</h2>
<p>Streaming and video platforms often adjust the level of playback so that loud and quiet files sound more alike. In general, very loud files are turned down. Whether quiet files are turned up depends on the platform and its settings, so you should not rely on the platform to fix a low mix. Check the current guidance from the platform you publish to, because the rules can change.</p>
<h2>Check your export, not your project</h2>
<p>A project can sound fine on your studio speakers and still export low. Export the file, then measure its loudness and peaks. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> gives the loudness of the exported file, which is the number that matters for the viewer.</p>
<h2>Raise the level to a sensible target</h2>
<p>If the exported file is much quieter than your target, raise the level, then check the peaks again. Raising the level too far makes the peaks clip, so use a limiter gently if you need extra level. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the common targets for online video.</p>
<h2>Compare with a reference</h2>
<p>Choose a video in a similar genre that you think sounds right, and compare it with yours on the same device. Match the overall level, not the exact number, because different genres and mixes call for different levels. Listen at the same volume setting, and switch between the two quickly.</p>
<h2>Check the sound on a phone</h2>
<p>Many viewers watch on a phone, where the speaker is small and the level is set differently. Play the final video on your phone before you publish. If it is hard to hear the speech over background sound, the mix needs a clearer voice, not only more level.</p>
<h2>Limits</h2>
<p>Platforms change their processing, and some devices add their own. A video that sounds right on your computer may still sound different on a television or a speaker. Aim for a clear, steady mix, and do not chase one exact number. The viewer&rsquo;s volume knob will do the rest.</p>
''',
    faq=[('Will YouTube make my video louder?', 'Not reliably. Do not depend on playback processing. Set a sensible level before you upload.'),
         ('What level should my video be?', 'Use a loudness target suited to your content, and check the guidance from the platform you publish to.'),
         ('Why does my video sound quiet on my phone only?', 'Phone speakers are small and their levels differ. Check the video on a phone before you publish.'),
         ('Is it safe to just turn up the volume in editing?', 'Only if the peaks stay below full scale. Check the true peak after you raise the level.')])

add(slug='how-to-read-a-lufs-meter', cluster='loudness', kw='how to read a LUFS meter',
    title='How to Read a LUFS Meter for Speech and Music',
    desc='How to read a LUFS meter: integrated, short-term and momentary readings, what each one means for speech, and how to use them to set a steady level.',
    h1='How to Read a LUFS Meter for Speech and Music',
    answer='Read the integrated LUFS for the overall level of a whole file, the short-term reading for how loud a passage feels, and the momentary reading for quick changes. For speech, aim the integrated figure at your target and keep the short-term reading steady.',
    body='''
<p>A LUFS meter can look intimidating, with several numbers moving at once. Most of them answer one question each. Once you know which reading to use for which job, the meter becomes a simple guide to level, and you stop guessing from the waveform.</p>
<h2>Integrated loudness: the whole file</h2>
<p>The integrated reading is the loudness of the whole file, averaged over its length. It is the number you match to your target, and it is the one most platforms use. Read it at the end of the project, after editing, because it changes whenever you add or remove material.</p>
<h2>Short-term loudness: a passage</h2>
<p>The short-term reading averages over a few seconds. It tells you how loud a passage feels, which is useful for checking that a section of speech sits at the same level as the one before. If the short-term reading jumps between sections, the balance needs work, even when the integrated figure looks right.</p>
<h2>Momentary loudness: quick changes</h2>
<p>The momentary reading averages over a fraction of a second. It moves quickly, so it is useful for spotting a loud word or a sudden noise, but it is too jumpy to set a level by. Watch it while you play, and ignore it when you make the final decision.</p>
<h2>Loudness range: how much it varies</h2>
<p>Some meters also show loudness range, which measures how much the level varies across the file. A speech file with a wide range can have quiet passages that are hard to hear on a phone. A narrow range can sound squashed. The right range depends on the content, so use it as a guide rather than a rule.</p>
<h2>A practical routine</h2>
<ol>
<li>Play the finished file from start to end, and watch the short-term reading.</li>
<li>Check that the integrated figure is at your target.</li>
<li>Check the true peak of the export, as covered in the true peak post.</li>
<li>Listen on headphones and a phone speaker, and adjust only if the sound needs it.</li>
</ol>
<h2>Limits</h2>
<p>A meter cannot judge quality. A file can hit the right number and still have a muddy mix or a harsh voice. Use the meter to set the level, and your ears to judge the balance. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> is a good place to practise reading the numbers on your own files.</p>
''',
    faq=[('Which reading should I use to set the level?', 'The integrated loudness of the whole finished file, checked against your target.'),
         ('Why does the momentary reading keep moving?', 'It averages over a fraction of a second, so it reacts to every word. That is normal.'),
         ('What is loudness range?', 'It shows how much the level varies over the file. A very narrow range can sound squashed.'),
         ('Should I trust the meter over my ears?', 'Use the meter to set the level, and your ears to judge the balance and quality.')])

add(slug='how-much-headroom-to-leave-in-audio', cluster='loudness', kw='how much headroom to leave in audio',
    title='How Much Headroom to Leave in Audio and Why',
    desc='How much headroom to leave in audio: what headroom means, the margin speech and music need, and the mistakes that eat it up before export.',
    h1='How Much Headroom to Leave in Audio and Why',
    answer='Leave a few decibels of headroom below full scale for speech, more if the mix is loud or heavily processed. Headroom protects the sound during conversion and playback, so keep the peaks below full scale and check the true peak of the exported file.',
    body='''
<p>Headroom is the space between the loudest moment of a recording and the point where digital audio clips. A mix with plenty of headroom can be converted, processed and played back without distortion. A mix with none sounds harsh the moment anything adds gain, which happens often.</p>
<h2>What headroom protects against</h2>
<p>Headroom gives room for the things that happen after you finish mixing. Encoding to MP3 or AAC can add small overshoots. Playback devices and streaming services may adjust the level. A listener may turn the volume up. Each of these can push a loud peak over full scale, and headroom absorbs that.</p>
<h2>How much to leave</h2>
<p>For speech, a few decibels of headroom below full scale is a common and sensible choice. Music that is heavily compressed or limited may need more, or the margin disappears on export. There is no single correct number, because it depends on the content and the format. Choose a margin you can explain, then check it on the exported file.</p>
<h2>Where headroom disappears</h2>
<ul>
<li><strong>Stacked gain</strong> from many effects, each adding a little level.</li>
<li><strong>Heavy limiting</strong> pushed to make the file louder, which removes the margin.</li>
<li><strong>Boosting after processing</strong> to match a target, without rechecking the peaks.</li>
<li><strong>Normalising to the peak,</strong> which sets the loudest sample to full scale and leaves nothing spare.</li>
</ul>
<h2>Check headroom on the export</h2>
<p>Check the true peak of the final file, not only the project. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> shows the peak alongside the loudness, so you can see both at once. If the peak is too close to full scale, lower the level before export, rather than fixing it later.</p>
<h2>Limits</h2>
<p>Headroom is a safety margin, not a sound. A file with a generous margin can still sound quiet or thin, so aim for the right balance between level and headroom. The goal is a clean, steady sound with no clipping, not the lowest possible peak.</p>
''',
    faq=[('Is zero headroom ever acceptable?', 'It is risky. A file at full scale can clip after conversion or playback adjustment.'),
         ('Does headroom make audio quieter?', 'It leaves a margin below full scale. Your loudness target still sets the overall level.'),
         ('How do I check headroom after export?', 'Measure the true peak of the exported file, not the project, and compare it with your margin.'),
         ('Is headroom the same as dynamic range?', 'No. Headroom is the space to full scale. Dynamic range is the difference between the loud and quiet parts.')])

add(slug='what-is-dynamic-range-in-speech-audio', cluster='loudness', kw='what is dynamic range in audio',
    title='What Is Dynamic Range in Speech Audio?',
    desc='Dynamic range in speech audio: the difference between the loud and quiet parts of a recording, why it matters for listeners and how to keep it natural.',
    h1='What Is Dynamic Range in Speech Audio?',
    answer='Dynamic range is the difference between the loudest and quietest parts of a recording. Speech with a wide range can feel natural but hard to hear on a phone, and speech with a narrow range is easier to follow but can sound flat. Aim for a range that suits the listening place.',
    body='''
<p>Dynamic range describes how much the level changes across a recording. Live speech has a natural dynamic range, from soft words to strong emphasis. Editing and processing change it, and every step can make the sound more even, or less natural. Understanding it helps you decide how much processing a voice needs.</p>
<h2>A wide range sounds natural</h2>
<p>A wide range keeps the expression in a voice. Soft words, emphasis and pauses all stay in place. For a relaxed listening environment, such as headphones at home, a wide range can sound very natural. The risk is that the quiet parts become hard to hear in a noisy place like a car or a train.</p>
<h2>A narrow range is easier to follow</h2>
<p>A narrow range keeps the level steady, so listeners do not need to adjust the volume. This suits podcasts, voice-overs played in noisy places and content that people listen to while doing something else. Too narrow, and the voice sounds squashed, with no life.</p>
<h2>Where the range comes from</h2>
<p>The range comes from the performance, the microphone distance, the room and the processing. Stepping back from the microphone, or speaking softly, widens the range. A close microphone and a steady voice narrow it. Compression and limiting narrow it further, which is why heavy processing can flatten a voice.</p>
<h2>How to choose the right range</h2>
<ol>
<li>Decide where most people will listen: headphones, a car, a phone speaker.</li>
<li>Keep enough range that the expression survives in that place.</li>
<li>Use gentle levelling to smooth the largest jumps, rather than squashing everything.</li>
<li>Listen to the final file on the device your audience will use.</li>
</ol>
<h2>Limits</h2>
<p>There is no ideal range for every voice. A dramatic narration needs more range than a news summary. Use the content and the listening place to decide, and listen before you commit. The <a href="/tunedzy/how-to-level-voices-between-speakers">levelling guide</a> shows how to smooth a conversation without losing its natural feel.</p>
''',
    faq=[('Is a wide dynamic range better?', 'Not always. It depends on where the audience listens. Wide range suits headphones, narrow range suits noisy places.'),
         ('Does compression reduce dynamic range?', 'Yes. That is its job, so use it lightly on speech if you want the voice to stay natural.'),
         ('How do I know if my voice is too squashed?', 'If the voice sounds flat, tiring or lifeless on headphones, reduce the processing and compare.'),
         ('Can a phone speaker hear dynamic range?', 'Not well. A small speaker struggles with quiet passages, so the mix needs more even levels for phones.')])

add(slug='what-is-loudness-normalization-explained', cluster='loudness', kw='what is loudness normalization',
    title='What Is Loudness Normalization and How It Works',
    desc='Loudness normalization explained: how platforms and players adjust the level of each file, why it changes how your audio sounds, and what to do about it.',
    h1='What Is Loudness Normalization and How It Works',
    answer='Loudness normalization adjusts the playback level of each file so that different files sound at a similar loudness. Players and platforms measure each file, then turn it up or down. You can prepare for it by setting your file to a sensible target, and by leaving headroom for the adjustment.',
    body='''
<p>When you play a playlist and the songs sound roughly the same level, you are hearing loudness normalization at work. A player or a platform measures each file, then adjusts the playback level so it lands near a common target. The idea is simple, but it changes how your audio sounds, and it rewards a well-prepared mix.</p>
<h2>How it works in practice</h2>
<p>The player measures the loudness of each file, usually in LUFS. It compares that figure with its target, then applies a gain change during playback. A file that is much louder than the target is turned down. Whether a quiet file is turned up depends on the player and its settings. The original file is not changed.</p>
<h2>Why it matters for your audio</h2>
<p>Normalization means that a very loud, heavily compressed file may not sound louder than a quieter, more dynamic one. The loud file is turned down, and its extra level is removed. A file that is quiet and dynamic may sound natural after normalization. Mixing for the loudest possible level no longer makes the file sound louder to listeners.</p>
<h2>Prepare your file for it</h2>
<ul>
<li>Set the file to a sensible loudness target, rather than as loud as possible.</li>
<li>Keep the true peak below full scale, so the adjustment does not add distortion.</li>
<li>Check the result on a streaming app or a player you know, if you can.</li>
</ul>
<h2>Which platform does what</h2>
<p>Platforms differ in their targets and their settings, and they change over time. Check the current guidance from each platform before you publish. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the common approach for online video and audio.</p>
<h2>Limits</h2>
<p>Normalization is not a substitute for a good mix. It can reduce loudness, but it cannot fix a muddy voice or a noisy recording. Use it as a guide to what listeners will hear, and check your work on the devices they use.</p>
''',
    faq=[('Does normalization change my file?', 'Not usually. The player adjusts the playback level, and the original file stays the same.'),
         ('Should I make my file as loud as possible?', 'No. A file mixed for maximum loudness can sound worse after normalization.'),
         ('Do all platforms normalize the same way?', 'No. Targets and settings differ and change over time, so check each platform.'),
         ('Does normalization affect podcasts?', 'It can. Platforms may adjust the level of each episode, so set a steady target before you publish.')])

add(slug='limiter-settings-for-voice-explained', cluster='loudness', kw='limiter settings for voice',
    title='Limiter Settings for Voice: A Gentle Starting Point',
    desc='Limiter settings for voice: what a limiter does, a gentle starting point for speech, the controls to adjust and how to tell when you have gone too far.',
    h1='Limiter Settings for Voice: A Gentle Starting Point',
    answer='For speech, start with a ceiling a few decibels below full scale, a release that lets the voice breathe, and only enough gain reduction to catch the loudest peaks. If the voice sounds squashed or pumps, you have done too much.',
    body='''
<p>A limiter stops the loudest peaks from going over a set ceiling. Used lightly, it protects the sound and keeps the level steady. Used heavily, it squashes the voice and removes the life from it. The skill is in using only enough to do the job, and speech needs a gentler touch than many music presets suggest.</p>
<h2>What a limiter actually does</h2>
<p>A limiter reduces the gain when the signal would exceed its ceiling. The amount of reduction shows on the meter. A small amount, a few decibels on the loudest words, is normal. Large, constant reduction means the input is too loud for the setting, or the mix needs more gentle levelling first.</p>
<h2>A starting point for speech</h2>
<ol>
<li><strong>Ceiling:</strong> set it a few decibels below full scale, leaving headroom for the export.</li>
<li><strong>Release:</strong> choose a moderate release that lets the voice recover between words, not one so fast it distorts.</li>
<li><strong>Gain:</strong> raise the input only until the loudest peaks touch the limiter, not beyond.</li>
<li><strong>Lookahead:</strong> use a short lookahead if the tool offers it, so the peaks are caught cleanly.</li>
</ol>
<h2>Signs you have gone too far</h2>
<p>The voice sounds squashed or small, the breaths get louder, or the background noise rises between words. Pumping, where the level moves audibly with each word, is another sign. Reduce the gain reduction, then listen again. If the mix needs that much limiting, fix the levels earlier in the chain.</p>
<h2>Check the export</h2>
<p>After limiting, check the true peak and the loudness of the exported file, not only the project. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> is useful for confirming the final level, and listening on a phone will tell you whether the voice still sounds natural.</p>
<h2>Limits</h2>
<p>Limiter presets are starting points, not answers. Every voice and recording is different. Use the settings as a place to begin, and adjust by ear until the voice sounds clear and natural, with only the peaks caught.</p>
''',
    faq=[('Should I use a limiter on speech at all?', 'A light limiter can help, especially for protecting against peaks. Use it gently.'),
         ('What does pumping mean?', 'The level moves audibly with each word because the limiter reacts too strongly. Use a slower release or less gain.'),
         ('How much gain reduction is too much?', 'If the voice sounds flat or the breaths get loud, you are using too much. A few decibels on the peaks is typical.'),
         ('Can a limiter make my voice louder?', 'It can raise the average level, but it does so by reducing the peaks. It cannot add clarity.')])

add(slug='why-does-my-podcast-sound-quieter-than-other-shows', cluster='loudness', kw='why does my podcast sound quieter than others',
    title='Why Does My Podcast Sound Quieter Than Other Shows?',
    desc='Why a podcast sounds quieter than other shows: the mix level, platform playback, phone speakers and the processing choices that make a show feel loud.',
    h1='Why Does My Podcast Sound Quieter Than Other Shows?',
    answer='Your podcast probably sounds quieter because its average loudness is lower, its voice is less clear, or the intro and music are mixed differently. Check the loudness of your export against a target, make the voice clearer, and listen against other shows on the same device.',
    body='''
<p>Listeners often describe a podcast as quiet when they mean that they struggle to hear it. Real loudness matters, but clarity matters just as much. A show can have the right number on a meter and still feel quiet if the speech is thin, buried under music or hard to hear on a phone.</p>
<h2>Check the loudness of the export</h2>
<p>Measure your exported episode, not the project, and compare its loudness with your target. If it is well below the target, the mix is low. Raise it, then check the peaks so the voice does not clip. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the common targets for online audio.</p>
<h2>Make the voice clearer</h2>
<p>A voice that is quiet to the ear may be missing presence in the mid frequencies, or it may be masked by noise. Gentle cleanup, a clear microphone position and careful levelling make the voice easier to hear without raising the whole file. Clarity often does more than a higher level.</p>
<h2>Listen on a phone</h2>
<p>Many listeners use phone speakers or earbuds, which reproduce the speech range differently from studio monitors. Play the episode on a phone, then compare it with a show you think sounds loud and clear. Match the feeling, not the exact number.</p>
<h2>Check the intro and the music</h2>
<p>If the intro is loud and then the speech is quiet, listeners turn the volume down after the intro and the voice feels weak. Balance the music under the voice, and keep the intro at a level close to the speech.</p>
<h2>Compare with a reference show</h2>
<p>Pick one or two shows in your genre that sound right to you. Play them and your episode at the same device volume, and switch between them. Adjust your level and clarity until the comparison feels fair. Do not chase a louder sound than the reference, because a loud, squashed show is tiring.</p>
<h2>Limits</h2>
<p>A quiet podcast can be a deliberate choice, especially for calm, intimate shows. The problem is when listeners cannot hear the words comfortably. Aim for speech that is clear and steady, not simply loud.</p>
''',
    faq=[('Should I make my podcast as loud as other shows?', 'Aim for a steady, comfortable level and clear speech. Matching a very loud show can make yours tiring.'),
         ('Will a louder mix fix a quiet podcast?', 'Not on its own. A louder mix with thin speech still sounds weak. Improve clarity too.'),
         ('Why does my show sound quiet on a phone?', 'Phone speakers reproduce speech differently. Test your episode on a phone before you publish.'),
         ('Is it the platform?', 'Partly. Platforms may adjust playback levels, so set your export to a sensible target.')])

add(slug='loudness-war-and-why-modern-music-is-compressed', cluster='loudness', kw='what is the loudness war',
    title='What Is the Loudness War and Why Modern Music Sounds Squashed',
    desc='The loudness war explained: why music was made louder for decades, how streaming changed the race, and what it means for mixes you make yourself.',
    h1='What Is the Loudness War and Why Modern Music Sounds Squashed',
    answer='The loudness war was a long trend of mastering music louder, using heavy compression and limiting to stand out on the radio and on CDs. Streaming normalization has reduced the reward for being loudest, but the habit of squashed masters remains, so choose your loudness on purpose.',
    body='''
<p>Many people who listen to older recordings notice that they sound more open and dynamic than some newer ones. That difference has a name. The loudness war describes a long period in which mastering engineers pushed records louder and louder, often by squeezing out the quiet parts to lift the average level.</p>
<h2>Why it started</h2>
<p>When listeners compared songs one after another on the radio or on a CD player, the louder one often seemed better. Louder songs jumped out, and labels and broadcasters rewarded them. Heavy compression and limiting were the easiest way to raise the average level, so the trend spread across genres.</p>
<h2>What it cost</h2>
<p>Squashed masters lose dynamic range, so the drums hit less, the vocals feel less alive and the listener gets tired. Clipping and distortion became common, because the loudest peaks were pushed past what the format could handle cleanly. Many people still describe the result as fatiguing.</p>
<h2>What streaming changed</h2>
<p>Streaming platforms adjust playback loudness, which removes much of the reward for being the loudest. A very loud master can be turned down, so its extra level no longer makes it sound better. This has encouraged mixes with more dynamic range, though the habit of heavy limiting has not disappeared.</p>
<h2>What it means for your own mixes</h2>
<p>Choose your loudness on purpose, rather than pushing for the highest number. A target that suits your content, with peaks kept below full scale, gives a clean result that survives playback adjustment. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains how to pick a target for each platform.</p>
<h2>Limits</h2>
<p>Loud, dense music is a valid style, and some genres are meant to be heavily compressed. The point is not that loud is bad, but that loudness should be a choice you can justify, rather than a race you lose by default.</p>
''',
    faq=[('Is the loudness war over?', 'Not entirely. Streaming has reduced its reward, but heavy limiting is still common in some genres.'),
         ('Does streaming make loud masters quieter?', 'In playback, very loud masters are often turned down by normalization.'),
         ('Should I make my mix as loud as possible?', 'No. A clean mix at a sensible target usually sounds better after playback adjustment.'),
         ('What is the opposite of a squashed master?', 'A master with more dynamic range, where the quiet and loud parts keep their contrast.')])
