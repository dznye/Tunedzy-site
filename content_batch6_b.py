"""Batch 6b (25 October 2026): twelve competitor 'alternative' pages and thirteen Tunedzy feature pages.

Alternative pages describe the competitor fairly, say where it is the better choice, and say where Tunedzy fits. Feature pages describe
one real Tunedzy feature, checked against the app. No prices, ratings or benchmarks are quoted.

GROUP_OF marks 'alternative' or 'feature' for the guides hub.
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


# ----------------------------------------------------------------------------------- alternatives
add('lalal-ai-alternative', 'alternative', 'neon', ['song-key-finder', 'vocal-checker'],
    title='LALAL.AI Alternative: Separate Vocals on Your Own PC',
    desc='Looking for a LALAL.AI alternative? Compare a browser separator with an on-device vocal remover, and see where each one fits your song.',
    h1='A LALAL.AI Alternative',
    kw='lalal ai alternative',
    lead='LALAL.AI is a dedicated separation service that runs in the browser and offers several stem options. If you want the separation to stay on your own computer, or you need the voice finished afterwards, Tunedzy is a different route.',
    tldr=['LALAL.AI is a browser service, so the file is uploaded.',
          'Tunedzy has a vocal remover in the Windows app, and it runs on your PC.',
          'For more stems from one service, LALAL.AI is the stronger fit.',
          'For a private song and a finished voice, Tunedzy fits better.'],
    body='''
<h2>What LALAL.AI is good at</h2>
<p>LALAL.AI is a dedicated separation tool. Its own material describes several stems and a voice cleaning option, and it works from any browser. For a quick separation of a single song with several stems, it is an easy choice.</p>
<h2>Where it is different from Tunedzy</h2>
<p>A browser service receives your file. Tunedzy separates a vocal on your PC, so an unreleased song does not leave the machine. Tunedzy also cleans, levels and mixes the voice afterwards, in the same app.</p>
<h2>Which to pick</h2>
<p>Choose LALAL.AI when you want a fast online separation with several stems and do not mind uploading. Choose Tunedzy when the song is private, or when you want the separated voice cleaned and mixed in one place. The <a href="/tunedzy/best-vocal-remover-apps">vocal remover roundup</a> compares the field.</p>
''',
    vf_title='Separate on your PC, finish the voice',
    vf='<p>Tunedzy separates the vocal on your PC, then cleans, levels and mixes it in the same app.</p>',
    faq=[('Is Tunedzy a free LALAL.AI replacement?', 'It is a different tool. Tunedzy separates on your PC and finishes the voice; check its credits for the Windows app.'),
         ('Does LALAL.AI keep uploaded files?', 'Check its privacy terms. An online service receives the file.'),
         ('Which gives more stems?', 'Check each tool. LALAL.AI describes several stem options in its material.')],
    related=['best-vocal-remover-apps', 'best-ai-stem-splitter', 'how-to-isolate-a-voice-from-background-music'])

add('moises-alternative', 'alternative', 'hero-wide', ['song-key-finder', 'bpm-finder'],
    title='Moises Alternative for Musicians and Vocal Separation',
    desc='Looking for a Moises alternative? Compare a musician practice app with an on-device vocal remover and voice finisher, and choose by what you need.',
    h1='A Moises Alternative',
    kw='moises alternative',
    lead='Moises is built around musicians: separation plus practice features such as tempo change and muting parts, and a mobile app. Tunedzy is a voice finisher with a vocal remover, not a practice app.',
    tldr=['Moises combines separation with practice tools such as tempo change.',
          'Tunedzy separates a vocal on your PC and finishes the voice.',
          'For practice features and a phone app, Moises is the better fit.',
          'For a private song and a clean, mixed voice, Tunedzy fits better.'],
    body='''
<h2>What Moises is good at</h2>
<p>Moises is for musicians. It separates songs and adds practice tools: changing tempo, muting parts to play along, and a mobile app. Check its current plans on its site.</p>
<h2>Where Tunedzy differs</h2>
<p>Tunedzy is not a practice app. It has a vocal remover and a stem mixer in the Windows app, and it works on your PC. Its main job is the voice: repair, cleanup, editing by transcript, Multitrack and loudness targets.</p>
<h2>Which to pick</h2>
<p>For practising a song with tempo and muting, Moises. For a private song to separate and a voice to finish, Tunedzy. The <a href="/tunedzy/how-to-isolate-a-voice-from-background-music">voice isolation guide</a> shows the method and its rights caveat.</p>
''',
    vf_title='Separate the song, finish the voice',
    vf='<p>Tunedzy separates a song on your PC and finishes the voice in the same app.</p>',
    faq=[('Does Tunedzy have practice features?', 'Not like Moises. Use it for a separated vocal and a finished voice.'),
         ('Is there a phone app?', 'Tunedzy Go is a free phone app for cleaning recordings. It is not a practice app.'),
         ('Which is cheaper?', 'Check both sites for current plans. Tunedzy credits apply to the Windows app.')],
    related=['best-vocal-remover-apps', 'best-karaoke-maker-app', 'how-to-make-a-karaoke-track-from-a-song'])

add('uvr-alternative', 'alternative', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='UVR Alternative: Free Vocal Removers With Less Setup',
    desc='Looking for a UVR alternative? Compare a free desktop separator that needs model choices with an app that does the steps for you on your PC.',
    h1='A UVR Alternative',
    kw='uvr alternative',
    lead='UVR (Ultimate Vocal Remover) is free and runs on your computer, but it asks you to choose models and settings. If you want a simpler route on your PC, look at an app that runs the steps for you.',
    tldr=['UVR is free and desktop-based, aimed at technical users.',
          'Good results depend on choosing models and settings.',
          'Tunedzy runs the vocal separation and the finishing steps in one app.',
          'Tunedzy is not free for the Windows app; it runs on credits.'],
    body='''
<h2>What UVR is good at</h2>
<p>UVR is free, runs on your computer, and gives you control over the models. It suits people who enjoy testing settings and want to choose the model for each song.</p>
<h2>Where it asks more of you</h2>
<p>Choosing a model and its settings takes time, and the best one changes from song to song. Beginners often find the choice hard to judge.</p>
<h2>Where Tunedzy fits</h2>
<p>Tunedzy runs the separation on your PC with its own settings, then cleans, levels and mixes the voice in the same app. You do not need to choose models. The Windows app uses credits; the phone app, Tunedzy Go, is free but does not separate songs.</p>
<h2>Which to pick</h2>
<p>For free control and model testing, UVR. For a simpler route on your PC that finishes the voice too, Tunedzy. Use either only with music you have the right to use.</p>
''',
    vf_title='Separate and finish on your PC',
    vf='<p>Tunedzy separates the vocal on your PC and finishes the voice in one app, with Before and After.</p>',
    faq=[('Is UVR better than Tunedzy?', 'For model testing and free control, UVR. For a simpler route to a finished voice, Tunedzy.'),
         ('Is UVR free?', 'Yes, it is free and desktop-based. Check its project page for current details.'),
         ('Can I use either on a song I do not own?', 'Only with the rights. Separation does not change who owns the music.')],
    related=['best-vocal-remover-apps', 'best-free-vocal-remover', 'best-ai-stem-splitter'])

add('voicemeeter-alternative', 'alternative', 'desk-wide', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='Voicemeeter Alternative for Streaming and Voice Routing',
    desc='Looking for a Voicemeeter alternative? Compare virtual audio mixers and cables, and see how a cleaned voice reaches Discord, Zoom or OBS with Tunedzy.',
    h1='A Voicemeeter Alternative',
    kw='voicemeeter alternative',
    lead='Voicemeeter is a virtual audio mixer by VB-Audio. Alternatives include JACK, MixDesk X and simple virtual cables. If your need is a cleaned microphone for a call or stream, Tunedzy Live Studio covers that part.',
    tldr=['Voicemeeter is a virtual mixer that routes audio between apps and devices.',
          'JACK is free and open source, for pro use with a steeper learning curve.',
          'MixDesk X routes up to 16 stereo outputs, on Mac and Windows.',
          'Tunedzy Live Studio cleans the microphone and sends it through a virtual cable.'],
    body='''
<h2>Mixer or cable</h2>
<p>A mixer routes sound and adjusts levels between sources. A cable only moves audio between two apps. Many streamers only need a cable plus one cleaning step.</p>
<h2>The alternatives</h2>
<ul>
<li><strong>JACK Audio Connection Kit</strong>: free and open source, for pro-audio routing.</li>
<li><strong>MixDesk X</strong>: routing on Mac and Windows, with per-channel EQ.</li>
<li><strong>VB-Audio Virtual Cable</strong>: a simple Windows driver that creates a virtual device.</li>
</ul>
<h2>Where Tunedzy fits</h2>
<p>Tunedzy Live Studio cleans your microphone and sends the cleaned voice into a virtual cable, so Discord and Zoom hear the cleaned voice. It is not a full mixer. The <a href="/tunedzy/blog/virtual-audio-cable-setup-obs-discord-zoom">cable setup guide</a> has the steps, and the <a href="/tunedzy/best-virtual-audio-mixer-for-streamers">mixer roundup</a> compares the options.</p>
''',
    vf_title='Clean the mic, route it on',
    vf='<p>Tunedzy Live Studio cleans your mic and sends it to a virtual cable for Discord, Zoom or OBS.</p>',
    faq=[('Is Tunedzy a Voicemeeter replacement?', 'No. Tunedzy cleans the microphone. A mixer or cable routes it.'),
         ('Do I need a virtual cable for Discord?', 'Usually yes, to send a cleaned voice into the app.'),
         ('Does Voicemeeter clean noise?', 'Check Voicemeeter’s own site for its features. Tunedzy cleans the voice as a separate step.')],
    related=['best-virtual-audio-mixer-for-streamers', 'vb-cable-alternative', 'voice-cleanup-for-streamers'])

add('vb-cable-alternative', 'alternative', 'booth-wide', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='VB-Cable Alternative: Virtual Audio Cables Compared',
    desc='Looking for a VB-Cable alternative? Compare virtual audio cables and per-app capture, and see how a cleaned voice reaches a call or stream with Tunedzy.',
    h1='A VB-Cable Alternative',
    kw='vb cable alternative',
    lead='VB-Audio Virtual Cable is a Windows driver that creates a virtual playback device. Alternatives vary: some are full mixers, some capture individual apps. Choose by whether you need routing, capture or cleaning.',
    tldr=['A virtual cable moves audio between apps; it does not clean it.',
          'win-capture-audio is an OBS plugin that captures individual application audio on Windows.',
          'JACK is a free, open-source audio system for pro routing.',
          'Tunedzy cleans the microphone and sends it on through a virtual cable.'],
    body='''
<h2>What a virtual cable does</h2>
<p>A virtual cable creates a device that one app plays into and another app records from. It is the simplest way to send audio from one program to another on Windows.</p>
<h2>The alternatives</h2>
<ul>
<li><strong>win-capture-audio</strong>: an OBS plugin that captures individual application audio.</li>
<li><strong>JACK</strong>: free and open source, a pro-audio system with routing.</li>
<li><strong>MixDesk X</strong>: a routing app with per-channel EQ, on Mac and Windows.</li>
</ul>
<h2>Cable and cleaning</h2>
<p>A cable does not clean the voice. Tunedzy Live Studio is the step that cleans the microphone; the cable then carries the cleaned voice into the call or stream. The <a href="/tunedzy/blog/virtual-audio-cable-setup-obs-discord-zoom">setup guide</a> shows the routing.</p>
''',
    vf_title='A cable for the cleaned voice',
    vf='<p>Tunedzy Live Studio cleans the mic and sends it through a virtual cable into your call or stream.</p>',
    faq=[('Do I need a cable for OBS?', 'OBS can take the voice from a browser source, according to the Tunedzy Live Studio page. Check the setup for your version.'),
         ('Is a virtual cable safe to install?', 'It is a driver. Install it from the publisher’s site, and read the setup notes.'),
         ('Does the cable add delay?', 'A little. Check the latency on your setup before a stream.')],
    related=['best-virtual-audio-mixer-for-streamers', 'voicemeeter-alternative', 'voice-cleanup-for-streamers'])

add('riverside-alternative', 'alternative', 'mic-wide', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='Riverside Alternative: Recording Remote Guests and Finishing the Audio',
    desc='Looking for a Riverside alternative? Compare remote recording platforms with a finishing tool, and see how Tunedzy cleans the files they produce.',
    h1='A Riverside Alternative',
    kw='riverside alternative',
    lead='Riverside records remote guests locally, with a track for each participant, and offers transcript-based editing. Tunedzy does not record remote calls. It finishes the audio that a recorder such as Riverside produces.',
    tldr=['Riverside records each participant locally and offers transcript-based editing.',
          'Tunedzy does not host remote recording; it cleans and mixes finished files.',
          'For remote guests, a recording platform is the right tool.',
          'For a finished episode, Tunedzy takes the files and makes them sound clean.'],
    body='''
<h2>What Riverside is good at</h2>
<p>Recording remote guests with local tracks, video, and transcript-based editing. Its own material describes uncompressed local audio for each participant.</p>
<h2>What Tunedzy is good at</h2>
<p>Cleaning and finishing the files: repair, studio sound, levelling, editing by transcript on your PC, Multitrack and a loudness target. It does not host a call.</p>
<h2>Use both</h2>
<p>Record the episode in Riverside, download each track, then clean and level them in Tunedzy. The <a href="/tunedzy/how-to-record-a-remote-podcast-guest">remote guest guide</a> covers the setup on both ends.</p>
''',
    vf_title='Record in Riverside, finish in Tunedzy',
    vf='<p>Download each track from your recording platform, then clean and level it in Tunedzy.</p>',
    faq=[('Can Tunedzy record a remote guest?', 'No. Use a recording platform for the call, and clean the files in Tunedzy.'),
         ('Does Riverside clean the audio?', 'It offers audio tools. Check its current features on its site.'),
         ('Why clean a local recording?', 'Local files are cleaner than call audio, and a clean pass still helps.')],
    related=['best-podcast-recording-software', 'how-to-record-a-remote-podcast-guest', 'podcast-sound-professional-on-a-budget'])

add('podcastle-alternative', 'alternative', 'desk', ['clean-streaming-mic', 'lufs-meter'],
    title='Podcastle Alternative: Recording, Editing and a Finishing Tool',
    desc='Looking for a Podcastle alternative? Compare browser podcast tools with a finishing app that works on your PC and phone, and when each one fits.',
    h1='A Podcastle Alternative',
    kw='podcastle alternative',
    lead='Podcastle records and edits podcasts in the browser or a desktop app, with voice enhancement and sound effects. If you want a finishing tool that keeps the audio on your device, Tunedzy is a different route.',
    tldr=['Podcastle offers recording, editing and voice enhancement in one place.',
          'Tunedzy finishes recordings on your PC or phone, with nothing uploaded.',
          'For one place to record and edit, Podcastle is the simpler option.',
          'For private episodes and loudness control, Tunedzy fits better.'],
    body='''
<h2>What Podcastle is good at</h2>
<p>Recording and editing in one place, with voice enhancement, trimming, sound effects and filler removal. A reviewer notes its multitrack editing as a strength. Check its plans on its site.</p>
<h2>Where Tunedzy differs</h2>
<p>Tunedzy does not record and edit a whole show in the browser. It cleans each file on your device, edits the transcript, mixes voices in Multitrack and exports at a loudness target.</p>
<h2>Which to pick</h2>
<p>For one tool that records and edits in the browser, Podcastle. For private recordings you want cleaned and levelled on your own device, Tunedzy. The <a href="/tunedzy/best-podcast-editing-software">podcast editing roundup</a> lists the other options.</p>
''',
    vf_title='Finish the episode on your device',
    vf='<p>Tunedzy cleans, levels, edits by words and exports the episode on your PC, nothing uploaded.</p>',
    faq=[('Is Tunedzy a podcast recorder?', 'No. It finishes files. Use a recorder for the call.'),
         ('Does Podcastle keep my audio in the cloud?', 'Check its privacy terms. Browser tools generally store uploads on their servers.'),
         ('Which is easier for beginners?', 'Podcastle for one place to do everything. Tunedzy Go for a simple cleanup on the phone.')],
    related=['best-podcast-recording-software', 'best-podcast-editing-software', 'voice-cleanup-for-podcasters'])

add('alitu-alternative', 'alternative', 'booth', ['lufs-meter', 'vocal-checker'],
    title='Alitu Alternative: All-in-One Podcast Tools and a Finishing App',
    desc='Looking for an Alitu alternative? Compare all-in-one podcast tools with a finishing app for your own files, and see how each handles cleanup and levels.',
    h1='An Alitu Alternative',
    kw='alitu alternative',
    lead='Alitu is an all-in-one web app that automates recording, cleanup, levelling and publishing. If you want one tool for the whole show, it is a strong choice. Tunedzy suits people who want more control over the finishing step on their own files.',
    tldr=['Alitu automates recording, cleanup, levelling and publishing in one web app.',
          'Tunedzy finishes files on your PC or phone, with editing by transcript.',
          'For a fully automated show, Alitu is the simpler option.',
          'For control and private files, Tunedzy fits better.'],
    body='''
<h2>What Alitu is good at</h2>
<p>An all-in-one web workflow: recording, automatic cleanup and levelling, and publishing. Its own material describes a fast route from recording to episode. Check its current plans on its site.</p>
<h2>What Tunedzy is good at</h2>
<p>Finishing your own files with control: repair steps you can see, a studio sound model, editing by transcript and a loudness target with a true peak check. The processing stays on your device.</p>
<h2>Which to pick</h2>
<p>If you want one web tool to handle the whole show, Alitu. If you want to keep files private and control each step, Tunedzy. The <a href="/tunedzy/best-podcast-editing-software">podcast editing roundup</a> places both.</p>
''',
    vf_title='Control the finish on your own files',
    vf='<p>Tunedzy finishes your files on your PC, with each step visible and Before and After to compare.</p>',
    faq=[('Is Alitu automatic?', 'Its material describes automatic cleanup and levelling. Check its features on its site.'),
         ('Can Tunedzy publish my episode?', 'No. It finishes the audio; publish with your host.'),
         ('Which gives more control?', 'Tunedzy, for each step. Alitu, for a faster automated route.')],
    related=['best-podcast-editing-software', 'podcast-sound-professional-on-a-budget', 'edit-a-podcast-by-its-words'])

add('hindenburg-alternative', 'alternative', 'neon-wide', ['lufs-meter', 'vocal-checker'],
    title='Hindenburg Alternative for Narrative Audio and Storytelling',
    desc='Looking for a Hindenburg alternative? Compare narrative audio editors with a voice finisher, and see where each fits a documentary or storytelling project.',
    h1='A Hindenburg Alternative',
    kw='hindenburg alternative',
    lead='Hindenburg Pro is a narrative editor aimed at storytelling and documentary work, sold as a one-time purchase. If you need a finishing tool for the voice in a story, Tunedzy covers the cleanup and loudness part.',
    tldr=['Hindenburg is built for narrative and storytelling audio.',
          'Tunedzy finishes the voice: cleanup, transcript editing, Multitrack and loudness.',
          'For full story editing and assembly, a narrative editor is the stronger tool.',
          'For cleaning interviews and narration on your PC, Tunedzy fits well.'],
    body='''
<h2>What Hindenburg is for</h2>
<p>Narrative and storytelling shows: assembling interviews, narration and music. Check its current licence and features on its site.</p>
<h2>Where Tunedzy fits</h2>
<p>Tunedzy is for the cleanup and the voice. Clean an interview, edit it by its transcript, level the speakers in Multitrack, and export at a loudness target. It does not assemble a documentary.</p>
<h2>Use them together</h2>
<p>Assemble the story in your narrative editor, export the voice tracks, and finish them in Tunedzy. The <a href="/tunedzy/how-to-clean-up-an-interview-recording">interview guide</a> covers the cleanup steps.</p>
''',
    vf_title='Finish the voices in the story',
    vf='<p>Export the interview and narration tracks, then clean and level them in Tunedzy.</p>',
    faq=[('Can Tunedzy edit a documentary?', 'It finishes the voice tracks. Use a narrative editor for assembly.'),
         ('Is Hindenburg a one-time purchase?', 'Its material describes one. Check its site for current terms.'),
         ('What about music in a story?', 'Duck it under the voice with Auto-duck in Multitrack.')],
    related=['how-to-clean-up-an-interview-recording', 'audio-cleanup-for-journalists', 'how-to-duck-music-under-a-voiceover'])

add('garageband-alternative-for-windows', 'alternative', 'desk', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='GarageBand Alternative for Windows Users',
    desc='GarageBand is free on Apple devices but not on Windows. Compare Windows options for recording and editing voices, with Tunedzy as a finishing app.',
    h1='A GarageBand Alternative for Windows',
    kw='garageband alternative for windows',
    lead='GarageBand is free and capable on Mac and iOS, but it is not available on Windows. Windows users can use Audacity or DaVinci Resolve for basic editing, and the Tunedzy Windows app for cleanup and loudness.',
    tldr=['GarageBand is free on Apple devices and not on Windows.',
          'Audacity is free, open source and runs on Windows.',
          'DaVinci Resolve is free and has a dialogue page, built for video.',
          'Tunedzy is a Windows app for cleaning and finishing voices.'],
    body='''
<h2>The Windows options</h2>
<ul>
<li><strong>Audacity</strong>: free and open source, a good manual editor for voices.</li>
<li><strong>DaVinci Resolve</strong>: free, with a dialogue page for speech; built for video.</li>
<li><strong>Tunedzy</strong>: a Windows app for cleanup, editing by transcript, Multitrack and loudness.</li>
</ul>
<h2>Which to pick</h2>
<p>For basic voice editing, Audacity. For a video project with speech, DaVinci Resolve. For cleaning and finishing a voice to a loudness target, Tunedzy. The <a href="/tunedzy/tunedzy-vs-garageband">GarageBand comparison</a> covers the music side.</p>
''',
    vf_title='Finish the voice on Windows',
    vf='<p>Tunedzy finishes the voice on your Windows PC: cleanup, editing by words, Multitrack and a loudness target.</p>',
    faq=[('Is there GarageBand for Windows?', 'No. Use Audacity, DaVinci Resolve or another Windows option.'),
         ('Which free editor is best on Windows?', 'Audacity for voice editing; DaVinci Resolve if the work is video.'),
         ('Can Tunedzy make music?', 'No. It finishes voices.')],
    related=['tunedzy-vs-garageband', 'best-free-audio-editor-for-beginners', 'tunedzy-vs-audacity'])

add('free-alternative-to-adobe-audition', 'alternative', 'booth-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Free Alternative to Adobe Audition for Voice Work',
    desc='Looking for a free alternative to Adobe Audition? Compare free editors and a finishing app for voice work, with the trade-offs in noise tools and learning curve.',
    h1='A Free Alternative to Adobe Audition',
    kw='free alternative to adobe audition',
    lead='Adobe Audition is a paid professional editor with strong restoration tools. For voice work, free options cover many jobs: Audacity for manual editing, and Tunedzy for a finished voice with less to learn.',
    tldr=['Audition is a paid professional editor with detailed restoration tools.',
          'Audacity is free and handles basic voice editing and noise profiles.',
          'DaVinci Resolve is free and has a dialogue page.',
          'Tunedzy finishes the voice with less to learn; the Windows app uses credits.'],
    body='''
<h2>What Audition does better</h2>
<p>A spectral view for precise repair, detailed noise tools, and close integration with Premiere Pro. For demanding restoration work, it is a strong choice. Check Adobe&rsquo;s plans on its site.</p>
<h2>Free options for voice</h2>
<ul>
<li><strong>Audacity</strong>: manual editing and noise profiles, free.</li>
<li><strong>DaVinci Resolve</strong>: free, with a dialogue page for speech.</li>
<li><strong>Tunedzy</strong>: repair, cleanup, editing by transcript and loudness in one pass.</li>
</ul>
<h2>Which to pick</h2>
<p>For detailed restoration and video, Audition. For free manual editing, Audacity. For a voice finished without learning each tool, Tunedzy. The <a href="/tunedzy/tunedzy-vs-adobe-audition">Audition comparison</a> covers the trade-off.</p>
''',
    vf_title='A finished voice, less to learn',
    vf='<p>Tunedzy finishes the voice in one pass on your PC, with Before and After to check each step.</p>',
    faq=[('Is there a free version of Audition?', 'Adobe’s plans change. Check its site. Audacity is free for voice editing.'),
         ('Which free option is closest to Audition?', 'DaVinci Resolve has a dialogue page; Audacity is the manual choice.'),
         ('Is Tunedzy as deep as Audition?', 'No. It covers the common steps with fewer controls.')],
    related=['tunedzy-vs-adobe-audition', 'tunedzy-vs-audacity', 'best-audio-cleanup-software-for-windows'])

add('free-alternative-to-izotope-rx', 'alternative', 'mic-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Free Alternative to iZotope RX for Dialogue Repair',
    desc='Looking for a free alternative to iZotope RX? Compare free dialogue repair options with a finishing app, and see where RX remains the stronger professional tool.',
    h1='A Free Alternative to iZotope RX',
    kw='free alternative to izotope rx',
    lead='iZotope RX is a professional repair suite with deep dialogue tools, sold on its own licence. For many everyday repairs, free options and a finishing app are enough. For the hardest jobs, RX stays the stronger tool.',
    tldr=['RX is a professional suite with dialogue modules and a repair assistant.',
          'Audacity is free and covers noise profiles, clicks and manual repair.',
          'Tunedzy covers the common repair steps automatically, with a spectral box in Quick edit.',
          'For film and broadcast repair, RX is the stronger tool.'],
    body='''
<h2>What RX is for</h2>
<p>Difficult dialogue repair: reverb, noise and damaged speech, with detailed modules and a repair assistant. Check iZotope’s site for its current versions and licence.</p>
<h2>Free and lighter options</h2>
<ul>
<li><strong>Audacity</strong>: free manual repair, noise profiles and click removal.</li>
<li><strong>Tunedzy</strong>: repair for clipping, clicks, hum and DC offset, a studio sound model, and a spectral repair box in Quick edit.</li>
</ul>
<h2>Which to pick</h2>
<p>For a hard repair on a film or broadcast file, RX. For everyday cleanup of voice recordings, Audacity or Tunedzy. The <a href="/tunedzy/tunedzy-vs-izotope-rx">RX comparison</a> goes into the detail.</p>
''',
    vf_title='Repair the everyday problems',
    vf='<p>Tunedzy repairs clipping, clicks and hum, then cleans and levels the voice on your PC.</p>',
    faq=[('Can free tools match RX?', 'For everyday voice cleanup, often yes. For the hardest repairs, RX has more control.'),
         ('Does Tunedzy have spectral repair?', 'It has a spectral repair box in Quick edit. It is simpler than RX.'),
         ('Is RX worth it?', 'For professional dialogue repair, many engineers say yes. Check the cost against your work.')],
    related=['tunedzy-vs-izotope-rx', 'best-audio-cleanup-software-for-windows', 'fix-clipped-distorted-audio'])

# ----------------------------------------------------------------------------------- features
add('tunedzy-perfect-it', 'feature', 'hero', ['vocal-checker', 'lufs-meter'],
    title='Tunedzy Perfect It: One-Pass Voice Cleanup Explained',
    desc='Perfect it is Tunedzy’s one-pass voice cleanup: repair, studio sound, level and tone in order. What it does, what it cannot do and how to check the result.',
    h1='Tunedzy Perfect It',
    kw='tunedzy perfect it',
    lead='Perfect it runs the voice cleanup in one pass on your PC: it repairs clipping, clicks, hum and offset first, then runs the studio sound model, then sets the level and tone. Use Before and After to check the result.',
    tldr=['Perfect it repairs first, then cleans noise, then levels and tones the voice.',
          'It runs on your PC and nothing is uploaded.',
          'It cannot rebuild lost speech or remove heavy room echo completely.',
          'Compare Before and After before you keep the result.'],
    body='''
<h2>What it does, in order</h2>
<ol>
<li><strong>Repair</strong>: rebuilds flat-topped clipping where it can, removes clicks and hum, and takes out any DC offset.</li>
<li><strong>Studio sound</strong>: a speech model (DeepFilterNet 3) reduces noise and room sound while keeping the voice.</li>
<li><strong>Level and tone</strong>: a voice chain sets the level, de-esses, guards pops and shapes the tone toward a clear voice.</li>
</ol>
<h2>What it cannot do</h2>
<p>It cannot restore speech that was never recorded, and it cannot remove a heavy echo completely. A badly clipped recording stays audible. Re-recording closer to the mic is the real fix.</p>
<h2>How to use it well</h2>
<p>Start with the recording as it is. Listen to Before and After, lower the amount if the voice sounds watery, and export only when it sounds right. The <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup guide</a> walks through the steps.</p>
''',
    vf_title='Try Perfect it on one recording',
    vf='<p>Run Perfect it on a short recording in the Windows app, then compare Before and After.</p>',
    faq=[('Does Perfect it upload my file?', 'No. It runs on your PC.'),
         ('Can it fix a bad recording?', 'It improves many, but not all. A very damaged file stays damaged.'),
         ('Is there a phone version?', 'Tunedzy Go cleans recordings on the phone for free, with studio sound.')],
    related=['clean-up-a-phone-voice-recording', 'what-is-a-noise-gate', 'does-ai-cleanup-change-your-voice'])

add('tunedzy-repair', 'feature', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Tunedzy Repair: Clipping, Clicks, Hum and Offset',
    desc='Tunedzy Repair finds and mends clipping, clicks, mains hum and DC offset in a recording, and reports what it did. What each repair does and its limits.',
    h1='Tunedzy Repair',
    kw='tunedzy repair audio',
    lead='Repair is Tunedzy’s set of targeted fixes: flat-topped clipping, clicks and crackle, mains hum, and DC offset. It runs before the cleanup and reports what it changed.',
    tldr=['Clipping repair rebuilds flat peaks at the file’s own sample rate.',
          'Click repair mends short spikes and crackle.',
          'Hum repair notches the mains frequency and its harmonics.',
          'DC offset is removed so the wave sits around zero.'],
    body='''
<h2>Clipping</h2>
<p>Flat-topped sections of a waveform are found and rebuilt from the curve around them. The repair works at the file&rsquo;s own sample rate, so a 48 kHz phone file is repaired correctly. Heavy clipping cannot be rebuilt reliably.</p>
<h2>Clicks and crackle</h2>
<p>Short spikes that stand out from the voice are replaced with the sound around them. Use the lowest setting that removes them.</p>
<h2>Hum</h2>
<p>Mains hum at 50 or 60 Hz and its harmonics is notched out. The <a href="/tunedzy/remove-hum-from-audio">hum guide</a> explains the method.</p>
<h2>DC offset</h2>
<p>A DC offset shifts the wave away from zero, and it can make a file look louder than it sounds. It is removed.</p>
''',
    vf_title='Repair first, then clean',
    vf='<p>Repair runs before the cleanup in Perfect it, and tells you what it changed.</p>',
    faq=[('Does Repair change the voice?', 'It changes only the faults it finds. Compare Before and After.'),
         ('Why does Repair report clipping in my file?', 'It found flat tops in the waveform. Repair rebuilds what it can.'),
         ('Can Repair fix every click?', 'It fixes most short clicks. Recurring clicks point to a fault to fix at source.')],
    related=['fix-clipped-distorted-audio', 'how-to-fix-a-crackling-recording', 'remove-hum-from-audio'])

add('tunedzy-studio-sound', 'feature', 'neon-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Tunedzy Studio Sound: On-Device Speech Noise Reduction',
    desc='Studio sound is Tunedzy’s on-device speech model for noise and room sound, based on DeepFilterNet 3. What it does, how it runs on PC and phone and its limits.',
    h1='Tunedzy Studio Sound',
    kw='tunedzy studio sound',
    lead='Studio sound is a speech model that reduces noise and room sound while keeping the voice. It runs on your PC in the Windows app and on your phone in Tunedzy Go, with nothing uploaded.',
    tldr=['Studio sound uses DeepFilterNet 3, a speech noise reduction model.',
          'It runs on your PC, and in Tunedzy Go on your phone.',
          'Its licence is MIT or Apache 2.0, according to the project.',
          'Use the lowest setting that gives a clean result.'],
    body='''
<h2>What it does</h2>
<p>It separates the speech from the noise and the room, and reduces the noise while keeping the voice. It works best on steady noise such as a fan or hiss, and on room sound.</p>
<h2>Where it runs</h2>
<p>In the Windows app, inside Perfect it, on your PC. In Tunedzy Go, on your phone; the model downloads once the first time you use it, which is about 22 MB in the phone app.</p>
<h2>Limits</h2>
<p>Speech that sits right under the voice, such as another person close by, is hard to separate. Heavy settings can make the voice sound watery. Compare with the original.</p>
''',
    vf_title='Clean the room sound on your device',
    vf='<p>Studio sound reduces noise and room sound on your PC or phone, with nothing uploaded.</p>',
    faq=[('Is studio sound AI?', 'Yes, it is a neural speech model that runs on your device.'),
         ('Does it upload my audio?', 'No. It runs on your PC or phone.'),
         ('Why does it sound watery?', 'The setting is too strong. Lower it and compare with the original.')],
    related=['tunedzy-perfect-it', 'remove-background-noise-from-a-voice-recording', 'what-is-a-noise-floor'])

add('tunedzy-multitrack', 'feature', 'desk-wide', ['clean-streaming-mic', 'lufs-meter'],
    title='Tunedzy Multitrack: Voices and Music in One Mix',
    desc='Multitrack is Tunedzy’s timeline for voices and music: tracks, clips, fades, volume lines, markers, Auto-duck and export. What it does and how to use it.',
    h1='Tunedzy Multitrack',
    kw='tunedzy multitrack',
    lead='Multitrack is a timeline for several voices and music. You can record onto a track, arrange clips, add fades and volume lines, duck music under speech, and export the mix at a loudness target.',
    tldr=['Tracks, clips and fades on one timeline.',
          'Volume lines, pan and simple EQ and compression per track.',
          'Auto-duck lowers music under voices.',
          'Export the mix, the stems or chapter markers.'],
    body='''
<h2>The timeline</h2>
<p>Each track holds clips. Drag clips to arrange them, split and trim them, and set fades at the start and end. Markers become chapters on export.</p>
<h2>Mixing</h2>
<p>Each track has volume, pan and tone controls. Volume lines let you ride the level over time. Match loudness sets clips to a common level.</p>
<h2>Ducking and export</h2>
<p>Auto-duck lowers the music under the voices. Export the finished mix at a loudness target with a true peak check, or export one file per track as stems.</p>
''',
    vf_title='Mix the voices and music',
    vf='<p>Multitrack mixes your voices and music on one timeline, then exports at a loudness target.</p>',
    faq=[('How many tracks can I use?', 'As many as your project needs. Very long projects use more memory.'),
         ('Can I record onto a track?', 'Yes, you can record a take onto a track.'),
         ('Is Multitrack a full DAW?', 'No. It is a finishing mixer for voices and music, not a beat maker.')],
    related=['how-to-duck-music-under-a-voiceover', 'how-to-export-stems-for-a-daw', 'voice-cleanup-for-podcasters'])

add('tunedzy-transcript-editor', 'feature', 'booth-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Tunedzy Transcript Editor: Cut Audio by Its Words',
    desc='The Tunedzy transcript editor writes what was said on your PC, lets you cut words and pauses, removes ums and exports captions. What it does and its limits.',
    h1='Tunedzy Transcript Editor',
    kw='tunedzy transcript editor',
    lead='The transcript editor writes out what was said, with the time of each word, on your PC. You can cut words from the audio, remove ums and uhs, shorten long pauses, and export captions.',
    tldr=['The transcript is made on your PC with a speech model.',
          'Cut words to cut the audio; the sound follows the text.',
          'Remove ums and uhs, and shorten long pauses.',
          'Export SRT, VTT or plain text.'],
    body='''
<h2>The transcript</h2>
<p>A speech model writes out the words with their times. It works best on clear speech and a good recording. Check names and technical words before you use the text.</p>
<h2>Cutting</h2>
<p>Select words in the transcript and cut them, and the audio follows. Remove ums and uhs in one action, or shorten pauses over a set length to a shorter gap.</p>
<h2>Captions</h2>
<p>Export SRT or VTT captions for video, or a plain text file for show notes. The <a href="/tunedzy/edit-a-podcast-by-its-words">edit-by-words guide</a> shows the process.</p>
''',
    vf_title='Edit the audio by its words',
    vf='<p>The transcript editor cuts the audio from its text, removes fillers and exports captions, on your PC.</p>',
    faq=[('Does the transcript upload my audio?', 'No. It is made on your PC.'),
         ('How accurate is it?', 'Good on clear speech; check names, accents and noisy parts.'),
         ('Can I export captions?', 'Yes, as SRT or VTT.')],
    related=['edit-a-podcast-by-its-words', 'best-transcription-app-for-podcasts', 'how-to-trim-silence-from-a-recording'])

add('tunedzy-match-loudness', 'feature', 'mic', ['lufs-meter', 'vocal-checker'],
    title='Tunedzy Match Loudness: Set a Target, Check the Peak',
    desc='Match loudness sets a recording or a mix to a loudness target, with presets for podcasts, online video and audiobooks, and checks the true peak. How it works.',
    h1='Tunedzy Match Loudness',
    kw='tunedzy match loudness',
    lead='Match loudness sets a file to a loudness target and checks the true peak, so the level suits where it is going. Choose a preset that matches the destination, then listen.',
    tldr=['Presets include podcast, online video, audiobook, broadcast and loud targets.',
          'The level is set to the target across the whole file.',
          'The true peak is checked, so the export does not clip after conversion.',
          'Listen on a phone speaker after you export.'],
    body='''
<h2>The presets</h2>
<p>Each preset sets a loudness target suited to a kind of output: podcast, online video, audiobook, broadcast, or a louder preset for a mix. Choose the one for your destination.</p>
<h2>The peak check</h2>
<p>After the level is set, the true peak is checked against a ceiling. A file that would clip after conversion is held below it.</p>
<h2>Where it is used</h2>
<p>On a voice in Perfect it, on clips in Multitrack, and on the final mix on export. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the targets people use.</p>
''',
    vf_title='Set the target, then export',
    vf='<p>Match loudness sets the level for your destination and checks the true peak before you export.</p>',
    faq=[('Which preset should I choose?', 'The one for where the file goes: podcast, online video, or audiobook.'),
         ('Does it squash the voice?', 'It sets the level; it does not push the voice with heavy limiting.'),
         ('Can I set my own target?', 'Use the presets and check the result by ear.')],
    related=['loudness-for-youtube-podcasts-and-spotify', 'what-is-true-peak-dbtp', 'how-to-normalize-audio-the-right-way'])

add('tunedzy-auto-duck', 'feature', 'desk', ['lufs-meter', 'vocal-checker'],
    title='Tunedzy Auto-Duck: Music Under the Voice, Automatically',
    desc='Auto-duck in Tunedzy Multitrack lowers music under your voices automatically, then brings it back in the gaps. How it works and how to set the amount.',
    h1='Tunedzy Auto-Duck',
    kw='tunedzy auto duck',
    lead='Auto-duck lowers the music under the voices in Multitrack and lets it return in the gaps. It keeps the words clear without you drawing the volume by hand.',
    tldr=['Auto-duck follows the voice and lowers the music under it.',
          'The music returns in the pauses.',
          'Set the amount and the recovery to keep it smooth.',
          'Listen to the whole passage, not one phrase.'],
    body='''
<h2>How it works</h2>
<p>Auto-duck treats the voice as the trigger. When the voice speaks, the music or effects are turned down by the amount you set. When the voice stops, they come back. Overlapping ducks are merged so the music does not pump.</p>
<h2>Setting it</h2>
<p>Start with the default. If the music pumps, reduce the amount or slow the return. If the words still compete, increase the reduction slightly. Play the passage on a phone speaker too.</p>
<h2>Where it is used</h2>
<p>In Multitrack, on the music tracks under the voices. The <a href="/tunedzy/how-to-duck-music-under-a-voiceover">ducking how-to</a> has the steps, and the <a href="/tunedzy/what-is-ducking">ducking explanation</a> covers the idea.</p>
''',
    vf_title='Music under the words, automatically',
    vf='<p>Auto-duck in Multitrack lowers the music under your voices, so the words stay clear.</p>',
    faq=[('Why does the music pump?', 'The reduction is too strong or the return too fast. Adjust both.'),
         ('Can I duck several music tracks?', 'Yes, each music track can be ducked under the same voice.'),
         ('Does it work on video?', 'It works on the audio in Multitrack. Replace the sound in a video separately.')],
    related=['how-to-duck-music-under-a-voiceover', 'what-is-ducking', 'how-to-add-background-music-to-a-voiceover'])

add('tunedzy-replace-audio-in-video', 'feature', 'neon', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Tunedzy Replace Audio in Video: Keep the Picture',
    desc='Replace the sound in an MP4 or MOV with a cleaned voice, without re-encoding the picture. How the feature works, its limits and what to check.',
    h1='Tunedzy Replace Audio in Video',
    kw='tunedzy replace audio in video',
    lead='Replace audio puts a cleaned sound into an MP4 or MOV and copies the picture as it is. The picture is not re-encoded, so its quality is kept. The new sound is cut to the picture length if it is longer.',
    tldr=['The picture stream is copied, not re-encoded.',
          'MP4 and MOV work; a file with no picture is refused.',
          'A longer soundtrack is cut to the video length.',
          'Check the start, the end and any join after replacing.'],
    body='''
<h2>What happens</h2>
<p>Tunedzy reads the video, copies the picture, and writes the new sound beside it. The FFmpeg tool that does the work runs as a separate program under the LGPL licence.</p>
<h2>Limits</h2>
<p>A shorter soundtrack leaves silence at the end of the video. A file without a picture stream is refused. Other formats may need converting first.</p>
<h2>Check it</h2>
<p>Play the new file from the start, the end and any cut. The <a href="/tunedzy/put-clean-audio-back-into-a-video">replace audio guide</a> has the steps.</p>
''',
    vf_title='Clean the sound, keep the picture',
    vf='<p>Replace the sound in an MP4 or MOV with a cleaned version, and keep the picture as it was.</p>',
    faq=[('Is the picture quality reduced?', 'No, the picture is copied, not re-encoded.'),
         ('Can I replace audio in a phone video?', 'Yes, for MP4 and MOV files, in the Windows app.'),
         ('What if the new sound is shorter?', 'The video ends with silence after the sound stops.')],
    related=['put-clean-audio-back-into-a-video', 'how-to-clean-audio-from-a-smartphone-video', 'best-tool-to-remove-background-noise-from-video'])

add('tunedzy-vocal-remover', 'feature', 'hero-wide', ['song-key-finder', 'vocal-checker'],
    title='Tunedzy Vocal Remover and Stem Mixer',
    desc='The Tunedzy vocal remover separates a song into a vocal and an instrumental on your PC, with a stem mixer for the parts. What it does and how to use it.',
    h1='Tunedzy Vocal Remover',
    kw='tunedzy vocal remover',
    lead='The vocal remover splits a song into a vocal and an instrumental on your PC, and the stem mixer lets you set the balance of the parts. Use it only with music you have the right to use.',
    tldr=['Separates a song into a vocal and an instrumental on your PC.',
          'The stem mixer sets the balance of the parts.',
          'Nothing is uploaded.',
          'Use it only with music you have the right to use.'],
    body='''
<h2>What it does</h2>
<p>A separation model splits a song into its vocal and its instrumental. The stem mixer lets you balance the parts, for practice, a karaoke version or a remix you have rights to make.</p>
<h2>Limits</h2>
<p>Separation is never perfect. Expect some bleed between parts and artifacts on dense mixes. A short practice loop is often more useful than a perfect track.</p>
<h2>Rights</h2>
<p>Separating a commercial song can be a rights issue, even for personal use. Check before you make or share a version. The <a href="/tunedzy/how-to-make-a-karaoke-track-from-a-song">karaoke track guide</a> covers the rules of thumb.</p>
''',
    vf_title='Separate on your PC',
    vf='<p>The vocal remover runs on your PC, and the stem mixer balances the parts. Use it with music you have rights to.</p>',
    faq=[('Is the separation done on your servers?', 'No. It runs on your PC.'),
         ('Can I make a karaoke track?', 'Yes, for music you have the right to use.'),
         ('Why does the vocal sound thin?', 'Separation removes some of the voice with the music. Use a light clean.')],
    related=['best-vocal-remover-apps', 'how-to-isolate-a-voice-from-background-music', 'best-karaoke-maker-app'])

add('tunedzy-key-and-speed', 'feature', 'neon-wide', ['song-key-finder', 'bpm-finder', 'chord-finder'],
    title='Tunedzy Key and Speed: Change a Clip’s Pitch or Tempo',
    desc='Key and speed changes the key or the speed of a clip in Tunedzy. How it works, when small changes sound natural and how to check the result.',
    h1='Tunedzy Key and Speed',
    kw='tunedzy key and speed',
    lead='Key and speed changes the key or the speed of a clip. Small changes sound natural; large changes can add artifacts. Keep the original, and check the highest and lowest notes after each change.',
    tldr=['Change the key by semitones, or the speed of a clip.',
          'Small changes sound natural; large ones can smear.',
          'Keep the original and listen to the whole clip.',
          'Check the range for a vocal after a key change.'],
    body='''
<h2>What it changes</h2>
<p>Key moves a clip up or down in pitch by semitones. Speed changes how fast the clip plays, with the pitch kept where the tool allows it.</p>
<h2>Limits</h2>
<p>Large changes add artifacts and can change how a voice sounds. Check the highest and lowest notes, and listen on a phone speaker.</p>
<h2>Guides</h2>
<p>The <a href="/tunedzy/how-to-change-the-key-of-a-vocal">key change guide</a> and the <a href="/tunedzy/how-to-change-speed-without-changing-pitch">speed guide</a> explain the method.</p>
''',
    vf_title='Change the key or speed, check it',
    vf='<p>Key and speed changes a clip in small, checkable steps. Keep the original and listen after each change.</p>',
    faq=[('How many semitones are safe?', 'Small moves are usually natural. Check the singer’s range rather than a number.'),
         ('Does speed change the pitch?', 'Simple speed changes do. The tool keeps the pitch where it can.'),
         ('Can I change both?', 'Yes, but check the result after each change.')],
    related=['how-to-change-the-key-of-a-vocal', 'how-to-change-speed-without-changing-pitch', 'best-autotune-alternatives'])

add('tunedzy-live-studio', 'feature', 'desk-wide', ['clean-streaming-mic', 'live-autotune'],
    title='Tunedzy Live Studio: Clean Your Mic Live on Windows',
    desc='Live Studio cleans your microphone as you speak or stream on Windows, and can send the cleaned voice into Discord, Zoom or OBS. What it does and how to set it up.',
    h1='Tunedzy Live Studio',
    kw='tunedzy live studio',
    lead='Live Studio is the Windows part of Tunedzy that cleans your microphone as you speak or stream. The cleaned voice can go into a call or stream through a virtual cable, or into OBS.',
    tldr=['Cleans the microphone live on Windows.',
          'Sends the cleaned voice into Discord or Zoom through a virtual cable.',
          'OBS can take the voice from a browser source.',
          'A live cleaner adds a small delay; check it on your setup.'],
    body='''
<h2>What it does</h2>
<p>It takes your microphone, cleans the room noise and the harsh edges, and plays the cleaned voice out. It includes a live autotune tool for singing.</p>
<h2>Routing</h2>
<p>For Discord and Zoom, install a virtual cable and choose it as the microphone in those apps. OBS can take the cleaned voice from a browser source. The <a href="/tunedzy/blog/virtual-audio-cable-setup-obs-discord-zoom">setup guide</a> has the steps.</p>
<h2>Limits</h2>
<p>A live cleaner adds a small delay, and it cannot fix a poor mic position. Set the mic close and the room soft first.</p>
''',
    vf_title='Clean the mic live on Windows',
    vf='<p>Live Studio cleans your microphone live on Windows and sends it into your call or stream.</p>',
    faq=[('Does it work on Mac?', 'Live Studio is part of the Windows app. A Mac build is being prepared.'),
         ('Will there be a delay?', 'A small one. Check it on your setup before a stream.'),
         ('Do I need a virtual cable?', 'For Discord and Zoom, usually yes. OBS can use a browser source.')],
    related=['best-virtual-audio-mixer-for-streamers', 'voice-cleanup-for-streamers', 'voicemeeter-alternative']
)

add('tunedzy-go', 'feature', 'hero', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='Tunedzy Go: The Free Phone App for Studio Sound',
    desc='Tunedzy Go is the free phone app that records or takes a file and cleans it with studio sound in your browser, with nothing uploaded and offline use after the first visit.',
    h1='Tunedzy Go',
    kw='tunedzy go',
    lead='Tunedzy Go is a free web app for your phone. Record audio or video, or pick a file, then clean it with studio sound. It works offline after the first visit, and nothing you record is uploaded.',
    tldr=['Free, and it does not use credits.',
          'Records audio or video, or picks a file.',
          'Studio sound runs on the phone, after a one-time model download of about 22 MB.',
          'Works offline after the first visit; nothing is uploaded.'],
    body='''
<h2>What it does</h2>
<p>Record or pick a recording, clean it with studio sound and the level and tone steps, compare Before and After, then share or save the result.</p>
<h2>Install and offline</h2>
<p>Open it in your phone browser and add it to the home screen. After the first visit, it works without a connection.</p>
<h2>Limits</h2>
<p>It is a web app with less control than the Windows app. Multitrack, transcripts and replacing audio in video are Windows features.</p>
<p>The <a href="/tunedzy/tunedzy-go-faq">Tunedzy Go FAQ</a> answers the common questions.</p>
''',
    vf_title='Open Tunedzy Go on your phone',
    vf='<p>Open Tunedzy Go in your phone browser, record or choose a file, and clean it. Free, with nothing uploaded.</p>',
    faq=[('Is Tunedzy Go free?', 'Yes. It does not use credits.'),
         ('Is my recording uploaded?', 'No. It is processed in the browser on your phone.'),
         ('Does it need an account?', 'No.')],
    related=['tunedzy-go-faq', 'clean-up-a-phone-voice-recording', 'best-app-to-clean-phone-audio']
)

add('tunedzy-export-stems', 'feature', 'desk', ['song-key-finder', 'bpm-finder'],
    title='Tunedzy Export Stems: One File Per Track',
    desc='Export stems exports one file per track from Multitrack, so a voice can be finished in your DAW. How it works, the naming and the sync check.',
    h1='Tunedzy Export Stems',
    kw='tunedzy export stems',
    lead='Export stems writes one file per track from Multitrack. Each file starts at the same time, so the stems stay in sync when you bring them into a DAW.',
    tldr=['One file per track, all starting at the same time.',
          'Name files by track, so the DAW shows what each one is.',
          'Keep one sample rate across the stems.',
          'Check the sync by importing them together.'],
    body='''
<h2>What it exports</h2>
<p>Each track becomes its own file, from the start of the project. The files line up, so they can be imported together in a DAW.</p>
<h2>Using them</h2>
<p>Import the stems into your DAW, check the start and a join, then finish the mix there. The <a href="/tunedzy/how-to-export-stems-for-a-daw">stem export guide</a> has the steps.</p>
<h2>Limits</h2>
<p>Stems carry the processing of each track. If a track has no clips, it may not be exported.</p>
''',
    vf_title='Export the voice for your DAW',
    vf='<p>Export stems from Multitrack, one file per track, so the voice finishes cleanly in your DAW.</p>',
    faq=[('Why export stems?', 'To change the balance and effects in your DAW.'),
         ('Are the stems in sync?', 'They start at the same time. Check by importing them together.'),
         ('What format?', 'WAV is the usual choice for stems.')],
    related=['how-to-export-stems-for-a-daw', 'tunedzy-multitrack', 'tunedzy-vs-fl-studio']
)
