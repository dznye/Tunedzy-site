"""How-to guides, batch 1 (25 October 2026). Same shape as content.GUIDES: merged in content.py.

Rules for these pages: answer the question first, give steps that work without Tunedzy, say where Tunedzy helps and where it cannot,
never invent results or numbers. Links go to tools, comparisons and the phone app so every guide leads somewhere useful.
"""

PHOTO = {}
TOOLS = {}
GUIDES = {}
ORDER = []


def add(slug, photo, tools, **g):
    GUIDES[slug] = g
    PHOTO[slug] = photo
    TOOLS[slug] = tools
    ORDER.append(slug)


add('clean-up-a-phone-voice-recording', 'hero', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Clean Up a Phone Voice Recording (Steps That Work)',
    desc='Clean up a voice recording made on your phone: a better room, a noise cleaner, a level check and a copy you keep. Free steps, and what Tunedzy adds.',
    h1='How to Clean Up a Phone Voice Recording',
    kw='clean up phone voice recording',
    lead='A phone picks up a lot of room noise and echo, but most of it can be cut back in a few steps. Record better first, then clean, then check the result by ear.',
    tldr=['Record in the quietest small room you can find, with soft things around you (a wardrobe full of clothes is a good booth).',
          'Hold the phone about 15 to 20 cm (6 to 8 inches) from your mouth, a little to the side, to avoid pops.',
          'Clean with a noise tool, then listen to the result, not only to the number on screen.',
          'Level the voice to a target loudness and save a copy. Keep the original.'],
    body='''
<h2>Step 1: Record it well, because cleaning cannot add what was never captured</h2>
<p>Most of the damage to a phone recording happens before any editing. Choose a small room with soft surfaces: a bedroom with a bed and curtains is better than a kitchen with tiles. Turn off fans, air conditioners and the fridge if you can, and close the windows on a busy street. Put the phone flat on a cushion or hold it steady, away from walls. If you can, record a few seconds of the room with nobody speaking: that quiet is what a noise cleaner needs to learn from.</p>
<h2>Step 2: Keep the original file</h2>
<p>Save the untouched recording somewhere else before you start. Every cleaning step should write a new file. If a result sounds wrong, you can start again from the original instead of cleaning a damaged copy.</p>
<h2>Step 3: Remove the noise</h2>
<p>There are three kinds of noise to deal with. Steady hiss and fan noise can be reduced with a noise profile or an AI noise tool. Clicks and pops from your mouth or a bump on the desk need a click repair. Room echo is the hardest and is only partly fixable. For a single pass, <a href="/tunedzy/tools/voice-recorder-noise-cancellation">the free voice recorder cleaner</a> runs in your browser and nothing is uploaded.</p>
<p>In <a href="https://fuidzy.com/tunedzy">Tunedzy</a>, the Perfect it button does the whole pass on your PC: it repairs clipping, clicks and hum first, then runs studio sound (an AI speech model that runs on your computer), then levels and tones the voice. On your phone, <a href="/tunedzy/go/">Tunedzy Go</a> cleans a recording you make or pick with studio sound, on the device.</p>
<h2>Step 4: Check it by ear</h2>
<p>Listen on the phone speaker and on headphones. Look for a watery or "underwater" sound: that means the cleaning was too strong. Words that sound cut off mean the gate or the noise reduction took too much. If you are unsure, use the Before and After switch and pick the version that is easier to listen to for a minute.</p>
<h2>Step 5: Level it and export</h2>
<p>Most phone recordings are too quiet or too loud in places. Set a target loudness for where the voice will go: about -16 LUFS for podcasts, about -14 LUFS for online video (see <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">the loudness guide</a>). Export WAV for editing and MP3 for sharing.</p>
<h2>What no tool can do</h2>
<p>A voice buried in a loud echo, a recording clipped hard into distortion, or a mouth that was far from the mic will improve a lot but will not sound like a studio take. Re-recording closer to the mic in a quieter room is always the better fix.</p>
''',
    vf_title='Clean it in one pass',
    vf='<p>Perfect it in Tunedzy runs the repair, the studio sound and the level in one go, on your own computer. On your phone, Tunedzy Go does it for free with nothing uploaded.</p>',
    faq=[('Can I clean a phone recording for free?', 'Yes. Tunedzy Go and the free voice cleaner on this site do not charge for a basic pass. The Windows app counts use with credits, and your first month includes free credits.'),
         ('Why does my cleaned recording sound watery?', 'The noise reduction was too strong. Run it again with less reduction, or re-record in a quieter room. A gentler setting with a better recording almost always sounds more natural.'),
         ('Should I clean before or after editing?', 'Clean first, on the whole recording, then edit. Cutting first can leave the noise changing from one cut to the next.')],
    related=['ai-vocal-cleanup-explained', 'fix-vocals-recorded-on-phone', 'remove-background-noise-from-a-voice-recording'])

