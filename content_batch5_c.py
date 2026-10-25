"""Batch 5c (25 October 2026): ten problem-fix pages. Each starts from what the listener hears, then gives the cause and the fix.

GROUP_OF marks every page 'problem' for the guides hub.
"""

PHOTO = {}
TOOLS = {}
GUIDES = {}
ORDER = []
GROUP_OF = {}


def add(slug, photo, tools, **g):
    GUIDES[slug] = g
    PHOTO[slug] = photo
    TOOLS[slug] = tools
    ORDER.append(slug)
    GROUP_OF[slug] = 'problem'


add('my-audio-has-background-hiss', 'booth', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='My Audio Has Background Hiss: What Causes It and How to Fix It',
    desc='A constant hiss under a recording has a few common causes: gain, the mic, the cable and the room. How to find the source and reduce the hiss.',
    h1='My Audio Has Background Hiss',
    kw='my audio has background hiss',
    lead='Hiss is a steady, high-pitched noise under the voice. It comes from the electronics, the gain, the room or the cable, and each has a different fix.',
    tldr=['Find out whether the hiss is there with nobody speaking; that is the noise floor.',
          'Raising the gain late raises the hiss; set the gain properly at the start.',
          'A steady hiss responds well to a noise reduction tool.',
          'Fix the source on the next recording: a quieter room, a closer mic or a better cable.'],
    body='''
<h2>Find out what is there</h2>
<p>Record ten seconds of silence and listen on headphones. If the hiss is there, it is the noise floor of your setup. If it appears only when you speak, it is more likely the gain or the cable.</p>
<h2>Gain</h2>
<p>If the level was low and you raised it later, the hiss rose with it. Set the input gain at the start so the voice is strong, as the <a href="/tunedzy/how-to-set-the-gain-on-a-microphone">gain guide</a> explains.</p>
<h2>The room and the mic</h2>
<p>A steady hiss often comes from a fan, the air conditioning, an audio interface or the mic&rsquo;s own electronics. Turn off what you can, and move the mic closer to the mouth so the voice sits above the hiss.</p>
<h2>The cable</h2>
<p>A damaged or long cable can add hiss. Try a shorter, better cable and see if the hiss changes.</p>
<h2>Clean what remains</h2>
<p>A steady hiss responds well to noise reduction. Use the lowest setting that removes it, and check the voice for a watery sound. The <a href="/tunedzy/remove-background-noise-from-a-voice-recording">noise removal guide</a> has the steps.</p>
''',
    vf_title='Reduce the hiss, keep the voice',
    vf='<p>Tunedzy&rsquo;s cleanup reduces steady hiss. Compare Before and After and use the lowest setting that works.</p>',
    faq=[('Why does hiss get worse when I raise the level?', 'Because the hiss was already there and it rises with the voice. Set the gain higher at the start.'),
         ('Is hiss from the mic or the room?', 'Record silence with the mic on and off the room noise to tell. Both are common.'),
         ('Can a noise tool remove all hiss?', 'It can reduce it a lot. Removing all of it can make the voice sound unnatural.')],
    related=['what-is-a-noise-floor', 'remove-background-noise-from-a-voice-recording', 'how-to-set-the-gain-on-a-microphone'])

