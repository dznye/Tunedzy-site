"""SEO articles for the two noise-cancelling tools. Each article targets ONE specific search (kw), puts it in the title, URL, H1, first answer and meta description,
gives a direct answer first, then real steps and numbers, admits limits, and links to its tool and to neighbouring guides.
No invented statistics, reviews or benchmarks. App names and menu labels change between versions, so settings are described as "usually" where they vary."""

CLUSTERS = {
    'stream': dict(tool='clean-streaming-mic', label='Streaming mic and noise', tool_name='Clean Streaming Mic'),
    'record': dict(tool='voice-recorder-noise-cancellation', label='Voice recording and noise removal', tool_name='Noise-Free Voice Recorder'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


# ============================================================================================== STREAMING MIC CLUSTER
add(slug='remove-background-noise-from-mic-obs', cluster='stream', kw='remove background noise from mic OBS',
    title='Remove Background Noise From Your Mic in OBS (Step by Step)',
    desc='How to remove background noise from your mic in OBS: Noise Suppression, Noise Gate, filter order and a free browser noise canceller for stubborn noise.',
    h1='How to Remove Background Noise From Your Mic in OBS',
    answer=('In OBS, open the Audio Mixer, click the gear next to your mic, choose Filters, and add <strong>Noise Suppression</strong> (RNNoise), then a <strong>Noise Gate</strong>, then a <strong>Compressor</strong>. '
            'If steady noise such as a fan is still audible, clean the mic before OBS with a free browser noise canceller and a virtual audio cable.'),
    body='''
<h2>Step 1: Add the Noise Suppression filter</h2>
<p>Right-click your microphone in the Audio Mixer (or click the gear icon), choose <strong>Filters</strong>, press the plus button and add <strong>Noise Suppression</strong>. You normally get a choice of methods:</p>
<ul>
<li><strong>RNNoise</strong> is a trained model that is good at removing steady noise and some non-speech sounds. It is the usual best choice on a normal computer.</li>
<li><strong>Speex</strong> is lighter on the CPU but less effective, so it is only worth using on a very weak machine.</li>
<li><strong>NVIDIA noise removal</strong> appears on some versions when you have a supported NVIDIA graphics card and the needed components installed.</li>
</ul>
<p>Menu names change a little between OBS versions, but the idea is the same. Listen in the OBS preview or a local recording, not just the meter.</p>
<h2>Step 2: Add a Noise Gate after it</h2>
<p>Suppression turns noise down while you talk. A <strong>Noise Gate</strong> silences the mic between words. Add it below Noise Suppression. The OBS defaults (open around &minus;26 dB, close around &minus;32 dB, attack 25 ms, hold 200 ms, release 150 ms) are a sane starting point; see our guide to <a href="/tunedzy/blog/noise-gate-settings-for-streaming">noise gate settings for streaming</a> for how to tune them to your own noise level.</p>
<h2>Step 3: Order your filters correctly</h2>
<p>Filters run from top to bottom, so order matters. A good order is:</p>
<ol>
<li>Gain (only if the mic is too quiet)</li>
<li>Noise Suppression</li>
<li>Noise Gate</li>
<li>Equalizer (optional)</li>
<li>Compressor</li>
<li>Limiter</li>
</ol>
<p>Compressing before removing noise makes quiet noise louder, which is the most common reason a mic that &ldquo;should be fine&rdquo; still sounds hissy.</p>
<h2>Step 4: Fix the noise at the source</h2>
<p>No filter beats a quieter source. Set the mic gain low in Windows or your audio interface and sit closer instead; every 3&nbsp;dB of gain you remove also removes 3&nbsp;dB of noise. Keep the mic away from the PC and point the dead side of a cardioid mic toward the fan. More ideas are in <a href="/tunedzy/blog/how-to-stop-fan-noise-on-my-microphone">how to stop fan noise on your microphone</a>.</p>
<h2>When OBS alone is not enough: clean the mic first</h2>
<p>If the noise is steady (a fan, hiss, hum, air conditioning), a tool that <em>learns your room</em> can remove more than a generic model. The free <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> listens to three seconds of your room tone, removes that noise live in your browser, and sends the clean mic to OBS through a virtual audio cable. Setup is in our <a href="/tunedzy/blog/virtual-audio-cable-setup-obs-discord-zoom">virtual audio cable guide</a>. In OBS, add the cable as an <em>Audio Input Capture</em>, and keep OBS suppression on low or off so you do not process the voice twice.</p>
<h2>Quick troubleshooting</h2>
<table><tr><th>Problem</th><th>Likely cause</th><th>Fix</th></tr>
<tr><td>Words cut off at the start</td><td>Gate opens too late</td><td>Lower the open threshold, shorten attack to 10 ms</td></tr>
<tr><td>Voice sounds watery or robotic</td><td>Over-processing</td><td>Use only one suppression method; lower reduction</td></tr>
<tr><td>Noise pumps up between sentences</td><td>Compressor before the gate</td><td>Move the gate above the compressor</td></tr>
<tr><td>Keyboard still audible</td><td>Sudden noises are hard to remove</td><td>Mic closer, mechanical keyboard further, lower gain</td></tr></table>
''',
    faq=[('What is the best noise suppression method in OBS?', 'RNNoise is usually the best all-round choice on a normal computer. Speex is lighter but weaker, and NVIDIA noise removal is available on some setups with a supported graphics card.'),
         ('Why does my mic still pick up background noise in OBS?', 'Common reasons are high mic gain, a sensitive condenser mic, no gate, or compressing the signal before the noise is removed. Lower the gain, add the gate, and put the compressor last.'),
         ('Can I remove noise without a plugin?', 'Yes. OBS has built-in Noise Suppression and Noise Gate filters. A browser tool and a virtual audio cable can add stronger cleaning for steady noise.')])

add(slug='virtual-audio-cable-setup-obs-discord-zoom', cluster='stream', kw='virtual audio cable setup',
    title='Virtual Audio Cable Setup for OBS, Discord and Zoom (Free)',
    desc='Set up a free virtual audio cable (VB-Cable on Windows, BlackHole on Mac) to send a cleaned microphone into OBS, Discord, Zoom or Teams. Step-by-step.',
    h1='Virtual Audio Cable Setup for OBS, Discord and Zoom',
    answer=('Install a free virtual audio cable (VB-Cable on Windows or BlackHole on Mac). Send your processed audio to the cable&rsquo;s <strong>input</strong>, then choose the cable&rsquo;s <strong>output</strong> as the microphone in OBS, Discord, Zoom or Teams. '
            'The cable works like a short patch lead between two programs.'),
    body='''
<h2>What a virtual audio cable does</h2>
<p>A web page or a plugin cannot create a new microphone on your computer by itself. A virtual audio cable adds a pair of fake devices: anything played into the cable&rsquo;s <strong>input</strong> (it looks like a speaker) comes out of its <strong>output</strong> (it looks like a microphone). That lets one program, such as a noise canceller in your browser, feed another program, such as OBS or Discord.</p>
<h2>Windows: VB-Cable</h2>
<ol>
<li>Download the free <em>VB-Cable</em> driver from the official VB-Audio website, unzip it, right-click the setup file and run it as administrator. Restart if asked.</li>
<li>Open Windows Sound settings. You will now see <strong>CABLE Input</strong> (a playback device) and <strong>CABLE Output</strong> (a recording device).</li>
<li>In the <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> page, set <em>Send clean mic to</em> the device called <strong>CABLE Input</strong>.</li>
<li>In OBS, add an <em>Audio Input Capture</em> source and choose <strong>CABLE Output</strong>. In Discord, Zoom or Teams, set the microphone to <strong>CABLE Output</strong>.</li>
</ol>
<h2>Mac: BlackHole</h2>
<ol>
<li>Install the free <em>BlackHole 2ch</em> driver from its official project page (or with Homebrew) and restart your audio apps.</li>
<li>Send the clean mic to <strong>BlackHole 2ch</strong> in the page&rsquo;s output list.</li>
<li>Pick <strong>BlackHole 2ch</strong> as the input device in OBS, Discord, Zoom or Teams.</li>
<li>To also hear yourself, create a <em>Multi-Output Device</em> in Audio MIDI Setup that includes BlackHole and your headphones, but do not use it as an input.</li>
</ol>
<h2>Choosing the output device needs Chrome or Edge</h2>
<p>Letting a web page pick an output device is supported in Chrome and Edge on a computer. Other browsers may not offer the list. If the choice is missing, switch browsers rather than fighting the settings.</p>
<h2>No-install alternative for OBS</h2>
<p>On Windows 10 or 11, recent versions of OBS have an <strong>Application Audio Capture</strong> source. Add it, choose your browser window, and OBS captures that browser&rsquo;s audio, which includes the cleaned mic from the page. It also captures every other tab&rsquo;s sound, so keep other audio muted.</p>
<h2>Troubleshooting</h2>
<table><tr><th>Symptom</th><th>Fix</th></tr>
<tr><td>No sound reaches the app</td><td>Check the page&rsquo;s output is the cable <em>input</em> and the app&rsquo;s mic is the cable <em>output</em>; keep the browser tab open</td></tr>
<tr><td>You hear an echo or doubling</td><td>Turn off Windows &ldquo;Listen to this device&rdquo; on the cable, and do not monitor in two places</td></tr>
<tr><td>Crackling or dropouts</td><td>Set the cable and your devices to the same sample rate (usually 48 kHz) and close heavy apps</td></tr>
<tr><td>App does not list the cable</td><td>Restart the app after installing the driver</td></tr></table>
<p>Once it works, go through the <a href="/tunedzy/blog/discord-zoom-teams-noise-suppression-settings">Discord, Zoom and Teams noise suppression settings</a> so the app does not process the voice a second time.</p>
''',
    faq=[('Is a virtual audio cable safe?', 'The well-known free ones come from their official websites. Download only from the official site of the project and avoid re-uploads on random download pages.'),
         ('Does a virtual cable add delay?', 'A little: the cable itself adds very little, and the rest comes from your browser and audio devices. Use a wired headset and a 48 kHz sample rate for the lowest delay.'),
         ('Can I use it for music and not just my mic?', 'Yes, but keep it simple: route one source to one cable. Sending everything to the same cable can mix your game or music into your microphone by accident.')])

add(slug='noise-gate-settings-for-streaming', cluster='stream', kw='noise gate settings for streaming',
    title='Noise Gate Settings for Streaming: OBS Values That Work',
    desc='What a noise gate does and the OBS noise gate settings that work: thresholds, attack, hold and release, with a simple way to set them for your own mic.',
    h1='Noise Gate Settings for Streaming: OBS Values That Work',
    answer=('A good starting point in OBS is a <strong>close threshold</strong> of about &minus;32 dB, an <strong>open threshold</strong> of about &minus;26 dB, <strong>attack</strong> 10&ndash;25 ms, <strong>hold</strong> 150&ndash;250 ms and <strong>release</strong> 100&ndash;200 ms. '
            'Then adjust: set the close threshold a few dB above your room noise and below your quietest words.'),
    body='''
<h2>What a noise gate actually does</h2>
<p>A noise gate is a switch for sound level. When your mic is louder than the <strong>open threshold</strong> the gate opens and passes your voice. When the level falls below the <strong>close threshold</strong> it closes and mutes the mic. It removes noise only <em>between</em> words and sentences; it cannot remove noise during speech. That is why it works best together with noise suppression.</p>
<h2>The five settings, in plain words</h2>
<table><tr><th>Setting</th><th>What it does</th><th>Typical value</th></tr>
<tr><td>Open threshold</td><td>Level that opens the gate</td><td>&minus;26 dB</td></tr>
<tr><td>Close threshold</td><td>Level that closes it again</td><td>&minus;32 dB</td></tr>
<tr><td>Attack</td><td>How fast it opens</td><td>10&ndash;25 ms</td></tr>
<tr><td>Hold</td><td>How long it stays open after you stop</td><td>150&ndash;250 ms</td></tr>
<tr><td>Release</td><td>How fast it fades shut</td><td>100&ndash;200 ms</td></tr></table>
<h2>How to set it for your own mic (2 minutes)</h2>
<ol>
<li>Open the gate filter and watch the mic meter in OBS.</li>
<li>Stay silent for five seconds and note the highest level of your room noise. Say it peaks around &minus;50 dB.</li>
<li>Speak the way you stream, including quiet words, and note your lowest speaking level, maybe &minus;35 dB.</li>
<li>Set the <strong>close threshold</strong> a few dB above the noise (say &minus;44 dB) and well below your quiet speech, and set the <strong>open threshold</strong> about 5&ndash;6 dB higher (say &minus;38 dB).</li>
<li>Record a short test and listen for clipped word starts and endings.</li>
</ol>
<h2>Fixing the common gate problems</h2>
<ul>
<li><strong>First syllable gets cut off:</strong> lower the open threshold or shorten the attack.</li>
<li><strong>Ends of words chopped:</strong> lengthen hold and release, or lower the close threshold.</li>
<li><strong>Gate flutters on and off (chatter):</strong> widen the gap between open and close thresholds.</li>
<li><strong>Noise comes through with every word:</strong> that is normal for a gate. Add noise suppression for noise during speech.</li>
</ul>
<h2>Gate versus noise suppression</h2>
<p>Use both. Suppression reduces noise while you talk; the gate silences the gaps. In the free <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a>, the gate is set automatically from the room noise it learned, so you can start there and fine-tune only if needed. For OBS-specific filter order, see <a href="/tunedzy/blog/remove-background-noise-from-mic-obs">how to remove background noise from your mic in OBS</a>.</p>
''',
    faq=[('What is a good noise gate threshold?', 'Set the close threshold a few decibels above your room noise and below your quietest speech, then the open threshold roughly 5&ndash;6 dB higher. Around &minus;32 dB close and &minus;26 dB open is a common starting point in OBS.'),
         ('Why does my noise gate cut off my words?', 'The threshold is too high, the attack is too slow, or hold and release are too short. Lower the thresholds and lengthen hold and release.'),
         ('Do I need a noise gate if I use noise suppression?', 'It still helps. Suppression cleans noise during speech, and the gate silences the pauses, so the two work well together.')])

add(slug='how-to-stop-fan-noise-on-my-microphone', cluster='stream', kw='stop fan noise on microphone',
    title='How to Stop Fan Noise on Your Microphone (7 Fixes)',
    desc='PC fan or air conditioner noise on your mic? Seven fixes in order of impact, from mic position and gain to a noise canceller that learns your room.',
    h1='How to Stop Fan Noise on Your Microphone: 7 Fixes',
    answer=('Move the mic away from the fan and point its quiet side at it, lower the mic gain and speak closer, then remove the remaining steady noise with a noise canceller that learns your room tone. '
            'Fan noise is steady, so it is the easiest kind of noise to remove with software.'),
    body='''
<h2>Why fan noise is so common (and so fixable)</h2>
<p>A computer fan, GPU, air conditioner or heater makes a <em>steady</em> sound with a stable spectrum. Steady noise is the best case for noise reduction because a tool can learn exactly what it sounds like and subtract it. Start with physical fixes; each one lowers the noise before any software touches it.</p>
<h2>Fix 1: Move the mic away from the noise</h2>
<p>Sound gets quieter quickly with distance. Mount the mic on an arm so it sits to the side of the monitor and away from the PC case. Moving the mic a few centimetres away from a fan can matter more than any filter.</p>
<h2>Fix 2: Point the mic&rsquo;s dead side at the fan</h2>
<p>A cardioid mic hears best from the front and least from the back. Aim the back of the mic at the noise source, with your mouth in front.</p>
<h2>Fix 3: Lower the gain and move your mouth closer</h2>
<p>Noise and voice get amplified together. If you sit 10&ndash;15 cm from the mic you can turn the gain down a lot, which turns the fan down by the same amount while your voice stays loud.</p>
<h2>Fix 4: Use a dynamic mic in a noisy room</h2>
<p>Dynamic mics are less sensitive than condensers and pick up less of the room. If your condenser hears everything, a dynamic mic used close to your mouth is often the simplest upgrade.</p>
<h2>Fix 5: Slow the fans down</h2>
<p>Many PCs run fans faster than they need to. In your motherboard or fan software, flatten the fan curve so fans stay slow while you are idle. Make sure temperatures are safe before you change anything.</p>
<h2>Fix 6: Learn the room noise and remove it</h2>
<p>The Clean Streaming Mic tool asks you to stay quiet for three seconds, learns the fan&rsquo;s sound at every pitch, and then removes it while you talk. Steady fan noise is exactly what it is built for. Start with 18 dB of reduction and the gate on; if the voice sounds thin, lower it. Setup for OBS and Discord is in our <a href="/tunedzy/blog/virtual-audio-cable-setup-obs-discord-zoom">virtual audio cable guide</a>.</p>
<h2>Fix 7: Add a noise gate</h2>
<p>A gate silences the fan between words. See <a href="/tunedzy/blog/noise-gate-settings-for-streaming">noise gate settings for streaming</a> to tune it.</p>
<h2>What software cannot fix</h2>
<p>Software removes steady noise well, but it cannot remove another person talking, a TV, or a loud keyboard. If you mostly have those problems, change the room, not the filter.</p>
''',
    faq=[('Why is my mic picking up my PC fan?', 'The mic is too close to the PC, the gain is too high, or the mic is very sensitive. Move it away, lower the gain, and speak closer.'),
         ('Can software remove fan noise completely?', 'It can remove most of it, especially if the noise is steady. A tiny residual may remain; combine software with a lower gain and a gate for the best result.'),
         ('Is a dynamic or condenser mic better for fan noise?', 'A dynamic mic used close to your mouth usually picks up less room noise than a sensitive condenser.')])

add(slug='discord-zoom-teams-noise-suppression-settings', cluster='stream', kw='discord noise suppression settings',
    title='Discord, Zoom and Teams Noise Suppression Settings',
    desc='The best noise suppression settings for Discord, Zoom and Microsoft Teams, and how to avoid double-processing when you use a noise canceller.',
    h1='Discord, Zoom and Teams Noise Suppression Settings',
    answer=('Open the app&rsquo;s audio settings and turn <strong>noise suppression</strong> on: Discord has Standard or an AI option, Zoom has Suppress Background Noise (Auto, Low, Medium, High), and Teams has Noise suppression (Auto, Low, High). '
            'If you already clean your mic before the app, set the app to Low or Off so the voice is not processed twice.'),
    body='''
<h2>Discord</h2>
<p>Open <strong>User Settings &rarr; Voice &amp; Video</strong>. Under noise suppression you will usually see <em>None</em>, <em>Standard</em> and an AI-based option (the labels change over time). Echo cancellation and automatic gain control are separate switches.</p>
<ul>
<li>Use the stronger suppression for a noisy room and speech-only chat.</li>
<li>Turn <strong>automatic gain control</strong> off if you are a musician or you want a steady level; it pumps the volume up in quiet moments.</li>
<li>Use <strong>manual input sensitivity</strong> if the automatic one cuts you off, and set it just above your room noise.</li>
</ul>
<h2>Zoom</h2>
<p>Open <strong>Settings &rarr; Audio</strong> and find <strong>Suppress background noise</strong>. It usually offers <em>Auto</em>, <em>Low</em>, <em>Medium</em> and <em>High</em>. Auto is a good default; High removes the most but can clip soft speech or music. For music or singing, use <em>Original sound</em> options instead of suppression.</p>
<h2>Microsoft Teams</h2>
<p>Open <strong>Settings &rarr; Devices</strong> and look for <strong>Noise suppression</strong>. Typical choices are <em>Auto</em>, <em>Low</em>, <em>High</em> and <em>Off</em>. Auto and High are enough for most home offices; Low suits quiet rooms and keeps your voice more natural.</p>
<h2>Using a noise canceller before the app</h2>
<p>If you clean your mic with a tool such as the free <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> and send it through a virtual audio cable, the app receives a voice that is already clean. Running strong suppression on top can make speech sound thin or choppy.</p>
<table><tr><th>Setup</th><th>App suppression setting</th></tr>
<tr><td>App only, noisy room</td><td>Highest suppression the app offers</td></tr>
<tr><td>App only, quiet room</td><td>Low or Standard</td></tr>
<tr><td>Pre-cleaned mic via virtual cable</td><td>Low or Off</td></tr>
<tr><td>Singing or instruments</td><td>Off, use the app&rsquo;s original-sound option</td></tr></table>
<p>Cable setup steps are in our <a href="/tunedzy/blog/virtual-audio-cable-setup-obs-discord-zoom">virtual audio cable guide</a>.</p>
<h2>Quick checks that fix most call audio</h2>
<ul>
<li>Use headphones so the app&rsquo;s echo cancellation has nothing to fight.</li>
<li>Choose the correct input device; many laptops list several microphones.</li>
<li>Do a test recording or a call with a friend before an important meeting.</li>
</ul>
''',
    faq=[('Which Discord noise suppression setting is best?', 'Use the stronger option for noisy rooms and the lighter one for quiet rooms. If your mic is already cleaned before Discord, use the lightest setting.'),
         ('Why does noise suppression make me sound robotic?', 'Heavy suppression removes parts of your voice along with the noise. Lower the strength, or clean the mic once before the app instead of stacking filters.'),
         ('Should I turn off automatic gain control?', 'For steady levels, music, or if you use a compressor, yes. It raises the volume in quiet moments, which brings noise up with it.')])

# ============================================================================================== VOICE RECORDER CLUSTER
add(slug='how-to-record-a-voice-over-without-background-noise', cluster='record', kw='record a voice over without background noise',
    title='Record a Voice-Over Without Background Noise (Home Guide)',
    desc='How to record a clean voice-over at home: choose the room, set mic distance and level, record room tone, and remove leftover noise. A simple checklist.',
    h1='How to Record a Voice-Over Without Background Noise',
    answer=('Record in a small, soft room at a quiet time, sit 10&ndash;20 cm from the mic, set levels so peaks reach about &minus;12 to &minus;6 dB, record 10 seconds of silence for noise removal, and switch off every noise source. '
            'Then remove any steady leftover noise with a tool that learns your room tone.'),
    body='''
<h2>1. Pick the right room and time</h2>
<p>Noise from outside and echo from bare walls cause most problems. Choose a small room with soft things in it: a bedroom with curtains and a bed, a closet full of clothes, or a corner with a sofa. Record when traffic, neighbours and appliances are quiet, often early morning or late evening.</p>
<h2>2. Remove noise sources before you press record</h2>
<ul>
<li>Switch off fans, air conditioning, and noisy refrigerators if you can.</li>
<li>Silence phone notifications and close chat apps.</li>
<li>Close the door and window. Hang a blanket behind you if the room echoes.</li>
</ul>
<h2>3. Set the mic distance and angle</h2>
<p>Place the mic 10&ndash;20 cm from your mouth, slightly off to the side or above, so breaths and &ldquo;p&rdquo; sounds do not blast it. Distance matters more than expensive gear: the closer you are, the louder your voice is compared with the room.</p>
<h2>4. Set the recording level</h2>
<p>Speak at your normal volume and set the input gain so the loudest peaks reach about <strong>&minus;12 to &minus;6 dB</strong> on the meter. Never let it hit 0 dB; clipped audio cannot be repaired. A quieter-but-clean recording is better than a loud distorted one.</p>
<h2>5. Record room tone first</h2>
<p>Before you speak, record 10 to 30 seconds of silence in the same position. This gives noise removal a clean sample of your room. The free <a href="/tunedzy/tools/voice-recorder-noise-cancellation">voice recorder with noise cancellation</a> does this with a three-second &ldquo;Learn my room noise&rdquo; step. See <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">what room tone is and how to record it</a>.</p>
<h2>6. Record, listen back, then clean</h2>
<p>Do a short test, listen on headphones, and fix problems at the source. When the recording is good, remove steady leftover noise. Do it once and gently; see <a href="/tunedzy/blog/why-noise-reduction-makes-voice-sound-watery">why noise reduction makes a voice sound watery</a> for how much is too much.</p>
<h2>Before-you-record checklist</h2>
<table><tr><th>Check</th><th>Done?</th></tr>
<tr><td>Small, soft room, door closed</td><td>&#9744;</td></tr>
<tr><td>Fans, AC and notifications off</td><td>&#9744;</td></tr>
<tr><td>Mic 10&ndash;20 cm away, off-axis</td><td>&#9744;</td></tr>
<tr><td>Peaks at &minus;12 to &minus;6 dB</td><td>&#9744;</td></tr>
<tr><td>10 seconds of room tone recorded</td><td>&#9744;</td></tr>
<tr><td>Headphones on, test listened to</td><td>&#9744;</td></tr></table>
''',
    faq=[('How do I record a voice-over with no background noise?', 'Use a quiet, soft room, switch off noise sources, speak close to the mic, record at healthy levels, and capture room tone so leftover steady noise can be removed.'),
         ('Do I need an expensive microphone?', 'No. Room, distance and level matter more. A basic USB mic in a soft room used 10&ndash;20 cm away beats an expensive mic in an echoey room.'),
         ('Can I remove noise after recording?', 'Yes, steady noise such as hiss or a fan can be reduced afterwards. Echo, other voices and sudden sounds are much harder to remove.')])

add(slug='remove-background-noise-from-audio-free', cluster='record', kw='remove background noise from audio free',
    title='Remove Background Noise From Audio for Free (3 Ways)',
    desc='Three free ways to remove background noise from audio: a private in-browser tool, Audacity, and your video editor, with the settings that work and their limits.',
    h1='How to Remove Background Noise From Audio for Free',
    answer=('Drop the file into a free in-browser noise remover that learns the noise from a quiet part of your recording, or use Audacity&rsquo;s Noise Reduction (12 dB, sensitivity 6, smoothing 3 as a start). '
            'Both work best on steady noise such as hiss, hum and fans, and neither can remove other voices.'),
    body='''
<h2>Way 1: A private in-browser noise remover</h2>
<p>Open the <a href="/tunedzy/tools/voice-recorder-noise-cancellation">voice recorder with noise cancellation</a> and use <strong>Clean an existing recording</strong>. Drop in your MP3, WAV, FLAC or OGG file. The tool looks for a quiet stretch to learn your noise from, removes it, and gives you a before-and-after player and a WAV download. Because it runs in your browser, the file is never uploaded, which matters for private or unreleased audio.</p>
<h2>Way 2: Audacity (free desktop editor)</h2>
<ol>
<li>Select 1&ndash;2 seconds of pure background noise (a pause with no speech).</li>
<li>Open <strong>Effect &rarr; Noise Reduction</strong> and click <strong>Get Noise Profile</strong>.</li>
<li>Select the whole track, open Noise Reduction again, and start with <strong>12 dB</strong> reduction, <strong>6</strong> sensitivity and <strong>3</strong> frequency smoothing.</li>
<li>Press Preview, then OK. Undo and lower the dB if the voice sounds thin.</li>
</ol>
<h2>Way 3: Your video editor</h2>
<p>Most free video editors have an audio denoise or &ldquo;reduce noise&rdquo; effect. They are fast and convenient but give you few controls, so they suit light hiss rather than heavy noise.</p>
<h2>Which way should you pick?</h2>
<table><tr><th>If you want&hellip;</th><th>Use</th></tr>
<tr><td>A quick fix with no install and no upload</td><td>The in-browser noise remover</td></tr>
<tr><td>Full control and other editing tools</td><td>Audacity</td></tr>
<tr><td>Cleaner audio inside a video project</td><td>Your editor&rsquo;s denoise effect</td></tr></table>
<h2>What you can and cannot remove</h2>
<ul>
<li><strong>Works well:</strong> steady hiss, hum, fans, air conditioning and computer noise.</li>
<li><strong>Works partly:</strong> distant traffic and constant crowd murmur.</li>
<li><strong>Does not work:</strong> another person talking, music, room echo, clicks and coughs. Those need a re-record or a more advanced repair.</li>
</ul>
<h2>Tips for better results</h2>
<p>Leave 1&ndash;2 seconds of silence at the start of any recording so noise can be learned, apply noise reduction only once, and work from the original WAV rather than a compressed MP3 whenever you can. If the voice sounds watery, read <a href="/tunedzy/blog/why-noise-reduction-makes-voice-sound-watery">why noise reduction does that and how to fix it</a>.</p>
''',
    faq=[('How can I remove background noise from audio for free?', 'Use a free in-browser noise remover, Audacity&rsquo;s Noise Reduction, or your video editor&rsquo;s denoise effect. Steady noise responds best.'),
         ('Is it safe to upload audio to online noise removers?', 'Many online tools upload your file to a server. A tool that runs entirely in your browser keeps the audio on your own device.'),
         ('Can noise removal fix a very noisy recording?', 'It can reduce steady noise a lot, but it cannot rebuild a voice that is buried in noise. A closer, quieter re-record is always better.')])

add(slug='what-is-room-tone-and-how-to-record-it', cluster='record', kw='what is room tone',
    title='What Is Room Tone? How to Record It for Cleaner Audio',
    desc='Room tone is the sound of an empty room. Learn why it matters, how to record 10 to 30 seconds of it, and how it improves noise removal and editing.',
    h1='What Is Room Tone? How to Record It for Cleaner Audio',
    answer=('<strong>Room tone</strong> is the quiet background sound of a room with nobody speaking: fans, hum, distant traffic. Record 10 to 30 seconds of it in the same position and conditions as your recording. '
            'It lets noise removal learn exactly what to subtract and lets editors fill gaps naturally.'),
    body='''
<h2>What room tone is</h2>
<p>Every room has a sound even when it feels silent: air conditioning, a computer fan, the refrigerator next door, the hum of electrical gear. That steady background is room tone. It is part of every recording you make in that space, and it has its own consistent &ldquo;fingerprint&rdquo;.</p>
<h2>Why room tone is useful</h2>
<ul>
<li><strong>Noise removal:</strong> a tool that learns the noise from room tone can remove it much more accurately than a generic filter, because it knows the exact sound to take away.</li>
<li><strong>Editing:</strong> when you cut out a cough or a pause, silence sounds unnatural. Pasting room tone in the gap keeps the background continuous.</li>
<li><strong>Consistency:</strong> clips recorded in the same room match when each one has the same underlying tone.</li>
</ul>
<h2>How to record room tone</h2>
<ol>
<li>Set up exactly as you will record: same mic, same position, same gain, same room conditions.</li>
<li>Press record and stay completely still and silent for <strong>10 to 30 seconds</strong>. Do not clear your throat, shift in your chair or type.</li>
<li>Then record your voice-over in the same file or session.</li>
<li>Keep each room tone clip with its recording. If you change the room or the gain, record new room tone.</li>
</ol>
<h2>How the free recorder uses room tone</h2>
<p>In the <a href="/tunedzy/tools/voice-recorder-noise-cancellation">voice recorder with noise cancellation</a>, press <strong>Learn my room noise</strong> and stay quiet for three seconds. The tool measures the noise at every pitch and then removes only that sound while you speak. For a file you already recorded, it searches for the quietest steady stretch and learns from that, so leaving a second or two of silence at the start helps a lot.</p>
<h2>Common room tone mistakes</h2>
<table><tr><th>Mistake</th><th>Result</th></tr>
<tr><td>Recording room tone in a different position</td><td>Noise profile does not match; some noise stays</td></tr>
<tr><td>Breathing, shifting or swallowing during the clip</td><td>Those sounds are learned as noise and can damage the voice</td></tr>
<tr><td>Too short (1 second)</td><td>Less reliable estimate; use at least 3 seconds</td></tr>
<tr><td>Changing the gain afterwards</td><td>Noise level changes, so the profile no longer fits</td></tr></table>
<h2>Next step</h2>
<p>Read <a href="/tunedzy/blog/how-to-record-a-voice-over-without-background-noise">how to record a voice-over without background noise</a> for the whole workflow.</p>
''',
    faq=[('How long should room tone be?', 'Ten to thirty seconds is plenty for editing; for noise learning, even three seconds of clean silence works well.'),
         ('Is room tone the same as silence?', 'No. Room tone is the sound a quiet room actually makes. True digital silence sounds unnatural in a recording.'),
         ('Do I need room tone if I use noise removal?', 'You can remove noise without it, but a clean room tone sample makes the result noticeably more accurate.')])

add(slug='why-noise-reduction-makes-voice-sound-watery', cluster='record', kw='noise reduction voice sounds watery',
    title='Why Noise Reduction Makes a Voice Sound Watery (and Fix)',
    desc='Noise reduction making your voice sound robotic, thin or watery? Learn why it happens and the exact settings and habits that give a natural result.',
    h1='Why Noise Reduction Makes a Voice Sound Watery or Robotic',
    answer=('Watery or robotic sound is usually <strong>over-processing</strong>: too much reduction, too high sensitivity, or stacking several denoisers. '
            'Lower the reduction to 6&ndash;12 dB, lower sensitivity, apply noise removal once, and fix the noise at the source so less removal is needed.'),
    body='''
<h2>Why it happens</h2>
<p>Noise reduction works by estimating the noise at each frequency and turning those frequencies down. Voice and noise share the same frequencies, so every cut also takes away a little voice. If the cut is too deep, or the noise estimate is too high, parts of your voice vanish and leave a thin, bubbly, &ldquo;underwater&rdquo; character. When the gain changes rapidly from moment to moment the ear hears &ldquo;musical noise&rdquo;, small chirpy artifacts.</p>
<h2>Symptoms and fixes</h2>
<table><tr><th>You hear</th><th>Cause</th><th>Fix</th></tr>
<tr><td>Thin, hollow voice</td><td>Reduction too deep</td><td>Lower reduction to 6&ndash;12 dB</td></tr>
<tr><td>Bubbly or chirpy background</td><td>Sensitivity too high or noise estimate too aggressive</td><td>Lower sensitivity; learn noise from a clean sample</td></tr>
<tr><td>Words start or end oddly</td><td>Gate or reduction reacts too fast</td><td>Reduce the gate; slow the response</td></tr>
<tr><td>Robotic sound after several tools</td><td>Stacked denoisers</td><td>Use one denoiser, once</td></tr>
<tr><td>Worse on MP3 files</td><td>Compression artifacts already present</td><td>Start from the original WAV when possible</td></tr></table>
<h2>How much reduction is enough?</h2>
<p>A useful rule is to remove only as much noise as you need to stop noticing it. For light hiss, 6&ndash;12 dB is usually enough. For a loud fan, 15&ndash;20 dB may be needed. If you reach for 30 dB, the real fix is a quieter recording. In the free <a href="/tunedzy/tools/voice-recorder-noise-cancellation">noise-cancelling recorder</a>, tick <em>Hear original</em> and compare while you adjust.</p>
<h2>Habits that keep it natural</h2>
<ul>
<li><strong>Record close to the mic.</strong> A stronger voice means you need less reduction.</li>
<li><strong>Learn the noise from clean room tone</strong>, not from a sample that contains breaths or words. See <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">what room tone is</a>.</li>
<li><strong>Denoise once,</strong> early, and then do EQ and compression.</li>
<li><strong>Leave a little noise.</strong> A faint natural background sounds better than a perfectly dead one.</li>
</ul>
<h2>When to stop and re-record</h2>
<p>If you need to push the settings to the maximum, the recording itself is the problem. A closer mic, a softer room and noise sources switched off will always sound better than heavy processing. For the full process, read <a href="/tunedzy/blog/how-to-record-a-voice-over-without-background-noise">how to record a voice-over without background noise</a>.</p>
''',
    faq=[('Why does my voice sound underwater after noise reduction?', 'The reduction is too strong or the noise estimate is too high, so parts of the voice are removed with the noise. Lower the reduction and sensitivity.'),
         ('How much noise reduction should I use?', 'Use the least that makes the noise unnoticeable, often 6&ndash;12 dB for hiss and up to about 15&ndash;20 dB for a loud steady fan.'),
         ('Can I fix a voice that is already over-processed?', 'Not really. Go back to the original recording and apply gentler settings once.')])

add(slug='what-loudness-should-a-voice-over-be', cluster='record', kw='voice over loudness LUFS',
    title='What Loudness Should a Voice-Over Be? LUFS and Peak Levels',
    desc='Voice-over loudness explained: LUFS and peak targets for YouTube, podcasts and audiobooks, how to measure them, and how to normalize safely.',
    h1='What Loudness Should a Voice-Over Be? LUFS and Peak Levels',
    answer=('For online video, aim for roughly <strong>&minus;16 to &minus;14 LUFS</strong> with peaks below about <strong>&minus;1 dBTP</strong>. Podcasts commonly target around &minus;16 LUFS (stereo) or &minus;19 LUFS (mono). '
            'Audiobooks sold through ACX have their own rules: RMS between &minus;23 and &minus;18 dB, peaks under &minus;3 dB, and a very low noise floor.'),
    body='''
<h2>Two numbers matter: loudness and peak</h2>
<p><strong>Loudness</strong> (measured in LUFS) is how loud audio sounds on average to a listener. <strong>Peak level</strong> is the highest instant the waveform reaches, measured in dBFS or dBTP. A voice-over can have a safe peak but still be too quiet or too loud, so you need to check both.</p>
<h2>Typical targets</h2>
<table><tr><th>Where it will be heard</th><th>Loudness target</th><th>Peak</th></tr>
<tr><td>YouTube, social video</td><td>about &minus;16 to &minus;14 LUFS</td><td>under &minus;1 dBTP</td></tr>
<tr><td>Podcast (stereo)</td><td>about &minus;16 LUFS</td><td>under &minus;1 dBTP</td></tr>
<tr><td>Podcast (mono)</td><td>about &minus;19 LUFS</td><td>under &minus;1 dBTP</td></tr>
<tr><td>Audiobook for ACX</td><td>RMS &minus;23 to &minus;18 dB</td><td>under &minus;3 dB, noise floor under &minus;60 dB RMS</td></tr></table>
<p>Platforms change their guidance, and normalisation can turn very loud audio down, so treat these as sensible targets and check the current rules of the platform you publish on, especially for audiobooks.</p>
<h2>How to measure your voice-over</h2>
<p>Drop the file into the free <a href="/tunedzy/tools/lufs-meter">LUFS meter</a>. It shows integrated loudness, an estimated true peak and loudness range, and tells you how streaming platforms would treat the file. The <a href="/tunedzy/tools/vocal-checker">vocal quality checker</a> also flags clipping and noise.</p>
<h2>How to bring a voice-over to the right level</h2>
<ol>
<li>Clean the noise first. Raising the level raises the noise too.</li>
<li>Apply gentle compression so quiet and loud words are closer together.</li>
<li>Normalize or raise the gain until the loudness reaches your target.</li>
<li>Check that peaks stay below the limit; use a limiter if they do not.</li>
<li>Measure again and listen on headphones and a phone speaker.</li>
</ol>
<p>In the free <a href="/tunedzy/tools/voice-recorder-noise-cancellation">voice recorder with noise cancellation</a>, the <em>Normalize the level</em> option raises the peak of a cleaned file to a safe level, and the LUFS meter confirms the result.</p>
<h2>Common mistakes</h2>
<ul>
<li>Normalizing before removing noise, which makes the noise louder.</li>
<li>Pushing loudness so high that the platform turns the audio down anyway.</li>
<li>Letting peaks reach 0 dB, which can cause clipping after conversion to MP3 or AAC.</li>
</ul>
<p>For the recording stage, see <a href="/tunedzy/blog/how-to-record-a-voice-over-without-background-noise">how to record a voice-over without background noise</a>.</p>
''',
    faq=[('What LUFS should a voice-over be?', 'For online video, around &minus;16 to &minus;14 LUFS is a common target. Podcasts often use about &minus;16 LUFS for stereo and about &minus;19 LUFS for mono.'),
         ('What peak level is safe for a voice-over?', 'Keep true peaks below about &minus;1 dBTP for online delivery, and follow a platform&rsquo;s own limits where they exist, such as &minus;3 dB for ACX audiobooks.'),
         ('Does normalizing make a voice-over louder?', 'It raises the level based on the loudest peak, not the average loudness, so check LUFS as well and use compression if the loudness is still too low.')])

# ============================================================================================== VOCAL CLEANUP CLUSTER (Tunedzy 5)
CLUSTERS['vocal'] = dict(tool='vocal-checker', label='Vocal recording fixes', tool_name='Vocal Checker')
CLUSTERS['compare'] = dict(tool='vocal-checker', label='Vocal tools compared', tool_name='Vocal Checker')

add(slug='fix-clipped-vocal-recording', cluster='vocal', kw='fix clipped vocal recording',
    title='How to Fix a Clipped Vocal Recording: What Can Be Saved',
    desc='Clipped vocals sound crackly and flat-topped. Check for clipping, see what declipping can rebuild, and learn how to record so it never happens.',
    h1='How to Fix a Clipped Vocal Recording',
    answer=('Clipping happens when the signal goes past the maximum the recorder can store, so the top of each waveform is cut flat and the sound turns harsh. '
            'Light clipping can be partly rebuilt by a declipper; heavy clipping cannot be undone, so re-record if you can.'),
    body='''
<h2>Step 1: Check whether it is clipped</h2>
<p>Zoom in on the waveform. Clipped audio has rows of samples sitting exactly at the top or bottom of the scale, looking like flat-topped peaks. Listen for crackle or a buzzy edge on loud words.</p>
<h2>Step 2: Try a declipper on a light clip</h2>
<p>A few brief flat tops can be estimated and rebuilt from the shape around them. Run the declipper on a copy, keep the original, and listen to the loud words in particular. Tunedzy&rsquo;s repair tools include declipping for light clipping.</p>
<h2>Step 3: Know when to stop</h2>
<p>If the flat tops run for milliseconds at a time across the whole take, a declipper can only guess. It will remove some harshness and leave the rest. Re-record at a lower level instead.</p>
<h2>How to avoid clipping next time</h2>
<ol>
<li>Set the input gain so your loudest words peak around &minus;12 to &minus;6 dBFS, not at 0.</li>
<li>Sing or speak at your loud moments at your real distance from the mic, and set the level for those, not for a quiet line.</li>
<li>Turn off automatic gain control, and any &ldquo;boost&rdquo; in the phone or laptop, while recording.</li>
<li>Leave headroom: a recording at &minus;12 dBFS is easy to raise later, a clipped one is not.</li>
</ol>
<h2>Limits</h2>
<p>Declipping estimates missing peaks. It works best on short, isolated clips and gets worse as the damage spreads. Treat the result as a rescue, not a replacement for a clean take.</p>
''',
    faq=[('Can clipping be fixed completely?', 'No. Light clipping can be partly rebuilt. Heavy clipping cannot be restored to what the microphone heard.'),
         ('What level should I record at?', 'Aim for loudest words around &minus;12 to &minus;6 dBFS, leaving room above them.'),
         ('Does a limiter fix clipping?', 'A limiter can make clipped audio quieter, but it does not restore the lost peaks. Fix the level at the source.')])

add(slug='remove-mic-pops-plosives', cluster='vocal', kw='remove mic pops plosives',
    title='How to Remove Mic Pops and Plosives From a Vocal',
    desc='Plosives are the thumps from P and B sounds. Fix them with mic placement, a pop filter, a high-pass filter and careful editing.',
    h1='How to Remove Mic Pops and Plosives From a Vocal',
    answer=('Plosives are bursts of air that hit the microphone on P, B, T and K sounds. Prevent them with a pop filter and an angled microphone. '
            'In the edit, a high-pass filter around 80 to 100 Hz removes most of the thump, and a short volume dip or a cut on the worst word fixes the rest.'),
    body='''
<h2>Step 1: Prevent them at the mic</h2>
<p>Place a pop filter a few centimetres in front of the capsule. Angle the mic a little off-axis so the air goes past it rather than into it. Keep the same distance for the whole take.</p>
<h2>Step 2: High-pass filter</h2>
<p>Voice has little useful content below about 80 Hz. A high-pass filter in that range removes most of the low thump while keeping the body of the voice. Raise the cutoff only if the voice sounds thin.</p>
<h2>Step 3: Fix the worst words by hand</h2>
<ol>
<li>Zoom in on the pop: it is a short low burst at the start of the word.</li>
<li>Cut the burst or lower the volume for a few milliseconds, then fade back in.</li>
<li>Listen at normal speed. A fix that you can only hear when zoomed in is good enough.</li>
</ol>
<h2>Limits</h2>
<p>Pops that hit hard enough to clip cannot be fixed well. Some plosives overlap with the note itself, so over-cutting makes the word sound clipped. Stop when the speech sounds natural.</p>
''',
    faq=[('What causes mic pops?', 'Bursts of breath on P, B, T and K sounds hitting the diaphragm of the microphone.'),
         ('Does a high-pass filter change the voice?', 'It removes low rumble and thump. Keep the cutoff gentle so the voice does not lose its warmth.'),
         ('Is a pop filter needed?', 'It is the simplest fix. It costs little and saves a lot of editing.')])

add(slug='how-to-de-ess-vocals', cluster='vocal', kw='how to de-ess vocals',
    title='How to De-Ess Vocals: Taming Harsh S and T Sounds',
    desc='How to de-ess vocals: find the sibilance, set a de-esser on the right frequency, and avoid the dull, lisping sound that over-processing causes.',
    h1='How to De-Ess Vocals',
    answer=('De-essing reduces the harsh hiss of S, SH and T sounds (sibilance). Find the frequency where the hiss is strongest, set a compressor-style de-esser to reduce only when that band gets loud, '
            'then listen in context. Sibilance often sits roughly between 4 and 9 kHz, but it depends on the voice and the mic.'),
    body='''
<h2>Step 1: Find the sibilance</h2>
<p>Solo the vocal and loop a phrase with several S sounds. Sweep a narrow EQ boost across the top of the voice until the hiss jumps out. That frequency is where the de-esser should work.</p>
<h2>Step 2: Set the de-esser</h2>
<ol>
<li>Set the frequency to the hiss you found.</li>
<li>Lower the threshold until the de-esser reduces only the S sounds, usually a few dB.</li>
<li>Keep the attack fast enough to catch the sound and the release quick so the vowels are not affected.</li>
</ol>
<h2>Step 3: Check it in context</h2>
<p>Bypass the de-esser and compare. If the vocal sounds lisped or dull, you are reducing too much or the wrong frequency. Check on phone speakers too, where sibilance is easy to miss.</p>
<h2>Limits</h2>
<p>A de-esser cannot fix a bad recording. If the mic is too close or the singer is very bright, reduce the top end a little more gently and record with the mic placed off-axis next time.</p>
''',
    faq=[('What frequency does de-essing use?', 'Often roughly 4 to 9 kHz, but find yours by listening. The exact number depends on the voice and the microphone.'),
         ('Can I de-ess too much?', 'Yes. Over-processed sibilance sounds dull and lisped. Reduce the amount until the words still sound clear.'),
         ('Do I need a de-esser plugin?', 'Any de-esser works. What matters is setting the frequency and threshold by ear.')])

add(slug='how-loud-should-vocals-be-on-a-beat', cluster='vocal', kw='how loud should vocals be on a beat',
    title='How Loud Should Vocals Be on a Beat? A Practical Answer',
    desc='How loud should vocals sit on a beat: there is no fixed number, but a practical method and a loudness check on several speakers give a balance that holds up.',
    h1='How Loud Should Vocals Be on a Beat?',
    answer=('There is no fixed number. Set the vocal so the words are clear over the loudest part of the beat, then check the balance on phone speakers, earphones and a car or a laptop. '
            'Many producers keep vocals a few decibels above the beat in the chorus, but the right level is the one that carries the lyric.'),
    body='''
<h2>A method that works on any beat</h2>
<ol>
<li>Play the loudest section of the beat, then bring the vocal up until the words sit clearly on top without feeling shouted.</li>
<li>Check the lyric. If you have to strain to hear a word, the vocal is too low or buried in the low mids.</li>
<li>Check the peaks: the loudest words should not clip. Use the <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> to see the overall level of the finished mix.</li>
</ol>
<h2>Test it where people will listen</h2>
<p>Most listeners use phone speakers or earphones. A vocal that sounds right on monitors can disappear on a phone, so play the mix on at least two other devices and adjust.</p>
<h2>Limits</h2>
<p>Genre, tempo and the singer change the balance. A fast rap verse and a slow ballad need different levels. Use the method, not a number from a chart.</p>
''',
    faq=[('Is there a standard dB level for vocals?', 'No. The balance depends on the song. Set it by the lyric, then check it on several speakers.'),
         ('Should the vocal be louder than the beat?', 'Usually the vocal sits on top of the beat for clarity, but the exact difference depends on the mix.'),
         ('What is the first thing to check?', 'Whether you can hear every word over the loudest part of the beat, on a phone speaker.')])

add(slug='what-lufs-for-spotify-and-youtube', cluster='vocal', kw='what LUFS for Spotify and YouTube',
    title='What LUFS for Spotify and YouTube? Targets and Why',
    desc='What LUFS should a mix hit for Spotify and YouTube: the common loudness targets, why platforms turn loud tracks down, and how to measure your own mix.',
    h1='What LUFS for Spotify and YouTube?',
    answer=('Both Spotify and YouTube turn loud audio down to a standard loudness, about &minus;14 LUFS integrated for Spotify. '
            'Mixing louder than that does not make your track sound louder on the platform; it only makes it more squashed. Aim near &minus;14 LUFS and keep the true peaks below about &minus;1 dBTP.'),
    body='''
<h2>What the platforms do</h2>
<p>Streaming services use loudness normalisation: they measure each track and adjust its playback level to a target. Spotify&rsquo;s own guidance uses about &minus;14 LUFS. YouTube also normalises, so very loud uploads are turned down.</p>
<h2>Why louder is not better</h2>
<p>If you push a track far above the target, the platform lowers it again, and the extra compression you used to get there leaves the mix dull. A track that lands near the target keeps its dynamics.</p>
<h2>How to check your mix</h2>
<ol>
<li>Export the mix without a limiter that pushes beyond your target.</li>
<li>Measure the integrated loudness with the <a href="/tunedzy/tools/lufs-meter">LUFS meter</a>.</li>
<li>Check the true peak. Keep it below about &minus;1 dBTP so conversion to lossy formats does not clip.</li>
</ol>
<h2>Limits</h2>
<p>Platforms change their guidance and the rules differ between music, podcasts and video. Check the current documentation of the platform you publish on before you master for it.</p>
''',
    faq=[('What is LUFS?', 'A measure of perceived loudness over a whole track. Platforms use it to set playback levels.'),
         ('Should I master to -14 LUFS exactly?', 'Aim close to it. A few tenths of a dB do not matter.'),
         ('Why does my track sound quieter on Spotify?', 'The platform normalises loud masters down to its target. Compare with a louder master and you will hear that it is squashed.')])

add(slug='vocal-chain-for-rap-in-order', cluster='vocal', kw='vocal chain order for rap',
    title='Vocal Chain for Rap: The Right Order and Why It Matters',
    desc='The vocal chain for rap in order: clean up, filter, de-ess, tune, compress, add colour, then space. Why the order changes the result and what each step is for.',
    h1='The Vocal Chain for Rap, in Order',
    answer=('A rap vocal chain works best in this order: clean up noise, high-pass filter, de-ess, EQ, compression, pitch correction if needed, saturation for colour, then reverb and delay on sends. '
            'Order matters because each step reacts to what came before: compressing before de-essing makes the sibilance louder.'),
    body='''
<h2>The order</h2>
<ol>
<li><strong>Clean up.</strong> Remove hum, hiss and room noise first, so later steps do not amplify them.</li>
<li><strong>High-pass filter.</strong> Around 80 to 100 Hz, to remove thump.</li>
<li><strong>De-ess.</strong> Before compression, so it reacts to the real sibilance.</li>
<li><strong>EQ.</strong> Remove mud around 200 to 400 Hz and add presence where the words need clarity.</li>
<li><strong>Compression.</strong> Even out the loud and quiet words so the lyric stays clear.</li>
<li><strong>Pitch correction</strong>, only if the performance needs it, and set to be transparent.</li>
<li><strong>Saturation</strong> for warmth, lightly.</li>
<li><strong>Reverb and delay on sends</strong>, so the space sits behind the voice and the dry vocal stays clear.</li>
</ol>
<h2>Why the order matters</h2>
<p>Put the compressor before the de-esser and it lifts the S sounds along with everything else, so the de-esser has to work harder and sounds worse. Put reverb before compression and the tail gets squashed. Keep the chain in order and each step has a clean input.</p>
<h2>Limits</h2>
<p>This is a starting point, not a rule. Some voices need less processing, and some styles use more. Change one step at a time, and bypass each to hear what it does.</p>
''',
    faq=[('Do I need every step?', 'No. Many rap vocals need only cleanup, de-essing, compression and a little reverb.'),
         ('Where should pitch correction go?', 'After compression and before the colour and space, so it works on a clean, even signal.'),
         ('Should reverb be on the vocal track?', 'Usually on a send, so you can control how much space sits behind the voice.')])

add(slug='ai-voice-cover-vocals-sound-robotic', cluster='vocal', kw='AI voice cover vocals sound robotic',
    title='Why AI Voice Covers Sound Robotic and How to Fix It',
    desc='Why AI voice cover vocals sound robotic, what causes the stiff timing and flat breaths, and the editing steps that make them more natural.',
    h1='Why AI Voice Covers Sound Robotic (and How to Fix It)',
    answer=('AI vocals often sound robotic because the timing is too exact, the breaths are missing or too clean, the tone is too even and the room is too dry. '
            'Fixing them means loosening the timing, adding breath and air where a singer would take one, de-essing harsh sounds, and adding a small amount of room.'),
    body='''
<h2>What makes it sound robotic</h2>
<ul>
<li><strong>Exact timing.</strong> Real singers drift a few milliseconds ahead or behind the beat.</li>
<li><strong>No breaths.</strong> Breaths in the wrong places, or none at all, make a line feel unreal.</li>
<li><strong>Too dry.</strong> A bone-dry vocal in an unnatural space sounds like a voice in a box.</li>
<li><strong>Harsh sibilance.</strong> AI voices often over-sharpen S and T sounds.</li>
</ul>
<h2>What to do</h2>
<ol>
<li>Move a few phrase starts slightly, and nudge the loudest notes so they land a little differently from the beat.</li>
<li>Add breaths from a clean recording where a singer would take one, at a low level.</li>
<li>De-ess, then check that the words are still clear.</li>
<li>Add a small amount of room reverb so the voice sits in a space, not on top of the beat.</li>
</ol>
<h2>Limits</h2>
<p>Editing can make an AI vocal sound more natural, but it cannot give it a real singer&rsquo;s expression. Check the rights to the voice model before you publish a cover, and say clearly that it is an AI voice.</p>
''',
    faq=[('Why does an AI vocal sound flat?', 'Usually because its tone and timing are too even, and it has no natural room or breath.'),
         ('Can editing fix every AI vocal?', 'No. It improves many, but a poor source model will still sound artificial.'),
         ('Do I need to label AI vocals?', 'Be clear with your audience that the vocal is AI-made, and check the rules of the platform you publish on.')])

add(slug='auto-tune-alternative-one-time-price', cluster='compare', kw='auto tune alternative one time price',
    title='Auto-Tune Alternatives With a One-Time Price (2026)',
    desc='Auto-Tune alternatives with a one-time price, compared by what they cost and what they do, plus a free option and a finishing app.',
    h1='Auto-Tune Alternatives With a One-Time Price',
    answer=('Several pitch tools sell for a one-time price: Waves Tune Real-Time, Synchro Arts RePitch and Celemony Melodyne are common examples. Prices change and differ by version, so check each vendor page. '
            'If you do not run a DAW and want to finish a rough vocal in one app, Tunedzy is a different kind of tool: it cleans, tunes, fits and masters a recording.'),
    body='''
<h2>The main options</h2>
<table><tr><th>Tool</th><th>Type</th><th>Price (check the vendor)</th><th>Best for</th></tr>
<tr><td>Waves Tune Real-Time</td><td>Plugin, real-time</td><td>listed at about $40 one-time</td><td>fast tracking and tuning in a DAW</td></tr>
<tr><td>Synchro Arts RePitch</td><td>Plugin, post-edit</td><td>listed from about $69 one-time</td><td>natural tuning after recording</td></tr>
<tr><td>Celemony Melodyne</td><td>Plugin, note editor</td><td>listed from about $99 one-time</td><td>note-by-note editing</td></tr>
<tr><td>BandLab AutoPitch</td><td>Free, in BandLab</td><td>free</td><td>beginners and mobile</td></tr>
<tr><td>Tunedzy</td><td>Standalone Windows app</td><td>free to start: 30 credits in the first month, then packs from $0.99 or a plan with no counting from $1.99 a month</td><td>finishing a rough vocal without a DAW</td></tr></table>
<h2>How to choose</h2>
<ul>
<li>Working in a DAW and tuning live? A real-time plugin fits.</li>
<li>Editing note by note? Melodyne is the tool people use for that.</li>
<li>No DAW, and you want the whole finish in one place? Use Tunedzy, and keep your own DAW for beats.</li>
</ul>
<h2>Limits</h2>
<p>Prices in this table were read from public pages in October 2026 and vary by version and sale. We do not claim any tool is better than another for every job. Try the free trial or the free option on one of your own recordings before you buy.</p>
''',
    faq=[('Is there a free Auto-Tune alternative?', 'BandLab AutoPitch is free within BandLab. Tunedzy also starts free with credits.'),
         ('Does Tunedzy replace a DAW?', 'No. It finishes a recording. Keep your DAW for writing and arranging beats.'),
         ('Why are prices in this article not exact?', 'Vendors change prices and sales often. Always check the current price on the vendor site.')])

add(slug='melodyne-alternative-for-beginners', cluster='compare', kw='melodyne alternative for beginners',
    title='Melodyne Alternative for Beginners: What to Use Instead',
    desc='A Melodyne alternative for beginners: when Melodyne is too much, the simpler tools to try first, and how to finish a vocal without learning note editing.',
    h1='A Melodyne Alternative for Beginners',
    answer=('Melodyne is a powerful note-by-note editor, and it has a learning curve. Beginners who need a clean vocal can start with simpler real-time pitch tools, a free option such as BandLab AutoPitch, '
            'or an app that finishes the vocal from start to end.'),
    body='''
<h2>When Melodyne is more than you need</h2>
<p>If you need to fix a few notes in one song, a note editor is slow to learn. A real-time tuner or a finishing app gets you to a usable vocal faster.</p>
<h2>Simpler options</h2>
<ul>
<li><strong>BandLab AutoPitch</strong>: free, simple, aimed at beginners.</li>
<li><strong>Waves Tune Real-Time</strong>: a one-time plugin for tracking and fast tuning.</li>
<li><strong>Tunedzy</strong>: a finishing app for a rough recording, with cleanup, tuning, fitting to the beat and mastering in one window. Free to start with credits.</li>
</ul>
<h2>When to keep Melodyne</h2>
<p>If you need precise control over timing and pitch of each note, a note editor is the right tool. Learning it takes time, and that is normal.</p>
<h2>Limits</h2>
<p>Simpler tools do less. They will not replace detailed note editing on a demanding vocal. Check each tool on one of your own recordings before you choose.</p>
''',
    faq=[('Is Melodyne hard to learn?', 'It has more controls than most beginners need. Start with the basic pitch and timing tools.'),
         ('Can I finish a vocal without learning note editing?', 'Yes, for many rough recordings a finishing app or real-time tuner is enough.'),
         ('Which free option should I try?', 'BandLab AutoPitch is free and simple. Tunedzy starts free with credits.')])

add(slug='nectar-alternative-without-a-daw', cluster='compare', kw='vocal chain plugin alternative without a DAW',
    title='A Vocal Chain Without a DAW: Nectar Alternatives',
    desc='A vocal chain without a DAW: what iZotope Nectar does, the alternatives for people who do not run one, and how to finish a rough vocal in a single app.',
    h1='A Vocal Chain Without a DAW: Nectar Alternatives',
    answer=('iZotope Nectar is a plugin vocal chain: it runs inside a DAW and has an assistant that suggests settings. '
            'If you do not run a DAW, or you want one window that cleans, tunes and masters a rough vocal, a finishing app is the alternative to look at.'),
    body='''
<h2>What Nectar is for</h2>
<p>Nectar puts the common vocal steps in one plugin: tuning, EQ, compression and effects, with an assistant. It needs a DAW and some mixing knowledge to use well.</p>
<h2>Alternatives by situation</h2>
<ul>
<li><strong>You have a DAW and want separate tools:</strong> a de-esser, an EQ, a compressor and a reverb you already own, in the order on the <a href="/tunedzy/blog/vocal-chain-for-rap-in-order">rap vocal chain guide</a>.</li>
<li><strong>You have no DAW:</strong> Tunedzy takes a rough recording through cleanup, tuning, fitting to a beat and mastering in one app, on Windows, with free credits to start.</li>
<li><strong>You want a phone app:</strong> Tunedzy Go runs on your phone for quick finishing.</li>
</ul>
<h2>Limits</h2>
<p>A finishing app is not a full DAW. Use it to finish a vocal, and do the writing and arranging in the tool you already know. Check the current price of Nectar on iZotope&rsquo;s site, since it changes.</p>
''',
    faq=[('Is Nectar a DAW plugin?', 'Yes. It runs inside a digital audio workstation.'),
         ('Can I use Tunedzy with my DAW?', 'Yes. Finish the vocal in Tunedzy and bring the file into your DAW for the mix.'),
         ('Does Tunedzy need an internet connection?', 'Processing runs on your own PC or phone. The app checks your credits online.')])