add('remove-background-noise-from-a-voice-recording', 'mic', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Remove Background Noise From a Voice Recording',
    desc='Remove fan, hiss, traffic and room noise from a voice recording. Manual steps with free tools, when AI helps, and where noise removal reaches its limit.',
    h1='How to Remove Background Noise From a Voice Recording',
    kw='remove background noise from voice recording',
    lead='Background noise is easiest to remove when it is steady, like a fan or hiss, and hardest when it moves with the voice, like a TV or another person in the room.',
    tldr=['Steady noise (fan, air conditioner, hiss) is the easiest: use a noise profile or an AI cleaner.',
          'Noise that comes and goes needs a gate, or a cut between sentences.',
          'Noise under the voice cannot be fully removed; reduce it, do not chase it to zero.',
          'Always compare against the original.'],
    body='''
<h2>First, identify the noise</h2>
<p>Listen to the recording with the voice paused. A hum or hiss that stays the same all the way through is steady noise. A sound that starts and stops (a car, a dog, a keyboard) is intermittent. A sound that changes with your words (an echo, another person speaking) is the hardest kind. Your strategy depends on which one you have.</p>
<h2>Method 1: a noise profile (free, in any editor)</h2>
<p>In Audacity, select a second or two of the room with nobody talking, choose the noise reduction effect and take a noise profile from that selection. Then select the whole recording and apply the effect with moderate settings, about 12 dB of reduction to start. Listen. If the voice sounds thin, lower the reduction. Audacity's own manual explains each setting.</p>
<h2>Method 2: an AI cleaner</h2>
<p>AI speech models separate the voice from the room better than a noise profile when the noise is not steady. The free voice cleaner on this site works in your browser, and Tunedzy runs a studio sound model (DeepFilterNet 3) on your own PC or phone. In Tunedzy, the noise removal sits inside Perfect it. Use a moderate setting first.</p>
<h2>Method 3: a gate between sentences</h2>
<p>A noise gate silences the recording when the voice stops. It removes noise between words but not under them. Set the threshold just above the room noise, with a short attack and a longer release, so the ends of words are not clipped.</p>
<h2>Where it stops</h2>
<p>Noise that sits under the voice (a TV in the next room, a fan right beside you) can be reduced, but not removed without changing the voice. If the cleaned version sounds worse than the noisy one, the cleaning was too strong: use less, or record again away from the noise.</p>
''',
    vf_title='Reduce it without ruining the voice',
    vf='<p>Tunedzy&rsquo;s noise removal is part of Perfect it, which also repairs clipping and hum first. Use Before and After to choose the amount you like.</p>',
    faq=[('What is the best free noise remover?', 'For a steady hiss, Audacity with a noise profile is free and works well. For mixed or moving noise, an AI cleaner is more accurate. Test both on your own file.'),
         ('Does noise removal make voices sound robotic?', 'Too much does. Keep the reduction moderate and compare with the original. A little residual room sound is more natural than a voice with no room at all.'),
         ('Can I remove a TV in the background?', 'Only partly. Speech on a TV is hard for any tool to separate from your voice. Turning the TV off or moving to another room is the reliable fix.')],
    related=['clean-up-a-phone-voice-recording', 'ai-vocal-cleanup-explained', 'remove-echo-from-vocal-recording'])