add('my-audio-sounds-tinny', 'neon', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='My Audio Sounds Tinny: Why and How to Fix It',
    desc='A tinny recording has too little low end and too much middle. The usual causes, a mic or phone far away, a laptop speaker and an over-filtered file, and the fix.',
    h1='My Audio Sounds Tinny',
    kw='my audio sounds tinny',
    lead='A tinny sound is thin, hollow and nasal: the low end is missing and the middle sounds harsh. It is usually the distance, the device or a filter that went too far.',
    tldr=['A tinny recording is short of body, the low-mid range around 150 to 300 Hz.',
          'Common causes are a distant mic, a laptop or phone mic and a high-pass set too high.',
          'A small low-mid lift can bring back body without muddiness.',
          'Record closer and in a softer room for the lasting fix.'],
    body='''
<h2>What tinny means</h2>
<p>A tinny voice lacks body: the low end is thin and the middle sounds hollow or nasal. It is different from muffled, which is dull and lacks the top.</p>
<h2>Common causes</h2>
<ul>
<li>A mic far from the mouth, so the room and the reflections dominate.</li>
<li>A small built-in mic on a laptop or a phone.</li>
<li>A low cut set too high, which removes the body of the voice.</li>
<li>A codec or a compressed call that removed the low end.</li>
</ul>
<h2>The fix</h2>
<p>Start with the cause. Move closer and soften the room for the next recording. In the file, a gentle lift around 150 to 300 Hz adds body. Lower the low cut if you set it high. The <a href="/tunedzy/how-to-make-a-voice-sound-warmer">warmth guide</a> covers the steps.</p>
<h2>Check the result</h2>
<p>Listen for a boom. If the voice gets muddy, the lift is too big. Stop before the boom.</p>
''',
    vf_title='Bring back the body',
    vf='<p>Tunedzy&rsquo;s tone step adds body to a thin voice without muddiness. Compare Before and After.</p>',
    faq=[('Is tinny the same as muffled?', 'No. Tinny is thin and nasal; muffled is dull and lacks the top end.'),
         ('Can a laptop mic sound full?', 'Not as full as a close dedicated mic. Move closer and soften the room.'),
         ('Why did my call sound tinny?', 'Calls are compressed and lose low frequencies. Record locally for a fuller sound.')],
    related=['how-to-make-a-voice-sound-warmer', 'fix-a-muffled-voice-recording', 'how-to-record-a-voice-on-a-laptop-microphone']
)

add('my-voice-sounds-too-bright', 'desk', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='My Voice Sounds Too Bright: How to Calm the Top End',
    desc='A bright, harsh or hissy top end usually comes from a close mic, a sensitive mic or an over-boosted presence band. How to find it and calm it.',
    h1='My Voice Sounds Too Bright',
    kw='my voice sounds too bright',
    lead='A bright voice has too much energy at the top: sharp s sounds, a metallic edge and fatigue after a few minutes. Cut the harshness rather than adding more brightness.',
    tldr=['Brightness is often a harsh band around 3 to 6 kHz, not air at the very top.',
          'A small, broad cut in that band softens the edge.',
          'Sharp s sounds may need a de-esser rather than an EQ cut.',
          'Check the cause: a sensitive condenser mic close to the mouth can be bright.'],
    body='''
<h2>Where the brightness is</h2>
<p>Harshness usually sits between 3 and 6 kHz, the range that makes speech carry. Air sits higher. If the voice feels sharp, look at the 3 to 6 kHz band before you touch the very top.</p>
<h2>Cut, do not boost</h2>
<p>Try a broad cut of 1 to 3 dB in the harsh band, then listen. If the voice becomes dull, the cut was too big. Remove a little more brightness before you add back clarity.</p>
<h2>Sibilance</h2>
<p>If the brightness is mostly on s and sh sounds, a de-esser is the better tool. The <a href="/tunedzy/what-is-a-de-esser">de-esser explanation</a> covers the setting.</p>
<h2>The mic</h2>
<p>A sensitive condenser mic very close to the mouth can sound bright. Move back a little, or try a dynamic mic for a softer top end.</p>
''',
    vf_title='Soften the edge, keep the clarity',
    vf='<p>Tunedzy&rsquo;s tone and de-ess steps soften a harsh voice. Use Before and After to keep the clarity.</p>',
    faq=[('Is bright always bad?', 'Some clarity is good. Harshness and fatigue are the problem.'),
         ('Why does my voice get harsh on loud words?', 'Often the mic is close and the top end jumps when you project. Move back or lower the input.'),
         ('Should I cut the very top?', 'Only if it is hissy. Harshness is usually in the middle of the top range.')],
    related=['what-is-a-de-esser', 'what-is-an-equalizer', 'how-to-make-a-voice-sound-warmer']
)

