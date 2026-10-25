"""Batch 6c (25 October 2026): fifteen glossary pages and eight audience pages.

Glossary pages give one plain definition first, why it matters for a voice or a mix, and how to check it. Audience pages describe a
specific use with practical steps. GROUP_OF marks 'glossary' or 'audience' for the guides hub.
"""

PHOTO = {}
TOOLS = {}
GUIDES = {}
ORDER = []
GROUP_OF = {}


def add(slug, group, photo, tools, **g):
    GUIDES[slug] = g
    PHOTO[slug] = photo
    TOOLS[slug] = tools
    ORDER.append(slug)
    GROUP_OF[slug] = group


# ----------------------------------------------------------------------------------- glossary
add('what-is-stem-separation', 'glossary', 'neon', ['song-key-finder', 'vocal-checker'],
    title='What Is Stem Separation? Plain Explanation',
    desc='Stem separation splits a finished song into parts such as vocals, drums and bass. What it means, how it works and what it can and cannot do.',
    h1='What Is Stem Separation?',
    kw='what is stem separation',
    lead='Stem separation splits a finished mix into its parts, called stems: usually vocals and instruments, or drums, bass and other parts too. It uses a model trained to recognise each part.',
    tldr=['A stem is one part of a finished mix, such as the vocal or the drums.',
          'A model learns to recognise each part and separate it from the mix.',
          'Separation is never perfect: expect some bleed between stems.',
          'Use separated stems only with music you have the right to use.'],
    body='''
<h2>The short definition</h2>
<p>A stem is one part of a mix, and stem separation pulls those parts apart from a finished song. The common split is a vocal and an instrumental, but many tools also separate drums and bass.</p>
<h2>How it works</h2>
<p>A model trained on many songs learns what a voice sounds like and what drums and bass sound like, then estimates each part in the mix. Dense mixes with many instruments in the same range are harder to split.</p>
<h2>What to expect</h2>
<p>Some bleed is normal: a little drum in the vocal, a little voice in the instrumental. Artifacts show on cymbals and reverb. Listen critically before you use a stem.</p>
<h2>Where it is used</h2>
<p>Karaoke tracks, practice, remixing and cleaning a vocal. The <a href="/tunedzy/tunedzy-vocal-remover">Tunedzy vocal remover</a> is one tool that does it on your PC.</p>
''',
    vf_title='Split a song on your PC',
    vf='<p>Tunedzy separates a vocal from a song on your PC. Use it with music you have the right to use.</p>',
    faq=[('Is a stem the same as a track?', 'A stem is a part of a finished mix. A track is one part of a project.'),
         ('Does separation keep full quality?', 'Separated parts are never identical to the original. Listen for artifacts.'),
         ('Is stem separation legal?', 'It depends on the rights to the music and how you use the parts.')],
    related=['best-ai-stem-splitter', 'how-to-isolate-a-voice-from-background-music', 'how-to-export-stems-for-a-daw'])

add('what-is-spectral-editing', 'glossary', 'desk', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='What Is Spectral Editing? Plain Explanation',
    desc='Spectral editing shows audio as a picture of frequency over time, so you can select and repair a sound you can see. What it is and when it helps.',
    h1='What Is Spectral Editing?',
    kw='what is spectral editing',
    lead='Spectral editing shows a recording as a picture: frequency up the side, time across, and brightness for loudness. You select a sound you can see, such as a click or a hum, and repair just that part.',
    tldr=['A spectrogram shows frequency over time, with loudness as brightness.',
          'You select a sound on the picture and repair only that part.',
          'Good for clicks, hum lines, coughs and noises that stand out visually.',
          'Overuse leaves artifacts, so repair in small steps.'],
    body='''
<h2>The short definition</h2>
<p>Spectral editing is editing audio on a spectrogram, a picture of the sound. Time runs across the screen, frequency runs up, and the brightness shows how loud each part is. Sounds that stand out, such as a hum line or a cough, are easy to see.</p>
<h2>What it is good for</h2>
<p>Removing a sound that sits in a narrow band, such as a hum, a whistle or a cough, without touching the voice around it. It is precise, which is why professional repair tools use it.</p>
<h2>Limits</h2>
<p>Repair in small, careful steps. A large spectral repair leaves a dull patch or a watery sound. Compare the result with the original.</p>
<h2>In Tunedzy</h2>
<p>Quick edit has a spectral repair box: select a region on the spectrogram and it is repaired from the sound around it. The <a href="/tunedzy/free-alternative-to-izotope-rx">repair comparison</a> covers how it compares with professional tools.</p>
''',
    vf_title='Repair what you can see',
    vf='<p>Tunedzy Quick edit has a spectral repair box, so you can select a sound on the spectrogram and repair it.</p>',
    faq=[('Is spectral editing hard?', 'It takes practice. Start with one clear sound, such as a hum line.'),
         ('Can it remove a cough?', 'Often, if the cough is distinct on the picture. Repair in small steps.'),
         ('Does it need a special display?', 'No. A spectrogram view is enough.')],
    related=['tunedzy-repair', 'remove-hum-from-audio', 'free-alternative-to-izotope-rx'])