add('fix-a-muffled-voice-recording', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Fix a Muffled Voice Recording',
    desc='Why a voice recording sounds muffled (distance, a case over the mic, too much processing) and how to brighten it without making it harsh.',
    h1='How to Fix a Muffled Voice Recording',
    kw='fix muffled voice recording',
    lead='A muffled recording has lost its high frequencies: the crisp consonants that make speech clear. Some can be brought back with tone shaping, but not all of them.',
    tldr=['First check the cause: distance, a phone case or hand over the mic, or a filter that is too strong.',
          'A little presence boost around 2 to 5 kHz makes speech clearer; too much sounds harsh.',
          'A high-pass filter around 80 to 100 Hz clears rumble without thinning the voice.',
          'Lost high frequencies cannot be recreated; re-record if the voice is far from the mic.'],
    body='''
<h2>Find the cause first</h2>
<p>Three causes account for most muffled recordings. The mic was far away, so the room sound was louder than the voice and the top end was lost in it. The mic was covered (a case, a hand, a pop filter fitted the wrong way round). Or the recording was processed with a noise filter that cut too high. Check your settings and the position of the phone before you fix anything in the file.</p>
<h2>Fix it in the file</h2>
<p>Use an equaliser, not a gain change. Start with a high-pass filter at about 80 to 100 Hz to remove rumble. Then add a gentle boost of 2 to 4 dB around 3 kHz for presence, and a little air above 8 kHz if the voice still sounds dull. Listen at normal volume after every change: a boost that sounds bright at low volume often sounds harsh when louder.</p>
<h2>Do not over-boost sibilance</h2>
<p>Boosting the top end also raises harsh "s" and "t" sounds. If the voice now hisses, use a de-esser on the sibilant range (roughly 5 to 9 kHz) before you boost further.</p>
<h2>Tunedzy and the muffled voice</h2>
<p>Tunedzy's tone step in Perfect it adds presence and removes rumble for a voice, and it measures the tone of a recording against what usually sounds clear. It cannot restore frequencies the microphone never captured. If the recording is very dull, the honest fix is a second take from closer to the mic.</p>
''',
    vf_title='Brighten a voice, not the hiss',
    vf='<p>Tunedzy checks the tone of a voice and shapes it in Perfect it. Use the Before and After switch to stop before the voice turns harsh.</p>',
    faq=[('Can EQ fix a muffled recording completely?', 'No. EQ can make a muffled voice clearer, but high frequencies that were never recorded stay missing. A closer, cleaner recording is the real fix.'),
         ('What frequency makes a voice clearer?', 'Presence, roughly 2 to 5 kHz, is where speech becomes intelligible. Clarity and air sit above that. Start small and adjust by ear.'),
         ('Why does my voice sound thin after EQ?', 'Usually a low cut set too high, or too much reduction below 200 Hz. Bring the low cut down to about 80 Hz and check again.')],
    related=['clean-up-a-phone-voice-recording', 'fix-vocals-recorded-on-phone', 'remove-echo-from-vocal-recording'])

add('remove-hum-from-audio', 'desk', ['vocal-checker', 'lufs-meter'],
    title='How to Remove Hum From Audio (50 Hz and 60 Hz)',
    desc='Find and remove mains hum from a recording: how to tell it apart from other noise, how a notch filter works and when not to use one.',
    h1='How to Remove Hum From Audio',
    kw='remove hum from audio',
    lead='Mains hum is a steady tone at 50 Hz (most of the world) or 60 Hz (North America and parts of Asia), with its harmonics. It usually comes from a cable, a power supply or a lamp dimmer near the mic.',
    tldr=['Look at the spectrum: hum is a comb of narrow spikes at 50 or 60 Hz and multiples of it.',
          'A notch filter at each spike removes it with little harm to the voice.',
          'Fix the cause too: move cables away from power, use a balanced mic cable, check the grounding.',
          'Do not notch harmonics you cannot see; check the result on the spectrum.'],
    body='''
<h2>Is it mains hum?</h2>
<p>A hum has a steady pitch that never moves. Mains hum sits at exactly 50 or 60 Hz and its harmonics at 100 or 120, 150 or 180 Hz, and so on. A spectrum view in any audio editor shows it as a row of narrow lines. Broadband hiss and fan noise look like a smear, not lines.</p>
<h2>Remove it with a notch filter</h2>
<p>A notch filter removes a very narrow band of frequency. In a free editor, apply a notch at the fundamental first, then at each harmonic you can see, and listen after each one. Keep the notches narrow (high Q) so the voice around them is untouched.</p>
<h2>Fix the cause too</h2>
<p>Moving the cable that carries the hum is faster than any filter. Keep mic cables away from power cables and lamp dimmers. A balanced XLR mic cable is more resistant than an unbalanced one. A ground loop, where two devices are connected through two different earth paths, is a common hidden cause: try a different power socket or a ground-lift adapter with care.</p>
<h2>Tunedzy</h2>
<p>Tunedzy's Repair tool measures hum, finds the fundamental and its harmonics, and notches them, then reports what it removed. It works on files at any sample rate. It will not remove a hum that changes pitch, and it will not notch a sound that only looks like hum.</p>
''',
    vf_title='Notch the hum, keep the voice',
    vf='<p>Tunedzy&rsquo;s Repair tool finds the hum, notches the fundamental and its harmonics, and tells you what it removed.</p>',
    faq=[('Is the hum 50 or 60 Hz?', 'It depends on the mains in your country. Europe, Asia and Africa mostly use 50 Hz, the Americas mostly 60 Hz. Measure it on the spectrum rather than guessing.'),
         ('Will a notch filter thin my voice?', 'A narrow notch affects only a tiny band. Wide notches or too many of them do thin the voice, so keep them as narrow as the hum allows.'),
         ('Can I remove hum from a video?', 'Yes, from the audio track. Tunedzy can repair the sound and put it back into the video with the picture unchanged.')],
    related=['remove-background-noise-from-a-voice-recording', 'fix-clipped-distorted-audio', 'clean-up-a-phone-voice-recording'])

