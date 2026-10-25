"""Batch 4d (25 October 2026): five comparisons and eight audience pages.

Comparison facts come from the vendors' public material and reviews checked on 25 October 2026. No prices are quoted; each page
sends the reader to the vendor's own site. GROUP_OF marks 'compare' or 'audience' for the hub.
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


# ----------------------------------------------------------------------------------- comparisons
add('tunedzy-vs-krisp', 'compare', 'mic', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='Tunedzy vs Krisp: Live Calls or Finished Recordings',
    desc='Krisp removes noise from live calls as they happen. Tunedzy cleans finished recordings. Here is which one to use for which job.',
    h1='Tunedzy vs Krisp',
    kw='krisp alternative recording',
    lead='Krisp is built to clean the sound of a live call, in real time, so the other person hears less of your room. Tunedzy is built to clean a recording after it is made. They solve different problems.',
    tldr=['Krisp works during a live call: it runs between your mic and the call app.',
          'Tunedzy works on finished recordings, with repair, editing and loudness.',
          'For a call that must sound clean as it happens, Krisp is the right tool.',
          'For a recording you want to edit and publish, Tunedzy is the right tool.'],
    body='''
<h2>What Krisp does</h2>
<p>Krisp is a noise-cancelling app for calls. It sits between your microphone and your calling app, and it removes background sound from your side and, if you choose, from the incoming audio too. The company describes its processing as running on your device rather than in the cloud. It works with most calling apps, because it presents itself as a microphone and speaker.</p>
<h2>What Tunedzy does</h2>
<p>Tunedzy processes recordings. Perfect it repairs clipping, clicks and hum, runs a studio sound model on the file, then levels and tones the voice. You can edit the recording by its transcript, mix several voices in Multitrack, and export at a loudness target. It is a recording tool, not a call tool.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>Krisp</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Main job</td><td>Clean a live call as it happens</td><td>Clean and finish a recording</td></tr>
<tr><td>Where it runs</td><td>On your device, between mic and call app</td><td>On your Windows PC or phone (Tunedzy Go)</td></tr>
<tr><td>Editing and mixing</td><td>Not its job</td><td>Transcript editing, Multitrack, fades</td></tr>
<tr><td>Loudness target</td><td>Not its job</td><td>Set a target and check the true peak</td></tr>
</tbody></table>
<h2>Use both</h2>
<p>Use Krisp so a call sounds clean while you talk. Record the call locally, then finish the recording in Tunedzy. Check Krisp&rsquo;s own site for its current plans and features.</p>
''',
    vf_title='Clean the call after you record it',
    vf='<p>Record the call locally, then finish the recording in Tunedzy. Tunedzy Go does a quick cleanup on your phone for free.</p>',
    faq=[('Can Tunedzy clean a live call?', 'Not in real time. The Windows app has a live microphone cleaner for streams; for calls, Krisp is built for that job.'),
         ('Which is better for a podcast interview?', 'Record each person locally, then clean and edit the recordings in Tunedzy.'),
         ('Does Krisp upload my audio?', 'The company says processing happens on your device. Check its current privacy statement.')],
    related=['how-to-clean-up-a-zoom-or-video-call-recording', 'how-to-record-a-remote-podcast-guest', 'voice-cleaner-alternatives'])

add('tunedzy-vs-izotope-rx', 'compare', 'desk', ['vocal-checker', 'voice-recorder-noise-cancellation'],
    title='Tunedzy vs iZotope RX: Simple Cleanup or Deep Repair',
    desc='iZotope RX is a professional repair suite with deep manual control. Tunedzy is simpler and automatic. Here is where each fits.',
    h1='Tunedzy vs iZotope RX',
    kw='izotope rx alternative',
    lead='iZotope RX is the professional standard for audio repair, with detailed tools for dialogue, reverb and noise. Tunedzy covers the common cleanup automatically, with less depth and far less to learn.',
    tldr=['RX is a deep, professional repair suite with many modules and manual control.',
          'Its dialogue tools include Dialogue Isolate, De-reverb and a Repair Assistant, according to its own material.',
          'Tunedzy automates the standard steps and reports what it did, with fewer controls.',
          'For a hard repair, RX is the stronger tool; for everyday cleanup, Tunedzy is quicker.'],
    body='''
<h2>What RX is good at</h2>
<p>RX is used in film, broadcast and post production for difficult repairs. Its dialogue modules, the Repair Assistant and its spectral tools let an engineer see and shape problems in detail. Its own material describes the newer Dialogue Isolate as using a neural network, with de-reverb built in for some versions. Check the current version and its licence on iZotope&rsquo;s site.</p>
<h2>What Tunedzy is good at</h2>
<p>Tunedzy runs the common steps for you: repair for clipping, clicks and hum, a studio sound model for noise, a level and tone step, and a loudness target with a true peak check. It also has a transcript editor, Multitrack and a spectral repair box in Quick edit. It is simpler, and it reports each step it takes.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>iZotope RX</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Depth of control</td><td>Deep, many modules</td><td>Simpler, automatic steps</td></tr>
<tr><td>Learning curve</td><td>Steep</td><td>Gentle</td></tr>
<tr><td>Hard repairs</td><td>Stronger</td><td>Limited to what it automates</td></tr>
<tr><td>Everyday cleanup</td><td>Possible, more steps</td><td>Quick, one pass</td></tr>
<tr><td>Price</td><td>Paid, check iZotope&rsquo;s site</td><td>Free on the phone; credits on the Windows app</td></tr>
</tbody></table>
<h2>Which to pick</h2>
<p>Pick RX for film, broadcast or a recording that needs detailed repair. Pick Tunedzy for podcasts, voiceovers, streams and home vocals, where a clean result in one pass matters more than every control.</p>
''',
    vf_title='Standard cleanup in one pass',
    vf='<p>Tunedzy runs the common repair, cleanup and loudness steps on your PC, and tells you what it changed.</p>',
    faq=[('Is Tunedzy as good as RX?', 'For everyday cleanup, it covers the common steps. For difficult repairs, RX gives far more control.'),
         ('Can I learn RX easily?', 'It takes time. Its modules are powerful, and the learning curve is steep.'),
         ('Does Tunedzy have spectral editing?', 'It has a spectral repair tool in Quick edit. It is simpler than RX&rsquo;s spectral tools.')],
    related=['tunedzy-vs-audacity', 'tunedzy-vs-adobe-audition', 'voice-cleaner-alternatives'])

add('tunedzy-vs-adobe-audition', 'compare', 'booth', ['voice-recorder-noise-cancellation', 'clean-streaming-mic'],
    title='Tunedzy vs Adobe Audition: Editor or Automatic Cleanup',
    desc='Adobe Audition is a full audio editor with spectral tools and multitrack. Tunedzy is an automatic cleanup and mix studio. Compare them honestly.',
    h1='Tunedzy vs Adobe Audition',
    kw='adobe audition alternative',
    lead='Adobe Audition is a full audio workstation for editing, restoration and mixing. Tunedzy is narrower: it cleans, edits by words, mixes voices and sets loudness, with much less to learn.',
    tldr=['Audition is a full editor with waveform, spectral and multitrack tools.',
          'Adobe describes its noise tools as real-time restoration and offline effects.',
          'Tunedzy automates the cleanup and the loudness, and edits by transcript.',
          'Audition is the stronger editor; Tunedzy is quicker for a finished voice.'],
    body='''
<h2>What Audition is for</h2>
<p>Audition is a professional editor. Its waveform and spectral displays let you find and select noise or artifacts exactly, and its multitrack editor layers clips, effects and markers. Adobe&rsquo;s documentation describes real-time restoration effects and offline processes for harder problems. It is a paid product, so check Adobe&rsquo;s current plans.</p>
<h2>What Tunedzy is for</h2>
<p>Tunedzy is for getting a voice to a finished state. It repairs, cleans, levels and tones the voice in one pass, edits the recording by its transcript, mixes voices and music in Multitrack, and exports at a loudness target with a true peak check. You do not need to learn each effect.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>Adobe Audition</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Main job</td><td>Full editor and restoration</td><td>Finishing a voice recording</td></tr>
<tr><td>Spectral editing</td><td>Yes, detailed</td><td>A spectral repair box in Quick edit</td></tr>
<tr><td>Multitrack</td><td>Full</td><td>Voices and music, with fades and ducking</td></tr>
<tr><td>Transcript editing</td><td>Not its focus</td><td>Core feature</td></tr>
<tr><td>Learning curve</td><td>Steep</td><td>Gentle</td></tr>
</tbody></table>
<h2>Which to pick</h2>
<p>Pick Audition if you edit audio in depth every day and want a full studio. Pick Tunedzy if you need a clean, finished voice and a transcript without the learning curve.</p>
''',
    vf_title='Finish the voice without the learning curve',
    vf='<p>Tunedzy cleans, edits by words and sets loudness in one app, on your own PC.</p>',
    faq=[('Can Tunedzy replace Audition?', 'For voice finishing and podcast editing, it covers most of the job. For full audio production, Audition is the stronger tool.'),
         ('Does Audition edit by transcript?', 'Recent versions add speech tools; check Adobe&rsquo;s documentation for what your version does.'),
         ('Which is faster for a podcast?', 'For a single voice finished in one pass, Tunedzy. For detailed editing, Audition.')],
    related=['tunedzy-vs-izotope-rx', 'tunedzy-vs-audacity', 'edit-a-podcast-by-its-words'])

add('tunedzy-vs-cleanvoice', 'compare', 'desk-wide', ['clean-streaming-mic', 'vocal-checker'],
    title='Tunedzy vs Cleanvoice: Upload or Stay on Your Device',
    desc='Cleanvoice is an online AI cleaner that works on uploaded files. Tunedzy works on your own device. Compare the cleanup, the privacy and the editing.',
    h1='Tunedzy vs Cleanvoice',
    kw='cleanvoice alternative',
    lead='Cleanvoice is an online tool: you upload a file, choose cleanup options such as filler removal and breath reduction, and download the result. Tunedzy does its cleanup on your own device.',
    tldr=['Cleanvoice works on uploaded files and offers filler, breath and mouth-sound options.',
          'Tunedzy processes files on your PC or phone, so your audio does not leave the device.',
          'Cleanvoice has a dedicated breath option; Tunedzy handles breaths manually.',
          'If the file must stay private, the on-device tool is the safer choice.'],
    body='''
<h2>How Cleanvoice works</h2>
<p>Cleanvoice takes an uploaded file, detects fillers, stutters, mouth noises and long silences, and offers options to reduce them. You review the options and download the cleaned file. Its own blog describes the steps and the accepted formats. Check its current plans and terms before you upload.</p>
<h2>How Tunedzy works</h2>
<p>Tunedzy processes the file on your computer or phone. The transcript, the repair, the studio sound and the mix stay with you. Tunedzy Go does a basic cleanup on your phone for free.</p>
<h2>The honest difference</h2>
<p>Cleanvoice has dedicated breath and mouth-sound options that Tunedzy does not have. Tunedzy handles breaths by hand, through the transcript and the Before and After check. Tunedzy keeps the audio on your device; Cleanvoice needs the file on its servers.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>Cleanvoice</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Where it runs</td><td>Online, on uploaded files</td><td>On your PC or phone</td></tr>
<tr><td>Filler and breath options</td><td>Yes, dedicated options</td><td>Fillers in the transcript; breaths by hand</td></tr>
<tr><td>Privacy</td><td>The file is uploaded</td><td>The file stays on your device</td></tr>
<tr><td>Loudness target</td><td>Not its focus</td><td>Set a target, true peak checked</td></tr>
</tbody></table>
<h2>Which to pick</h2>
<p>Pick Cleanvoice for quick breath and filler removal on a file you are happy to upload. Pick Tunedzy for private recordings, for a loudness target, and for work you want kept on your own device.</p>
''',
    vf_title='Keep the file on your device',
    vf='<p>Tunedzy cleans, transcribes and levels your recording on your own PC or phone. Nothing is uploaded.</p>',
    faq=[('Is Cleanvoice bad for privacy?', 'It is an upload service. Read its privacy terms before you send a private recording.'),
         ('Does Tunedzy remove breaths automatically?', 'No. Breaths are a manual step; the transcript and Before and After help you decide.'),
         ('Which is better for fillers?', 'Cleanvoice has a dedicated option. Tunedzy finds ums and uhs in the transcript so you can cut them one by one.')],
    related=['tunedzy-vs-descript', 'how-to-remove-breath-noise-from-a-voice-recording', 'voice-cleaner-alternatives'])

add('tunedzy-vs-garageband', 'compare', 'mic-wide', ['song-key-finder', 'bpm-finder'],
    title='Tunedzy vs GarageBand: Making Music or Finishing Voices',
    desc='GarageBand is a free music app on Apple devices for making songs. Tunedzy finishes voice recordings. Here is which one suits your job.',
    h1='Tunedzy vs GarageBand',
    kw='tunedzy vs garageband',
    lead='GarageBand is a free music-making app on Apple devices, with instruments, loops and recording. Tunedzy does not make music; it finishes voice recordings and mixes them with music you bring in.',
    tldr=['GarageBand is for making music: recording, instruments, loops and arrangement.',
          'Tunedzy is for finishing voices: repair, cleanup, transcripts, voice mixing and loudness.',
          'Tunedzy is not for making beats, and it is Windows-only for now.',
          'Many people use GarageBand to make a track and Tunedzy to finish the voice.'],
    body='''
<h2>What GarageBand is for</h2>
<p>GarageBand is a free app included with Apple devices. It records, arranges and mixes music, and includes instruments and loops. It is a strong starting point for making songs on a Mac or an iPhone. Check Apple&rsquo;s own page for the current version.</p>
<h2>What Tunedzy is for</h2>
<p>Tunedzy is for the voice: cleaning a rough recording, editing it by its words, mixing voices with music you bring in, and exporting at a loudness target. It does not make beats and does not run virtual instruments. The Windows app is the full version; Tunedzy Go runs in a phone browser for a quick cleanup.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>GarageBand</th><th>Tunedzy</th></tr></thead>
<tbody>
<tr><td>Main job</td><td>Making and arranging music</td><td>Finishing voice recordings</td></tr>
<tr><td>Instruments and loops</td><td>Yes</td><td>No</td></tr>
<tr><td>Voice cleanup</td><td>Basic tools</td><td>Repair, studio sound, level, tone</td></tr>
<tr><td>Transcript editing</td><td>Not its focus</td><td>Core feature</td></tr>
<tr><td>Platforms</td><td>Apple devices</td><td>Windows app, and Tunedzy Go in any browser</td></tr>
</tbody></table>
<h2>Use them together</h2>
<p>Make the track in GarageBand, record the vocal, then clean and level the vocal in Tunedzy and bring it back. Your beat stays in GarageBand.</p>
''',
    vf_title='Finish the voice, make the track elsewhere',
    vf='<p>Tunedzy finishes the vocal: cleanup, editing and loudness. Use it with any beat-making app you already have.</p>',
    faq=[('Can Tunedzy make a beat?', 'No. Use GarageBand or another beat-making app for that.'),
         ('Is GarageBand free?', 'It is included with Apple devices. Check Apple&rsquo;s site for the current details.'),
         ('Is there a Mac version of Tunedzy?', 'Not yet. A Mac build is being prepared; for now, Tunedzy Go works in a Mac browser.')],
    related=['record-a-vocal-at-home-for-a-song', 'what-is-a-condenser-vs-dynamic-microphone', 'voice-cleaner-alternatives'])

# ----------------------------------------------------------------------------------- audience
add('voice-cleanup-for-youtube-creators', 'audience', 'neon', ['lufs-meter', 'vocal-checker'],
    title='Voice Cleanup for YouTube Creators',
    desc='A practical audio routine for YouTube creators: recording the voice, cleaning it, setting the loudness and putting it back into the video.',
    h1='Voice Cleanup for YouTube Creators',
    kw='audio cleanup for youtube creators',
    lead='YouTube viewers judge a video on its sound within seconds. A short, repeatable audio routine gives a steady voice across every upload.',
    tldr=['Record the voice in the same spot every time, and keep the settings the same.',
          'Clean every video with the same settings, then check the loudness.',
          'Put the cleaned voice back into the video without re-encoding the picture.',
          'Keep the master, so you can re-export when the rules change.'],
    body='''
<h2>The routine</h2>
<p>Record in the same corner, with the same mic distance and level. Save the raw voice files in one folder per video. Clean each one with the same settings, check the loudness, and put the voice back into the edit.</p>
<h2>What to listen for</h2>
<p>Listen for room echo, fan noise, mouth clicks and any change in level between sections. Fix the cause on the next recording rather than cleaning harder each time.</p>
<h2>Loudness</h2>
<p>Set the voice to a target for online video and check the true peak. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the targets people use.</p>
<h2>Keep a master</h2>
<p>Keep the cleaned voice as a master so you can re-export it. The <a href="/tunedzy/how-to-choose-wav-mp3-or-flac">format guide</a> explains why.</p>
''',
    vf_title='One routine for every video',
    vf='<p>Tunedzy cleans the voice the same way every time, sets the loudness, and puts the sound back into your video.</p>',
    faq=[('How long does the routine take?', 'It depends on the length of the video. Once the settings are saved, it is mostly listening.'),
         ('Should I use the same settings every time?', 'Start there, then adjust only when the recording changes.'),
         ('Do I need a studio?', 'No. A consistent quiet corner matters more than studio equipment.')],
    related=['how-to-record-audio-for-youtube-videos', 'put-clean-audio-back-into-a-video', 'record-a-voiceover-on-your-phone'])

add('audio-cleanup-for-tiktok-creators', 'audience', 'neon-wide', ['clean-streaming-mic', 'voice-recorder-noise-cancellation'],
    title='Audio Cleanup for TikTok Creators',
    desc='Clean voiceovers and talking clips for TikTok: a quick phone workflow, the room and distance tips, and what to fix before you post.',
    h1='Audio Cleanup for TikTok Creators',
    kw='audio cleanup for tiktok creators',
    lead='Short clips are judged in the first seconds. A clean, close voice and a quick cleanup make a clip sound professional without a long edit.',
    tldr=['Record close to the phone in a soft space, even for a ten-second clip.',
          'Clean the take on the phone before you put it into the edit.',
          'Keep the voice clear over music by setting the music lower.',
          'Check the sound on a phone speaker, where most people will hear it.'],
    body='''
<h2>Record close and quiet</h2>
<p>A short clip gives you little time to recover. Record with the phone a hand&rsquo;s width from the mouth, in a room with soft things around, and turn off the fan.</p>
<h2>Clean on the phone</h2>
<p><a href="/tunedzy/go/">Tunedzy Go</a> cleans a take on your phone for free. Clean first, then put the cleaned sound into the edit, so you do not have to fix noise in a short clip with a tight deadline.</p>
<h2>Balance under music</h2>
<p>Keep the voice clearly above any music. If you have to strain to hear the words on a phone speaker, the music is too loud.</p>
<h2>Check on a phone</h2>
<p>Listen on the phone you will post from, at normal volume. What sounds good on headphones can sound thin on a phone speaker.</p>
''',
    vf_title='Clean the take before the edit',
    vf='<p>Tunedzy Go cleans a voiceover on your phone for free. Record, clean, then edit.</p>',
    faq=[('Can I clean a voiceover in the TikTok app?', 'Use the app for the edit; clean the voice first in Tunedzy Go or another tool.'),
         ('Why does my TikTok voice sound quiet?', 'The phone is far from the mouth, or the music is too loud. Move closer and lower the music.'),
         ('Do I need a mic?', 'Not to start. A phone close to the mouth in a soft room is a good base.')],
    related=['record-a-voiceover-on-your-phone', 'my-recording-is-too-quiet', 'why-does-my-phone-recording-sound-far-away'])

add('voice-cleanup-for-podcasters', 'audience', 'desk', ['clean-streaming-mic', 'lufs-meter'],
    title='Voice Cleanup for Podcasters',
    desc='A podcaster’s audio routine: recording each voice, cleaning per speaker, levelling, editing by words and exporting for the platforms.',
    h1='Voice Cleanup for Podcasters',
    kw='audio cleanup for podcasters',
    lead='A podcast is a series, so every episode should sound like the last. A repeatable routine for recording, cleaning and levelling keeps the show consistent.',
    tldr=['Record each speaker on their own track whenever you can.',
          'Clean and level each voice, then mix the episode.',
          'Edit by the transcript and cut the ums and long pauses.',
          'Export at a loudness target and keep the master.'],
    body='''
<h2>Record each voice on its own</h2>
<p>Separate tracks are the best foundation. If you cannot, record one phone or mic per speaker. The <a href="/tunedzy/how-to-record-a-podcast-on-your-phone">phone podcast guide</a> covers the setup.</p>
<h2>Clean per speaker</h2>
<p>Each person has a different room, mic and voice, so clean them separately. Use gentle settings and listen to each one on headphones.</p>
<h2>Level and mix</h2>
<p>Bring the voices to a similar loudness, then mix. The <a href="/tunedzy/how-to-level-voices-between-speakers">levelling guide</a> explains the steps.</p>
<h2>Edit and export</h2>
<p>Edit by the transcript, then export at a loudness target with the true peak checked. The <a href="/tunedzy/how-to-export-audio-for-spotify-and-apple-podcasts">export guide</a> covers the upload.</p>
''',
    vf_title='Clean, level and export every episode',
    vf='<p>Tunedzy cleans each voice, levels them in Multitrack, edits by words and exports the episode at a loudness target.</p>',
    faq=[('How long does a clean episode take?', 'It depends on the length. A routine makes it faster each time.'),
         ('Should I record each guest on their own track?', 'Yes, whenever you can. It is the best way to keep the balance.'),
         ('Do I need a separate editor?', 'Not for a basic show. Tunedzy handles cleanup, levelling and export in one place.')],
    related=['podcast-sound-professional-on-a-budget', 'edit-a-podcast-by-its-words', 'how-to-record-a-remote-podcast-guest'])

add('voice-cleanup-for-streamers', 'audience', 'hero-wide', ['clean-streaming-mic', 'live-autotune'],
    title='Voice Cleanup for Streamers',
    desc='Clean a streamer’s voice for live shows and recorded VODs: mic setup, live cleaning on Windows, and the clean-up of the recording afterwards.',
    h1='Voice Cleanup for Streamers',
    kw='voice cleanup for streamers',
    lead='A stream needs a voice that is clear live and clean in the replay. Set the mic well, clean it live, and keep a clean recording to fix later.',
    tldr=['Set the mic close and the room soft; live cleanup cannot fix a poor mic position.',
          'The Windows app has a live microphone cleaner for streams.',
          'Record the mic locally, so the replay can be cleaned properly.',
          'Clean the replay with gentle settings and check the loudness.'],
    body='''
<h2>Start with the mic</h2>
<p>Put the mic a hand&rsquo;s width from your mouth, a little off-axis, with a pop filter. A close mic in a soft room does more for a stream than any filter.</p>
<h2>Clean it live</h2>
<p>The Windows app has a live microphone cleaner, Live Studio, that cleans the voice as you stream. Set it once, then check the level during a quiet moment. The <a href="/tunedzy/tools/clean-streaming-mic">clean streaming mic tool</a> on this site shows the idea in your browser.</p>
<h2>Record locally</h2>
<p>Record your mic on the computer too. A local file is cleaner than the stream and lets you fix the replay properly.</p>
<h2>Clean the replay</h2>
<p>Clean the local file with gentle settings, then check the loudness before you post the VOD. The <a href="/tunedzy/how-to-clean-up-a-zoom-or-video-call-recording">call cleanup guide</a> has the same sequence.</p>
''',
    vf_title='Clean it live, fix the replay',
    vf='<p>Live Studio cleans the mic during the stream on Windows; Tunedzy finishes the recording afterwards.</p>',
    faq=[('Does live cleanup add delay?', 'A little. Check the delay on your setup before a stream.'),
         ('Can I clean a VOD after the stream?', 'Yes. Record the mic locally and clean the file in Tunedzy.'),
         ('Do I need a special mic?', 'A close, well-placed mic in a soft room is the base. Cleanup helps with the rest.')],
    related=['remove-background-noise-from-a-voice-recording', 'how-to-set-up-a-quiet-recording-corner-on-a-budget', 'how-to-record-with-a-usb-microphone'])

add('voice-cleanup-for-voice-actors', 'audience', 'booth', ['voice-recorder-noise-cancellation', 'lufs-meter'],
    title='Voice Cleanup for Voice Actors and Voiceover Artists',
    desc='A voiceover artist’s cleanup routine: a consistent booth, clean takes, the loudness that clients expect and clean deliverables.',
    h1='Voice Cleanup for Voice Actors',
    kw='audio cleanup for voice actors',
    lead='A voiceover is judged on how clean and consistent it sounds. A repeatable booth and a careful cleanup make every take sound like the same session.',
    tldr=['Keep the booth and the mic position the same for every session.',
          'Clean gently: a voiceover needs clear, natural speech.',
          'Deliver to the loudness the client asks for, with a true peak check.',
          'Keep the raw takes and the cleaned masters.'],
    body='''
<h2>Keep the booth consistent</h2>
<p>A client may book you again in a month. Keep the same booth, the same mic position and the same level, and write the settings down. A consistent room is what makes two sessions sound like one voice.</p>
<h2>Clean gently</h2>
<p>A voiceover must sound natural. Use the lowest cleanup that works, and listen for any watery or thin sound. The <a href="/tunedzy/blog/why-noise-reduction-makes-voice-sound-watery">watery sound guide</a> explains what to avoid.</p>
<h2>Deliver to the brief</h2>
<p>Clients often name a loudness or a format. Set the level to their target and check the true peak before you send the file.</p>
<h2>Keep the masters</h2>
<p>Keep the raw take and the cleaned master for each job. The <a href="/tunedzy/how-to-choose-wav-mp3-or-flac">format guide</a> explains which to keep.</p>
''',
    vf_title='Clean, level and deliver',
    vf='<p>Tunedzy cleans the take gently, sets the loudness the client asks for and exports the master.</p>',
    faq=[('What loudness should a voiceover be?', 'It depends on the client and the platform. The voice-over loudness guide on this site covers the common targets.'),
         ('Should I clean every take?', 'Clean the takes you deliver. Keep the raw takes so you can re-process later.'),
         ('Do I need a professional booth?', 'Not always. A consistent quiet room is the practical start.')],
    related=['record-a-voiceover-on-your-phone', 'how-to-record-an-audiobook-at-home', 'loudness-for-youtube-podcasts-and-spotify'])

add('vocal-cleanup-for-singers-and-rappers', 'audience', 'neon', ['song-key-finder', 'bpm-finder', 'chord-finder'],
    title='Vocal Cleanup for Singers and Rappers',
    desc='A singer’s or rapper’s home vocal workflow: a clean take, the key and tempo, light tuning and a level that sits on the beat.',
    h1='Vocal Cleanup for Singers and Rappers',
    kw='vocal cleanup for singers and rappers',
    lead='A home vocal sounds finished when the take is clean, the key and tempo match the beat, and the level sits well on the track. Each step is simple on its own.',
    tldr=['Record a clean, dry take in a soft room.',
          'Match the vocal to the key and tempo of the beat.',
          'Clean, level and tune lightly, listening after each step.',
          'Keep the takes, so you can comp the best parts later.'],
    body='''
<h2>The take</h2>
<p>Record dry, with no effects, in a soft room. Several takes of each section give you choice later. Keep the mic a steady distance and the level at the same place.</p>
<h2>Key and tempo</h2>
<p>Find the key and tempo of the beat first, so the vocal can match them. The <a href="/tunedzy/tools/song-key-finder">song key finder</a> and the <a href="/tunedzy/tools/bpm-finder">BPM finder</a> measure both in your browser.</p>
<h2>Clean, level and tune</h2>
<p>Clean the takes gently, level the vocal so it sits clearly above the beat, and tune lightly. The <a href="/tunedzy/how-to-clean-a-song-vocal-recorded-on-a-phone">phone vocal guide</a> has the steps in order.</p>
<h2>Keep the choice</h2>
<p>Keep the other takes until the song is finished. The best parts often come from different takes.</p>
''',
    vf_title='Clean the vocal, sit it on the beat',
    vf='<p>Tunedzy cleans the vocal, lines it up in Multitrack and exports the mix at a loudness target. Your beat stays in your own DAW.</p>',
    faq=[('Do I need a pro mic to sound good?', 'No. A clean take in a soft room matters more than the mic.'),
         ('Should I tune every note?', 'A light touch sounds more natural. Heavy tuning sounds robotic.'),
         ('Can I use this for a release?', 'A clean home vocal can work well. Check the mix on several speakers before you release it.')],
    related=['record-a-vocal-at-home-for-a-song', 'how-to-clean-a-song-vocal-recorded-on-a-phone', 'clean-up-a-phone-voice-recording'])

add('audio-cleanup-for-teachers', 'audience', 'desk-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='Audio Cleanup for Teachers and Course Makers',
    desc='Make lessons and course recordings clear for students: a practical room setup, a steady voice, cleanup and captions for accessibility.',
    h1='Audio Cleanup for Teachers and Course Makers',
    kw='audio cleanup for teachers',
    lead='Students learn better when they can hear the teacher clearly. A quiet room, a steady level and a gentle cleanup make a lesson recording easy to follow.',
    tldr=['A steady voice at a steady level is easier to follow than a loud, quiet mix.',
          'Record in a quiet room and switch off the fans for the take.',
          'Clean gently, then add captions from the transcript.',
          'Check the recording on a phone, where many students will listen.'],
    body='''
<h2>Clear voice first</h2>
<p>A calm voice at a steady level helps students follow. Keep the mic at a steady distance and speak a little more slowly than in conversation.</p>
<h2>Clean gently</h2>
<p>Clean the room noise and any clicks. Keep the voice natural, because a robotic lesson is tiring. The <a href="/tunedzy/clean-up-a-phone-voice-recording">phone cleanup steps</a> apply to a lesson too.</p>
<h2>Captions for everyone</h2>
<p>Captions help students who are deaf or hard of hearing, and help everyone who listens in a noisy place. A transcript made on your PC exports as captions; check the wording before you publish.</p>
<h2>Check on a phone</h2>
<p>Listen on a phone speaker and on headphones. Many students will hear the lesson that way.</p>
''',
    vf_title='Clean the lesson, add captions',
    vf='<p>Tunedzy cleans the lesson, transcribes it on your PC and exports captions. Nothing is uploaded.</p>',
    faq=[('Do captions need to be perfect?', 'They should be accurate. Check names and technical words before you publish.'),
         ('How do I record a lesson at home?', 'Use the lecture voice guide on this site: a quiet room, a steady level and short sections.'),
         ('Is this accessible?', 'Captions and clear audio help many students, including those who are deaf or hard of hearing.')],
    related=['how-to-record-a-lecture-or-tutorial-voice', 'edit-a-podcast-by-its-words', 'how-to-record-an-audiobook-at-home'])

add('audio-cleanup-for-journalists', 'audience', 'booth-wide', ['voice-recorder-noise-cancellation', 'vocal-checker'],
    title='Audio Cleanup for Journalists and Interviewers',
    desc='Clean interview and field recordings for publication: keeping the speaker natural, handling noise on location, and checking the quotes.',
    h1='Audio Cleanup for Journalists',
    kw='audio cleanup for journalists',
    lead='For journalism, the audio must be clean, but it must also be true. Clean gently, keep the original, and check every quote against the recording.',
    tldr=['Keep the original recording, unaltered, as the record.',
          'Clean gently so the speaker still sounds like themselves.',
          'Check every quote against the original before you publish.',
          'Note what you changed, if the story needs that transparency.'],
    body='''
<h2>Keep the original</h2>
<p>Store the original recording as received, with its date and where it was made. Work only on copies. If a question comes up later, the original is the record.</p>
<h2>Clean gently</h2>
<p>Field recordings have wind, traffic and room noise. Clean enough to hear the speaker, and no more. A speaker who sounds like a different person is a problem for the story, not a success. The <a href="/tunedzy/how-to-remove-wind-noise-from-audio">wind guide</a> and the <a href="/tunedzy/how-to-clean-up-an-interview-recording">interview guide</a> cover the common cases.</p>
<h2>Check the quotes</h2>
<p>A transcript helps you find quotes, but speech models can mishear names and technical words. Check every quote against the audio before it goes out.</p>
<h2>Be open about editing</h2>
<p>Cutting ums is normal. Changing what someone said is not. Keep the meaning, and note any editing that matters to the story.</p>
''',
    vf_title='Clean the recording, keep it true',
    vf='<p>Tunedzy cleans field recordings on your PC, transcribes them for quote-finding and keeps the original untouched.</p>',
    faq=[('Can I edit an interview for length?', 'Yes, with care. Do not change the meaning of what was said, and keep the original.'),
         ('Should I tell listeners about edits?', 'It depends on the story and the outlet. Follow your newsroom&rsquo;s rules.'),
         ('Is the transcript reliable enough to quote from?', 'Use it to find the quote, then check the audio before you publish.')],
    related=['how-to-clean-up-an-interview-recording', 'how-to-remove-wind-noise-from-audio', 'edit-a-podcast-by-its-words'])
