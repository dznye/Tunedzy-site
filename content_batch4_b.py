"""Batch 4b (25 October 2026): seven how-to guides and four problem-fix pages. Same shape as content.GUIDES.

GROUP_OF tells the hub which section each page belongs to ('how' or 'problem').
"""

PHOTO = {}
TOOLS = {}
GUIDES = {}
ORDER = []
GROUP_OF = {}


def add(slug, group, photo, tools, **g):
    GUIDES[slug] = g
    PHOTO[slug] = photo
    TOOLS[slug] = tools
    ORDER.append(slug)
    GROUP_OF[slug] = group


add('how-to-clean-up-a-voice-recording-in-audacity', 'how', 'mic', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Clean Up a Voice Recording in Audacity (Free)',
    desc='A free, step-by-step Audacity method for cleaning a voice recording: a noise profile, a gentle reduction, a click check and a loudness check.',
    h1='How to Clean Up a Voice Recording in Audacity',
    kw='clean up voice recording in audacity',
    lead='Audacity is free and does a good job on steady noise when you use it carefully. The method is the same for any recording: a profile, a gentle reduction, then checks.',
    tldr=['Select a second or two of room tone and take a noise profile from it.',
          'Apply noise reduction to the whole recording with a moderate setting.',
          'Use the click removal tool only on the clicks you can hear.',
          'Compare with the original and keep the file you like.'],
    body='''
<h2>Before you start</h2>
<p>Save the original file under another name. Audacity edits in place, so keep a copy you can go back to. Set the project to the sample rate of the recording to avoid resampling.</p>
<h2>Step 1: take a noise profile</h2>
<p>Find a part of the recording where nobody is speaking, about one or two seconds long. Select it, then open the noise reduction effect and choose to get the noise profile. This tells the effect what the room sounds like.</p>
<h2>Step 2: apply a gentle reduction</h2>
<p>Select the whole recording, open noise reduction again, and use moderate settings. Start with a reduction around 12 dB and listen. If the voice sounds watery or thin, lower it. The <a href="/tunedzy/blog/why-noise-reduction-makes-voice-sound-watery">watery sound guide</a> explains the cause.</p>
<h2>Step 3: check for clicks</h2>
<p>Listen for clicks, mouth pops and crackle. Use the click removal effect with its default settings on a short selection, and listen again. Over-using it leaves dull patches.</p>
<h2>Step 4: check the level</h2>
<p>Use the amplify effect or normalise to bring the loudest peaks to a safe level, and check the loudness with the <a href="/tunedzy/tools/lufs-meter">free LUFS meter</a>.</p>
<h2>Where Tunedzy fits</h2>
<p>Audacity is a manual method, so the steps take time and your ear decides each setting. Tunedzy runs the same kinds of steps automatically and reports what it changed. Many people use Audacity for a precise fix and Tunedzy for the standard cleanup.</p>
''',
    vf_title='Automatic, if you do not want the steps',
    vf='<p>Tunedzy runs the cleanup, the repair and the loudness check in one pass on your PC. Use Before and After to compare.</p>',
    faq=[('Is Audacity free?', 'Yes. It is free and open source, for Windows, macOS and Linux.'),
         ('Why does Audacity sound robotic after noise reduction?', 'The reduction was too strong. Lower it and use a shorter noise profile from quieter room tone.'),
         ('Can Audacity remove echo?', 'Not directly. Reducing echo in Audacity is a workaround, and the results are limited.')],
    related=['tunedzy-vs-audacity', 'remove-background-noise-from-a-voice-recording', 'how-to-trim-silence-from-a-recording'])