add('fix-clipped-distorted-audio', 'neon-wide', ['vocal-checker', 'lufs-meter'],
    title='How to Fix Clipped, Distorted Audio',
    desc='What clipping is, why a recording distorts, how much can be recovered and how to rebuild the peaks without making the voice harsh.',
    h1='How to Fix Clipped, Distorted Audio',
    kw='fix clipped audio',
    lead='Clipping happens when a signal is louder than the recorder can record: the peaks are flattened, and the voice sounds fuzzy or crackly. Some of the flattened peaks can be rebuilt. Not all of them.',
    tldr=['Clipping shows as flat tops on the waveform, or as a crackle on loud words.',
          'Lower the input level and record again if you can, because the damage cannot be undone in the original.',
          'Repairs can rebuild a small number of clipped peaks from the wave around them; heavy clipping stays audible.',
          'Keep the original and compare.'],
    body='''
<h2>What clipping looks like</h2>
<p>Zoom into the waveform. Clipped audio has flat sections at the top and bottom, sometimes many samples long, where the recorder ran out of range. You hear it as a harsh, fuzzy distortion on the loudest words. A little clipping on a single shout is often hardly noticeable; clipping on every word is not.</p>
<h2>The fix that matters most: record lower</h2>
<p>Set the input so the loudest words peak around -6 dB on the meter. A recording that was never clipped sounds better than any repair. On a phone, move the mic a little further away or turn the input down in the recorder app.</p>
<h2>Repairing the file</h2>
<p>When clipping is already in the file, repair works by finding the flat tops and rebuilding the peaks from the curve of the wave on either side. This works well for short clips and rebuilds up to a limited length. Long flat runs (heavy clipping) cannot be rebuilt reliably, and a repair that claims otherwise is guessing.</p>
<p>Tunedzy's repair finds clipping at the file&rsquo;s own sample rate (phone files at 48 kHz included), rebuilds the peaks and then leaves headroom so the result does not clip again. It reports how many peaks it rebuilt. Check the Before and After: if the voice still sounds fuzzy, the clipping was too heavy to fix.</p>
<h2>After the repair</h2>
<p>Lower the level a little and check the true peak. A repaired file can still have peaks near full scale, which can distort when converted to MP3. Target -1 dBTP as a ceiling.</p>
''',
    vf_title='Rebuild the peaks, keep the file',
    vf='<p>Tunedzy&rsquo;s repair rebuilds clipped peaks at your file&rsquo;s own rate, then keeps headroom, and reports what it did.</p>',
    faq=[('Can clipping be removed completely?', 'Not always. Short clipped peaks can be rebuilt well. Long, heavy clipping leaves the voice fuzzy. Re-recording with the input turned down is the only complete fix.'),
         ('Why does my phone recording clip?', 'Phones apply gain automatically, and a loud voice close to the mic can push past full scale. Move back a little or lower the recorder input.'),
         ('Does a limiter fix clipping?', 'A limiter controls future peaks; it does not restore peaks that were already flattened. Use it to stop new clipping, not to repair old clipping.')],
    related=['remove-hum-from-audio', 'clean-up-a-phone-voice-recording', 'loudness-for-youtube-podcasts-and-spotify'])

