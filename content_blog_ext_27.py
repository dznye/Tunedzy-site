"""Blog posts, batch 27: using the free Tunedzy tools and the phone app (how-to). Merged into content_blog.py.
Each post describes only what the tool's own listing says it does. Tools run in the browser and the site describes them
as private; the posts repeat that only where the listing says so. No invented statistics or features.
Funnel: each post ends with a link to the matching free tool and to Tunedzy Go."""

CLUSTERS = {
    'app-how-to': dict(tool='vocal-checker', label='Using the free tools', tool_name='Vocal Checker'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='how-to-check-a-vocal-recording-online', cluster='app-how-to', kw='check vocal recording online',
    title='How to Check a Vocal Recording Online: A Step-by-Step Guide',
    desc='How to check a vocal recording online: what the Vocal Checker looks for, how to read its results and how to act on clipping, noise, rumble and level problems.',
    h1='How to Check a Vocal Recording Online: A Step-by-Step Guide',
    answer='The Vocal Checker lets you drop in a recording and see clipping, noise, rumble and level problems, with plain-English fixes. Use it on a finished take before publishing, read each result, fix the most important problem first and check again. It runs in your browser and the tool describes itself as private.',
    body='''
<p>Before a vocal recording goes public, it is worth checking the basics that listeners notice most: whether the peaks are clipping, whether there is noise or rumble in the quiet parts, and whether the level is steady. Those problems are easy to miss after many hours of listening, and a fresh check can catch them quickly. The Vocal Checker is designed for this job. You drop in a recording, and it reports the problems it finds with plain-English fixes.</p>
<p>This guide walks through a check from start to finish: what to prepare, how to run the check, how to read the results and how to act on them. It is written for podcasters, singers and voice-over artists who want a quick, honest review before publishing.</p>
<h2>What the tool checks</h2>
<p>The Vocal Checker looks for four kinds of problem: clipping, where the loudest sounds are cut off; noise, where a steady background sits under the voice; rumble, where low-frequency sound builds up; and level, where the voice is too quiet or too loud overall. Each one affects how the recording sounds, and each has a different fix. A recording can have one, several or none of them.</p>
<p>The tool does not judge the performance. A recording can be technically clean and still need a better take. Use the check for the technical side, and your ears for the rest.</p>
<h2>Prepare the file</h2>
<p>Export the recording in the form you plan to publish, or as close to it as possible. Check the file plays from start to end in a media player, so you know it is complete. If the recording has several sections, you can check the whole file, or check the sections that worry you most. A finished file gives the most useful results, since an early rough edit may show problems you will fix anyway.</p>
<h2>Run the check</h2>
<p>Drop the file into the Vocal Checker in your browser. The tool analyses the recording and reports its findings. Take a moment to read each result before changing anything, since one problem can cause another in the report. Note the results you want to act on, and the order in which you will fix them.</p>
<h2>Read the results</h2>
<p>Start with clipping, because it cannot be fully repaired and it affects everything else. If the recording clips, re-record or re-export with lower levels before dealing with other problems. Next, look at noise and rumble, which are easier to reduce but can be damaged by heavy processing. Finally, check the level, since changing it can bring noise up or push peaks into clipping.</p>
<h2>Act on the results in order</h2>
<ol>
<li>Fix or accept clipping first, since it is the hardest to repair.</li>
<li>Reduce rumble with a gentle high-pass filter, keeping the warmth of the voice.</li>
<li>Reduce steady noise lightly, listening for any watery change in the speech.</li>
<li>Adjust the level last, with a small gain change, and check the peaks again.</li>
<li>Run the check a second time on the revised file, to confirm the fixes.</li>
</ol>
<h2>Check the result by ear</h2>
<p>After each fix, listen to the recording on headphones and on a phone speaker. A correction that reduces a problem on the report but makes the voice sound thin or distant is not an improvement. Compare the revised version with the original at the same level, and keep the one that sounds better to a listener.</p>
<h2>Common mistakes</h2>
<ul>
<li>Fixing the noise before the clipping, which leaves the damage in place.</li>
<li>Applying heavy noise reduction to remove every trace of background.</li>
<li>Raising the level to clear a warning, which brings the noise up with it.</li>
<li>Checking an early rough edit and publishing a different version.</li>
<li>Treating the report as a score rather than a set of things to listen for.</li>
</ul>
<h2>Using the results to plan the next recording</h2>
<p>A check on one file can reveal a pattern across several files, such as clipping at the start of each take, or a noise floor that rises late in a session. Use those patterns to change the setup for the next recording, rather than fixing the same problem at the editing stage every time.</p>
<h2>Checking a take against the project</h2>
<p>Compare the level and the noise of the file with the others in the same project. A take that sits clearly louder or quieter than the rest will stand out in the final mix, even when it passes the basic checks. Use the same clip length and position in the check, so the comparison is fair.</p>
<h2>Limits</h2>
<p>A check is only as good as the file it reads, and the tool cannot judge taste, timing or performance. Results describe what is measurable, and your ears decide what matters. If a recording has serious problems, the best fix is usually a new take, placed closer to the microphone in a quieter room.</p>
<h2>Try the Vocal Checker</h2>
<p>Run a check on your next finished vocal before you publish. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> is free and runs in your browser. If you record on a phone, the <a href="/tunedzy/go/">Tunedzy Go</a> page explains how to clean a phone recording in your phone’s browser, and the guide to <a href="/tunedzy/blog/what-is-true-peak-in-audio-and-why-it-matters">true peak</a> explains the clipping check in more depth.</p>
''',
    faq=[('What does the Vocal Checker look for?', 'Clipping, noise, rumble and level problems, with plain-English fixes for each.'),
         ('Should I check a rough edit?', 'Better to check the finished file you plan to publish, since a rough edit may show problems you will fix anyway.'),
         ('Which problem should I fix first?', 'Clipping, because it cannot be fully repaired and it affects the other fixes.'),
         ('Is my file private?', 'The tool describes itself as private and running in your browser. Check its page for the current details.')])

add(slug='how-to-check-song-loudness-online', cluster='app-how-to', kw='check song loudness online',
    title='How to Check Song Loudness Online With the LUFS Meter',
    desc='How to check song loudness online with the LUFS Meter: what it reports, how to read integrated loudness and true peak, and what platforms do.',
    h1='How to Check Song Loudness Online With the LUFS Meter',
    answer='The LUFS Meter lets you drop in a mix or master and see its integrated loudness, true peak and loudness range, and what Spotify, YouTube and Apple Music would do to it. Check the integrated figure against your target, the true peak for clipping, and the range for how much the dynamics vary. Use the result to adjust the master before release.',
    body='''
<p>Loudness is one of the most important and least understood parts of finishing a song. A master that is too quiet sounds weak next to other tracks, and one that is too loud can be squashed and tiring. Streaming services also adjust the playback level, so the number you aim for in the studio is not always the number a listener hears. A quick, reliable check helps you see where your mix sits before you release it.</p>
<p>The LUFS Meter is a free online tool for this job. This guide explains what it reports, how to read the figures and how to use them to make decisions about your master.</p>
<h2>What the meter reports</h2>
<p>The LUFS Meter shows three main figures. Integrated loudness is the average loudness of the whole song, measured on a scale that reflects how the ear hears. True peak shows the highest level the signal reaches between samples, which is where clipping can hide. Loudness range shows how much the loudness varies across the track. The tool also shows what streaming services would do to the file, which helps you judge how the master will sound after playback adjustment.</p>
<h2>Prepare the file</h2>
<p>Export the master as you would release it, at the sample rate and format you plan to deliver. Check that it plays from start to end, with no unexpected silence or clicks. Measuring the file you intend to release is more useful than measuring the project, because the export can change the level and the peaks.</p>
<h2>Read the integrated loudness</h2>
<p>The integrated figure is the one most people compare with a target. Check it against your release plan or the guidance from the platform you are delivering to. A lower figure is not automatically a fault: a quiet, dynamic track may suit a particular style. Use the number to decide whether the master is in the right range, and let your ears decide the balance.</p>
<h2>Read the true peak</h2>
<p>True peak tells you whether the file is likely to clip on playback, even if the sample meter in your studio looked safe. A true peak above zero is a clear sign that the signal exceeds full scale somewhere between samples. Reduce the level or the limiting until the true peak is comfortably below zero, leaving headroom for playback and conversion.</p>
<h2>Read the loudness range</h2>
<p>Loudness range describes how much the loudness changes across the song. A very narrow range can mean the track is squashed, with little contrast between loud and quiet. A very wide range can mean quiet passages that are hard to hear in noisy places. Compare the range with other tracks in your genre, and choose the balance that suits the song.</p>
<h2>See what the platforms would do</h2>
<p>The meter shows what Spotify, YouTube and Apple Music would do to the file. Platforms may turn louder files down and sometimes turn quieter files up, depending on their settings. A master that is very loud will be reduced on playback, so pushing the level for its own sake gains little. Check the platform view to see whether your master will sit well after adjustment.</p>
<h2>Make decisions from the numbers</h2>
<ol>
<li>Check the integrated loudness against your target.</li>
<li>Check the true peak, and reduce the level if it is too close to zero.</li>
<li>Check the loudness range, and compare it with similar tracks.</li>
<li>Review the platform view, and decide whether the balance suits the release.</li>
<li>Re-export, re-measure and listen before releasing.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Chasing a louder number, and squashing the master to reach it.</li>
<li>Measuring the project rather than the export.</li>
<li>Ignoring the true peak, and publishing a file that clips on playback.</li>
<li>Comparing your number with a track from a different genre.</li>
<li>Judging the master by the meter alone, without listening.</li>
</ul>
<h2>Compare with a reference track</h2>
<p>Measure a commercial track you know well, in the same style, and compare its loudness and peak with your mix. The numbers will not decide the balance for you, but the comparison shows whether your mix sits in a similar range. Play both tracks at the same level in your monitoring, and listen for differences in the vocal and the low end.</p>
<h2>Check a rough mix as well as the final</h2>
<p>Measuring a rough mix early shows whether the balance is heading in a sensible direction. A rough mix with very high loudness and clipping peaks often needs gain staging before the mastering stage, and that is far easier to correct at the start than at the end.</p>
<h2>Limits</h2>
<p>The meter measures what can be measured, and it cannot judge the arrangement, the performance or the feel of the track. Platform behaviour can change, so check the current guidance before a release. Use the figures as a guide, and trust the listening test on several devices.</p>
<h2>Try the LUFS Meter</h2>
<p>Measure your next master before release. The <a href="/tunedzy/tools/lufs-meter">LUFS Meter</a> is free and shows the figures described above. For a speech episode, the guide to <a href="/tunedzy/blog/how-to-check-a-vocal-recording-online">checking a vocal recording</a> covers the Vocal Checker, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers phone recordings.</p>
''',
    faq=[('What is integrated loudness?', 'The average loudness of the whole track, measured on a scale that reflects how the ear hears.'),
         ('Why is true peak important?', 'It shows where clipping can occur on playback, between the stored samples.'),
         ('Does a louder master always win?', 'Not necessarily. Platforms may turn louder files down, and squashing can cost quality.'),
         ('Should I measure the project or the export?', 'The export, since it is the file you will release.')])

add(slug='how-to-find-a-songs-key-in-your-browser', cluster='app-how-to', kw='song key finder online',
    title='How to Find a Song’s Key in Your Browser, Step by Step',
    desc='How to find a song’s key in your browser: what the Song Key Finder reports, how to read the key and Camelot code, and how to use them.',
    h1='How to Find a Song’s Key in Your Browser, Step by Step',
    answer='The Song Key Finder lets you drop in a song or beat and see its key, the Camelot code and the relative key. It runs in your browser and the tool describes itself as nothing uploaded. Use the key to choose a suitable vocal range, match a beat, or plan a transpose, and check the result by ear.',
    body='''
<p>Knowing the key of a song is one of the most useful pieces of information a musician can have. It helps a singer find a comfortable range, helps a producer match a sample or a vocal to a beat, and helps a songwriter plan a change of key. Working out the key by ear takes practice, and a quick, reliable check saves time. The Song Key Finder is a free tool that reports the key of a track in a few steps.</p>
<p>This guide explains what the tool reports, how to read its results and how to use the key in practice.</p>
<h2>What the tool reports</h2>
<p>The Song Key Finder reports the key of a song or beat, the Camelot code and the relative key. The key is the home note and the scale the music is built around. The Camelot code is a notation used by DJs and producers to find keys that mix well together. The relative key is the related major or minor key that shares the same notes, which is useful when you move between the two.</p>
<h2>Prepare the file</h2>
<p>Use the cleanest version of the track you have. A full, undistorted mix gives the best reading, while a heavily compressed or noisy file can make the key harder to find. If a song has a long intro without melody, it may help to use a section where the harmony is clear. Check the file plays properly before you drop it in.</p>
<h2>Run the finder</h2>
<p>Drop the file into the Song Key Finder in your browser. The tool analyses the track and reports the key. Note the key name, the Camelot code and the relative key, so you have all three for your records. The tool runs in your browser, and the description says nothing is uploaded.</p>
<h2>Read the key and its relatives</h2>
<p>The key name tells you the note the song centres on, such as C major or A minor. The Camelot code is a number and a letter, which lets you see at a glance which other keys work well alongside it. The relative key is the major or minor partner, which can be useful when a song sits in a range that suits one version but not the other.</p>
<h2>Check the result by ear</h2>
<p>Play the song and sing or hum the tonic, the home note, to confirm the reading. If it sounds right, the key is probably correct. If the note feels wrong, look at the relative key, since the two can be easy to confuse. Trust your ear when the two disagree, because the goal is music that feels right.</p>
<h2>Use the key</h2>
<ol>
<li>For singing, check whether the melody sits in your comfortable range.</li>
<li>For mixing, use the Camelot code to match a vocal or sample to the beat.</li>
<li>For a transpose, count the semitones from the key to the new key.</li>
<li>For songwriting, choose a key that suits the voice and the chords you want.</li>
<li>Check the final choice by listening, and adjust by ear.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Trusting the reading without checking the home note by ear.</li>
<li>Confusing the key with the relative key, which share the same notes.</li>
<li>Using a noisy or heavily processed file, which can give a less reliable reading.</li>
<li>Assuming a song has one key throughout, when it may modulate.</li>
<li>Forgetting that a key suits a voice only if the melody sits in range.</li>
</ul>
<h2>Check the key against the chords</h2>
<p>Play the chords of the song, or a simple progression you can hear, and listen for the note the song settles on. The home note is usually the key, although some songs move between centres. If the tool gives a key that does not match what you hear, look at the chord shapes and the bass line before deciding which to trust.</p>
<h2>When the key is unclear</h2>
<p>Some tracks, such as ambient pieces, modal music or songs with a long intro, do not have one clear centre. In these cases the tool may return an answer that is technically possible but musically weak. Note the uncertainty, and choose a key by the sound that suits the singer or the instrument rather than by the number alone.</p>
<h2>Limits</h2>
<p>A key reading describes the harmony as the tool hears it, and some music is ambiguous or changes key partway through. The tool cannot judge whether a key suits a voice, and it cannot tell you the best key for a performance. Use the reading as a starting point, and let your ear and your voice make the final choice.</p>
<h2>Try the Song Key Finder</h2>
<p>Find the key of your next reference track. The <a href="/tunedzy/tools/song-key-finder">Song Key Finder</a> is free and runs in your browser. For the tempo side of a track, the guide to <a href="/tunedzy/blog/how-to-find-the-bpm-of-a-song">finding the BPM</a> covers the BPM Finder, and the <a href="/tunedzy/tools/bpm-finder">BPM Finder</a> reports tempo for any song or beat.</p>
''',
    faq=[('What is the Camelot code?', 'A number and letter notation that shows which keys mix well together, used by DJs and producers.'),
         ('Why does the key sound wrong?', 'You may be hearing the relative key. Check the home note by ear, and try the other key.'),
         ('Can a song change key?', 'Yes, some do. The tool reports the key it finds, which may not hold for the whole track.'),
         ('Does a reading tell me the best key for my voice?', 'No. It tells you the key, and you must check that the melody sits in your range.')])

add(slug='how-to-record-a-voice-over-in-your-browser', cluster='app-how-to', kw='record voice over in browser',
    title='Record a Voice-Over in Your Browser With the Noise-Free Voice Recorder',
    desc='How to record a voice-over in your browser with the Noise-Free Voice Recorder: setting up, recording with live noise removal and cleaning an existing recording.',
    h1='Record a Voice-Over in Your Browser With the Noise-Free Voice Recorder',
    answer='The Noise-Free Voice Recorder runs in your browser and lets you record voice-overs and content with live noise removal, or clean an existing recording. Set up a quiet spot, test the microphone, record in short takes and check the result on headphones and a phone. The tool describes itself as private, in your browser.',
    body='''
<p>A voice-over does not need a studio. With a quiet room, a decent microphone and a browser, you can record narration for a video, a presentation or a short course. The Noise-Free Voice Recorder is a free tool that records voice-overs in your browser, and it offers live noise removal while you record. It can also clean an existing recording. This guide walks through setting up and recording a voice-over with it.</p>
<p>The steps below assume a laptop or a computer with a microphone. A separate microphone usually gives a better result, and the placement advice applies whichever microphone you use.</p>
<h2>Choose the spot</h2>
<p>Pick the quietest room you have, with soft surfaces around you. A bedroom with curtains, a rug and some cushions often works well. Turn off fans, air conditioners and notifications, and close the door. Record a few seconds of silence to hear what the room sounds like with nobody speaking, since that is the background you are working against.</p>
<h2>Set up the microphone</h2>
<p>Place the microphone a hand’s width or two from your mouth, slightly to one side, and keep that distance for the whole session. Use a pop filter or a foam windscreen to soften breath sounds. If you use a built-in laptop microphone, sit close to the screen and keep your head still, since laptop microphones pick up more room sound at a distance.</p>
<h2>Test before you record</h2>
<p>Record ten seconds of you reading a paragraph at your normal speaking voice. Play it back on headphones, and check for echo, background noise and whether the voice is clear. Watch the level, and keep the peaks comfortably below the top. Adjust the position or the room, and test again until the sound is right.</p>
<h2>Record in short takes</h2>
<p>Record each sentence or short paragraph as its own take, with a short pause between. Short takes are easier to check and easier to replace, and they keep your energy steady. If you make a mistake, repeat the line from the start of the sentence, rather than in the middle of a word.</p>
<h2>Use live noise removal wisely</h2>
<p>The tool offers live noise removal while you record. Use it at the level that suits the room, and listen to the result on headphones. If the voice starts to sound watery or thin, reduce the processing, and rely more on a quiet room and a close microphone. The aim is a natural voice with the background kept down, not a voice with every sound removed.</p>
<h2>Check the take</h2>
<p>After recording, listen to the whole take on headphones and on a phone speaker. Check for clicks, dropouts, breath noise and any change in level. Re-record any take that has a problem you cannot accept, rather than trying to fix it heavily afterwards.</p>
<h2>Clean an existing recording</h2>
<p>The same tool can clean a recording you already have. Load the file, apply the cleaning gently and compare it with the original at the same level. Keep the original, so you can go back if the cleaned version sounds worse. Light cleaning is almost always better than heavy cleaning.</p>
<h2>Common mistakes</h2>
<ul>
<li>Recording in a room with hard, echoey surfaces.</li>
<li>Letting the microphone drift away from the mouth during a take.</li>
<li>Recording long takes, so a single mistake spoils the whole thing.</li>
<li>Using heavy noise removal that makes the voice sound artificial.</li>
<li>Skipping the check on headphones and a phone before delivery.</li>
</ul>
<h2>Read the script aloud first</h2>
<p>Read the script once at speaking pace before you record, and mark any word or phrase that trips you. Rewrite awkward sentences, add a breath mark where you will need one and check the pronunciation of any name. A script that is easy to say produces a smoother take and reduces the number of retakes you need.</p>
<h2>Save and name each take</h2>
<p>Give each take a short name that records the section and the take number, such as intro-2. Keep the best take in a separate folder, and note its number in the script. A clear system makes editing faster, and it stops you losing the take you wanted in a pile of similar files.</p>
<h2>Checking the take before moving on</h2>
<p>After each take, listen back for a moment before recording the next line. Check that the level was steady, that the words were clear and that no sound from the room intruded. A quick listen catches a problem while the script is still fresh, which is far quicker than discovering it during editing.</p>
<h2>Limits</h2>
<p>A browser recording is limited by the microphone and the room. A very noisy space or a distant microphone will produce a noisier voice-over than a close recording in a quiet room, whatever the tool does. For a professional release, a higher quality setup may be worth the investment.</p>
<h2>Try the Noise-Free Voice Recorder</h2>
<p>Record your next voice-over in the browser. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> is free and runs in your browser. For a phone recording, the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording, and the guide to <a href="/tunedzy/blog/how-to-record-voice-over-for-youtube-videos">voice-over for YouTube</a> covers the wider setup.</p>
''',
    faq=[('Do I need a special microphone?', 'Not to start. A close, steady microphone in a quiet room matters more than the model.'),
         ('Can it clean a recording I already made?', 'Yes. The tool can clean an existing recording, and you should keep the original.'),
         ('How much noise removal should I use?', 'The least that solves the problem. Heavy removal can make the voice watery.'),
         ('Is my recording private?', 'The tool describes itself as private and running in your browser. Check its page for the current details.')])

add(slug='how-to-clean-a-noisy-recording-online', cluster='app-how-to', kw='clean noisy recording online',
    title='How to Clean a Noisy Recording Online in Your Browser',
    desc='How to clean a noisy recording online in your browser: what cleanup can and cannot do, the order of the steps and how to compare the result with the original.',
    h1='How to Clean a Noisy Recording Online in Your Browser',
    answer='You can clean a noisy recording in your browser with the Noise-Free Voice Recorder, which can clean background noise from an existing recording. Check the recording first, clean gently, compare the result with the original at the same level and keep the original. Cleanup helps most with steady background noise and cannot restore speech that noise has covered.',
    body='''
<p>Many recordings come with a background problem: a fan, a street, a room tone that is louder than it should be. A browser-based cleaning tool can reduce that background without installing software, which is useful when you need a quick result. The key is to set expectations. Cleanup reduces steady noise well, struggles with sudden sounds, and cannot restore words that the noise has covered.</p>
<p>This guide explains how to approach a noisy recording in the browser, the order of the steps and the checks that keep the voice natural.</p>
<h2>What cleanup can and cannot do</h2>
<p>Cleanup works best on steady background sounds, such as a fan, a hum or a constant room noise. It reduces these by estimating what is noise and what is voice. It does less well with sudden noises, such as a door, a cough or a passing vehicle, and it cannot bring back speech that is buried under a loud sound. Knowing this helps you decide whether a recording is worth cleaning or should be re-recorded.</p>
<h2>Check the recording first</h2>
<p>Listen to the whole recording on headphones and note the problems. Is the noise steady or sudden? Are there clicks, dropouts or clipping? Is the level even? Cleaning should come after the faults are noted, because a click or a clip is not improved by noise reduction. Use the Vocal Checker to look at clipping, noise, rumble and level, and fix the most serious problem first.</p>
<h2>Run the cleanup gently</h2>
<p>Open the recording in the Noise-Free Voice Recorder, and apply the cleaning at the lightest setting that makes a difference. Listen to the result before increasing the amount. A small reduction that keeps the voice natural is usually better than a large reduction that makes it thin or watery.</p>
<h2>Compare with the original</h2>
<p>Play the cleaned version and the original at the same level, one after the other. Listen to the quiet pauses for the background, and to the consonants and the breath for signs of damage. If the cleaned version sounds clearer without sounding artificial, it is an improvement. If it sounds thinner or more distant, reduce the amount or keep the original.</p>
<h2>Keep the original</h2>
<p>Always keep the original file untouched. Cleaning is a change you may want to undo, and a second attempt is only possible if the original is safe. Save the cleaned version with a clear name, so you can tell the two apart.</p>
<h2>Fix the remaining problems by hand</h2>
<p>Sudden clicks and pops are usually better fixed by hand, by zooming in and smoothing each one with a short fade. Level changes can be corrected with gentle gain changes. These targeted repairs keep the voice more natural than a broad cleaning would.</p>
<h2>Common mistakes</h2>
<ul>
<li>Cleaning before fixing clipping or clicks.</li>
<li>Using a strong setting to remove every trace of background.</li>
<li>Judging the result on headphones alone, without a phone check.</li>
<li>Overwriting the original, and losing the chance to try again.</li>
<li>Expecting cleanup to recover words that the noise has covered.</li>
</ul>
<h2>Choose a short section to test first</h2>
<p>Pick ten or fifteen seconds that contain both speech and the noise you want to remove, such as a pause with a hum or a passage with traffic. Try the settings on that section before applying them to the whole file. A short test shows whether the voice survives, and it saves time if the first attempt is too heavy.</p>
<h2>Know when to stop</h2>
<p>If each step makes the voice sound more distant or more processed, the file has reached its limit. At that point the most useful option may be to accept some background, or to re-record the part that matters. Pushing the cleanup further usually damages the speech more than it improves the noise.</p>
<h2>Judging the cleaned file on a second device</h2>
<p>A cleaned file can sound fine on the device used to make it and worse on another. Listen to the result on headphones, on a laptop speaker and on a phone, at the same level as the original. Pay attention to the voice first, then the background. If the voice sounds hollow or thin on any device, the cleanup has gone too far, and a lighter setting is the better choice. Keep notes on the setting that worked, so the next recording starts from a known point.</p>
<h2>Limits</h2>
<p>Browser cleanup is quick and convenient, but it is limited by the recording. A very noisy or distant recording will stay noisy, and the best result comes from a better recording. The tool reduces noise; it does not make a poor recording into a studio one.</p>
<h2>Try the cleanup on your recording</h2>
<p>Run a gentle cleanup on your next noisy recording. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> is free and runs in your browser. Check the result with the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a>, and for a phone recording, the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning in your phone’s browser.</p>
''',
    faq=[('Can a browser tool clean any recording?', 'It works best on steady noise in a reasonably clear recording. It cannot restore covered speech.'),
         ('Should I clean before or after fixing clicks?', 'Fix clicks and clipping first, then clean the steady noise.'),
         ('How do I know the cleaning worked?', 'Compare with the original at the same level, and listen to the quiet pauses and the consonants.'),
         ('Should I keep the original?', 'Always. It lets you try again or undo a cleaning you regret.')])

add(slug='free-audio-tools-that-run-in-the-browser', cluster='app-how-to', kw='free browser audio tools',
    title='Free Audio Tools That Run in Your Browser: What Each One Is For',
    desc='Free audio tools that run in your browser: what each one is for, when a browser tool suits a job and when a desktop editor is the better choice.',
    h1='Free Audio Tools That Run in Your Browser: What Each One Is For',
    answer='Several free audio tools run in your browser: the Vocal Checker for clipping, noise, rumble and level, the LUFS Meter for loudness, the Song Key Finder and BPM Finder for musical information, the Chord Finder for progressions, and the Noise-Free Voice Recorder for recording and cleaning. Each has a specific job, and a browser tool suits quick checks well.',
    body='''
<p>Browser audio tools have become a practical part of many workflows. They need no installation, they open quickly and they handle many quick jobs well: checking a file, finding a key, measuring loudness or recording a short voice-over. They do not replace a full editor or a studio, but used for the right tasks they save time and reduce friction. This guide sets out what the main free tools are for and where each one fits.</p>
<p>The descriptions here follow what each tool says about itself. Check each tool’s page for the current details.</p>
<h2>The Vocal Checker</h2>
<p>The Vocal Checker drops in a recording and reports clipping, noise, rumble and level problems, with plain-English fixes. It is a quick check before publishing a vocal, and it helps you decide what to fix first. It describes itself as private and running in your browser.</p>
<h2>The LUFS Meter</h2>
<p>The LUFS Meter shows integrated loudness, true peak and loudness range for a mix or master, and what Spotify, YouTube and Apple Music would do to the file. It is the tool for checking a master or an export against a target. It helps you avoid both the weak, quiet master and the squashed, over-loud one.</p>
<h2>The Song Key Finder</h2>
<p>The Song Key Finder reports the key of a song or beat, the Camelot code and the relative key. It runs in your browser, and its description says nothing is uploaded. It is useful for singers choosing a range, for producers matching a beat and for anyone planning a transpose.</p>
<h2>The BPM Finder</h2>
<p>The BPM Finder reports the tempo of any song or beat, and it includes a tap tempo option. Its description says the file never leaves your browser. It is useful for matching a track to a tempo, for planning a loop and for building playlists by pace.</p>
<h2>The Chord Finder</h2>
<p>The Chord Finder shows the chord progression, the repeating loop and Roman numerals for a song. It runs in your browser. It helps songwriters learn a song’s structure and helps producers understand how a loop is built.</p>
<h2>The Noise-Free Voice Recorder</h2>
<p>The Noise-Free Voice Recorder records voice-overs and content with live noise removal, or cleans an existing recording. It is designed for speech and narration, and it runs in your browser.</p>
<h2>Live Autotune and Clean Streaming Mic</h2>
<p>Live Autotune lets you turn on your microphone, pick a key, hear yourself autotuned in real time and record the take. The Clean Streaming Mic learns your room noise, cleans it in real time and feeds OBS, Discord or Zoom. Both are designed for live use, and both describe themselves as private and in the browser.</p>
<h2>When a browser tool suits the job</h2>
<ul>
<li>Quick checks on a finished file, before publishing.</li>
<li>Finding a key, tempo or chord progression for a reference track.</li>
<li>Recording a short voice-over without installing software.</li>
<li>Live use, where a browser tool is ready on any computer.</li>
</ul>
<h2>When a desktop editor is better</h2>
<ul>
<li>Long, complex edits with many tracks and effects.</li>
<li>Work that needs fine control over every parameter.</li>
<li>Sessions that must run offline, or with very large files.</li>
<li>Mixing and mastering that needs a full signal chain.</li>
</ul>
<h2>Keeping files private</h2>
<p>The tools described here run in your browser, and the file stays on your device. That makes them useful for unreleased material, private recordings and work under a client's confidentiality. Check the page of any tool before you rely on it for sensitive work, and keep your own backup, since a browser tab is not a storage system.</p>
<h2>Combining tools in a sensible order</h2>
<p>A common route is to check a recording for problems first, clean it lightly if needed, check the loudness of the finished file, and then look at the key and tempo if you are working with music. Each step answers one question. Working in that order keeps the decisions clear, and it avoids fixing a problem that a later step would create.</p>
<h2>Checking that a tool is working as expected</h2>
<p>Before you trust a result from any browser tool, check it against a file where you already know the answer. Use a recording with a known level, or a simple tone at a set frequency, and see whether the tool reports what you expect. A quick known-answer check takes a minute and catches a misreading before it reaches a finished file. A short note of the result keeps the check easy to repeat, and it is worth repeating when the tool changes.</p>
<h2>Limits</h2>
<p>Browser tools have limits in size, control and speed, and their features change over time. Use them for the jobs they do well, and move to a fuller editor when the work demands it. Check each tool’s own description for the current details.</p>
<h2>Start with a quick check</h2>
<p>Try a browser tool on your next file. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a>, the <a href="/tunedzy/tools/lufs-meter">LUFS Meter</a> and the <a href="/tunedzy/tools/song-key-finder">Song Key Finder</a> are a good place to start, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers phone recordings.</p>
''',
    faq=[('Do browser audio tools need installing?', 'No. They run in your browser, which is their main convenience.'),
         ('Are they private?', 'Several describe themselves as private and running in the browser. Check each tool’s page.'),
         ('Can they replace a full editor?', 'For quick, focused jobs, often yes. For complex edits, a full editor is better.'),
         ('Which tool should I try first?', 'The one that matches your next job, such as the Vocal Checker before publishing a vocal.')])

add(slug='tunedzy-go-on-your-phone-explained', cluster='app-how-to', kw='audio app for phone',
    title='Tunedzy Go on Your Phone: What It Does and How to Start',
    desc='Tunedzy Go on your phone explained: what it does for a phone recording, how to open it in your browser and how to start with a first clean recording.',
    h1='Tunedzy Go on Your Phone: What It Does and How to Start',
    answer='Tunedzy Go runs in your phone’s browser and helps you clean a phone recording, so a voice memo or a phone interview can become a cleaner file. Open the Tunedzy Go page, record or load a short test, clean it gently and compare the result with the original. Keep the original file, and check the result on headphones and a speaker.',
    body='''
<p>Most people already carry a capable recorder in their pocket, and a phone can produce clear speech when it is used well. The gap between a usable phone recording and a clean one is often a matter of cleanup, and Tunedzy Go is designed to help with that on a phone. It runs in your phone’s browser, so there is nothing to install, and it works with recordings you already have. This guide explains what it does and how to start.</p>
<p>The aim is practical: a clearer voice from a phone recording, with the original kept and the result checked by ear.</p>
<h2>What Tunedzy Go does</h2>
<p>Tunedzy Go is the phone version of the Tunedzy tools. It is built to clean speech recorded on a phone, reducing background noise and tidying the sound so that the voice is easier to follow. It is best used for voice memos, phone interviews, lectures and short voice-overs, where the phone is the only recorder.</p>
<p>It is a cleanup tool, not a magic fix. A recording made far from the microphone or in a very noisy place will remain difficult, whatever the cleanup.</p>
<h2>Open it in the browser</h2>
<p>Open the Tunedzy Go page in your phone’s browser. Because it runs in the browser, you do not need to install an app to start. Keep the page open while you work, and check that the recording you want to clean is saved where you can reach it on the phone.</p>
<h2>Start with a short test</h2>
<p>Choose a short recording, around thirty seconds, with a clear mix of speech and background. Clean the test first, to see what the tool does to your voice in your room. A short test saves time and shows whether the setting suits the recording before you process a long file.</p>
<h2>Clean gently</h2>
<p>Use the lightest cleanup that makes the voice clearer. Listen to the result on headphones and on the phone speaker. If the voice sounds thin, watery or distant, reduce the amount, since a little background is better than a damaged voice.</p>
<h2>Compare and keep the original</h2>
<p>Play the cleaned version and the original at the same level, one after the other. Keep the original file untouched, so you can compare again or start over. Save the cleaned version with a clear name, such as the date and the word cleaned.</p>
<h2>Check the result</h2>
<p>Listen to the final file on headphones and on a phone speaker, in a quiet place and a noisy one if you can. Check that the words are clear and the voice sounds natural. If a problem remains, re-record the section if you can, rather than pushing the cleanup further.</p>
<h2>A first session</h2>
<ol>
<li>Open the Tunedzy Go page in your phone’s browser.</li>
<li>Choose a thirty-second test from a recording you have.</li>
<li>Clean it gently, and compare with the original.</li>
<li>Keep the original, and save the cleaned version with a clear name.</li>
<li>Check both versions on headphones and a phone speaker.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Cleaning a long file before testing a short sample.</li>
<li>Pushing the cleanup until the voice sounds artificial.</li>
<li>Overwriting or deleting the original recording.</li>
<li>Judging the result only in a quiet room.</li>
<li>Expecting cleanup to fix a recording made too far from the microphone.</li>
</ul>
<h2>Record well in the first place</h2>
<p>Hold the phone steady, keep it a comfortable distance from the mouth and turn off notifications before you begin. A closer and steadier recording gives the cleanup less to do, and it keeps more of the voice. Most of the improvement comes from the recording habit, not from the processing afterwards.</p>
<h2>Share the cleaned file carefully</h2>
<p>Check the cleaned version on headphones and a phone speaker before you send it on. Keep the original alongside it, and name the cleaned version so the difference is clear. If a colleague or client needs the file, say which version it is and what cleanup was applied.</p>
<h2>Working in a noisy place</h2>
<p>If you must record in a busy place, such as a café or a street, move the phone closer to the voice and turn your back to the noise where you can. Shield the microphone from wind with a cloth or a foam cover. A closer recording of the voice gives the cleanup a better starting point than a distant one.</p>
<h2>Limits</h2>
<p>Tunedzy Go is limited by the phone’s microphone and the recording conditions. It cleans what is there; it cannot restore speech that was never captured clearly. Results depend on the recording, the device and the browser, so test on your own material. Check the Tunedzy Go page for the current features and any requirements.</p>
<h2>Start with your next phone recording</h2>
<p>The next time you have a voice memo worth keeping, try a short test on Tunedzy Go. The <a href="/tunedzy/go/">Tunedzy Go</a> page is where to start. For the phone recording habits that give the cleanest result, read the guide to <a href="/tunedzy/blog/how-to-record-a-voice-memo-on-an-iphone">recording a voice memo on an iPhone</a>, and the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> can check the cleaned file.</p>
''',
    faq=[('Do I need to install anything?', 'No. Tunedzy Go runs in your phone’s browser, so you can open it straight away.'),
         ('Can it clean any phone recording?', 'It cleans what is there. A recording made far from the microphone will stay difficult.'),
         ('Should I keep the original?', 'Always. It lets you compare, or start again, if the cleaned version does not suit.'),
         ('Is it for long recordings?', 'Test with a short sample first. Long files take longer, so check a sample before processing all of it.')])

add(slug='how-to-check-a-podcast-loudness-online', cluster='app-how-to', kw='check podcast loudness online',
    title='How to Check a Podcast Episode’s Loudness Online Before You Publish',
    desc='How to check a podcast episode’s loudness online before you publish: what to measure on the export, what the LUFS Meter reports and how to act on the result.',
    h1='How to Check a Podcast Episode’s Loudness Online Before You Publish',
    answer='To check a podcast episode’s loudness online, export the finished episode, drop it into the LUFS Meter and read the integrated loudness, true peak and loudness range. Compare the integrated figure with your target, reduce the level if the true peak is too close to zero, and confirm the result by listening on a phone before publishing.',
    body='''
<p>A podcast episode is judged on its loudness as much as on its content. An episode that is quieter than the rest of a listener’s playlist will be turned up, and the next louder episode will feel uncomfortable. An episode that clips on playback sounds harsh. A quick loudness check on the exported file catches both problems before the episode reaches listeners.</p>
<p>This guide explains how to run the check with the LUFS Meter, what each figure means for a speech episode and how to act on the result.</p>
<h2>Export the finished episode</h2>
<p>Export the episode in the format you will publish, not from the editing project. The export can change the level and the peaks, so the file you measure should be the one listeners will hear. Check that it plays from start to end, with the intro, the outro and the music in place.</p>
<h2>Drop it into the LUFS Meter</h2>
<p>Drop the exported file into the LUFS Meter in your browser. The tool reports the integrated loudness, the true peak and the loudness range, along with what the major streaming services would do to the file on playback. Read each figure before changing anything.</p>
<h2>Read the integrated loudness</h2>
<p>The integrated figure is the average loudness of the whole episode. Compare it with the target you set for your show, and with the platform guidance you are delivering to. Speech often sits in a particular range, and a consistent target from episode to episode helps your show sound the same to listeners.</p>
<h2>Read the true peak</h2>
<p>The true peak tells you whether the episode is likely to clip on playback. If it is above zero, or very close to it, reduce the level or the limiting until there is headroom. Clipping on a voice is harsh and distracting, and it is one of the faults listeners notice most.</p>
<h2>Read the loudness range</h2>
<p>For speech, the loudness range shows how much the level varies. A very wide range can mean quiet passages that are hard to hear on a phone in a noisy place. A very narrow range can mean a squashed, tiring voice. Choose a balance that keeps the words clear without flattening the natural expression of the speakers.</p>
<h2>Act on the result</h2>
<ol>
<li>Adjust the level to bring the integrated loudness close to your target.</li>
<li>Reduce the level or the limiting if the true peak is too close to zero.</li>
<li>Check the loudness range, and adjust the balance of quiet and loud passages.</li>
<li>Re-export the episode, and measure the new file.</li>
<li>Listen to the whole episode on a phone speaker before publishing.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Measuring the project rather than the exported file.</li>
<li>Raising the whole episode without checking the peaks.</li>
<li>Using a different target for each episode, so the show sounds uneven.</li>
<li>Judging the loudness only on headphones.</li>
<li>Forgetting to re-measure after a change.</li>
</ul>
<h2>Check the intro, the adverts and the segments</h2>
<p>Check each part of the episode, not only the whole file. An intro with music, a host-read advert and an interview segment can each sit at a different level, even when the total seems right. Export the segments separately if you can, or check the full episode and listen closely at the joins. A loud advert after a quiet interview is one of the most common complaints listeners notice.</p>
<p>Music under speech needs its own check. Play the bed at the level you intend, then listen to the voice on top. If the voice has to strain to be heard, lower the music rather than raising the voice until it clips.</p>
<h2>Compare episodes over time</h2>
<p>Keep a short log of the integrated loudness and the true peak for each episode. The numbers help you see drift, such as a guest who was recorded quietly, or an edit that added a louder section. A log lets you set a target for the series and check new episodes against it, rather than judging each one from memory. Use the numbers as a guide and your ear as the final check.</p>
<h2>Listening on other devices</h2>
<p>Play the finished episode on a phone and, if you can, in a car, and listen for places where the speech is hard to follow. A level that works on studio headphones can sound thin or harsh on a small speaker. Use these device checks to decide whether the speech needs more presence, not only whether the loudness number is correct.</p>
<h2>Limits</h2>
<p>The meter reports measurements, and it cannot judge the warmth, clarity or pacing of the episode. Platform behaviour can change, so check the current guidance before publishing. Use the figures as a guide, and trust the listening check on the devices your listeners use.</p>
<h2>Check your next episode</h2>
<p>Run the check on your next export before publishing. The <a href="/tunedzy/tools/lufs-meter">LUFS Meter</a> is free and runs in your browser. For the voice itself, the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise, rumble and level problems, and the guide to <a href="/tunedzy/blog/podcast-export-settings-for-hosts-explained">podcast export settings</a> covers the export.</p>
''',
    faq=[('What loudness should a podcast be?', 'Set a steady target for your show and check the platform guidance you deliver to.'),
         ('Why check the export?', 'The export can change the level and peaks, so it is the file listeners will hear.'),
         ('What is the most important figure for speech?', 'The true peak, to avoid clipping, and the integrated loudness, to keep episodes consistent.'),
         ('How often should I check?', 'Every episode, before publishing, so the show stays consistent over a season.')])

add(slug='bpm-finder-for-workout-playlists', cluster='app-how-to', kw='bpm for workout playlist',
    title='Using a BPM Finder to Build Workout Playlists by Tempo',
    desc='Using a BPM finder to build workout playlists by tempo: how to find the BPM of a track, sort by pace and check the result by ear for a steady session.',
    h1='Using a BPM Finder to Build Workout Playlists by Tempo',
    answer='The BPM Finder reports the tempo of a song or beat, and its tap tempo option helps when you want to check by hand. Use the BPM to sort tracks by pace, build a playlist that rises and falls with a workout, and check each transition by ear. The file stays in your browser, according to the tool’s description.',
    body='''
<p>Tempo matters to a workout. A steady beat helps set a rhythm, a faster one can lift the pace, and a slower one can ease a cool-down. Building a playlist by tempo is one of the most practical uses of a BPM reading, because it turns a list of songs into a session with a shape. The BPM Finder is a free tool for reading the tempo of any song or beat, and it includes a tap tempo option for checking by hand.</p>
<p>This guide explains how to find the tempo, how to sort a playlist by pace and how to check the result for a session that feels right.</p>
<h2>What the BPM Finder reports</h2>
<p>The BPM Finder reports the tempo of a song or beat in beats per minute. Drop in a track and read the figure. The tool also offers tap tempo, which lets you tap along to the beat and read the tempo yourself, useful for checking a reading or for tracks where you want a manual result. The tool describes itself as private, with the file never leaving your browser.</p>
<h2>Prepare the tracks</h2>
<p>Gather the tracks you want to consider, and make sure each file plays properly. A track with a clear beat in the main section gives the most reliable reading. Tracks with a long, free intro may need a section with a steady pulse, so check the reading by listening to where the beat is clear.</p>
<h2>Find the tempo of each track</h2>
<p>Drop each track into the BPM Finder, and note the reading. Record the tempo in a simple list next to the title. If a reading seems odd, check it with tap tempo, tapping along to the main beat for about ten seconds. A tempo that is double or half of the one you expected is a common case, so check that you have the right beat.</p>
<h2>Sort by pace</h2>
<p>Sort the list by tempo, from slow to fast. This gives you a set of tracks you can arrange into a session. A warm-up can start slower and build, a main set can hold the fastest tracks, and a cool-down can return to the slower end. The order of the tempos does more for the session than any single track.</p>
<h2>Check the transitions by ear</h2>
<p>A big jump in tempo can jolt the rhythm, so place tracks with a gradual change next to each other. Listen to each transition at the workout pace, and move a track if the change feels abrupt. The aim is a session that feels like one flow, not a list of songs.</p>
<h2>Use the key too</h2>
<p>Tempo is not the only factor. A track in a key that suits a particular mood, or that is easy to sing along with, may matter as much as its pace. The Song Key Finder can help with the key, as covered in the guide to <a href="/tunedzy/blog/how-to-find-a-songs-key-in-your-browser">finding a song’s key</a>.</p>
<h2>Common mistakes</h2>
<ul>
<li>Trusting one reading without checking the main beat.</li>
<li>Mixing double and half tempos without noticing.</li>
<li>Making big jumps in tempo between tracks.</li>
<li>Choosing tracks by BPM alone, and ignoring how they feel.</li>
<li>Leaving the playlist unchecked at the workout pace.</li>
</ul>
<h2>Tap tempo for tracks the finder misreads</h2>
<p>Some tracks have a loose groove, a slow intro or a tempo that shifts. If the reading does not match what you hear, tap along to the beat for a few bars and compare the two. Use the tapped value when it fits the feel of the track, and note any track where the tempo is unclear, so you can check it before a workout.</p>
<h2>Build the playlist around the session</h2>
<p>Start with the warm-up pace, move through the main block and finish with the cool-down. A playlist shaped around the plan keeps the energy where you want it. Test the order once on a short run or a walk before you rely on it, since a track that feels right on the sofa may not suit the pace of a run.</p>
<h2>Keeping the playlist current</h2>
<p>Playlists drift as tastes change and new tracks arrive. Review the list every few weeks, remove tracks that no longer suit the session and add new ones with a known tempo. Note the BPM beside each track, so the next update takes minutes rather than an afternoon.</p>
<h2>Limits</h2>
<p>A tempo reading is a measurement, and some tracks have changing tempos or a loose beat that does not suit a single number. The reading also says nothing about how a track will feel during a session. Use the BPM as a guide, and test the playlist during an actual workout before relying on it.</p>
<h2>Try the BPM Finder</h2>
<p>Read the tempo of your next playlist. The <a href="/tunedzy/tools/bpm-finder">BPM Finder</a> is free and includes tap tempo. For the key of the same tracks, the <a href="/tunedzy/tools/song-key-finder">Song Key Finder</a> reports the key, the Camelot code and the relative key.</p>
''',
    faq=[('How accurate is a BPM reading?', 'Good for most steady tracks. Check odd readings with tap tempo on the main beat.'),
         ('What if the tempo is double or half?', 'Check the main beat by tapping. Many tracks have a feel at either the double or the half of a reading.'),
         ('How do I order a workout playlist?', 'Sort by tempo, start slower, build in the main set and return to slower for the cool-down.'),
         ('Is my file uploaded?', 'The tool describes itself as private, with the file staying in your browser. Check its page for the current details.')])

add(slug='chord-finder-for-songwriters', cluster='app-how-to', kw='chord finder for songwriters',
    title='Using a Chord Finder as a Songwriter: Progressions and Loops',
    desc='Using a chord finder as a songwriter: reading chord progressions, spotting repeating loops, understanding Roman numerals and using them to learn and write.',
    h1='Using a Chord Finder as a Songwriter: Progressions and Loops',
    answer='The Chord Finder shows the chord progression, the repeating loop and Roman numerals for a song. Songwriters can use it to learn how a song is built, spot the loop that repeats and see the Roman numerals that describe the relationships between chords. Use the reading to learn, then write your own progression and check it by ear.',
    body='''
<p>Many songwriters learn by studying songs they love, and a chord progression is one of the best things to study. Working out the chords by ear takes time, and a reference reading can speed the process. The Chord Finder is a free tool that shows the chord progression of a song, the repeating loop and the Roman numerals that describe how the chords relate. It is a learning aid, and a way to start writing your own material.</p>
<p>This guide explains how to read the output, how to use the loop and the Roman numerals in your writing and how to check the result by ear.</p>
<h2>What the Chord Finder reports</h2>
<p>The Chord Finder shows the chord progression of a song, the repeating loop and Roman numerals. The progression is the sequence of chords. The loop is the part that repeats, which is often the core of a verse or a chorus. Roman numerals describe each chord by its position in the key, which makes it easier to see how the chords relate and to transfer the pattern to another key.</p>
<h2>Prepare the song</h2>
<p>Use a clean version of the song, ideally with the harmony clear. A full mix with a steady chord pattern gives the best reading. Songs with a sparse arrangement or a changing feel may be harder to read, so listen to the section you want to study and check that the chords are clear.</p>
<h2>Run the reading</h2>
<p>Drop the song into the Chord Finder in your browser. The tool analyses the track and shows the progression and the loop. Note the loop first, since it is the part you are most likely to use, and then the progression around it. The tool runs in your browser, and its description says nothing is uploaded.</p>
<h2>Read the Roman numerals</h2>
<p>Roman numerals show the chords by their position in the key. A chord labelled I is the home chord, IV is the chord four steps up, and V is the chord five steps up. Minor chords are often shown in lower case. The numerals are useful because they let you move the same pattern to any key, and they show the emotional logic of a progression, such as the pull from V back to I.</p>
<h2>Learn from the loop</h2>
<p>Play the loop on an instrument, and sing a melody over it. Then try changing one chord, or swapping the order, and listen to how the feel changes. Learning a loop in several keys strengthens your understanding of the pattern, and it prepares you for writing your own version.</p>
<h2>Write your own progression</h2>
<p>Take the Roman numeral pattern and choose new chords for it, or write a new progression with a similar logic. Check the result by ear, since a progression that reads well on paper may not sound right. Adjust one chord at a time, and listen after each change, until the progression supports the melody you have.</p>
<h2>Check the result by ear</h2>
<p>Always confirm the reading by ear. Play the progression, and check that the chords sound as the reading says. If a chord seems wrong, listen again, since the tool and your ear may disagree on an ambiguous chord. Trust the ear, because the goal is a progression that serves the song.</p>
<h2>Common mistakes</h2>
<ul>
<li>Copying a progression without learning why it works.</li>
<li>Trusting every chord label without listening to it.</li>
<li>Forgetting that the Roman numerals describe relationships, not fixed chords.</li>
<li>Studying only one song, and missing the variety of progressions.</li>
<li>Writing a progression that reads well but does not suit the melody.</li>
</ul>
<h2>Using the finder to learn a song</h2>
<p>When you want to play a song you love, the chord reading gives you a starting point, and the loop shows which part repeats. Play the progression slowly, then at tempo, and listen for changes the reading may have missed, such as a passing chord or a short turnaround. The finder is a map, and your ear makes the final corrections.</p>
<h2>Changing the progression on purpose</h2>
<p>Once you can hear a progression clearly, change one chord at a time and listen to how the mood shifts. Swapping a chord for its relative, or moving the last chord of a loop, can give a new feeling without losing the song's structure. Record each version so you can compare them later.</p>
<h2>Limits</h2>
<p>A reading describes the harmony as the tool hears it, and some chords are ambiguous or sit between two labels. Songs can use inversions, passing chords and modal colours that a simple reading does not show. Use the reading as a starting point, and learn the detail by ear.</p>
<h2>Try the Chord Finder</h2>
<p>Read the progression of a song you love, and try writing your own version. The <a href="/tunedzy/tools/chord-finder">Chord Finder</a> is free and runs in your browser. For the key that goes with a progression, the <a href="/tunedzy/tools/song-key-finder">Song Key Finder</a> reports the key and its relatives.</p>
''',
    faq=[('What are Roman numerals in a chord progression?', 'Labels that show each chord by its position in the key, so the pattern can move to any key.'),
         ('What is a repeating loop?', 'The part of the progression that repeats, often the core of a verse or chorus.'),
         ('Should I trust every chord label?', 'Check by ear. The reading can be ambiguous, and your ear decides what sounds right.'),
         ('Can I copy a progression?', 'Learn from it, and write your own version. Using a progression is a common practice, but the melody and the choices should be yours.')])