add('what-is-bitrate', 'glossary', 'booth', ['lufs-meter', 'vocal-checker'],
    title='What Is Bitrate? Plain Explanation for Audio Files',
    desc='Bitrate is how much data an audio file uses per second. What bitrate means for MP3 quality, how to choose one for speech and why it matters for size.',
    h1='What Is Bitrate?',
    kw='what is bitrate audio',
    lead='Bitrate is the amount of data an audio file uses each second, measured in kilobits per second. For a compressed file such as MP3, a higher bitrate keeps more of the original sound and makes the file larger.',
    tldr=['Bitrate is data per second, in kbps.',
          'A higher bitrate keeps more detail in a compressed file.',
          'For speech, a moderate high bitrate sounds very close to the original.',
          'Bitrate does not apply to uncompressed WAV, which has its own fixed size.'],
    body='''
<h2>The short definition</h2>
<p>Bitrate is how many kilobits of data are used for each second of sound. It is a property of compressed formats such as MP3 and AAC. The compression chooses which detail to keep at that rate.</p>
<h2>What it means in practice</h2>
<p>A low bitrate sounds thin or artifacted, especially on sibilance and breath. A high bitrate keeps the sound close to the original. For speech, the difference between a high bitrate and the original is hard to hear for most people.</p>
<h2>Choosing one</h2>
<p>Use the highest bitrate the platform accepts for your final MP3, and keep a WAV master. Check the platform guidance first.</p>
<h2>Bitrate and WAV</h2>
<p>WAV is uncompressed, so it has no bitrate choice; its size depends on the sample rate and bit depth. The <a href="/tunedzy/how-to-choose-wav-mp3-or-flac">format guide</a> explains the trade-off.</p>
''',
    vf_title='Export at a sensible bitrate',
    vf='<p>Tunedzy exports MP3 from its master at a bitrate you choose, and checks the peak before export.</p>',
    faq=[('What bitrate is good for speech?', 'A high bitrate is safe. Check the platform recommendation.'),
         ('Does a higher bitrate always sound better?', 'Up to the point where the original is preserved, yes. Beyond that, the gain is small.'),
         ('Is WAV a bitrate format?', 'WAV is uncompressed, so it does not have a bitrate choice.')],
    related=['my-mp3-sounds-worse-than-my-wav', 'how-to-choose-wav-mp3-or-flac', 'what-is-bit-depth'])

add('what-is-lossless-audio', 'glossary', 'mic', ['lufs-meter', 'vocal-checker'],
    title='What Is Lossless Audio? Plain Explanation',
    desc='Lossless audio keeps every bit of the original sound, even when the file is compressed. What lossless means, which formats are lossless and why to keep one as a master.',
    h1='What Is Lossless Audio?',
    kw='what is lossless audio',
    lead='Lossless audio keeps every part of the original sound. A lossless file can be smaller than WAV when compressed, such as FLAC, and it decodes back to exactly the same sound.',
    tldr=['Lossless means the decoded sound matches the original exactly.',
          'WAV is uncompressed and lossless; FLAC is compressed and lossless.',
          'MP3 is lossy: it removes detail to save space.',
          'Keep a lossless master for editing and re-exporting.'],
    body='''
<h2>The short definition</h2>
<p>Lossless audio is stored so that the decoded result is identical to the original. Compression can make a lossless file smaller, but nothing is thrown away. WAV and FLAC are the common lossless formats.</p>
<h2>Lossless and lossy</h2>
<p>A lossy format such as MP3 throws away detail the ear is supposed to miss. Each conversion from a lossy file adds loss. That is why editors keep a lossless master.</p>
<h2>What to keep</h2>
<p>Keep the WAV or FLAC master. Export a lossy copy only for sharing, from the master, at a high bitrate.</p>
<h2>In Tunedzy</h2>
<p>The master is kept in a high-precision form for editing, and exports to WAV, FLAC or MP3 come from it. The <a href="/tunedzy/how-to-choose-wav-mp3-or-flac">format guide</a> explains each choice.</p>
''',
    vf_title='Keep the master lossless',
    vf='<p>Tunedzy keeps a high-precision master and exports WAV, FLAC or MP3 from it, so you never edit a lossy copy.</p>',
    faq=[('Is FLAC lossless?', 'Yes. It is compressed and lossless.'),
         ('Is WAV lossless?', 'Yes. It is uncompressed and lossless.'),
         ('Can I hear the difference between lossless and high-bitrate MP3?', 'For speech, most listeners cannot. Check on your own equipment.')],
    related=['what-is-bitrate', 'how-to-choose-wav-mp3-or-flac', 'what-is-bit-depth'])

add('what-is-an-audio-codec', 'glossary', 'booth-wide', ['vocal-checker', 'lufs-meter'],
    title='What Is an Audio Codec? Plain Explanation',
    desc='An audio codec encodes and decodes sound, either lossless or lossy. What a codec is, the common ones (AAC, MP3, FLAC, Opus) and why it matters for uploads.',
    h1='What Is an Audio Codec?',
    kw='what is an audio codec',
    lead='A codec is the method that encodes sound into a file and decodes it back to play. Each codec trades size against quality in its own way, and the container holds the codec and the data.',
    tldr=['A codec encodes and decodes the sound.',
          'A container, such as MP4 or MP3, holds the codec and the data.',
          'Common codecs include AAC, MP3, FLAC and Opus.',
          'Players and platforms need to support the codec you export.'],
    body='''
<h2>The short definition</h2>
<p>An audio codec is a method for encoding sound into data and decoding it for playback. A codec may be lossy, like MP3 or AAC, or lossless, like FLAC.</p>
<h2>Codec and container</h2>
<p>The file you see, such as MP4 or MP3, is a container. It holds one or more streams, each with a codec. An MP4 video often carries AAC audio.</p>
<h2>Why it matters</h2>
<p>A platform may accept some codecs and not others. Check the upload requirements. Export a common codec at a high quality, and keep a lossless master.</p>
<h2>In Tunedzy</h2>
<p>Exports are WAV, FLAC or MP3 from the master. For a video, the picture is copied and the sound replaced, so the video codec stays as it was.</p>
''',
    vf_title='Export a codec the platform accepts',
    vf='<p>Tunedzy exports common formats from its master, and copies the picture when it replaces a video soundtrack.</p>',
    faq=[('What is the most common audio codec?', 'AAC and MP3 are widespread. Check the platform.'),
         ('Is a codec the same as a format?', 'Not quite. A format is the file type; a codec is the method inside it.'),
         ('Does changing codec lose quality?', 'A lossy codec does. Convert from a lossless master.')],
    related=['what-is-bitrate', 'what-is-lossless-audio', 'how-to-choose-wav-mp3-or-flac'])