add('record-a-voiceover-on-your-phone', 'booth', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='How to Record a Voiceover on Your Phone (TikTok, Reels, Shorts)',
    desc='Record a voiceover on your phone that sounds clear on TikTok, Reels and Shorts: room, distance, levels, timing and the cleanup that makes it sound pro.',
    h1='How to Record a Voiceover on Your Phone',
    kw='record voiceover on phone tiktok',
    lead='A good phone voiceover depends on the room and the distance more than the phone. A few habits make a short video sound professional.',
    tldr=['Record in a small, soft room with the fans off.',
          'Hold the phone 15 to 20 cm from your mouth, a little to the side, so pops are rare.',
          'Speak at an even pace, a little slower than you would talk.',
          'Trim the dead air before you line the voice up with the picture.'],
    body='''
<h2>Set the room</h2>
<p>A wardrobe full of clothes is a classic home booth: fabric soaks up the echo that makes a phone sound thin. Turn off fans, air conditioning and the fridge. Put a blanket or a towel over a hard table if the sound bounces.</p>
<h2>Set the distance and the level</h2>
<p>Hold the phone about 15 to 20 cm from your mouth, slightly to the side, so the breath hits the side of the mic. Record a few seconds at your normal speaking volume and play it back. Loud peaks mean move back; a faint voice means move closer or raise the input.</p>
<h2>Read it as if you are talking</h2>
<p>Speak at a steady pace, with a little more space between sentences than in conversation. Take two or three takes and keep the one where you sound like yourself, not the one where you sound most careful.</p>
<h2>Clean and trim</h2>
<p>Cut the silence at the start and end of each take. A rough take often becomes a much tighter read after you remove the gaps. Then run a cleanup: <a href="/tunedzy/clean-up-a-phone-voice-recording">the phone cleanup steps</a> apply to a voiceover too.</p>
<h2>Line it up with the picture</h2>
<p>Place the voice on the video timeline and check the first and last words against the picture. If the app lets you set the balance between the original sound and your voiceover, lower the music, not the voice. The exact controls change between app versions.</p>
''',
    vf_title='Clean the take in your pocket',
    vf='<p>Tunedzy Go cleans a voiceover on your phone for free. Record in the app or choose a file, then download the cleaned sound.</p>',
    faq=[('What app is best for a phone voiceover?', 'Any recorder you already have is fine if the room is right. Tunedzy Go is a free phone app for cleaning the take afterwards.'),
         ('Should the voiceover be louder than the music?', 'Usually yes, or at least clearly easier to hear. A good starting point is to set the music to about half the voice level.'),
         ('Why does my voiceover echo?', 'A bare room with hard walls. Move to a room with soft surfaces, or record in a wardrobe.')],
    related=['clean-up-a-phone-voice-recording', 'put-clean-audio-back-into-a-video', 'voice-note-sounds-better-on-an-iphone'])

add('podcast-sound-professional-on-a-budget', 'desk', ['clean-streaming-mic', 'lufs-meter'],
    title='How to Make a Podcast Sound Professional on a Budget',
    desc='A realistic budget podcast setup: room, mic and headphones, one good habit per step, and the loudness and cleanup that make it sound finished.',
    h1='How to Make a Podcast Sound Professional on a Budget',
    kw='podcast sound professional budget',
    lead='Most podcasts sound amateur because of the room, the distance from the mic and uneven levels, not the price of the mic. Fix those three first.',
    tldr=['Record in a small, soft room; this matters more than any gear.',
          'Use one mic per person, close to the mouth, and keep everyone at the same distance.',
          'Level each speaker separately, then set the whole episode to one loudness target.',
          'Clean the noise once, edit by the words, and export a loudness the platforms expect.'],
    body='''
<h2>The room</h2>
<p>Record in a room that has soft surfaces, curtains, rugs and a sofa. A closet with clothes is still the cheapest good booth. Turn off the fan and the fridge while you record.</p>
<h2>The mic and the distance</h2>
<p>A USB or XLR mic close to each speaker beats an expensive mic far away. Keep each person the same distance from their mic, about a hand&rsquo;s width, and use a pop filter or a foam cover to stop breath pops.</p>
<h2>Levels</h2>
<p>Each speaker is usually at a different level. Bring each one to about the same loudness before you mix them together. A loud guest and a quiet host is the most common reason a podcast sounds unfinished.</p>
<h2>Cleanup and loudness</h2>
<p>Remove the noise once on the whole recording, then cut the dead air and the ums. Finally set the episode to one loudness target. Tunedzy&rsquo;s Match loudness and its podcast preset (-16 LUFS) do this in one step, with a check for true peak. Check your podcast host&rsquo;s guidance before you publish, because platforms can change their recommendations.</p>
<h2>Keep the sound consistent</h2>
<p>Record each episode the same way: the same room, the same mic position, the same level. Consistent recordings clean up more easily and sound more like one show.</p>
''',
    vf_title='Level the voices and export the episode',
    vf='<p>Multitrack in Tunedzy lines up each voice, levels them and exports the mix at a podcast loudness, with a pass or fail check.</p>',
    faq=[('Do I need an expensive mic?', 'No. A close, well-placed mic in a soft room sounds better than an expensive mic in a hard room far away.'),
         ('How loud should a podcast be?', 'Many podcast guides use around -16 LUFS for stereo and -19 LUFS for mono. Check the rules of the platform you publish on.'),
         ('How do I stop one guest sounding quieter?', 'Level each track separately before mixing. Automatic levelling can help, but setting each track by hand first gives better results.')],
    related=['record-a-voiceover-on-your-phone', 'loudness-for-youtube-podcasts-and-spotify', 'edit-a-podcast-by-its-words'])

