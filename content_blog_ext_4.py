"""Blog posts, batch 4 of 10: audio repair and clean-up cluster. Merged into content_blog.py.
Each post answers one search first, then explains it in plain steps, admits its limits, and links to a tool or guide.
No invented statistics, reviews, prices or benchmarks."""

CLUSTERS = {
    'repair': dict(tool='vocal-checker', label='Audio repair and clean-up', tool_name='Vocal Checker'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='how-to-remove-hum-from-a-voice-recording', cluster='repair', kw='remove hum from voice recording',
    title='How to Remove Hum From a Voice Recording',
    desc='Remove hum from a voice recording: find the source, fix it at the root where you can, then use a narrow filter only where needed, without making the voice dull.',
    h1='How to Remove Hum From a Voice Recording',
    answer='Find the source of the hum first, because most hum comes from power cables, lights, a computer or a bad ground. Fix it there if you can. If hum remains, use a narrow notch filter at the hum frequency, and listen to make sure the voice has not lost its warmth.',
    body='''
<p>Hum is a steady low tone that sits under a recording, often at 50 or 60 hertz depending on the mains supply, with harmonics above it. It is one of the most common problems in home recordings and one of the easiest to fix if you find the cause. Filtering helps, but the best fix is removing the source.</p>
<h2>Find the source before you filter</h2>
<p>Turn things off one at a time and record a few seconds of silence after each change. Common sources are a laptop charger, a light dimmer, a fridge, a USB hub, a monitor or a poor audio cable. A microphone cable run beside a power cable can pick up hum too. Once the hum drops when something is switched off, you know the cause.</p>
<h2>Fix the root cause where you can</h2>
<ul>
<li>Move the microphone cable away from power cables and chargers.</li>
<li>Plug the computer and the interface into the same power outlet or power strip.</li>
<li>Use a different USB port or a short, shielded cable.</li>
<li>Switch off or move the device that makes the hum, or record in a different room.</li>
</ul>
<h2>Use a narrow filter only where needed</h2>
<p>If hum remains, a notch filter at the hum frequency and its harmonics can reduce it. Keep the notch narrow, so the voice keeps its warmth. Wide filters remove the body of the voice as well. Listen carefully, because a notch that is too wide makes the speech sound thin and hollow.</p>
<h2>Check the result</h2>
<p>Play the processed file on headphones, then on a phone speaker. Check the quiet pauses in particular, since hum shows most clearly when the voice stops. The <a href="/tunedzy/clean-up-a-phone-voice-recording">cleanup guide</a> shows how to apply light cleanup without over-processing.</p>
<h2>Limits</h2>
<p>A filter cannot remove hum that overlaps the voice closely, and heavy filtering damages the sound. If the hum is strong, fix the cause and re-record where you can. Clean recordings are always easier to finish than repaired ones.</p>
''',
    faq=[('Why does my recording have a low buzz?', 'Usually a power source, a cable run beside power, or a poor ground. Find the source by switching things off one at a time.'),
         ('Can I remove hum completely?', 'Often you can reduce it a lot. Complete removal is harder, especially when hum overlaps the voice.'),
         ('Will a noise reducer remove hum?', 'Some can, but a targeted notch is usually more precise. Check the result on the pauses.'),
         ('Does the hum change with the country I am in?', 'Mains frequency differs by country, which is why hum is often at 50 or 60 hertz. The cause is still a nearby source.')])

add(slug='how-to-fix-clicks-and-pops-in-an-audio-recording', cluster='repair', kw='how to fix clicks in audio recording',
    title='How to Fix Clicks and Pops in an Audio Recording',
    desc='Fix clicks and pops in an audio recording: find whether the cause is the mic, the cable, the file or the edit, then repair each one with a small change.',
    h1='How to Fix Clicks and Pops in an Audio Recording',
    answer='Clicks and pops come from a few sources: a loose cable, a digital glitch, a sudden edit, or a mouth or breath sound. Find which one you have by listening closely, then fix the cause where possible. Repair the rest by zooming in and smoothing each click with a very short fade.',
    body='''
<p>A click is a sharp, short sound that interrupts a recording, and a pop is a louder, rounder burst. Both are easy to notice and easy to make worse if you fix them carelessly. The first step is to work out where each one comes from.</p>
<h2>Listen to find the source</h2>
<p>A click that appears at the same point every time, or on every take, usually comes from the equipment. A click that happens only when you speak may be a mouth sound or a breath. A click that follows an edit points to a join. A click that appears only when you move the cable is a loose connection. Note the pattern, then fix the source where you can.</p>
<h2>Fix the equipment first</h2>
<p>Check the cable, the plug and the connection to the interface. Replace a cable that crackles when moved. Turn off any power-saving setting on a USB device that drops out. A digital glitch from a buffer or a driver problem may need the settings adjusted, then the recording repeated.</p>
<h2>Repair each click by hand</h2>
<ol>
<li>Zoom in on the waveform until the click is clear.</li>
<li>Select a very small area around it, and cut or smooth it.</li>
<li>Apply a short fade on either side of the repair, so the join does not jump.</li>
<li>Play the repair at normal speed, and compare it with the original.</li>
</ol>
<h2>Watch out for over-repair</h2>
<p>Repairing every small sound makes a voice sound robotic and unnatural. Breaths, lip sounds and room noise are part of a human voice. Repair only what is distracting. A little natural noise is better than an edit that sounds cut.</p>
<h2>Prevent them next time</h2>
<p>Use a pop filter for plosive pops, keep the microphone cable away from power, and record a little room tone before each session. The <a href="/tunedzy/blog/remove-mic-pops-plosives">plosive post</a> covers pops from speech in more detail.</p>
<h2>Limits</h2>
<p>Clicks inside loud speech are hard to repair without leaving a mark. If a recording has many clicks, check the cable and the setup before you spend time on edits. Repairing a bad recording takes much longer than recording it well the first time.</p>
''',
    faq=[('Where do most clicks come from?', 'Loose cables, digital glitches and edits. Mouth sounds and breaths also cause clicks in speech.'),
         ('Should I fix clicks before or after cleaning the noise?', 'Fix the clicks first, then clean the noise, so the cleanup does not spread the repair.'),
         ('Can I remove a pop completely?', 'Usually you can reduce it a lot. A pop from a plosive is best prevented with a pop filter.'),
         ('Why does my repair sound like a cut?', 'The fade is too short or the room tone does not match. Smooth the join and match the sound on each side.')])

add(slug='how-to-remove-wind-noise-from-a-recording', cluster='repair', kw='remove wind noise from recording',
    title='How to Remove Wind Noise From a Recording',
    desc='Remove wind noise from a recording: why wind is so hard to fix, how to use a windscreen and placement, and what a filter can and cannot save.',
    h1='How to Remove Wind Noise From a Recording',
    answer='Wind noise is a rumbling, low-frequency sound caused by moving air across the microphone. The best fix is prevention: use a windscreen or a furry cover and move the microphone out of the wind. A filter can reduce the rumble, but it cannot restore speech that the wind has covered.',
    body='''
<p>Wind noise sounds like a roar or a rumble, and it can bury speech on an outdoor recording. It is caused by air moving over the microphone capsule, not by the sound you want to capture. That is why it is so hard to remove afterwards: the wind is not the same as the voice, and it often covers the same frequencies.</p>
<h2>Prevent it before you record</h2>
<p>Use a foam windscreen, and for strong wind a furry cover, which breaks up the air movement. Shelter the microphone behind a person, a wall or a car, and keep it out of the direct path of the breeze. Record when the wind is lower, or move to a more sheltered spot. Prevention beats any cure.</p>
<h2>Check the placement</h2>
<p>A microphone pointing into the wind picks up much more noise than one pointing across it. Turn the microphone slightly, so the wind passes over the front rather than straight into the capsule. Keep the same distance from the speaker, so the voice sounds consistent.</p>
<h2>Use a high-pass filter carefully</h2>
<p>A high-pass filter removes low frequencies, which reduces the rumble. Set the cutoff low enough that the voice keeps its body. If you cut too high, the speech becomes thin and tinny. Listen carefully and adjust in small steps, rather than cutting the low end hard.</p>
<h2>Reduce what remains</h2>
<p>For steady wind noise, a gentle noise reducer can help, but it may leave a watery sound. Use it lightly, and compare with the original. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can reduce background noise on speech, though strong wind is still best prevented.</p>
<h2>Limits</h2>
<p>When wind has covered the words, no filter can bring them back. In that case, re-record the line, or use a different take. A short, clean take in a sheltered spot is worth more than a long, repaired one.</p>
''',
    faq=[('Is a windscreen enough?', 'For light breeze, usually yes. Strong wind needs a furry cover or a sheltered spot.'),
         ('Can I remove wind noise completely in editing?', 'Rarely. Filters reduce the rumble but cannot restore speech that the wind has covered.'),
         ('Should I cut all the low end to remove wind?', 'No. It thins the voice. Use a high-pass filter gently and listen carefully.'),
         ('Does a phone need a windscreen?', 'Often, yes. A phone microphone is small and sensitive to wind, so a cover helps.')])

add(slug='how-to-remove-a-dropout-from-an-audio-file', cluster='repair', kw='fix dropouts in audio recording',
    title='How to Fix a Dropout in an Audio Recording',
    desc='Fix a dropout in an audio recording: why sudden silences or cut-outs happen, how to check the source, and how to repair a short gap without an audible join.',
    h1='How to Fix a Dropout in an Audio Recording',
    answer='A dropout is a sudden gap or cut-out in the sound, often caused by a loose connection, a wireless signal problem or a recording buffer error. Check the cause first, then repair a short dropout by filling it with a matched piece of room tone or by repeating a clean word, if the content allows.',
    body='''
<p>A dropout is a short moment where the sound disappears or cuts out for a fraction of a second, then returns. It can sound like a stutter, a missing word or a digital hiccup. Dropouts are frustrating because they often happen once, and nobody notices until playback.</p>
<h2>Find out what caused it</h2>
<p>Check the connection between the microphone, the cable and the interface. A wireless microphone can drop out when it moves out of range or meets interference. A computer that is busy can cause a buffer error. Check the recording settings, the buffer size and any power-saving options on the computer and the USB devices.</p>
<h2>Check the take</h2>
<p>Listen to the whole take, not only the part you noticed. Dropouts can be short and easy to miss, so zoom in on the waveform to see flat sections. If the dropout is in a quiet pause, the repair is easy. If it cuts a word, the repair is harder, and a re-record may be the better choice.</p>
<h2>Repair a short gap in a pause</h2>
<p>In a pause, fill the gap with a short piece of room tone from the same recording. Copy a few seconds of quiet, match its level, and crossfade both ends. Listen for any change in the room sound. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone post</a> explains how to capture usable room tone.</p>
<h2>Repair a gap in speech carefully</h2>
<p>If the dropout cuts a word, you may be able to repeat a clean word from elsewhere in the take, but only if the pitch, speed and emphasis match. Otherwise the join will be obvious. Re-recording the phrase is often faster and sounds better.</p>
<h2>Prevent the next one</h2>
<p>Keep wireless microphones charged and close, and test them before recording. Use a stable buffer setting, and close heavy programs before a session. Record a short test and listen to it before a long take.</p>
<h2>Limits</h2>
<p>Repairing a dropout is a short-term fix. If the problem is the equipment, it will return. Fix the cause before the next session, so you do not spend hours repairing takes.</p>
''',
    faq=[('Is a dropout always a hardware problem?', 'Not always. Buffer errors and busy computers can cause them too, so check the settings.'),
         ('How do I find a short dropout?', 'Zoom in on the waveform and look for flat sections, or listen closely to pauses.'),
         ('Can I copy a word to replace a dropout?', 'Only if the pitch, speed and emphasis match. Otherwise re-record the phrase.'),
         ('Does a wireless microphone cause more dropouts?', 'It can, if it moves out of range or meets interference. Test it before you record.')])

add(slug='how-to-fix-uneven-volume-in-a-voice-recording', cluster='repair', kw='fix uneven volume in recording',
    title='How to Fix Uneven Volume in a Voice Recording',
    desc='Fix uneven volume in a voice recording: find out whether the problem is distance, the take or the edit, then level the speech evenly without flattening it.',
    h1='How to Fix Uneven Volume in a Voice Recording',
    answer='Uneven volume usually comes from changing distance to the microphone, speaking at different strengths, or joining takes recorded at different levels. Level the sections by hand first, using gain changes on the clips, then apply gentle levelling if needed. Keep the natural variation that gives the voice life.',
    body='''
<p>Some variation is natural in speech, because people get louder and softer as they talk. Uneven volume is different. It is the jump from a quiet section to a loud one that makes a listener reach for the volume knob. The fix is to match the levels between sections while keeping the voice expressive.</p>
<h2>Find the cause</h2>
<p>Listen for patterns. If the speaker moves closer or further from the microphone, the level changes with their position. If the level jumps at the edit point, two takes were recorded at different levels. If one passage is consistently quiet, the speaker probably turned away or spoke more softly. Each cause has a different fix.</p>
<h2>Level the clips by hand</h2>
<ol>
<li>Start with the loudest section, and set it to a comfortable level.</li>
<li>Raise or lower the quieter sections so they sit near it.</li>
<li>Use small gain changes, and check each join by listening.</li>
<li>Leave the natural lift and drop of emphasis in place.</li>
</ol>
<h2>Use gentle levelling</h2>
<p>If the variation is still large after hand levelling, a gentle levelling tool can smooth the remaining differences. Keep the amount low, or the voice will sound compressed and lifeless. The <a href="/tunedzy/how-to-level-voices-between-speakers">levelling guide</a> shows how to apply levelling across two or more speakers.</p>
<h2>Check the peaks and the quiet parts</h2>
<p>After levelling, check that the loudest moments do not clip, and that the quiet passages are still clear on a phone. If the quiet parts are now noisy, reduce the background noise before raising them further.</p>
<h2>Prevent the problem</h2>
<p>Keep the microphone distance steady, use a marker on the desk, and record a short test at the start of each session. Speak at a steady strength, and record each section with its own check before moving on.</p>
<h2>Limits</h2>
<p>Levelling cannot fix every problem. A very quiet take with a lot of noise will sound noisy when raised, and a loud take with clipping cannot be made clean. In those cases, re-recording is the better choice.</p>
''',
    faq=[('Should I make the whole recording the same level?', 'Level the sections so they sit together, but keep the natural emphasis of the voice.'),
         ('Why does the volume change at every edit?', 'Two takes were recorded at different levels. Match them by hand before levelling.'),
         ('Will levelling make my voice sound squashed?', 'Only if you use too much. Keep it gentle and listen for flatness.'),
         ('Is it better to re-record?', 'If the take is very quiet, very loud or clipped, re-recording usually sounds better.')])

add(slug='how-to-fix-a-tinny-voice-recording', cluster='repair', kw='fix tinny voice recording',
    title='How to Fix a Tinny or Thin Voice Recording',
    desc='Fix a tinny or thin voice recording: why speech sounds small, how to add warmth with care, how to avoid harshness and when a re-record is the better option.',
    h1='How to Fix a Tinny or Thin Voice Recording',
    answer='A tinny voice is usually missing low warmth and has too much harsh upper midrange. Add a little body with a gentle low shelf or a wide boost, reduce any harsh band with a narrow cut, and check the result on headphones and a phone. If the thinness comes from a distant microphone, a re-record will do more than any filter.',
    body='''
<p>A thin or tinny voice sounds small, hollow or like it is coming through a telephone. It is one of the most common complaints about phone and laptop recordings. The cause is usually the microphone, the distance or the room, and the fix starts with understanding which one you have.</p>
<h2>Why a voice sounds tinny</h2>
<p>Speech has energy across the low and middle range, which gives it warmth and body. A microphone far from the speaker, or a small built-in microphone, can lose low energy and emphasise a harsh upper midrange. A reflective room adds a hollow, bright edge. Together, they make the voice sound thin.</p>
<h2>Add a little body</h2>
<p>A gentle low shelf or a wide, mild boost in the low middle range can restore some warmth. Make small changes, and listen to the voice as a whole. Too much low boost makes the voice boomy, which is a different problem, covered in the <a href="/tunedzy/blog/how-to-fix-boomy-vocals-proximity-effect">proximity effect post</a>.</p>
<h2>Reduce the harsh band</h2>
<p>Many thin recordings have a harsh band in the upper middle range. Find it by sweeping a narrow boost across the range, then cut the band you hear as harsh. A narrow cut keeps the clarity of speech, and a wide cut dulls it. Use the smallest change that works.</p>
<h2>Check the result</h2>
<p>Play the voice on headphones, then on a phone speaker and a laptop. A good fix sounds warmer without becoming muddy and keeps the words clear. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise, rumble and level problems in a recording, which helps you see what to fix before you change the tone.</p>
<h2>When to re-record</h2>
<p>If the voice is far from the microphone or the room is very reflective, a filter cannot put back the body the microphone never captured. Move closer, add soft surfaces, and record again. A short, close take usually sounds better than a long, heavily processed one.</p>
<h2>Limits</h2>
<p>EQ can change the tone of a voice, but it cannot make a distant recording sound close. Use it to improve what is there, and fix the recording setup for the next session.</p>
''',
    faq=[('Is a tinny voice always a microphone problem?', 'Often it is distance and room, not the microphone. Move closer and reduce reflections first.'),
         ('Should I boost the bass to fix it?', 'Only a little. Too much bass makes the voice boomy and muddy.'),
         ('What frequency is the harsh part?', 'It varies by voice and microphone. Find it by sweeping a narrow boost, then cut the band you hear as harsh.'),
         ('Can a phone recording sound less tinny?', 'Yes, with a closer position, a quieter room and gentle EQ.')])

add(slug='how-to-make-a-harsh-voice-recording-sound-warmer', cluster='repair', kw='make harsh voice recording warmer',
    title='How to Make a Harsh Voice Recording Sound Warmer',
    desc='Make a harsh voice recording sound warmer: where harshness comes from, how to tame it with careful EQ and light processing, and how to keep the voice clear.',
    h1='How to Make a Harsh Voice Recording Sound Warmer',
    answer='Harshness usually sits in the upper middle range, often between 2 and 5 kilohertz, and it can come from a bright microphone, a close position or a reflective room. Find the harsh band, cut it gently, and add a little low warmth. Compare with the original to make sure the voice still sounds clear.',
    body='''
<p>A harsh recording is hard to listen to, even when the words are clear. It can feel sharp, edgy or fatiguing, and listeners may leave after a few minutes. Warming a harsh voice is a balance: you reduce the edge without losing the clarity that makes speech easy to follow.</p>
<h2>Where harshness comes from</h2>
<p>Harshness often comes from a bright microphone, a close position that exaggerates the consonants, or a hard room that reflects the high frequencies. Compression can also make a harsh voice more noticeable, by raising quiet high-frequency detail. Knowing the source helps you decide whether to fix the sound or the setup.</p>
<h2>Find the harsh band</h2>
<p>Use a narrow boost on the equaliser and sweep slowly across the upper middle range. When the voice sounds most unpleasant, you have found the band. Cut that band by a small amount, then sweep again to check you have not removed the clarity from the words.</p>
<h2>Add a little warmth</h2>
<p>A gentle boost in the low middle range can add body and make the voice sound closer and warmer. Keep the change small, and listen to the whole sentence rather than a single word. The <a href="/tunedzy/blog/how-to-de-ess-vocals">de-essing post</a> covers the sharp S sounds that often add to the harshness.</p>
<h2>Keep the clarity</h2>
<p>Do not cut the high frequencies too far, or the voice will sound dull and muffled. Speech needs some brightness to be clear. Aim to take off the edge, not the air.</p>
<h2>Check the result</h2>
<p>Compare the processed file with the original on headphones, then on a phone. The warmer version should be easier to listen to over a few minutes, and the words should still be clear. If it sounds muddy, you have cut too much body or boosted too much low middle.</p>
<h2>Limits</h2>
<p>EQ can soften a harsh recording, but it cannot change the microphone or the room. For a recording that is consistently harsh, the setup is the real problem. Adjust the distance and the room for the next session, and use a light touch on the current one.</p>
''',
    faq=[('What frequency makes a voice sound harsh?', 'It varies, but the upper middle range is common. Find it with a narrow boost, then cut it gently.'),
         ('Will cutting the highs make it warmer?', 'Cutting too much makes the voice dull. Cut only the harsh band and keep the clarity.'),
         ('Does compression make harshness worse?', 'It can, by raising quiet high detail. Check the EQ before you compress.'),
         ('Should I re-record a harsh take?', 'If the setup caused the harshness, yes. Move the microphone and check the room first.')])

add(slug='how-to-check-an-audio-recording-before-you-edit', cluster='repair', kw='how to check audio recording quality',
    title='How to Check an Audio Recording Before You Edit It',
    desc='Check an audio recording before you edit: listen for noise, clipping, levels, dropouts and room sound, so you know which fixes are needed and which are not.',
    h1='How to Check an Audio Recording Before You Edit It',
    answer='Listen to the whole recording once without changing anything, then check for clipping, the level, background noise, dropouts and the room sound. Write down what you find, and only then choose the fixes. A check first saves time and stops you repairing problems that do not matter.',
    body='''
<p>Many editing sessions go wrong before the first change is made. The editor starts fixing things that do not matter, or misses a problem that will ruin the final file. A short, structured check at the start tells you what the recording needs, so each fix has a reason.</p>
<h2>Listen to the whole recording first</h2>
<p>Play the file from start to end, with headphones and at a comfortable volume. Do not change anything yet. Note where you hear a problem, including the start and end, the pauses and the edits. The first listen tells you the overall character of the recording.</p>
<h2>Check the peaks and clipping</h2>
<p>Look at the waveform for flat tops, which show clipping. Check the peak level, and the true peak if your tool shows it. Clipping cannot be fully repaired, so a clipped recording may need to be re-recorded or accepted with care.</p>
<h2>Check the level and the noise</h2>
<p>Listen to the quiet pauses. A steady hiss, hum or room noise will be obvious there. Check the level of the speech, and whether it changes between sections. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone post</a> explains how to use the quiet sections to judge the noise.</p>
<h2>Look for clicks, dropouts and mouth noise</h2>
<p>Zoom in on the waveform in a few places, looking for sharp spikes and flat gaps. Listen for mouth clicks, breath pops and sudden cut-outs. Write each one down, with its time, so you can find it again during the edit.</p>
<h2>Decide the order of fixes</h2>
<p>Fix the equipment-related problems first, such as clicks, dropouts and hum. Then clean the noise, level the voice, and only then add any tonal changes. Following this order stops later steps from spreading earlier problems.</p>
<h2>Limits</h2>
<p>A check gives you a plan, not a guarantee. Some problems only show on the final playback, and a fresh pair of ears often catches what you missed. If a recording has too many problems, re-recording is usually faster than repairing it.</p>
''',
    faq=[('How long should a check take?', 'A few minutes for a short clip. For a long recording, check in sections and note the problems as you go.'),
         ('Should I edit while I check?', 'No. Listen and note first, then edit. Changing things during the check makes it hard to judge.'),
         ('What is the most common problem?', 'Background noise and uneven levels are the most common. Clipping and clicks are also frequent.'),
         ('Does a checker tool replace listening?', 'No. A tool helps you see levels and peaks, but your ears judge the sound.')])

add(slug='how-to-repair-a-recording-with-a-voice-that-drifts', cluster='repair', kw='fix voice drifting in recording',
    title='How to Fix a Voice That Drifts Away From the Microphone',
    desc='Fix a voice that drifts away from the microphone during a recording: why the level and tone change, how to level and match the sections, and how to prevent it.',
    h1='How to Fix a Voice That Drifts Away From the Microphone',
    answer='A voice drifts when the speaker slowly moves away from the microphone or turns their head. The level falls and the tone thins. Level the sections, match the tone, and reduce the room noise that rises when the voice gets quieter. Prevent it next time with a fixed seat and a marker.',
    body='''
<p>A voice that drifts sounds fine at the start and then gets quieter and thinner as the speaker moves. It often happens in long takes, when people lean back, relax, or turn toward a second person. The change is gradual, which makes it easy to miss until playback.</p>
<h2>Why it happens</h2>
<p>Moving away from a microphone reduces the level and changes the tone. The voice loses its close, warm sound, and the room becomes more noticeable. Turning the head changes the angle, so consonants and high frequencies also shift. Each change is small, but together they make the sound feel like it moved.</p>
<h2>Level the sections</h2>
<p>Split the recording into a few sections, and level each one to match the start. Use small gain changes at the joins, and check each one by listening. The <a href="/tunedzy/blog/how-to-fix-uneven-volume-in-a-voice-recording">uneven volume post</a> shows the steps for a full level match.</p>
<h2>Match the tone</h2>
<p>When the distance has changed, the tone often changes too. A gentle low shelf can restore warmth to a section that thinned out. Match the tone section by section, rather than applying one setting to the whole take, so the start and end still sound alike.</p>
<h2>Reduce the room noise</h2>
<p>As the voice gets quieter, the room noise becomes more noticeable. Apply noise reduction gently to the quieter sections, or raise the level only after the noise is controlled. Keep the amount of reduction the same across sections, so the background does not change.</p>
<h2>Prevent it next time</h2>
<p>Mark the microphone position and the seat with tape. Place the microphone so the speaker can move slightly without changing the distance. Use a stand, a chair that does not roll, and a reminder to stay in place. Record shorter takes, so the drift has less time to build.</p>
<h2>Limits</h2>
<p>Repairing drift is slower than preventing it. Heavy levelling can make the sound unnatural, so keep each change small. If the drift is strong, re-record the section rather than repairing it.</p>
''',
    faq=[('Why does my voice get quieter over a long take?', 'The speaker often moves away or turns. Mark the position and take shorter breaks.'),
         ('Can levelling fix drift completely?', 'It can improve it a lot. It cannot fully restore the close, warm sound of a voice that moved away.'),
         ('Should I apply noise reduction to the whole take?', 'Apply it consistently, but check the quieter sections most carefully, because the noise shows there.'),
         ('What is the simplest prevention?', 'A fixed seat and a marker on the desk. It costs nothing and works every time.')])

add(slug='how-to-remove-a-mouth-noise-from-a-speech-recording', cluster='repair', kw='remove mouth noise from speech recording',
    title='How to Remove Mouth Noise From a Speech Recording',
    desc='Remove mouth noise from a speech recording: lip smacks, tongue clicks and saliva sounds, how to find them, and how to reduce them without losing the voice.',
    h1='How to Remove Mouth Noise From a Speech Recording',
    answer='Mouth noise includes lip smacks, tongue clicks and saliva sounds. Find each one by listening closely and zooming in, then cut or reduce it in a small area with a short fade. Prevent the most common sounds with water, a steady microphone position and short breaks.',
    body='''
<p>Mouth noise is one of the sounds that makes speech feel close and real, and too much of it makes a recording uncomfortable. A close microphone picks up every lip smack and tongue click, and a dry mouth makes them worse. The aim is to reduce the distracting ones while keeping the voice natural.</p>
<h2>What counts as mouth noise</h2>
<p>Common examples are lip smacks, which appear as short, sharp sounds at the start or end of words; tongue clicks, which are small, high-pitched ticks; and saliva sounds, which are wet or crackling noises. Breaths are a separate category, covered in the breath editing post. Knowing the type helps you choose the right fix.</p>
<h2>Find them by zooming in</h2>
<p>Listen once at normal speed, and note the moments that stand out. Then zoom in on the waveform, where mouth noise appears as a short spike or a small burst. Select the smallest area that covers the sound, so you do not touch the word around it.</p>
<h2>Reduce, do not erase</h2>
<p>Lower the mouth noise by a few decibels, or cut it with a short fade on each side. Aim for a sound that is quieter but still natural. Removing every trace of mouth sound makes the voice sound artificial, so accept that some natural sounds stay.</p>
<h2>Prevent the common ones</h2>
<ul>
<li>Drink water before the session and sip between takes.</li>
<li>Keep the microphone a steady distance, and slightly off-axis.</li>
<li>Relax the jaw and tongue, and avoid tensing the mouth.</li>
<li>Take short breaks, because a tired mouth makes more noise.</li>
</ul>
<h2>Limits</h2>
<p>Some people produce more mouth noise than others, and no editing will remove all of it. The goal is a pleasant, clear voice. If the mouth noise is constant, check your microphone position and your drinking habits before editing.</p>
''',
    faq=[('Should I remove every lip smack?', 'No. Remove the distracting ones and keep the natural sounds that make speech feel human.'),
         ('Does water help?', 'Yes, especially a sip before and between takes. Avoid taking a drink during a take.'),
         ('Can a pop filter reduce mouth noise?', 'It helps with plosive pops, but not much with clicks and lip smacks. Distance and technique matter more.'),
         ('Is mouth noise the same as breath?', 'No. Breaths are air, and mouth noise is the sound of lips, tongue and saliva. They are edited differently.')])