add('what-is-dither', 'glossary', 'booth', ['lufs-meter', 'vocal-checker'],
    title='What Is Dither? Plain Explanation for Bit Depth',
    desc='Dither adds a tiny, controlled noise when you reduce bit depth, so the quiet detail stays smooth. What dither is, when to use it and when not to.',
    h1='What Is Dither?',
    kw='what is dither audio',
    lead='Dither is a very small amount of noise added when you reduce the bit depth of a recording, such as from 24 to 16 bit. It hides the rounding error, which otherwise can sound like distortion in quiet passages.',
    tldr=['Dither is added when reducing bit depth, for example to 16 bit.',
          'It replaces harsh rounding distortion with a smooth, very quiet noise.',
          'Apply it once, at the last step of export.',
          'Do not dither a file more than once, and do not dither while editing.'],
    body='''
<h2>The short definition</h2>
<p>When a recording is reduced from a higher bit depth to a lower one, the values are rounded. In very quiet passages the rounding can sound like a harsh distortion. Dither adds a tiny noise that breaks up that pattern.</p>
<h2>When it matters</h2>
<p>Reducing a master to 16 bit for a CD or a format that needs it. For a voice recording with a noisy floor, dither is mostly hidden, but it is still the correct step.</p>
<h2>When not to use it</h2>
<p>Do not dither while you edit, because each dither adds noise. Apply it once, as the last step of the export.</p>
<h2>In Tunedzy</h2>
<p>Exports to 16-bit formats can use dither at the export step. Check the export setting for your version.</p>
''',
    vf_title='Dither once, at the end',
    vf='<p>Tunedzy exports from a high-precision master. Apply dither only at the final bit-depth reduction.</p>',
    faq=[('Does dither add audible noise?', 'A very small amount, and it is designed to be hidden. It is safer than rounding distortion.'),
         ('Should I dither a 24-bit master?', 'Only when reducing bit depth. Keep the master at 24 bit.'),
         ('Is dither the same as noise reduction?', 'No. Dither adds a controlled tiny noise; noise reduction removes noise.')],
    related=['what-is-bit-depth', 'how-to-choose-wav-mp3-or-flac', 'what-is-headroom'])

add('what-is-crossfade', 'glossary', 'desk-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='What Is a Crossfade? Plain Explanation',
    desc='A crossfade blends the end of one sound into the start of the next, so the join cannot be heard. What a crossfade is, its length and where it is used.',
    h1='What Is a Crossfade?',
    kw='what is a crossfade',
    lead='A crossfade blends one sound out while another blends in over a short overlap. It is used to join two pieces of audio, or two clips, so the change is smooth.',
    tldr=['A crossfade overlaps the end of one clip with the start of the next.',
          'One fades out while the other fades in.',
          'The length depends on the material: short for speech, longer for music.',
          'Match the room tone on both sides, so the join stays hidden.'],
    body='''
<h2>The short definition</h2>
<p>In a crossfade, one sound gets quieter at the same time as another gets louder. The overlap makes the join smooth, rather than a click or a sudden change in the background.</p>
<h2>Where it is used</h2>
<p>Joining two recordings, joining two clips in an edit, and moving from one piece of music to another. For speech, a short crossfade keeps the words clear.</p>
<h2>How to check it</h2>
<p>Play the join several times at normal volume. A click, a dip or a change in the room means the fade needs changing.</p>
<p>The <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade how-to</a> has the steps.</p>
''',
    vf_title='Join without a seam',
    vf='<p>Tunedzy Multitrack lets you overlap clips with fades and check the join by ear.</p>',
    faq=[('How long should a crossfade be?', 'Short for speech. Listen to the join rather than measure it.'),
         ('Is a crossfade the same as a fade?', 'A fade changes one sound on its own. A crossfade joins two sounds.'),
         ('Why does my join still click?', 'The overlap is too short, or the room tone differs. Adjust both.')],
    related=['how-to-crossfade-two-recordings', 'how-to-add-fades-to-a-recording', 'how-to-trim-silence-from-a-recording'])

add('what-is-normalisation', 'glossary', 'mic-wide', ['lufs-meter', 'vocal-checker'],
    title='What Is Normalisation in Audio? Plain Explanation',
    desc='Normalisation sets a file so its loudest peak reaches a chosen level, or its average loudness reaches a target. Peak and loudness normalisation compared.',
    h1='What Is Normalisation?',
    kw='what is normalisation audio',
    lead='Normalisation changes the level of a whole file by one amount. Peak normalisation sets the loudest peak to a level. Loudness normalisation sets the average loudness to a target, which is closer to how loud a file feels.',
    tldr=['Normalising changes the whole file by a single amount.',
          'Peak normalisation sets the highest peak, and does not measure loudness.',
          'Loudness normalisation matches a target, measured in LUFS.',
          'Use loudness for the final level, and peak only as a safety check.'],
    body='''
<h2>The short definition</h2>
<p>Normalising raises or lowers a file by one amount so that a chosen measure reaches a target. The shape of the sound is unchanged; only the level moves.</p>
<h2>Peak and loudness</h2>
<p>Peak normalisation looks at the highest sample. Loudness normalisation looks at the average over time. Two files normalised to the same peak can feel very different in loudness.</p>
<h2>Which to use</h2>
<p>For a final level, loudness. For a check that nothing will clip, the true peak. The <a href="/tunedzy/how-to-normalize-audio-the-right-way">normalising how-to</a> has the steps.</p>
''',
    vf_title='Normalise to loudness, check the peak',
    vf='<p>Tunedzy matches a file to a loudness target and checks the true peak before export.</p>',
    faq=[('Does normalising improve the sound?', 'No. It changes the level only.'),
         ('Is peak normalising wrong?', 'Not wrong, but it does not measure how loud a file feels.'),
         ('Should I normalise before cleanup?', 'After. Clean first, then set the level.')],
    related=['how-to-normalize-audio-the-right-way', 'what-is-lufs', 'what-is-true-peak-dbtp'])

