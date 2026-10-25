"""How-to guides, batch 3 (25 October 2026). Topics come from the search research in seo/RESEARCH.md. Same shape as content.GUIDES.

Topics already covered by blog posts (mic pops, clipping, de-essing, LUFS targets, room tone) are not repeated here.
Every page says what works without a tool, and where Tunedzy helps. No invented numbers; no reviews or counts.
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


add('how-to-remove-breath-noise-from-a-voice-recording', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Remove Breath Noise From a Voice Recording',
    desc='Reduce or remove breaths in a voice recording: manual methods, the gate trick, and why breath removal can make a voice sound unnatural.',
    h1='How to Remove Breath Noise From a Voice Recording',
    kw='remove breath noise from voice recording',
    lead='Breaths are part of how a voice sounds human. The goal is to make loud or frequent breaths quieter, not to remove every one.',
    tldr=['Lower the loudest breaths rather than deleting them all.',
          'A gate set just above the room noise can catch the quiet breaths between phrases.',
          'Manual gain changes on each breath give the most natural result and take the longest.',
          'Record a little further from the mic next time: most breaths are loud because the mic is close.'],
    body='''
<h2>Decide how many to remove</h2>
<p>A recording with no breaths at all sounds unnatural, and listeners notice it. Aim to make the loudest and most frequent breaths quieter, so they no longer draw attention, and leave the rest. Listen to the take through once and mark only the breaths that distract.</p>
<h2>Method 1: lower each breath by hand</h2>
<p>In any editor, select a single breath and turn its gain down by a few decibels, then listen. This is slow, but it is the most natural method and it works on any length of recording. Keep the change small, and check that the words on either side of the breath are untouched.</p>
<h2>Method 2: a gate with a careful threshold</h2>
<p>A gate set just above the room noise can quieten the breaths between phrases, because a breath is quieter than speech and louder than silence. Measure the room tone first, set the threshold a little above it, and use a short attack and a longer release so word starts are not cut off. See <a href="/tunedzy/what-is-a-noise-gate">what a noise gate does</a> for the terms.</p>
<h2>Method 3: a breath tool</h2>
<p>Dedicated breath tools detect breaths automatically and reduce them. They can be very good on long voiceovers, but they also work on the breaths you want to keep, so compare the result with the original before you use it.</p>
<h2>Prevention</h2>
<p>Breath noise is mostly a distance problem. Move the mic a hand&rsquo;s width further away, speak slightly off-axis, and use a pop filter. A little distance lowers breath noise more than any filter does.</p>
<h2>Tunedzy</h2>
<p>Tunedzy&rsquo;s cleanup reduces steady noise and levels the voice in one pass. It does not target individual breaths, so breath handling is still a manual step: use Before and After to check that the phrasing still sounds like a person breathing.</p>
''',
    vf_title='Clean the take, keep the breath',
    vf='<p>Tunedzy reduces the noise and levels the voice in Perfect it. Breaths are a manual step: compare Before and After and keep the breaths that make the voice sound human.</p>',
    faq=[('Should I remove all breaths?', 'No. Removing every breath makes a voice sound unnatural. Reduce the loud ones and leave the rest.'),
         ('Why do my breaths sound louder on a phone?', 'The phone is close to the mouth and the mic is sensitive to air. Move back a hand&rsquo;s width and speak slightly off-axis.'),
         ('Can a gate remove breaths without cutting words?', 'It can, with a careful threshold and a short attack. A threshold set too high cuts the starts of words, so listen to the result.')],
    related=['clean-up-a-phone-voice-recording', 'remove-background-noise-from-a-voice-recording', 'record-a-voiceover-on-your-phone'])

add('how-to-clean-up-a-zoom-or-video-call-recording', 'desk', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='How to Clean Up a Zoom or Video Call Recording',
    desc='Clean up a recorded Zoom, Teams or Meet call: local versus cloud recordings, what cleanup can and cannot fix, and a sequence that works.',
    h1='How to Clean Up a Zoom or Video Call Recording',
    kw='clean up zoom recording audio',
    lead='Call audio is compressed and often mixed into one track, so cleanup has less to work with than a studio recording. Start with the best file you can get, then clean gently.',
    tldr=['Get separate local recordings for each speaker if the app offers them; they clean up much better.',
          'Use gentle settings on a mixed file: heavy noise reduction makes call audio sound thin.',
          'Fix echo and noise first, then level each speaker, then check the result.',
          'Recording locally on each person&rsquo;s own device beats any cleanup of a call.'],
    body='''
<h2>Get the best file</h2>
<p>Many call apps record a single mixed file, and some can record each participant on their own. Separate tracks are the best case, because you can clean and level each person before you combine them. Ask the people on the call to record locally too, if the app allows it, and keep the original file.</p>
<h2>Know what cleanup can fix</h2>
<p>Cleanup helps with steady fan noise, room hiss, light keyboard noise and mild echo. It cannot rebuild speech that was clipped or cut out, separate two people who talk over each other, or restore the thin sound that call compression leaves behind.</p>
<h2>A sequence that works</h2>
<ol>
<li>Remove the steady noise with a gentle setting.</li>
<li>Reduce echo only if it is clearly there; heavy echo removal makes the voice hollow.</li>
<li>Level each speaker so the quiet and loud guests sit at a similar volume.</li>
<li>Check the loudness and the true peak before you export.</li>
</ol>
<p>The <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup steps</a> apply to a call recording too. For a call with several people, the Multitrack studio in Tunedzy lets you level each voice on its own track before you mix.</p>
<h2>Where to start on your own call</h2>
<p>Record locally next time, use headphones so the other side does not echo back, and keep each person close to a mic. A good local recording needs less cleanup than any call audio.</p>
''',
    vf_title='Clean each voice on its own track',
    vf='<p>Multitrack in Tunedzy lets you clean and level each voice separately, then mix them with the loudness set to a target.</p>',
    faq=[('Can I clean a Zoom recording for free?', 'Yes, with a free editor or a browser tool, with the limits each one has. Tunedzy Go cleans a file on your phone for free.'),
         ('Why does my call sound thin after cleanup?', 'The noise reduction was too strong, or the call was already compressed. Use less reduction and a gentler setting.'),
         ('Can I separate two people who talk at once?', 'Not reliably. Overlapping speech is very hard to separate. Separate local tracks are the best way to avoid the problem.')],
    related=['clean-up-a-phone-voice-recording', 'edit-a-podcast-by-its-words', 'podcast-sound-professional-on-a-budget'])

add('how-to-remove-wind-noise-from-audio', 'neon', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Remove Wind Noise From Audio',
    desc='Remove wind rumble from an outdoor recording: why it happens, the high-pass fix, what it cannot do, and how to avoid it next time.',
    h1='How to Remove Wind Noise From Audio',
    kw='remove wind noise from audio',
    lead='Wind makes a deep, rumbling noise that is mostly low frequency. It is easier to remove than most noise, but only if the recording is not overloaded.',
    tldr=['Wind noise is mainly low rumble below about 100 to 150 Hz.',
          'A high-pass filter removes most of it without much harm to speech.',
          'Heavy wind that overloads the mic cannot be repaired.',
          'A foam or fur windshield is the real fix on location.'],
    body='''
<h2>What wind noise is</h2>
<p>Wind is turbulent air hitting the capsule of the microphone. It produces a low, moving rumble that is loudest in the bass and often sounds like a crackle or a roar. Speech sits mostly above that range, so the rumble can be removed without changing how the voice sounds.</p>
<h2>Remove it with a high-pass filter</h2>
<p>A high-pass filter lets the high frequencies through and cuts the lows. Start at about 100 Hz and move up slowly until the rumble is gone, then back off until the voice sounds natural. Going much higher than about 150 Hz thins a voice noticeably.</p>
<h2>What the filter cannot fix</h2>
<p>If the wind was loud enough to overload the mic, the crackle is distortion, not rumble, and a filter will not remove it. Check the waveform for flat tops. Those are clipping and need a clipping repair, which is a different job.</p>
<h2>Prevent it on location</h2>
<p>A foam windshield covers most breezes. A furry windshield (a deadcat) is the answer for stronger wind. Turn the mic so the capsule is out of the wind line and keep the recording level low enough that the wind does not push the meters into the red.</p>
<h2>Tunedzy</h2>
<p>Tunedzy&rsquo;s cleanup includes a low cut and a repair for clicks and clipping. Use Before and After to check that the low rumble is gone and that the voice is still full.</p>
''',
    vf_title='Cut the rumble, keep the voice',
    vf='<p>Tunedzy&rsquo;s cleanup removes low rumble and repairs the clipping that heavy wind can leave. Compare Before and After to check the result.</p>',
    faq=[('What frequency is wind noise?', 'Mostly below about 100 to 150 Hz, with the strongest part near the bottom of the voice range.'),
         ('Can a high-pass filter remove all the wind?', 'Not if the mic was overloaded. A filter removes rumble, but not distortion from a clipped recording.'),
         ('Is a foam windshield enough?', 'For a light breeze, yes. For strong wind, a furry windshield works much better.')],
    related=['remove-hum-from-audio', 'fix-clipped-distorted-audio', 'clean-up-a-phone-voice-recording'])

add('how-to-remove-keyboard-and-desk-noise-from-a-recording', 'desk-wide', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='How to Remove Keyboard and Desk Noise From a Recording',
    desc='Get rid of keyboard clicks, mouse clicks and desk bumps in a voice recording: a gate, a click repair and better mic placement.',
    h1='How to Remove Keyboard and Desk Noise From a Recording',
    kw='remove keyboard noise from recording',
    lead='Keyboard and mouse clicks are short, sharp sounds that sit on top of the voice. They are easier to remove with a click repair than with noise reduction.',
    tldr=['Keyboard clicks are short transients; treat them as clicks, not as steady noise.',
          'A gate can hide clicks between phrases; a click repair removes them under the voice.',
          'Use a boom arm or a stand so the mic is not on the desk.',
          'Record with the keyboard switched off where you can.'],
    body='''
<h2>Why the usual noise cleaner misses it</h2>
<p>Noise reduction is built for steady sound like a fan. A keyboard click is a single short sound, and it is over before a noise profile can learn it. A click repair is the right tool: it finds short spikes that stand out from the voice and replaces them with the sound around them.</p>
<h2>Step 1: move the mic off the desk</h2>
<p>Most desk noise travels through the desk. A boom arm, a stand or a shock mount takes the mic off the surface. This is the fix that matters most, and it costs little.</p>
<h2>Step 2: gate between phrases</h2>
<p>A gate silences the recording when the voice stops, so clicks between phrases disappear. It does nothing to clicks under the voice, so use it only for the gaps. Set a short attack and a long enough release that the ends of words are kept.</p>
<h2>Step 3: repair the clicks</h2>
<p>A click repair finds the short spikes and replaces them with interpolated audio. Use the lowest strength that removes the clicks. Listen to the result, because too strong a repair leaves a dull patch in the voice.</p>
<h2>Step 4: record it right</h2>
<p>If you can, record with the keyboard idle, type in a separate pass, or switch to a quieter keyboard with a softer key feel. Mouse clicks can be avoided by using a keyboard shortcut for the recording software.</p>
<h2>Tunedzy</h2>
<p>Tunedzy&rsquo;s Repair finds clicks and crackle and mends them, then the cleanup handles the steady noise. Check each click by ear: a few missed clicks are less noticeable than a patch of muffled voice.</p>
''',
    vf_title='Mend the clicks, keep the voice',
    vf='<p>Tunedzy&rsquo;s Repair finds clicks and crackle and mends them before the cleanup. Use Before and After to listen for any patches.</p>',
    faq=[('Why does a noise cleaner not remove keyboard clicks?', 'A noise cleaner works on steady sound. Clicks are short and sharp, and need a click repair.'),
         ('Does a boom arm help?', 'Yes. It takes the mic off the desk, so the desk does not carry the typing into the mic.'),
         ('Can I remove mouse clicks too?', 'Yes, with the same click repair. Using keyboard shortcuts while recording avoids most of them.')],
    related=['remove-background-noise-from-a-voice-recording', 'clean-up-a-phone-voice-recording', 'remove-background-noise-from-a-voice-recording'])

add('how-to-make-audio-louder-without-distortion', 'mic', ['lufs-meter', 'vocal-checker'],
    title='How to Make Audio Louder Without Distortion',
    desc='Raise the level of a quiet recording safely: gain, normalising, true peak checks and when a limiter helps, with the limits of each.',
    h1='How to Make Audio Louder Without Distortion',
    kw='make audio louder without distortion',
    lead='A quiet recording can be made louder, but only up to the point where the peaks reach the top. Past that, the sound distorts. Measure first, then raise the level in one clean step.',
    tldr=['Measure the peaks before you raise the level; the highest peak sets the limit.',
          'Raise the gain in one step rather than stacking many small boosts.',
          'Check the true peak after you raise the level, not only the sample peak.',
          'A limiter can raise the average level, but it squashes the voice if you push it.'],
    body='''
<h2>Find the limit first</h2>
<p>The loudest peak in the file is what limits how much you can raise it. If the peak is at -20 dB, you have about 20 dB of room before it reaches full scale. Measure this in your editor before you change anything.</p>
<h2>Raise the gain once</h2>
<p>Apply one gain change that brings the peaks to a safe level, rather than boosting several times. Each boost adds a little noise and distortion, so one step is cleaner.</p>
<h2>Check the true peak</h2>
<p>Peaks in a file can be higher once the audio is converted to MP3 or AAC. Check the true peak, not only the sample peak, and keep it below about -1 dBTP. The <a href="/tunedzy/what-is-true-peak-dbtp">true peak explanation</a> covers the reasons.</p>
<h2>A limiter, used carefully</h2>
<p>A limiter lowers the loudest peaks so you can raise the rest of the level. A gentle limit of a few decibels can make a voice sound more even. Push it too far and the voice sounds squashed and tired. Use it to even out, not to force a level.</p>
<h2>Do not fix a clipped file by making it louder</h2>
<p>If the file already clips, raising the level makes the distortion louder. Repair the clipping first, then raise the level.</p>
<h2>Tunedzy</h2>
<p>Tunedzy&rsquo;s match loudness raises or lowers a recording to a target and checks the true peak, so you do not need to do the arithmetic. Pick the target that matches where the file is going.</p>
''',
    vf_title='Raise it to a target, check the peak',
    vf='<p>Tunedzy sets the loudness to a target and checks the true peak, so a quiet recording comes up without clipping.</p>',
    faq=[('Is normalising the same as making it louder?', 'Normalising raises the file so its highest peak reaches a chosen level. It makes the file louder only as far as the peak allows.'),
         ('Why does my louder file sound harsh?', 'Either it clipped, or it was pushed with too much limiting. Check the peaks and reduce the limiter.'),
         ('What level should I aim for?', 'It depends on the platform. The loudness guide on this site explains the targets people use.')],
    related=['loudness-for-youtube-podcasts-and-spotify', 'fix-clipped-distorted-audio', 'what-is-true-peak-dbtp'])

add('how-to-export-audio-for-spotify-and-apple-podcasts', 'desk', ['lufs-meter', 'vocal-checker'],
    title='How to Export Audio for Spotify and Apple Podcasts',
    desc='Export a podcast or music file that plays well on Spotify and Apple Podcasts: format, sample rate, loudness, true peak and what to check before you upload.',
    h1='How to Export Audio for Spotify and Apple Podcasts',
    kw='export audio for spotify apple podcasts',
    lead='Streaming platforms re-encode your file, so the export matters. Export a clean, high-quality master, check its loudness and true peak, and upload that file.',
    tldr=['Export a high-quality file (WAV or a high-bitrate MP3) as the master you keep.',
          'Check the loudness and the true peak of the final file, not the project.',
          'Keep the true peak at or below -1 dBTP so the platform re-encoding does not distort it.',
          'Check each platform&rsquo;s current guidance before you upload, because it changes.'],
    body='''
<h2>Keep a master</h2>
<p>Export a lossless or high-quality master, usually WAV at the project sample rate, and keep it. Every MP3 is a copy made from the master, and the master lets you re-export if a platform asks for something different.</p>
<h2>Choose the upload format</h2>
<p>Most podcast hosts and streaming services accept WAV or MP3. A high-bitrate MP3 is a common upload format and works well. Check the format and bit rate the platform recommends, because the rules change.</p>
<h2>Set the loudness</h2>
<p>Measure the loudness of the whole episode or track, not a short part, and set it to the target you want. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> lists the targets people use and why they differ between platforms.</p>
<h2>Check the true peak</h2>
<p>Re-encoding can raise the peaks. Keep the true peak at or below -1 dBTP so the file does not distort when the platform converts it. If it is higher, lower the level or use a true-peak limiter at -1 dBTP.</p>
<h2>Listen to the exported file</h2>
<p>Play the exported file, not the project. Listen on a phone and on headphones, and check the start, the end and any music bed. A file that sounds right in the editor can still sound different after conversion.</p>
<h2>Tunedzy</h2>
<p>Tunedzy exports the mix at a loudness target with the true peak checked, and keeps the master. Use the free LUFS meter on this site to check a file you did not make in Tunedzy.</p>
''',
    vf_title='Export the master and the upload',
    vf='<p>Tunedzy exports at a loudness target with the true peak checked, and keeps the master for re-exports.</p>',
    faq=[('Should I upload WAV or MP3?', 'Check the platform. Many accept both. Keep the WAV master and upload the format the platform recommends.'),
         ('Why does my upload sound louder or quieter than my export?', 'The platform normalises loudness and re-encodes the file. Measure the export and check its true peak before you upload.'),
         ('Is there one correct loudness?', 'No. Targets differ by platform and change over time. Check the current guidance for each one.')],
    related=['loudness-for-youtube-podcasts-and-spotify', 'what-is-true-peak-dbtp', 'podcast-sound-professional-on-a-budget'])

add('how-to-make-a-voice-sound-warmer', 'booth-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Make a Voice Sound Warmer',
    desc='Make a thin or harsh voice sound warmer and fuller with equalisation, a low-mid lift, and a gentle compressor, without muddying it.',
    h1='How to Make a Voice Sound Warmer',
    kw='make voice sound warmer',
    lead='A warm voice has body in the low mids and smooth top end. A thin voice often needs a small lift in the low mids and a little less harshness, not more bass.',
    tldr=['Warmth lives roughly in the low mids, around 150 to 300 Hz, not in the deep bass.',
          'Cut a little harshness around 3 to 5 kHz before you add anything.',
          'A gentle compressor evens the voice so the warmth stays steady.',
          'Too much bass makes a voice muddy. Adjust by ear, in small steps.'],
    body='''
<h2>What warmth is</h2>
<p>People hear a voice as warm when the low mids have body and the top end is smooth rather than sharp. Warmth is not the same as bass. A voice with too much low end sounds boomy; a voice with a gentle lift in the low mids sounds full.</p>
<h2>Step 1: find what is wrong</h2>
<p>A thin voice usually lacks the low mids. A harsh voice has too much energy around 3 to 5 kHz. Listen on headphones, then pick the one that is wrong before you change anything.</p>
<h2>Step 2: lift the low mids gently</h2>
<p>Try a small boost of 1 to 3 dB between about 150 and 300 Hz. Keep the boost broad and modest. Stop when the voice sounds fuller without any boom.</p>
<h2>Step 3: soften the harshness</h2>
<p>If the voice sounds sharp, cut 1 to 3 dB around 3 to 5 kHz with a broad cut. That removes the edge without dulling the words, which need the presence range to stay clear.</p>
<h2>Step 4: even it with a compressor</h2>
<p>A gentle compressor, a ratio of about 2 to 1 with a slow attack, keeps the voice at a steady level. That makes the warmth consistent from one phrase to the next. The <a href="/tunedzy/blog/what-is-vocal-compression-and-what-settings-to-use">vocal compression guide</a> covers the settings.</p>
<h2>What to avoid</h2>
<p>Do not chase warmth with a big bass boost. It makes the voice muddy and hides the words. Keep the low cut in place, and make small changes.</p>
<h2>Tunedzy</h2>
<p>Tunedzy&rsquo;s tone step in Perfect it shapes the voice toward a clear, even sound. Use Before and After to check the warmth, and reduce the effect if it starts to sound muddy.</p>
''',
    vf_title='Warm it up without the mud',
    vf='<p>Tunedzy&rsquo;s tone step sets the voice toward a clear, even sound. Compare Before and After before you keep it.</p>',
    faq=[('Is warm the same as bass?', 'No. Warmth is body in the low mids. Too much bass makes a voice boomy and muddy.'),
         ('Which frequency makes a voice sound thin?', 'A lack of energy around 150 to 300 Hz often makes a voice thin. Try a small lift there first.'),
         ('Will a compressor make it warmer?', 'It makes the level steadier, which often sounds fuller. It does not add warmth by itself.')],
    related=['fix-a-muffled-voice-recording', 'remove-background-noise-from-a-voice-recording', 'clean-up-a-phone-voice-recording'])

add('how-to-isolate-a-voice-from-background-music', 'neon', ['vocal-checker', 'song-key-finder'],
    title='How to Isolate a Voice From Background Music',
    desc='Pull the voice out of a song or a video with music: how stem separation works, what it can and cannot do, and the rights you need first.',
    h1='How to Isolate a Voice From Background Music',
    kw='isolate voice from background music',
    lead='Stem separation splits a mix into a voice and an instrumental. It works well on a clear mix and less well on a dense one. Use it only on audio you have the right to use.',
    tldr=['Separation works best on a clear recording with a single voice and a moderate backing.',
          'Expect some bleed: a little music or a little voice always ends up in the other part.',
          'Check the rights first: only separate audio you own or are allowed to use.',
          'Clean the separated voice afterwards, the same as any other recording.'],
    body='''
<h2>Check you are allowed to use it</h2>
<p>Separating a voice from a song you do not own can be a copyright issue, even for personal use. Use your own recordings, material with a licence that allows it, or your own vocal stems. Check before you start.</p>
<h2>How it works</h2>
<p>A separation model learns what a voice sounds like and what music sounds like, then splits a mix into parts. The voice part is the vocal stem, and the rest is the instrumental. Dense, loud mixes with many instruments in the same range are harder to split cleanly.</p>
<h2>What to expect</h2>
<p>The result is rarely perfect. Expect some bleed, with drums or reverb in the vocal and a little voice in the instrumental. A short phrase often comes out better than a whole song. Check the separated voice by ear before you use it.</p>
<h2>Clean the result</h2>
<p>A separated voice often has a watery or crunchy edge. Use gentle noise reduction, and check the level and the tone the same way you would for a recording made in a room.</p>
<h2>Tunedzy</h2>
<p>Tunedzy has a vocal remover and a stem mixer. The Quick edit and Multitrack tools let you line the voice up with your beat and clean it. Use it only on audio you have the right to use.</p>
''',
    vf_title='Separate it, check it, then clean it',
    vf='<p>Tunedzy&rsquo;s vocal remover separates a voice from music on your own PC. Check the result by ear, then clean it.</p>',
    faq=[('Can a separated vocal sound perfect?', 'Rarely. Some bleed is normal, especially on a dense mix. Short passages come out cleaner.'),
         ('Is it legal to remove vocals from a song?', 'It depends on the rights. Only separate audio you own or are licensed to use, and check the rules where you live.'),
         ('Does Tunedzy upload the song?', 'No. Separation runs on your PC.')],
    related=['record-a-vocal-at-home-for-a-song', 'clean-up-a-phone-voice-recording', 'tunedzy-vs-audacity'])

add('how-to-record-a-voice-on-a-laptop-microphone', 'desk', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='How to Record a Voice on a Laptop Microphone',
    desc='Get a usable voice recording from a laptop mic: placement, room, levels, and the cleanup that helps most.',
    h1='How to Record a Voice on a Laptop Microphone',
    kw='record voice on laptop microphone',
    lead='A laptop microphone picks up the fan, the keyboard and the room. You can still get a clear voice from it by controlling the room and the distance.',
    tldr=['Sit close to the laptop, a hand&rsquo;s width or so from the mic, and speak towards it.',
          'Turn off the fan where you can, and move the laptop off the desk onto a stand.',
          'Record in a soft room; the laptop mic makes the room more obvious.',
          'Clean the recording afterwards with gentle settings.'],
    body='''
<h2>Position the mic</h2>
<p>Most laptop mics sit on the top edge or underneath the screen, and they pick up sound best from the front. Sit a hand&rsquo;s width away, speak towards the screen and keep your voice at a steady distance.</p>
<h2>Control the noise</h2>
<p>Lift the laptop onto a stand so the fan and the desk are not right under the mic. Close other programs that make the fan run, and turn off the fan if the laptop allows it. Keep the keyboard quiet by typing in a pause, not during the take.</p>
<h2>Control the room</h2>
<p>A laptop mic is very sensitive to the room. A bedroom with a rug, curtains and soft furniture gives a far better voice than a bare kitchen. A wardrobe full of clothes is still the cheapest good booth.</p>
<h2>Level and record</h2>
<p>Check the level before the take. Loud peaks mean move back; a faint voice means move closer or raise the input. Record a few takes and keep the best.</p>
<h2>Clean it afterwards</h2>
<p>Use the <a href="/tunedzy/clean-up-a-phone-voice-recording">cleanup steps</a>. Start gently: the laptop mic has less detail than a dedicated mic, so heavy processing makes it sound thin.</p>
''',
    vf_title='Clean the laptop take',
    vf='<p>Tunedzy cleans a recording from any mic, including a laptop mic, in one pass on your PC. Compare Before and After.</p>',
    faq=[('Can a laptop mic sound good enough for a podcast?', 'For speech in a good room, yes, it can be usable. A dedicated mic close to the mouth in the same room will sound better.'),
         ('Why does my laptop voice sound tinny?', 'The laptop mic is small and far from the mouth. Move closer and record in a softer room.'),
         ('Should I use the laptop mic for streaming?', 'It works for a simple stream. Live cleanup of the mic can help, and a dedicated mic helps more.')],
    related=['clean-up-a-phone-voice-recording', 'voice-note-sounds-better-on-an-iphone', 'how-to-remove-keyboard-and-desk-noise-from-a-recording'])

add('how-to-record-a-remote-podcast-guest', 'mic-wide', ['voice-recorder-noise-cancellation', 'lufs-meter'],
    title='How to Record a Remote Podcast Guest Well',
    desc='Get a usable recording from a remote podcast guest: their room, their mic, a local backup and the cleanup that makes the two voices match.',
    h1='How to Record a Remote Podcast Guest Well',
    kw='record remote podcast guest',
    lead='A remote guest is recorded on their own device in their own room, so you control less. Ask for the basics, keep a local backup, and level the two voices together.',
    tldr=['Ask the guest for a quiet room, a mic close to the mouth and headphones.',
          'Record locally on each device if the call app allows it, as a backup.',
          'Level the guest and the host to the same loudness before you mix.',
          'Clean each voice separately, then export a single loudness target.'],
    body='''
<h2>Set expectations before the call</h2>
<p>Send the guest a short note: a quiet room with soft furnishings, headphones rather than speakers, a mic close to the mouth, and a test recording a day before. Most poor remote audio is a guest who did not know these things.</p>
<h2>Keep a local backup</h2>
<p>Ask the guest to record locally on their device while you talk. The call audio is compressed, and a local file is far cleaner. If the call drops, the local file is the one you use.</p>
<h2>Level the two voices</h2>
<p>A guest on a laptop mic and a host on a dedicated mic will sound very different. Bring each voice to a similar loudness before you mix, and check the balance on headphones and on a phone speaker.</p>
<h2>Clean each voice</h2>
<p>Clean the guest and the host separately, because their rooms and their mics differ. Gentle settings are safer on the call audio. The <a href="/tunedzy/how-to-clean-up-a-zoom-or-video-call-recording">call cleanup guide</a> has the sequence.</p>
<h2>Export one loudness</h2>
<p>When both voices match, set the whole episode to one loudness target and check the true peak. Then export the master.</p>
''',
    vf_title='Match two voices in one mix',
    vf='<p>Multitrack in Tunedzy levels each voice on its own track and exports the episode at a loudness target.</p>',
    faq=[('Should I ask the guest to record locally?', 'Yes, if the call app allows it. It is the best backup and gives much cleaner audio.'),
         ('What if the guest has a bad mic?', 'Ask them to move the mic closer and use headphones. Clean what you can, and record the next episode with better settings.'),
         ('How do I make the voices match?', 'Level each voice separately before mixing, then check the balance on headphones and a phone speaker.')],
    related=['podcast-sound-professional-on-a-budget', 'how-to-clean-up-a-zoom-or-video-call-recording', 'edit-a-podcast-by-its-words'])

add('how-to-clean-up-an-interview-recording', 'booth', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='How to Clean Up an Interview Recording',
    desc='Clean up an interview recorded on a phone or a recorder: noise, levels, the two voices, and cutting the ums and pauses without losing the speaker.',
    h1='How to Clean Up an Interview Recording',
    kw='clean up interview recording',
    lead='An interview is mostly speech, so the job is to make both voices clear and even, cut the distractions and keep the speaker sounding like themselves.',
    tldr=['Clean the whole recording once, gently, before you edit.',
          'Level the interviewer and the speaker so neither is too quiet.',
          'Cut ums and long pauses, but leave the natural breaths and the thinking pauses.',
          'Always keep the original and check every cut by ear.'],
    body='''
<h2>Clean first, edit second</h2>
<p>Clean the whole interview before you cut it. Editing first can leave the background noise changing at every cut, which sounds worse than one steady clean.</p>
<h2>Level both voices</h2>
<p>An interviewer often sits closer to the mic than the speaker. Bring each voice to a similar level, so the listener does not have to adjust the volume between questions and answers.</p>
<h2>Cut carefully</h2>
<p>Remove ums, long gaps and repeated words, but keep the pauses that let a thought land. A speaker who sounds too quick and too smooth often sounds less like themselves. The <a href="/tunedzy/edit-a-podcast-by-its-words">edit by words guide</a> covers the process.</p>
<h2>Check the speaker</h2>
<p>Play the edited interview back and check that the speaker still sounds like themselves: the same pace, the same warmth and the same breath. Keep the original file in case a cut sounds wrong later.</p>
''',
    vf_title='Clean and edit the interview',
    vf='<p>Tunedzy cleans the recording, levels the voices, and lets you edit by the transcript with the captions exported at the end.</p>',
    faq=[('Should I remove every um?', 'No. Remove the distracting ones and keep the natural ones that make the speaker sound human.'),
         ('Can I transcribe an interview for captions?', 'Yes. A transcript made on your own PC gives you captions and show notes. Check names and quotes before you publish.'),
         ('Why does the interview sound uneven?', 'The two voices were at different distances from the mic. Level them separately.')],
    related=['edit-a-podcast-by-its-words', 'how-to-record-a-remote-podcast-guest', 'podcast-sound-professional-on-a-budget'])