add('edit-a-podcast-by-its-words', 'desk-wide', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='How to Edit a Podcast by Its Words (Remove Ums and Pauses)',
    desc='Edit a podcast or interview by reading the transcript: cut ums and long pauses, check the cuts by ear and export captions. Works on your own PC.',
    h1='How to Edit a Podcast by Its Words',
    kw='edit podcast by words remove ums',
    lead='Editing by the transcript is faster than editing the waveform: you read what was said, delete the parts you do not want, and listen to the cut.',
    tldr=['Transcribe the recording on your own computer, so nothing is uploaded.',
          'Delete ums, uhs and repeated words, then shorten long pauses rather than deleting every one.',
          'Listen to every cut: a cut in the middle of a breath or a word can sound wrong.',
          'Export captions from the same transcript for video.'],
    body='''
<h2>Transcribe</h2>
<p>A speech model writes out what is said, with the time of each word. The transcript is your map. Accuracy depends on the audio: a clean recording gives a near-perfect transcript, a noisy one needs checking. Clean the audio first, then transcribe, for the best result.</p>
<h2>Remove the ums and uhs</h2>
<p>Ums and uhs are easy to find in a transcript. Cut them, then listen. Some are part of a natural speech rhythm; removing every one can make a voice sound robotic. Keep the ones that sit between thoughts.</p>
<h2>Shorten the pauses, do not delete them</h2>
<p>Long pauses make an episode drag. Shorten the ones over about 0.8 seconds to a third of a second, and leave the pauses that give a line weight. A pause that falls after a joke or before a change of topic is usually worth keeping.</p>
<h2>Check each cut</h2>
<p>Every cut is a join. Listen to it at normal volume and listen for a click, a change of room tone or a clipped word. A short crossfade at each cut hides most joins.</p>
<h2>Export captions</h2>
<p>The same transcript can become SRT or VTT caption files for video platforms, or a plain text file for show notes. Check the captions against the audio before you publish.</p>
<h2>What it cannot do</h2>
<p>A transcript is only as good as the audio, and speech models can mishear names and technical words. Proofread the names and check any quote before publishing.</p>
''',
    vf_title='Edit the words, keep the voice',
    vf='<p>Tunedzy writes the transcript on your PC, lets you cut words, removes fillers and shortens pauses, then exports captions. Nothing is uploaded.</p>',
    faq=[('Do ums always need to go?', 'No. Remove the ones that distract. Keeping a few makes the speech sound human.'),
         ('Is the transcript accurate?', 'Good on clear speech, weaker on accents, names and noise. Always check names and quotes before you publish.'),
         ('Where is the transcript stored?', 'On your PC, with your project. Tunedzy does not upload it.')],
    related=['podcast-sound-professional-on-a-budget', 'clean-up-a-phone-voice-recording', 'record-a-voiceover-on-your-phone'])

add('put-clean-audio-back-into-a-video', 'neon', ['vocal-checker', 'clean-streaming-mic'],
    title='How to Put Clean Audio Back Into a Video',
    desc='Replace the sound in a phone video with a cleaned voice without re-encoding the picture. Steps, quality tips and the limits.',
    h1='How to Put Clean Audio Back Into a Video',
    kw='replace audio in video',
    lead='You can clean a video&rsquo;s sound and put it back without touching the picture. The key is to copy the picture and replace only the audio track.',
    tldr=['Clean the audio on its own first, then put it back.',
          'Replace the audio track and copy the video stream: the picture is not re-encoded.',
          'Check the length: a longer audio track is cut to the picture, a shorter one leaves silence.',
          'Keep the original video in case you need it again.'],
    body='''
<h2>Why the picture should not be re-encoded</h2>
<p>Every time a video is re-encoded it loses a little quality. If you only change the sound, the video stream can be copied as it is. That is faster and keeps the picture identical.</p>
<h2>The steps</h2>
<ol>
<li>Clean the audio. The phone cleanup and the Perfect it steps in <a href="/tunedzy/clean-up-a-phone-voice-recording">the cleanup guide</a> apply.</li>
<li>Open the video in Tunedzy and choose the replace-audio option. Pick the cleaned file.</li>
<li>Tunedzy copies the picture and writes the new sound beside it. Play the result and check the start, the end and the joins.</li>
</ol>
<h2>Limits</h2>
<p>The replacement works for common phone formats (MP4 and MOV), and the picture is copied, not changed. If the new sound is longer than the picture it is cut; if it is shorter, the rest of the video is silent. A video with no picture stream is refused.</p>
<p>On your phone, <a href="/tunedzy/go/">Tunedzy Go</a> cleans the sound of a recording or a file you choose. Putting the sound back into a video is a Windows app step for now.</p>
''',
    vf_title='Clean the sound, keep the picture',
    vf='<p>Tunedzy puts a cleaned voice back into your video and copies the picture as it is.</p>',
    faq=[('Will the video get worse?', 'No, the picture is copied, not re-encoded. Only the sound changes.'),
         ('Which video formats work?', 'MP4 and MOV from phones work well. Other common containers are read as well; ask in the app if one fails.'),
         ('Can I use this on TikTok or Reels?', 'Yes. Export the video with the new sound, then upload it as you normally would.')],
    related=['record-a-voiceover-on-your-phone', 'clean-up-a-phone-voice-recording', 'remove-hum-from-audio'])