add('my-recording-has-a-pop-on-every-p', 'booth-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='My Recording Has a Pop on Every P: How to Stop It',
    desc='A thump on every p and b sound is a plosive. The cause is air hitting the mic. How to stop pops while recording and how to reduce them in a file.',
    h1='My Recording Has a Pop on Every P',
    kw='my recording has a pop on every p',
    lead='A thump on p and b sounds is a plosive: a puff of air hits the microphone. Stop it at the source with a screen and placement, and reduce what is left in the file.',
    tldr=['Pops come from air hitting the capsule when you say p and b.',
          'A pop filter, placed in front of the mic, is the standard fix.',
          'Speaking slightly off-axis moves the air past the mic.',
          'A high-pass filter reduces pops in the file, but the source fix is better.'],
    body='''
<h2>What causes the pop</h2>
<p>A p or a b releases a short puff of air. If the mic is directly in its path, the capsule moves and records a low thump. The thump is mostly low frequency, which is why a low cut helps.</p>
<h2>Stop it while recording</h2>
<p>Place a pop filter a few centimetres in front of the mic and keep the speaker about a hand&rsquo;s width from the filter. Speaking a little to the side helps as well. The <a href="/tunedzy/what-is-a-pop-filter">pop filter explanation</a> covers placement.</p>
<h2>Reduce it in the file</h2>
<p>A high-pass filter around 80 to 120 Hz removes much of the thump. Repeated light passes sound better than one heavy one. The <a href="/tunedzy/blog/remove-mic-pops-plosives">plosive removal guide</a> has the steps.</p>
<h2>Check the voice</h2>
<p>A low cut set too high thins the voice. Check that the words still sound full after the filter.</p>
''',
    vf_title='Stop the pop, then clean',
    vf='<p>Tunedzy&rsquo;s cleanup includes a pop guard and a low cut. Use Before and After to check the voice stays full.</p>',
    faq=[('Is a pop filter enough?', 'For most speech, yes. Some very strong plosives still need a little file cleanup.'),
         ('Why does my phone pop on p?', 'The phone is directly in front of the mouth. Speak slightly to the side.'),
         ('Does a foam cover work?', 'Often, for voice. A mesh screen is more effective for strong plosives.')],
    related=['clean-up-a-phone-voice-recording', 'what-is-a-pop-filter', 'how-to-record-with-a-headset-microphone']
)

add('my-audio-has-clicks-every-few-seconds', 'neon-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='My Audio Has Clicks Every Few Seconds: Causes and Fixes',
    desc='Regular clicks through a recording come from a loose connection, a power or USB issue, a clock fault or the recorder itself. How to find the cause and mend the clicks.',
    h1='My Audio Has Clicks Every Few Seconds',
    kw='my audio has clicks every few seconds',
    lead='Regular clicks through a recording usually point to a fault in the chain, not the voice. Find the cause before you repair the file, because the clicks will come back on the next take.',
    tldr=['Clicks at a regular interval often come from a power, USB or clock issue.',
          'Test by recording silence and moving or unplugging things one at a time.',
          'Single clicks are easy to mend in the file; regular ones point to a fault.',
          'Fix the fault, then mend the remaining clicks.'],
    body='''
<h2>Find the pattern</h2>
<p>Note how often the clicks come. A click every few seconds or at a steady rhythm suggests an electrical or clock fault. Random clicks are more often a cable or a mouse or keyboard nearby.</p>
<h2>Test the chain</h2>
<p>Record silence, then change one thing at a time: unplug a USB device, move the cable, switch the power adapter, close other apps. When the clicks stop, you have found the cause.</p>
<h2>Common causes</h2>
<ul>
<li>A USB hub or port sharing power with other devices.</li>
<li>A sample-rate mismatch between the mic and the computer.</li>
<li>A loose XLR or USB connection.</li>
<li>Background apps that use the audio device.</li>
</ul>
<h2>Mend what remains</h2>
<p>Once the fault is fixed, a few stray clicks in a file can be mended with a click repair. Use the lowest setting that removes them. The <a href="/tunedzy/how-to-fix-a-crackling-recording">crackle guide</a> has the steps.</p>
''',
    vf_title='Mend the clicks after the fault is fixed',
    vf='<p>Tunedzy&rsquo;s Repair finds clicks and mends them in the file. Fix the cause on the next recording.</p>',
    faq=[('Are the clicks in the mic?', 'Usually not. They come from the chain: power, USB, connection or software.'),
         ('Why do clicks appear only sometimes?', 'A background process or a shared power line can cause them at intervals.'),
         ('Can the file be fully fixed?', 'Stray clicks yes. A recording with constant faults needs the fault fixed first.')],
    related=['how-to-fix-a-crackling-recording', 'how-to-record-with-a-usb-microphone', 'clean-up-a-phone-voice-recording']
)

