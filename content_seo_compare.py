"""Comparison and alternatives pages (25 October 2026). Same shape as content.GUIDES; merged in content.py.

Rules: name the competitor fairly and say where it is the better choice. No prices or limits in the copy: those change, so each page
sends the reader to the vendor's own page. Facts were checked against the vendors' public material and reviews on 25 October 2026.
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


add('tunedzy-vs-adobe-podcast-enhance', 'mic', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Tunedzy vs Adobe Podcast Enhance Speech: Which Cleans a Voice Better',
    desc='Adobe Podcast Enhance Speech against Tunedzy: where the browser tool is quick, where Tunedzy runs on your own PC, and which one to pick for your recording.',
    h1='Tunedzy vs Adobe Podcast Enhance Speech',
    kw='adobe podcast enhance speech alternative',
    lead='Adobe Podcast Enhance Speech is a fast, one-click way to improve speech in your browser. Tunedzy does the same job on your own computer and adds editing, mixing and loudness work around it.',
    tldr=['Adobe Podcast is quick and simple for one file at a time, in your browser.',
          'Tunedzy runs on your own PC, so the recording is not uploaded, and it adds editing, a multitrack mix and loudness control.',
          'Adobe Podcast has free-tier limits that third-party reviews describe as daily caps; check Adobe&rsquo;s page for today&rsquo;s terms.',
          'If you need one quick clean of a short file and you are happy to upload it, Adobe is a fine choice.'],
    body='''
<h2>What each one does</h2>
<p>Adobe Podcast Enhance Speech takes a recording, removes noise and makes the speech sound closer to a recording made in a better room. You upload the file to Adobe&rsquo;s service and download the result. It is designed for speech, and it is a single step.</p>
<p>Tunedzy&rsquo;s Perfect it is also a single step for speech, but it runs on your own PC or phone. Before the noise step it repairs clipping, clicks and hum, then it levels the voice and sets the tone. The result is the start of a finished track rather than the end of one.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>Adobe Podcast Enhance Speech</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Where it runs</td><td>In your browser; the audio is uploaded to Adobe for processing</td><td>On your Windows PC or your phone; nothing is uploaded</td></tr>
<tr><td>Speech cleanup</td><td>Yes, one click</td><td>Yes: repair, studio sound, level and tone in Perfect it</td></tr>
<tr><td>Editing</td><td>Not its job</td><td>Edit by words, cut pauses, multitrack, fades</td></tr>
<tr><td>Loudness control</td><td>Not its job</td><td>Match loudness to podcast, online video and other targets, with a true peak check</td></tr>
<tr><td>Free use</td><td>A free tier with limits (check Adobe&rsquo;s page)</td><td>Free: Tunedzy Go on the phone; free credits in the first month of the Windows app</td></tr>
</tbody></table>
<h2>When Adobe Podcast is the better pick</h2>
<ul>
<li>You have one short file, you want a result in a minute, and you are comfortable uploading it.</li>
<li>You do not need to edit, mix or set loudness; you only want the voice cleaned.</li>
<li>You work in a browser on a machine you cannot install software on.</li>
</ul>
<h2>When Tunedzy is the better pick</h2>
<ul>
<li>The recording is private (an interview, a client, unreleased music) and should stay on your device.</li>
<li>You will cut, reorder and mix several voices or a voice with music.</li>
<li>You need the level and the true peak checked for a platform, or the sound put back into a video.</li>
</ul>
<p>Adobe&rsquo;s free tier and its features change, so check the live page before you choose. This page was written from public information on 25 October 2026.</p>
''',
    vf_title='Clean it on your own device',
    vf='<p>Try Perfect it on your own recording: on your PC in the Windows app, or on your phone in Tunedzy Go for free.</p>',
    faq=[('Is Adobe Podcast Enhance Speech free?', 'Adobe offers a free tier with limits. Check Adobe&rsquo;s page for the current terms.'),
         ('Does Tunedzy upload my audio?', 'No. Tunedzy processes files on your PC or phone. Its credit server only counts use; it does not receive your audio.'),
         ('Which one sounds better?', 'Test both on the same recording and pick by ear. Both can over-process a voice if pushed; the Before and After comparison is the test that matters.')],
    related=['voice-cleaner-alternatives', 'clean-up-a-phone-voice-recording', 'remove-background-noise-from-a-voice-recording'])

add('tunedzy-vs-dolby-on', 'mic-wide', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='Tunedzy vs Dolby On: Recording on Your Phone and Cleaning Afterwards',
    desc='Dolby On records and processes audio on your phone as you capture it. Tunedzy cleans, edits and mixes what you recorded. Here is how to choose between them or use both.',
    h1='Tunedzy vs Dolby On',
    kw='dolby on alternative',
    lead='Dolby On is a phone app for capturing better audio and video in the moment. Tunedzy is for cleaning, editing and mixing the recording afterwards. They solve different steps, and they can work together.',
    tldr=['Dolby On is built for recording: it processes the sound as you capture it and can live-stream.',
          'Tunedzy is built for after the recording: repair, studio sound, editing by words, multitrack and loudness, on your own PC or phone.',
          'Use Dolby On to capture a good take, then Tunedzy to finish it.',
          'If you need one app for the whole job on a phone, check which steps you actually use.'],
    body='''
<h2>What Dolby On is for</h2>
<p>Dolby On is a recording app for phones. Its processing reduces background noise, levels the sound, adds some stereo width and offers a few presets, and it has an option to compare with the unprocessed sound. Its App Store listing also highlights lossless recording, live streaming on iOS and a simple trim editor. Check the store listing for the current feature set, because the app changes.</p>
<h2>What Tunedzy is for</h2>
<p>Tunedzy starts after the recording. Perfect it repairs clipping, clicks and hum, runs a studio sound model on the recording, then levels and tones the voice. Transcripts let you edit by the words and remove ums and pauses. Multitrack mixes several voices with music and exports at a loudness target. On the phone, Tunedzy Go cleans recordings and files for free.</p>
<h2>Which one for which step</h2>
<table>
<thead><tr><th>Step</th><th>Dolby On</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Capture a good take</td><td>Yes, the core job</td><td>Tunedzy Go records and cleans, but a dedicated recorder is the better capture tool</td></tr>
<tr><td>Live streaming</td><td>Yes (iOS listing)</td><td>Not its job; Live Studio on Windows cleans the mic for a stream</td></tr>
<tr><td>Cleanup of a file</td><td>Processing as you record</td><td>Repair, studio sound, level, tone</td></tr>
<tr><td>Editing and mixing</td><td>A trim editor</td><td>Transcript editing, multitrack, fades, ducking</td></tr>
<tr><td>Loudness to a platform</td><td>Leveling as you record</td><td>Target loudness with a true peak check</td></tr>
</tbody></table>
<h2>The combination that works</h2>
<p>Record the take with the recorder you like and a quiet room. Then clean and finish it in Tunedzy, on the phone with Tunedzy Go or on the PC in the Windows app. Keep the original recording as well, so you can go back if a step sounds wrong.</p>
<p>Dolby On&rsquo;s features and platform support change. Check the App Store or Google Play listing for the current version.</p>
''',
    vf_title='Capture with any recorder, finish in Tunedzy',
    vf='<p>Record with any app you like, then open the file in Tunedzy Go on your phone for a free cleanup.</p>',
    faq=[('Is Dolby On better for recording?', 'For capturing the take in the moment, Dolby On is built for that job. Tunedzy is for what happens after.'),
         ('Can Tunedzy record too?', 'Tunedzy Go records and cleans on your phone. The Windows app has a recorder and a live microphone cleaner. A dedicated recording app may suit capture better.'),
         ('Does Dolby On edit audio?', 'Only lightly, with a trim tool. For transcripts, multitrack mixing and loudness targets you need an editing tool, such as Tunedzy.')],
    related=['voice-cleaner-alternatives', 'record-a-voiceover-on-your-phone', 'voice-note-sounds-better-on-an-iphone'])

add('tunedzy-vs-descript', 'desk', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='Tunedzy vs Descript: Editing a Podcast by Words',
    desc='Descript and Tunedzy both edit speech by its transcript. Here is where each is stronger: video and collaboration against offline cleanup, mixing and loudness.',
    h1='Tunedzy vs Descript',
    kw='descript alternative podcast editing',
    lead='Descript edits audio and video through a transcript, and it is strong for video and shared work. Tunedzy edits by transcript too, on your own computer, and adds the cleanup, mixing and loudness work.',
    tldr=['Descript is a cloud-based editor for audio and video, with transcript editing and filler-word removal.',
          'Tunedzy keeps the transcript and the files on your PC, and adds repair, studio sound and loudness targets.',
          'Descript is the stronger choice for video editing and for working with a team.',
          'Tunedzy is the stronger choice for offline work, private recordings and loudness control.'],
    body='''
<h2>Where Descript is strong</h2>
<p>Descript is built around the transcript: you edit the words and the picture and sound follow. It is a strong choice for video, for overdubbing, and for sharing a project with other people. It is a cloud service with paid plans, so check its current pricing and limits on its site before you choose.</p>
<h2>Where Tunedzy is strong</h2>
<p>Tunedzy edits by transcript on your own PC. The transcript is made with a speech model that runs on the computer, so the recording is not uploaded. You can cut words, remove ums, shorten pauses, export captions and then go on to the cleanup: repair, studio sound and a level set to a loudness target with a true peak check. It is a Windows app for now.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>Descript</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Edit by transcript</td><td>Yes, its core feature</td><td>Yes: cut words, filler removal, pause shortening</td></tr>
<tr><td>Video editing</td><td>Strong</td><td>Replaces the sound in a video; not a video editor</td></tr>
<tr><td>Where the work happens</td><td>Cloud service</td><td>Your PC (Windows) or phone (Tunedzy Go)</td></tr>
<tr><td>Speech cleanup</td><td>Included, with its own tools</td><td>Repair, studio sound, level and tone</td></tr>
<tr><td>Loudness to a target</td><td>Not its focus</td><td>Match loudness with true peak</td></tr>
<tr><td>Teamwork</td><td>Strong</td><td>Single user</td></tr>
</tbody></table>
<h2>Which to pick</h2>
<p>Pick Descript when your work is video and a team. Pick Tunedzy when the recording is private, when you need offline work, or when the loudness and cleanup matter more than the video.</p>
<p>Both products change often. Check each vendor&rsquo;s site for current features before you decide.</p>
''',
    vf_title='Edit the words on your own PC',
    vf='<p>Transcribe, cut and clean a recording on your computer. Nothing is uploaded.</p>',
    faq=[('Is Tunedzy a Descript replacement?', 'For podcast and voice editing that you do offline, yes. For video and team work, Descript is the stronger tool.'),
         ('Does Tunedzy remove filler words?', 'Yes. It finds ums and uhs in the transcript and lets you remove them. Check each cut by ear.'),
         ('Is my audio uploaded to Tunedzy?', 'No. The transcript and the files are on your PC. The credit server counts use only.')],
    related=['edit-a-podcast-by-its-words', 'voice-cleaner-alternatives', 'podcast-sound-professional-on-a-budget'])

add('tunedzy-vs-audacity', 'mic', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='Tunedzy vs Audacity: Free Editing or Automatic Cleanup',
    desc='Audacity is a free, manual audio editor. Tunedzy is an automatic cleanup and mixing studio. Here is what each does well and which one to start with.',
    h1='Tunedzy vs Audacity',
    kw='audacity alternative voice cleanup',
    lead='Audacity is free and gives you full manual control over every edit. Tunedzy does more of the cleanup automatically. For many people the right answer is to learn one basic Audacity skill and use Tunedzy for the rest.',
    tldr=['Audacity is free, open source and manual: you choose each noise profile, cut and setting.',
          'Tunedzy automates the repair, the studio sound and the loudness target, and reports what it did.',
          'Audacity is better for precise manual editing and for learning how audio works.',
          'Tunedzy is faster for a voice that needs a standard cleanup and a loudness target.'],
    body='''
<h2>What Audacity does well</h2>
<p>Audacity is a free editor that runs on Windows, macOS and Linux. Its noise reduction works from a noise profile you take from a quiet part of the recording. It is good for precise cuts, fades, and learning what each effect does. Its manual is the reference for every setting.</p>
<h2>What Tunedzy does well</h2>
<p>Tunedzy analyses the recording first and then runs the steps it finds are needed: clipping, clicks, hum and DC offset, then studio sound, then level and tone. It reports what it changed, and you can compare with the original. Its transcript, multitrack and loudness tools cover jobs Audacity does not automate. Tunedzy is a Windows app and a phone app; Audacity is a desktop app.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>Audacity</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Price</td><td>Free</td><td>Free on the phone; credits on the Windows app, with free credits in your first month</td></tr>
<tr><td>Noise removal</td><td>Manual, from a noise profile</td><td>Automatic studio sound, with a reduction you choose</td></tr>
<tr><td>Manual editing</td><td>Full control</td><td>Basic cuts, fades and multitrack</td></tr>
<tr><td>Loudness</td><td>Manual measurement</td><td>Match loudness to a target, true peak checked</td></tr>
<tr><td>Transcripts</td><td>None built in</td><td>Edit by words; captions</td></tr>
</tbody></table>
<h2>Which to start with</h2>
<p>If you want to learn how each step works, start with Audacity. If you want a good voice in less time, start with Tunedzy. Many people use both: Audacity for a precise fix, Tunedzy for the cleanup and the loudness.</p>
''',
    vf_title='Automatic first, manual when you need it',
    vf='<p>Run Perfect it on the recording, compare with the original, then open the result in your editor for any manual fix.</p>',
    faq=[('Is Audacity good enough for podcasts?', 'Yes, for a single voice with manual cleanup. For several voices with a loudness target, an automatic tool saves time.'),
         ('Is Tunedzy free?', 'The phone app is free. The Windows app uses credits, with free credits in the first month and more for purchase.'),
         ('Which one removes noise better?', 'It depends on the recording. Test both on the same file and listen; a careful manual noise profile can beat an automatic step, and the other way round too.')],
    related=['remove-background-noise-from-a-voice-recording', 'voice-cleaner-alternatives', 'remove-hum-from-audio'])

add('tunedzy-vs-auphonic', 'desk-wide', ['lufs-meter', 'vocal-checker'],
    title='Tunedzy vs Auphonic: Podcast Post-Production Compared',
    desc='Auphonic is an online and desktop post-production service for podcasts. Tunedzy does the same kind of work offline. Compare levelling, loudness and where your audio goes.',
    h1='Tunedzy vs Auphonic',
    kw='auphonic alternative podcast',
    lead='Auphonic is a well-known post-production service for podcasts: it levels speakers, normalises loudness and reduces noise. Tunedzy does the same kind of work offline, with transcripts and a multitrack mix added.',
    tldr=['Auphonic is a web service for podcast post-production, with a leveller for speakers and loudness targets.',
          'Auphonic processes your uploaded files on its servers; Tunedzy processes them on your computer.',
          'Tunedzy adds the transcript editor, a multitrack mix and the video sound replacement.',
          'Auphonic is the stronger choice for batch processing many episodes on a web workflow.'],
    body='''
<h2>What Auphonic does</h2>
<p>Auphonic is built for podcast post-production. Its official help describes an adaptive leveller that sorts audio into speech, music and background, evens out quieter speakers, and applies a true peak limiter and common loudness targets. It also has a desktop batch processor with the leveller and noise and hum reduction, and it can process several files at once.</p>
<h2>What Tunedzy does</h2>
<p>Tunedzy does cleanup and loudness on your own PC or phone. Perfect it repairs clipping, clicks and hum, runs studio sound and sets the level and tone. Multitrack levels and mixes several voices and music, and exports at a target loudness with a true peak check. Transcripts let you edit the episode by its words.</p>
<h2>The big difference: where the audio goes</h2>
<p>Auphonic is a service: your files are uploaded and processed on its servers. Tunedzy processes files on your device, and the transcript and the mix stay with you. If your recordings are private or under contract, that difference matters more than any feature.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>Auphonic</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Where it runs</td><td>Its servers (web) and a desktop batch tool</td><td>Your PC (Windows) and phone (Tunedzy Go)</td></tr>
<tr><td>Speaker levelling</td><td>Adaptive leveller</td><td>Match loudness per clip; set each voice in Multitrack</td></tr>
<tr><td>Loudness targets</td><td>Standard targets and presets</td><td>Presets for podcast, online video, audiobooks and broadcast</td></tr>
<tr><td>Transcript editing</td><td>Not its focus</td><td>Edit by words, captions</td></tr>
<tr><td>Multitrack mix</td><td>Not its focus</td><td>Tracks, fades, ducking</td></tr>
</tbody></table>
<h2>Which to pick</h2>
<p>Pick Auphonic for a batch of episodes through a web workflow and its leveller. Pick Tunedzy when the files must stay on your device, or when you want the transcript, the mix and the cleanup in one app. Check Auphonic&rsquo;s own site for its current plans and terms.</p>
''',
    vf_title='Finish the episode on your own device',
    vf='<p>Clean, level and export an episode in Tunedzy. The files stay on your computer.</p>',
    faq=[('Does Auphonic keep my files?', 'Check Auphonic&rsquo;s privacy terms and its retention policy; a web service handles uploads on its own servers.'),
         ('Does Tunedzy have a leveller like Auphonic?', 'Tunedzy levels each clip to a target and lets you set each voice in Multitrack, rather than an automatic speaker leveller. For many episodes, set each voice by hand once.'),
         ('Which is better for many episodes?', 'For a batch on a web workflow, Auphonic. For an offline workflow with editing, Tunedzy.')],
    related=['podcast-sound-professional-on-a-budget', 'loudness-for-youtube-podcasts-and-spotify', 'voice-cleaner-alternatives'])

add('voice-cleaner-alternatives', 'desk', ['voice-recorder-noise-cancellation', 'clean-streaming-mic', 'vocal-checker'],
    title='Voice Cleaner Alternatives: Free, Browser, Desktop and Phone Options',
    desc='An honest map of voice cleaners: free editors, browser tools, phone recorders, AI editors and Tunedzy, with what each is best at and where privacy matters.',
    h1='Voice Cleaner Alternatives',
    kw='voice cleaner alternatives',
    lead='There is no single best voice cleaner. The right one depends on how many files you have, whether they are private, and whether you need editing or only a clean voice.',
    tldr=['Free editors (Audacity, and GarageBand on Apple devices) give manual control.',
          'Browser tools are the quickest for one file, but the file is uploaded to the service.',
          'Phone recorders capture better audio; they rarely clean a file afterwards.',
          'Tunedzy covers cleanup, editing, multitrack and loudness on your own device, with a free phone app.'],
    body='''
<h2>If you want free and manual</h2>
<p>Audacity is the standard free editor. It needs a few minutes to learn the noise profile and the reduction setting, and then it does a good job on steady noise. <a href="/tunedzy/tunedzy-vs-audacity">Our comparison</a> covers the trade-offs. On Apple devices, GarageBand is free and has voice tools for recordings made in it.</p>
<h2>If you want one file cleaned quickly</h2>
<p>Browser tools such as Adobe Podcast Enhance Speech are fast and simple. The file is uploaded to the service for processing, and free use has limits. <a href="/tunedzy/tunedzy-vs-adobe-podcast-enhance">See the comparison</a>.</p>
<h2>If you record on the phone</h2>
<p>Use a good recorder and a quiet room; the capture matters most. Dolby On is built for capturing audio on a phone with processing as you record. <a href="/tunedzy/tunedzy-vs-dolby-on">See how it compares with Tunedzy</a>.</p>
<h2>If you edit by words</h2>
<p>Descript is a strong editor for transcripts, and it includes video. It is a cloud service. <a href="/tunedzy/tunedzy-vs-descript">Compare the two</a>.</p>
<h2>If you run many episodes</h2>
<p>Auphonic is a post-production service for podcasts, with a leveller and loudness targets. It processes files on its servers. <a href="/tunedzy/tunedzy-vs-auphonic">Compare the two</a>.</p>
<h2>If the files are private, or you want one app</h2>
<p>Tunedzy runs on your PC and your phone. Perfect it cleans a voice, the transcript edits by words, Multitrack mixes voices and music, and the loudness is set to a target with a true peak check. Tunedzy Go does the cleanup on your phone for free.</p>
<h2>Privacy in one line</h2>
<p>Browser and cloud tools receive your audio. Read each service&rsquo;s privacy terms before you upload a private or unreleased recording.</p>
''',
    vf_title='Try the one that fits your file',
    vf='<p>Start with Tunedzy Go on your phone for free, or the Windows app for the full studio.</p>',
    faq=[('What is the best free voice cleaner?', 'For manual control, Audacity. For a quick browser result, a free browser tool, with its limits. For private recordings on a phone, Tunedzy Go is free and stays on your device.'),
         ('Are AI voice cleaners safe to use?', 'They are a processing step like any other. They can over-process a voice, so keep the original and check the result by ear. Privacy depends on whether the audio leaves your device.'),
         ('Which should a beginner use?', 'Start with a quiet room and a good distance, then try Tunedzy Go or a free editor on one file. Learn one tool well before adding another.')],
    related=['tunedzy-vs-audacity', 'tunedzy-vs-adobe-podcast-enhance', 'clean-up-a-phone-voice-recording'])