add('loudness-for-youtube-podcasts-and-spotify', 'mic-wide', ['lufs-meter', 'vocal-checker'],
    title='Loudness for YouTube, Podcasts and Spotify: LUFS and True Peak Explained',
    desc='What LUFS and true peak mean, which targets people use for YouTube, podcasts and music, and how to set a voice to them without clipping.',
    h1='Loudness for YouTube, Podcasts and Spotify',
    kw='LUFS for YouTube podcast Spotify',
    lead='Loudness is measured in LUFS, a single number for how loud something sounds over its length. True peak tells you how close the loudest moment is to clipping.',
    tldr=['LUFS measures average loudness; true peak measures the highest moment.',
          'Many platforms turn loud files down, so a target near -14 LUFS for online video and about -16 LUFS for podcasts is a safe starting point.',
          'Keep the true peak below -1 dBTP so the file does not distort when converted.',
          'Measure the whole file, not a short part.'],
    body='''
<h2>LUFS, in one paragraph</h2>
<p>LUFS (loudness units relative to full scale) is the loudness people actually hear, averaged over the whole file and weighted to how the ear works. Two files with the same LUFS feel about equally loud. A peak meter cannot tell you that.</p>
<h2>The targets people use</h2>
<p>Platforms set their own rules and change them, so check the current guidance before you publish. As a starting point many creators use about -14 LUFS for online video (YouTube turns louder files down to around that level), about -16 LUFS for stereo podcasts and about -19 LUFS for mono or audiobook work. Tunedzy&rsquo;s match loudness has presets for these targets.</p>
<h2>True peak</h2>
<p>True peak shows the highest level after conversion, including the overs a conversion to MP3 can create. Keep it at or below -1 dBTP. A file that reads -0.1 dBTP on the peak meter can still sound distorted once it is converted.</p>
<h2>Set the level</h2>
<ol>
<li>Measure the loudness of the whole file with a LUFS meter.</li>
<li>Raise or lower the level to the target. Do not use a limiter to reach a high LUFS target: it squashes the voice.</li>
<li>Check the true peak. If it is above -1 dBTP, a true-peak limiter at -1 dBTP is the safe fix.</li>
</ol>
<p>The <a href="/tunedzy/tools/lufs-meter">free LUFS meter</a> on this site measures a file in your browser. Nothing is uploaded.</p>
''',
    vf_title='Set the loudness, check the peak',
    vf='<p>Tunedzy&rsquo;s match loudness sets a voice to a target with the true peak checked, and the free LUFS meter measures a file in your browser.</p>',
    faq=[('Is -14 LUFS the YouTube standard?', 'It is a common reference, because YouTube turns louder files down toward that level. Check YouTube&rsquo;s own guidance for the current rule.'),
         ('Does a higher LUFS sound better?', 'Not always. A very high LUFS usually means the voice is squashed. A moderate level with a clean voice sounds better.'),
         ('Why does my file sound quieter on Spotify?', 'Music platforms normalise loudness. A file that is far above the target is turned down; a file far below may be turned up with more noise.')],
    related=['podcast-sound-professional-on-a-budget', 'fix-clipped-distorted-audio', 'record-a-voiceover-on-your-phone'])