add('how-to-trim-silence-from-a-recording', 'how', 'desk', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Trim Silence From a Recording',
    desc='Cut the dead air at the start, end and between phrases of a recording, without making the speech sound rushed or chopped.',
    h1='How to Trim Silence From a Recording',
    kw='trim silence from recording',
    lead='Dead air at the start and end of a recording is easy to cut. Silence between phrases needs more care, because cutting all of it makes speech sound rushed.',
    tldr=['Cut the start and end first; it is always safe.',
          'Shorten long gaps between sentences rather than removing them all.',
          'Keep a little room tone, so the cuts do not sound like a switch.',
          'Listen to each cut at normal volume.'],
    body='''
<h2>Start and end</h2>
<p>Remove the silence before the first word and after the last one. Leave about a quarter of a second of room tone so the start is not abrupt. This is the safest cut in any recording.</p>
<h2>Gaps between phrases</h2>
<p>A pause tells the listener that a thought has finished. Cut the gaps that are clearly too long, perhaps over a second, down to a shorter pause. Keep the natural ones. A speaker who never pauses sounds breathless and hard to follow.</p>
<h2>Keep room tone</h2>
<p>When you join two pieces, the room sound can change, and the join becomes audible. A short crossfade or a little room tone at each join keeps the sound steady. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone guide</a> explains why it matters.</p>
<h2>Check each cut</h2>
<p>Play each cut at normal volume and listen for a click, a jump in the room sound or a clipped word. If a cut sounds wrong, undo it and try a different point.</p>
<h2>Tunedzy</h2>
<p>In Tunedzy you can shorten pauses in the transcript with one action, leaving a short pause in place. The <a href="/tunedzy/edit-a-podcast-by-its-words">edit-by-words guide</a> shows the steps.</p>
''',
    vf_title='Shorten the pauses, keep the rhythm',
    vf='<p>Tunedzy shortens long pauses in the transcript and leaves a natural gap, so the speech keeps its rhythm.</p>',
    faq=[('How long should a pause be?', 'It depends on the speech. Keep the pauses that let a thought land, and shorten the ones that drag.'),
         ('Will cutting silence make a recording sound fake?', 'Not if you keep some room tone at each cut and leave natural pauses.'),
         ('Should I trim before or after cleaning?', 'Clean first, then trim. Trimming first can leave the noise changing at each cut.')],
    related=['edit-a-podcast-by-its-words', 'how-to-clean-up-a-voice-recording-in-audacity', 'how-to-clean-up-an-interview-recording'])

add('how-to-record-with-a-usb-microphone', 'how', 'mic-wide', ['clean-streaming-mic', 'vocal-checker'],
    title='How to Record With a USB Microphone',
    desc='Get the best from a USB microphone: placement, gain, the room, the cable and monitoring, with the steps in order.',
    h1='How to Record With a USB Microphone',
    kw='how to record with a usb microphone',
    lead='A USB microphone plugs straight into a computer and records well when it is placed and set up correctly. Most of the gain is in the setup, not the price.',
    tldr=['Place the mic about a hand&rsquo;s width from the mouth, slightly off-axis.',
          'Set the gain so the loudest words sit well below full scale.',
          'Use headphones to hear what you record, and check for latency.',
          'Keep the cable away from power cables, to avoid hum.'],
    body='''
<h2>Position</h2>
<p>Put the mic on a stand or arm at the height of your mouth. Speak slightly across the front rather than straight into it, which cuts pops. Keep the distance steady.</p>
<h2>Gain</h2>
<p>Set the gain in the software or on the mic so the loudest words peak around the middle of the meter. If the level only reaches the bottom of the meter, the recording will be noisy when you raise it later. Record a test and listen back.</p>
<h2>Monitoring</h2>
<p>Use headphones, not speakers, so the mic does not pick up the sound from your speakers. Some USB mics have a direct monitor; turn it on to hear your voice without delay.</p>
<h2>Cable and power</h2>
<p>Keep the USB cable away from power cables and chargers. Hum is often a cable running beside a power lead. A short, good-quality cable helps.</p>
<h2>Room</h2>
<p>A USB mic picks up the room as much as any mic. A soft space with rugs and curtains makes the biggest difference. For a quiet corner on a budget, see <a href="/tunedzy/how-to-set-up-a-quiet-recording-corner-on-a-budget">the quiet corner guide</a>.</p>
''',
    vf_title='Clean the USB take',
    vf='<p>Tunedzy cleans a USB mic recording in one pass on your PC. Compare Before and After.</p>',
    faq=[('Do I need an audio interface?', 'Not for a single USB mic. An interface is useful for several mics or for more control of gain.'),
         ('Why is my USB mic so quiet?', 'The gain is low, or the mic is far away. Move closer and raise the gain until the loudest words are well below full scale.'),
         ('Can a USB mic record with other people?', 'Yes, but each person needs their own mic or a separate recording to stay balanced.')],
    related=['how-to-choose-a-microphone-for-voice-recording', 'how-to-set-up-a-quiet-recording-corner-on-a-budget', 'clean-up-a-phone-voice-recording'])

