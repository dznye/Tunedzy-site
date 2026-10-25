"""Batch 5e (25 October 2026): five help pages. Facts come from the app's own menus and the account design as of 25 October 2026:
Help menu items, the Fuidzy login and recovery key, the device limit, the open-source notices and the report-a-problem tool.

GROUP_OF marks every page 'help' for the guides hub.
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
    GROUP_OF[slug] = 'help'


add('how-to-enter-a-lifetime-license-key', 'desk', ['vocal-checker', 'lufs-meter'],
    title='How to Enter a Lifetime License Key in Tunedzy',
    desc='Enter a Tunedzy lifetime license key from the Help menu, check it has been accepted, and what to do if the key does not work.',
    h1='How to Enter a Lifetime License Key',
    kw='how to enter tunedzy license key',
    lead='A lifetime key bought before the credit system unlocks everything in Tunedzy. You enter it once from the Help menu, and then no credits are needed.',
    tldr=['Open Help in the menu bar, then choose License key (lifetime).',
          'Paste the key from your receipt and confirm it.',
          'A key bought before credits unlocks everything, without counting use.',
          'If the key is refused, check it for spaces and write to support.'],
    body='''
<h2>Find your key</h2>
<p>The key came in the email you received when you bought Tunedzy. Copy it exactly, without extra spaces. If you cannot find it, check your spam folder, then write to fuidzy@outlook.com with the email address you bought with.</p>
<h2>Enter it</h2>
<p>In Tunedzy, open the Help menu and choose License key (lifetime). Paste the key and confirm. The app checks the key and then unlocks the features it covers.</p>
<h2>What it unlocks</h2>
<p>A lifetime key unlocks everything without counting use or needing credits. The key is checked online the first time it is entered.</p>
<h2>If it is refused</h2>
<p>Check for a missing or extra character, and that you are not copying the words around the key. Make sure you are connected, since the first check is online. If it still fails, write to support with the email you bought with, and do not post the key in a public forum.</p>
''',
    vf_title='Use the key, then get on with the work',
    vf='<p>Once the key is entered, Tunedzy processes without counting credits. Explore the Credits screen to confirm.</p>',
    faq=[('Do I need credits with a lifetime key?', 'No. A lifetime key bought before the credit system unlocks everything.'),
         ('Can I give my key to someone else?', 'Read the terms that came with your purchase, and follow them.'),
         ('I lost my key. What do I do?', 'Write to fuidzy@outlook.com with the email you bought with. We will help you find it.')],
    related=['how-to-sign-in-with-your-fuidzy-login', 'what-happens-when-tunedzy-credits-run-out', 'install-tunedzy-on-windows'])

add('how-to-sign-in-with-your-fuidzy-login', 'desk-wide', ['vocal-checker', 'lufs-meter'],
    title='How to Sign In With Your Fuidzy Login',
    desc='Create or sign in to your Fuidzy login in Tunedzy, keep the recovery key safe and use the same login in Streamdzy.',
    h1='How to Sign In With Your Fuidzy Login',
    kw='how to sign in fuidzy login tunedzy',
    lead='Your Fuidzy login keeps your credits and passes in one place, shared with Streamdzy. You create it once, and sign in on the other app with the same details.',
    tldr=['Open Help and choose Credits and login, then create a login with a name and a PIN.',
          'Save the recovery key the app shows you. It is shown once.',
          'In Streamdzy, choose I already have one and sign in with the same login.',
          'Each PC gets its own device token, up to five PCs per login.'],
    body='''
<h2>Create a login</h2>
<p>Open Help in Tunedzy, then choose Credits and login. Choose a name and a PIN. An email is optional. The app creates your account in the background, if one was not already made.</p>
<h2>Keep the recovery key</h2>
<p>The app shows a recovery key once. Write it down or store it in a password manager. If you lose your PIN and the key, the account can be hard to get back, so do not skip this step.</p>
<h2>Use it in Streamdzy</h2>
<p>In Streamdzy, open the credits and login screen and choose I already have one. Enter the same name and PIN. Both apps then use the same credits and passes.</p>
<h2>What is shared</h2>
<p>Credits, passes, purchases and the 24-hour window are shared. One day opened in one app is a day in the other. Your audio is not shared; it stays on the device you process it on.</p>
''',
    vf_title='One login, both apps',
    vf='<p>Create your Fuidzy login in Tunedzy, keep the recovery key, and sign in to Streamdzy with the same details.</p>',
    faq=[('Do I need an email for the login?', 'No. An email is optional. It helps if you ever need to recover the account.'),
         ('What if I forget my PIN?', 'Use the recovery key. Keep it safe, because without it recovery is difficult.'),
         ('Does my audio go to the account?', 'No. The account holds credits and purchases. Your recordings stay on your device.')],
    related=['using-tunedzy-on-more-than-one-pc', 'tunedzy-privacy-explained', 'how-to-enter-a-lifetime-license-key'])

add('using-tunedzy-on-more-than-one-pc', 'desk', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Using Tunedzy on More Than One PC',
    desc='How one Fuidzy login works on more than one PC: the device limit, how credits are shared, and what to do when you change computers.',
    h1='Using Tunedzy on More Than One PC',
    kw='using tunedzy on more than one pc',
    lead='One Fuidzy login can be used on up to five PCs. Each PC has its own device token, and the credits belong to the login, so they follow you between computers.',
    tldr=['A login can be used on up to five PCs.',
          'Each PC gets its own device token when you sign in.',
          'Credits belong to the login and are shared across the PCs you sign in on.',
          'A lifetime key follows the terms you received with it.'],
    body='''
<h2>How the limit works</h2>
<p>The login allows up to five PCs. Signing in on a new PC gives that PC its own device token. The token is how the credit server knows which PC is using the login.</p>
<h2>Credits</h2>
<p>Credits and passes belong to the login, not to a PC. Use the same login on any of your PCs, and the credit rules apply the same way: the first use in a day takes one credit, and it covers 24 hours of both apps.</p>
<h2>When you change PCs</h2>
<p>Sign in on the new PC with your login. If you are at the limit, remove an old PC from your account first; if the Credits screen does not offer that, write to fuidzy@outlook.com. Keep your recovery key ready.</p>
<h2>Lifetime keys</h2>
<p>A lifetime key has its own terms, including how many PCs it covers. Check the email you received when you bought it.</p>
''',
    vf_title='Sign in on each PC, credits follow you',
    vf='<p>Sign in to your Fuidzy login on each PC. Credits belong to the login and work the same way on any of them.</p>',
    faq=[('Can I use it on five PCs at once?', 'The limit is five PCs per login. Sign out of one to add another if you reach it.'),
         ('Do my projects move between PCs?', 'No. Projects and recordings stay on the PC where they were made. Copy the files yourself if you need them elsewhere.'),
         ('Do lifetime keys have the same limit?', 'Lifetime keys follow their own terms. Check the email you received when you bought the key.')],
    related=['how-to-sign-in-with-your-fuidzy-login', 'tunedzy-privacy-explained', 'what-happens-when-tunedzy-credits-run-out'])

add('open-source-notices-explained', 'desk-wide', ['vocal-checker', 'lufs-meter'],
    title='Open-Source Notices in Tunedzy: What They Are',
    desc='Where to find Tunedzy open-source notices in the Help menu, what they list, and why a voice app ships third-party software and licences.',
    h1='Open-Source Notices in Tunedzy',
    kw='tunedzy open source notices',
    lead='Tunedzy includes open-source software, and we say so openly. The notices list each component, its licence and where its code comes from.',
    tldr=['Open Help and choose Open-source notices to read the full list.',
          'The list includes components such as FFmpeg, Whisper and DeepFilterNet.',
          'Each component keeps its own licence, which the notices name.',
          'Tunedzy does not ship a GPL build of FFmpeg.'],
    body='''
<h2>Where to find them</h2>
<p>Open Help in Tunedzy and choose Open-source notices. The notices open in a browser window.</p>
<h2>What they list</h2>
<p>The notices list the software Tunedzy includes, such as FFmpeg, which runs as a separate program under the LGPL, the Whisper speech model under the MIT licence, DeepFilterNet under the MIT or Apache licence, and the other libraries the app uses.</p>
<h2>What it means for you</h2>
<p>You may use the bundled software under the terms in the notices. Tunedzy does not ship a GPL build of FFmpeg; the FFmpeg it uses is an LGPL build, checked when the app is built.</p>
<h2>If you have a question</h2>
<p>Write to fuidzy@outlook.com if a notice is unclear or you believe a licence is missing. We will check and update the notices.</p>
''',
    vf_title='What is inside Tunedzy',
    vf='<p>Open-source notices are in the Help menu. Read them to see each component and its licence.</p>',
    faq=[('Why does a voice app include FFmpeg?', 'FFmpeg reads and writes many audio and video formats. Tunedzy runs it as a separate program.'),
         ('Is the Whisper model open source?', 'Its weights are published under the MIT licence. The notices give the details.'),
         ('Can I see the source of the components?', 'Each component has a public source. The notices name where to find it.')],
    related=['tunedzy-privacy-explained', 'install-tunedzy-on-windows', 'how-to-report-a-problem-in-tunedzy'])

add('how-to-report-a-problem-in-tunedzy', 'desk', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='How to Report a Problem in Tunedzy',
    desc='Use Report a problem in Tunedzy to send the app version and recent error messages, what it does not send, and how to add a useful description.',
    h1='How to Report a Problem in Tunedzy',
    kw='how to report a problem in tunedzy',
    lead='The Report a problem tool sends the app version and the recent error messages. It never sends your audio. A short description with the steps you took helps us most.',
    tldr=['Open Help and choose Report a problem.',
          'The report includes the app version and recent error messages.',
          'It never includes your audio or your project files.',
          'Add what you were doing, the file type and what you expected to happen.'],
    body='''
<h2>How to send one</h2>
<p>Open Help in Tunedzy and choose Report a problem. The report adds the app version and the recent error messages. Add a short description of what you were doing.</p>
<h2>What is not sent</h2>
<p>The report never includes your audio, your recordings or your project files. It is for the app&rsquo;s behaviour, not your work.</p>
<h2>What helps most</h2>
<ul>
<li>The steps you took, in order.</li>
<li>The type of file you were working with, such as WAV, MP3 or MP4.</li>
<li>What you expected to happen, and what happened instead.</li>
<li>A screenshot, if it shows the problem clearly.</li>
</ul>
<h2>If the report does not open</h2>
<p>Email fuidzy@outlook.com with the same details. Describe the steps and the version number from the About screen.</p>
''',
    vf_title='Tell us what happened',
    vf='<p>The Report a problem tool sends the app version and error messages, never your audio. Add the steps you took.</p>',
    faq=[('Does the report include my recordings?', 'No. It sends the version and recent error messages only.'),
         ('Will someone reply?', 'We read every message. Include an email address if you want a reply.'),
         ('What if the problem is with my file?', 'Say which format it is. If it is a phone format, Tunedzy Go may help while we look.')],
    related=['tunedzy-troubleshooting', 'tunedzy-privacy-explained', 'open-source-notices-explained'])
