"""Batch 4c (25 October 2026): eight glossary pages. Each gives one plain definition first, why it matters for a voice recording, and how to check it.

GROUP_OF marks every page as 'glossary' for the hub.
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


add('what-is-dynamic-range', 'mic-wide', ['lufs-meter', 'vocal-checker'],
    title='What Is Dynamic Range? Plain Explanation for Audio',
    desc='Dynamic range is the gap between the quietest and loudest parts of a recording. What it means for a voice, and when to keep it or reduce it.',
    h1='What Is Dynamic Range?',
    kw='what is dynamic range audio',
    lead='Dynamic range is the difference between the quietest and the loudest sound in a recording, measured in decibels. A wide range is natural; a narrow one is tight and even.',
    tldr=['Dynamic range is the gap from the quietest part to the loudest part.',
          'Speech naturally varies, so some range is normal and expressive.',
          'Too much range makes quiet words hard to hear on a phone.',
          'Compression narrows the range; keep it gentle to stay natural.'],
    body='''
<h2>The short definition</h2>
<p>Dynamic range is the distance, in decibels, between the quietest and the loudest parts of a recording that you can hear above the noise. A voice recorded in a quiet room has a wide range. The same voice in a noisy room has a smaller one, because the noise fills the quiet parts.</p>
<h2>Why it matters for voice</h2>
<p>Speech needs some range to sound expressive. Listeners on a phone, in a car or in a noisy kitchen do not hear the quiet parts well, so a very wide range makes the voice hard to follow. That is where gentle levelling helps.</p>
<h2>How to change it</h2>
<p>A compressor narrows the range by lowering the loud parts. A limiter stops the peaks. Raising the quiet parts with gain widens the apparent evenness without changing the peaks. The <a href="/tunedzy/what-is-a-compressor">compressor explanation</a> covers the controls.</p>
<h2>How to check it</h2>
<p>Listen to the recording on a phone speaker and on headphones. If you have to keep reaching for the volume, the range is too wide. If it sounds flat and tired, the range is too narrow.</p>
''',
    vf_title='Even it out without losing the voice',
    vf='<p>Tunedzy levels a voice to a target and checks the peaks. Compare Before and After to keep the expression.</p>',
    faq=[('Is a wide dynamic range good?', 'For a natural voice, a reasonable range is good. Very wide ranges need levelling for phone listening.'),
         ('What is a typical dynamic range for speech?', 'It depends on the room and the speaker. Measure your own recording rather than relying on a number.'),
         ('Does dynamic range equal loudness?', 'No. Dynamic range is the gap between quiet and loud; loudness is the average level.')],
    related=['what-is-a-compressor', 'what-is-a-limiter', 'what-is-lufs'])

add('what-is-a-compressor', 'mic', ['vocal-checker', 'lufs-meter'],
    title='What Is a Compressor? Plain Explanation for Voice',
    desc='A compressor turns down the loud parts of a sound once they pass a threshold, evening out a voice. The controls and how to set a gentle one.',
    h1='What Is a Compressor?',
    kw='what is a compressor audio',
    lead='A compressor reduces the level of a sound once it goes above a threshold. For a voice, it evens out the loud and quiet words so the speaker stays steady.',
    tldr=['A compressor lowers the loud parts above a threshold you set.',
          'Ratio sets how much it lowers them; a ratio of about 2 to 1 is gentle.',
          'Attack and release control how quickly it reacts.',
          'Make-up gain raises the whole sound back to a usable level.'],
    body='''
<h2>The short definition</h2>
<p>A compressor is a processor that reduces the volume of a sound when it rises above a level called the threshold. The amount of reduction is set by the ratio. Compression makes the loud parts quieter, so the overall level can be raised without the peaks getting too high.</p>
<h2>The main controls</h2>
<ul>
<li><strong>Threshold:</strong> the level above which compression starts.</li>
<li><strong>Ratio:</strong> how much the loud parts are reduced. 2 to 1 is gentle, 4 to 1 is firm for voice.</li>
<li><strong>Attack:</strong> how quickly the compressor reacts. Slow attack keeps the start of words.</li>
<li><strong>Release:</strong> how quickly it lets go. Too fast can sound pumpy.</li>
<li><strong>Make-up gain:</strong> raises the level back up after compression.</li>
</ul>
<h2>A gentle setting for voice</h2>
<p>Start with a ratio near 2 to 1, a moderate threshold so it works on the loud words only, a slow-to-medium attack and a medium release. Listen. The voice should sound steadier, not squashed. The <a href="/tunedzy/blog/what-is-vocal-compression-and-what-settings-to-use">vocal compression guide</a> has more detail.</p>
<h2>Watch for</h2>
<p>Too much compression makes a voice sound tired and close, and it raises the room noise between words. Use less compression and a cleaner recording rather than more compression to hide noise.</p>
''',
    vf_title='Even the voice, keep it natural',
    vf='<p>Tunedzy levels and evens a voice in its finishing steps. Use Before and After to check the voice still sounds like the speaker.</p>',
    faq=[('Is a compressor the same as a limiter?', 'They are related. A limiter is a compressor with a very high ratio that stops the peaks.'),
         ('Why does my compressed voice sound pumpy?', 'The release is too fast, or the ratio is too high. Slow the release and lower the ratio.'),
         ('Should I compress every recording?', 'Not always. A steady, well-recorded voice may need little or none.')],
    related=['what-is-a-limiter', 'what-is-dynamic-range', 'what-is-headroom'])

add('what-is-a-limiter', 'mic', ['lufs-meter', 'vocal-checker'],
    title='What Is a Limiter? Plain Explanation for Loudness',
    desc='A limiter stops the peaks of a sound from going above a ceiling. What it does for loudness, when it helps and when it squashes a voice.',
    h1='What Is a Limiter?',
    kw='what is a limiter audio',
    lead='A limiter is a compressor set to stop the peaks above a ceiling. It lets you raise the overall level while keeping the loudest moments under control.',
    tldr=['A limiter stops peaks from going above a set ceiling.',
          'It is used to protect against clipping and to control loudness.',
          'Pushed hard, it squashes the voice and makes it sound tired.',
          'A true-peak limiter at -1 dBTP is a common safe setting for exports.'],
    body='''
<h2>The short definition</h2>
<p>A limiter is a processor that keeps the level of a sound below a ceiling. Anything that would go above it is turned down, so the peaks cannot clip. It acts very quickly and usually has a very high ratio.</p>
<h2>Why people use one</h2>
<p>A limiter lets you raise the average level of a recording, because the loud peaks are held back. This is how a file reaches a loudness target without clipping. A true-peak limiter also watches the levels between the samples, which matters for conversion. The <a href="/tunedzy/what-is-true-peak-dbtp">true peak explanation</a> covers why.</p>
<h2>When it hurts</h2>
<p>A limiter pushed too far squashes the voice. The consonants lose their snap and the speech sounds flat and tired. If you need a lot of limiting to reach a target, the recording needs more level control before the limiter, or a quieter target.</p>
<h2>A safe setting</h2>
<p>Set the ceiling to -1 dBTP for an export that will be converted. Use only enough gain reduction to catch the peaks. Listen to the speech, not the meter.</p>
''',
    vf_title='Reach the target without clipping',
    vf='<p>Tunedzy sets a loudness target and checks the true peak, so a file reaches its level without clipping.</p>',
    faq=[('Does a limiter remove clipping?', 'It prevents new clipping. It cannot restore peaks that were already clipped.'),
         ('What ceiling should I use?', 'For a file that will be converted, -1 dBTP is a common choice.'),
         ('Is limiting the same as loudness?', 'Limiting lets you raise loudness. The level you reach depends on how far you push it.')],
    related=['what-is-true-peak-dbtp', 'what-is-a-compressor', 'how-to-make-audio-louder-without-distortion'])

add('what-is-headroom', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='What Is Headroom? Plain Explanation for Recording',
    desc='Headroom is the space between your recording level and full scale. Why leaving some headroom protects your recording and how much to leave.',
    h1='What Is Headroom?',
    kw='what is headroom audio',
    lead='Headroom is the space left between the loudest level of a recording and the top of the meter, full scale. It protects the recording from clipping.',
    tldr=['Headroom is the gap between your peaks and full scale.',
          'Leaving some headroom while recording avoids clipping.',
          'Too much headroom makes the recording quiet and noisy when raised.',
          'A typical recording aims for peaks well below full scale, then is raised later.'],
    body='''
<h2>The short definition</h2>
<p>Headroom is the margin between the loudest part of a recording and the point where digital audio clips, which is full scale. It is measured in decibels. If your loudest word peaks at -6 dB, you have 6 dB of headroom.</p>
<h2>Why leave some</h2>
<p>An unexpected laugh, a loud consonant or a sudden movement can push a recording over full scale. Leaving headroom while you record gives room for those moments. It is much better to record a little quiet and raise the level afterwards than to clip the take.</p>
<h2>How much</h2>
<p>A common target for recording is peaks around -6 dB, which leaves room but keeps the recording clean. The exact number matters less than keeping the loudest moments well below the top of the meter.</p>
<h2>Too much headroom</h2>
<p>If the recording is very quiet, raising it also raises the noise. Use the gain on the mic or the recorder to bring the level up before you record, rather than raising it in the editor.</p>
''',
    vf_title='Record with room, master with care',
    vf='<p>Tunedzy checks the peaks and the true peak before it exports, so the headroom is kept on the file you publish.</p>',
    faq=[('What is a good peak level when recording?', 'Many people aim for peaks around -6 dB. That leaves room for surprises.'),
         ('Is headroom the same as a limiter?', 'No. Headroom is space left in the recording. A limiter is a tool that controls the peaks.'),
         ('Should I leave headroom in the final export?', 'Yes, a true peak at or below -1 dBTP is the usual safe ceiling for a published file.')],
    related=['what-is-true-peak-dbtp', 'what-is-a-limiter', 'my-recording-is-too-quiet'])

add('what-is-sample-rate', 'booth', ['lufs-meter', 'vocal-checker'],
    title='What Is Sample Rate? Plain Explanation for Audio',
    desc='Sample rate is how many times per second a recording measures the sound. What 44.1 kHz and 48 kHz mean for voice, and whether it matters.',
    h1='What Is Sample Rate?',
    kw='what is sample rate audio',
    lead='Sample rate is how many times per second a digital recording measures the sound. For voice, 44.1 kHz and 48 kHz are both more than enough; the room and the mic matter far more.',
    tldr=['Sample rate is the number of measurements per second, in kHz.',
          '44.1 kHz is the CD rate; 48 kHz is the video and phone rate.',
          'Both are far above what speech needs; the difference is rarely audible for voice.',
          'Keep the sample rate of the original recording to avoid conversion.'],
    body='''
<h2>The short definition</h2>
<p>A digital recording measures the sound many thousands of times each second. The sample rate is that number. 44.1 kHz means 44,100 measurements per second. Higher rates capture higher frequencies, but the audible range is limited, so the extra detail is mostly above what people hear.</p>
<h2>44.1 and 48 kHz</h2>
<p>44.1 kHz is the standard for music CDs and is common for audio. 48 kHz is standard for video and many phones and recorders. Either works well for voice, and Tunedzy works at both.</p>
<h2>Why it matters in practice</h2>
<p>Changing the sample rate means resampling, and each conversion can add a little processing. Keep the rate of the original where you can. If a project and a file have different rates, the software converts them, which is normal and safe.</p>
<h2>What matters more</h2>
<p>For a voice recording, the room, the mic distance and the noise matter far more than the sample rate. A 48 kHz recording of a noisy room sounds worse than a close 44.1 kHz recording of a quiet one.</p>
''',
    vf_title='Keep the original rate',
    vf='<p>Tunedzy keeps the sample rate of your recording where it can, and converts only when a format needs it.</p>',
    faq=[('Is 48 kHz better than 44.1 kHz for voice?', 'Not for hearing. Both are more than enough. Choose the rate your device or video uses.'),
         ('Does sample rate change loudness?', 'No. It changes how finely the sound is measured, not how loud it is.'),
         ('What is the sample rate of a phone recording?', 'It depends on the phone and the app. Check the file properties in your editor.')],
    related=['what-is-bit-depth', 'how-to-choose-wav-mp3-or-flac', 'what-is-headroom'])

add('what-is-bit-depth', 'booth-wide', ['lufs-meter', 'vocal-checker'],
    title='What Is Bit Depth? Plain Explanation for Audio',
    desc='Bit depth sets how finely a recording measures loudness: 16, 24 and 32 bit. What each means for voice and why 24 bit is a sensible master.',
    h1='What Is Bit Depth?',
    kw='what is bit depth audio',
    lead='Bit depth is how finely a recording measures how loud each sample is. 16 bit is the CD standard, 24 bit gives more room for editing, and 32 bit float is common in editors.',
    tldr=['Bit depth sets the precision of each measurement: 16, 24 or 32 bit.',
          '16 bit is the CD standard and is enough for playback.',
          '24 bit gives more room for editing and quieter sections without noise.',
          'Edit at 24 or 32 bit float, and export to 16 bit only for the final format that needs it.'],
    body='''
<h2>The short definition</h2>
<p>Bit depth is the number of bits used to store each measurement of the sound. More bits give a finer scale, so quiet sounds are described more precisely and the noise floor of the recording is lower. It does not change the sample rate, which is how often the sound is measured.</p>
<h2>16, 24 and 32 bit</h2>
<ul>
<li><strong>16 bit:</strong> the CD standard. Enough for playback, but less room for editing.</li>
<li><strong>24 bit:</strong> common for recording and editing. A safe master for voice.</li>
<li><strong>32 bit float:</strong> used inside many editors. It handles very large changes in level without clipping inside the editor.</li>
</ul>
<h2>What to do</h2>
<p>Record and edit at 24 bit or higher. Keep the master at 24 bit. Export to 16 bit only when a platform or a format asks for it, usually at the very end. Each step down is a loss you cannot undo.</p>
<h2>Does it change how a voice sounds?</h2>
<p>Only in the quiet detail, and only when you cut or boost a lot. A voice recorded and exported at 24 bit sounds the same as at 16 bit on most devices. The difference is the room you keep for editing.</p>
''',
    vf_title='Edit at 24 bit, export what you need',
    vf='<p>Tunedzy keeps a higher-precision master and exports the format you choose, so editing does not cost detail.</p>',
    faq=[('Is 16 bit enough for podcasts?', 'For listening, yes. Edit and keep the master at 24 bit, then export 16 bit or MP3 at the end if you need to.'),
         ('Does 24 bit make a file louder?', 'No. It changes the precision, not the level.'),
         ('What is 32 bit float?', 'A format editors use internally. It keeps the sound precise through many changes.')],
    related=['what-is-sample-rate', 'how-to-choose-wav-mp3-or-flac', 'what-is-headroom'])

add('what-is-a-condenser-vs-dynamic-microphone', 'mic', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='Condenser vs Dynamic Microphone: Which for Voice?',
    desc='The difference between condenser and dynamic microphones, what each is good at for voice, and which to choose for your room.',
    h1='Condenser vs Dynamic Microphone',
    kw='condenser vs dynamic microphone voice',
    lead='A dynamic microphone is sturdy and rejects room sound, so it suits untreated rooms. A condenser is more sensitive and detailed, and suits quiet, soft rooms.',
    tldr=['Dynamic mics are sturdy and handle loud sounds and untreated rooms well.',
          'Condenser mics are more sensitive and detailed, and pick up more of the room.',
          'Condenser mics often need phantom power, from an interface or a mixer.',
          'For most untreated rooms, start with a dynamic mic; for a soft room, a condenser can sound lovely.'],
    body='''
<h2>How they work</h2>
<p>A dynamic mic uses a moving coil and a magnet, like a small loudspeaker in reverse. It is simple, sturdy and does not need power. A condenser mic uses a charged plate that moves with sound. It needs power, often 48 volts called phantom power, and it is more sensitive.</p>
<h2>What that means for voice</h2>
<p>A dynamic mic rejects more of the room, so it suits an untreated room or a loud space. A condenser captures more detail and air, which can sound very good in a soft, quiet room, and it also captures more of the room and the noise.</p>
<h2>Which to choose</h2>
<p>If the room is hard, noisy or you record at a desk with fans, a dynamic mic is the safer choice. If the room is soft and quiet, a condenser can sound open and detailed. Test in your own space if you can.</p>
<h2>Power and cables</h2>
<p>Condensers need phantom power. USB condensers provide their own power. Dynamic mics need no power and are often easier to start with.</p>
''',
    vf_title='Clean the take from either mic',
    vf='<p>Tunedzy cleans a recording from a dynamic or a condenser mic, so you can start with the one that suits your room.</p>',
    faq=[('Which is better for a podcast?', 'It depends on the room. A dynamic mic is a common, forgiving choice for untreated rooms.'),
         ('Do condenser mics need a special cable?', 'They usually need phantom power, through an XLR connection or a USB mic that powers itself.'),
         ('Is a condenser always better?', 'No. In a noisy room, a condenser can make the room sound more obvious.')],
    related=['how-to-choose-a-microphone-for-voice-recording', 'how-to-record-with-a-usb-microphone', 'how-to-set-up-a-quiet-recording-corner-on-a-budget'])

add('what-is-a-de-esser', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='What Is a De-Esser? Plain Explanation for Voice',
    desc='A de-esser reduces harsh sibilance: the sharp s and sh sounds in a voice. What it does, its controls and how to set it without lisping.',
    h1='What Is a De-Esser?',
    kw='what is a de-esser',
    lead='A de-esser is a compressor for one band of frequencies, the sharp range where s and sh sounds sit. It turns down only the harsh sibilance and leaves the rest of the voice alone.',
    tldr=['A de-esser reduces the sibilant band, roughly 4 to 9 kHz, only when it is loud.',
          'It targets the harsh s and sh sounds, not the whole voice.',
          'Set it to act on the loudest sibilance only, so the voice keeps its clarity.',
          'Too much de-essing makes speech sound lisped or dull.'],
    body='''
<h2>The short definition</h2>
<p>A de-esser is a dynamic processor that watches a narrow band of high frequencies, where sibilance sits, and reduces it when it gets too loud. Sibilance is the hiss on s, sh, z and ch sounds. A de-esser acts on those moments, not on the whole voice.</p>
<h2>The main controls</h2>
<ul>
<li><strong>Frequency:</strong> the centre of the band it watches, often between about 4 and 9 kHz for voice.</li>
<li><strong>Threshold:</strong> the level above which it starts to reduce the band.</li>
<li><strong>Reduction:</strong> how much it lowers the band when it acts.</li>
</ul>
<h2>Setting it</h2>
<p>Play a passage with lots of s sounds. Lower the threshold until the de-esser just starts to act on the loudest s, then stop. Listen to the whole passage. If the voice sounds lisped or muffled, the reduction or the band is too strong.</p>
<h2>Related guide</h2>
<p>For a worked example, the <a href="/tunedzy/blog/how-to-de-ess-vocals">de-essing guide</a> on this site has the steps.</p>
''',
    vf_title='Soften the s, keep the words',
    vf='<p>Tunedzy&rsquo;s voice chain includes a de-esser that acts only on harsh sibilance. Use Before and After to check the words stay clear.</p>',
    faq=[('Is a de-esser the same as a high-cut filter?', 'No. A high-cut removes all the highs; a de-esser only reduces them when they are loud.'),
         ('Why does my voice lisp after de-essing?', 'The reduction is too strong or the band is too wide. Lower the reduction and listen again.'),
         ('Do I need a de-esser on every recording?', 'Only if the s sounds are harsh. Many voices need none.')],
    related=['fix-a-muffled-voice-recording', 'what-is-an-equalizer', 'what-is-a-compressor'])