add('how-to-choose-a-microphone-for-voice-recording', 'how', 'mic', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='How to Choose a Microphone for Voice Recording',
    desc='What to look for in a microphone for voice: dynamic or condenser, USB or XLR, polar pattern and the room, with honest trade-offs.',
    h1='How to Choose a Microphone for Voice Recording',
    kw='how to choose a microphone for voice recording',
    lead='The right microphone depends on the room, the voice and how you plan to record. A close mic in a soft room beats an expensive mic in a hard room.',
    tldr=['Dynamic mics reject room sound well and suit loud or untreated rooms.',
          'Condenser mics are more sensitive and suit quiet, treated rooms.',
          'USB mics are simplest; XLR mics need an interface but offer more control.',
          'A cardioid pattern picks up the voice in front and rejects some sound from behind.'],
    body='''
<h2>Dynamic or condenser</h2>
<p>A dynamic mic is sturdy and less sensitive to the room, which makes it a good choice in an untreated space. A condenser mic is more detailed and sensitive, and needs a quiet room, because it also picks up more of the room.</p>
<h2>USB or XLR</h2>
<p>USB mics plug straight into a computer and are the simplest to start with. XLR mics need an audio interface, which gives more control of gain and often better sound, at more cost and complexity.</p>
<h2>Pattern</h2>
<p>A cardioid pattern picks up mainly from the front, which helps in a room with noise behind you. Omnidirectional mics pick up from all sides and suit a group in one place.</p>
<h2>The room comes first</h2>
<p>Any mic records its room. Before you buy, improve the room: rugs, curtains and a closet of clothes often make more difference than moving up in price.</p>
<h2>What to choose</h2>
<p>For a single voice at a desk, a cardioid USB mic in a soft room is a good start. For a shared space or a mixed room, a dynamic mic is safer. Test the mic in your room before you commit, if the shop allows it.</p>
''',
    vf_title='Clean the recording from any mic',
    vf='<p>Tunedzy cleans a recording from any mic, so you can start with the setup you have and improve it later.</p>',
    faq=[('Is an expensive mic always better?', 'No. The room and the distance matter more for most voice recordings.'),
         ('Do I need a pop filter?', 'For speech close to the mic, a pop filter or foam cover helps a lot with breath pops.'),
         ('Can I use a phone instead?', 'Yes. A phone close to the mouth in a soft room is a sensible start, and cleanup can help.')],
    related=['how-to-record-with-a-usb-microphone', 'what-is-a-condenser-vs-dynamic-microphone', 'how-to-set-up-a-quiet-recording-corner-on-a-budget'])

add('how-to-set-up-a-quiet-recording-corner-on-a-budget', 'how', 'booth-wide', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Set Up a Quiet Recording Corner on a Budget',
    desc='Make a usable voice recording corner from things you already have: where to sit, what to soften, and how to check the room before you record.',
    h1='How to Set Up a Quiet Recording Corner on a Budget',
    kw='quiet recording corner on a budget',
    lead='You do not need a studio. A corner with soft surfaces and no noise sources is enough for most voice work, and it costs little or nothing.',
    tldr=['Pick a corner away from the window, the fridge and the air conditioning.',
          'Soften the wall behind you with fabric, rugs or a row of clothes.',
          'Check the room tone with the mic on: close your eyes and listen.',
          'Record in the same corner every time, so the sound stays consistent.'],
    body='''
<h2>Choose the corner</h2>
<p>Pick a spot away from windows, the fridge, the washing machine and any corridor with traffic. A corner of a room with two walls behind you is quieter than a space in the middle of a room with hard floors.</p>
<h2>Soften the surfaces</h2>
<p>Hang a blanket or curtain on the wall behind and to the side of the mic. A rug under the desk and cushions on hard surfaces cut reflections. A closet of clothes is still the cheapest good booth: fabric absorbs the echo that makes a voice sound thin.</p>
<h2>Check the room</h2>
<p>Turn the mic on, close your eyes and listen to the room with nobody talking. Hear the fan, the hum from a light, the traffic outside? Switch each source off until the room is quiet. This room tone is also what a noise cleaner learns from.</p>
<h2>Keep it the same</h2>
<p>Record in the same spot, with the same distance and the same mic position. Consistency is what makes the recordings match.</p>
<h2>What not to buy first</h2>
<p>Acoustic panels and foam can help, but a soft room and a quiet space do more for less money. Start with the room, then decide whether you need anything else.</p>
''',
    vf_title='Clean the recording from your corner',
    vf='<p>Tunedzy cleans what your corner records. Start with the room, then use the cleanup for what is left.</p>',
    faq=[('Do I need foam panels?', 'Not to start. Soft fabric and a quiet space do much of the work. Panels can help later.'),
         ('How do I know the room is quiet enough?', 'Record ten seconds of silence and listen on headphones. If you hear a fan, a hum or traffic, switch it off.'),
         ('Can I use a wardrobe?', 'Yes. A closet full of clothes is a classic, practical booth for voice.')],
    related=['how-to-record-with-a-usb-microphone', 'clean-up-a-phone-voice-recording', 'remove-background-noise-from-a-voice-recording'])

