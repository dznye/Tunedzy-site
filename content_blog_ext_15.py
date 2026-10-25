"""Blog posts, batch 15: speech recognition and on-device transcription. Merged into content_blog.py.
Company claims are attributed to the company and are not repeated as measured facts. Where a feature was reported
rather than confirmed on the company's own page, the post says so. No invented statistics.
Funnel: each post ends with a link to Tunedzy Go and to the matching free tool."""

CLUSTERS = {
    'trend-ai-speech': dict(tool='voice-recorder-noise-cancellation', label='Speech recognition and on-device transcription', tool_name='Noise-Free Voice Recorder'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='on-device-transcription-explained', cluster='trend-ai-speech', kw='on device transcription',
    title='On-Device Transcription: What Runs on Your Phone and Why It Matters',
    desc='On-device transcription explained: how speech recognition runs on a phone or laptop, what changes for privacy and speed, and what to check before you rely on it.',
    h1='On-Device Transcription Explained: What Runs on Your Phone and Why It Matters',
    answer='On-device transcription runs the speech model on your own phone or computer, so the audio does not have to be sent to a server. That can help privacy and speed, and it can work offline. The trade-offs are that models are smaller, updates depend on the device, and accuracy still varies with the recording.',
    body='''
<p>For years, most speech-to-text systems sent your audio to a remote server, processed it there and sent the text back. That still happens, and it works well for many people. A growing number of tools now run the speech model on the device itself, which means the audio can stay on your phone or laptop. The shift matters for privacy, for speed and for whether a transcript is available when there is no connection.</p>
<p>This post explains how on-device transcription works in plain terms, what it changes, where it still falls short and what to check before you trust it with a sensitive recording. It is general information, and the features of any particular product may change.</p>
<h2>How the model runs</h2>
<p>A speech recognition model is a large set of numbers that has learned how sounds map to words. Running the model means the device takes the audio, turns it into the form the model expects, runs the calculation and produces text. In a cloud service, that calculation happens on powerful servers. On a device, it happens on the phone or laptop, using its processor and sometimes a dedicated chip.</p>
<p>The same basic steps apply either way. The difference is where the calculation runs, and that decides who can see the audio while it is processed.</p>
<h2>What on-device means for privacy</h2>
<p>When the audio never leaves the device, the provider does not receive it for processing. That reduces the number of places a recording can be stored, copied or exposed. For a private interview, a medical note or a confidential meeting, that can be a meaningful difference. It does not make a tool automatically private, because the app may still send other data, such as usage logs or the finished text, to a server. Read what the app says it sends.</p>
<p>On-device processing also helps when a recording is sensitive for legal or professional reasons. A journalist or a researcher may prefer a tool that keeps the raw audio on their own machine, and this is one reason on-device options are attractive.</p>
<h2>Speed and offline use</h2>
<p>Local processing can be faster, because it avoids the upload and the round trip to a server. It also works without an internet connection, which is useful on a train, in a remote location or when a network is poor. The speed depends on the device, and an older phone may be slower than a modern laptop for the same job.</p>
<p>Offline use is also a question of storage. A speech model takes up space on the device, and it may need downloading before the first use. Check how large the model is and whether it can be removed when you no longer need it.</p>
<h2>What Apple and Google have reported</h2>
<p>Apple introduced a speech analysis framework at its developer conference in 2025, which Apple describes as running entirely on the device, and which shipped with its iOS 26 software. Reports on the framework describe it as faster than some open models, but those claims come from comparisons that are not independently verified here. Google has been reported to make its on-device language model available to developers for phone features on newer Pixel hardware. Treat these as company and press statements, and check the developer documentation before building a workflow around them.</p>
<p>The general pattern is clear, even if the details are changing: more speech features are moving onto the device, and developers are being given tools to use them.</p>
<h2>Where on-device tools fall short</h2>
<p>On-device models are often smaller than the largest cloud models, which can mean less accuracy on difficult audio. Names, technical terms, accents and crosstalk remain hard for any model. A quiet recording of one speaker will transcribe well, while a noisy room with several people will produce more errors. The device does not change the basic problem of the recording.</p>
<p>Updates can also differ. A cloud service can improve its model for everyone at once, while an on-device model may update only when the operating system or the app is updated. That can leave older devices behind for longer.</p>
<h2>What to check before you rely on it</h2>
<ol>
<li>Confirm whether the audio is processed on the device, and whether any of it is sent to a server.</li>
<li>Check the app&rsquo;s privacy policy for what is stored, logged or shared with others.</li>
<li>Test the tool on a short sample of your own recording, with the same microphone and room.</li>
<li>Check the transcript against the audio for names, numbers and quotes.</li>
<li>Find out how the model is updated, and whether the device needs to be upgraded to keep it current.</li>
</ol>
<h2>When a cloud tool is still the better choice</h2>
<p>A cloud tool can be better for very long recordings, for languages with less local support, or for work that needs the most accurate model available. The choice depends on the recording, the privacy needs and the quality required. Some teams use a local tool for drafts and a cloud tool for final transcripts, after checking that the cloud service meets their privacy requirements.</p>
<h2>Limits</h2>
<p>Product features and platform support change quickly, and company claims about speed and accuracy are not independent measures. This post describes the category, not a ranking of products. Test the tool you plan to use on your own audio before you depend on it.</p>
<h2>Clean the recording first</h2>
<p>A cleaner recording gives any model a better chance. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps before a transcript. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording in your browser. For the question of private processing, read the <a href="/tunedzy/blog/is-ai-audio-cleaning-private">privacy post</a> in this series.</p>
''',
    faq=[('Does on-device transcription need the internet?', 'Usually not once the model is installed. Check the app, since some features still need a connection.'),
         ('Is on-device automatically private?', 'It keeps the audio on your device, but the app may still send other data. Read its privacy policy.'),
         ('Is on-device less accurate?', 'Often it can be, because the models may be smaller. Test on your own recordings.'),
         ('Do I need a new phone for it?', 'Some features need recent hardware and software. Check the requirements for the app you use.')])

add(slug='speech-recognition-on-phones-2026', cluster='trend-ai-speech', kw='speech recognition on phone 2026',
    title='Speech Recognition on Phones in 2026: What Has Changed for Creators',
    desc='Speech recognition on phones in 2026: what has changed for creators, the reported features from Apple and Google, and how to use them for captions and notes.',
    h1='Speech Recognition on Phones in 2026: What Has Changed for Creators',
    answer='Phones now handle more speech recognition on the device, with features for transcripts, captions and voice notes built into the operating system. For creators, that means quicker first drafts and more private options. The features vary by device and software version, so check each one on the phone you use before building a routine around it.',
    body='''
<p>A few years ago, dictating a note or getting a transcript from a recording on a phone was often a clumsy experience. Recognition was slow, the results needed heavy editing and many features needed a connection. That has been changing. Phones now handle more of the work themselves, and a creator with a recent device can get a usable first draft from a recording without leaving the phone.</p>
<p>This post looks at what has changed for creators, which features have been reported, and how to use them well. The details depend on the device and the software version, so check each feature on your own phone.</p>
<h2>What has changed</h2>
<p>The main change is that more recognition runs on the device, which makes it faster and more private for many tasks. A creator can record a voice note, get a transcript, edit it and file it without the audio leaving the phone. Captions and transcripts are also more widely available in the apps that creators already use, such as recording tools and video editors.</p>
<p>The second change is the quality of the first draft. A modern recognition model usually gets the bulk of clear speech right, which saves time on the typing. The editing that remains is about names, numbers, technical terms and the places where the speaker mumbled.</p>
<h2>What Apple and Google have reported</h2>
<p>Apple has said its speech analysis framework runs on the device and shipped with its iOS 26 software. Reports describe features built on the framework in apps such as recording and notes. Google has been reported to provide developers with on-device language models for phone features on its newer Pixel devices. These are reports and company statements, so check the current feature list on your own device rather than relying on a summary.</p>
<p>Both platforms have also been adding chapters and summaries to recordings in some apps. Those features are useful for finding a point in a long file, but they should be checked against the audio before you publish them.</p>
<h2>What it means for captions</h2>
<p>Captions made on a phone are fast, and they are often good enough for a first pass. The risk is that a small error in a name or a number goes unnoticed and then appears in a published video. Read every caption against the audio, especially the first and last lines, because those are the ones viewers notice most. The <a href="/tunedzy/how-to-export-captions-srt-and-vtt">caption export guide</a> explains how to save the captions in the formats platforms accept.</p>
<h2>What it means for voice notes</h2>
<p>For a creator who records ideas on the go, on-device transcription turns a voice note into searchable text almost at once. That is a strong habit to build. Name the note with the date and topic, keep the transcript with the audio, and move the useful ideas into a project folder once a week, so nothing is lost in a long list.</p>
<h2>Check the privacy settings</h2>
<p>On-device recognition keeps the audio on the phone, but not every feature does. Some apps send audio or text to a server for extra processing, and some keep logs. Check the settings of each app, and turn off any feature you do not need. For a sensitive interview, confirm the processing location before recording.</p>
<h2>Where phones still fall short</h2>
<p>A phone microphone in a noisy place will produce more errors than a close microphone in a quiet room, and no recognition model can fully overcome a poor recording. Several speakers talking at once, strong accents and specialist vocabulary also cause problems. A phone is a good recorder for many jobs, but it is not a substitute for a clean setup when the transcript matters.</p>
<h2>A simple routine</h2>
<ol>
<li>Record in a quiet spot, with the phone close to the speaker.</li>
<li>Get the first draft transcript on the phone, while the details are fresh.</li>
<li>Check names, numbers and quotes against the audio.</li>
<li>Export the transcript and the captions in the formats you need.</li>
<li>Note which features you used, so you can repeat the routine on the next device.</li>
</ol>
<h2>Teaching the routine to a team</h2>
<p>If a team shares a phone workflow, write the routine down once and keep it where everyone can see it. Include the app names, the settings, the steps for checking names and numbers, and the place where the final transcript is stored. A written routine makes it easy for a new team member to produce the same quality of work, and it stops every person inventing their own method.</p>
<p>Agree a single place for the finished files, with a clear naming pattern, and make sure the phone&rsquo;s own storage is not the only copy. A routine that depends on one phone is fragile when that phone is lost, updated or replaced.</p>
<h2>Limits</h2>
<p>Features on phones change with each software update, and some are limited to newer devices or to certain regions. Reports about new features may be early or incomplete. Check the current feature list on your own phone before you plan a routine around it.</p>
<h2>Start with a clean recording on your phone</h2>
<p>Good recognition starts with good audio. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording in your browser. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can record voice-overs with live noise removal or clean an existing recording. For the on-device question in more depth, read the <a href="/tunedzy/blog/on-device-transcription-explained">on-device transcription post</a> in this series.</p>
''',
    faq=[('Can my phone transcribe without the internet?', 'Some features can, on newer devices. Check the feature on your own phone.'),
         ('Are phone captions accurate enough to publish?', 'Often good for a first pass, but check every caption against the audio before publishing.'),
         ('Do newer phones do better?', 'Usually, because they can run larger models. The software version also matters.'),
         ('Is my voice note private?', 'Depends on the app. Check whether processing is on the device and what the app stores.')])

add(slug='live-captions-for-streams-explained', cluster='trend-ai-speech', kw='live captions for streaming',
    title='Live Captions for Streams Explained: How They Work and What to Check',
    desc='Live captions for streams explained: how real-time speech recognition works, the delay and error trade-offs, and the checks to run before going live.',
    h1='Live Captions for Streams Explained: How They Work and What to Check',
    answer='Live captions turn speech into text as you talk, using real-time recognition. They help viewers who are deaf or hard of hearing, and viewers watching without sound. Expect a short delay and some errors, check the settings before going live, and keep the captions readable against the video.',
    body='''
<p>Live captions have moved from a niche feature to a common option on video platforms and streaming tools. A caption appears under the picture as the speaker talks, which helps viewers who are deaf or hard of hearing, viewers in a noisy place and anyone watching with the sound off. For a creator, captions also improve accessibility and can keep people watching longer. They come with trade-offs that are worth understanding before going live.</p>
<p>This post explains how live captions work, the delay and error trade-offs, the settings to check and the habits that make captions useful rather than distracting.</p>
<h2>How live recognition works</h2>
<p>Live captioning runs a speech recognition model on a continuous stream of audio. The model produces partial text as the speaker goes, then revises it as more context arrives. That is why a caption can change a word after it first appears. The process is fast, but it cannot wait for a full sentence without adding delay, so it makes a judgement with less context than a recording would allow.</p>
<p>The result is a good first pass, not a finished transcript. Expect the captions to be less accurate than a transcript made afterwards from a clean recording.</p>
<h2>The delay</h2>
<p>Live captions usually lag the speech by a short time. The lag depends on the tool, the connection and the length of phrase the model waits for. A viewer may see the caption a moment after the words are spoken, which can feel slightly out of step. For fast-paced talk, the lag is more noticeable, and the caption may seem to arrive in bursts.</p>
<p>Test the delay before you go live, by speaking a few sentences and watching the caption. If the lag is large, consider slowing your pace slightly or choosing a different setting.</p>
<h2>The errors</h2>
<p>Live recognition makes errors with names, technical terms, numbers and accents. A wrong word can change the meaning of a sentence, and a viewer may notice the error more than the correct text around it. Use a shared glossary of names and terms before the stream, and check the most important words in the first minutes to see how the tool handles them.</p>
<p>Consider telling viewers that captions are automatic and may contain errors. A short note sets fair expectations, and it helps viewers who rely on the captions to understand the limits.</p>
<h2>Settings to check before going live</h2>
<ul>
<li>The language, and whether it matches the speech you will use.</li>
<li>The caption size, colour and background, so the text is readable on a phone.</li>
<li>The position of the captions, so they do not cover important parts of the picture.</li>
<li>The microphone input, since captions depend on clean audio.</li>
<li>Whether the captions are saved, so you can publish them with the recording later.</li>
</ul>
<h2>Readability on the screen</h2>
<p>Captions should be large enough to read on a phone, with enough contrast against the picture. Keep each line short, and avoid changing the position of the captions during the stream. A caption that jumps around distracts the viewer from the speaker. The guidance in the <a href="/tunedzy/blog/caption-readability-rules">readability post</a> in this series explains the basics.</p>
<h2>Audio quality matters more</h2>
<p>Captions depend on clean audio, and a noisy microphone produces more errors. A steady, close microphone, a quiet room and a level that is not clipping all improve the captions as well as the sound. A live stream with good audio gives the recognition a better chance, so treat the audio setup as part of the captioning.</p>
<h2>Saving the captions</h2>
<p>If you save the stream, keep the captions as a file. A saved transcript can be corrected after the event, and the corrected captions can be attached to the recording. Editing the captions afterwards makes the replay more useful, because the errors that mattered in the live version can be fixed for later viewers.</p>
<h2>Plan for technical failure</h2>
<p>A live caption feed can fail in the middle of a stream, through a dropped connection, a crashed app or a microphone that stops sending audio. Decide in advance what you will do: whether the stream continues without captions, whether a second caption source is ready, and how you will tell viewers. A short pinned message that explains the problem and the expected return is far better than silence.</p>
<p>Rehearse the recovery once. Turn the captions off and on again during a test, and time how long it takes to restore them. A rehearsed fix turns a panic into a routine change.</p>
<h2>Limits</h2>
<p>Live captions are a first pass, and they cannot match a carefully checked transcript. Features and accuracy vary between platforms and tools, and claims from vendors are not independent measures. Test the setup before a live event, and be ready to explain that the captions are automatic.</p>
<h2>Start with clean audio</h2>
<p>Good captions begin with a good microphone signal. The <a href="/tunedzy/tools/clean-streaming-mic">Clean Streaming Mic</a> offers live noise cancellation for OBS, Discord and Zoom, which helps keep the speech clear before it reaches the recognition. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the wider picture of recognition, read the <a href="/tunedzy/blog/on-device-transcription-explained">on-device transcription post</a>.</p>
''',
    faq=[('Are live captions accurate?', 'They are a good first pass, but they make errors, especially with names and terms. Tell viewers they are automatic.'),
         ('Why do captions lag behind speech?', 'The recognition waits for context before it finalises text. Some lag is normal.'),
         ('Can I save live captions?', 'Often yes, depending on the tool. A saved file can be corrected and attached to the replay.'),
         ('Do captions help viewers without hearing loss?', 'Yes. They help anyone watching with sound off, in a noisy place or in another language.')])

add(slug='caption-readability-rules', cluster='trend-ai-speech', kw='caption readability rules',
    title='Caption Readability Rules for Creators: Size, Timing and Placement',
    desc='Caption readability rules for creators: line length, reading speed, timing, placement and contrast, with checks to run on a phone before publishing.',
    h1='Caption Readability Rules for Creators: Size, Timing and Placement',
    answer='Readable captions are short, well timed and placed where they do not hide the picture. Keep lines to a comfortable length, give viewers enough time to read each caption, use strong contrast, and check the result on a phone at the size most people watch. Accuracy matters as much as layout.',
    body='''
<p>Captions are only useful if people can read them. A caption that appears too briefly, sits on a busy background or covers the speaker&rsquo;s face is not doing its job, however accurate the words. Readability is a set of small choices about length, timing, placement and contrast, and they add up to a caption that viewers can follow without effort.</p>
<p>This post sets out the rules that matter most for creators, explains why each one matters and gives a simple check to run before publishing. The principles apply to live and recorded captions alike.</p>
<h2>Keep lines short</h2>
<p>A caption line should be short enough to read in one glance. Long lines force the eye to travel, and viewers miss the start of the next line. Aim for a comfortable length that fits the screen width and leaves room around the edges. Break the line at a natural point, such as before a clause or a pause, rather than in the middle of a phrase.</p>
<p>Most captions work best in one or two lines. A caption that runs to three or four lines is hard to follow, especially on a phone where the text is smaller relative to the screen.</p>
<h2>Give viewers time to read</h2>
<p>The reading speed is the most common cause of unreadable captions. A caption that disappears before the viewer finishes reading is frustrating. Give each caption enough time on screen to be read at a steady pace, and allow a little more for longer lines. Avoid keeping a caption on screen so long that it lags behind the speech, because the viewer then reads ahead of the speaker and loses the thread.</p>
<p>Check the timing by playing the video at normal speed and reading each caption as it appears. If you cannot finish a line before it vanishes, adjust the timing or shorten the text.</p>
<h2>Place captions carefully</h2>
<p>The bottom of the frame is the usual place for captions, but it is not always the right one. Check that the captions do not hide on-screen text, a product, a face or a chart. Some platforms place their own elements over the bottom of the frame, so check the layout on the platform itself before publishing.</p>
<p>Keep the position steady across the video. A caption that jumps from one side to the other makes the viewer search for the text.</p>
<h2>Use strong contrast</h2>
<p>Readable captions need contrast with the background. A white or light caption on a bright picture can disappear, and a dark caption on a dark scene is just as difficult. Use a background box or outline where needed, and choose a size that remains clear on a small screen. Test the captions on the busiest part of the video, not only the calmest.</p>
<h2>Keep the text accurate</h2>
<p>Readability includes accuracy. A caption that is easy to read but wrong in a name or a number misleads the viewer. Check each caption against the audio, paying particular attention to names, numbers, dates and specialist words. Automatic captions often make the same errors repeatedly, so a single fix can improve the whole file.</p>
<p>Remove filler words where they add nothing, but keep the speaker&rsquo;s meaning and tone. Captions are a transcript of meaning, not a perfect copy of every sound.</p>
<h2>Mark speakers and sounds</h2>
<p>When more than one person speaks, identify the speaker at the start of a new speaker&rsquo;s line, or use a consistent colour or label. Mark important sounds, such as laughter or music, where they change the meaning. Keep these markers brief so they do not crowd the caption.</p>
<h2>Check the result on a phone</h2>
<p>Watch the video on a phone at the size most viewers use, with the sound off. Read every caption as it appears. Ask whether you could follow the video without the sound, and fix any caption that causes a pause. The phone check is the most useful test you can run.</p>
<h2>Caption long-form interviews differently</h2>
<p>A long interview needs a slightly different approach from a short, fast video. Viewers are more likely to watch in pieces, so each caption must still make sense when someone joins mid-conversation. Keep speaker labels visible at the start of each new section, and avoid captions that depend on a joke or reference from several minutes earlier.</p>
<p>Consider adding a short on-screen title at the start of each chapter, so viewers can orient themselves. Captions and titles together make a long conversation easier to enter at any point.</p>
<h2>Limits</h2>
<p>Reading speed and preference vary between viewers, and some platforms offer their own caption settings. The rules here are guidelines, not a standard that every platform enforces. Check the platform&rsquo;s guidance for its own display, and keep the captions as clear as you can.</p>
<h2>Make the audio clear too</h2>
<p>Captions help, but the sound still matters to everyone who listens. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, which helps the recognition as well as the listener. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the export formats, see the <a href="/tunedzy/how-to-export-captions-srt-and-vtt">caption export guide</a>.</p>
''',
    faq=[('How many lines should a caption have?', 'Usually one or two. Three or four lines are hard to follow, especially on a phone.'),
         ('How long should a caption stay on screen?', 'Long enough to read at a steady pace. Check by reading each caption at normal speed.'),
         ('Where should captions sit?', 'Usually at the bottom, away from on-screen text and faces. Check the platform layout.'),
         ('Do captions need to match the speech word for word?', 'They should match the meaning accurately. Remove filler where it adds nothing.')])

add(slug='multilingual-transcription-for-creators', cluster='trend-ai-speech', kw='transcribe in multiple languages',
    title='Multilingual Transcription for Creators: Working Across Languages',
    desc='Multilingual transcription for creators: how tools handle more than one language, the errors to expect, how to translate captions safely and how to check the result.',
    h1='Multilingual Transcription for Creators: Working Across Languages',
    answer='Multilingual transcription lets creators caption and translate content for wider audiences. Tools vary in the languages they support and in how they handle mixed-language speech. Test each language on your own material, check names and terms, and have a fluent reviewer check translations before publishing.',
    body='''
<p>A creator who works in more than one language can reach far more listeners, but the tools that help are uneven. A transcription model may be very good in one language and weaker in another. Mixed-language speech, where a speaker moves between languages in the same sentence, is harder still. The result is that multilingual work needs more testing and more checking than a monolingual project.</p>
<p>This post explains how multilingual transcription works in general, what errors to expect and how to produce captions and translations that serve the audience well.</p>
<h2>What the tools can and cannot do</h2>
<p>Many recognition tools support a list of languages, but the quality for each one varies. Some languages have large amounts of training data and perform strongly, while others have less and perform less well. A tool&rsquo;s list of supported languages does not tell you how accurate it is for your speaker, your accent or your subject. Test before you rely on it.</p>
<p>Translation is a separate step in most workflows. A transcription tool may offer a translation, but the translation quality varies, and it can miss cultural meaning, idioms and humour. Translation needs its own check.</p>
<h2>Mixed-language speech</h2>
<p>When a speaker switches between languages, many tools struggle. They may force every word into one language, or they may misidentify a language and produce nonsense. If your content mixes languages, check whether the tool supports multiple languages in the same recording, and test a sample that contains the switches you expect.</p>
<p>Consider marking the switches in the transcript, so a reader can see where the language changed. That helps the editing and the translation.</p>
<h2>Names and terms</h2>
<p>Names, places and specialist terms are the most common errors in any language. A name may be spelled in several ways, and a tool may choose the wrong one. Build a glossary before you transcribe, with the correct spellings of names, products and technical words in each language. Check the transcript against the glossary during editing.</p>
<h2>Translating captions</h2>
<p>When you translate captions, keep the timing in mind. A translated line may be longer than the original, and a longer line may not fit the time on screen. Shorten the translation where needed, while keeping the meaning. Use the same caption rules as the original, so readability is preserved in each language.</p>
<p>Keep the speaker&rsquo;s tone. A formal speaker should not sound casual in translation, and a joke should still be a joke. Those are judgements a fluent reviewer makes better than a tool.</p>
<h2>Who should check the translation</h2>
<p>A fluent reviewer should check every translation before publishing, especially for a public video. Machine translation can be useful for a first draft, but it can make errors that change the meaning, and some errors are embarrassing. A reviewer who knows the subject will catch more than a general speaker.</p>
<p>Pay for the review if you can. A small fee for a careful check is often worth more than a faster release with errors.</p>
<h2>Keeping track of versions</h2>
<p>Keep each language version in a separate file, with a clear name and date. Record which tool produced the first draft and who reviewed the translation. A record makes updates easier, and it helps when a correction is needed later.</p>
<h2>Choose the right language for the audience</h2>
<p>The language of the captions should follow the language your audience reads most comfortably, which is not always the language the speaker uses. A creator who speaks a regional dialect may choose a standard form for captions, so more viewers can follow. Decide this deliberately, and say in the description which languages are available.</p>
<p>Some audiences prefer subtitles in their own language even when they understand the original. Ask a few viewers, and let their answers guide the choice rather than assumptions about what they want.</p>
<h2>Plan the review budget</h2>
<p>Review takes time, and it is easy to underestimate. A translated video of ten minutes may need an hour or more of careful checking, depending on the content and the reviewer. Build that time into the schedule and the budget, so the review is not the step that gets cut when a deadline approaches.</p>
<p>Keep a note of the reviewer, the date and the version checked. A record of who approved each language is useful if an error is found later.</p>
<h2>Limits</h2>
<p>Language support and quality change as tools are updated, and vendor claims about accuracy are not independent measures. This post describes the general problems, not the performance of any particular product. Test your own languages and your own content before you commit.</p>
<h2>Start with clean audio in every language</h2>
<p>Clean audio helps every language, and it is the first step in any multilingual workflow. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the readability of the captions themselves, read the <a href="/tunedzy/blog/caption-readability-rules">caption readability post</a>.</p>
''',
    faq=[('Does a tool that lists a language work well for it?', 'Not necessarily. Test the language on your own material, with your speaker and subject.'),
         ('Can I trust machine translation for captions?', 'Use it for a first draft only, and have a fluent reviewer check the result.'),
         ('What about mixed-language speech?', 'Test a sample with the switches you expect, and mark the switches in the transcript.'),
         ('How do I keep names correct across languages?', 'Build a glossary of names, places and terms before you transcribe, and check against it.')])

add(slug='meeting-recording-transcription-and-consent', cluster='trend-ai-speech', kw='meeting recording transcription consent',
    title='Meeting Recording and Transcription: Consent and Good Practice',
    desc='Meeting recording and transcription: when consent is needed, what to tell attendees, how to store transcripts and how to avoid the common mistakes.',
    h1='Meeting Recording and Transcription: Consent and Good Practice',
    answer='Recording and transcribing a meeting requires consent in many places, and the rules vary by country and by the people present. Tell everyone before recording, say what the recording and transcript will be used for, store them securely and delete them when they are no longer needed.',
    body='''
<p>Meeting recordings and automatic transcripts have become common in offices, classrooms and remote teams. They save time and make it easier to share decisions, but they also raise questions about privacy and consent. A recording that captures a candid discussion can be sensitive, and a transcript can be searched, copied and shared far more easily than a conversation was ever shared before.</p>
<p>This post covers the practical side: when consent is needed, what to tell people, how to handle the files and the mistakes that cause trouble. It is general guidance, not legal advice, and the rules differ between places and workplaces.</p>
<h2>Why consent matters</h2>
<p>A recording captures what people said, in their own voices, and a transcript captures the words in a searchable form. Many people are comfortable in a meeting but not comfortable being recorded or transcribed. Consent respects that difference, and it protects the organisation as well as the people in the room. In many places, recording a conversation without the consent of the people involved is not allowed, and it can damage trust even where it is.</p>
<p>The safest practice is to ask every participant before the recording starts, and to make it easy to say no without consequence.</p>
<h2>What to tell attendees</h2>
<p>Say that the meeting is being recorded and transcribed, who will have access to the files, what they will be used for and how long they will be kept. Explain whether an automatic tool will process the audio, and whether the audio or transcript leaves the organisation. A short written note in the invitation helps, and a spoken confirmation at the start of the meeting makes the consent clear.</p>
<p>Offer an alternative, such as a manual note-taker, for anyone who does not want to be recorded. Respect that choice.</p>
<h2>Check the tool before you use it</h2>
<p>Before you use a meeting recording or transcription tool, read its privacy terms. Check whether the audio is stored, for how long, whether it is used to train models, and where it is processed. A tool that processes on the device, or that deletes files quickly and clearly, is easier to justify than one that keeps everything. The <a href="/tunedzy/blog/is-ai-audio-cleaning-private">privacy post</a> in this series sets out the questions to ask.</p>
<p>Keep the tool&rsquo;s terms with your records, so you can show what was agreed.</p>
<h2>Store and share with care</h2>
<p>Store recordings and transcripts in a secure place with limited access. Share them only with people who need them, and avoid sending them by open links that anyone can use. Consider setting an expiry date for the files, and delete them when the purpose has been met, unless a rule requires you to keep them.</p>
<p>A transcript is easy to copy, so mark it as confidential where appropriate, and think about what would happen if it were shared more widely than intended.</p>
<h2>Common mistakes</h2>
<ul>
<li>Recording before asking, or assuming that a participant has agreed by staying in the room.</li>
<li>Using a tool without reading its terms about storage and training.</li>
<li>Keeping recordings indefinitely, long after the meeting has served its purpose.</li>
<li>Sharing transcripts with people outside the meeting who were never meant to see them.</li>
<li>Forgetting that a transcript can include personal or sensitive details that were said in passing.</li>
</ul>
<h2>When to avoid recording</h2>
<p>Some meetings should not be recorded at all, such as those that discuss individual performance, health, legal advice or confidential matters that need strict control. In those cases, a short written summary, agreed by the participants, may be a better record than an automatic transcript.</p>
<h2>Keep the record of consent</h2>
<p>When consent is given, record it in a way you can show later. A written email, a message in the meeting invitation or a recorded spoken confirmation at the start all work, provided they say what was agreed. Store the record with the recording, so the two stay together and nobody has to search for the proof of consent.</p>
<p>If someone withdraws consent during the meeting, stop recording straight away, and note the time. Delete the part that was made without consent, and tell the people involved what you have done.</p>
<h2>Limits</h2>
<p>The rules on recording and transcription vary by country, sector and workplace policy, and they change over time. This post describes good practice rather than the law of any place. For a workplace policy, consult the people responsible for data protection and employment, and take advice where needed.</p>
<h2>Keep the recording clear and fair</h2>
<p>A clear recording is a fair recording, because it captures what was said rather than what the tool guessed. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the question of which tools keep audio on the device, read the <a href="/tunedzy/blog/on-device-transcription-explained">on-device transcription post</a>.</p>
''',
    faq=[('Do I need consent to record a meeting?', 'In many places, yes, from everyone present. Check the rules where you are and tell attendees before recording.'),
         ('Can I rely on the default settings of a tool?', 'Check them. Defaults may keep audio longer or use it for training.'),
         ('How long should I keep a transcript?', 'Only as long as the purpose requires, unless a rule says otherwise. Set an expiry date.'),
         ('What if someone refuses to be recorded?', 'Respect the choice and offer another way to take notes.')])

add(slug='voice-notes-to-text-workflow', cluster='trend-ai-speech', kw='voice notes to text workflow',
    title='A Voice Notes to Text Workflow for Creators and Writers',
    desc='A voice notes to text workflow for creators and writers: capture, transcribe, tag and file ideas so nothing is lost, with a simple weekly review.',
    h1='A Voice Notes to Text Workflow for Creators and Writers',
    answer='A good voice notes workflow captures ideas quickly, transcribes them while they are fresh, tags each note by project and moves the useful ideas into a working file each week. The aim is to keep the thinking that happens on the move without letting the notes pile up unread.',
    body='''
<p>Many good ideas arrive when you are not at a desk: on a walk, in a queue, in the car. A voice note captures them quickly, but voice notes have a habit of piling up unheard. A simple workflow turns them into searchable text and moves the best ideas into the work you actually do. This post sets out a routine that creators and writers can adapt to their own habits.</p>
<p>The routine has four stages: capture, transcribe, tag and review. Each one is short, and together they make the difference between a collection of audio files and a working archive.</p>
<h2>Capture quickly and simply</h2>
<p>Use one recorder app that is always available, and keep the capture step as simple as possible. Start the recording, say the idea, and stop. Do not stop to organise the file while you are walking or driving. A good habit is to say the project name at the start of each note, so the file is labelled from the beginning.</p>
<p>Keep the recording short, and split long thoughts into separate notes. Shorter notes are easier to transcribe, search and review.</p>
<h2>Transcribe while the idea is fresh</h2>
<p>Transcribe each note soon after recording, while you still remember the context. A transcript made the same day is easier to correct than one made a month later. On a phone, on-device transcription makes this quick. Check the transcript for names and technical terms, since those are where errors gather.</p>
<p>Keep the transcript with the audio, in the same folder or in the same note. That way you can listen again if a word is unclear.</p>
<h2>Tag by project and type</h2>
<p>Tag each note with the project it belongs to, and a simple type such as idea, task, quote or research. Tags make the notes searchable, and they let you see which projects are getting the most attention. Use the same tags every time. A short list of tags is more useful than a long one that nobody follows.</p>
<p>Consider a short title for each note, in plain words. Titles make the list easy to scan, and they help when you search later.</p>
<h2>Review once a week</h2>
<p>Set aside thirty minutes each week to review the notes. Move the useful ideas into the working file for each project, delete notes you no longer need and mark any idea that needs more work. The review is what stops the notes from becoming an archive nobody reads. Keep the review on the calendar, and treat it as part of the work.</p>
<p>In the review, look for patterns. A cluster of notes on one theme may be a project waiting to start.</p>
<h2>Keep the working file clean</h2>
<p>The working file should hold ideas in a form you can use: a sentence or two, the source note and the next step. Copy the important parts from the transcript into the working file, rather than leaving them buried in the audio. A clean working file is the one you return to when you start a project.</p>
<h2>Protect the privacy of your notes</h2>
<p>Voice notes can contain personal, confidential or sensitive material. Check where the audio and transcript are stored, and whether a cloud service keeps them. Use on-device tools where you can, and make sure the notes are backed up somewhere you control. The <a href="/tunedzy/blog/on-device-transcription-explained">on-device transcription post</a> covers the trade-offs.</p>
<h2>Build the habit with a trigger</h2>
<p>A workflow needs a trigger to start it, so the habit does not depend on memory. Pair the review with something you already do each week, such as a Monday coffee or the end of the working day on Friday. Put the review in the calendar as a recurring item, and treat missing it as a real cost, because the notes will pile up quickly.</p>
<p>Keep the first weeks simple. Capture and tag only, and add the transcription and the review once the capture habit feels automatic. Adding every step at once is the surest way to abandon the routine.</p>
<h2>Share ideas safely with collaborators</h2>
<p>When a collaborator needs an idea, share the working file rather than the raw audio, unless the audio is needed. A short note with the key points is easier to read and reduces the chance that private remarks reach people who were not meant to hear them. Check the sharing settings of the folder before you send anything.</p>
<p>If the audio must be shared, trim it to the relevant section and say clearly what it is. A trimmed clip is less exposing than a full voice note and easier for the collaborator to use.</p>
<h2>Limits</h2>
<p>A workflow helps only if you use it. Expect to adjust the routine after a few weeks, and drop any step that does not earn its place. Tools change, so keep the routine simple enough to survive a change of app.</p>
<h2>Turn the notes into recordings</h2>
<p>Some of the best voice notes become the start of an episode or a video. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can record voice-overs with live noise removal, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For a related habit, read the <a href="/tunedzy/blog/how-to-record-a-song-idea-on-your-phone">song idea post</a> in this series.</p>
''',
    faq=[('How long should a voice note be?', 'Short enough to transcribe and search easily. Split long thoughts into separate notes.'),
         ('Should I transcribe every note?', 'Transcribe the ones you may use. Keep the audio for the rest in case you need it later.'),
         ('How often should I review?', 'Once a week, for about thirty minutes, is enough for most people.'),
         ('What if my transcript is wrong?', 'Correct it while the context is fresh, and check names and terms in particular.')])

add(slug='ai-note-takers-privacy-checklist', cluster='trend-ai-speech', kw='ai note taker privacy',
    title='AI Note Takers and Privacy: A Checklist Before You Use One',
    desc='AI note takers and privacy: a checklist for choosing and using an AI note-taking tool, covering storage, training, access, consent and deletion.',
    h1='AI Note Takers and Privacy: A Checklist Before You Use One',
    answer='An AI note taker records or processes meetings and produces summaries. Before using one, check where audio and text are stored, whether they are used to train models, who can access them, how participants are told and how files are deleted. Choose a tool whose answers are clear and in writing.',
    body='''
<p>AI note takers have become a common feature in video calls and meeting apps. They join a call, record or process the audio, and produce a transcript and a summary. The time saved is real, but a note taker also collects a great deal of information about who said what and when. Before you use one, it is worth checking a few things carefully, because the answers differ widely between tools.</p>
<p>This checklist is for teams, teachers and individuals who want to use an AI note taker without giving away more than they intended. It is general guidance, and the rules that apply to you depend on where you are and what the meeting covers.</p>
<h2>Where is the audio processed?</h2>
<p>Find out whether the audio is processed on your device, on the provider&rsquo;s servers, or on a third party&rsquo;s servers. On-device processing keeps the raw audio closest to you, while server processing means the audio leaves your control. Read the answer in the provider&rsquo;s documentation rather than relying on a marketing phrase.</p>
<p>If the provider uses a third party for speech processing, find out who that is and where they are located. A chain of processors makes the privacy question longer and harder to answer.</p>
<h2>How long is it stored?</h2>
<p>Check how long audio, transcripts and summaries are kept, and whether you can change that period. Some tools keep files for a short time by default. Others keep them until you delete them. Set the shortest period that still meets your needs, and make sure deletion is possible.</p>
<p>Also check whether deleting a meeting removes all copies, including backups, or only the version you can see.</p>
<h2>Is it used to train models?</h2>
<p>Read whether the provider uses your audio or transcripts to improve its models, and whether you can opt out. Training use can be sensitive for meetings that contain personal or confidential information. Look for a clear statement, and for a setting that lets you turn training off.</p>
<h2>Who can access the files?</h2>
<p>Check who inside the provider can access the recordings, and under what conditions. Find out whether the files are shared with third parties, including sub-processors. A short, clear answer is a good sign. A long, vague one is a reason to look more closely.</p>
<h2>How are participants told?</h2>
<p>A note taker that joins a call should announce itself, and participants should be able to object. Check whether the tool posts a visible notice, and whether it can be turned off for a specific meeting. Consent is the basis for most recordings, so the tool should make it easy to obtain.</p>
<h2>What about the summaries?</h2>
<p>Summaries can distort what was said, and they can include details that were never meant to be recorded. Review each summary before sharing it, and check it against the transcript where the content matters. A summary is a draft, not an official record.</p>
<h2>Can you export and delete?</h2>
<p>Check that you can export your data in a usable form, and that you can delete it on request. A tool that locks your files in its own system makes it hard to leave or to meet a deletion request. Test the export and the deletion on a short, unimportant meeting before relying on them.</p>
<h2>A short decision</h2>
<ol>
<li>Choose a tool where the answers to these questions are clear and written down.</li>
<li>Turn off training use if the setting exists and the meetings are sensitive.</li>
<li>Set a short storage period, and test deletion.</li>
<li>Tell participants before each recording, and offer a way to opt out.</li>
<li>Review summaries before sharing, and keep the tool&rsquo;s terms with your records.</li>
</ol>
<h2>Ask for a written data processing description</h2>
<p>If your organisation is considering a note taker for regular use, ask the provider for a written description of how data is processed, stored and deleted. A short document that covers these points is more useful than a sales conversation, and it gives your data protection and legal colleagues something to review. Keep the description with the approval record.</p>
<p>Review the description again when the provider changes its terms or adds a feature. A feature added in an update can change what happens to the audio, even when the core product stays the same.</p>
<h2>Limits</h2>
<p>Terms and settings change, and the answers you find today may not hold later. This checklist does not replace reading the current terms or taking advice on a specific case, especially where personal data or regulated information is involved.</p>
<h2>Keep your own recordings clear</h2>
<p>Whatever tool you use, a clear recording gives a more accurate summary. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the wider question of what happens to audio on a device, read the <a href="/tunedzy/blog/on-device-transcription-explained">on-device transcription post</a>.</p>
''',
    faq=[('Should I use an AI note taker for every meeting?', 'No. Use it where the benefit is clear and the privacy answers are satisfactory.'),
         ('Can I turn off training use?', 'Some tools allow it. Check the settings and the terms, and turn it off for sensitive meetings.'),
         ('What if a participant objects?', 'Respect the objection and switch the note taker off for that meeting.'),
         ('Is a summary a reliable record?', 'Treat it as a draft. Check it against the transcript before sharing.')])

add(slug='what-is-word-error-rate', cluster='trend-ai-speech', kw='what is word error rate',
    title='What Is Word Error Rate and How to Use It Without Being Misled',
    desc='What word error rate means: how it is calculated, why a single score can mislead, how to compare transcription tools fairly and how to test one on your own audio.',
    h1='What Is Word Error Rate and How to Use It Without Being Misled',
    answer='Word error rate is the share of words in a transcript that are wrong, counting substitutions, deletions and insertions against a reference. It is useful for comparing tools on the same audio, but a single score hides which errors matter. Test on your own recordings and check the errors that affect meaning.',
    body='''
<p>Word error rate, usually written as WER, is the most common way transcription accuracy is measured. It appears in research papers, product announcements and comparison charts. It is a useful measure, but it is easy to misread. A single percentage can hide the errors that matter most to you, and a tool that scores well on one kind of audio may do poorly on another.</p>
<p>This post explains what WER counts, why it can mislead, how to compare tools fairly and how to test a tool on your own material. It is written for creators, editors and anyone choosing a transcription tool.</p>
<h2>How the measure works</h2>
<p>WER compares a transcript with a reference transcript, which is a checked version of what was said. It counts the words that have been substituted, deleted or inserted, adds those up and divides by the number of words in the reference. A lower score means fewer errors. The measure is simple to calculate, which is one reason it is so widely used.</p>
<p>The result depends entirely on the reference. A careless reference, or one that treats spelling and punctuation differently, can change the score.</p>
<h2>Why a single score misleads</h2>
<p>A WER figure treats every error as equal. A missed filler word counts the same as a wrong name, a wrong number or a reversed negative. For a creator, the errors that change meaning are far more serious than the ones that do not. Two tools with the same WER may produce very different transcripts for your purposes.</p>
<p>The audio also matters. A score measured on clean studio speech may not hold for a noisy phone recording, a fast-talking panel or a speaker with a strong accent. Scores quoted by vendors often come from test sets that do not match your work.</p>
<h2>Errors that change meaning</h2>
<p>Some errors are more harmful than others. A negative that is dropped (&ldquo;did not&rdquo; becoming &ldquo;did&rdquo;) reverses a claim. A number that changes (&ldquo;fifteen&rdquo; becoming &ldquo;fifty&rdquo;) misleads. A name that is wrong damages trust. When you check a transcript, look first for these high-impact errors, not for the total score.</p>
<h2>How to compare tools fairly</h2>
<ol>
<li>Use the same audio for every tool, ideally a few minutes of your own recording.</li>
<li>Create a careful reference transcript, checked by a person who listens closely.</li>
<li>Count the errors by type, and note which ones change meaning.</li>
<li>Compare the time you spend correcting each transcript, not only the score.</li>
<li>Repeat the test on a second recording with different conditions, such as a noisier room.</li>
</ol>
<h2>What the score is good for</h2>
<p>WER is useful for a rough comparison of tools on the same material, and for tracking whether a tool improves over time on your own audio. Use it as one measure among several. The time it takes to fix a transcript is often the most practical measure of all.</p>
<h2>Why vendor scores need care</h2>
<p>Vendors choose test sets, references and conditions that show their product well. A score from a vendor is a claim to be tested, not a fact to rely on. Ask what audio was used, how the reference was made and whether the test matches your work. An independent test on similar audio is more useful than any headline figure.</p>
<h2>Use the score to track your own progress</h2>
<p>A score is most useful over time, on your own audio. If you run the same short test each month, with the same recording and the same reference, you can see whether a tool, a setting or your own recording habits are improving the result. Keep the reference transcript and the test file in a folder, so the comparison stays honest.</p>
<p>A small change in the score is not always meaningful, especially on a short recording. Look for consistent movement across several tests before drawing a conclusion.</p>
<h2>Explain the score to a non-specialist</h2>
<p>When you report a transcription score to a client, a colleague or a funder, explain what it counts and what it does not. A plain statement, such as &ldquo;about one word in twenty was wrong, and most of the errors were filler words&rdquo;, is more honest and more useful than a percentage on its own. The people who read the report need the meaning, not only the number.</p>
<h2>Limits</h2>
<p>WER does not capture meaning, tone, timing or the usefulness of a transcript to a particular reader. Two transcripts with the same score can read very differently. Use WER as a starting point, and judge the transcript on what it does for your work.</p>
<h2>Start with a clean recording</h2>
<p>A clean recording lowers the error rate for any tool, which makes comparisons easier to trust. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the practical side of checking a transcript, read the <a href="/tunedzy/blog/how-accurate-is-ai-transcription-for-interviews">interview accuracy post</a> in this series.</p>
''',
    faq=[('Is a lower word error rate always better?', 'Usually, but only on similar audio. Check the errors that change meaning as well.'),
         ('How do I calculate it myself?', 'Compare your transcript with a careful reference, count the substitutions, deletions and insertions, and divide by the reference words.'),
         ('Why do vendor scores differ so much?', 'They use different test sets, references and conditions. Compare on your own audio.'),
         ('Which errors matter most?', 'Errors that reverse a claim, change a number or get a name wrong, because they mislead the reader.')])

add(slug='how-background-noise-affects-speech-recognition', cluster='trend-ai-speech', kw='background noise speech recognition',
    title='How Background Noise Affects Speech Recognition and What to Do',
    desc='How background noise affects speech recognition: why steady noise, overlapping voices and reverb cause errors, and the practical steps that improve a transcript.',
    h1='How Background Noise Affects Speech Recognition and What to Do',
    answer='Background noise makes speech recognition worse because the model has to separate the voice from the noise before it can read the words. Steady noise, overlapping voices and echo each cause different errors. Improve the recording with a closer microphone and a quieter room, and clean lightly before transcribing.',
    body='''
<p>Ask a speech recognition tool to transcribe a clean studio recording and the result is usually strong. Ask it to transcribe a recording made in a busy café, on a windy street or in a room with an air conditioner, and the errors multiply. The reason is that the model has to separate the speech from everything else before it can read the words, and the separation is never perfect.</p>
<p>This post explains how different kinds of noise cause different errors, what you can do to improve the recording and when cleaning helps more than it hurts. The advice applies to automatic transcripts, live captions and any tool that works from sound.</p>
<h2>Steady noise</h2>
<p>A steady sound, such as a fan, a fridge or a hum, is one of the easier problems for a model to handle, because it stays the same from moment to moment. Even so, steady noise lowers the clarity of the speech, and quieter consonants become harder to hear. The model may drop soft sounds or confuse similar words, especially in the quiet parts of the recording.</p>
<p>Reducing steady noise at the source, by switching off the fan or moving the microphone, is the most effective fix. A light cleanup afterwards can help further, but a heavy one can remove the speech along with the noise.</p>
<h2>Overlapping voices</h2>
<p>When two or more people talk at once, the model has to decide which words belong to which speaker, and it often fails. Crosstalk produces errors that are harder to fix than steady noise, because the sounds genuinely overlap. A single microphone shared by several speakers makes the problem worse.</p>
<p>The best fix is one microphone per speaker, placed at a steady distance. Where that is not possible, ask speakers to take turns, and expect more correction in the transcript.</p>
<h2>Echo and reverb</h2>
<p>Echo smears the speech over time, so each sound lingers and blurs into the next. A model can struggle to decide where one word ends and another begins. Echo is often caused by a hard room, and it can be reduced by moving the microphone closer and adding soft surfaces around the speaker. The <a href="/tunedzy/how-to-test-your-room-for-echo">clap test</a> helps you find a room that sounds dry.</p>
<h2>Sudden noises</h2>
<p>A door slam, a cough or a passing siren can cause a short burst of errors. The model may misread the words around the sound, or insert text where there was none. Note these moments when you check the transcript, and consider re-recording a short section if the sound covered an important line.</p>
<h2>Distance and level</h2>
<p>The further the microphone is from the speaker, the more room sound and noise it picks up relative to the voice. A quiet speaker at a distance can be the worst case. Move the microphone closer, and check the level so the voice is clear without clipping. A good level helps more than most cleanup.</p>
<h2>What to do</h2>
<ol>
<li>Record in the quietest room you can, and switch off steady noise sources.</li>
<li>Place each microphone close to its speaker, at a steady distance.</li>
<li>Check the level, keeping the peaks well below the top.</li>
<li>Clean lightly, if at all, before transcribing, and listen to the result.</li>
<li>Check the transcript most carefully in the parts where the noise was loudest.</li>
</ol>
<h2>When cleaning helps and when it hurts</h2>
<p>Light cleanup can improve a transcript when the noise is steady and the voice is clear. Heavy cleanup can make speech watery and remove the soft sounds that the model needs. Compare a transcript made from the original with one made from the cleaned version, and keep the one that is more accurate. Do not assume that cleaner audio always gives a better transcript.</p>
<h2>Test the setup before a long recording</h2>
<p>Before a long interview or a live session, record a short test in the actual room with the actual microphones. Transcribe it, read the result, and look for the errors that matter most. If the test transcript is poor, the setup is the problem, and no tool will fix it later. Change the position, the level or the room, and repeat the test until the transcript is usable.</p>
<p>Keep a note of the setup that worked. Recording the microphone, the distance, the room and the level gives you a template for the next session.</p>
<h2>Limits</h2>
<p>Noise will always make transcription harder, and no tool can fully overcome a poor recording. Results vary between models, languages and accents. Test on your own material, and treat the transcript as a draft that needs checking.</p>
<h2>Start with a clean signal</h2>
<p>A clean signal is the best help a model can have. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording. For how transcription errors are measured, read the <a href="/tunedzy/blog/what-is-word-error-rate">word error rate post</a> in this series.</p>
''',
    faq=[('Does noise cancellation always improve transcripts?', 'Not always. Heavy cleanup can make speech harder to recognise. Compare the results.'),
         ('What is the worst kind of noise for transcription?', 'Overlapping voices and echo are often the hardest, because the sounds genuinely mix.'),
         ('Should I re-record a noisy section?', 'If the noise covered an important line, yes. Re-record a short section rather than trying to fix it.'),
         ('Does distance matter?', 'Yes. A microphone close to the speaker gives a much clearer signal than one at a distance.')])
