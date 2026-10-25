"""Blog posts, batch 17: live streaming audio. Merged into content_blog.py.
Platform rules and tool behaviour are described generally, because they change. No invented statistics and no
claims about how any product works beyond what the product's own description says. Funnel: each post ends with a link
to Tunedzy Go and to the matching free tool."""

CLUSTERS = {
    'trend-streaming': dict(tool='clean-streaming-mic', label='Live streaming audio', tool_name='Clean Streaming Mic'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='live-streaming-audio-setup-2027', cluster='trend-streaming', kw='streaming audio setup 2027',
    title='Live Streaming Audio Setup for 2027: What to Plan Now',
    desc='Live streaming audio setup for 2027: the microphone, the room, the routing and the processing choices to plan now, with a practical order of priorities.',
    h1='Live Streaming Audio Setup for 2027: What to Plan Now',
    answer='A good live streaming audio setup in 2027 starts with a close, steady microphone in a quiet room, then clean routing, sensible processing and a monitoring habit. Plan the setup in that order. The equipment matters less than the position, the room and the checks you run before each stream.',
    body='''
<p>Streamers often start by buying equipment, and then wonder why their audio still sounds poor. The microphone is rarely the main problem. Most streams that sound bad suffer from distance, a noisy room, a mix that is too loud or too quiet, and a routing setup that nobody has tested. Planning the setup in the right order saves money and makes the stream sound better from the first minute.</p>
<p>This guide is about what to plan for the next year, rather than a list of products. The principles stay steady even as tools change, so a setup built on them will survive upgrades. Each section below covers one part of the chain, from the voice in the room to the sound that reaches the viewer.</p>
<h2>Start with the microphone position</h2>
<p>A microphone placed close and steady to the mouth does more for the sound than almost any other change. Set it a hand’s width or two away, slightly off-axis to reduce breath pops, and keep that distance for the whole stream. A boom arm or a stand helps you keep the position without leaning or shifting. If you move around, a clip-on microphone keeps the distance constant, though it needs careful placement to avoid rustle.</p>
<p>Mark the microphone position on the desk so you can return to it after a break. Consistency matters more to viewers than a slightly better microphone that drifts away from the mouth.</p>
<h2>Treat the room before buying gear</h2>
<p>Most home rooms are hard and noisy, and they add echo and background sound to the voice. Soft furnishings, a rug, curtains and a few cushions around the speaker do more than many upgrades. Turn off fans, air conditioning and anything that hums, and close the door if traffic or family noise is an issue. Record a short test before the stream and listen on headphones to hear what the room adds.</p>
<p>A quiet room also makes any noise reduction work better, because the processing has less to remove and is less likely to damage the voice.</p>
<h2>Plan the routing</h2>
<p>Routing is the path the audio takes from the microphone to the streaming software and then to the viewer. Each step can add delay, change the level or create a loop. Draw the path on paper before you set it up, naming each device and each program. The simpler the route, the fewer surprises during a live show.</p>
<p>Decide which audio goes to viewers and which only to you. Music you play, notifications, chat sounds and game audio each need a deliberate path, so that viewers hear what you intend and nothing private.</p>
<h2>Choose processing with restraint</h2>
<p>Noise suppression, gates, compressors and equaliser settings can improve a stream, but each one can also damage the voice if it is set too hard. Start with the lightest settings that solve the problem you can hear, and add one tool at a time. A noise gate that cuts the start of words, or a suppressor that makes the voice sound watery, is worse than a little background noise.</p>
<p>The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> describes live noise cancellation that learns the room noise and feeds OBS, Discord or Zoom. Test any processing with a friend before using it live, and listen for artefacts on the consonants.</p>
<h2>Set the level before the show</h2>
<p>The level should be steady and clear, with the peaks well below the top. Speak at your normal volume during the check, and watch the meter. A stream that is too quiet forces viewers to turn up the volume, and then the next loud moment is uncomfortable. A stream that clips sounds harsh and distorted. A steady level is the target, and it is easy to hold once it has been set.</p>
<h2>Monitor while you stream</h2>
<p>Use headphones to monitor your own output, so you hear what viewers hear. Check periodically, especially after a change in the room, the microphone or the game. Many problems arrive mid-stream: a fan switches on, a cable loosens, a program starts playing a sound. A short check every half hour catches most of them before a viewer complains.</p>
<h2>What to plan for next year</h2>
<p>Expect more streams to include captions, immersive game audio and cloud-based processing. Plan for captions by keeping the speech clear, because recognition works best on clean audio. Keep the routing flexible enough to add a new source without rebuilding everything. Review your setup each season, and remove any processing that no longer earns its place.</p>
<h2>Limits</h2>
<p>Streaming software, platforms and hardware change quickly, and menu names move around. The principles here are more stable than any product-specific steps. Test every change before going live, and keep a written note of the settings that worked, so you can restore them after an update.</p>
<h2>Start with a checklist</h2>
<p>A checklist keeps the setup consistent across streams. The <a href="/tunedzy/blog/stream-audio-checklist-before-going-live">pre-stream checklist</a> in this series sets out the steps. For a phone recording that will become a clip, the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning the audio in your browser. For the noise side of the chain, read the <a href="/tunedzy/blog/noise-suppression-vs-echo-cancellation-explained">noise and echo post</a>.</p>
''',
    faq=[('What matters most in a streaming audio setup?', 'Microphone position and room first, then routing, processing and monitoring.'),
         ('Do I need expensive equipment?', 'Not to start. Position and a quiet room often make a bigger difference than a new microphone.'),
         ('How often should I check my audio mid-stream?', 'Every thirty minutes or so, and after any change in the room or the setup.'),
         ('Should I plan for captions now?', 'Yes, by keeping the speech clear and the routing flexible, since captions work best on clean audio.')])

add(slug='stream-audio-levels-for-viewers', cluster='trend-streaming', kw='stream audio levels',
    title='Stream Audio Levels: How Loud Your Voice Should Be for Viewers',
    desc='Stream audio levels for viewers: how to set a steady speech level, avoid clipping, balance game and music, and check the result on a phone.',
    h1='Stream Audio Levels: How Loud Your Voice Should Be for Viewers',
    answer='Set your voice to a steady, comfortable level that sits clearly above the game and music, with the peaks kept well below the top of the meter. Check the level during a test, listen on a phone speaker, and adjust the balance rather than turning the stream up or down during the show.',
    body='''
<p>A viewer’s first decision about a stream is often made in the first minute, and the level of the voice is a big part of that decision. If the voice is too quiet, the viewer reaches for the volume control. If the next sound is a loud game effect, the viewer reaches for it again. A stream with a steady, clear voice feels relaxed, and it keeps people listening even when the game is noisy.</p>
<p>This guide explains how to set the level, how to balance the voice against the other sources and how to check the result the way most viewers will hear it. The aim is a stream that needs no adjustment from the viewer once it has started.</p>
<h2>Why the level matters to viewers</h2>
<p>Viewers listen on a range of devices, from headphones to small phone speakers and laptops. Each has a different sensitivity, and the same stream can sound very different on each. A voice set too low will disappear on a phone, while a voice set too high will sound harsh on headphones. The target is a level that works on all of them, which means a steady balance rather than a loud one.</p>
<p>Viewers also judge the sound by its consistency. A voice that rises and falls between segments is tiring, even when each part is acceptable on its own. Steady levels build trust, and they let viewers forget about the sound and enjoy the content.</p>
<h2>Set the voice level first</h2>
<p>Speak at your normal volume during the setup, and watch the level meter in your streaming software. Aim for the voice to sit comfortably in the middle of the meter, with the loudest words peaking well below the top. Leave some headroom, because a sudden shout or a laugh will push the peaks up. A voice that sits too close to the top will clip, and clipping sounds harsh and distorted to viewers.</p>
<p>Once set, keep the microphone position and the distance steady. Changing the distance changes the level, and then you will be chasing the meter throughout the stream.</p>
<h2>Balance against game and music</h2>
<p>Game audio, music and alerts should sit below the voice, so the viewer can follow the speech without strain. A common approach is to set the voice as the loudest source, then lower the game and music until they support it. Test with a real game scene, since a loud explosion can overpower a quiet voice in a way that the setup check did not reveal.</p>
<p>If the game is loud, consider a ducking setup that lowers the game when you speak. That keeps the voice clear without making the game too quiet during your silences. The <a href="/tunedzy/how-to-duck-music-under-a-voiceover">ducking guide</a> explains the principle, which applies to streams as well.</p>
<h2>Check the result the way viewers will</h2>
<p>Listen to your stream on a phone speaker and on headphones, using the same platform the viewers will use if you can. Ask a friend to watch for a minute and tell you whether the voice is comfortable. Many streamers only listen through their own headphones, which hides the problems that viewers hear on a small speaker.</p>
<p>Record a short clip of the stream, and check its loudness with the <a href="/tunedzy/tools/lufs-meter">LUFS meter</a>. A recording gives you a steady reference for comparing one stream with the next.</p>
<h2>Adjust the balance, not the volume</h2>
<p>When something sounds wrong mid-stream, adjust the balance between sources rather than turning the whole stream up or down. Changing the master volume affects everything, including what viewers hear as the level of your voice. Make small, planned changes, and note any change you make so you can return to the setting later.</p>
<h2>A simple checklist</h2>
<ol>
<li>Set the voice level with a test, keeping the peaks below the top of the meter.</li>
<li>Balance the game and music so the voice is clearly the loudest source.</li>
<li>Test with a real game scene and a real alert.</li>
<li>Listen on a phone speaker and on headphones, or ask a viewer to report back.</li>
<li>Save the settings, and recheck after every update or change of microphone.</li>
</ol>
<h2>Make the level part of your brand</h2>
<p>Viewers come back to streams that feel comfortable, and a steady level is part of that comfort. A streamer who keeps the same voice level, the same balance and the same loudness across every stream is building a recognisable sound, in the same way a radio presenter does. Viewers may never name it, but they notice when a stream suddenly sounds different, and that difference can make them leave.</p>
<p>Write your level settings down, and keep them in a template for each new stream. When you change the microphone or the room, record a short reference and update the notes, so the sound returns to the same place after every change.</p>
<h2>Limits</h2>
<p>Viewer devices and platform playback settings vary, so no single level will suit everyone. The aim is a level that is comfortable for most people on common devices. Platforms may also adjust the audio on playback, which changes the final result, so check the stream as viewers will hear it rather than only the signal leaving your computer.</p>
<h2>Start with a clean voice</h2>
<p>A clean voice makes the level easier to set, because there is less noise to fight. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> offers live noise cancellation for OBS, Discord and Zoom. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording for clips. For the full pre-stream routine, read the <a href="/tunedzy/blog/stream-audio-checklist-before-going-live">pre-stream checklist</a> in this series.</p>
''',
    faq=[('How loud should my voice be on stream?', 'Steady and comfortable, sitting clearly above the game and music, with peaks well below the top of the meter.'),
         ('Should I turn the stream volume up during the show?', 'Avoid it. Adjust the balance between sources, and keep the master level steady.'),
         ('Why does my stream sound quiet on phones?', 'Phone speakers reproduce speech differently. Test on a phone and raise the clarity of the voice.'),
         ('How do I stop the game drowning out my voice?', 'Lower the game and music, and consider ducking the game when you speak.')])

add(slug='background-music-rules-for-live-streams', cluster='trend-streaming', kw='background music on stream rules',
    title='Background Music on Live Streams: Rules, Risks and Safer Choices',
    desc='Background music on live streams: why platforms act on copyrighted music, what licences cover, the safer choices streamers can make and how to avoid takedowns.',
    h1='Background Music on Live Streams: Rules, Risks and Safer Choices',
    answer='Playing copyrighted music on a live stream can lead to muted audio, removed streams or account penalties, even when it is only in the background. Use music you have licensed for streaming, music from a library that allows live use, or the platform’s own music options, and check each platform’s current rules before going live.',
    body='''
<p>Background music can make a stream feel alive, but it is one of the fastest ways to get into trouble. Streaming platforms use automated systems to detect copyrighted music, and the response can range from a muted replay to a removed stream or a penalty on the account. Many streamers do not realise that music playing softly in the background, or heard through a game, can be enough to trigger one of these actions.</p>
<p>This post explains the risk, what licences generally cover, the safer choices available and how to set up a stream so that the music you want is the music viewers hear. It is general guidance, and the rules differ by platform and by country, so check the current policy of each service you use.</p>
<h2>Why platforms act on music</h2>
<p>Platforms have agreements with rights holders, and they use detection tools to find music that is not licensed for their services. When a match is found, the platform may mute the audio on the replay, remove the recording or act against the account. Live streams are harder to check than uploads, but they are still monitored, and many platforms also review reports from rights holders after the event.</p>
<p>The detection can catch music you did not choose to play. A song on a car radio, a track in a game, or music from another window can be enough. Streamers who want certainty should control every source of sound that reaches the stream.</p>
<h2>What a licence covers</h2>
<p>A licence to listen to music at home is not the same as a licence to broadcast it. A streaming licence, where it exists, sets out the places and services where the music may be played, and it may limit live use. Some libraries sell music specifically for streaming, with terms that allow it on named platforms. Read the terms closely, and keep records of the licence, its date and the platforms it covers.</p>
<p>Some platforms also offer their own music libraries or licensed sound options. These are often the simplest route, because the platform has already agreed the terms. Check whether the library is available on your stream type and in your region.</p>
<h2>Safer choices for streamers</h2>
<ol>
<li>Use music from a library that explicitly allows live streaming on your platform.</li>
<li>Use the platform’s own music options, where they exist and meet your needs.</li>
<li>Create your own music, or commission a track with a licence for streaming.</li>
<li>Keep the stream free of other music sources, such as a playlist in another app.</li>
<li>Mute or pause the music when a segment depends on sound that might be detected.</li>
</ol>
<h2>Setting up the stream</h2>
<p>Route the music through a separate source that you can mute quickly, and check that no other program is playing music into the stream. Test the setup with a short run, and check the platform’s notices afterwards. A mute button that you can reach without thinking is one of the most useful safety tools a streamer has.</p>
<p>Be careful with game audio too. Some games contain licensed music, and the music may reach viewers even though it is part of the game. Check the terms of the game and the platform, and consider muting the game music while leaving the effects on.</p>
<h2>If you receive a notice</h2>
<p>If the platform notifies you of a copyright claim or a mute, read the notice, check what was detected and respond through the platform’s process if you believe it was wrong. Keep records of the music you use and the licences that cover it. A calm, documented response is more effective than an angry one.</p>
<h2>Choose music before the stream</h2>
<p>The safest time to decide about music is before the stream starts, not during it. Build a short playlist from licensed sources, check each track against the platform&rsquo;s rules, and save it under a clear name. A playlist chosen in advance removes the temptation to play something on impulse, which is how most rights problems begin. Keep the playlist separate from your everyday music library, so the wrong song cannot slip in.</p>
<p>Review the playlist when the platform updates its rules, or when you add a new licence. Remove any track whose licence no longer covers live use, and note the date of each review.</p>
<h2>Limits</h2>
<p>Platform rules, detection methods and licensing options change, and this post cannot describe every case. The safe habit is to know the source of every sound on the stream, and to check the current policy of each platform. For a specific business or a large audience, take advice on the licences you need.</p>
<h2>Keep the sound under control</h2>
<p>Good audio control makes it easier to manage what viewers hear, including music. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> describes live noise cancellation for your voice, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the balance between voice and music, read the <a href="/tunedzy/blog/stream-audio-levels-for-viewers">stream levels post</a> in this series.</p>
''',
    faq=[('Can I play music quietly in the background?', 'Not safely. Detection can pick up quiet music, so use licensed music or none at all.'),
         ('Is a licence for listening enough?', 'No. A streaming licence is needed for live broadcast, and the terms vary.'),
         ('What if my game plays licensed music?', 'Check the game and platform terms, and consider muting game music while keeping the effects.'),
         ('What should I do after a notice?', 'Read the notice, check what was detected, respond through the platform process and keep records.')])

add(slug='voice-changers-on-streams-explained', cluster='trend-streaming', kw='voice changer for streaming',
    title='Voice Changers on Streams: How They Work and When to Disclose',
    desc='Voice changers on streams explained: how real-time voice effects work, the audio side effects to test, the ethics of impersonation and when to tell viewers.',
    h1='Voice Changers on Streams: How They Work and When to Disclose',
    answer='A voice changer alters your voice in real time, for effect or for character. It can add distortion or artefacts, and it can change how clearly you are heard. Test it for clarity, avoid impersonating real people, and tell viewers when the voice is changed, especially where the change could mislead.',
    body='''
<p>Voice changers are popular with streamers who play characters, tell stories or want a distinctive sound. They take the voice from the microphone, alter its pitch, timbre or character in real time, and send the altered sound to the stream. The effect can be entertaining, and it can also cause problems with clarity, with fairness to viewers and with the people whose voices might be imitated. This post covers how they work, the audio issues to test, the ethics and when to disclose.</p>
<p>The guidance here is general. Tools differ, and the rules about impersonation and synthetic media are changing, so check the current policy of your platform and the laws that apply to you.</p>
<h2>How a real-time voice changer works</h2>
<p>A voice changer analyses the incoming voice and processes it through effects such as pitch shifting, formant changes, filters or a model that changes the character of the sound. The processing has to run in a fraction of a second to keep up with speech, which means the result is an approximation. Some changers are simple effects, while others use machine learning models that can produce more convincing results at a higher cost in processing power.</p>
<p>Because the processing happens live, any artefacts it creates go straight to viewers. The more complex the change, the more likely it is to produce distortion or a delay.</p>
<h2>Clarity is the first test</h2>
<p>A voice changer that makes you hard to understand defeats its purpose. Test the setting by speaking at normal speed, with the words you use most often, and ask a friend to repeat back what they heard. Listen for consonants that blur, words that run together and a delay that makes the voice feel out of sync with the game or the chat.</p>
<p>Keep the change as light as the character allows. A slight change in pitch may be enough, and a dramatic change may be more distracting than helpful.</p>
<h2>Audio side effects to check</h2>
<p>Voice changers can introduce metallic, watery or robotic artefacts, especially at extreme settings. They can also add noise or a hiss, and they may change the level so the voice is much quieter or louder than before. Check the output on a phone speaker and on headphones, and listen for any sound that is not your voice. The noise and level habits in the <a href="/tunedzy/blog/stream-audio-levels-for-viewers">levels post</a> apply here too.</p>
<h2>Impersonation and fairness</h2>
<p>A voice changer that imitates a real person can mislead viewers and harm the person imitated. Impersonating a public figure for a joke may be treated as harassment or deception by platforms, and it can damage your reputation. Avoid imitating real people, especially in ways that suggest they said or endorsed something. Stick to a character you have created.</p>
<h2>When to disclose</h2>
<p>Tell viewers when your voice is changed, especially if the change is convincing enough that someone might think you sound differently in person or that you are someone else. A short note in the stream title or on screen is usually enough. Disclosure is part of trust, and viewers who know the voice is a character can enjoy it more.</p>
<p>If the changed voice is used in a context where it could mislead, such as a sponsored read or a claim about a product, the disclosure matters even more, and the content may need more care than a playful character.</p>
<h2>Respect the people around you</h2>
<p>A voice changer can affect guests and co-hosts as well. If others speak on your stream, make sure they know the voice is changed, and that their own voices are not being altered without consent. Agree the rules before the stream starts.</p>
<h2>Keep the character consistent</h2>
<p>A voice character works best when it is consistent. Viewers quickly learn the voice, and a sudden change in pitch or tone can break the illusion or confuse people who are new to the stream. Choose a setting that you can hold for hours, and avoid tweaking it mid-stream unless something is clearly wrong. Save the setting so you can restore it exactly after a restart or an update.</p>
<p>If you use more than one character, make the switch obvious and planned, such as a clear announcement. Unplanned changes feel like faults, while planned ones feel like part of the show.</p>
<h2>Limits</h2>
<p>Voice changer technology and platform policies are both developing. The effects that are acceptable today may change, and some platforms have rules about synthetic voices that differ from their rules about other effects. Check the current policy, test the setup before going live and keep the change honest and clear.</p>
<h2>Keep your real voice clear too</h2>
<p>Even if you change your voice, the clean signal is the best foundation. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> describes live noise cancellation for your microphone input, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning recordings. For the rules about labelling generated voices, read the <a href="/tunedzy/blog/how-to-label-ai-generated-voice-in-content">labelling guide</a> in this series.</p>
''',
    faq=[('Do I have to disclose a voice changer?', 'Tell viewers when the change could mislead. A short note is usually enough.'),
         ('Can I imitate a famous person?', 'Avoid it. Imitation can mislead viewers and may breach platform rules.'),
         ('Why is my changed voice hard to understand?', 'The change is too strong or the delay is too long. Lighten the effect and test.'),
         ('Can a voice changer affect other people on my stream?', 'Yes, if it processes their voices too. Agree the rules with guests first.')])

add(slug='duck-game-audio-for-streams', cluster='trend-streaming', kw='duck game audio stream',
    title='How to Duck Game Audio on a Stream So Your Voice Stays Clear',
    desc='How to duck game audio on a stream so your voice stays clear: the principle of ducking, setup options, the timing to get right and the common mistakes.',
    h1='How to Duck Game Audio on a Stream So Your Voice Stays Clear',
    answer='Ducking lowers the game audio automatically when you speak, then brings it back when you stop. Set the threshold so it responds to your voice and not to background noise, use a quick attack and a gentle release, and test with a real game scene to make sure your voice stays clear during action.',
    body='''
<p>On a live stream, the game is often the loudest thing in the room. An explosion, a crowd or a soundtrack can drown out the streamer, and viewers lose the words. Ducking solves that problem by lowering the game audio while you speak, then bringing it back when you stop. Done well, it is invisible. Done badly, it pumps, cuts off the start of words or responds to noise instead of speech.</p>
<p>This guide explains the principle, the setup options, the timing to get right and the mistakes that most often spoil the effect. The idea is the same as ducking music under a voice-over, which is covered in the guide linked below.</p>
<h2>The principle of ducking</h2>
<p>Ducking uses the level of your voice as a trigger. When your voice rises above a threshold, the game audio is reduced by a set amount. When your voice stops, the game returns to its normal level. The effect is a steady balance that favours the speech, without any manual adjustment during the stream.</p>
<p>The important settings are the threshold, which decides when ducking starts, the amount, which decides how far the game drops, and the timing, which decides how quickly it responds and recovers. Each one affects how natural the effect sounds.</p>
<h2>Choose a setup</h2>
<p>Ducking can be set up in streaming software with a sidechain or ducking filter, in a separate audio program that sits between the game and the stream, or in a hardware mixer. The exact steps depend on your software and version, so check the current menus rather than relying on old instructions. The principle stays the same whichever route you take.</p>
<p>Keep the setup as simple as possible. A single ducking filter on the game source is easier to test and to troubleshoot than a chain of separate effects.</p>
<h2>Set the threshold carefully</h2>
<p>The threshold should sit just above the background noise in your room, so the game drops when you speak and stays up during silence. If the threshold is too low, the room noise will trigger the ducking, and the game will flicker. If it is too high, your quieter words will not trigger it, and the game will stay loud while you talk.</p>
<p>Test the threshold with normal speech, a quiet word and a loud laugh. The ducking should respond to all three without pumping or hesitating.</p>
<h2>Timing: attack and release</h2>
<p>The attack is how quickly the game drops when you start speaking. A quick attack protects the start of your words, but if it is too fast the change can sound abrupt. The release is how slowly the game returns after you stop. A slow release keeps the game from jumping back in the gaps between words, which otherwise makes the stream sound choppy.</p>
<p>A good starting point is a quick attack and a release that feels gentle, then adjust by listening. Test with a real game, because timing that works in a quiet menu may fail in a battle.</p>
<h2>The amount of reduction</h2>
<p>Reduce the game enough to make the voice clear, but not so much that the game feels absent. A moderate reduction often works well, and you can adjust it while you test. Too much reduction can make the stream feel like a podcast with a silent game, which is not what viewers came for.</p>
<h2>Common mistakes</h2>
<ul>
<li>Setting the threshold below the room noise, so the game flickers constantly.</li>
<li>Using an attack so fast that the change sounds abrupt.</li>
<li>Using a release so fast that the game pumps back between words.</li>
<li>Reducing the game so much that the stream loses its energy.</li>
<li>Testing only in a quiet scene, and missing the problems in a loud one.</li>
</ul>
<h2>Test before going live</h2>
<p>Record a short clip of a loud game scene while you talk, then play it back on a phone and on headphones. Check that the voice stays clear, the game returns smoothly and nothing sounds choppy. Adjust one setting at a time, and record again.</p>
<h2>Ducking for different games</h2>
<p>Different games need different settings. A slow, narrative game with quiet music may need only a light reduction, while a fast shooter with constant effects may need a stronger one. Keep a profile for each game you stream, with its own threshold and amount, and load it when you switch. A profile saved after a good test saves time and avoids the guesswork of setting everything again.</p>
<p>Pay attention to menus and loading screens, which can be quiet and then suddenly loud. A ducking setup that works in combat may react strangely in a menu, so test those moments too.</p>
<h2>Limits</h2>
<p>Ducking is a balance, not a cure. A very loud game can still mask a quiet voice, and a noisy room can make ducking unreliable. Pair ducking with a clean microphone and a steady level. The effect also depends on your software and your game, so test your own setup.</p>
<h2>Keep the voice clean</h2>
<p>Ducking works best when the voice is clean. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> describes live noise cancellation that learns the room noise, which can help the threshold stay reliable. For the same principle applied to a recorded voice-over, read the <a href="/tunedzy/how-to-duck-music-under-a-voiceover">music ducking guide</a>.</p>
''',
    faq=[('What is ducking?', 'Automatically lowering the game or music while you speak, then bringing it back in the gaps.'),
         ('Why does my game flicker when I am quiet?', 'The threshold is too low, so room noise triggers the ducking. Raise it.'),
         ('Why does the start of my words get cut off?', 'The attack is too slow. Make it quicker so the game drops before you speak.'),
         ('Does ducking work for music too?', 'Yes. The same principle applies to background music and to a voice-over.')])

add(slug='noise-suppression-vs-echo-cancellation-explained', cluster='trend-streaming', kw='echo cancellation vs noise suppression',
    title='Echo Cancellation vs Noise Suppression: What Each One Does',
    desc='Echo cancellation vs noise suppression explained: what each does, why they are different, how they interact and how to set them for calls and streams.',
    h1='Echo Cancellation vs Noise Suppression: What Each One Does',
    answer='Echo cancellation removes sound from your speakers that returns into your microphone, while noise suppression reduces steady or background sound around your voice. They solve different problems and can interact. Enable echo cancellation when speakers are in the room, and use noise suppression lightly to avoid damaging the voice.',
    body='''
<p>Calls and streams often offer two settings that sound similar and do different jobs: echo cancellation and noise suppression. Many people switch them both on and assume the result will be better. Sometimes it is, but the two can interact, and the wrong combination can make the voice sound distant, watery or choppy. Understanding what each one does makes the settings easier to choose.</p>
<p>This post explains the difference, the problems each solves, the way they can interact and how to test them before a call or stream.</p>
<h2>What echo cancellation does</h2>
<p>Echo cancellation solves a feedback problem. Sound from your speakers, such as the voice of the person you are talking to, can travel back into your microphone and be sent to them again. They hear their own voice a moment late, which is confusing and tiring. Echo cancellation compares the sound going to the speakers with the sound arriving at the microphone, and it removes the part that is an echo.</p>
<p>The effect is strongest when the sound from the speakers is a clean signal that the system can recognise. It is less effective in a very reverberant room, or when the speakers are loud, and it can fail if the delay between the speakers and the microphone changes.</p>
<h2>What noise suppression does</h2>
<p>Noise suppression reduces sound that is not speech, such as a fan, typing, traffic or a steady hum. It estimates which parts of the signal are speech and which are background, and it reduces the background. Modern suppressors can be quite effective on steady noise, but they can also remove quiet consonants or make the voice sound thin when set too strongly.</p>
<p>Noise suppression works on the sound around the microphone. Echo cancellation works on the sound coming from the speakers. They are different problems, and they need different solutions.</p>
<h2>How they interact</h2>
<p>Using both can help, but the order and the strength of each matter. An aggressive noise suppressor can make the echo cancellation work harder, and the two can produce artefacts when they fight over the same sound. Some systems apply echo cancellation first and noise suppression second, while others differ. Check how your software orders them, and test the combination.</p>
<p>A practical rule is to use echo cancellation whenever the speakers are in the room, and to add noise suppression only if the background is a real problem. Starting with the lightest settings that work is safer than the strongest settings available.</p>
<h2>When to use each</h2>
<ol>
<li>Use echo cancellation if you use speakers rather than headphones, or if the other person hears themselves.</li>
<li>Use noise suppression if a steady background sound is audible to the other side.</li>
<li>Use headphones where you can, since they remove most of the echo problem at the source.</li>
<li>Test both settings with a friend, and ask them whether your voice is clear.</li>
<li>Change one setting at a time, so you know which change caused a problem.</li>
</ol>
<h2>Signs that the settings are wrong</h2>
<p>Too much noise suppression makes the voice watery, thin or robotic, and it can cut the ends of words. Too little echo cancellation leaves the other person hearing an echo of themselves. Echo cancellation that is working too hard can sound like the voice is breaking up or dropping in and out. Listen for these signs, and reduce the processing when you hear them.</p>
<h2>Testing before a call or stream</h2>
<p>Record a short test and play it back. Check the voice for artefacts and the room for background sound. If possible, make a test call with a friend and ask them to tell you what they hear. Test with the speakers at the volume you normally use, since echo changes with the level.</p>
<h2>Keep a settings log</h2>
<p>Write down the settings that work, with the app, the version, the device and the date. A log turns a lucky setup into a repeatable one, and it helps you recover quickly after an update changes the menus or the defaults. Include the microphone, the distance, the echo setting, the noise setting and any notes about what you heard during the test.</p>
<p>Update the log when you change anything, even a small thing. A single line in a notebook is enough, and it is far more useful than trying to remember what you did a month ago.</p>
<h2>Limits</h2>
<p>Processing behaviour varies by app, device and version, and menu names change. The principles are stable, but the exact settings will differ. A setting that works in one app may behave differently in another, so test in the app you use.</p>
<h2>Start with a good microphone position</h2>
<p>Processing works best when the signal is already clean. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> describes live noise cancellation that feeds OBS, Discord and Zoom, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning recordings. For the wider noise options in apps, read the <a href="/tunedzy/blog/discord-zoom-teams-noise-suppression-settings">app noise settings post</a> in this series.</p>
''',
    faq=[('Do I need echo cancellation with headphones?', 'Usually not, since headphones keep the speaker sound out of the microphone.'),
         ('Why does my voice sound watery on a call?', 'Noise suppression may be set too strongly. Reduce it and test.'),
         ('Can I use both settings together?', 'Yes, but start light and test. The two can interact and cause artefacts.'),
         ('What is the first thing to try?', 'A good microphone position and headphones, then light processing only where you hear a problem.')])

add(slug='two-pc-streaming-audio-routing', cluster='trend-streaming', kw='audio routing two pc streaming',
    title='Two-PC Streaming Audio Routing: A Clear Way to Set It Up',
    desc='Two-PC streaming audio routing explained: how a second computer handles the stream, how audio is sent between the machines, the common problems and a clear setup.',
    h1='Two-PC Streaming Audio Routing: A Clear Way to Set It Up',
    answer='A two-PC setup moves the game to one computer and the streaming software to another, which keeps the stream smooth. Audio must be sent from the game machine to the streaming machine and your microphone must go to the stream. Plan each path on paper, test the delay and make sure you can mute each source quickly.',
    body='''
<p>Many serious streamers run two computers: one for the game and one for the streaming software, the overlays and the chat. The split keeps the game running smoothly while the stream is encoded, and it protects the frame rate from heavy processing. It also makes the audio harder to manage, because sound must travel between machines and still reach the viewer in the right balance. A clear plan saves a great deal of frustration.</p>
<p>This post explains how two-PC audio routing works, the main paths to plan, the problems that appear most often and a setup that is easy to understand and test.</p>
<h2>Why a second computer changes the audio</h2>
<p>On a single computer, the game, the microphone and the stream all share one audio system, which is simple but can be overloaded. On two computers, the game audio must leave the game machine and arrive at the streaming machine, which adds a link to the chain. Each link can add delay, change the level or create an echo loop if it is set up badly.</p>
<p>The aim is to make each link deliberate, so you know exactly what the viewer hears and where each source comes from.</p>
<h2>Plan the paths on paper</h2>
<p>Draw the path for each source before you set anything up. The game audio goes from the game machine to the streaming machine. Your microphone goes from the streaming machine into the stream, and may also go to the game machine if you talk to teammates. Music, alerts and chat sounds each need their own path. A diagram with boxes and arrows makes the plan easy to check.</p>
<p>Decide which sources you want viewers to hear and which should stay private. Private sounds, such as voice chat from a game or notifications, need a path that does not reach the stream.</p>
<h2>Sending game audio between machines</h2>
<p>There are several ways to send game audio from one machine to another, including dedicated network audio software, a virtual audio device or a hardware mixer. Each has its own setup steps, which change between versions, so check the current instructions for the tool you choose. Whichever method you use, test it with a short clip and listen for delay and dropouts.</p>
<p>Keep the sample rate consistent between the two machines. A mismatch can cause crackles, pitch shifts or dropouts that are hard to trace.</p>
<h2>Routing your microphone</h2>
<p>Your microphone should go to the streaming machine, which is where the stream is built. If you also need to talk to teammates on the game machine, you may need a separate path for the voice chat, so that the game and the stream do not create an echo loop. Test the loop carefully: a voice that comes back into the stream a moment later is one of the most irritating problems for viewers.</p>
<h2>Common problems</h2>
<ul>
<li>An echo loop, where the stream sends your voice back to your headset.</li>
<li>Delay between the game and the voice, which makes reactions feel late.</li>
<li>Dropouts or crackles from a mismatched sample rate or a weak network link.</li>
<li>Private sounds, such as voice chat or notifications, reaching the stream by accident.</li>
<li>Music or alerts playing twice, because two paths were set up for the same source.</li>
</ul>
<h2>Test before going live</h2>
<p>Run a full test with the game, the microphone, the music and an alert. Watch the stream on a second device to check the delay and the balance as viewers will hear it. Check for the echo loop, and mute each source in turn to confirm that the mute works. A test takes a few minutes and prevents most of the problems.</p>
<h2>Keep the second machine simple</h2>
<p>The more software you run on the streaming machine, the more chances there are for audio conflicts. Close anything you do not need, especially background music players, sync tools and notification-heavy programs. Keep the audio drivers updated, but change them only one at a time, and test after each change, since a new driver can alter how the routing behaves.</p>
<p>Consider making the streaming machine a dedicated stream computer, with only the programs the stream needs. A simple machine is easier to diagnose when something goes wrong during a live show. Label the cables and the ports on each machine, so anyone can follow the path during a fault.</p>
<h2>Limits</h2>
<p>Two-PC setups have more parts, and more parts mean more things to go wrong. Software and hardware change quickly, and the steps here are general. Keep notes of the working setup, and rebuild the path carefully after an update.</p>
<h2>Keep the voice clean on both machines</h2>
<p>A clean voice is easier to route and to balance. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> describes live noise cancellation that feeds OBS, Discord and Zoom. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning recordings. For a single-machine version of the same idea, read the <a href="/tunedzy/blog/virtual-audio-cable-setup-obs-discord-zoom">virtual cable setup post</a> in this series.</p>
''',
    faq=[('Why do I get an echo loop?', 'The voice path returns to the microphone. Remove the loop by changing which sources go where.'),
         ('Is a second computer necessary?', 'Not for everyone. It helps heavy games and high-quality streams, but a single computer can be enough.'),
         ('How do I stop private sounds reaching viewers?', 'Give private sources their own path that does not connect to the stream, and test it.'),
         ('What should I test first?', 'The echo loop and the delay, using a full run with the game and the microphone.')])

add(slug='live-podcast-recording-with-a-stream', cluster='trend-streaming', kw='live podcast recording stream',
    title='Recording a Live Podcast on a Stream: Audio Setup and Checks',
    desc='Recording a live podcast on a stream: separate tracks, a clean audio master, guest setup, the stream mix and the checks that keep the recording usable.',
    h1='Recording a Live Podcast on a Stream: Audio Setup and Checks',
    answer='Recording a live podcast on a stream is easier if you capture a separate clean audio master for each voice, while the stream carries the public mix. Keep a local recording as the source of truth, check each guest’s connection and level, and test the whole setup before the show.',
    body='''
<p>A live podcast on a stream combines two jobs: producing a show that viewers watch as it happens, and producing a recording that can be published later as an episode. The two can conflict. The live mix is often compressed, delayed and balanced for the viewer, while the podcast needs clean separate tracks. A good setup serves both, so the stream is smooth and the episode is clean.</p>
<p>This guide covers how to capture a usable master, how to set up guests, how to keep the stream mix separate and how to check the recording before it is needed. It assumes a small team and a simple setup, which is the most common case.</p>
<h2>Keep a local master</h2>
<p>The most important rule is to record a local, clean copy of each voice on the host’s computer or on a separate recorder. A stream recording is a compressed mix, which is fine for a replay but not ideal for a podcast. Local recording gives you separate tracks with no compression from the platform and no dropouts from a weak network. If the stream fails, the local recording still exists.</p>
<p>Set the local recording to start before the show, and check that the files are saving every few minutes during the stream. Many lost episodes were lost because the recording was never started or never checked.</p>
<h2>Set up each guest carefully</h2>
<p>Each guest should use headphones, sit in a quiet room and keep a steady distance from the microphone. Ask them to record their own local copy if the platform allows it, since a guest’s local recording can be cleaner than the stream. Test each guest’s connection and level before the show, and agree a signal for when something goes wrong.</p>
<p>Guest setup is the most common weak point. A guest who joins on a poor connection or in a noisy room can damage the episode, and it is better to find that out in a test than in the middle of a show.</p>
<h2>Separate the stream mix from the master</h2>
<p>The stream mix is what viewers hear, and it may include music, alerts and processing that you do not want in the podcast. Keep those elements out of the master recording, or record them as separate tracks so they can be removed later. A clean master of each voice is the foundation of the episode, and the stream mix is the public performance.</p>
<h2>Balance the stream without damaging the master</h2>
<p>Processing applied to the stream can be different from the processing you want in the master. For example, a heavy limiter on the stream will make the live mix loud and steady, but it may flatten the master. Keep the master lightly processed, and apply the stronger processing only to the stream.</p>
<h2>A short pre-show check</h2>
<ol>
<li>Start the local recordings and confirm each file is saving.</li>
<li>Check each voice at normal speaking level, with peaks well below the top.</li>
<li>Test the stream with a short run, and watch it on a second device.</li>
<li>Check the guest connections, and agree what to do if a guest drops out.</li>
<li>Note the time and the episode title, so the recording is easy to find later.</li>
</ol>
<h2>After the show</h2>
<p>Stop the local recordings properly, and check that every file is complete. Back up the files as soon as possible, using the routine in the <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup post</a>. Then edit the master, and publish the episode with a clear note that it was recorded live.</p>
<h2>Edit with the stream in mind</h2>
<p>When you prepare the episode from a live recording, keep the stream in mind. A moment that worked live because of the energy of the room may need tightening for a listener who was not there. A joke that depended on a chat reaction may need context. Cut the dead air, but keep the spontaneity that made the live show enjoyable, because that is part of why people listen.</p>
<p>Mark the points where the stream had a technical problem, so you can cut or repair them. Listeners forgive a small glitch, but a long silence or a repeated sentence from a dropped connection is harder to hear through.</p>
<h2>Limits</h2>
<p>Platform features, file formats and recording options change, and some platforms limit local recording. The principles stay steady: keep a local master, separate the stream from the recording and test everything. For a complex show with many guests, plan a dedicated recording setup. Test that setup with the same guests before you rely on it, and write down what each person needs to bring.</p>
<h2>Keep every voice clean</h2>
<p>Clean sources make both the stream and the episode better. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> describes live noise cancellation for the stream, and the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. For the pre-stream routine, read the <a href="/tunedzy/blog/stream-audio-checklist-before-going-live">pre-stream checklist</a> in this series.</p>
''',
    faq=[('Should I rely on the stream recording for the podcast?', 'Better not. Keep a local master, since a stream recording is compressed and can drop out.'),
         ('Should guests record locally?', 'Yes, where the platform allows it, because a local copy is often cleaner.'),
         ('How do I keep music out of the podcast?', 'Keep the music out of the master, or record it on a separate track you can remove.'),
         ('What if a guest drops out?', 'Agree the plan before the show, and keep the local recordings of everyone who stayed.')])

add(slug='audio-for-live-qa-streams', cluster='trend-streaming', kw='live q and a audio',
    title='Audio for Live Q and A Streams: Hearing Questions Clearly',
    desc='Audio for live Q and A streams: how to capture viewer questions, set up hosts and guests, and keep answers and questions clear.',
    h1='Audio for Live Q and A Streams: Hearing Questions Clearly',
    answer='A live Q and A stream works when viewers can hear the questions as well as the answers. Read questions aloud or use a clear question channel, keep the host and any guest at steady levels, and test the path that brings questions into the stream. A clear question is part of the answer.',
    body='''
<p>A live question and answer stream has a special problem: the audience often cannot hear the question. The host answers something that has been typed in chat or asked by a caller, and viewers who did not see the question are left guessing. The fix is partly editorial, in reading the question aloud, and partly technical, in making sure the question channel is clear. Both matter for a Q and A to feel useful.</p>
<p>This post explains how to set up the audio for a live question stream, how to bring questions into the show and how to keep the answers clear for everyone watching.</p>
<h2>Why the question matters</h2>
<p>An answer without the question is confusing, and it wastes the viewer’s attention. Viewers come to a Q and A to hear the host respond to specific questions, so the question has to reach them. Reading the question aloud before answering is the simplest way to make the stream work, and it also gives you a moment to think before you reply.</p>
<p>Some streams use a question overlay on screen as well, which helps viewers who are reading rather than listening. Use both where you can.</p>
<h2>Set up the host microphone</h2>
<p>The host’s voice should be clear, steady and close to the microphone, as in any stream. Keep the level constant between questions and answers, since a sudden change in level can make the answer feel disconnected from the question. The <a href="/tunedzy/blog/stream-audio-levels-for-viewers">stream levels guide</a> explains how to set a steady level.</p>
<p>If the host reads questions aloud, consider a second, slightly different tone or volume for the question, so viewers can tell where the question ends and the answer begins. Keep the difference subtle, and make sure it stays consistent.</p>
<h2>Bring in callers or guests</h2>
<p>If callers or guests speak on the stream, each needs a clean microphone path and a level check before the show. A caller on a phone line or a weak connection will sound worse than the host, and the difference can make the show feel uneven. Test each caller before they go live, and ask them to use headphones to avoid echo.</p>
<p>Agree a simple cue for when a caller is about to speak and when they have finished. A short signal avoids cutting people off or talking over them.</p>
<h2>Route the question channel</h2>
<p>Questions may come from chat, from a form or from a phone line. Each route needs a path that is tested before the show. A question typed in chat is text, so it must be read aloud or shown on screen. A phone question must be connected to the stream without echo or delay. Test each route, and make sure the host can see the queue of questions without looking away from the camera.</p>
<h2>Keep the pace comfortable</h2>
<p>Viewers need time to hear a question and to take in the answer. A show that jumps from question to question too quickly can feel rushed, while one that lingers can lose attention. Pace the show to match the number of questions and the length of the answers, and leave a short pause between items so the transition is clear.</p>
<h2>Save the questions</h2>
<p>Keep a record of the questions and answers, either as a text log or as a saved recording. A saved Q and A is useful for a replay, for clips and for future content. The record also helps you see which questions the audience cares about most.</p>
<h2>Handle a question you cannot answer</h2>
<p>Some questions will be outside your knowledge, or too personal, or too unclear to answer well. Decide before the show how you will handle them. Saying honestly that you do not know, or that you will look into it, builds more trust than a confident guess. Read the question aloud first, so viewers know what you are declining, and then move on without a long apology.</p>
<p>Keep a short list of questions you promised to follow up on, and share the answers later. Following up shows viewers that their questions matter, and it often brings them back. Give the follow-up its own short segment, so it is easy to find in a replay, and name the viewer only if they agree to be named. A short, clear answer is usually better than a long one that wanders.</p>
<h2>Limits</h2>
<p>A live Q and A depends on the audience, the platform and the connections of everyone involved. Expect some technical problems, and have a plan for them. The goal is a clear conversation, not a flawless broadcast.</p>
<h2>Start with clean voices</h2>
<p>Clear voices make a Q and A much easier to follow. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> describes live noise cancellation for the host’s microphone, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning recordings. For the routing side, read the <a href="/tunedzy/blog/two-pc-streaming-audio-routing">two-PC routing post</a> in this series.</p>
''',
    faq=[('Should I always read the question aloud?', 'Usually yes, so viewers who are listening can follow the answer.'),
         ('How do I bring in a phone caller cleanly?', 'Test the connection, ask the caller to use headphones and check the level before the show.'),
         ('How fast should the show move?', 'Pace it to the number of questions and the length of answers, with a short pause between items.'),
         ('Should I save the Q and A?', 'Yes. It makes replays, clips and future content easier to produce.')])

add(slug='stream-audio-checklist-before-going-live', cluster='trend-streaming', kw='stream audio checklist',
    title='The Stream Audio Checklist: What to Check Before You Go Live',
    desc='A stream audio checklist for before you go live: microphone, room, levels, routing, music rights, processing and a final test on a second device.',
    h1='The Stream Audio Checklist: What to Check Before You Go Live',
    answer='Before going live, check the microphone position and room, set the voice level with a test, confirm the routing and mutes, check music and game sources for rights, review processing, and watch a short test on a second device. A written checklist catches the mistakes that are easy to make when you are excited to start.',
    body='''
<p>Going live is exciting, and it is easy to skip the basics. A stream that starts with a loud alert, a microphone pointing the wrong way or music that should not be playing can lose viewers in the first minute. A short checklist protects the start of every stream, and it becomes faster with repetition. The aim is not to make the stream stiff, but to make sure the things that matter are already right.</p>
<p>The checklist below is grouped by the parts of the chain, from the room to the final test. Keep a printed copy near the setup, and tick each line before you press the button.</p>
<h2>The room and the microphone</h2>
<ul>
<li>Turn off fans, air conditioning and anything that hums or rattles.</li>
<li>Check the microphone position, at a hand’s width or two from the mouth.</li>
<li>Check that the cable is tidy, and that nothing rubs or pulls on the microphone.</li>
<li>Close the door if traffic, family or pets could interrupt.</li>
</ul>
<h2>The levels</h2>
<ul>
<li>Speak at your normal volume and check the voice level, with peaks well below the top.</li>
<li>Set the game and music so the voice is clearly the loudest source.</li>
<li>Check the alerts, which can be much louder than the voice if left unchecked.</li>
</ul>
<h2>The routing</h2>
<ul>
<li>Confirm each source goes to the path you planned, and nothing goes where it should not.</li>
<li>Check that private sounds, such as voice chat or notifications, do not reach the stream.</li>
<li>Test each mute, and confirm it works before you need it.</li>
<li>Check for an echo loop by speaking and listening on the other side.</li>
</ul>
<h2>Music and rights</h2>
<ul>
<li>Confirm that all music is licensed for live streaming on your platform.</li>
<li>Check that no music player or another app is running in the background.</li>
<li>Check whether any game you play contains music that could be detected.</li>
</ul>
<h2>Processing</h2>
<ul>
<li>Check that noise suppression, gates and compressors are set lightly.</li>
<li>Listen for artefacts on the consonants and for any cut-off at the start of words.</li>
<li>Confirm that any voice effect is clear and that the disclosure, if needed, is ready.</li>
</ul>
<h2>The final test</h2>
<ol>
<li>Start the stream as private or unlisted, and run a short test.</li>
<li>Watch the stream on a second device, with the sound on, and check the balance.</li>
<li>Ask a friend to listen and tell you whether the voice is clear.</li>
<li>Check the delay between speech and the picture, and fix any large lag.</li>
<li>Make the stream public, and keep a note of anything to change next time.</li>
</ol>
<h2>After the stream</h2>
<p>Save the stream recording, and check that it has the audio you expected. Make a note of any problem, the time it happened and what caused it. Over a few weeks, the notes show which steps prevent problems, and which ones you can drop.</p>
<h2>Set a pre-stream routine</h2>
<p>A routine that starts about fifteen minutes before the stream helps you arrive calm and prepared. Begin with the room and the microphone, then the levels, then the routing, and finish with the test. Following the same order each time means you never skip a step by accident, and the process stops feeling like a chore once it becomes habit.</p>
<p>Keep water nearby, and do the checks before you feel rushed. Starting a stream in a hurry is the most common reason the basics get missed.</p>
<p>Think of the checklist as a note to your future self, the one who is tired or distracted when the stream is about to start. Keep the wording plain, the steps short and the order the same every time, so the list stays quick to follow even on a difficult evening.</p>
<p>Review the checklist after every stream for a month, then once a month after that. Each review should ask one question: which line caught a problem, and which line never does? Keep the lines that catch things and retire the ones that never do, so the list stays short and useful. Add a short note beside any line that caused trouble, so next time the reason is already written down.</p>
<h2>Make the checklist yours</h2>
<p>A checklist should match your setup. Remove the lines that do not apply, add the ones that do, and reorder the steps to suit how you work. A checklist that fits your stream is one you will actually use, and every stream that goes well is a reason to keep it.</p>
<h2>Limits</h2>
<p>Platforms, software and hardware change, and some steps will need updating. Keep the checklist simple enough to use every time, and review it every few months. A checklist that is too long will be skipped.</p>
<h2>Start with clean sound</h2>
<p>A checklist catches mistakes, but clean sources prevent them. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> describes live noise cancellation for OBS, Discord and Zoom. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the levels in detail, read the <a href="/tunedzy/blog/stream-audio-levels-for-viewers">stream levels post</a> in this series.</p>
''',
    faq=[('How long should the checklist take?', 'A few minutes, most of which is the final test. It saves far more time than it costs.'),
         ('Do I need a checklist for a short stream?', 'Yes, a shorter version. The first minute matters just as much.'),
         ('What is the most common mistake?', 'An alert or a background app that is louder than the voice, found only after the stream starts.'),
         ('Should I test with the stream public?', 'Better not. Start as private or unlisted, and make it public once the test is clean.')])