add('how-to-choose-wav-mp3-or-flac', 'how', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='How to Choose WAV, MP3 or FLAC for Your Audio',
    desc='WAV, FLAC and MP3 explained for creators: which to keep as a master, which to upload, and why conversions lose quality.',
    h1='How to Choose WAV, MP3 or FLAC',
    kw='wav vs mp3 vs flac',
    lead='Keep a lossless master for editing and re-exporting, and make an MP3 only for sharing. Each conversion from a lossy file loses a little quality, so do not work from an MP3.',
    tldr=['WAV is uncompressed and the usual editing master.',
          'FLAC is lossless and compressed, so it is smaller than WAV with the same quality.',
          'MP3 is lossy: it is small and widely supported, but it loses detail.',
          'Export MP3 from the master, never from another MP3.'],
    body='''
<h2>WAV</h2>
<p>WAV is uncompressed audio. It is large, but every application reads it, and it is the common format for an editing master. Keep one for each project.</p>
<h2>FLAC</h2>
<p>FLAC is lossless: it compresses the file without losing any sound, so it is smaller than WAV. Many players and some hosts accept it, but not all, so check the platform before you upload.</p>
<h2>MP3</h2>
<p>MP3 is lossy. It removes detail the ear is supposed to miss, which saves space. It is widely accepted for uploads and sharing. A high bit rate sounds good for speech; a low one shows its flaws quickly.</p>
<h2>The rule</h2>
<p>Keep the master in WAV or FLAC. Export MP3 from the master when you share the file. If you need another format later, export it from the master again. Repeated lossy conversions add up.</p>
<h2>Check the final file</h2>
<p>The <a href="/tunedzy/how-to-export-audio-for-spotify-and-apple-podcasts">export guide</a> covers what to check on the final file, including the true peak after conversion.</p>
''',
    vf_title='Keep the master, export the rest',
    vf='<p>Tunedzy keeps the master and exports WAV, FLAC or MP3 from it, so you never work from a lossy copy.</p>',
    faq=[('Is FLAC better than WAV?', 'They are equal in quality. FLAC is smaller; WAV is more widely read by editing software.'),
         ('Does MP3 always sound worse?', 'At a high bit rate, speech is hard to tell apart. Repeated conversions are the real problem.'),
         ('Which format do podcast hosts want?', 'Many accept MP3 and WAV. Check your host before you upload.')],
    related=['how-to-export-audio-for-spotify-and-apple-podcasts', 'what-is-bit-depth', 'what-is-sample-rate'])