add('my-voice-is-too-loud-on-my-phone', 'mic', ['lufs-meter', 'vocal-checker'],
    title='My Voice Is Too Loud on My Phone: Fixing Peaks and Level',
    desc='A recording that is too loud on a phone is peaking or sits above the target. How to find the peaks, reduce the level safely and check the result on a phone.',
    h1='My Voice Is Too Loud on My Phone',
    kw='my voice is too loud on my phone',
    lead='A recording that is too loud on a phone usually peaks too high or sits above the listening level. Lower it to a target and check the peaks; do not just turn the file down until the peaks are hidden.',
    tldr=['Check whether the peaks reach the top, or whether the average level is high.',
          'Lower the level to a loudness target, not by eye.',
          'Check the true peak after the change.',
          'Listen on a phone speaker, where too-loud recordings are most obvious.'],
    body='''
<h2>Peaks or average?</h2>
<p>A file can be too loud because its peaks clip, or because its average level is high and the voice is pushed. Look at the waveform for flat tops, and measure the loudness of the whole file.</p>
<h2>Lower it to a target</h2>
<p>Set the file to a loudness target for where it will be played, rather than lowering it until it feels right. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> lists the targets people use.</p>
<h2>Check the peaks</h2>
<p>After you lower the level, check the true peak. A file that is quiet on average can still have high peaks, which a phone will play harshly.</p>
<h2>Listen on a phone</h2>
<p>Play the file on the phone you will use. Adjust only once you have heard the result on that device.</p>
''',
    vf_title='Set the level to a target',
    vf='<p>Tunedzy sets a recording to a loudness target and checks the true peak before you export.</p>',
    faq=[('Should I lower the file until it sounds right on my phone?', 'No. Set a target and check the peaks, so it sounds right on other devices too.'),
         ('Why does it sound loud on my phone but not my computer?', 'Phone speakers can exaggerate peaks. Check the true peak as well as the level.'),
         ('Does a limiter fix a loud file?', 'A limiter controls peaks. For an overall level, set the loudness target first.')],
    related=['what-is-true-peak-dbtp', 'how-to-make-audio-louder-without-distortion', 'my-recording-is-too-quiet']
)

add('my-export-is-quieter-than-my-project', 'desk', ['lufs-meter', 'vocal-checker'],
    title='My Export Is Quieter Than My Project: Why It Happens',
    desc='An exported file that sounds quieter than the project it came from usually has a loudness target, a mix gain or a format conversion. How to find the cause and match the level.',
    h1='My Export Is Quieter Than My Project',
    kw='my export is quieter than my project',
    lead='An export that is quieter than the project is usually doing what you asked: a loudness target, a lowered master, or a format change. Check the setting before you raise the file.',
    tldr=['A loudness target lowers loud projects to the target level.',
          'A master fader or a mix gain may be set lower than the project preview.',
          'Some formats are read at a different level by players.',
          'Match the level on purpose, with a loudness target, not by guessing.'],
    body='''
<h2>Check the loudness target</h2>
<p>If you chose a loudness target, the export is set to that level, even if the project was louder. A loud project is turned down to the target.</p>
<h2>Check the master</h2>
<p>The master level in the mix may be lower than the preview. Check that the master fader is where you think it is, and that nothing is muted or ducked unexpectedly.</p>
<h2>Check the format</h2>
<p>A WAV and an MP3 of the same file can sound a little different in level on some players. Measure the export itself, rather than comparing to the project by ear.</p>
<h2>Match it on purpose</h2>
<p>Set a loudness target that suits the destination. Then the export will sound as loud as it should, with the true peak checked. The <a href="/tunedzy/how-to-export-audio-for-spotify-and-apple-podcasts">export guide</a> has the steps.</p>
''',
    vf_title='Export at the level you chose',
    vf='<p>Tunedzy exports at a loudness target with the true peak checked, so the file is at the level you set.</p>',
    faq=[('Will the export be as loud as the project?', 'Not if a loudness target is set below the project level. That is the point.'),
         ('How do I make it louder?', 'Raise the target within the true-peak limit, or raise the level before the target is applied.'),
         ('Does the format change the level?', 'Not normally, but players can differ. Measure the file.')],
    related=['how-to-export-audio-for-spotify-and-apple-podcasts', 'what-is-lufs', 'my-podcast-sounds-different-on-spotify']
)