add('what-is-rms', 'glossary', 'booth-wide', ['lufs-meter', 'vocal-checker'],
    title='What Is RMS Level? Plain Explanation',
    desc='RMS is the average power of a sound over a short window, a simple measure of how loud a signal feels. How it differs from peak and LUFS.',
    h1='What Is RMS Level?',
    kw='what is rms level audio',
    lead='RMS, or root mean square, is the average level of a signal over a short time. It is a simple measure of how loud a sound feels, and it sits between the peak and the LUFS measure.',
    tldr=['RMS is an average level over a short window.',
          'Peak is the single highest sample; RMS is the average.',
          'LUFS weights the average to how people hear, which RMS does not.',
          'RMS is useful for a quick comparison of two clips.'],
    body='''
<h2>The short definition</h2>
<p>RMS measures the average power of a signal. It rises when the sound is steadily loud, and falls in quiet passages, so it is a fair guide to how loud a sound feels.</p>
<h2>RMS, peak and LUFS</h2>
<p>A peak meter shows the loudest moment. RMS shows the average. LUFS is a loudness measure that weights frequencies the way the ear does, so it matches perceived loudness better than RMS.</p>
<h2>When to use it</h2>
<p>For a quick check of two voice clips, RMS is simple and useful. For a final loudness target on a platform, use LUFS. The <a href="/tunedzy/what-is-lufs">LUFS explanation</a> covers the difference.</p>
''',
    vf_title='Measure loudness, not just peaks',
    vf='<p>The free LUFS meter on this site measures loudness; Tunedzy sets a voice to a target and checks the peak.</p>',
    faq=[('Is RMS the same as LUFS?', 'No. LUFS weights the average to how people hear.'),
         ('Why does my peak meter show a low number but the file sounds loud?', 'The average is high while the peaks are moderate. That is what RMS and LUFS measure.'),
         ('Which should I aim for?', 'For a platform target, LUFS.')],
    related=['what-is-lufs', 'what-is-true-peak-dbtp', 'what-is-dynamic-range'])

add('what-is-sibilance', 'glossary', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='What Is Sibilance? Plain Explanation for Voice',
    desc='Sibilance is the sharp hiss on s, sh, z and ch sounds in speech. Why it becomes harsh in a recording and how to tame it with a de-esser or EQ.',
    h1='What Is Sibilance?',
    kw='what is sibilance',
    lead='Sibilance is the sharp hiss on s, sh, z and ch sounds. It sits high in the frequency range, and a close mic or a bright voice can make it harsh.',
    tldr=['Sibilance is the hiss of s, sh, z and ch sounds.',
          'It sits roughly between 4 and 9 kHz.',
          'A close mic, a bright voice or compression can make it harsh.',
          'Tame it with a de-esser or a narrow cut, not by removing the highs.'],
    body='''
<h2>The short definition</h2>
<p>Sibilance is the sharp, hissing energy in consonants such as s, sh, z and ch. It is part of speech and needs to stay clear, but too much makes a voice harsh.</p>
<h2>Causes</h2>
<p>A close mic, a bright voice, a sensitive condenser mic and compression can all make sibilance stand out. Some people produce more of it than others.</p>
<h2>Fixes</h2>
<p>A de-esser reduces the sibilant band only when it is loud. A narrow cut can help if the problem sits in one place. The <a href="/tunedzy/what-is-a-de-esser">de-esser explanation</a> and the <a href="/tunedzy/blog/how-to-de-ess-vocals">de-essing guide</a> cover the setting.</p>
''',
    vf_title='Soften the s, keep the words',
    vf='<p>Tunedzy&rsquo;s voice chain includes a de-esser that acts only on harsh sibilance.</p>',
    faq=[('Is sibilance a fault?', 'No, it is part of speech. Only too much is a problem.'),
         ('Should I remove all sibilance?', 'No. Remove the harsh peaks, and keep the clarity.'),
         ('Why is my voice sibilant on phones?', 'Phone speakers can exaggerate the high range. Check on a phone speaker.')],
    related=['what-is-a-de-esser', 'my-voice-sounds-too-bright', 'what-is-an-equalizer'])

add('what-is-a-plosive', 'glossary', 'neon', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='What Is a Plosive? Plain Explanation for Mic Pops',
    desc='A plosive is a consonant such as p, b, t or d that releases a puff of air, which can make a mic pop. What a plosive is and how to prevent it.',
    h1='What Is a Plosive?',
    kw='what is a plosive',
    lead='A plosive is a speech sound, such as p, b, t or d, that releases a short burst of air. Close to a mic, the burst can hit the capsule and make a pop.',
    tldr=['A plosive is a consonant that releases a burst of air.',
          'Close to a mic, the burst makes a thump called a pop.',
          'A pop filter and a slight off-axis position prevent most pops.',
          'A low cut reduces the thump in a file, but prevention is better.'],
    body='''
<h2>The short definition</h2>
<p>A plosive is a consonant made by stopping and releasing the air, such as p, b, t, d, k and g. The release is a short puff of air.</p>
<h2>Why it pops</h2>
<p>A mic close to the mouth catches the puff. The capsule moves, and the recording records a low thump. Plosives on p and b are the usual culprits.</p>
<h2>Prevention and fixes</h2>
<p>A pop filter, a little distance and speaking slightly to the side prevent most pops. In a file, a high-pass filter reduces the thump. The <a href="/tunedzy/what-is-a-pop-filter">pop filter explanation</a> covers placement.</p>
''',
    vf_title='Prevent the pop, then clean',
    vf='<p>Tunedzy&rsquo;s cleanup includes a pop guard. Prevent pops at the mic first.</p>',
    faq=[('What is the difference between a plosive and a pop?', 'The plosive is the speech sound; the pop is the thump it can make in a mic.'),
         ('Do all mics pop?', 'Any close mic can pop. Directional mics are more sensitive to the burst.'),
         ('Can I remove a plosive completely?', 'Often most of it. Prevention is the reliable fix.')],
    related=['what-is-a-pop-filter', 'my-recording-has-a-pop-on-every-p', 'clean-up-a-phone-voice-recording'])