add('my-recording-is-too-quiet', 'problem', 'mic', ['lufs-meter', 'vocal-checker'],
    title='My Recording Is Too Quiet: What to Do',
    desc='A recording that is too quiet is usually a gain or distance problem. How to tell, how to raise the level safely and when it has to be re-recorded.',
    h1='My Recording Is Too Quiet',
    kw='my recording is too quiet',
    lead='A quiet recording can often be raised, but only up to the point where the noise rises with it. Find out why it is quiet before you turn it up.',
    tldr=['Check whether the input gain was low or the mic was far away.',
          'Raise the level in one step, to a safe peak.',
          'If the noise rises with the voice, re-record closer to the mic.',
          'Check the loudness and the true peak after you raise it.'],
    body='''
<h2>Find the cause</h2>
<p>Quiet recordings have two usual causes: the gain was set low, or the mic was far from the mouth. A low gain means the voice is weak but the noise is also weak, so raising it works. A far mic means the room is louder than the voice, so raising it brings up the room too.</p>
<h2>Raise it safely</h2>
<p>Measure the peaks, then raise the level in one step so the loudest words stay below full scale. The <a href="/tunedzy/how-to-make-audio-louder-without-distortion">louder without distortion guide</a> has the steps.</p>
<h2>When to re-record</h2>
<p>If the noise rises as much as the voice, cleanup cannot separate them well. Re-record closer to the mic, with the gain set properly. A short re-take is quicker than heavy repair.</p>
<h2>Check the result</h2>
<p>Listen on headphones and on a phone speaker. Check the loudness against the platform you publish on.</p>
''',
    vf_title='Raise it to a target, check the peak',
    vf='<p>Tunedzy sets a recording to a loudness target and checks the true peak, so a quiet take comes up safely.</p>',
    faq=[('Can I just turn up the volume?', 'Only as far as the peaks allow. Turning it up past that point adds distortion.'),
         ('Why is my phone recording quiet?', 'The phone is far from the mouth, or the input is low. Move closer and check the level before you record.'),
         ('Will raising the level add noise?', 'It raises the noise too. Clean the recording after you raise it, or re-record closer.')],
    related=['how-to-make-audio-louder-without-distortion', 'why-does-my-phone-recording-sound-far-away', 'loudness-for-youtube-podcasts-and-spotify'])

add('my-voice-sounds-robotic-after-cleanup', 'problem', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='My Voice Sounds Robotic After Cleanup: How to Fix It',
    desc='Why a cleaned voice sounds robotic or watery, which setting causes it, and how to get the cleanup back to natural without losing the noise removal.',
    h1='My Voice Sounds Robotic After Cleanup',
    kw='voice sounds robotic after cleanup',
    lead='Robotic or watery speech almost always means the cleanup was too strong. The fix is to lower the strength, not to stop cleaning.',
    tldr=['The cause is usually too much noise reduction or too high a gate.',
          'Go back to the original and clean again with a lower setting.',
          'Keep a little of the room sound; a natural room is better than a dead one.',
          'Compare the result with the original, not only with your memory of it.'],
    body='''
<h2>What causes it</h2>
<p>Noise reduction works by lowering sound it thinks is noise. If it lowers too much, or the same frequencies in the voice are also lowered, the voice loses its natural texture. The result sounds metallic or underwater. A gate set too high does the same by cutting the ends of words.</p>
<h2>How to fix it</h2>
<ol>
<li>Go back to the original recording, not the cleaned copy.</li>
<li>Lower the reduction and the gate. Use less than you did.</li>
<li>Listen to a whole sentence, not one word.</li>
<li>Keep the room sound a little; a dead room sounds unnatural.</li>
</ol>
<h2>What a good result sounds like</h2>
<p>The background is quieter, and the voice still sounds like the person. A little room sound is normal. The <a href="/tunedzy/blog/why-noise-reduction-makes-voice-sound-watery">watery sound guide</a> explains the causes in more detail.</p>
<h2>Tunedzy</h2>
<p>Use Before and After to compare the cleaned voice with the original. If the cleanup sounds unnatural, lower the amount in Perfect it.</p>
''',
    vf_title='Clean it back to natural',
    vf='<p>Tunedzy lets you lower the cleanup and compare Before and After, so the voice stays natural.</p>',
    faq=[('Is some room sound good?', 'Yes. A completely dead voice sounds unnatural. Keep a little of the room.'),
         ('Why does my cleaned voice have a lisp?', 'Usually a noise reduction or a de-esser set too high. Lower it and listen again.'),
         ('Can an AI cleaner sound robotic?', 'Yes, if it is pushed too hard. Use the lowest setting that works.')],
    related=['remove-background-noise-from-a-voice-recording', 'what-is-a-noise-gate', 'clean-up-a-phone-voice-recording'])