add('voice-note-sounds-better-on-an-iphone', 'mic', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Make an iPhone Voice Note Sound Better',
    desc='Get a clearer voice note or voice memo on an iPhone: recording settings, the room, and how to clean the recording afterwards.',
    h1='How to Make an iPhone Voice Note Sound Better',
    kw='iphone voice memo sound better',
    lead='An iPhone records a good voice, but a voice note made in a bad room sounds like it. The fix is mostly in the recording, then a cleanup for what is left.',
    tldr=['Hold the phone at the same distance you would for a call: about 15 to 20 cm.',
          'Record in a soft room; a car with the windows closed is often quieter than a kitchen.',
          'Check the input level before the recording starts; avoid the red.',
          'Clean the note afterwards and keep the original.'],
    body='''
<h2>Recording</h2>
<p>Use the built-in Voice Memos app or any recorder you like. Hold the phone steady, speak across the top, and avoid covering the microphone holes with your fingers. Record a few seconds first to check the level.</p>
<h2>Room</h2>
<p>A quiet room with soft furnishings is best. Turn off fans and fridges and close the window. Recording in a car with the engine off and the windows up is a surprisingly good trick for a quiet, soft space.</p>
<h2>After the recording</h2>
<p>Clean the note with the steps in <a href="/tunedzy/clean-up-a-phone-voice-recording">the cleanup guide</a>. Tunedzy Go does this on the phone for free, and the Windows app does it with more control. Keep the original file.</p>
''',
    vf_title='Clean the note on the phone',
    vf='<p>Tunedzy Go works on the phone for free: record or choose the note, clean it and download the result. Nothing is uploaded.</p>',
    faq=[('Is there a better app than Voice Memos?', 'Voice Memos records well. Cleaning and levelling the note is a separate step, and that is where a cleanup app helps.'),
         ('Why does my voice note sound far away?', 'The phone is far from your mouth or the room is echoey. Move closer and try a softer room.'),
         ('Will Tunedzy Go work on an iPhone?', 'It is a web app for modern phone browsers, and you can add it to the home screen. It has been tested in desktop Chromium so far; test it on your own iPhone before relying on it.')],
    related=['clean-up-a-phone-voice-recording', 'record-a-voiceover-on-your-phone', 'remove-background-noise-from-a-voice-recording'])

add('record-a-vocal-at-home-for-a-song', 'booth-wide', ['song-key-finder', 'bpm-finder', 'vocal-checker'],
    title='How to Record a Vocal at Home for a Song',
    desc='Record a song vocal in a bedroom: room, mic position, headphones, levels, takes, and how to clean and mix the result in Tunedzy.',
    h1='How to Record a Vocal at Home for a Song',
    kw='record vocal at home',
    lead='A home vocal sounds finished when the room is controlled, the level is right and the takes are chosen well. The recording matters more than the plugins.',
    tldr=['Record in a soft room, and put the mic away from hard walls.',
          'Use headphones so the beat does not come back into the mic.',
          'Set the level so the loudest words peak around -6 dB, then record several takes.',
          'Clean, tune and mix the best take; you can keep the others.'],
    body='''
<h2>Room</h2>
<p>A wardrobe of clothes, or a room with a rug, curtains and a sofa, controls the echo that makes a home vocal sound thin. Stand facing the wall with the soft things, not into a bare corner.</p>
<h2>Mic and headphones</h2>
<p>Any decent condenser or dynamic mic works if the room is right. Use closed headphones so the beat does not leak into the mic. Keep the mic a hand&rsquo;s width from your mouth and use a pop filter for the breath sounds.</p>
<h2>Level and takes</h2>
<p>Set the input so the loudest part of the song peaks around -6 dB. Record several takes of each section. Choose the best parts of each take in editing rather than trying to get one perfect take.</p>
<h2>Clean and mix</h2>
<p>Clean each take, check the key and tempo against your beat with the <a href="/tunedzy/tools/song-key-finder">key finder</a> and the <a href="/tunedzy/tools/bpm-finder">BPM finder</a>, and check the vocal level with the <a href="/tunedzy/tools/vocal-checker">vocal checker</a>. In Tunedzy, the Multitrack studio stacks the takes, levels the voice against the beat, and exports the mix at a loudness target.</p>
<p>Tunedzy is not a beat maker: keep your beat in your own DAW and bring the vocal into Tunedzy for the cleanup and the mix.</p>
''',
    vf_title='From take to finished vocal',
    vf='<p>Tunedzy cleans the vocal, lines up the takes in Multitrack and exports the mix at a loudness target. Your beat stays in your own DAW.</p>',
    faq=[('Do I need an audio interface?', 'A USB mic works well for a home vocal. An interface gives more control of levels, but the room matters more than the connection.'),
         ('Can Tunedzy replace a DAW?', 'For recording, cleaning, editing and mixing voices, yes. It does not make beats, and it does not run VST or AU plugins.'),
         ('Should I tune the vocal?', 'Tuning is a style choice. Tunedzy has autotune in your key, but a light touch usually sounds more natural than a hard effect.')],
    related=['podcast-sound-professional-on-a-budget', 'clean-up-a-phone-voice-recording', 'fix-vocals-recorded-on-phone'])