add('what-is-reverb-vs-echo', 'glossary', 'booth-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='Reverb vs Echo: What Is the Difference?',
    desc='Reverb and echo are both reflections of sound, but echo is a distinct repeat and reverb is a dense wash. The difference, why it matters in recording and how to reduce each.',
    h1='Reverb vs Echo',
    kw='reverb vs echo difference',
    lead='Echo is a distinct repeat of a sound after a short delay. Reverb is a dense wash of reflections that blends into a room. Both come from sound bouncing off hard surfaces, and each is treated differently.',
    tldr=['Echo is a clear repeat after a delay you can hear.',
          'Reverb is a dense, smooth wash of reflections in a room.',
          'Soft furnishings reduce both at the source.',
          'Cleanup can reduce reverb and some echo, but not remove them all.'],
    body='''
<h2>Echo</h2>
<p>Echo is a single or a few repeats of a sound, separated by a delay you can hear. A large hall with a hard wall far away gives echo.</p>
<h2>Reverb</h2>
<p>Reverb is the dense mass of reflections that follows a sound in a room. It is smooth and continuous, and it makes a voice sound far away or hollow.</p>
<h2>Fixing each</h2>
<p>Soft furnishings reduce both at the source. In a file, a de-reverb tool reduces reverb, and an echo can sometimes be reduced with careful editing. The <a href="/tunedzy/remove-echo-from-vocal-recording">echo guide</a> covers the steps.</p>
''',
    vf_title='Soften the room first',
    vf='<p>A soft room reduces both echo and reverb at the source. Tunedzy can reduce some of what remains.</p>',
    faq=[('Is reverb always bad?', 'Not for music. For speech, too much makes a voice distant.'),
         ('Why does my voice echo on a call?', 'A hard room and speakers. Use headphones and a soft room.'),
         ('Can AI remove reverb?', 'It can reduce it. Removing all of it can change the voice.')],
    related=['remove-echo-from-vocal-recording', 'how-to-make-a-voice-sound-close-and-intimate', 'how-to-set-up-a-quiet-recording-corner-on-a-budget']
)

add('what-is-mono-vs-stereo', 'glossary', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='Mono vs Stereo: Which to Use for Voice',
    desc='Mono has one channel and stereo has two. Why a single voice is usually better in mono, when stereo helps and how converting to mono affects file size.',
    h1='Mono vs Stereo',
    kw='mono vs stereo for voice',
    lead='Mono has one channel; stereo has two, left and right. A single voice does not need two channels, so mono is usually the better choice for speech. Stereo suits music and effects that move across the sound field.',
    tldr=['Mono has one channel; stereo has a left and right channel.',
          'A single voice recorded in mono sounds the same and is half the size.',
          'Stereo suits music, ambience and effects that move across the sound.',
          'Check that a stereo recording is balanced before you convert to mono.'],
    body='''
<h2>The short definition</h2>
<p>Mono is one channel of sound, played from both speakers equally. Stereo has two channels, left and right, which can carry different sound.</p>
<h2>For voice</h2>
<p>A voice recorded in mono is the same voice, and the file is half the size of stereo. Most podcasts and voiceovers are mono. A stereo recording of one voice often has the same sound in both channels anyway.</p>
<h2>For music</h2>
<p>Stereo gives width and movement, which music and effects use. Keep stereo for a mix that needs it.</p>
<h2>Converting</h2>
<p>Check that the two channels are balanced and not out of phase before you convert. A cancelling channel can thin the sound when it is summed to mono.</p>
''',
    vf_title='Mono for voice, stereo for music',
    vf='<p>Tunedzy works on mono voice files and stereo mixes, and exports the format you choose.</p>',
    faq=[('Should a podcast be mono?', 'Most are. Mono suits a single voice and keeps files small.'),
         ('Does mono sound worse?', 'For a single voice, no. For music with stereo effects, yes.'),
         ('Why does my stereo file sound thin in mono?', 'The channels may be out of phase. Check the balance.')],
    related=['my-audio-file-is-too-big', 'what-is-phantom-power', 'how-to-choose-wav-mp3-or-flac'])

add('what-is-a-daw', 'glossary', 'mic-wide', ['song-key-finder', 'bpm-finder'],
    title='What Is a DAW? Plain Explanation',
    desc='A DAW, or digital audio workstation, is the software used to record, edit, arrange and mix audio. The common DAWs and what Tunedzy does next to them.',
    h1='What Is a DAW?',
    kw='what is a daw',
    lead='A DAW, short for digital audio workstation, is the software used to record, edit, arrange and mix audio. Logic Pro, Ableton Live, FL Studio, Reaper and GarageBand are DAWs. Tunedzy is not a DAW; it finishes voices.',
    tldr=['A DAW records, edits, arranges and mixes audio.',
          'Logic Pro, Ableton Live, FL Studio, Reaper and GarageBand are DAWs.',
          'Plugins add effects and instruments inside a DAW.',
          'Tunedzy finishes voice recordings alongside a DAW; it is not one.'],
    body='''
<h2>The short definition</h2>
<p>A digital audio workstation is an application for recording, editing, arranging and mixing sound. It has tracks, a timeline, effects and often instruments.</p>
<h2>Common DAWs</h2>
<p>Logic Pro and GarageBand on Apple devices, Ableton Live, FL Studio, Reaper and others. They differ in workflow and in what they are best at, such as beats or live performance.</p>
<h2>Where Tunedzy fits</h2>
<p>Tunedzy is not a DAW. It cleans, repairs, edits by transcript and mixes voices with music, and exports at a loudness target. Many people finish the voice in Tunedzy and mix the song in a DAW. The <a href="/tunedzy/best-daw-for-vocal-recording">DAW roundup</a> compares the options.</p>
''',
    vf_title='Finish the voice next to your DAW',
    vf='<p>Export the vocal from your DAW, clean and level it in Tunedzy, and bring it back for the mix.</p>',
    faq=[('Do I need a DAW?', 'For making and mixing music, yes. For a podcast or a voiceover, a finishing tool may be enough.'),
         ('Which DAW is best?', 'The one you will learn. Compare the common options first.'),
         ('Is Tunedzy a DAW?', 'No. It finishes voice recordings.')],
    related=['best-daw-for-vocal-recording', 'tunedzy-vs-logic-pro', 'what-is-a-vst-plugin']
)

