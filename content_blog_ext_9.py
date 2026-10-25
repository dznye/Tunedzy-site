"""Blog posts, batch 9 of 10: mics and recording gear cluster. Merged into content_blog.py.
Each post answers one search first, then explains it in plain steps, admits its limits, and links to a tool or guide.
No invented statistics, reviews, prices, product rankings or benchmarks. No product names are recommended."""

CLUSTERS = {
    'gear': dict(tool='clean-streaming-mic', label='Mics and recording gear', tool_name='Clean Streaming Mic'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='how-to-choose-headphones-for-audio-editing', cluster='gear', kw='best headphones for audio editing',
    title='How to Choose Headphones for Audio Editing',
    desc='How to choose headphones for audio editing: closed or open back, flat or coloured sound, comfort for long sessions and how to test them before you rely on them.',
    h1='How to Choose Headphones for Audio Editing',
    answer='For editing, choose closed-back headphones that are comfortable for long sessions and reproduce the middle and low frequencies accurately. Avoid strongly boosted bass, because it hides problems. Test them with your own recordings, and check the result on a phone speaker too.',
    body='''
<p>Headphones for editing have a different job from headphones for music. You need to hear problems clearly, such as noise, clicks and harshness, rather than enjoy a rich, boosted sound. The right pair is accurate and comfortable, and it lets you trust what you hear.</p>
<h2>Closed or open back</h2>
<p>Closed-back headphones seal the sound inside the ear cups. They keep outside noise out and reduce leakage, which suits a recording room. Open-back headphones sound more spacious and can feel more natural, but they let in outside sound and leak into a microphone. For editing alone, either can work; for recording, closed-back is usually safer.</p>
<h2>Flat or coloured sound</h2>
<p>A flat, accurate sound shows the true balance of a recording. A pair with a strong bass boost can make a voice sound full while hiding muddiness or rumble. Look for a balanced sound, and avoid anything that makes everything sound exciting, because it will mislead your edits.</p>
<h2>Comfort for long sessions</h2>
<p>You may wear headphones for hours. Check the weight, the clamping force and the padding. Ear cups that press too hard make you tire quickly, and tired ears make poor decisions. Try a pair for at least twenty minutes before you decide.</p>
<h2>Test with your own material</h2>
<p>Play a recording you know well, with clear speech and some background noise. Listen for the noise, the breaths and the level changes. If you can hear the problems you already know are there, the headphones are doing their job.</p>
<h2>Check on other speakers</h2>
<p>Headphones are only one listening place. Check the final edit on a phone speaker, a laptop and a car if you can. The <a href="/tunedzy/blog/what-is-dynamic-range-in-speech-audio">dynamic range post</a> explains why the listening place matters for the level.</p>
<h2>Limits</h2>
<p>No headphone is perfect for every job, and a good pair cannot replace a well-treated room. Choose the most accurate and comfortable pair you can afford, then use it with care.</p>
''',
    faq=[('Should I buy closed-back or open-back?', 'For recording, closed-back. For editing alone, either can work if you check on other speakers.'),
         ('Are bass-heavy headphones bad for editing?', 'They can be. A boosted bass hides muddiness and rumble, which you need to hear.'),
         ('How long should I test headphones?', 'At least twenty minutes, to check comfort and to judge the sound fairly.'),
         ('Do I need expensive headphones?', 'Not necessarily. Accuracy and comfort matter more than price, so test before you buy.')])

add(slug='pop-filter-vs-foam-windscreen', cluster='gear', kw='pop filter vs windscreen',
    title='Pop Filter vs Foam Windscreen: Which One Do You Need?',
    desc='Pop filter vs foam windscreen: how each one works, which problems they solve, when to use each, and how to place them for clear speech.',
    h1='Pop Filter vs Foam Windscreen: Which One Do You Need?',
    answer='A pop filter is a mesh screen placed between the mouth and the microphone, and it reduces plosive pops from speech. A foam windscreen covers the microphone and reduces wind and breath noise. For speech in a quiet room, a pop filter is the usual choice; for outdoor or windy recording, a foam windscreen is better.',
    body='''
<p>Both a pop filter and a foam windscreen sit between the speaker and the microphone, and both are cheap. They solve different problems, so buying the wrong one leaves the problem in place. Knowing which problem you have is the first step.</p>
<h2>What a pop filter does</h2>
<p>A pop filter is a mesh or fabric screen mounted a few centimetres in front of the microphone. It breaks up the burst of air from sounds such as &ldquo;p&rdquo; and &ldquo;b&rdquo;, which can thump the microphone. It works indoors, and it does not stop wind. The <a href="/tunedzy/blog/remove-mic-pops-plosives">plosive post</a> explains the sounds it targets.</p>
<h2>What a foam windscreen does</h2>
<p>A foam windscreen is a soft cover that fits over the microphone itself. It reduces air moving across the capsule, which is what causes wind noise, and it softens some breath sounds. It can also help with plosives, but it is mainly for air movement. A fuller furry cover is more effective outdoors.</p>
<h2>When to use each</h2>
<ul>
<li><strong>Indoors, close to the mouth:</strong> a pop filter, to stop plosive thumps.</li>
<li><strong>Indoors, with a fan or a draught:</strong> a foam windscreen, to reduce air movement.</li>
<li><strong>Outdoors or in wind:</strong> a furry cover over a foam windscreen.</li>
</ul>
<h2>Placement matters</h2>
<p>Place a pop filter a few centimetres in front of the microphone, and keep it between the mouth and the capsule. Too close and it touches the mouth; too far and it does little. A foam windscreen should fit snugly, without changing the sound of the voice.</p>
<h2>Limits</h2>
<p>A pop filter does not stop wind, and a foam windscreen does not replace good technique. Speak slightly off-axis, and keep the distance steady. The <a href="/tunedzy/blog/how-to-remove-wind-noise-from-a-recording">wind noise post</a> covers outdoor recording in more depth.</p>
''',
    faq=[('Can I use a foam windscreen instead of a pop filter?', 'It helps a little with plosives, but a pop filter is more effective for speech pops.'),
         ('Does a pop filter reduce wind?', 'No. Wind needs a foam or furry cover, not a mesh screen.'),
         ('How far should a pop filter be from the mic?', 'A few centimetres, between the mouth and the capsule, not touching either.'),
         ('Do I need both?', 'Not always. Indoors, a pop filter is often enough. Add a foam cover for air movement.')])

add(slug='how-to-set-up-a-boom-arm-for-a-microphone', cluster='gear', kw='boom arm for microphone setup',
    title='How to Set Up a Boom Arm for a Microphone',
    desc='How to set up a boom arm for a microphone: placing it at the right height and distance, balancing the arm, keeping the cable tidy and stopping vibration.',
    h1='How to Set Up a Boom Arm for a Microphone',
    answer='Set the boom arm so the microphone sits a hand&rsquo;s width or two from the mouth, slightly off-axis and at mouth height. Balance the arm so it stays where you put it, route the cable so it does not pull, and isolate the arm from the desk to stop vibration.',
    body='''
<p>A boom arm holds the microphone in the same place every session, and it frees the desk. Once it is set up well, the microphone stays close and steady, which is the most important part of clear speech. A poorly set boom arm can sag, vibrate or pick up cable noise, so the setup is worth doing carefully.</p>
<h2>Position the microphone</h2>
<p>Bring the arm over the desk so the microphone sits a hand&rsquo;s width or two from the mouth, slightly to one side. Keep it at mouth height, or a little below, so you do not have to lean. Mark the position on the desk, so you can return to it.</p>
<h2>Balance the arm</h2>
<p>Most arms have a tension adjustment. Set it so the microphone stays where you leave it, without drooping, and without needing a strong grip to move it. A well-balanced arm lets you adjust with one hand.</p>
<h2>Route the cable</h2>
<p>Run the cable along the arm and secure it with clips or ties, leaving slack at each joint. A tight cable pulls on the microphone and transmits noise. Keep the cable away from power cables, to reduce hum.</p>
<h2>Stop vibration</h2>
<p>Desks transmit vibration, from keyboard taps, footsteps and the chair. Clamp the arm to a sturdy part of the desk or a stand, and place a soft pad under the clamp if you can. Test by tapping the desk while recording a short sample.</p>
<h2>Check the sound</h2>
<p>Record a test, listen on headphones, and check for pops, rumble and cable noise. Adjust the position and the arm, then record again. The <a href="/tunedzy/how-to-test-your-room-for-echo">clap test</a> helps you find the best spot in the room.</p>
<h2>Limits</h2>
<p>A boom arm does not fix a noisy room or a poor microphone. It makes the setup consistent, which helps every recording sound more even. Treat it as a tool for stability, not a cure for everything else.</p>
''',
    faq=[('How close should the microphone be?', 'About a hand&rsquo;s width or two from the mouth, slightly off-axis.'),
         ('Why does my boom arm drift down?', 'The tension is too loose. Adjust it so the arm holds its position.'),
         ('How do I stop desk noise?', 'Clamp the arm to a sturdy part of the desk, add a soft pad, and avoid tapping the desk while recording.'),
         ('Should the cable be tight?', 'No. Leave slack at each joint, so the cable does not pull on the microphone.')])

add(slug='do-i-need-an-audio-interface-for-voice', cluster='gear', kw='do I need an audio interface',
    title='Do You Need an Audio Interface for Voice Recording?',
    desc='Do you need an audio interface for voice recording: when a USB microphone is enough, what an interface does, and when it becomes worth buying.',
    h1='Do You Need an Audio Interface for Voice Recording?',
    answer='You do not need an audio interface for simple voice recording. A USB microphone connects straight to a computer and is enough for most home work. An interface becomes useful when you use an XLR microphone, need more than one input, or want more control over the gain and monitoring.',
    body='''
<p>An audio interface converts a microphone&rsquo;s signal into digital audio for a computer, and it usually provides a gain control and a headphone output. Many people buy one too early, when a simpler setup would do. The question is what the interface would add to the way you record.</p>
<h2>When a USB microphone is enough</h2>
<p>A USB microphone plugs straight into a computer and includes its own converter. It is simple, cheap and sufficient for most solo voice recording, podcasts and voice-overs. If you record one voice in one room, a USB microphone is usually the right place to start.</p>
<h2>When an interface helps</h2>
<ul>
<li>You want to use an XLR microphone, which needs an interface or a preamp.</li>
<li>You record more than one person at the same time, and need several inputs.</li>
<li>You want a dedicated gain control and direct monitoring with no delay.</li>
<li>You plan to upgrade the microphone later, and want a setup that grows with you.</li>
</ul>
<h2>What to check before you buy</h2>
<p>Check the number of inputs, the type of connection your computer has, and whether the interface needs its own power. Look for a headphone output with enough level for your headphones. Test the setup with your own voice before you rely on it.</p>
<h2>Gain staging still matters</h2>
<p>Whatever you use, set the gain so the peaks stay well below the top, and the quiet parts are clear. An interface with a gain knob makes this easier, but it does not replace listening. The <a href="/tunedzy/blog/how-much-headroom-to-leave-in-audio">headroom post</a> explains the margin to leave.</p>
<h2>Limits</h2>
<p>An interface does not improve a poor room or a noisy environment. Spend first on the room and the microphone position. Add an interface when the setup needs it, not because it looks like part of a serious studio.</p>
''',
    faq=[('Is a USB microphone as good as an interface setup?', 'For one voice in one room, it is often just as good. The difference is in flexibility, not always sound quality.'),
         ('When do I need phantom power?', 'For condenser microphones that need it. The next post explains it.'),
         ('Can I record a second person on a USB mic?', 'It is harder. Two microphones usually need an interface with two inputs.'),
         ('What should I buy first?', 'Usually a good microphone position, a quiet room and a simple setup. An interface can wait.')])

add(slug='what-is-phantom-power-and-when-you-need-it', cluster='gear', kw='when to switch on phantom power',
    title='What Is Phantom Power and When Do You Need It?',
    desc='What is phantom power: the 48-volt supply that some microphones need, how to tell whether your microphone needs it, and the safety checks before you switch it on.',
    h1='What Is Phantom Power and When Do You Need It?',
    answer='Phantom power is a 48-volt supply sent down the microphone cable from an interface or a mixer, to power condenser microphones. Dynamic and most USB microphones do not need it. Check your microphone&rsquo;s instructions, and switch phantom power on only after the other equipment is connected and the levels are down.',
    body='''
<p>Phantom power is one of the most confusing terms for new recordists, and it is also one of the easiest to understand once you know the basics. It sends power to a microphone through the same cable that carries the audio. Some microphones need it, and some are damaged by it if it is switched on by mistake.</p>
<h2>What it does</h2>
<p>Condenser microphones have a small internal circuit that needs power to work. Phantom power supplies that power, usually at 48 volts, down the XLR cable. The microphone then sends its audio back along the same cable. Most condenser microphones need it, and most dynamic microphones do not.</p>
<h2>Which microphones need it</h2>
<p>Check the microphone&rsquo;s instructions. Condenser microphones usually need phantom power, and dynamic microphones usually do not. USB microphones have their own power, so they do not use phantom power. Ribbon microphones can be damaged by it, so check before you connect them.</p>
<h2>How to use it safely</h2>
<ol>
<li>Turn the level down on the interface or the mixer.</li>
<li>Connect the microphone and the cables.</li>
<li>Switch phantom power on only if the microphone needs it, and check its instructions.</li>
<li>Raise the level slowly, and listen before you record.</li>
</ol>
<h2>Common mistakes</h2>
<p>Switching phantom power on or off while a microphone is connected to a live channel can cause a loud pop, which can damage speakers and headphones. Do not switch it with the level high. Turn the monitoring down first, then make the change.</p>
<h2>Limits</h2>
<p>Phantom power is safe for most modern condenser microphones, but some older or specialist microphones are not. If you are unsure, check the manufacturer&rsquo;s guidance, and ask a knowledgeable person before you connect anything.</p>
''',
    faq=[('Does a dynamic microphone need phantom power?', 'Usually not. Check the instructions for your microphone.'),
         ('Can phantom power damage a microphone?', 'Some ribbon and older microphones can be damaged. Check before switching it on.'),
         ('Why did I hear a loud pop?', 'Phantom power was switched on or off while the level was high. Turn the level down first.'),
         ('Does a USB microphone need phantom power?', 'No. USB microphones have their own power supply.')])

add(slug='microphone-stand-setup-for-voice', cluster='gear', kw='microphone stand setup for voice',
    title='How to Set Up a Microphone Stand for Voice',
    desc='How to set up a microphone stand for voice: choosing a stable stand, the right height and angle, keeping it steady and avoiding common placement mistakes.',
    h1='How to Set Up a Microphone Stand for Voice',
    answer='Set the stand on a stable base, raise the microphone to mouth height, and angle it slightly off-axis from the mouth. Keep the stand away from the desk and the chair, tighten all the joints, and test for vibration before you record.',
    body='''
<p>A microphone stand looks simple, but a wobbly or badly placed stand causes many recording problems. It moves when you move, it transmits vibration, and it can change the distance without you noticing. A stable setup is more important than an expensive microphone.</p>
<h2>Choose a stable base</h2>
<p>A heavy, wide base keeps the stand still. A thin or light base tips easily and sends vibration into the microphone. If the stand is on a desk, check that the desk does not rattle when you tap it.</p>
<h2>Set the height and angle</h2>
<p>Raise the microphone to mouth height, or slightly below, so you can speak without leaning. Angle the capsule slightly off-axis from the mouth, so breath does not hit it directly. Mark the position on the stand or the desk, so you can return to it.</p>
<h2>Keep it away from noise</h2>
<p>Place the stand away from the chair, the keyboard and the desk edge. Avoid putting it on a surface that carries footsteps or fan vibration. A small pad under the base can help.</p>
<h2>Tighten and test</h2>
<p>Tighten all the joints, then record a short test while you tap the desk gently. Listen on headphones for thumps, rumble and changes in the voice. Adjust the stand, then record again until it is quiet.</p>
<h2>Limits</h2>
<p>A stand cannot fix a noisy room, and a heavy stand may be harder to move around. Choose a stand that suits your space, and keep the setup stable from session to session.</p>
''',
    faq=[('What height should a mic stand be?', 'Around mouth height, or slightly below, so you can speak without leaning.'),
         ('Why does my voice change when I move?', 'The distance or angle changes. Mark the position and keep your seat the same.'),
         ('Does a heavier stand help?', 'Usually yes, because it is more stable and carries less vibration.'),
         ('Should the stand touch the desk?', 'It can, but a soft pad under the base reduces vibration.')])

add(slug='dynamic-microphone-for-speech-explained', cluster='gear', kw='dynamic microphone for speech',
    title='Why a Dynamic Microphone Suits Speech in Untreated Rooms',
    desc='Why a dynamic microphone suits speech in untreated rooms: how it handles room noise, why it needs close placement and when a condenser is the better choice.',
    h1='Why a Dynamic Microphone Suits Speech in Untreated Rooms',
    answer='A dynamic microphone suits speech in an untreated room because it picks up less of the room and less background noise, especially when placed close to the mouth. It needs more gain and close placement, but it is forgiving of imperfect spaces. A condenser suits a quiet, treated room better.',
    body='''
<p>Dynamic microphones are often overlooked in favour of condensers, which are more sensitive and detailed. For speech in a home room, the dynamic has real advantages. It is robust, and it handles the reflections and noise of an untreated space better than many people expect.</p>
<h2>How a dynamic works</h2>
<p>A dynamic microphone uses a moving coil in a magnetic field, and it does not need external power. It is less sensitive than a condenser, which means it captures less of the room and less of the quiet background noise. That is useful when the room is not ideal.</p>
<h2>Why it suits speech</h2>
<p>Placed close to the mouth, a dynamic gives a warm, focused sound with little room reflection. It is also less likely to pick up fan noise, traffic and computer hum. Many broadcast voices use dynamic microphones for that reason.</p>
<h2>What it needs</h2>
<p>A dynamic needs more gain than a condenser, which can add some noise at the preamp. It also needs close placement, so keep the distance steady. Check the level before you record, and set the gain so the peaks stay below the top.</p>
<h2>When a condenser is better</h2>
<p>A condenser suits a quiet, treated room and a singer who needs fine detail. It captures more of the room too, so it is less forgiving of noise and echo. Choose it when your space is quiet and soft, and when you want detail rather than focus.</p>
<h2>Limits</h2>
<p>No microphone can fix a poor room, and a dynamic in a bare room will still sound echoey if it is placed far away. Use the microphone close, and soften the room, whichever type you choose.</p>
''',
    faq=[('Is a dynamic microphone good enough for a podcast?', 'Yes, for speech. Place it close, and keep the room as soft as you can.'),
         ('Why does a dynamic need more gain?', 'It produces a smaller signal than a condenser, so the preamp must boost it more.'),
         ('Can a dynamic sing as well as a condenser?', 'It can sound very good for singing, but the sound differs. Try both if you can.'),
         ('Does a dynamic need phantom power?', 'No. It generates its own signal, so phantom power is not needed.')])

add(slug='why-clean-a-microphone-and-how-to-do-it', cluster='gear', kw='how to clean a microphone',
    title='How to Clean a Microphone and Look After It',
    desc='How to clean a microphone and look after it: removing dust and saliva safely, cleaning the windscreen and pop filter, storing the microphone and avoiding damage.',
    h1='How to Clean a Microphone and Look After It',
    answer='Clean a microphone gently: wipe the body with a dry or lightly damp cloth, remove the grille cover only if the manual allows it, and clean the pop filter or windscreen regularly. Store the microphone in a dry place, and never spray cleaner directly onto it.',
    body='''
<p>A microphone collects dust, skin oil and saliva over time, and each of these can affect the sound. A clean microphone sounds more consistent, and it lasts longer. Cleaning is simple, but it needs care, because some parts are delicate.</p>
<h2>Clean the body gently</h2>
<p>Wipe the outside with a dry or lightly damp microfibre cloth. Avoid soaking the cloth, and never spray cleaner directly onto the microphone. Keep liquid away from the connector and any switches.</p>
<h2>Check the grille</h2>
<p>The grille protects the capsule. Some microphones can be cleaned with a soft brush, while others should not be touched at all. Check the manual before you clean the grille, and never poke inside the capsule.</p>
<h2>Clean the windscreen and pop filter</h2>
<p>A pop filter or foam windscreen collects saliva and dust, and it can smell over time. Wash a mesh pop filter in warm water with mild soap, then let it dry fully. Replace a foam windscreen when it becomes dirty or stiff. The <a href="/tunedzy/blog/pop-filter-vs-foam-windscreen">pop filter comparison</a> explains which one suits which job.</p>
<h2>Store it well</h2>
<p>Keep the microphone in a dry place, away from heat and dust, and in a case or a cover if you have one. Coil the cable loosely, rather than tightly, so it does not kink.</p>
<h2>Limits</h2>
<p>If a microphone is damaged, has a loose connector or sounds wrong after cleaning, stop using it and check the manufacturer&rsquo;s guidance. A repair is usually better than a DIY fix on a delicate part.</p>
''',
    faq=[('Can I wash a microphone in water?', 'No. Wipe the body with a lightly damp cloth, and wash only the removable pop filter.'),
         ('How often should I clean a pop filter?', 'Regularly, especially if it collects saliva or dust. Replace it when it stops looking clean.'),
         ('Should I clean the grille?', 'Only if the manual allows it. Some grilles should not be touched.'),
         ('How should I store the cable?', 'Coil it loosely, so it does not kink, and keep it away from heat.')])

add(slug='do-i-need-a-studio-to-record-voice', cluster='gear', kw='do I need a studio to record voice',
    title='Do You Need a Studio to Record a Good Voice?',
    desc='Do you need a studio to record a good voice: what a studio really provides, what a home setup can do, and the priorities that matter most for clear speech.',
    h1='Do You Need a Studio to Record a Good Voice?',
    answer='You do not need a studio to record a good voice. A quiet, soft room, a close microphone and a steady setup do most of the work. A studio adds a treated room and a controlled chain, which helps, but it is not required for clear, pleasant speech at home.',
    body='''
<p>Many people think a good voice recording needs an expensive studio. In practice, most of the quality comes from the room, the microphone position and the care taken during the recording. A studio helps with consistency and with difficult jobs, but it is not the only route to a clear voice.</p>
<h2>What a studio really gives you</h2>
<p>A professional studio has a treated room that controls reflections, a quiet space that excludes noise, and equipment that is set up consistently. It also gives you someone else to manage the room and the chain. These are valuable, but each can be approximated at home with more modest means.</p>
<h2>What a home setup can do</h2>
<p>A soft room, such as a bedroom or a wardrobe, reduces echo well. A close microphone with a pop filter gives clear speech. A steady setup and a short test catch most problems. Together these produce a clean recording for podcasts, voice-overs and online video.</p>
<h2>Priorities for a home recording</h2>
<ol>
<li>A quiet room, with the fans and traffic off.</li>
<li>A soft space around the speaker.</li>
<li>A close, steady microphone position.</li>
<li>Gentle cleanup, and a level that stays clear of the peaks.</li>
</ol>
<h2>When a studio is worth it</h2>
<p>A studio helps for music recording with several instruments, for work that must meet strict technical standards, or when you need a team and a controlled environment. For a single voice in a home room, a well-set-up space is often enough. Try the home setup first, and decide from the results.</p>
<h2>Limits</h2>
<p>A home room has limits, and some work will sound better in a studio. Know what the work needs, and choose the setup to meet it, not the other way round.</p>
''',
    faq=[('What is the most important part of a home setup?', 'The room and the microphone position. They matter more than any single piece of equipment.'),
         ('Is a closet really a good space?', 'It often is, if it is soft inside and you test it. Keep the door closed and the microphone close to the clothes.'),
         ('When should I book a studio?', 'For music with several instruments, strict standards or when a controlled environment is needed.'),
         ('Can a home recording pass as professional?', 'For many podcasts and voice-overs, yes, when the room, position and cleanup are right.')])

add(slug='what-is-a-reflection-filter-and-does-it-help', cluster='gear', kw='what is a reflection filter',
    title='What Is a Reflection Filter and Does It Help?',
    desc='What is a reflection filter: a panel placed behind a microphone to soak up room reflections, when it helps, what it cannot do and how to test it.',
    h1='What Is a Reflection Filter and Does It Help?',
    answer='A reflection filter is a small panel placed behind and around a microphone to absorb sound that would otherwise bounce back into it from the room. It can help in a bright, reflective space, but it works best alongside soft surfaces, and it does nothing about noise coming from outside.',
    body='''
<p>A reflection filter, sometimes called a sound shield or an isolation panel, is a soft, absorbent panel that stands behind or beside the microphone. Its job is to soak up reflections from the room, so the microphone hears more of the voice and less of the echo. It is a useful tool, but it is often oversold as a cure for a bad room.</p>
<h2>What it does</h2>
<p>Sound from the speaker reaches the microphone directly, and also after bouncing off walls, a desk or a ceiling. The reflections arrive a fraction of a second later and blur the voice. A reflection filter absorbs some of the sound that would reflect toward the microphone from behind it, which reduces that blur.</p>
<h2>When it helps</h2>
<ul>
<li>The room is hard, with bare walls or glass behind the microphone.</li>
<li>You cannot add soft fabrics behind the microphone.</li>
<li>The desk surface is very reflective, and sound bounces up into the capsule.</li>
</ul>
<h2>What it cannot do</h2>
<p>A reflection filter does not stop noise from outside, such as traffic, fans or a neighbour. It also does not absorb sound in front of the microphone, where most of the voice comes from. A small panel in a large, bright room has limited effect. It is not a substitute for soft furnishings or a well-chosen room.</p>
<h2>Placement</h2>
<p>Place the panel behind the microphone, on the side facing the room, with the microphone on the open side. Keep it a little above and behind the capsule, not directly beside the mouth. Test a few positions, rather than assuming the first one is right.</p>
<h2>How to test it</h2>
<p>Record a short sample with the panel in place, then move it away and record again. Use the same distance, level and text. Listen on headphones and compare the echo and the clarity. If the difference is small, a blanket or a rug may do the same job for less.</p>
<h2>Limits</h2>
<p>A reflection filter works best as one part of a soft setup, not as the whole plan. Treat it as a small improvement, and check the result on your own recordings.</p>
''',
    faq=[('Is a reflection filter the same as acoustic foam?', 'No. A filter is a small panel for the space behind the microphone. Foam treats wider areas of a room.'),
         ('Can a reflection filter remove echo completely?', 'No. It reduces some reflections from behind the microphone, but the rest of the room still matters.'),
         ('Do I need one if my room is soft?', 'Probably not. Soft furnishings already do much of the same work.'),
         ('How do I know if it is working?', 'Record with and without it, at the same distance and level, and compare the echo on headphones.')])