add('why-does-my-phone-recording-sound-far-away', 'problem', 'neon', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='Why Does My Phone Recording Sound Far Away?',
    desc='The causes of a distant, echoey phone recording (distance, room, the wrong mic and phone settings) and what to change to bring the voice forward.',
    h1='Why Does My Phone Recording Sound Far Away?',
    kw='why does my phone recording sound far away',
    lead='A phone recording sounds far away when the room is louder than the voice. Bring the phone closer and make the room softer, and the voice comes forward.',
    tldr=['The phone is too far from the mouth, so the room is louder than the voice.',
          'A hard room reflects sound and makes the voice sound distant.',
          'Some phones use a rear or top mic for video, which is further away.',
          'Move closer and soften the room before you touch the editing.'],
    body='''
<h2>Distance</h2>
<p>The biggest cause is distance. A phone at arm&rsquo;s length picks up the room. Bring it to about 15 to 20 cm from your mouth, a little to the side.</p>
<h2>Room</h2>
<p>A hard room reflects sound. The reflections arrive later than the direct voice and make it sound distant and hollow. Soft furnishings, rugs and curtains cut them.</p>
<h2>Which mic</h2>
<p>Some phones record video with a mic that is not near the mouth, especially in video mode. Use the audio recorder app, or hold the phone so the mic facing the speaker is nearest to you.</p>
<h2>Settings and cleanup</h2>
<p>Turn off any noise or wind filter that cuts the voice, and check the level before you record. Cleanup can reduce the room sound, but it cannot bring a voice forward that was never close to the mic.</p>
<h2>What to do now</h2>
<p>Record a short test at the new distance, then clean it with the <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup steps</a>.</p>
''',
    vf_title='Clean the close take',
    vf='<p>Tunedzy Go cleans a phone recording on your phone for free. Record closer and clean it there.</p>',
    faq=[('Will a better phone fix this?', 'It helps less than distance and the room. Move closer first.'),
         ('Is it the phone or the room?', 'Usually both. Record the same words at two distances and listen to the difference.'),
         ('Can I fix a far recording in the file?', 'Partly. A cleanup can reduce the room, but a close take is always better.')],
    related=['clean-up-a-phone-voice-recording', 'how-to-reduce-people-talking-in-the-background', 'fix-a-muffled-voice-recording'])

add('my-podcast-sounds-different-on-spotify', 'problem', 'desk', ['lufs-meter', 'vocal-checker'],
    title='My Podcast Sounds Different on Spotify: Why It Happens',
    desc='Why an episode sounds louder, quieter or thinner on Spotify than in your editor: loudness normalisation, re-encoding and the peak after conversion.',
    h1='My Podcast Sounds Different on Spotify',
    kw='podcast sounds different on spotify',
    lead='Streaming services turn playback level and re-encode the file. An episode can sound different on the platform even though the file is the same.',
    tldr=['Spotify and other platforms normalise loudness, so the level is turned up or down.',
          'The file is re-encoded for streaming, which can raise the peaks.',
          'Check the true peak of the uploaded file, not only the project.',
          'Compare the platform result with your own export on the same device.'],
    body='''
<h2>Normalisation</h2>
<p>Many streaming services adjust the playback level so tracks and episodes sound about equally loud. A file much louder than the target is turned down, and a quiet one may be turned up. This can make a loud episode sound quieter, and the other way round.</p>
<h2>Re-encoding</h2>
<p>The platform converts your file to its own streaming format. The conversion can add peaks above the level in your master. A file that sounded clean in the editor can sound harsher after conversion.</p>
<h2>What to check</h2>
<ul>
<li>The loudness of the exported file, not the project.</li>
<li>The true peak, kept at or below -1 dBTP.</li>
<li>The same episode on a phone and on a computer, after it is published.</li>
</ul>
<h2>What to do</h2>
<p>Re-export the file at a loudness target with the true peak checked, and upload that. The <a href="/tunedzy/how-to-export-audio-for-spotify-and-apple-podcasts">export guide</a> covers the steps, and the <a href="/tunedzy/what-is-true-peak-dbtp">true peak explanation</a> covers the reason.</p>
''',
    vf_title='Export the file the platform expects',
    vf='<p>Tunedzy exports at a loudness target with the true peak checked, and keeps the master for re-exports.</p>',
    faq=[('Is Spotify changing my audio quality?', 'The platform re-encodes the file for streaming. Keeping a clean master and a safe peak helps the result.'),
         ('Why is my episode quieter than others?', 'Usually the episode was set to a lower loudness. Measure it and set it to your target.'),
         ('Do I need to match another podcast?', 'Not exactly. Aim for a steady, comfortable level and a safe peak.')],
    related=['how-to-export-audio-for-spotify-and-apple-podcasts', 'what-is-true-peak-dbtp', 'loudness-for-youtube-podcasts-and-spotify'])