add('what-is-a-vst-plugin', 'glossary', 'neon-wide', ['vocal-checker', 'lufs-meter'],
    title='What Is a VST Plugin? Plain Explanation',
    desc='A VST plugin is an effect or instrument that runs inside a DAW. What VST, AU and CLAP plugins are, and how Tunedzy relates to them.',
    h1='What Is a VST Plugin?',
    kw='what is a vst plugin',
    lead='A VST plugin is a software effect or instrument that runs inside a digital audio workstation. Plugins add reverb, compression, EQ and synthesisers. Tunedzy does not host plugins.',
    tldr=['A plugin is an effect or instrument that runs inside a DAW.',
          'VST, AU and CLAP are common plugin formats.',
          'Plugins need a host, such as a DAW.',
          'Tunedzy has its own built-in steps and does not host plugins.'],
    body='''
<h2>The short definition</h2>
<p>A plugin is a piece of software that runs inside a host, usually a DAW. It processes audio or generates it. VST is the most common format, with AU on Apple systems and CLAP as a newer option.</p>
<h2>Why plugins matter</h2>
<p>They let you build a chain of effects in your DAW: EQ, compression, reverb, delay and more. Many vocal chains use several plugins in a row.</p>
<h2>Tunedzy and plugins</h2>
<p>Tunedzy does not host plugins. Its steps are built in: repair, studio sound, level, tone, de-ess, Auto-duck and loudness. If you rely on a particular plugin, keep using it in your DAW and finish the file in Tunedzy after.</p>
''',
    vf_title='Plugins in the DAW, finish in Tunedzy',
    vf='<p>Use your plugins in your DAW for the mix, and finish the voice file in Tunedzy.</p>',
    faq=[('What is the difference between a plugin and a DAW?', 'A DAW is the host application; a plugin runs inside it.'),
         ('Does Tunedzy run VST plugins?', 'No. Its steps are built in.'),
         ('What is the most common plugin format?', 'VST is the most common, with AU on Apple systems.')],
    related=['what-is-a-daw', 'best-daw-for-vocal-recording', 'tunedzy-vs-reaper']
)

# ----------------------------------------------------------------------------------- audience
add('karaoke-host-audio-setup', 'audience', 'hero-wide', ['karaoke-autotune', 'clean-streaming-mic'],
    title='Audio Setup for Karaoke Hosts and Singing Nights',
    desc='How to set up a karaoke night for a clear voice: a mic and a speaker plan, a soft room, levels for loud singers and the cleanup for recorded clips.',
    h1='Audio Setup for Karaoke Hosts',
    kw='karaoke host audio setup',
    lead='A karaoke night needs a clear mic for the host, a level that suits every singer, and a sound system that does not feed back. Plan the mic and the room first; the rest follows.',
    tldr=['Use a dynamic mic for the host and singers; it handles loud voices and the room.',
          'Keep the mic a hand&rsquo;s width from the mouth, and turn the level before feedback.',
          'Soften the room where you can, and place speakers away from the mic.',
          'Record the best moments, and clean the clips afterwards.'],
    body='''
<h2>The mic</h2>
<p>A dynamic mic is sturdy and rejects some of the room, which suits a loud, busy night. Keep one mic per singer where you can, so the levels stay even.</p>
<h2>Levels and feedback</h2>
<p>Turn the level up until you hear the first feedback, then back off slightly. Place speakers away from the mic and in front of the singer, not behind.</p>
<h2>The room</h2>
<p>Soft furnishings and curtains reduce echo, which helps a karaoke room sound clear. A crowded, hard room is hard to keep clear.</p>
<h2>Recorded clips</h2>
<p>If you record the night, clean the clips afterwards with gentle settings and check the loudness before you share them. The <a href="/tunedzy/best-karaoke-maker-app">karaoke app roundup</a> covers the software side.</p>
''',
    vf_title='Clean the clips after the night',
    vf='<p>Tunedzy cleans recorded karaoke clips on your PC and sets the loudness before you share them.</p>',
    faq=[('Which mic is best for karaoke?', 'A dynamic mic for loud singers in a busy room.'),
         ('How do I stop feedback?', 'Lower the level, move the speakers away from the mic, and keep the mic in front of the singer.'),
         ('Can I share recordings of singers?', 'Ask each singer first, and check the music rights.')],
    related=['best-karaoke-maker-app', 'how-to-record-with-a-usb-microphone', 'what-is-a-condenser-vs-dynamic-microphone']
)

add('wedding-speech-recording', 'audience', 'booth', ['voice-recorder-noise-cancellation', 'lufs-meter'],
    title='Recording a Wedding Speech So Everyone Can Hear',
    desc='How to record a wedding speech or toast clearly: where to put the mic, how to handle a hall, the levels for emotional speakers and the cleanup for the keepsake.',
    h1='Recording a Wedding Speech',
    kw='record wedding speech',
    lead='A wedding speech is a keepsake, and it is often recorded in a large, echoey room. A lav or a close mic, a level set for the loudest moments and a gentle cleanup make it clear to hear for years.',
    tldr=['A lav or headset mic keeps the speaker close as they move.',
          'Set the level for the loudest moments, including laughter and emotion.',
          'In a large room, a second recorder can capture the room sound.',
          'Clean gently, so the speaker sounds like themselves.'],
    body='''
<h2>The mic</h2>
<p>A lav mic clipped to the chest or a headset keeps the distance steady as the speaker moves. A phone on a table works if the speaker stays close.</p>
<h2>The hall</h2>
<p>Large halls are echoey. Record close to the speaker, and a second recorder near the back of the room gives the room sound if you need it.</p>
<h2>The level</h2>
<p>Set the level for the loudest moments, including laughter and applause. Speakers often get louder when emotional, so check the level during the speech, not only at the start.</p>
<h2>Clean and share</h2>
<p>Clean the recording gently and check the loudness for the platform you share it on. The <a href="/tunedzy/how-to-use-a-lavalier-microphone">lav mic guide</a> covers the clip position.</p>
''',
    vf_title='Clean the speech, keep the speaker',
    vf='<p>Tunedzy cleans the speech gently and sets the loudness for sharing, so the keepsake is clear.</p>',
    faq=[('Should I use a lav or a phone?', 'A lav keeps the distance steady. A phone works if the speaker stays close.'),
         ('What about the echo in the hall?', 'Record close. A soft-sounding room gives a better result than a hard hall.'),
         ('Can I clean a speech recorded on the day?', 'Yes. Keep the original and clean a copy.')],
    related=['how-to-use-a-lavalier-microphone', 'voice-cleanup-for-public-speakers', 'how-to-record-a-meeting-clearly']
)