add('my-mp3-sounds-worse-than-my-wav', 'booth-wide', ['vocal-checker', 'lufs-meter'],
    title='My MP3 Sounds Worse Than My WAV: Why and What to Do',
    desc='An MP3 can sound worse than the WAV it came from, through a low bit rate or repeated conversions. Why it happens and how to export a better MP3 from the master.',
    h1='My MP3 Sounds Worse Than My WAV',
    kw='my mp3 sounds worse than my wav',
    lead='MP3 is a lossy format, so it removes detail. A low bit rate or a conversion from another MP3 makes the loss audible. Export from the WAV master at a high bit rate.',
    tldr=['MP3 removes detail to save space; a low bit rate removes more.',
          'Converting an MP3 to another MP3 adds loss each time.',
          'Export from the WAV master at a high bit rate for speech.',
          'Keep the WAV as the master, and export MP3 only when you need it.'],
    body='''
<h2>Why MP3 loses detail</h2>
<p>MP3 removes sound the ear is supposed to miss, to make the file small. At a high bit rate, most listeners cannot tell it from the original for speech. At a low bit rate, artifacts show on sibilance, breath and room sound.</p>
<h2>Why conversions add up</h2>
<p>Every lossy conversion removes more detail. Converting an MP3 into another MP3 is the worst case. Always export from the lossless master.</p>
<h2>How to export a better MP3</h2>
<ol>
<li>Start from the WAV master, not an earlier MP3.</li>
<li>Choose a high bit rate, the highest your platform accepts.</li>
<li>Check the true peak of the exported file, because conversion can raise it.</li>
</ol>
<h2>When WAV is better</h2>
<p>For editing, for handing to another editor, or for platforms that accept WAV, keep the WAV. The <a href="/tunedzy/how-to-choose-wav-mp3-or-flac">format guide</a> explains the choice.</p>
''',
    vf_title='Export from the master, not a copy',
    vf='<p>Tunedzy keeps the master and exports MP3 from it, so the file is not a copy of a copy.</p>',
    faq=[('Is a high bit rate MP3 as good as WAV?', 'For speech most listeners cannot hear the difference. Check the platform and your ears.'),
         ('Why does my MP3 clip?', 'Conversion can raise the peaks. Check the true peak before you export.'),
         ('Should I upload WAV or MP3?', 'Check the platform. Upload the format it recommends, from your WAV master.')],
    related=['how-to-choose-wav-mp3-or-flac', 'what-is-true-peak-dbtp', 'how-to-export-audio-for-spotify-and-apple-podcasts']
)

