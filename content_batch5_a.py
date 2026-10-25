"""Batch 5a (25 October 2026): eight glossary pages. Each gives one plain definition first, why it matters for a voice, and how to check it.

GROUP_OF marks every page 'glossary' for the guides hub.
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
    GROUP_OF[slug] = 'glossary'


add('what-is-clipping', 'neon-wide', ['vocal-checker', 'lufs-meter'],
    title='What Is Clipping in Audio? Plain Explanation',
    desc='Clipping is what happens when a sound is louder than the recorder can store, so its peaks are flattened. Why it sounds harsh and how to avoid it.',
    h1='What Is Clipping?',
    kw='what is clipping in audio',
    lead='Clipping happens when a sound is louder than a digital recording can store. The loudest peaks are cut flat, and the sound becomes harsh and fuzzy.',
    tldr=['Clipping flattens the tops of the waveform when a sound exceeds full scale.',
          'It sounds like a harsh, buzzy distortion on the loudest words.',
          'It cannot be undone in the original; it can only be softened by repair.',
          'Record with peaks well below full scale to avoid it.'],
    body='''
<h2>The short definition</h2>
<p>A digital recording has a top level called full scale. Any sound louder than that cannot be stored, so the recorder cuts it off. On a waveform, the peaks look flat, like a plateau, where the real sound kept rising. That flattening is clipping.</p>
<h2>What it sounds like</h2>
<p>Clipping adds harsh overtones that were not in the original. It sounds like fuzz, crackle or buzz on loud consonants and laughs. A little on a single shout may hardly be noticed; clipping on every word is very obvious.</p>
<h2>Why it is hard to undo</h2>
<p>Once the peaks are flat, the information is gone. Repair tools can rebuild some clipped peaks from the wave around them, but heavy clipping cannot be rebuilt reliably. The <a href="/tunedzy/fix-clipped-distorted-audio">clipping repair guide</a> explains what is possible.</p>
<h2>How to avoid it</h2>
<p>Set the input so the loudest words peak well below the top of the meter, around -6 dB, and keep some headroom. Move the mic a little further away if the peaks are high, rather than turning the gain up and down.</p>
<h2>How to check it</h2>
<p>Look for flat tops on the waveform in your editor, and listen for a harsh edge on the loudest words. The <a href="/tunedzy/tools/vocal-checker">vocal checker</a> flags clipping in a file on this site.</p>
''',
    vf_title='Check the peaks before you record',
    vf='<p>Tunedzy&rsquo;s Repair finds flat-topped clipping and rebuilds what it can. Record with headroom to avoid needing it.</p>',
    faq=[('Is clipping always bad?', 'Yes for voice. A very short clip on one sound may be hardly noticeable, but repeated clipping is harsh.'),
         ('Does a limiter prevent clipping?', 'A limiter keeps future peaks under a ceiling. It does not repair peaks that already clipped.'),
         ('What is the difference between clipping and distortion?', 'Clipping is one kind of distortion, caused by going beyond full scale. Other distortion can come from overloaded gear.')],
    related=['fix-clipped-distorted-audio', 'what-is-headroom', 'my-recording-is-too-quiet'])

add('what-is-a-pop-filter', 'booth', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='What Is a Pop Filter? Plain Explanation',
    desc='A pop filter is a mesh screen between the mouth and the mic that softens the burst of air from p and b sounds. How it works and where to place it.',
    h1='What Is a Pop Filter?',
    kw='what is a pop filter',
    lead='A pop filter is a mesh or foam screen placed between the speaker and the microphone. It softens the rush of air from p and b sounds, which otherwise makes a loud thump.',
    tldr=['A pop filter diffuses the air burst from plosive sounds such as p and b.',
          'It sits between the mouth and the mic, a few centimetres from the mic.',
          'It does not reduce room noise or echo.',
          'A foam cover on the mic does a similar job more cheaply.'],
    body='''
<h2>The short definition</h2>
<p>A pop filter is a screen, usually a fine mesh or a layer of foam, placed between the speaker and the microphone. When you say a p or a b, a puff of air hits the capsule. The screen spreads that air out so the mic does not register a loud thump.</p>
<h2>Where to put it</h2>
<p>Place the filter a few centimetres in front of the mic, and keep the speaker about a hand&rsquo;s width from the filter. Putting it too close to the mic does not help; putting it too far lets the air still reach the capsule.</p>
<h2>What it does not do</h2>
<p>A pop filter does not reduce hiss, room sound or echo. It only handles the air burst. For a pop that has already been recorded, see the <a href="/tunedzy/blog/remove-mic-pops-plosives">pop removal guide</a>.</p>
<h2>A cheaper alternative</h2>
<p>A foam windscreen or cover over the mic head does a similar job for many setups and takes up less space on the desk.</p>
''',
    vf_title='Fewer pops, cleaner voice',
    vf='<p>A pop filter stops the pops at the source. Tunedzy can soften a pop that slipped through.</p>',
    faq=[('Do I need a pop filter for every mic?', 'Most close-up voice recording benefits from one. A distant mic picks up fewer pops.'),
         ('Can a pop filter reduce background noise?', 'No. It only handles the air from the mouth.'),
         ('Is a foam cover enough?', 'Often, for voice. Mesh screens are more effective for strong plosives.')],
    related=['clean-up-a-phone-voice-recording', 'how-to-choose-a-microphone-for-voice-recording', 'what-is-a-shock-mount'])

add('what-is-a-shock-mount', 'desk', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='What Is a Shock Mount? Plain Explanation',
    desc='A shock mount holds a microphone on elastic bands so that desk knocks and footsteps do not travel into the recording. When it helps and when it does not.',
    h1='What Is a Shock Mount?',
    kw='what is a shock mount',
    lead='A shock mount holds a microphone in a cradle of elastic bands, so vibrations through the stand, desk or floor do not reach the capsule.',
    tldr=['A shock mount isolates the mic from vibration through the stand and desk.',
          'It stops thumps from footsteps, typing and bumps reaching the recording.',
          'It does not reduce airborne noise such as a fan or voices in the room.',
          'It helps most on a boom arm or a desk stand that carries knocks.'],
    body='''
<h2>The short definition</h2>
<p>A shock mount is a bracket that suspends the microphone on elastic bands or springs. Vibration that travels through the stand, the arm or the desk is absorbed by the bands before it reaches the microphone.</p>
<h2>What it stops</h2>
<p>Typing on a desk, a knock on the stand, footsteps on a wooden floor and the thump of a boom arm being moved. These all travel through solid parts and into the capsule as low rumble or sharp knocks.</p>
<h2>What it does not stop</h2>
<p>Sound in the air, such as a fan, traffic or other people talking, still reaches the mic. A shock mount is about solid vibration, so pair it with a soft room and a close mic.</p>
<h2>When you need one</h2>
<p>If your mic sits on a desk or boom arm and you hear every tap, a shock mount is worth trying. A mic held on a stand with a soft base often needs none.</p>
''',
    vf_title='Isolate the desk from the mic',
    vf='<p>A shock mount stops solid knocks. Tunedzy&rsquo;s cleanup handles the steady noise that remains.</p>',
    faq=[('Is a shock mount the same as a pop filter?', 'No. A pop filter handles air from the mouth; a shock mount handles vibration through the stand.'),
         ('Can I use a shock mount on a phone?', 'Phones usually have no mount for one, but a phone holder with soft padding can reduce knocks.'),
         ('Does it reduce the room?', 'No. It isolates the mic from solid vibration only.')],
    related=['what-is-a-pop-filter', 'how-to-remove-keyboard-and-desk-noise-from-a-recording', 'how-to-set-up-a-quiet-recording-corner-on-a-budget'])

add('what-is-phantom-power', 'mic-wide', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='What Is Phantom Power? Plain Explanation',
    desc='Phantom power is 48 volts sent down an XLR cable to power condenser microphones. What it is, when you need it and when it can damage a mic.',
    h1='What Is Phantom Power?',
    kw='what is phantom power',
    lead='Phantom power is a 48-volt supply sent down an XLR cable from a mixer or interface. It powers condenser microphones, which cannot work without it.',
    tldr=['Phantom power is usually 48 volts, sent down the XLR cable.',
          'Condenser mics need it; dynamic mics do not.',
          'Switching it on can damage some ribbon or older mics, so check the mic first.',
          'USB mics have their own power and do not need it.'],
    body='''
<h2>The short definition</h2>
<p>Phantom power is a DC voltage, usually 48 volts, that travels down the same XLR cable that carries the audio. It is called phantom because it is invisible to a dynamic mic, which ignores it. A condenser mic uses it to power its internal electronics.</p>
<h2>Which mics need it</h2>
<p>Condenser microphones need phantom power. Most dynamic microphones do not. A USB condenser has its own power from the computer, so it does not need a separate supply.</p>
<h2>How to use it</h2>
<p>Turn phantom power on at the mixer or interface only when a condenser mic is connected, or check the mic&rsquo;s manual first. Some ribbon microphones and older vintage mics can be damaged by it, so many people switch it off for those.</p>
<h2>Common mistakes</h2>
<p>Switching phantom power on or off while a mic is plugged in can cause a loud pop through the speakers. Turn the monitor volume down first, then change the power.</p>
''',
    vf_title='Power the mic, keep the voice clean',
    vf='<p>Tunedzy cleans the recording from any mic, including condensers. Check the power setup on your interface.</p>',
    faq=[('Will phantom power harm a dynamic mic?', 'Usually not. Most dynamic mics ignore it. Ribbon mics are the exception to check.'),
         ('Do I need phantom power for a USB mic?', 'No. USB mics are powered by the computer.'),
         ('What voltage is phantom power?', 'Usually 48 volts, although the standard allows other values for some uses.')],
    related=['what-is-a-condenser-vs-dynamic-microphone', 'how-to-choose-a-microphone-for-voice-recording', 'how-to-record-with-a-usb-microphone'])

add('what-is-the-proximity-effect', 'booth-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='What Is the Proximity Effect? Plain Explanation',
    desc='The proximity effect is the rise in bass when a directional microphone is very close to a voice. Why it happens, when it helps and how to control it.',
    h1='What Is the Proximity Effect?',
    kw='what is the proximity effect',
    lead='The proximity effect is the extra bass a directional microphone adds when a sound source is very close to it. It can make a voice warm and full, or boomy and muddy.',
    tldr=['Directional mics boost low frequencies when the source is very close.',
          'A little proximity can add warmth; too much makes a voice boomy.',
          'Control it by changing the distance, the angle or a high-pass filter.',
          'It is normal and expected, not a fault in the mic.'],
    body='''
<h2>The short definition</h2>
<p>A directional microphone, such as a cardioid, picks up sound by comparing pressure at the front and back of its capsule. When the source is close, the bass pressure difference grows, so the low frequencies are boosted. That is the proximity effect.</p>
<h2>When it helps</h2>
<p>A little proximity gives a voice warmth and intimacy, which is why radio voices often sit close to the mic. For a narrator or a singer who wants a full sound, a close distance can be a deliberate choice.</p>
<h2>When it hurts</h2>
<p>Too close, the voice booms and the words become muddy. The low frequencies mask the clarity of speech. The <a href="/tunedzy/blog/how-to-fix-boomy-vocals-proximity-effect">boomy vocals guide</a> explains how to fix it in a recording.</p>
<h2>How to control it</h2>
<p>Move back a few centimetres, speak slightly off-axis, or use a high-pass filter around 80 to 120 Hz to remove the extra rumble without losing the warmth.</p>
''',
    vf_title='Keep the warmth, lose the boom',
    vf='<p>Tunedzy&rsquo;s tone step shapes the low end. Use Before and After to keep the warmth without the boom.</p>',
    faq=[('Is the proximity effect a fault?', 'No. It is how directional mics respond to close sources.'),
         ('Do all mics have it?', 'Directional mics have it. Omnidirectional mics do not, to the same degree.'),
         ('How do I hear it?', 'Record the same phrase at two distances and compare the low end.')],
    related=['how-to-make-a-voice-sound-close-and-intimate', 'what-is-a-high-pass-filter', 'what-is-an-equalizer'])

add('what-is-a-noise-floor', 'desk-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='What Is the Noise Floor? Plain Explanation',
    desc='The noise floor is the quietest level in a recording, the background hiss and room sound under the voice. Why it matters and how to measure it.',
    h1='What Is the Noise Floor?',
    kw='what is the noise floor',
    lead='The noise floor is the level of the background in a recording: the hiss, hum and room sound you hear when nobody is speaking. The lower it is, the cleaner the voice sounds.',
    tldr=['The noise floor is the quietest level, the background under silence.',
          'Speech must sit well above the noise floor to sound clear.',
          'Lower the noise floor by a quieter room and a closer mic, not only by cleanup.',
          'Measure it by recording a few seconds of silence.'],
    body='''
<h2>The short definition</h2>
<p>The noise floor is the background level of a recording. It is what remains when nobody is speaking: hiss from the electronics, the room, a fan, traffic. Everything in a recording sits above that floor.</p>
<h2>Why it matters</h2>
<p>The gap between the voice and the noise floor decides how clear the voice sounds. A voice 40 dB above a low noise floor is clear; the same voice 15 dB above a high one sounds muddy. Cleanup works by lowering the floor, but it works best when the floor starts low.</p>
<h2>How to lower it</h2>
<p>Record in a quieter room, turn off the fans and fridge, and place the mic closer to the mouth. A closer mic raises the voice relative to the room, which has the same effect as lowering the floor.</p>
<h2>How to measure it</h2>
<p>Record ten seconds of silence with the same settings, then look at its level in your editor or on a noise meter. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone guide</a> explains how to record it properly.</p>
''',
    vf_title='Record a quiet floor first',
    vf='<p>Tunedzy&rsquo;s cleanup lowers the noise floor. A quieter room before you record gives it less to do.</p>',
    faq=[('Is a low noise floor the same as no noise?', 'No. There is always some background. A low floor is the aim.'),
         ('What is a good noise floor for voice?', 'Lower is better. Measure your room and compare; there is no single target.'),
         ('Does cleanup raise the floor?', 'Cleanup lowers the floor. Heavy cleanup can make the remaining floor sound unnatural.')],
    related=['how-to-set-up-a-quiet-recording-corner-on-a-budget', 'remove-background-noise-from-a-voice-recording', 'what-is-headroom'])

add('what-is-gain-staging', 'booth', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='What Is Gain Staging? Plain Explanation',
    desc='Gain staging means setting the level at each step of a recording chain, so each stage works well and nothing clips or drowns in noise.',
    h1='What Is Gain Staging?',
    kw='what is gain staging',
    lead='Gain staging is setting the level at each step of a recording chain: the mic, the preamp, the interface, the software. Done well, each step works in its best range and the recording stays clean.',
    tldr=['Each step in the chain has a range where it sounds best.',
          'Set the input first, so the signal is strong without clipping.',
          'Avoid raising the level later in each step; set it once at the start.',
          'Check the peaks at the end, after every step is set.'],
    body='''
<h2>The short definition</h2>
<p>Gain is the amount a signal is made louder or quieter. Staging means arranging the gain at each stage of the chain, so the signal stays in a good range from the mic to the file. Too little gain and the noise of the electronics shows; too much and the signal clips.</p>
<h2>A simple order</h2>
<ol>
<li>Set the mic position and distance first.</li>
<li>Set the input gain on the preamp or interface, so the loudest words peak around -6 dB.</li>
<li>Leave the software fader at a sensible level, not at the top or bottom.</li>
<li>Check the peaks of the finished recording.</li>
</ol>
<h2>What to avoid</h2>
<p>Turning the input up to the top and then turning the software down is a common mistake. It can add noise from the early stages. Set the strongest clean level at the input instead.</p>
<h2>Why it matters for cleanup</h2>
<p>A recording with good gain staging needs less cleanup, because the voice already sits well above the noise. The <a href="/tunedzy/what-is-headroom">headroom guide</a> explains the peak target.</p>
''',
    vf_title='Set the level once, record clean',
    vf='<p>Tunedzy works best on a recording with sensible gain. Check the peaks before you record, and let the cleanup do the rest.</p>',
    faq=[('What is the first thing to set?', 'The input gain on the mic or interface, with the mic position fixed.'),
         ('Should the software fader be at maximum?', 'No. Keep the input strong and clean, and use the fader only for small changes.'),
         ('Is gain staging only for studios?', 'No. Any recording chain, including a USB mic and a laptop, has gain stages.')],
    related=['what-is-headroom', 'how-to-set-the-gain-on-a-microphone', 'my-recording-is-too-quiet'])

add('what-is-ducking', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='What Is Ducking in Audio? Plain Explanation',
    desc='Ducking lowers background music automatically while a voice speaks, then brings it back up. What it is, how it sounds and how to set it.',
    h1='What Is Ducking?',
    kw='what is ducking in audio',
    lead='Ducking is lowering background music or effects automatically while a voice is speaking, then raising them again when the voice stops. It keeps the words clear without losing the music.',
    tldr=['Ducking lowers the music while the voice is active.',
          'It is triggered by the voice, so the music returns between phrases.',
          'Keep the change gentle, so the music does not pump in and out.',
          'It is the standard way to put a voice over a bed of music.'],
    body='''
<h2>The short definition</h2>
<p>Ducking is a form of automatic level control. The voice is the trigger: when it speaks, the music or effects are turned down by a set amount, and when the voice stops, they come back. The name comes from the way the music seems to duck out of the way.</p>
<h2>What it sounds like</h2>
<p>Done well, the music sits under the voice and rises gently in the gaps. Done badly, the music pumps: it jumps up and down with every word, which is distracting.</p>
<h2>Setting it</h2>
<p>Set the amount of reduction first, usually a few decibels to around ten. Then set how fast the music drops and recovers. A slower return sounds smoother. Listen to the whole passage, not just one phrase.</p>
<h2>In Tunedzy</h2>
<p>Tunedzy&rsquo;s Auto-duck lowers the music under the voices in Multitrack. The <a href="/tunedzy/how-to-duck-music-under-a-voiceover">ducking how-to</a> has the steps.</p>
''',
    vf_title='Put the voice over the music',
    vf='<p>Auto-duck in Multitrack lowers the music under your voices, so the words stay clear.</p>',
    faq=[('Is ducking the same as compression?', 'They are related. Ducking is triggered by another signal, the voice; compression responds to its own level.'),
         ('Why does my music pump?', 'The reduction is too strong or too fast. Lower the amount and slow the return.'),
         ('Can I duck with a sidechain?', 'Yes. Sidechain compression is the same idea, set up as a trigger from the voice.')],
    related=['how-to-duck-music-under-a-voiceover', 'how-to-add-background-music-to-a-voiceover', 'what-is-a-compressor'])