add('church-and-worship-team-audio', 'audience', 'neon', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Audio Cleanup for Church and Worship Teams',
    desc='Clean sermons, readings and worship recordings for a church or a team: the recording setup, the cleanup for the podcast or the archive, and the loudness for sharing.',
    h1='Audio Cleanup for Church and Worship Teams',
    kw='audio cleanup for church',
    lead='A church recording has to serve two jobs: a clear sermon for the congregation online, and an archive that holds up in years to come. Record the speaker close, keep the original, and clean a copy for sharing.',
    tldr=['Record the speaker close with a lav or a desk mic at the lectern.',
          'Keep the original recording as the archive.',
          'Clean a copy gently for sharing, and set the loudness for the platform.',
          'Check worship recordings for clipping on the loud moments.'],
    body='''
<h2>Record the speaker</h2>
<p>A lav or a close mic at the lectern gives a clear voice. The room mic gives the congregation sound, and works as a second track.</p>
<h2>Keep the archive</h2>
<p>Store the original recording unaltered. Clean copies are for sharing; the original is the record.</p>
<h2>Clean for sharing</h2>
<p>Clean the speech gently, and keep the speaker natural. Set the loudness for the platform you share to, and check the true peak. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> lists the targets.</p>
<h2>Worship music</h2>
<p>Choir and band recordings are loud and wide. Check them for clipping, and use music rights rules where they apply.</p>
''',
    vf_title='Archive the original, share a clean copy',
    vf='<p>Tunedzy cleans a copy of the sermon for sharing and sets its loudness. Keep the original as the archive.</p>',
    faq=[('Should I clean the archive?', 'Keep the original unaltered. Clean a copy for sharing.'),
         ('How do I handle a loud choir?', 'Check for clipping, lower the input, and set the level in a second pass.'),
         ('Do I need permission to share music?', 'Check the rights for any music you share.')],
    related=['voice-cleanup-for-public-speakers', 'how-to-use-a-lavalier-microphone', 'what-is-headroom']
)

add('dj-voice-intro-recording', 'audience', 'desk-wide', ['bpm-finder', 'song-key-finder'],
    title='Recording Voice Intros for DJs and Radio Shows',
    desc='How to record clean voice intros and drops for a DJ set or a radio show: the mic, the level, the timing against the music and the cleanup that keeps them sharp.',
    h1='Recording Voice Intros for DJs',
    kw='record dj voice intro',
    lead='A voice intro for a set or a show has to cut through music and sound sharp in a short clip. A close mic, a level that stands out and a clean take make an intro work.',
    tldr=['A close mic and a dry room give a sharp intro.',
          'Set the level so the voice sits above the music without clipping.',
          'Record the intro against the tempo, so the timing lines up.',
          'Clean each drop gently and keep the takes.'],
    body='''
<h2>The mic and the room</h2>
<p>A close mic in a dry room gives a sharp, present voice. Soft furnishings keep the echo down, so the voice sits well on top of the music.</p>
<h2>Level and timing</h2>
<p>Set the level so the voice stands out from the music without clipping. Record against the tempo of the set, using the <a href="/tunedzy/tools/bpm-finder">BPM finder</a> to find it, so the words land on the beat.</p>
<h2>Clean the drops</h2>
<p>Clean each drop with gentle settings and check the loudness against the rest of the set. Keep the takes so you can swap them later.</p>
''',
    vf_title='Sharp intros, clean drops',
    vf='<p>Tunedzy cleans each intro and sets it to a level that sits well with the music.</p>',
    faq=[('How loud should an intro be?', 'Loud enough to cut through the music, and below clipping. Test it with the set.'),
         ('Should I match the tempo?', 'Yes, where the words land on the beat. The BPM finder helps.'),
         ('Can I use a phone?', 'Yes, close to the mouth in a dry room.')],
    related=['how-to-make-a-podcast-intro-and-outro', 'how-to-duck-music-under-a-voiceover', 'how-to-record-a-voicemail-greeting']
)

add('musicians-making-demos', 'audience', 'mic-wide', ['song-key-finder', 'bpm-finder', 'chord-finder'],
    title='Recording Song Demos at Home for Musicians',
    desc='How musicians record demos at home: a quick room setup, clean takes, key and tempo checks, and a finishing pass for the vocal that makes the demo usable.',
    h1='Recording Song Demos at Home',
    kw='record song demo at home',
    lead='A demo is a quick, clear record of a song idea. It does not need a studio, only a clean vocal, the right key and tempo, and a finish that lets people hear the song.',
    tldr=['Set up a quick, dry space and record the vocal close.',
          'Check the key and tempo before you sing the full song.',
          'Record several takes, and keep the best phrases.',
          'Finish the vocal gently so the demo is easy to hear.'],
    body='''
<h2>Set up quickly</h2>
<p>A demo is about the idea. A dry space with soft surfaces and a mic at a steady distance is enough. Record a few seconds of room tone first.</p>
<h2>Key and tempo</h2>
<p>Find the key and tempo of the beat before you record. The <a href="/tunedzy/tools/song-key-finder">key finder</a> and the <a href="/tunedzy/tools/bpm-finder">BPM finder</a> measure them in your browser.</p>
<h2>Takes and finish</h2>
<p>Record several takes, and keep the best phrases. Clean the vocal, level it against the beat and tune it lightly, using the <a href="/tunedzy/how-to-clean-a-song-vocal-recorded-on-a-phone">vocal cleanup steps</a>.</p>
''',
    vf_title='Finish the demo vocal',
    vf='<p>Tunedzy cleans and levels the demo vocal, and exports the mix at a loudness target.</p>',
    faq=[('Does a demo need a studio?', 'No. A clean vocal in a dry space is enough to hear the song.'),
         ('Should I master a demo?', 'A light finish is enough. A demo is for the idea.'),
         ('How many takes?', 'Several. Keep the best phrases, and comp them if you can.')],
    related=['record-a-vocal-at-home-for-a-song', 'vocal-cleanup-for-singers-and-rappers', 'best-daw-for-vocal-recording']
)

