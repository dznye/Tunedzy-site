"""Blog posts, batch 20: cleaning and restoring speech recordings (evergreen). Merged into content_blog.py.
Each post explains a clean-up job in steps, warns about over-processing and links to a tool or guide.
Settings are described generally because menus change between apps. No invented statistics.
Funnel: each post ends with a link to Tunedzy Go and to the matching free tool."""

CLUSTERS = {
    'evergreen-speech-clean': dict(tool='voice-recorder-noise-cancellation', label='Cleaning speech recordings', tool_name='Noise-Free Voice Recorder'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='how-to-remove-keyboard-noise-from-a-recording', cluster='evergreen-speech-clean', kw='how to stop keyboard noise on recordings',
    title='How to Remove Keyboard Noise From a Voice Recording',
    desc='How to remove keyboard noise from a voice recording: where the clicks come from, how to prevent them, and how to reduce what remains without damaging the voice.',
    h1='How to Remove Keyboard Noise From a Voice Recording',
    answer='Keyboard noise is the clicking and tapping picked up while you type during a recording. The best fix is prevention: move the microphone away from the keyboard, record between typing bursts, or use a quieter switch. What remains can be reduced with a gentle click-reduction or noise tool, checked carefully so the voice stays natural.',
    body='''
<p>Keyboard noise is one of the most common complaints in a home recording. A close microphone picks up every key press, and a narrator who types while speaking can fill a recording with clicks. The sound is sharp and repetitive, which makes it distracting even when the voice is clear. The good news is that most keyboard noise can be prevented, and what remains can be reduced with care.</p>
<p>This post explains where the sound comes from, how to stop it during recording, how to reduce it afterwards and when re-recording is the better choice. It is a common problem for podcasters, writers who narrate, and anyone who records while working at a computer.</p>
<h2>Where the sound comes from</h2>
<p>Keyboard noise travels in two ways. The key presses create sound in the air, which the microphone picks up directly. They also send vibration through the desk, which can reach the microphone stand and become a thump or a rumble. A close microphone on a desk is exposed to both, which is why the problem is worse when the microphone sits on the same surface as the keyboard.</p>
<p>Sharp, high clicks are the most noticeable. A low thud from a heavy key or a desk tap is easier to remove, but it can still be heard in quiet passages.</p>
<h2>Move the microphone away from the keyboard</h2>
<p>The simplest fix is distance from the source. Move the microphone further from the keyboard, or place it on a stand that is not connected to the desk. A boom arm that holds the microphone above and in front of the speaker separates it from the desk and keeps the keyboard out of the direct line. Keep the microphone close to the mouth, though, because moving too far away brings in more room sound.</p>
<p>If the keyboard must stay near the microphone, a soft pad under the stand can reduce the vibration that travels through the desk.</p>
<h2>Record between the typing</h2>
<p>For a narration, the cleanest approach is to stop typing while you speak. Write the script first, then record it without typing. If you must type during a recording, pause the take at each point where you touch the keys, and restart the sentence cleanly. A little planning makes the difference between a usable take and one that needs repair.</p>
<p>Many people find it easier to record in separate sessions, one for the script and one for the voice, so the two tasks do not compete.</p>
<h2>Use a quieter keyboard where you can</h2>
<p>Some keyboards are much quieter than others, and the difference matters for a recording. A keyboard with softer switches, or a silent option, reduces the click that reaches the microphone. Switching the keyboard is not always practical, but it is worth considering if you record often at the same desk. Test any change with a short recording before a long session.</p>
<h2>Reduce what remains</h2>
<p>If clicks remain after prevention, a click-reduction tool or a general noise reducer can help. Use the smallest setting that works, and listen to the result on headphones. Over-processing turns clicks into a watery or smeared sound that is harder to listen to than the clicks themselves. Sharp, isolated clicks can also be repaired by hand, by zooming in and smoothing each one with a very short fade.</p>
<p>Compare the processed version with the original. If the voice sounds thinner or the consonants soften, you have gone too far.</p>
<h2>When to re-record</h2>
<p>If the clicks are constant, loud or cover important words, re-recording the section is usually faster and gives a better result than repair. A short section recorded again in the right conditions will sound more natural than a long section cleaned heavily. Keep the good parts, and re-record only where the problem is worst.</p>
<h2>A simple checklist</h2>
<ol>
<li>Move the microphone away from the keyboard, and use a stand that does not share the desk.</li>
<li>Write the script before recording, so you can type less during the take.</li>
<li>Pause and restart each sentence where you must touch the keys.</li>
<li>Reduce any remaining clicks with the lightest setting, or by hand.</li>
<li>Listen on headphones and a phone, and re-record the worst sections.</li>
</ol>
<h2>Limits</h2>
<p>No tool removes keyboard noise perfectly, and a recording made while typing will always carry some trace of it. The aim is a recording where the clicks do not distract the listener. Prevention is far more effective than cure, so start there, and treat repair as the last step rather than the first.</p>
<h2>Start with a clean recording</h2>
<p>A clean take is easier to tidy. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can record voice-overs with live noise removal, or clean an existing recording. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the related problem of clicks in the mouth, read the <a href="/tunedzy/blog/how-to-remove-mouth-clicks-from-a-voiceover">mouth clicks post</a> in this series.</p>
''',
    faq=[('Can I remove keyboard clicks completely?', 'Rarely. Prevention works best. Repair reduces what remains, but a trace may stay.'),
         ('Is a boom arm worth it for this?', 'Often yes, because it separates the microphone from the desk and the keyboard.'),
         ('Should I type while recording?', 'Better not. Write the script first, then record it with few or no keystrokes.'),
         ('Does a quieter keyboard help?', 'Yes. Softer or silent switches reduce the sound that reaches the microphone.')])

add(slug='how-to-remove-air-conditioner-noise-from-a-recording', cluster='evergreen-speech-clean', kw='remove air conditioner noise recording',
    title='How to Remove Air Conditioner Noise From a Voice Recording',
    desc='How to remove air conditioner noise from a voice recording: switching it off, moving the microphone, choosing the right time and cleaning what remains.',
    h1='How to Remove Air Conditioner Noise From a Voice Recording',
    answer='Air conditioner noise is a steady hum or rush that sits under the voice. The best fix is to switch the unit off or record in another room. If that is not possible, record when it cycles off, place the microphone closer to the speaker, and reduce the steady noise gently afterwards.',
    body='''
<p>An air conditioner is one of the hardest household sounds to record around. It runs for long periods, its fan produces a steady rush, and its compressor adds a low hum. In summer, many home recordings are ruined by it. The noise is steady, so it is easier to reduce than sudden sounds, but it still lowers the clarity of the voice and tires the listener.</p>
<p>This post explains how to prevent the noise, how to choose the best time to record and how to clean what remains without making the voice sound thin.</p>
<h2>Switch it off, if you can</h2>
<p>The most effective fix is to turn the unit off for the length of the recording. A short break in the cooling is usually acceptable, especially if the room cools again afterwards. Plan the session around the time you can switch it off, and warn anyone else in the house. Ten or twenty minutes of quiet is often enough for a short episode or a voice-over.</p>
<p>Check that the room does not become uncomfortable during the session. Recording in a stuffy room is tiring for the speaker, and tired voices sound worse.</p>
<h2>Record in another room</h2>
<p>If the unit cannot be switched off, move to a room that is further from it, or on the other side of the house. The sound travels through walls, ducts and floors, so distance helps but does not solve the problem completely. A room with the door closed and the air vents sealed off is usually quieter. Test each room with a short recording before choosing.</p>
<h2>Choose the time</h2>
<p>Air conditioners cycle on and off, so there are often quiet periods. Record in the gap, starting just after the unit switches off. Keep the takes short enough to finish before it switches back on. A thermostat that you can set to delay the cycle can give you a longer window, if your system allows it.</p>
<h2>Move the microphone closer</h2>
<p>A microphone close to the mouth captures more of the voice and less of the room noise. Move the microphone a hand’s width or two from the speaker, and keep it steady. The closer position improves the signal-to-noise ratio, which makes the noise less noticeable. This is often the most effective change you can make without switching anything off.</p>
<h2>Clean the steady noise</h2>
<p>Steady noise, such as a fan hum, is one of the easier problems for a noise reducer. Record a few seconds of the air conditioner alone, so the reducer can learn its sound, then apply a gentle reduction to the voice. Keep the setting light, and listen for watery or thin speech. If the noise is strong, a heavy reduction will damage the voice, and a new recording is the better choice.</p>
<h2>Watch for the low hum</h2>
<p>The compressor may leave a low hum that is hard to hear on a laptop but obvious on headphones. Check the recording on good headphones, and listen to the quiet pauses. A high-pass filter can reduce very low rumble, but set it carefully so the warmth of the voice is not lost.</p>
<h2>A short routine</h2>
<ol>
<li>Plan the session around a switch-off window, or choose a quieter room.</li>
<li>Close the door and seal any vents you can reach.</li>
<li>Record a few seconds of the unit alone, as a noise sample.</li>
<li>Place the microphone close and steady, and record in short takes.</li>
<li>Apply a light reduction only if needed, and listen on headphones.</li>
</ol>
<h2>Plan around the unit&rsquo;s schedule</h2>
<p>Most air conditioners run on a thermostat, which means their noise is not random. The unit runs when the room is warm and rests when it is cool. Learn the pattern over a day or two by noting when the sound starts and stops. A simple schedule, written down, tells you the windows in which a take can be completed, and it lets you plan the session rather than waiting for the sound to drop.</p>
<p>If your home has a smart thermostat, check whether it can pause the cooling for a short period. Some models allow a temporary hold. Use that only where it is safe and comfortable, and never leave a room unventilated or too hot for the people in it.</p>
<p>When you finish a session, note the time the unit cycled and the length of each take, so the next session can be scheduled more accurately. Over a few weeks the pattern becomes clear, and planning gets quicker.</p>
<h2>Limits</h2>
<p>Some rooms and some units are too loud to fix after recording. If the noise is strong enough to mask the voice, re-record in a different time or place. Cleaning can reduce steady noise, but it cannot restore words that the noise has covered.</p>
<h2>Keep the voice natural</h2>
<p>A natural voice is the aim. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from an existing recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the wider background-noise picture, read the <a href="/tunedzy/blog/how-to-stop-fan-noise-on-my-microphone">fan noise post</a> in this series.</p>
''',
    faq=[('Can I just record during the cycle breaks?', 'Yes, if the breaks are long enough for the take. Keep the takes short.'),
         ('Does a closer microphone help?', 'Yes. A close position raises the voice above the room noise, which makes the hum less noticeable.'),
         ('Can noise reduction remove the hum completely?', 'Rarely. It reduces steady noise, but heavy settings damage the voice.'),
         ('Should I buy a noise reducer?', 'Only if you record often in the same noisy room. Prevention is usually cheaper and better.')])

add(slug='how-to-remove-tv-sound-from-a-recording', cluster='evergreen-speech-clean', kw='remove tv noise from recording',
    title='How to Remove TV Sound From a Voice Recording',
    desc='How to remove TV sound from a voice recording: why speech from a television bleeds into the microphone, how to prevent it and how to reduce what remains.',
    h1='How to Remove TV Sound From a Voice Recording',
    answer='TV sound in a recording is speech or music from a television that the microphone picks up. It is hard to remove because it sounds like voices. Prevent it by turning the television off or moving to another room, placing the microphone closer, and using headphones. What remains needs careful editing, not heavy noise reduction.',
    body='''
<p>Television sound is one of the most difficult interruptions in a home recording. It is not steady noise like a fan. It is speech, music and sound effects, and the microphone hears it as voices competing with your own. A quiet line of dialogue from a film in the next room can be enough to ruin a take, and noise reduction tools often struggle with it because it resembles the voice they are trying to protect.</p>
<p>This post explains why television sound is hard to fix, how to prevent it, how to clean what remains and when to re-record.</p>
<h2>Why it is hard to remove</h2>
<p>Most noise reducers work best on steady sound, because they can learn it and remove it. Television sound changes all the time, and much of it shares the frequencies of speech. A reducer that tries to remove it may also remove parts of your voice, or leave a warbling trace of the dialogue behind. That is why prevention matters so much.</p>
<h2>Switch it off or leave the room</h2>
<p>The most reliable fix is to turn the television off for the length of the session. If that is not possible, move to a room where the television cannot be heard, and close the door. Sound passes through walls, especially in older houses, so test the room with a short recording and listen for any leakage.</p>
<h2>Use headphones and a closer microphone</h2>
<p>Headphones help you hear what the microphone hears, and they can also reduce the television sound reaching your ears, which makes it easier to notice a leak. A closer microphone captures more of your voice and less of the room, so the television sound becomes quieter in the recording. Keep the distance steady, and place the microphone between you and the source of your voice, not toward the television.</p>
<h2>Choose the time</h2>
<p>If the household has a regular viewing time, record at another time of day. A quiet morning or a late evening may be far easier than the time when everyone is watching. Warn others in the house about the recording, and ask them to keep the sound down or move out of earshot.</p>
<h2>Edit what remains</h2>
<p>If a faint trace of the television remains, editing is usually better than heavy noise reduction. Cut the worst sections, and replace them with a short piece of room tone from the same recording, using a crossfade to hide the join. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone post</a> explains how to capture usable room tone.</p>
<p>For a long run of speech bleed, re-recording the passage is usually the better choice, because no repair will restore the voice cleanly.</p>
<h2>A simple checklist</h2>
<ol>
<li>Turn the television off, or move to a room where it cannot be heard.</li>
<li>Close the door and check the room with a short recording.</li>
<li>Place the microphone close, between you and your voice.</li>
<li>Record at a quiet time, and warn others in the house.</li>
<li>Edit the worst sections, and re-record any passage that is still unclear.</li>
</ol>
<h2>Talk to the household first</h2>
<p>Television is often the hardest interruption to plan around, because it belongs to shared time. Agree a recording window with everyone who uses the room, and explain what you need. A short, polite request works far better than an unplanned interruption, and most households will accommodate a fixed quiet period once they understand it. Write the window on a shared calendar, so nobody needs to be reminded.</p>
<p>If the television must stay on, ask for the volume to be lowered and for the set to be turned to a quieter channel or programme. Subtitles and a lower level often do more than moving to another room would.</p>
<p>Headphones make a difference here too. A recording made on speakers will pick up the television more easily than one made on headphones, so ask the speaker to wear headphones with the volume kept moderate. Check the quiet pauses in the recording for faint speech, since that is where television bleed is most obvious and hardest to remove.</p>
<p>If you record regularly in the same room, mark the spot where the television is least audible, and keep the microphone there for every session. Note that spot in your template, so the next session starts from it.</p>
<h2>Limits</h2>
<p>Some television sound will leak into almost any home recording. The goal is to reduce it below the level of the voice, so it does not distract the listener. For a professional recording, a dedicated room is the answer. For home work, prevention and editing are the practical tools.</p>
<h2>Keep the recording clean from the start</h2>
<p>A clean start saves hours of repair. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you already have, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the room side of the problem, read the <a href="/tunedzy/how-to-test-your-room-for-echo">room test guide</a>.</p>
''',
    faq=[('Can noise reduction remove TV dialogue?', 'Rarely cleanly. It often removes parts of the voice too, so prevention is better.'),
         ('What is the best fix?', 'Turn the television off or record in another room at a quiet time.'),
         ('Can I cut out the TV parts?', 'Yes, if they are short. Replace the cut with room tone and crossfade the join.'),
         ('Should I re-record?', 'If the television is clearly audible through a whole passage, yes. Repair will not restore it cleanly.')])

add(slug='how-to-clean-zoom-recording-for-publishing', cluster='evergreen-speech-clean', kw='clean zoom recording for publishing',
    title='How to Clean a Zoom Recording for Publishing',
    desc='How to clean a Zoom recording for publishing: getting the best local file, balancing the voices, reducing noise and echo, and checking the result before release.',
    h1='How to Clean a Zoom Recording for Publishing',
    answer='A video call recording is compressed and often uneven, but it can be cleaned for publishing. Record locally where possible, balance each voice, reduce steady noise and echo gently, and check the result on a phone. Expect limits: a call recording will not match a studio file, so set the expectations of the audience.',
    body='''
<p>Video calls are now a common source of interviews, panels and conversations that people want to publish. The recording tool is convenient, but the files are compressed, the voices can sound uneven and background noise is often mixed in. A call recording can still be cleaned into a listenable episode, provided you start with the best file available and keep the processing honest.</p>
<p>This post explains how to get the best file, how to balance and clean the voices, how to reduce the echo and noise without damaging the speech and what limits to expect when publishing a call.</p>
<h2>Get the best file you can</h2>
<p>The cloud recording of a call is a compromise. Many calling tools also allow each person to record locally, which gives a cleaner file with no network compression. Ask each participant to record their own side if the tool allows it, and to keep the recording running for the whole call. Local files can then be aligned later, which gives you a much better starting point than the shared file alone.</p>
<h2>Check the settings before the call</h2>
<p>Ask participants to use headphones, to sit in a quiet room and to keep a steady distance from the microphone. Turn on any noise setting the tool offers, but test it first, because it can make the voice watery. Check the connection, since a weak link causes dropouts that are very hard to repair.</p>
<h2>Balance the voices</h2>
<p>Call recordings often have one loud and one quiet speaker. Level each voice separately, using gain changes on each track if you have separate files. Aim for similar loudness across the speakers, and keep the natural variation within each voice. The <a href="/tunedzy/how-to-level-voices-between-speakers">levelling guide</a> covers the method in detail.</p>
<h2>Reduce the echo and noise gently</h2>
<p>If a participant hears their own voice through speakers, the recording may carry an echo. Asking that participant to use headphones is the best fix. Noise reduction should be light and used only on the parts that need it. Check the speech on headphones, and make sure the consonants still sound clear.</p>
<h2>Watch for the network glitches</h2>
<p>Dropouts, frozen audio and sudden jumps in level all come from the connection. Mark each glitch as you listen, and decide whether to cut, repair or re-record a short section. A glitch that repeats a word can often be removed by cutting, but a dropout that removes a word may need the speaker to repeat the line.</p>
<h2>Check the result before publishing</h2>
<p>Listen to the finished episode on headphones and on a phone speaker. Check that the voices are balanced, the noise is controlled and the speech is clear at a normal listening level. Check the loudness of the export with the <a href="/tunedzy/tools/lufs-meter">LUFS meter</a>, so the episode sits comfortably beside your other shows.</p>
<h2>Be honest about the source</h2>
<p>A call recording has a particular sound, and listeners may notice it. Tell them the episode was recorded on a call, so they know what to expect. That honesty builds trust, and it sets the right expectations for the sound.</p>
<h2>A simple workflow</h2>
<ol>
<li>Ask each participant to record a local copy, and keep it running.</li>
<li>Collect the local files and the shared recording, and align them.</li>
<li>Balance each voice, using gain on each track.</li>
<li>Clean lightly, marking and repairing the glitches.</li>
<li>Check on headphones and a phone, and export with a loudness check.</li>
</ol>
<h2>Make the local recording the master</h2>
<p>When you have local files from each participant, treat them as the master and the cloud file as a reference. Compare the two at the start of the episode, and use the local tracks for the final edit wherever they are cleaner. The cloud file remains useful for checking what was said, and for filling any gap where a local file failed. Keep both, and name them clearly, so the choice is always visible.</p>
<p>Aligning the tracks is a small but important step. Clap at the start of the recording, or ask each speaker to say a short phrase, then line the tracks up on that moment before you edit anything.</p>
<p>Test the full chain before the real call. Record a short conversation with the same people, using the same apps and connections, and listen to both local files and the shared recording. Problems with a microphone, a connection or a setting are far easier to fix on a test than in the middle of an important interview.</p>
<h2>Limits</h2>
<p>A call recording will never sound exactly like a studio recording. The compression, the network and the home rooms all limit the result. The aim is a clear, honest episode that listeners can follow without effort. Pushing the processing too far makes the voices sound odd, so keep the work light.</p>
<h2>Start with the best file</h2>
<p>The best starting point is a local recording. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean an existing recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For recording an interview on a call, read the <a href="/tunedzy/blog/how-to-record-a-phone-call-for-a-podcast">phone call post</a> in this series.</p>
''',
    faq=[('Can I publish a Zoom recording?', 'Yes, with the right consent and a clean edit. Tell listeners it was recorded on a call.'),
         ('Is the cloud file good enough?', 'Often it is a compromise. A local recording from each person is usually better.'),
         ('What is the biggest problem?', 'Echo from speakers and network dropouts. Headphones and a stable connection prevent most of both.'),
         ('Should I use the noise setting?', 'Test it first, and keep it light, because it can make the voice watery.')])

add(slug='how-to-clean-a-noisy-interview-audio', cluster='evergreen-speech-clean', kw='clean noisy interview audio',
    title='How to Clean a Noisy Interview Recording Without Ruining It',
    desc='How to clean a noisy interview: assess the damage, fix faults first, reduce noise gently and know when a recording is not worth saving.',
    h1='How to Clean a Noisy Interview Recording Without Ruining It',
    answer='Clean a noisy interview in a fixed order: assess the damage first, fix equipment faults, then reduce steady noise gently, then balance the voices and finally check the result. Over-cleaning makes the guest sound distant or watery, so keep each step light, and accept that a very noisy recording may not be worth saving.',
    body='''
<p>An interview recorded in a noisy place is a common problem. A café, a street, a busy office or a room with a fan can bring so much background into the recording that the guest is hard to hear. The temptation is to push the cleanup hard, and that often damages the voice more than the noise. A careful approach, in the right order, can save many recordings that a heavy-handed edit would ruin.</p>
<p>This post shows how to assess the damage, the order of the fixes, how to reduce noise gently and how to decide when a recording is not worth saving.</p>
<h2>Assess the damage first</h2>
<p>Before any cleaning, listen to the whole interview on headphones, and note the problems. Is the noise steady or sudden? Are the voices clear or muffled? Is the level even, or does it drop when the guest turns away? Are there clicks, dropouts or clipping? Write each problem down with its time, so you know what to fix and in what order.</p>
<p>The assessment also tells you whether the recording is worth saving. If the guest is hard to understand for long stretches, the time spent may not be justified.</p>
<h2>Fix the equipment faults first</h2>
<p>Clicks, dropouts and hum usually come from equipment or connections. Repair them before any noise reduction, because a noise reducer will spread a click into a smear, and it cannot remove a dropout. Use the targeted methods for each fault, such as cutting a click or filling a dropout with room tone.</p>
<h2>Reduce steady noise gently</h2>
<p>Steady noise, such as a fan or traffic hum, can be reduced with a noise reducer. Capture a short sample of the noise alone, if you have one, and apply a light reduction to the interview. Listen to the quiet pauses and the guest’s consonants. If the voice becomes thin or watery, reduce the amount, or accept more noise rather than a damaged voice.</p>
<h2>Balance the voices</h2>
<p>An interview in a noisy place often has a guest who was far from the microphone and a host who was close. Balance the two so they sit together, using gain changes on each voice. Keep the guest’s natural variation, and avoid lifting the quiet passages so far that the room noise rises with them.</p>
<h2>Check the result</h2>
<p>Listen to the finished interview on headphones, then on a phone speaker, at a normal volume. Check that the guest can be understood throughout, that the noise is controlled and that the voices are balanced. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can check the loudness of the export against your target.</p>
<h2>When to re-record the questions</h2>
<p>If a key answer is covered by noise, consider asking the guest to answer it again, perhaps in a quieter setting. A short re-recorded answer, clearly marked for the edit, is often better than a long repair. Be open with the guest about why you are asking, and keep the re-recording short.</p>
<h2>When the recording is not worth saving</h2>
<p>Some recordings are too damaged to save. If the guest is hard to hear for most of the interview, or if a vital part is lost to noise, a short summary or a written follow-up may be a better outcome. Decide early, and tell the guest what you plan to do.</p>
<h2>Keep the guest comfortable through the edit</h2>
<p>A guest who sounds poor on a recording may feel embarrassed, even when the problem came from the room. Explain what you plan to do before you send the edit, and let them hear the version you intend to publish. A guest who understands the process is more forgiving of the limits, and more likely to agree to a short re-record of a key answer.</p>
<p>Keep the guest&rsquo;s approval in writing if you change the content in any significant way, such as cutting an answer or moving sections. A short email confirming the agreed version protects both of you.</p>
<p>Keep the cleanup of each section separate, so a mistake in one part does not spread through the whole interview. Process the questions and answers in order, listening to each before moving on, and save a copy of each stage. If a later change damages the sound, you can return to the last good stage rather than starting from the raw recording again.</p>
<h2>Limits</h2>
<p>No tool recovers speech that noise has covered. The best cleanup keeps the voice natural and removes only what distracts. A recording made in the right place will always be easier to clean than one made in a noisy one.</p>
<h2>Start with the best recording</h2>
<p>The best recording is the one made well. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from an existing file, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the step-by-step process, read the <a href="/tunedzy/blog/how-to-cut-a-podcast-from-a-long-recording">long recording guide</a> in this series.</p>
''',
    faq=[('Should I clean the noise first or the clicks first?', 'Clicks and faults first, then steady noise, so the noise reducer does not smear them.'),
         ('How much noise reduction is too much?', 'When the guest sounds thin, watery or distant. Reduce the amount and accept some noise.'),
         ('Can I ask the guest to re-answer?', 'Yes, in a quieter setting, and keep it short. Tell the guest why you are asking.'),
         ('When should I give up on a recording?', 'When a large part is lost to noise and no repair will make it understandable.')])

add(slug='how-to-remove-hiss-from-old-recordings', cluster='evergreen-speech-clean', kw='remove hiss from old recording',
    title='How to Remove Hiss From Old Recordings Without Losing the Voice',
    desc='How to remove hiss from old recordings without losing the voice: capturing a noise profile, reducing gently and the limits of restoration.',
    h1='How to Remove Hiss From Old Recordings Without Losing the Voice',
    answer='Hiss in old recordings is a steady high-frequency noise from tape, electronics or the original equipment. Capture a sample of the hiss in a silent passage, reduce it gently with a noise profile, and stop before the voice thins. Very old or damaged recordings may need a specialist, and some hiss is part of the recording’s character.',
    body='''
<p>Old recordings, from tapes, early digital files or family voice notes, often carry a steady hiss. The sound is high and thin, and it can hide the voice, especially in the quiet passages. Removing it is one of the most satisfying restoration jobs, but it is also one where it is easy to damage the voice. A careful approach keeps the speech natural, and it accepts that some hiss will remain.</p>
<p>This post explains where hiss comes from, how to capture a noise profile, how to reduce it gently and when a specialist is the better route.</p>
<h2>Where the hiss comes from</h2>
<p>Hiss can come from several sources: the magnetic medium in a tape, the electronics of the original recorder, or the amplifier and cables used to play the recording back. Each has a steady, broadband character, which is why it sits across the frequency range rather than in a single band. The older the recording, the more hiss tends to be present.</p>
<p>Understanding the source helps you decide what is possible. Some hiss is part of the original sound, and removing all of it can make the recording feel artificial.</p>
<h2>Capture a noise profile</h2>
<p>A noise profile is a sample of the hiss alone. Find a silent passage in the recording, such as a pause between speakers or the lead-in before the first word, and capture a few seconds of it. Many noise reducers use this sample to learn the hiss, and then reduce it throughout. Choose the quietest passage you can find, and make sure it contains no speech.</p>
<h2>Reduce gently</h2>
<p>Apply the reduction in small steps, and listen after each one. Start with a light setting, and increase it only until the hiss is noticeably reduced without the voice becoming thin. A common mistake is to remove the hiss completely, which leaves the speech sounding hollow and robotic. The goal is a quieter background, not silence.</p>
<h2>Watch the high frequencies</h2>
<p>Hiss lives in the high frequencies, and the speech also has important high-frequency detail in consonants. Heavy reduction in the top range can make the words sound dull and muffled. Listen to the sibilant sounds, the s and t sounds, and keep them clear. If they become soft, reduce the amount.</p>
<h2>Restore the balance</h2>
<p>After reducing the hiss, the recording may sound thinner. A gentle lift in the presence range can restore clarity, and a light low-end boost can restore warmth. Make small changes, and compare the result with the original at the same level. The <a href="/tunedzy/blog/how-to-fix-a-tinny-voice-recording">tinny voice post</a> covers the balance in more detail.</p>
<h2>When to use a specialist</h2>
<p>Badly damaged tapes, warped discs or recordings with serious distortion are often better handled by a specialist audio restoration service. They have tools and experience that a home setup may not match. For a family or archive recording of real importance, consider that route, and keep an untouched copy of the original.</p>
<h2>A simple workflow</h2>
<ol>
<li>Make a safe copy of the original file, and never work on it directly.</li>
<li>Capture a noise profile from the quietest silent passage.</li>
<li>Reduce the hiss in small steps, listening after each one.</li>
<li>Restore clarity and warmth with gentle EQ if the voice has thinned.</li>
<li>Compare with the original at the same level, and keep the best version.</li>
</ol>
<h2>Document every change</h2>
<p>A restoration is only as trustworthy as its record. Keep a short log of each step: the settings used, the noise profile chosen, the repairs made and the versions produced. The log lets you reproduce the work, explain it to family members, and correct a mistake without starting again. It also helps the next person who inherits the files, who may want to know exactly what was changed from the original.</p>
<p>Store the log with the files, not in a separate place where it may be lost.</p>
<p>Many restorations are shared with family, so think about who will hear the result. A version that is clear enough for a family gathering may not suit an archive, and the other way round. Decide the purpose first, and set the level of restoration to match it, rather than aiming for an abstract idea of perfection.</p>
<h2>Limits</h2>
<p>Restoration has limits. Hiss can be reduced, but a very noisy or damaged recording cannot be made as clean as a modern one. Some character is lost in any restoration, and some is worth keeping. Judge the result by how well the voice can be understood and enjoyed, not by how silent the background becomes. A restoration that people return to is a better outcome than one that sounds perfect for a moment.</p>
<h2>Keep the original safe</h2>
<p>Always keep the original recording untouched. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean an existing recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the backup routine that protects an original, read the <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup post</a> in this series.</p>
''',
    faq=[('Can I remove all the hiss?', 'Usually not without damaging the voice. Reduce it to a level that does not distract.'),
         ('What is a noise profile?', 'A short sample of the hiss alone, used by the reducer to learn the noise.'),
         ('Why does my restored voice sound hollow?', 'The reduction was too strong. Lower the amount and restore some presence.'),
         ('Should I use a specialist?', 'For damaged or important recordings, yes. Keep an untouched copy of the original either way.')])

add(slug='how-to-restore-old-voice-memos', cluster='evergreen-speech-clean', kw='restore old voice memos',
    title='How to Restore Old Voice Memos and Family Recordings',
    desc='How to restore old voice memos and family recordings: checking the source file, making a safe copy, cleaning gently and deciding what to keep.',
    h1='How to Restore Old Voice Memos and Family Recordings',
    answer='Restore an old voice memo by first making a safe copy of the original file, then checking its format and quality, cleaning hiss and noise gently, and restoring clarity with light EQ. Keep the untouched original. For fragile or irreplaceable recordings, a specialist may be the better choice.',
    body='''
<p>Old voice memos and family recordings are often the most precious audio a person owns. A grandparent’s voice on a cassette, a message on an early digital recorder, or a phone file from years ago can carry meaning that no modern recording could replace. These files also tend to be fragile, noisy and stored in formats that are hard to play. Restoring them is a careful job, and the first rule is to protect the original.</p>
<p>This post walks through the restoration process in order, from the first safety step to the final decision about what to keep. It is written for people working on personal recordings, not for professional archives, although many of the principles apply to both.</p>
<h2>Protect the original first</h2>
<p>Before you open the file in any editor, make a complete copy of it, and store the copy somewhere separate. Keep the original untouched, even if it seems perfectly playable. Original files can be damaged by a bad edit or a failed transfer, and a copy you work on is always replaceable while an original is not. Label the copy clearly, with the date and what you did to it.</p>
<p>If the source is a physical medium such as a tape or a disc, consider making the first digital copy with a professional service or with careful equipment, since the playback itself can damage fragile media.</p>
<h2>Check the format and the quality</h2>
<p>Look at what the file is: its format, sample rate, bit depth and whether it is mono or stereo. Some old files use compressed formats or unusual sample rates, which can cause playback problems. Convert to a standard format for working, but keep the original format in the archive. Listen to the whole file once, without changing anything, and note the problems you hear: hiss, hum, clicks, dropouts, distortion and any sections that are very quiet.</p>
<h2>Fix the equipment faults first</h2>
<p>Clicks, dropouts and hum usually come from the original recording or the playback chain. Repair them before cleaning the noise, because a noise reducer can smear a click into a smudge and cannot restore a dropout. Cut the clicks by hand, and fill any short dropout with a piece of room tone from the same recording.</p>
<h2>Reduce the noise gently</h2>
<p>Hiss and background noise can be reduced with a noise profile, captured from a quiet passage, as described in the <a href="/tunedzy/blog/how-to-remove-hiss-from-old-recordings">hiss post</a> in this series. Apply the reduction in small steps. The aim is a quieter background, not silence, because complete removal makes the voice sound hollow and artificial. Keep an ear on the consonants, which carry the clarity of speech.</p>
<h2>Restore clarity and warmth</h2>
<p>Noise reduction can thin a voice, so a light restoration of presence and warmth often helps. Use small changes, and compare with the original at the same level. A gentle lift in the presence range can bring back the clarity of the words, and a light low boost can restore the body of the voice. Stop before the sound becomes artificial.</p>
<h2>Level the sections</h2>
<p>Old recordings often have uneven levels, with quiet passages that are hard to hear and loud ones that jump out. Level the sections with gain changes, rather than heavy compression, so the natural expression survives. The goal is that a listener can hear the whole recording without adjusting the volume.</p>
<h2>Decide what to keep</h2>
<p>Restoration is a set of choices, and not every change is an improvement. Some hiss and roughness belong to the recording’s character, and a family may want to keep the sound of the original machine. Keep two versions: a restored one for listening and the untouched original for the archive. Note what you changed, so the next person can understand the work.</p>
<h2>When to use a specialist</h2>
<p>A badly damaged tape, a warped disc or a recording of irreplaceable importance may need a professional restoration service. Specialists have tools and experience that home equipment rarely matches. Ask what they will do to the original, and make sure they keep it safe and return it to you.</p>
<h2>A simple workflow</h2>
<ol>
<li>Make a safe copy of the original, and store it separately.</li>
<li>Check the format, and listen to the whole file once.</li>
<li>Repair clicks and dropouts by hand.</li>
<li>Reduce the noise gently, using a profile from a quiet passage.</li>
<li>Restore clarity, level the sections and keep the original for the archive.</li>
</ol>
<h2>Limits</h2>
<p>Restoration cannot make an old recording sound like a modern studio file, and it should not try to. The aim is to make the voice clear and the words easy to follow, while keeping the character that makes the recording meaningful. Some loss is unavoidable, and the best result is one the family is happy to listen to.</p>
<h2>Keep the original safe</h2>
<p>The original is the most important file in the project. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean an existing recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the backup routine that protects the original and its copies, read the <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup post</a> in this series.</p>
''',
    faq=[('Should I work on the original file?', 'Never. Make a copy first, and work only on the copy.'),
         ('Can I restore a file that will not play?', 'Sometimes, by converting the format. If it is damaged, a specialist may be needed.'),
         ('How much should I clean?', 'Enough that the words are clear. Keep some character, and keep the original.'),
         ('What should I do with a fragile tape?', 'Consider a professional service, since playback itself can damage the medium.')])

add(slug='speech-enhancement-explained', cluster='evergreen-speech-clean', kw='speech enhancement explained',
    title='Speech Enhancement Explained: What It Does and What It Cannot Do',
    desc='Speech enhancement explained: what the term covers, how it differs from noise reduction, the common settings and the limits that matter for recorded speech.',
    h1='Speech Enhancement Explained: What It Does and What It Cannot Do',
    answer='Speech enhancement is a set of processes that make speech clearer, usually by reducing background noise, emphasising the voice and smoothing the level. It is broader than noise reduction. It helps most when the speech is already reasonably clear, and it can make a voice unnatural when pushed too far.',
    body='''
<p>Speech enhancement is a term that appears in phone settings, call apps, recording tools and research papers. It describes processes that make speech easier to hear, but the exact meaning depends on the tool. Some tools only reduce noise, others also boost the voice or even out the level. Understanding what the term covers helps you choose the right setting and avoid the damage that comes from using too much.</p>
<p>This post explains the main parts of speech enhancement, how they relate to noise reduction, what they can and cannot do, and how to use them with restraint.</p>
<h2>What the term covers</h2>
<p>Speech enhancement is an umbrella term. It can include noise reduction, which removes background sound, and voice emphasis, which boosts the frequencies that carry speech clarity. It can also include level control, which evens out loud and quiet passages, and echo reduction, which softens reflections. Each part does a different job, and a tool may combine several of them.</p>
<p>When a product says it enhances speech, check which of these processes it applies. The label alone does not tell you how strong the change is.</p>
<h2>How it differs from noise reduction</h2>
<p>Noise reduction is one part of speech enhancement, and it focuses on reducing unwanted sound. Speech enhancement may go further by reshaping the voice itself. A noise reducer makes the background quieter. A speech enhancer may also change the tone of the voice so it cuts through better. Both can change the sound, and both need care.</p>
<h2>What it does well</h2>
<p>Speech enhancement works best when the speech is already reasonably clear and the problem is background noise or a distant voice. It can make a phone call easier to follow, clean up a casual recording and improve the clarity of a voice that was quiet in the mix. For many everyday recordings, a light enhancement is a useful finishing step.</p>
<h2>What it cannot do</h2>
<p>Enhancement cannot restore words that were never recorded. If the speech is buried under loud noise, or the voice was far from the microphone, the processing has little clear sound to work with, and the result will be artificial. Enhancement also cannot fix clipping, which permanently removes the peaks of a sound.</p>
<h2>The common risks</h2>
<ul>
<li>A watery or metallic voice, from strong noise reduction.</li>
<li>A thin voice, from removing too much low and middle frequency.</li>
<li>A squashed voice, from heavy level control.</li>
<li>Artefacts on consonants, from aggressive processing.</li>
<li>A robotic or unnatural tone, from stacking several processes.</li>
</ul>
<h2>Use it with restraint</h2>
<ol>
<li>Start with the lightest setting that solves the problem you can hear.</li>
<li>Apply one process at a time, and listen after each one.</li>
<li>Compare with the original at the same level, on headphones and a phone.</li>
<li>Stop when the voice sounds natural, even if some noise remains.</li>
<li>Keep the original, so you can compare or start again.</li>
</ol>
<h2>Enhancement in calls and streams</h2>
<p>Calling and streaming apps often apply enhancement automatically, and the settings may be hidden behind a single switch. The processing is designed for speed rather than for the best sound, so it can be more aggressive than a careful edit would be. If a listener says your voice sounds odd on a call, check whether an enhancement setting is turned on, and test with it off before deciding.</p>
<p>The same caution applies to streaming. A live enhancement that suits a quiet game may damage a voice in a noisy room. Test the setting with the actual environment, not only in the studio.</p>
<h2>Judging enhancement by ear</h2>
<p>When you compare enhanced and unenhanced versions, listen for the words that matter most rather than for the overall impression. The best test is whether a stranger can understand a difficult sentence easily in each version. If the enhanced version is clearer for that sentence without sounding artificial elsewhere, it is doing its job. If it is only louder or only quieter, it is not.</p>
<p>Listen on the device your audience uses, and at the level they are likely to choose. Enhancement that sounds clear at high volume on headphones can sound harsh on a phone speaker.</p>
<p>A simple rule for enhancement is that it should be invisible. If a listener notices the processing before they notice the content, the setting is too strong. The goal is a voice that is easy to follow and comfortable to hear, with no reminder that the sound has been changed.</p>
<h2>Limits</h2>
<p>Speech enhancement tools differ widely in their methods and their strength, and their results depend on the recording. No tool is right for every voice or room. Test on your own material, and be ready to accept a small amount of noise rather than a damaged voice.</p>
<h2>Start with a clean recording</h2>
<p>The best enhancement starts with a good recording. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the noise side of the same question, read the <a href="/tunedzy/blog/how-much-noise-reduction-is-too-much">noise reduction limits post</a> in this series.</p>
''',
    faq=[('Is speech enhancement the same as noise reduction?', 'Noise reduction is one part of it. Enhancement can also reshape the voice and even the level.'),
         ('Why does my enhanced voice sound robotic?', 'Too many processes or too strong a setting. Use one light process at a time.'),
         ('Can it rescue a distant voice?', 'Only partly. Distance changes the sound in ways enhancement cannot fully restore.'),
         ('Should I always enhance?', 'No. Enhance when it helps, and skip it when the recording is already clear.')])

add(slug='how-much-noise-reduction-is-too-much', cluster='evergreen-speech-clean', kw='how much noise reduction is too much',
    title='How Much Noise Reduction Is Too Much for a Voice?',
    desc='How much noise reduction is too much for a voice: warning signs of over-processing, a simple test and why a little noise is often better.',
    h1='How Much Noise Reduction Is Too Much for a Voice?',
    answer='Noise reduction is too much when the voice sounds thin, watery, distant or robotic, or when consonants soften and words run together. A little residual noise is usually better than a damaged voice. Test the amount by comparing the processed and original versions at the same level, and stop as soon as the voice starts to change.',
    body='''
<p>Noise reduction is one of the most useful tools in voice recording, and one of the easiest to overuse. A slider that promises a silent background is tempting, but silence is rarely the goal. A voice that has been pushed too hard sounds artificial, tiring and harder to understand than a voice with some noise left in it. The question is not how quiet the background can become, but how much noise the listener will accept without losing the speech.</p>
<p>This post sets out the warning signs of over-processing, a simple way to test the amount, and why listeners usually prefer a little noise to a damaged voice.</p>
<h2>What the processing does to a voice</h2>
<p>Noise reduction estimates which parts of the signal are noise and reduces them. The estimate is never perfect, so some speech is reduced along with the noise. The more the processing reduces, the more of the voice it takes with it. That is why a strong setting changes the sound of the voice itself, and not only the background.</p>
<p>The loss falls mainly on quiet sounds, such as soft consonants and breaths, and on the subtle tones that give a voice its body. Those are exactly the details that make speech feel natural and warm.</p>
<h2>Warning signs</h2>
<ul>
<li>The voice sounds thin, as though the low body has been removed.</li>
<li>The voice sounds watery, metallic or bubbly, especially on sustained vowels.</li>
<li>The consonants soften, so “t” and “s” become hard to hear.</li>
<li>The breaths disappear, which makes the speaker sound unnaturally smooth.</li>
<li>The voice seems to move in and out with the background, a pumping effect.</li>
</ul>
<h2>A simple test</h2>
<ol>
<li>Play the original and the processed version, at the same level, one after the other.</li>
<li>Listen to a sentence with soft consonants and a sustained vowel.</li>
<li>Reduce the amount, and listen again, until the voice sounds like the original.</li>
<li>Check the quiet pauses, where the processing is most obvious.</li>
<li>Stop at the point where the noise is acceptable and the voice is intact.</li>
</ol>
<h2>Why a little noise is often better</h2>
<p>A listener adapts to a steady background quickly, and the brain filters it out after a few moments. A damaged voice is harder to adapt to, because its changes are unpredictable and unnatural. Many listeners find a recording with a faint, steady hiss more comfortable than one that sounds processed. The aim is comfort, and that usually means accepting some noise.</p>
<h2>Use other fixes first</h2>
<p>Before increasing the noise reduction, check the cause. A microphone further away, a louder room or a poor connection will all raise the noise, and a stronger setting will only damage the voice further. Moving closer, adding soft surfaces or fixing the source is always better than pushing the processing harder.</p>
<h2>When to stop</h2>
<p>Stop when the voice sounds natural and the background is no longer distracting. Do not chase perfect silence. If the recording still has too much noise, re-recording is often better than repairing it, especially for a long passage.</p>
<h2>Listen for the fatigue</h2>
<p>Some damage from over-processing is not obvious in a short clip. It shows up over minutes, as listener fatigue. A voice that is slightly too smooth or too thin can be tiring to hear for half an hour, even when a short sample sounds fine. Listen to a longer section, ideally a complete episode, before you settle on a setting. If you find yourself wanting to turn the volume up or to stop early, the processing may be too strong.</p>
<p>A useful habit is to take a break and listen again after an hour. A setting that still feels comfortable after a break is far more likely to suit the whole recording than one that only sounds good in the first minute.</p>
<p>Keep a written note of the amount you chose for each recording, together with the noise it was set for. When a later recording has a similar problem, the note gives you a starting point, and you can avoid repeating the trial and error that led to the first decision. Share the note with anyone who edits the same files later, because it saves them the same search and keeps the sound consistent across the archive.</p>
<h2>Limits</h2>
<p>How much reduction is right depends on the voice, the noise and the listener. A quiet voice in a loud room needs more care than a clear voice with a light hum. Judge by ear, on the devices your audience uses, and accept that a balance is the goal rather than a perfect result.</p>
<h2>Test on your own recording</h2>
<p>A side-by-side test is the best guide. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the speech-enhancement side of the same question, read the <a href="/tunedzy/blog/speech-enhancement-explained">speech enhancement post</a> in this series.</p>
''',
    faq=[('Is some background noise acceptable?', 'Yes. A faint, steady background is often more comfortable than a damaged voice.'),
         ('How do I know I have gone too far?', 'The voice sounds thin, watery or robotic, or consonants soften. Reduce the amount.'),
         ('Should I aim for silence?', 'No. Aim for a voice that sounds natural with the background no longer distracting.'),
         ('What is the first thing to fix instead?', 'The cause: distance, room or connection. Fix those before raising the processing.')])

add(slug='how-to-remove-clothing-rustle-from-a-recording', cluster='evergreen-speech-clean', kw='remove clothing rustle from recording',
    title='How to Remove Clothing Rustle From a Recording',
    desc='How to remove clothing rustle from a recording: why clothes rub against a microphone, how to prevent it with placement and fabric, and how to reduce what remains.',
    h1='How to Remove Clothing Rustle From a Recording',
    answer='Clothing rustle is the crackling or swishing caused by fabric rubbing against a microphone, especially a clip-on. Prevent it by choosing still, smooth clothing, placing the microphone where fabric cannot touch it, and securing it firmly. What remains can be reduced with careful editing, but prevention is far more effective.',
    body='''
<p>Clothing rustle is one of the most frustrating problems for a clip-on microphone. A shirt, a jacket, a scarf or a coat can brush the capsule every time the speaker moves, and the result is a crackle that drowns out the voice. The sound is sharp and irregular, which makes it hard to remove afterwards. Most of the problem can be prevented with a few simple choices about where the microphone sits and what the speaker wears.</p>
<p>This post explains why rustle happens, how to prevent it, how to reduce what remains and when re-recording is the better choice.</p>
<h2>Why rustle happens</h2>
<p>A microphone is sensitive, and it picks up any movement of the material that touches it. Fabric that slides across the capsule creates friction, which the microphone turns into noise. Rough, loose or synthetic fabrics are the worst, because they catch and release. The closer the microphone is to the fabric, the louder the rustle will be.</p>
<p>Movement is the trigger. A still speaker may produce no rustle at all, while someone who gestures, turns or leans will produce a lot.</p>
<h2>Choose the position carefully</h2>
<p>The best position is where fabric cannot reach the microphone. For a clip-on, that means clipping it to a part of the clothing that does not move, such as a firm collar edge or a lapel, and keeping it clear of the jacket front and the scarf. Some people place the microphone higher, near the collar, where the fabric is more stable. Test a few positions while the speaker moves naturally.</p>
<h2>Choose the clothing</h2>
<p>Smooth, close-fitting clothing rustles less than loose, textured or crinkly fabric. A shirt with a firm collar, or a top with a stable neckline, gives the microphone a clean place to sit. Avoid scarves, lanyards and necklaces near the microphone, because they swing and catch. Ask guests to wear something similar, if you are recording a group.</p>
<h2>Secure the cable and the microphone</h2>
<p>A loose cable pulls on the microphone, and the movement transmits to the capsule. Tape or clip the cable so it has slack but cannot tug. Make sure the microphone clip is firm, so the microphone does not slide. A foam windscreen can also reduce contact noise, because it adds a buffer between the fabric and the capsule.</p>
<h2>Test before recording</h2>
<p>Record a short test while the speaker moves naturally: turns the head, leans forward, gestures and sits back. Listen on headphones for rustle, and adjust the position or the clothing until the test is clean. A test takes a few minutes, and it prevents a session full of crackle.</p>
<h2>Reduce what remains</h2>
<p>If a little rustle remains, reduce it with careful editing. Zoom in on each crackle, cut it or smooth it with a very short fade, and check that the voice around it still sounds natural. Broad noise reduction will not remove rustle well, because the sound is irregular and sharp. Heavy processing also damages the voice.</p>
<h2>When to re-record</h2>
<p>If the rustle is constant or covers important words, re-recording the section is usually better than repair. A short retake in the right position will sound more natural than a long passage with many repairs.</p>
<h2>A simple checklist</h2>
<ol>
<li>Clip the microphone to a stable part of the clothing, away from fabric that moves.</li>
<li>Choose smooth, close-fitting clothing, and avoid swinging accessories.</li>
<li>Secure the cable so it has slack and cannot pull.</li>
<li>Test while the speaker moves naturally, and adjust.</li>
<li>Repair any remaining crackle by hand, and re-record the worst sections.</li>
</ol>
<h2>Rehearse the movements</h2>
<p>Most rustle comes from movements the speaker does not notice. Before a long recording, ask the speaker to talk through a short passage while doing the things they normally do: reaching for water, turning to a colleague, leaning on the chair. Listen to the rehearsal and identify the movements that cause trouble. Then agree a simple habit, such as keeping the arms still or resting them on the table, that the speaker can keep during the real take.</p>
<p>Explain the reason behind the habit. A speaker who understands why a movement matters will be more likely to remember it, and less likely to feel criticised.</p>
<p>Finally, check the rustle on the first minute of playback, since that is where a listener forms their impression. A clean start makes the rest of the recording easier to trust, even when small problems remain later on.</p>
<h2>Limits</h2>
<p>Some rustle is very hard to avoid with a clip-on, especially for speakers who move a lot. In those cases, a boom or desk microphone may be the better choice. Prevention works best, and repair should be the last step, not the first.</p>
<h2>Keep the voice clean</h2>
<p>A clean signal starts with the right placement. The <a href="/tunedzy/blog/clip-on-microphone-for-phone-recording">clip-on microphone post</a> in this series covers placement in more detail. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings.</p>
''',
    faq=[('Why does my clip-on rustle when I move?', 'Fabric is sliding across the capsule. Move the microphone to a stable part of the clothing.'),
         ('Which fabrics cause the most rustle?', 'Loose, textured and crinkly fabrics are the worst. Smooth, close-fitting clothing is quieter.'),
         ('Can I remove rustle completely in editing?', 'Rarely. Prevention works best, and repairs leave a trace if the rustle is heavy.'),
         ('Should I use a boom microphone instead?', 'For speakers who move a lot, often yes. A boom avoids the fabric contact altogether.')])
