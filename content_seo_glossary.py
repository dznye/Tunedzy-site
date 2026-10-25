"""Glossary pages (25 October 2026): short, correct definitions that link to the guides and tools that use each idea.

Each page answers "what is X" in the first paragraph, explains why it matters for a voice recording, and says how to check it.
Same shape as content.GUIDES, with the same funnel links.
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


add('what-is-a-noise-gate', 'mic', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='What Is a Noise Gate? Plain Explanation for Voice Recordings',
    desc='A noise gate mutes sound when the level falls below a threshold you set. What the controls mean, when a gate helps a voice, and when it cuts words.',
    h1='What Is a Noise Gate?',
    kw='what is a noise gate',
    lead='A noise gate is a processor that mutes or lowers the sound when the level drops below a threshold you set. It makes quiet gaps silent while the louder parts pass through.',
    tldr=['A gate opens when the signal is above the threshold and closes when it falls below.',
          'Attack, hold and release control how fast it opens, how long it stays open and how fast it closes.',
          'A gate removes noise between words, not noise under the voice.',
          'Set the threshold just above the room noise and listen for clipped word starts.'],
    body='''
<h2>The short definition</h2>
<p>A noise gate is an audio processor that reduces the level of a signal whenever it falls below a threshold. Above the threshold the gate is open and the sound passes; below it the gate closes and the sound is muted or turned down. Gates exist as hardware, as plug-ins and as a setting in many recorders.</p>
<h2>The controls</h2>
<ul>
<li><strong>Threshold:</strong> the level that opens the gate. It sits just above the background noise.</li>
<li><strong>Attack:</strong> how fast the gate opens when the voice starts. Too slow and the first sound of a word is lost.</li>
<li><strong>Hold:</strong> how long the gate stays open after the signal drops, so word endings are not cut.</li>
<li><strong>Release:</strong> how fast the gate closes after the hold. A longer release sounds more natural.</li>
<li><strong>Range:</strong> how much the gate reduces the sound when closed. Full mute can sound abrupt; a small reduction sounds more natural.</li>
</ul>
<h2>Why it helps a voice recording</h2>
<p>Most voice recordings have a steady background between words, such as a fan or a hiss. A gate removes that gap noise, so the silence between phrases is quiet. It does not touch noise that sits under the voice; for that you need a <a href="/tunedzy/remove-background-noise-from-a-voice-recording">noise cleaner</a>.</p>
<h2>When it hurts</h2>
<p>A threshold set too high cuts the starts and ends of words, and quiet speakers can sound clipped. A short release makes the gate chatter on and off. Listen to the whole recording after you set a gate, not just one phrase.</p>
<h2>How to check it</h2>
<p>Play the recording through once with the gate on and once with it off. The gate is right when the gaps go quiet and no word is clipped. If you hear a flutter in the room tone, lengthen the release.</p>
''',
    vf_title='Gate the gaps, keep the words',
    vf='<p>Tunedzy cleans the background between words as part of its cleanup. Use Before and After to check that no word starts are cut.</p>',
    faq=[('Does a noise gate remove background noise?', 'Only the noise between sounds. Noise under the voice needs a noise reduction tool.'),
         ('What is the difference between a gate and a compressor?', 'A gate reduces quiet sound below a threshold. A compressor reduces loud sound above a threshold, which evens out the level.'),
         ('Why does my gated voice sound choppy?', 'The release is too short, or the threshold sits right at the level of the room noise. Lengthen the release and lower the threshold slightly.')],
    related=['remove-background-noise-from-a-voice-recording', 'how-to-remove-breath-noise-from-a-voice-recording', 'clean-up-a-phone-voice-recording'])

add('what-is-true-peak-dbtp', 'desk', ['lufs-meter', 'vocal-checker'],
    title='What Is True Peak (dBTP)? Explained Simply',
    desc='True peak (dBTP) is the loudest level a file reaches once it is converted, including the overs a sample meter misses. Why -1 dBTP is the common ceiling.',
    h1='What Is True Peak (dBTP)?',
    kw='what is true peak dBTP',
    lead='True peak, measured in dBTP, is the highest level a file reaches when it is played back as sound. It can be higher than the highest sample in the file, because the waveform can rise between samples.',
    tldr=['True peak is measured after the waveform is reconstructed between the stored samples.',
          'Conversion to MP3 or AAC can raise the peaks, so a -1 dBTP ceiling leaves room.',
          'A sample peak meter can show -0.5 dB while the true peak is above 0 dB.',
          'Check the true peak of the exported file, not only the project.'],
    body='''
<h2>The short definition</h2>
<p>True peak is the maximum level of the waveform as it is reconstructed for playback. A digital file stores samples, but the analogue wave between them can rise higher than any single sample. True peak measures that. The unit is dBTP: decibels true peak, measured against full scale.</p>
<h2>Why it matters</h2>
<p>A file can look safe on a sample peak meter and still distort when it is played or converted. Conversion to a lossy format such as MP3 or AAC adds new peaks. A file that peaks at 0 dBTP can therefore clip after encoding, which is why many people keep a margin.</p>
<h2>The common ceiling</h2>
<p>Many people set a ceiling of -1 dBTP. That keeps about 1 dB of headroom for the peaks that conversion adds. The <a href="/tunedzy/how-to-export-audio-for-spotify-and-apple-podcasts">export guide</a> explains how to apply it before you upload.</p>
<h2>How to check it</h2>
<p>Use a meter that shows true peak, or a tool that reports dBTP for the whole file. Measure the exported file, because the project and the export can differ. If the true peak is too high, lower the level or use a true-peak limiter at -1 dBTP.</p>
<h2>True peak and loudness are different</h2>
<p>True peak measures the single highest moment. Loudness, measured in LUFS, measures the average level over time. A file can have a safe peak and still be too loud or too quiet on average. Both matter.</p>
''',
    vf_title='Check the peak on the exported file',
    vf='<p>The free LUFS meter on this site measures loudness and true peak in your browser. Tunedzy exports at a target with the true peak checked.</p>',
    faq=[('Is -1 dBTP a legal rule?', 'It is a common practice, not a law. Check the platform&rsquo;s guidance for its own limit.'),
         ('Why is my MP3 clipping when the WAV did not?', 'Conversion added peaks above the WAV level. Lower the true peak of the WAV to about -1 dBTP and export again.'),
         ('Does a limiter fix true-peak overs?', 'Yes, a true-peak limiter set to -1 dBTP keeps the peaks under the ceiling, at the cost of some squashing if pushed.')],
    related=['how-to-export-audio-for-spotify-and-apple-podcasts', 'how-to-make-audio-louder-without-distortion', 'loudness-for-youtube-podcasts-and-spotify'])

add('what-is-lufs', 'mic-wide', ['lufs-meter', 'vocal-checker'],
    title='What Is LUFS? Loudness Explained for Creators',
    desc='LUFS is the loudness people actually hear, averaged over a file. What the number means, how it differs from peak, and how to measure it.',
    h1='What Is LUFS?',
    kw='what is LUFS',
    lead='LUFS stands for loudness units relative to full scale. It is a single number for how loud a file sounds over its whole length, weighted to match human hearing.',
    tldr=['LUFS is an average loudness over the length of the file, not a single peak.',
          'Two files with the same LUFS feel about equally loud, even if their peaks differ.',
          'Platforms and podcast hosts use LUFS targets to set their playback level.',
          'Measure the whole file to get an honest number.'],
    body='''
<h2>The short definition</h2>
<p>LUFS (loudness units relative to full scale) is a measure of perceived loudness. It averages the level of a file over time and weights the frequencies the way human hearing does, so bass counts less than it would on a simple meter. The unit is written LUFS, and a value is often shown with the time frame used.</p>
<h2>How it differs from peak</h2>
<p>A peak meter shows the single loudest moment. LUFS shows the average. A quiet voice with one loud cough has a low LUFS and a high peak. Loudness targets are set in LUFS because they describe how a file feels, not how it spikes.</p>
<h2>Why platforms use it</h2>
<p>Many streaming services and podcast hosts measure LUFS and adjust playback so different files sound about equally loud. A file much louder than the target can be turned down, and a very quiet file may be turned up with more noise. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> lists the targets people use.</p>
<h2>How to measure it</h2>
<p>Use a LUFS meter on the whole file. Short-term or momentary readings change every moment, so use the integrated value for the file. The <a href="/tunedzy/tools/lufs-meter">free LUFS meter</a> on this site measures a file in your browser, and nothing is uploaded.</p>
<h2>What to do with it</h2>
<p>Set the file to the target you need, then check its true peak. Raising the level to a higher LUFS without checking the peak can cause distortion, and pushing it with a limiter squashes the voice.</p>
''',
    vf_title='Measure it in your browser',
    vf='<p>The free LUFS meter measures a file in your browser. Tunedzy sets a voice to a loudness target and checks the true peak.</p>',
    faq=[('Is a higher LUFS always better?', 'No. A higher number usually means more compression. The right target is the one for where the file is going.'),
         ('Is LUFS the same as RMS?', 'No. RMS is a simple average of power. LUFS is weighted to how people hear, so it matches perceived loudness better.'),
         ('What LUFS should a podcast be?', 'Many podcast guides use around -16 LUFS for stereo, but check your host and platform rules.')],
    related=['loudness-for-youtube-podcasts-and-spotify', 'what-is-true-peak-dbtp', 'how-to-export-audio-for-spotify-and-apple-podcasts'])

add('what-is-a-high-pass-filter', 'desk-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='What Is a High-Pass Filter? Plain Explanation',
    desc='A high-pass filter lets high frequencies through and cuts the low ones. Where to set it for a voice, what it removes and how to tell it is too strong.',
    h1='What Is a High-Pass Filter?',
    kw='what is a high pass filter',
    lead='A high-pass filter lets the high frequencies pass and reduces everything below a chosen cut-off. For voice recordings it is the first tool to remove rumble, handling noise and low hum.',
    tldr=['A high-pass filter reduces the low frequencies below a cut-off you set.',
          'For a voice, a cut-off around 80 to 120 Hz removes rumble with little harm.',
          'Set it too high and the voice sounds thin.',
          'It is usually the first step in cleaning a voice recording.'],
    body='''
<h2>The short definition</h2>
<p>A high-pass filter passes the frequencies above a cut-off and reduces those below it. The steepness of the cut, called the slope, decides how sharply the low end is removed. The filter is also called a low cut, and it is one of the most common tools in voice work.</p>
<h2>What it removes</h2>
<p>Most voice recordings carry low noise that speech does not need: rumble from a desk or a floor, handling noise, air movement and some mains hum. A high-pass filter removes these with little effect on speech, which lives mostly above 100 Hz.</p>
<h2>Where to set it</h2>
<p>A starting point for a voice is around 80 to 120 Hz. Move the cut-off up slowly until the rumble disappears, then move it back a little. Going much higher than about 150 Hz starts to thin the voice, because the chest warmth of the voice sits lower.</p>
<h2>Check it</h2>
<p>Listen with the filter on and off. The change should be in the rumble, not in the sound of the voice. If the voice sounds weaker, the cut-off is too high. For the rumble itself, see the <a href="/tunedzy/how-to-remove-wind-noise-from-audio">wind noise guide</a>.</p>
''',
    vf_title='Cut the rumble first',
    vf='<p>Tunedzy&rsquo;s cleanup applies a low cut as part of the voice repair. Use Before and After to check that the voice stays full.</p>',
    faq=[('What is the difference between a high-pass and a low-cut filter?', 'They are the same thing. Both names describe a filter that removes the low frequencies.'),
         ('Where should I set a high-pass for a male voice?', 'The same range works for most voices. Check by ear, because deeper voices need a lower cut.'),
         ('Does a high-pass filter remove hum?', 'Only the part of the hum below the cut-off. Mains hum at 50 or 60 Hz needs a notch filter.')],
    related=['remove-hum-from-audio', 'how-to-make-a-voice-sound-warmer', 'how-to-remove-wind-noise-from-audio'])

add('what-is-an-equalizer', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='What Is an Equalizer (EQ)? Plain Explanation for Voice',
    desc='An equalizer boosts or cuts parts of the frequency range. What EQ does to a voice, the main bands, and how to use it without making the voice harsh.',
    h1='What Is an Equalizer (EQ)?',
    kw='what is an equalizer EQ',
    lead='An equalizer, or EQ, changes the balance of frequencies in a sound. It can boost or cut a band, so a voice can be made warmer, clearer or less harsh.',
    tldr=['EQ boosts or cuts bands of frequency: low, low mid, presence and high.',
          'Cut what you do not like before you boost what you do like.',
          'Make small changes, 1 to 3 dB, and listen at normal volume.',
          'EQ shapes a sound; it cannot add detail that was never recorded.'],
    body='''
<h2>The short definition</h2>
<p>An equaliser changes the level of part of the frequency range. A band can be boosted to add emphasis or cut to reduce it. The bands are often named low, low mid, mid, presence and high, and most equalisers can set the centre frequency, the width of the band and the amount.</p>
<h2>What each part does to a voice</h2>
<ul>
<li><strong>Low (below about 150 Hz):</strong> body and rumble. Cut the rumble, boost gently for warmth.</li>
<li><strong>Low mid (about 150 to 500 Hz):</strong> fullness, and sometimes muddiness.</li>
<li><strong>Presence (about 2 to 5 kHz):</strong> clarity and the words. A small lift helps a muffled voice.</li>
<li><strong>High (above about 8 kHz):</strong> air and sheen, and also sibilance.</li>
</ul>
<h2>Use it gently</h2>
<p>Cut before you boost. A small cut in a problem area often does more than a large boost elsewhere. Change one band at a time and listen at normal volume, because a boost that sounds bright quietly can sound harsh when louder.</p>
<h2>What EQ cannot do</h2>
<p>EQ changes what is there. It cannot restore frequencies the microphone never captured. A very dull recording needs a better take, not a bigger boost. For a muffled voice, see the <a href="/tunedzy/fix-a-muffled-voice-recording">muffled voice guide</a>.</p>
''',
    vf_title='Shape the voice without the harshness',
    vf='<p>Tunedzy&rsquo;s tone step shapes a voice toward a clear, even sound. Use Before and After to check the result.</p>',
    faq=[('Should I boost or cut first?', 'Cut first. Removing a problem is usually cleaner than adding a boost to hide it.'),
         ('How much EQ is too much?', 'If the voice sounds unnatural, or the change is loud when you compare it, it is too much. Small moves are usually enough.'),
         ('Is a graphic EQ or a parametric EQ better?', 'A parametric EQ lets you set each band precisely, which suits voice work. A graphic EQ is simpler for quick moves.')],
    related=['fix-a-muffled-voice-recording', 'how-to-make-a-voice-sound-warmer', 'what-is-a-high-pass-filter'])