add('real-estate-voiceovers', 'audience', 'hero', ['voice-recorder-noise-cancellation', 'lufs-meter'],
    title='Voiceovers for Real Estate and Property Videos',
    desc='How to record clear voiceovers for property videos and tours: the room, the script, the level for a phone and the cleanup that keeps the narration clear.',
    h1='Voiceovers for Property Videos',
    kw='real estate voiceover recording',
    lead='A property video is watched with the sound low, often on a phone. A clear, warm narration in a quiet room, at a level that suits a phone, keeps viewers listening.',
    tldr=['Record the narration in a quiet, soft room, away from the street.',
          'Write a short script, one line per room or feature.',
          'Set the level so it reads clearly on a phone speaker.',
          'Put the cleaned narration into the video and check the timing.'],
    body='''
<h2>The room</h2>
<p>Record in a quiet room, away from traffic and appliances. Soft furnishings help. Record the narration in a room that is not the property itself, if you can, so the property sound does not mix in.</p>
<h2>The script</h2>
<p>Write one short line for each feature. Read it aloud and time it, so the narration fits the video.</p>
<h2>Level and clean</h2>
<p>Set the level so the narration reads clearly on a phone. Clean it gently and check the loudness. The <a href="/tunedzy/record-a-voiceover-on-your-phone">voiceover guide</a> covers the take.</p>
<h2>Put it in the video</h2>
<p>Align the narration with the video, and use <a href="/tunedzy/put-clean-audio-back-into-a-video">replace audio</a> if the video needs a new sound.</p>
''',
    vf_title='Clear narration for phones',
    vf='<p>Tunedzy cleans the narration and sets the level so it reads clearly on a phone speaker.</p>',
    faq=[('Should I use music?', 'Only music you have the right to use. Duck it under the narration.'),
         ('How long should a line be?', 'Short. A line per feature keeps the video moving.'),
         ('Can I use my phone for the narration?', 'Yes, in a quiet room, close to the mouth.')],
    related=['record-a-voiceover-on-your-phone', 'how-to-add-background-music-to-a-voiceover', 'put-clean-audio-back-into-a-video']
)

add('course-creator-audio', 'audience', 'booth-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='Audio for Online Course Creators',
    desc='How to record consistent audio for online courses: the set-up, lesson-by-lesson consistency, captions for accessibility and the cleanup that keeps a whole course even.',
    h1='Audio for Online Course Creators',
    kw='audio for online course creators',
    lead='A course is many lessons that must sound like the same teacher in the same room. Set the room and the mic once, record in sections, and clean every lesson with the same settings.',
    tldr=['Fix the room, the mic and the distance for the whole course.',
          'Record in sections, and keep a note of the settings.',
          'Clean each lesson the same way, and check the loudness across lessons.',
          'Add captions from the transcript for accessibility.'],
    body='''
<h2>Consistency</h2>
<p>Students notice when the sound changes between lessons. Use the same room, mic and distance for every session, and write the settings down.</p>
<h2>Sections</h2>
<p>Record each lesson in sections, so a stumble is easy to re-record. The <a href="/tunedzy/how-to-record-a-lecture-or-tutorial-voice">lecture voice guide</a> covers the take.</p>
<h2>Cleanup and captions</h2>
<p>Clean every lesson with the same settings, then check loudness across a few lessons together. Export captions from the transcript and check them against the audio. The <a href="/tunedzy/audio-cleanup-for-teachers">teacher routine</a> has the sequence.</p>
''',
    vf_title='One sound for the whole course',
    vf='<p>Tunedzy cleans every lesson the same way, sets the loudness, and exports captions from the transcript.</p>',
    faq=[('How do I keep the sound the same over months?', 'Note the mic, the distance and the level, and record in the same room.'),
         ('Do captions matter?', 'Yes, for accessibility and for viewers in noisy places.'),
         ('Should I clean every lesson?', 'Yes, with the same settings, so the course sounds even.')],
    related=['audio-cleanup-for-teachers', 'how-to-record-a-lecture-or-tutorial-voice', 'how-to-record-an-audiobook-at-home']
)

add('language-tutor-audio', 'audience', 'neon-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='Audio for Language Tutors and Lesson Recordings',
    desc='How language tutors record clear model pronunciation and lesson audio: a steady voice, clear word endings, short clips and the cleanup that keeps lessons easy to follow.',
    h1='Audio for Language Tutors',
    kw='audio for language tutors',
    lead='A language lesson lives on clear pronunciation. A steady voice, a close mic and short, well-separated clips help a learner hear every sound, and a light cleanup keeps the audio natural.',
    tldr=['Record model pronunciation close and steady, at a slightly slower pace.',
          'Keep clips short and separate them, so learners can repeat each one.',
          'Clean gently; over-processing can blur the sounds learners need.',
          'Export at a loudness that works on a phone.'],
    body='''
<h2>Clear model speech</h2>
<p>A close mic in a quiet room, a steady pace and clear word endings give learners a good model. Speak slightly more slowly than normal, without distorting the sounds.</p>
<h2>Short clips</h2>
<p>Record each phrase as its own clip, with a short pause before and after. Learners can repeat each one and replay it.</p>
<h2>Cleanup</h2>
<p>Clean the room noise gently. Blurred consonants and vowels defeat the purpose of a model recording, so keep the cleanup light. The <a href="/tunedzy/pronunciation-recording-for-language-learners">pronunciation recording guide</a> covers the learner side.</p>
''',
    vf_title='Clear models, light cleanup',
    vf='<p>Tunedzy cleans each clip gently and sets the loudness, so learners hear every sound clearly.</p>',
    faq=[('How long should a clip be?', 'A phrase or a sentence. Short clips are easier to repeat.'),
         ('Can cleanup change the sounds?', 'Over-processing can blur them. Keep it light and listen carefully.'),
         ('Do I need a studio?', 'No. A quiet room and a close mic are enough.')],
    related=['pronunciation-recording-for-language-learners', 'audio-cleanup-for-teachers', 'how-to-record-a-voicemail-greeting']
)