add('my-audio-file-is-too-big', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='My Audio File Is Too Big: How to Make It Smaller',
    desc='Reduce an audio file size without losing the voice: the format, the bit rate, mono for speech and trimming the silence, with the trade-offs.',
    h1='My Audio File Is Too Big',
    kw='my audio file is too big',
    lead='A large audio file is usually uncompressed stereo at a high sample rate. For speech, a mono file at a moderate bit rate is much smaller and sounds the same to most listeners.',
    tldr=['Speech in mono is half the size of stereo, with no loss for a single voice.',
          'A compressed format such as MP3 at a sensible bit rate is much smaller than WAV.',
          'Trim the silence at the start and end to save more.',
          'Keep the WAV master, and make the small copy for sharing.'],
    body='''
<h2>Why it is big</h2>
<p>WAV is uncompressed, so a long recording is large. Stereo doubles the size. A high sample rate and bit depth add more. For speech, most of that is not needed for listening.</p>
<h2>Mono for speech</h2>
<p>A single voice does not need two channels. Converting to mono halves the size and keeps the voice the same. Check that a stereo recording is not out of balance before you do.</p>
<h2>Format and bit rate</h2>
<p>MP3 at a sensible bit rate is much smaller than WAV, and good enough for listening. Keep the WAV master and make the small copy only for sharing. The <a href="/tunedzy/how-to-choose-wav-mp3-or-flac">format guide</a> explains the trade-off.</p>
<h2>Trim the silence</h2>
<p>Cut the dead air at the start and end. It adds size without adding anything. The <a href="/tunedzy/how-to-trim-silence-from-a-recording">trimming guide</a> shows how.</p>
''',
    vf_title='Smaller copy, same voice',
    vf='<p>Tunedzy exports a mono or compressed copy from the master, and keeps the full file for editing.</p>',
    faq=[('Will mono sound worse?', 'For a single voice, no. For music with stereo effects, yes.'),
         ('Is MP3 small enough for email?', 'Usually, for a short voice clip. Check the size limit of the service you send it to.'),
         ('Should I delete the WAV?', 'Keep it as the master. Make the small copy from it.')],
    related=['how-to-choose-wav-mp3-or-flac', 'how-to-trim-silence-from-a-recording', 'what-is-bit-depth']
)

add('my-voice-sounds-different-on-a-phone-speaker', 'booth', ['vocal-checker', 'lufs-meter'],
    title='My Voice Sounds Different on a Phone Speaker: What to Check',
    desc='A recording that sounds fine on headphones but thin or boomy on a phone speaker needs a check on the bass, the presence and the level. How to test and adjust.',
    h1='My Voice Sounds Different on a Phone Speaker',
    kw='my voice sounds different on phone speaker',
    lead='A phone speaker is small and cannot reproduce deep bass, so it exaggerates the middle and the peaks. Check your recording on the device your listeners will use, and adjust the low end and the level.',
    tldr=['Phone speakers lose the deep bass and exaggerate the middle range.',
          'A voice that sounds fine on headphones can be thin or harsh on a phone.',
          'Test on a phone speaker before you publish, every time.',
          'Adjust the low cut and the level, not the whole tone.'],
    body='''
<h2>What a phone speaker does</h2>
<p>A phone speaker cannot reproduce the very low frequencies, and it often pushes the middle range forward. A voice that sounds balanced on studio headphones can sound thin or sharp on a phone.</p>
<h2>How to test</h2>
<p>Play the recording on the phone you use most, at a normal listening volume. Listen to the words first, then the tone. If the words are hard to follow, the level or the presence is off.</p>
<h2>What to adjust</h2>
<p>Lower the low cut if the voice sounds thin. Reduce a harsh band if the voice sounds sharp. Check the level, because quiet voices get lost on phones. The <a href="/tunedzy/how-to-make-a-voice-sound-warmer">warmth guide</a> covers the low-mid range.</p>
<h2>Check again</h2>
<p>Make one change at a time, and test on the phone each time. Stop when the voice is clear on the phone and still sounds right on headphones.</p>
''',
    vf_title='Test on the phone before you post',
    vf='<p>Tunedzy Go lets you hear a cleaned recording on your phone, for free. Use it to check before you publish.</p>',
    faq=[('Should I master for a phone speaker?', 'Check that the voice works on a phone, but do not make the whole track sound like a phone.'),
         ('Why does my voice disappear on a phone?', 'Usually the level is too low or the presence is missing. Check the level first.'),
         ('Is headphone testing wrong?', 'No. Test on both, and make sure the balance works on each.')],
    related=['my-audio-sounds-tinny', 'my-voice-sounds-too-bright', 'tunedzy-go-faq']
)
