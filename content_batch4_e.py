"""Batch 4e (25 October 2026): six help pages, two ethics pages and one how-to. Same shape as content.GUIDES.

Help facts come from the app's own behaviour and documentation as of 25 October 2026: Windows 10 and 11 (64-bit), the installer,
the default port, the data folder, the credit rules and the privacy statement. GROUP_OF marks 'help', 'ethics' or 'how'.
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


add('install-tunedzy-on-windows', 'help', 'desk', ['vocal-checker', 'lufs-meter'],
    title='How to Install Tunedzy on Windows',
    desc='Install Tunedzy on Windows 10 or 11: download the installer, get past the Windows warning for an unsigned app, and start the app for the first time.',
    h1='How to Install Tunedzy on Windows',
    kw='how to install tunedzy on windows',
    lead='Tunedzy installs like any Windows app. The installer is not yet code-signed, so Windows shows a warning; the steps below get you past it safely.',
    tldr=['Use the download link on fuidzy.com/tunedzy, the installer is about 347 MB.',
          'Windows may say it protected your PC: choose More info, then Run anyway.',
          'The first start can take a moment while the engine opens.',
          'Models download the first time you need them, such as Transcript.'],
    body='''
<h2>Before you start</h2>
<p>Use Windows 10 or 11, 64-bit. Check the requirements in <a href="/tunedzy/tunedzy-system-requirements">the system requirements</a>. Download the installer only from the link on fuidzy.com/tunedzy, so you get the file this page describes.</p>
<h2>Run the installer</h2>
<p>Open the downloaded file. Windows may show a blue screen that says it protected your PC, because the installer is not yet signed with a publisher certificate. Choose More info, then Run anyway. Follow the steps and choose where to install.</p>
<h2>First start</h2>
<p>Start Tunedzy from the Start menu. The first start can take a short while as the engine opens. If a firewall asks about Tunedzy, allow it on private networks: the app talks to itself on your PC, and it reaches the credit server for your account.</p>
<h2>Models and downloads</h2>
<p>The studio sound model is part of the app. The transcription model (about 145 MB for the base size) downloads the first time you use Transcript, once. The optional AI separation pack is also a one-time download.</p>
<h2>If it does not start</h2>
<p>Read <a href="/tunedzy/tunedzy-troubleshooting">the troubleshooting guide</a>. Check your antivirus did not quarantine the app, and that the download finished completely.</p>
''',
    vf_title='Start with a clean file',
    vf='<p>Once Tunedzy is open, Perfect it cleans a recording in one pass. The free phone app, Tunedzy Go, works in any browser.</p>',
    faq=[('Is Tunedzy safe to install?', 'It runs on your PC and does not upload your audio. The installer is unsigned for now, so Windows warns you; check that you downloaded it from fuidzy.com.'),
         ('Can I install it on two PCs?', 'The credit system counts use per account, not per install. You can sign in on more than one PC; check the Credits screen for the current limits.'),
         ('How do I uninstall it?', 'Use Windows Settings, then Apps, and choose Tunedzy. Your project files stay in your user folder unless you delete them.')],
    related=['tunedzy-system-requirements', 'tunedzy-troubleshooting', 'tunedzy-privacy-explained'])

add('tunedzy-system-requirements', 'help', 'hero', ['vocal-checker', 'lufs-meter'],
    title='Tunedzy System Requirements',
    desc='What Tunedzy needs to run on Windows: the operating system, memory, disk space, a microphone for live use, and what needs the internet.',
    h1='Tunedzy System Requirements',
    kw='tunedzy system requirements',
    lead='Tunedzy runs on an ordinary Windows PC. Memory matters most for long recordings, and a graphics card is optional.',
    tldr=['Windows 10 or 11, 64-bit.',
          'About 8 GB of memory or more is recommended, especially for long files.',
          'No graphics card is needed; an NVIDIA card only speeds up the optional AI separation.',
          'Keep several gigabytes free for the app, models and your projects.'],
    body='''
<h2>Operating system</h2>
<p>Windows 10 or Windows 11, 64-bit. Tunedzy is a Windows app today. A Mac version is being prepared, and Tunedzy Go works in any modern browser on a phone or computer.</p>
<h2>Memory</h2>
<p>Eight gigabytes of memory or more is recommended. Long recordings and large projects use more memory, because the audio is held in memory while it is edited. Record long sessions in sections if your PC is short on memory.</p>
<h2>Disk space</h2>
<p>Keep several gigabytes free. The app, its models and the projects you save take space, and exports add to it. The installer on its own is about 347 MB.</p>
<h2>Graphics</h2>
<p>No graphics card is needed. An NVIDIA card makes the optional AI vocal-separation step faster, but the step still runs without one.</p>
<h2>Microphone and audio</h2>
<p>Live Studio needs a microphone and an audio output. For a stream or a call, a virtual audio cable may be needed to send the cleaned voice into another app.</p>
<h2>The internet</h2>
<p>Processing does not need the internet. Credits are counted through our credit server, and updates and optional models come from our download server. If the credit server cannot be reached, your work goes on.</p>
''',
    vf_title='Check it runs on your PC',
    vf='<p>If your PC meets these needs, install Tunedzy and clean a short recording first, to see how it performs.</p>',
    faq=[('Will it run on an older PC?', 'It may, but more slowly. Test with a short recording first.'),
         ('Do I need a microphone?', 'Only for live use and for recording. Cleaning an existing file needs no microphone.'),
         ('Does it need an NVIDIA card?', 'No. The card only speeds up the optional AI separation.')],
    related=['install-tunedzy-on-windows', 'tunedzy-troubleshooting', 'tunedzy-privacy-explained'])

add('tunedzy-privacy-explained', 'help', 'booth', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='Tunedzy Privacy Explained: What Stays on Your Device',
    desc='What Tunedzy sends and keeps: your audio never leaves your device, what the credit server sees, what the download server does and how to delete your account.',
    h1='Tunedzy Privacy Explained',
    kw='tunedzy privacy',
    lead='Your recordings stay on your device. The only things that go online are the credit count, the download of updates and models, and payments. Here is each one, in plain words.',
    tldr=['Your audio, projects and transcripts are processed and stored on your device.',
          'The credit server receives a device token, the app version and a one-way hash of the PC identifier.',
          'The download server serves updates and optional models; it does not receive your audio.',
          'Payments are handled by the payment provider; we do not see your card.'],
    body='''
<h2>What stays on your device</h2>
<p>Recordings, edits, transcripts, projects and exports are created and kept on your PC or phone. Processing happens there. Tunedzy does not upload your audio to process it.</p>
<h2>What the credit server sees</h2>
<p>To count your credits, the app sends a device token, its version and a one-way hash of the PC identifier, so one PC gets one welcome month. It does not send your audio, file names or project contents. The account keeps your login name, credits, passes and purchases.</p>
<h2>What the download server does</h2>
<p>It serves the installer, updates and optional models. Downloading a model does not send anything about your recordings.</p>
<h2>Payments</h2>
<p>Purchases are handled by the payment provider. We do not see or store your card details.</p>
<h2>Deleting your account</h2>
<p>Email fuidzy@outlook.com from the address on the account, or give the account name, and we will delete it. The full statement is in the <a href="/tunedzy/privacy">privacy policy</a>.</p>
''',
    vf_title='Your audio stays with you',
    vf='<p>Tunedzy processes your recordings on your own device. Read the privacy policy for the full statement.</p>',
    faq=[('Does Tunedzy read my files?', 'No. Your files are read on your device to process them. They are not sent to us.'),
         ('Can you see what I process?', 'No. We see credit counts and purchases, not what you process.'),
         ('Is Tunedzy Go private too?', 'Tunedzy Go processes the file in your browser. Nothing is uploaded.')],
    related=['tunedzy-system-requirements', 'install-tunedzy-on-windows', 'voice-cleaner-alternatives'])

add('what-happens-when-tunedzy-credits-run-out', 'help', 'mic', ['lufs-meter', 'vocal-checker'],
    title='What Happens When Tunedzy Credits Run Out',
    desc='What you can still do when your credits are used up: what waits, what still opens, how the next free pass arrives and how to buy more.',
    h1='What Happens When Tunedzy Credits Run Out',
    kw='what happens when tunedzy credits run out',
    lead='When your credits run out, nothing is deleted. Your projects still open and play, and processing waits until a credit is available. Here is how the next one arrives.',
    tldr=['Your projects, recordings and exports are kept; nothing is deleted.',
          'Opening, listening and the Credits screen cost nothing.',
          'Processing and exporting wait for a credit.',
          'A free pass arrives later, or you can buy a pack or a plan.'],
    body='''
<h2>What still works</h2>
<p>You can open your projects, listen to them, look at the Credits screen and read the guides. Looking at things never costs a credit.</p>
<h2>What waits</h2>
<p>Processing, repair, exporting and the AI steps need a credit. When none is available, the app tells you, and the work waits. Nothing is lost.</p>
<h2>How the next free pass arrives</h2>
<p>A free pass comes in a set order: during your first month, a pass arrives a day after you run out, up to three times, and then a monthly pass arrives. If you run out after that, a small weekly pass arrives seven days later. The Credits screen shows when the next one is due.</p>
<h2>Buying more</h2>
<p>You can buy a pack of 8 credits or 20 credits, or take a plan with no counting. Credits you buy do not expire. The <a href="/tunedzy/pricing">pricing page</a> lists the options.</p>
<h2>Tunedzy Go</h2>
<p>Tunedzy Go is free and does not use credits, so a phone cleanup is always available.</p>
''',
    vf_title='See when the next credit arrives',
    vf='<p>The Credits screen in Tunedzy shows the next free pass and the options to buy more.</p>',
    faq=[('Do my files get deleted?', 'No. Nothing is deleted when credits run out.'),
         ('Can I still open a project?', 'Yes. You can open and listen to projects; processing waits for a credit.'),
         ('Does a credit last a day?', 'A credit covers 24 hours of use of Tunedzy and Streamdzy from its first use in a day.')],
    related=['tunedzy-troubleshooting', 'tunedzy-privacy-explained', 'tunedzy-go-faq'])

add('tunedzy-troubleshooting', 'help', 'neon-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Tunedzy Troubleshooting: No Sound, Won’t Start, Export Fails',
    desc='Fix common Tunedzy problems: no sound, the app will not start, an export fails, a phone file will not open and what to check first.',
    h1='Tunedzy Troubleshooting',
    kw='tunedzy troubleshooting',
    lead='Most problems come from the audio device, a blocked port, a full disk or an unsupported file. Check those in order before you reinstall.',
    tldr=['No sound: check the input and output devices in Windows and in Tunedzy.',
          'The app will not start: check the antivirus and the firewall, then restart the PC.',
          'An export fails: check the free disk space and the file type.',
          'A phone file will not open: try Tunedzy Go, or convert the file first.'],
    body='''
<h2>No sound or no microphone</h2>
<p>Check that Windows has the right microphone and output device selected, and that the microphone is not muted in Windows. In Tunedzy, check the input and output choices on the Live Studio or Connect screen. Restart the app after you change a device.</p>
<h2>The app will not start</h2>
<p>Restart the PC first. Check that your antivirus did not quarantine the app, and that the firewall allows it on private networks. The engine uses port 8000 when it is free; if another program is using it, Tunedzy picks a free port by itself. Reinstall only if these checks fail.</p>
<h2>An export fails</h2>
<p>Check the free disk space on the drive where the exports go. Make sure the file name does not contain unusual characters, and that the file is not open in another program.</p>
<h2>A file will not open</h2>
<p>Most common audio and video formats work. Phone formats that the system does not read can be converted first. Tunedzy Go reads many phone files directly in a browser.</p>
<h2>Still stuck</h2>
<p>Email fuidzy@outlook.com with what you were doing, the file type and a screenshot if you can. We read every message.</p>
''',
    vf_title='Test with a short file first',
    vf='<p>Test any fix with a short recording. If it works, use the full file.</p>',
    faq=[('Why does Tunedzy say it is out of credits?', 'Processing needs a credit. See the credits guide for what runs out and what to do.'),
         ('Can I reinstall without losing my projects?', 'Your projects are kept in your Tunedzy folder under your user profile; check that folder before any reinstall.'),
         ('Is there a log I can send?', 'Describe the problem and the steps. We will ask for more detail if it helps.')],
    related=['install-tunedzy-on-windows', 'what-happens-when-tunedzy-credits-run-out', 'tunedzy-system-requirements'])

add('tunedzy-go-faq', 'help', 'hero-wide', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='Tunedzy Go FAQ: Using the Free Phone App',
    desc='Answers about Tunedzy Go, the free phone app: how to add it to the home screen, offline use, the first Studio sound download and what it does with your recordings.',
    h1='Tunedzy Go FAQ',
    kw='tunedzy go faq',
    lead='Tunedzy Go is the free phone app: it cleans a recording or a file in your browser, with nothing uploaded. Here are the questions people ask most.',
    tldr=['Open the Tunedzy Go page in your phone browser and add it to the home screen.',
          'It works offline after the first visit.',
          'Studio sound downloads a small model the first time you use it.',
          'Nothing you record or choose is uploaded.'],
    body='''
<h2>Installing it</h2>
<p>Open <a href="/tunedzy/go/">Tunedzy Go</a> in your phone browser, then choose the browser&rsquo;s Add to Home Screen option. It opens full-screen like an app.</p>
<h2>Offline use</h2>
<p>After the first visit the app loads without a connection, so you can record and clean on a train or a plane. The first Studio sound use downloads a model of about 22 MB, which is then kept on the phone.</p>
<h2>What it does</h2>
<p>You can record audio or video, or pick a file, then clean it with Studio sound and the level and tone steps. You can compare Before and After, and share or save the result.</p>
<h2>Privacy</h2>
<p>Recordings and files are processed in the browser on your phone. Nothing is uploaded, and the app does not need an account.</p>
<h2>Limits</h2>
<p>It is a web app, so it has less control than the Windows app. For long projects, multitrack editing and the transcript, use the Windows app.</p>
''',
    vf_title='Clean on the phone for free',
    vf='<p>Open Tunedzy Go on your phone, record or choose a file, and clean it. Nothing is uploaded.</p>',
    faq=[('Is Tunedzy Go free?', 'Yes. It does not use credits.'),
         ('Does it work on iPhone and Android?', 'It is a web app for modern phone browsers. It has been tested in desktop Chromium so far; try it on your own phone first.'),
         ('Can I use it on a computer?', 'Yes. It runs in any modern browser on a computer too.')],
    related=['clean-up-a-phone-voice-recording', 'voice-note-sounds-better-on-an-iphone', 'tunedzy-privacy-explained'])

add('recording-consent-before-you-record', 'ethics', 'desk-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='Recording Consent: Before You Record Someone',
    desc='Recording people needs their consent in many places. What to ask, how to record openly, and why cleanup does not make a secret recording lawful.',
    h1='Recording Consent: Before You Record Someone',
    kw='recording consent before you record',
    lead='Before you record another person, check the rules where you are. Some places need everyone in the recording to agree; others need only one person. Asking first is the safe habit.',
    tldr=['Some places require everyone in a recording to agree; others need only one person.',
          'Tell people you are recording, and get their agreement on the recording.',
          'Do not record private conversations you were not part of.',
          'Cleaning a secret recording does not make it lawful to use.'],
    body='''
<h2>The rules vary</h2>
<p>Laws on recording differ by country and by state or region. Some places allow a recording when one participant knows about it. Others require every participant to agree. Check the rules for where you are and where the recording will be used.</p>
<h2>Ask and record the agreement</h2>
<p>Tell everyone at the start that you are recording and why. A short recorded yes at the beginning is good practice for interviews, podcasts and calls. Keep a note of who agreed and when.</p>
<h2>Private conversations</h2>
<p>Do not record conversations you were not part of, or that people expect to be private. Recording a private call without consent can break the law even when you are one of the speakers in some places.</p>
<h2>Using a recording</h2>
<p>Consent to record is not always consent to publish. Agree on how the recording will be used, and keep to it.</p>
<h2>Cleanup does not change the rules</h2>
<p>A cleaned recording is still a recording of the person. Tunedzy cleans the file you have; it does not make a recording lawful to make or to use. Check the rules before you record, not after.</p>
''',
    vf_title='Record openly, clean what you have',
    vf='<p>Tunedzy cleans the recordings you are allowed to use, on your own device. Get consent first.</p>',
    faq=[('Do I need consent for a phone call?', 'It depends on where you are. Check the rules for the place you and the other person are in.'),
         ('Is it enough to tell people I am recording?', 'Telling them is the start. Getting an agreement you can show is better, and some places require it.'),
         ('Can I use a recording of a public speech?', 'Public speeches are often easier to use, but the rules still vary. Check before you publish.')],
    related=['how-to-clean-up-an-interview-recording', 'audio-cleanup-for-journalists', 'tunedzy-privacy-explained'])

add('does-ai-cleanup-change-your-voice', 'ethics', 'booth-wide', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Does AI Cleanup Change Your Voice?',
    desc='What AI cleanup changes in a recording, what it does not do, and how to keep the voice sounding like you: it cleans the file, it does not invent a new voice.',
    h1='Does AI Cleanup Change Your Voice?',
    kw='does ai cleanup change your voice',
    lead='AI cleanup changes the noise, the room and the balance of a recording. It does not make a new voice or copy someone else&rsquo;s. Too much cleanup can make a voice sound different, so use the least that works.',
    tldr=['Cleanup changes noise, room sound and balance in the recording you have.',
          'Tunedzy does not clone or generate a voice.',
          'Heavy cleanup can change the tone and texture, so check the result against the original.',
          'Keep the original, and use the lowest setting that gives a clean result.'],
    body='''
<h2>What cleanup changes</h2>
<p>Noise, room sound, clicks, clipping, hum and the level and tone of a recording are what cleanup works on. These changes can make the voice sound more open or more even, which is the point.</p>
<h2>What it does not do</h2>
<p>Tunedzy does not clone a voice, does not generate speech and does not make one person sound like another. It processes the recording you already have.</p>
<h2>When a voice starts to sound different</h2>
<p>Very strong noise reduction, a gate set too high and heavy tone changes can make a voice sound thin, watery or artificial. The voice is still the same person, but the recording no longer sounds like them. Lower the setting until it sounds natural.</p>
<h2>Keep the original</h2>
<p>Keep the raw recording. If the cleaned version sounds wrong, you can go back to the original and clean it again, more gently.</p>
<h2>Where to read more</h2>
<p>The <a href="/tunedzy/blog/why-noise-reduction-makes-voice-sound-watery">watery sound guide</a> explains the most common way a voice changes, and how to avoid it.</p>
''',
    vf_title='Clean it, keep it yours',
    vf='<p>Tunedzy cleans the recording you have and keeps the original. Compare Before and After to keep the voice natural.</p>',
    faq=[('Can Tunedzy make me sound like someone else?', 'No. It cleans the recording; it does not change who is speaking.'),
         ('Why does my cleaned voice sound different?', 'Usually the cleanup was too strong. Use less and compare with the original.'),
         ('Is it safe to use AI cleanup on other people?', 'Only with their consent, and within the rules where you are.')],
    related=['remove-background-noise-from-a-voice-recording', 'my-voice-sounds-robotic-after-cleanup', 'recording-consent-before-you-record'])

add('how-to-make-a-voice-sound-close-and-intimate', 'how', 'booth', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Make a Voice Sound Close and Intimate',
    desc='Get a close, intimate voice for narration, podcasts and ASMR-style recordings: the mic distance, the proximity bass and how to control it.',
    h1='How to Make a Voice Sound Close and Intimate',
    kw='how to make a voice sound close intimate',
    lead='A close, intimate voice feels like someone is speaking right beside you. It comes from a close mic, a dry room and controlled bass, not from processing.',
    tldr=['A close mic gives intimacy, but it adds bass through the proximity effect.',
          'Control the bass with a high-pass filter, not by moving away.',
          'Keep the room dry, so the voice sounds close rather than far.',
          'Add a little presence for clarity, and keep it gentle.'],
    body='''
<h2>The mic distance</h2>
<p>Close to the mic, a voice sounds intimate. Very close, the low frequencies rise: an effect called proximity, which makes the voice boomy. Keep the mic close, but a few centimetres back from the mouth, and speak slightly off-axis to tame the bass.</p>
<h2>Control the bass</h2>
<p>A high-pass filter around 80 to 120 Hz removes the extra rumble and boom from proximity. Set it by ear: too high and the voice thins, too low and it booms. The <a href="/tunedzy/what-is-a-high-pass-filter">high-pass guide</a> explains the setting.</p>
<h2>A dry room</h2>
<p>Echo makes a voice sound far away. A dry, soft space keeps the voice close. Rugs, curtains and a closet of clothes do most of the work.</p>
<h2>Clarity</h2>
<p>A small lift in the presence range, around 2 to 5 kHz, helps the words sit forward without sounding harsh. Keep it modest.</p>
<h2>Check it</h2>
<p>Listen at normal volume and on a phone speaker. Intimate should feel warm and clear, not heavy or boomy.</p>
''',
    vf_title='Close, clear and warm',
    vf='<p>Tunedzy shapes the tone and removes rumble. Use Before and After to keep the closeness without the boom.</p>',
    faq=[('Is closer always more intimate?', 'Not always. Very close adds boom. Find the distance where the voice is warm and clear.'),
         ('What is the proximity effect?', 'The rise in bass when a directional mic is very close to the source. It is normal and can be controlled.'),
         ('Do I need a special mic?', 'A close mic in a dry room is the basis. The mic type matters less than the distance and the room.')],
    related=['what-is-a-high-pass-filter', 'what-is-an-equalizer', 'fix-a-muffled-voice-recording'])
