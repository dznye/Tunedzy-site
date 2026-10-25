"""Blog posts, batch 12 of 20: video podcasts and audio-first shows. Merged into content_blog.py.
Platform facts are attributed to the company or to a named report. Where a date or feature was reported but not
confirmed on the company's own page, the post says so and points readers to the official source.
No invented statistics. Funnel: each post ends with a link to Tunedzy Go and to the matching free tool."""

CLUSTERS = {
    'trend-video-podcast': dict(tool='vocal-checker', label='Video podcasts and audio-first shows', tool_name='Vocal Checker'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='apple-video-podcasts-explained', cluster='trend-video-podcast', kw='apple video podcasts',
    title='Apple Video Podcasts Explained: What Changed and What to Do',
    desc='Apple video podcasts explained: the February 2026 announcement, switching between video and audio, video ads and what podcasters should prepare now.',
    h1='Apple Video Podcasts Explained: What Changed and What to Do',
    answer='Apple announced video podcasts in February 2026, letting listeners switch between watching and listening in the same episode. For podcasters, the practical steps are to keep a clean audio master, make video episodes that still work as audio, and check Apple&rsquo;s own newsroom for the release timing.',
    body='''
<p>In February 2026 Apple announced a video podcast feature for its Podcasts app. The headline is simple: a listener can watch an episode and then carry on with audio only, without losing their place. For a medium that has spent two decades as audio, that is a meaningful change. This post explains what Apple said, what was reported afterwards, and what a podcaster can do now without over-committing to details that may still shift.</p>
<p>Where a date or feature comes from a report rather than from Apple, this post says so. The best source for final details is always Apple&rsquo;s own newsroom and developer pages, and those should be checked before any launch plan.</p>
<h2>What Apple announced in February 2026</h2>
<p>According to Apple&rsquo;s announcement, listeners can switch between watching a video podcast and listening to the audio, with the playback position kept. Apple also described full-screen playback and the ability to download episodes for offline listening. These are the features most listeners will notice first, because they change the experience of a show they already follow.</p>
<p>Apple also said that creators would gain a way to earn from video, with video advertising available through named advertising partners. The exact terms, rates and eligibility are for the platform and its partners to set, so a podcaster should read the current creator guidance rather than rely on summaries.</p>
<h2>What was reported afterwards</h2>
<p>Coverage of Apple&rsquo;s developer conference in June 2026 reported that video podcast support would extend to Mac and Apple TV, with picture-in-picture multitasking, a redesigned interface and a search inside each show. These reports came from aggregators and trade sites rather than a single primary document, so treat the detail as provisional until it appears in Apple&rsquo;s materials.</p>
<p>One point is worth noting. Apple has said the software would ship in autumn 2026, while at least one report frames some features as part of a later update. A launch plan should allow for that difference, and should not promise a feature to sponsors before it is in listeners&rsquo; hands.</p>
<h2>Why this matters for podcasters</h2>
<p>A show that is available as video and audio has to work in both forms. A listener who starts on a phone and switches to audio on a commute still needs to understand what is happening on screen. That favours episodes where the spoken content carries the point, and where visual moments are explained in words. It also means the audio master becomes more important, because every version starts there.</p>
<p>The change also affects the economics. Video advertising opens a new route for income, which may suit shows with an audience that watches. It also means sponsors will ask about video results, so measure what you can from the start.</p>
<h2>What to prepare now</h2>
<ol>
<li>Keep a clean, lossless audio master of every episode, so the audio version is never compromised.</li>
<li>Test one episode in video form and check whether the audio still works on its own.</li>
<li>Name the speakers in the spoken content and describe any important on-screen material.</li>
<li>Write descriptions and chapter titles that make sense in both formats.</li>
<li>Check the platform&rsquo;s creator guidance before you agree a video sponsorship.</li>
</ol>
<h2>Chapters and structure</h2>
<p>Chapters have become more important as listeners switch between formats and skip ahead. Apple has added automatic chapter generation on recent versions of its software, and reports describe it as a way to make episodes easier to navigate. Automatic chapters are a starting point. They can mislabel a section or miss a turn in the conversation, so check them against the episode and rename any that are unclear.</p>
<p>Good chapter titles name the topic in plain words. &ldquo;Why the first draft failed&rdquo; tells a listener more than &ldquo;Part two&rdquo;. A well-marked episode is easier to share in clips and easier to return to later.</p>
<h2>What to avoid</h2>
<p>Do not treat the video version as a separate product that needs its own mix. Use one master and export the audio and video versions from it. Do not let the video feature change the sound of your show, and do not add visual gimmicks that the audio listener cannot follow. The most common mistake is making a video that depends on the picture so much that the audio version becomes confusing.</p>
<h2>Limits</h2>
<p>Platform features change, and the timing of any launch can slip. Some of the detail in this post comes from reports rather than from Apple&rsquo;s own pages, and it may be out of date by the time you read it. Check the official source before you plan a launch, and treat any date here as a guide, not a promise.</p>
<h2>Try it on your audio master</h2>
<p>Before you add a video version, make sure the audio stands on its own. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise, rumble and level problems in a recording. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording in your phone&rsquo;s browser. For the wider direction of the medium, read the <a href="/tunedzy/blog/why-podcasts-are-moving-to-video">video podcast post</a> and the <a href="/tunedzy/blog/podcast-trends-2027-what-to-expect">2027 trends post</a>.</p>
''',
    faq=[('Is Apple video podcast support available now?', 'Check Apple&rsquo;s newsroom. Reports describe a rollout in autumn 2026, but timing can differ by device and region.'),
         ('Do I need to change my audio for the video version?', 'No. Use the same audio master, and check that the episode still works without the picture.'),
         ('Can I earn from video podcasts on Apple?', 'Apple has said creators can use video advertising through partners. Read the current creator terms before you agree a deal.'),
         ('Should I stop audio-only episodes?', 'Not necessarily. Test video on one episode first and compare the results before changing the format.')])

add(slug='youtube-audio-only-listening-explained', cluster='trend-video-podcast', kw='youtube audio only mode',
    title='YouTube Audio-Only Listening Explained for Podcasters',
    desc='YouTube audio-only listening explained: what a reported audio-first mode means for podcasters, how listeners may use it and what to check before you rely on it.',
    h1='YouTube Audio-Only Listening Explained for Podcasters',
    answer='Reports describe a YouTube mode that turns the player into an audio-focused view and is limited to Premium subscribers. For podcasters, the lesson is to keep the audio strong, because a growing share of viewers may listen rather than watch. Confirm the feature on YouTube&rsquo;s own help pages before you plan around it.',
    body='''
<p>Many podcasts already live on YouTube, and many listeners play them with the screen off or in another app. In recent months, reports have described YouTube testing player features aimed at listening: an audio-first view, adaptive playback speed and other controls designed for speech. This post explains what has been reported, why it matters to a podcaster, and how to check the details before you act on them.</p>
<p>The important word is reported. These features have been described in news and product coverage, and some details may differ from what YouTube finally ships. Treat the claims here as a reason to pay attention, and check YouTube&rsquo;s official help and announcements for the current state.</p>
<h2>What has been reported</h2>
<p>One report describes an audio-first mode that replaces the video with a still image and enlarges the playback controls. According to that report, the mode is available only to Premium subscribers, and it can be turned on in settings or suggested by the app when it senses that the phone is moving, which suggests the listener is on the go. The same coverage describes a separate feature that speeds up playback during slower or denser speech, within a minimum speed the listener sets.</p>
<p>If these details are accurate, they change what a listener experiences. The episode is still the same, but the picture is smaller, the controls are larger and the pace may adjust during slow passages. Your audio then does more of the work, and any loud or unclear section is more likely to be noticed.</p>
<h2>Why a podcaster should care</h2>
<p>Listeners who choose audio-first modes are often the most loyal to a show, because they come back for the words rather than the picture. If those listeners find that your episode is hard to hear, or that the speed change makes it difficult to follow, they may leave. A feature that suits the listener should not make your work harder.</p>
<p>The speed feature also raises a question about pacing. A long pause that feels natural in your studio may be shortened by the player, and a fast section may be sped up more. Listen to your episode at a few playback speeds to check that the rhythm still works.</p>
<h2>Third-party tools are not YouTube features</h2>
<p>Some browser extensions claim to level or boost audio on YouTube. They are third-party tools, not YouTube features, and their behaviour depends on the extension. One extension described in search results uses the browser&rsquo;s audio interface to adjust gain toward a target. Read the permissions and reviews of any extension before you install it, and do not treat its target as an official standard.</p>
<p>The same caution applies to any claim that a platform will normalise your audio. Platforms may adjust playback levels, but the rules are theirs to set and they can change. Your own export is the part you control.</p>
<h2>What to do this month</h2>
<ol>
<li>Check the loudness and true peak of the exported file you upload to YouTube.</li>
<li>Listen to a recent episode at a faster playback speed and note any section that becomes hard to follow.</li>
<li>Check YouTube&rsquo;s official help pages for the current state of any audio feature.</li>
<li>Keep the audio master and the video version separate, so a change to one does not affect the other.</li>
</ol>
<h2>What not to assume</h2>
<p>Do not assume that a feature will reach every listener, every country or every device on the same day. Do not assume that a listener who chooses audio-first will forgive a poor mix. And do not change your production around a mode you have only read about. Wait for the platform to confirm it, then test on a short episode.</p>
<h2>Test a short episode before you change anything</h2>
<p>If you want to see how an audio-first view or a speed feature affects your show, test it with a short, simple episode rather than your flagship. Listen to it on the phone you use most, at the speed setting most listeners are likely to choose, and note the moments where the speech becomes hard to follow. Check the start, where the first impression is made, and any section where you speak quickly or quietly.</p>
<p>Then compare the same episode with an older one in the same format. If the newer one is harder to follow, the cause is probably the mix or the pacing, not the feature. Fix the cause in your editing, and test again. Keep the test small, so it takes an afternoon rather than a week.</p>
<h2>Limits</h2>
<p>Product features change quickly, and reports can be wrong or incomplete. The details in this post may not match what YouTube finally offers, and some features may be limited by region or subscription. Use this as a prompt to listen carefully, not as a reliable map of the platform&rsquo;s future.</p>
<h2>Check the sound before the platform does</h2>
<p>Whatever the platform adds, the sound of your episode is what listeners hear. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can check the loudness of the file you export, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording in your browser. For the broader change in how shows are watched and heard, read the <a href="/tunedzy/blog/apple-video-podcasts-explained">Apple video podcasts post</a> in this series.</p>
''',
    faq=[('Is there a YouTube audio-only mode?', 'Reports describe an audio-first mode for Premium subscribers. Check YouTube&rsquo;s official help pages for what is live.'),
         ('Does the speed feature change my audio?', 'It adjusts playback speed for the listener. The file itself does not change, but the pacing a listener hears may.'),
         ('Should I edit for the speed feature?', 'Not directly. Check your episode at a few speeds and fix any section that becomes unclear.'),
         ('Are audio-leveling extensions official?', 'No. They are third-party tools. Review their permissions before installing any of them.')])

add(slug='should-i-record-video-for-my-podcast', cluster='trend-video-podcast', kw='should I record video for podcast',
    title='Should I Record Video for My Podcast? A Decision Guide',
    desc='Should you record video for your podcast? A practical decision guide covering content, audience, time and cost, with a simple test before you commit.',
    h1='Should I Record Video for My Podcast? A Decision Guide',
    answer='Record video only when the picture adds something the audio cannot: visible reactions, a demonstration, a shared object or a place. Test one video episode, compare its completion with your audio episodes, and decide from the results rather than from fashion.',
    body='''
<p>Almost every podcaster who starts recording has been told that video is the future. Sometimes it is. Often the advice ignores the time, equipment and skill that video demands, and it assumes that a video of two people talking will hold an audience that an audio show already has. The honest answer is that video helps some shows and hurts others. A short decision process can tell you which kind of show you run.</p>
<p>This guide is for a solo creator or a small team deciding whether to add video. It assumes you already have an audio show that works, and it treats the audio as the thing you must not damage.</p>
<h2>Start with what the picture adds</h2>
<p>Ask what a viewer would see that a listener would miss. A guest who laughs, a host who points at a diagram, a chef at a stove, a musician playing an instrument, or a walk through a place can all add to the story. A conversation between two people sitting still often adds very little. If you cannot name a visual that matters, the episode may be better as audio.</p>
<p>Be honest about this test. Video is attractive to creators because it feels more like a finished product, not because it always improves the episode. The question is whether the picture serves the listener, not whether the show looks more professional.</p>
<h2>Check who your audience is</h2>
<p>Look at where your listeners already are. If most of them listen on commutes, in cars and while working, video will not reach them, and it may change how they experience the show. If you already have viewers on a video platform, or your guests bring their own audiences to video, the picture may be a natural extension.</p>
<p>Ask a few listeners directly whether they would watch. Their answer will be more useful than a general trend, and it costs nothing to ask.</p>
<h2>Count the time honestly</h2>
<p>Video adds recording setup, lighting, framing, a second export and the editing needed to keep cuts in sync. A video episode can take several times as long to finish as an audio one, and that time has to come from somewhere. If your current schedule is already tight, adding video may break the release rhythm, which hurts the show more than any picture helps it.</p>
<p>A practical estimate is to time one full episode from start to finish, including the setup and the export. Multiply that by your release schedule. If the result is more than you can sustain, plan a lighter video version, such as clips rather than full episodes.</p>
<h2>Consider the cost</h2>
<p>You do not need expensive equipment to start. A steady camera, a window or a simple lamp, and a clear background can be enough. But every extra item adds cost and something to maintain. Start with what you already own, and only buy more when a specific problem shows up in your test.</p>
<h2>Run a single test episode</h2>
<ol>
<li>Choose an episode whose content has a clear visual element.</li>
<li>Record the audio master first, in your usual room and at your usual level.</li>
<li>Add a simple video setup, with a fixed camera and good light.</li>
<li>Export the audio and video versions, and check each on a phone.</li>
<li>After a month, compare its completion and returning listeners with your audio episodes.</li>
</ol>
<p>Decide on the basis of that comparison, and be willing to drop video if the results do not justify the time.</p>
<h2>What to do if you say yes</h2>
<p>If the test works, keep the audio master as the foundation, and set one repeatable video format. Use the same camera position, light and background each time, so the show looks consistent. Keep the sound as the priority: a video episode with poor audio is worse than an audio episode with good audio.</p>
<h2>Plan for the rhythm of the show</h2>
<p>A video episode changes the rhythm of a show even when the topic stays the same. Viewers notice pauses while the camera is on, and some hosts start to perform for the lens. Watch your first test with that in mind. Note any moment where you feel self-conscious, and any point where the picture adds nothing. Those notes tell you whether video will strengthen the show or distract from it.</p>
<p>Decide ahead of time how long you will run the test and what result would make you stop. A clear rule, such as stopping if completion falls for three episodes in a row, keeps the decision honest. Without one, it is easy to keep going because you have already spent the time.</p>
<h2>Limits</h2>
<p>There is no universal answer. Some shows thrive on video, and some lose their intimacy when a camera is on. The test in this guide is designed to show you the difference for your show, not to predict the market. Expect to adjust after the first few episodes.</p>
<h2>Start with clean audio either way</h2>
<p>Whether you add video or not, the audio decides how long people stay. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise, rumble and level problems in a recording. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording in your phone&rsquo;s browser. For the wider context, read the <a href="/tunedzy/blog/why-podcasts-are-moving-to-video">video podcast post</a> in this series.</p>
''',
    faq=[('Do I need video to grow?', 'Not always. Many audio shows grow without it. Test before you commit.'),
         ('What if my guests do not want to be filmed?', 'Respect that. An audio-only episode is a fine choice, and you can record video only for guests who agree.'),
         ('How long should a test take?', 'One episode, plus about a month of data, is enough to see whether video changes listening.'),
         ('Can I start with clips instead of full episodes?', 'Yes. Short video clips from audio episodes are a lighter first step.')])

add(slug='budget-lighting-for-podcast-video', cluster='trend-video-podcast', kw='budget lighting for podcast video',
    title='Budget Lighting for Podcast Video: Simple Setups That Work',
    desc='Budget lighting for podcast video: a window, a soft lamp and a simple reflector, how to balance light on faces and how to avoid common mistakes.',
    h1='Budget Lighting for Podcast Video: Simple Setups That Work',
    answer='Good podcast video needs soft, even light on the faces. A window with a sheer curtain, a soft lamp at the side and a white reflector on the other side cover most home setups. Keep the light steady for the whole episode, and avoid mixing daylight with a warm lamp in the same frame.',
    body='''
<p>Lighting is the part of a video podcast that viewers notice most and creators fix least. A dim, uneven face makes an episode feel low quality, even when the sound is excellent. The good news is that a simple, cheap setup can look professional if it is soft, steady and placed with care. This guide covers the basics for a home studio.</p>
<p>The aim is not dramatic lighting. The aim is a face that is clear, a background that is not distracting and a look that stays the same across episodes. Once you have that, the rest of the production is easier.</p>
<h2>Use a window first</h2>
<p>Daylight from a window is the best free light most people have. Place the subject at an angle to the window, so the light falls across the face rather than straight on or from behind. A sheer curtain softens the light and reduces harsh shadows. Film at the same time of day if you can, because daylight changes quickly and can make two episodes look different.</p>
<p>Avoid placing the subject with the window directly behind them. The face will be dark, and the camera will try to compensate with noise and a washed-out background.</p>
<h2>Add a soft lamp</h2>
<p>When daylight is not enough, a soft lamp at the side can fill the shadows. A lamp with a diffuser, or a lamp pointed at a white wall, gives softer light than a bare bulb. Place it a little above eye level and to one side, and keep it at a similar distance each time. The aim is to add light, not to create a new shadow.</p>
<p>Mixing light sources is a common problem. Daylight is cool and a warm lamp is orange, and the two can make skin look strange. Either switch off the room light and use only one source, or set the camera&rsquo;s white balance to match what is on.</p>
<h2>Use a reflector</h2>
<p>A white card, a foam board or even a sheet of paper can bounce light back into the shadow side of the face. Place it on the side opposite the main light, and move it until the shadow softens. A reflector is cheap and one of the most effective tools for a small setup.</p>
<h2>Control the background</h2>
<p>A plain, slightly out-of-focus background is easiest to live with. Keep clutter out of the frame, and avoid a bright window behind the subject. A bookshelf or a plain wall works well. If the background is busy, move the chair or the camera rather than adding more lights.</p>
<h2>Keep the setup steady</h2>
<p>Mark the position of the chairs, the camera and the lamp on the floor with tape. Note the camera settings in a short template. A steady setup makes every episode look like part of the same show, and it saves time before each recording.</p>
<h2>Check the result on a phone</h2>
<p>Watch a short test on a phone. Check that the faces are clear, the shadows are soft and the background is calm. Adjust one thing at a time, and check again. Most viewers watch on a phone, so that is the screen that matters most.</p>
<h2>Common mistakes</h2>
<ul>
<li>Placing the subject in front of a bright window, which leaves the face dark.</li>
<li>Using a single harsh light close to the face, which creates strong shadows.</li>
<li>Mixing daylight and warm lamp light in one frame.</li>
<li>Letting the light change during an episode, so the face gets brighter or darker halfway through.</li>
</ul>
<h2>Work out the light for each seat</h2>
<p>In a two-person shot, each face needs its own light. A single window may light one person well and leave the other in shadow. Sit each person in the position they will use for the episode, then check their face on screen. If one face is much darker, move the reflector to their side or adjust the lamp, then check again.</p>
<p>Pay attention to hair and glasses too. A light placed high and to the side can throw glare onto lenses, and a light directly above can make hair look flat. Small changes in angle often solve these problems without any new equipment.</p>
<h2>Plan for changing daylight</h2>
<p>Daylight changes through the afternoon, and a session that starts in bright sun may end in dusk. Decide on a time of day for recording and stick to it, so every episode looks similar. If you must film at different times, add a soft lamp that you can use to match the daylight, and check the white balance before the first take.</p>
<p>Clouds can change the light in minutes. Keep the lamp on hand, and treat a sudden change as a reason to pause and re-check the frame rather than pressing on.</p>
<h2>Limits</h2>
<p>A budget setup will not match a studio. It will work well for a conversation show, but a complex scene needs more equipment and more time. Lighting cannot fix a poor camera or a cluttered room. Start with what you have, and improve one part at a time.</p>
<h2>Keep the audio as strong as the picture</h2>
<p>Good light does not rescue poor sound, and viewers judge both. Use the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> to check clipping, noise and level on a test recording, and use the <a href="/tunedzy/go/">Tunedzy Go</a> page to see how cleaning works on a phone recording. For the bigger decision about video, read the <a href="/tunedzy/blog/should-i-record-video-for-my-podcast">decision guide</a> in this series.</p>
''',
    faq=[('Can I use only a window?', 'Yes, if the window is at an angle to the subject and you film at a steady time of day.'),
         ('What is the cheapest improvement?', 'A reflector on the shadow side of the face. It costs very little and makes a visible difference.'),
         ('Do I need a special light?', 'Not to start. A soft lamp with a diffuser is enough for most small setups.'),
         ('Why does my face look orange?', 'Warm lamp light is mixed with daylight or a cool camera setting. Use one light source or fix the white balance.')])

add(slug='multi-camera-podcast-audio-setup', cluster='trend-video-podcast', kw='multi camera podcast audio',
    title='Multi-Camera Podcast Audio: How to Keep Sound Consistent Across Cuts',
    desc='Multi-camera podcast audio: why the sound must stay one take when the picture cuts, how to record the audio separately, sync it and avoid jumps between cameras.',
    h1='Multi-Camera Podcast Audio: How to Keep Sound Consistent Across Cuts',
    answer='Record one clean audio master for the whole conversation, separate from the cameras, and sync every camera to it with a clap. Keep microphone distances and levels the same across the episode, so the sound does not jump when the picture cuts between cameras.',
    body='''
<p>A multi-camera podcast cuts between two or more angles, and the sound has to stay smooth through every cut. Viewers do not expect a change in the audio when the picture changes, and a jump in level or room tone breaks the illusion quickly. The solution is to record the audio once, carefully, and let the cameras follow it.</p>
<p>This guide explains how to set up the audio so the cuts are invisible to the ear, how to sync each camera, and how to check the result before publishing. It assumes you have a small team or one person who can run more than one camera.</p>
<h2>Record the audio separately</h2>
<p>Do not rely on the camera&rsquo;s built-in microphone for a multi-camera show. Each camera records its own sound, at its own level and with its own room sound, and those differences show up at every cut. Record one audio master, using dedicated microphones and a single recorder, and use the camera sound only as a backup or a reference for syncing.</p>
<p>A separate recorder also gives you a clean file to edit even if one camera fails. That protection is worth the extra cable.</p>
<h2>Place the microphones with care</h2>
<p>Each speaker needs their own microphone at a steady distance. Shared microphones pick up the other speaker and blur the sound, which makes editing harder. If you use a shared microphone, keep it close to the centre and check the balance before recording. Mark each speaker&rsquo;s position on the floor, so the distance stays the same across the episode.</p>
<p>Keep the microphone cables away from the camera cables and from power cables, to reduce hum and crackle. Route them neatly so no one trips or moves the set during a take.</p>
<h2>Sync every camera with a clap</h2>
<p>At the start of each take, clap once in front of every camera, or tap the microphone sharply. The clap gives a sharp sound and a clear visual moment, which lets you line up each camera with the audio master. The <a href="/tunedzy/blog/how-to-sync-audio-and-video-in-an-editor">sync guide</a> explains the steps in detail.</p>
<p>Check the sync at the middle and the end of the take, not only at the start. Cameras with slightly different clocks can drift, and a drift of a few frames becomes obvious after an hour.</p>
<h2>Keep the level steady</h2>
<p>Set each microphone&rsquo;s level before the recording, and check it with a test. Speakers who move closer or further away change the level, so ask them to keep their position. If a level changes during the episode, correct it in the audio master before editing the picture, so every camera angle carries the same sound.</p>
<h2>Keep the room tone consistent</h2>
<p>Room tone is the quiet background that every recording has. If one camera angle is in a different corner, or the room changes between takes, the sound can jump. Record a short room-tone sample at the start of the session, and use it to smooth any join in the audio master. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone post</a> explains why this matters.</p>
<h2>Edit the audio first, then the picture</h2>
<p>Finish the audio master before you cut the picture. Remove mistakes, level the voices and clean the noise. Then cut the cameras to follow the edited sound. Editing the picture first often leaves the audio cut in places that do not match the new angles.</p>
<h2>Check the cuts by ear</h2>
<p>Play each cut at normal speed and listen for a change in level, room sound or breath. A cut that looks smooth can still sound abrupt, so listen with your eyes closed. Fix any join that makes the sound jump, and check again.</p>
<h2>Plan the edit before the recording</h2>
<p>Decide which moments you need from each camera before the session starts. A reaction shot of the listener is more useful when it is planned, because you can ask the speaker to pause and react on cue. A close shot of a speaker making a key point gives the edit a clear place to cut. Writing the cues into a running order makes the edit faster and reduces the number of times the audio has to be re-cut.</p>
<p>Keep the cameras in the same position for the whole session if you can. Moving a camera between takes changes the framing and, often, the sound around the speakers.</p>
<h2>Limits</h2>
<p>Multi-camera production takes more time and more people than a single camera, and sync problems can be hard to fix late in the project. Test the whole setup with a short recording before a real episode. If the team is small, start with two cameras and add more only when the workflow is steady.</p>
<h2>Check the final mix on a phone</h2>
<p>Once the episode is cut, play it on a phone with the sound on. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, which helps before you export. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the decision about whether video suits your show, read the <a href="/tunedzy/blog/should-i-record-video-for-my-podcast">decision guide</a> in this series.</p>
''',
    faq=[('Can I use the camera microphones?', 'Only as a backup or a sync reference. They change level and room sound between angles.'),
         ('How many microphones do I need for two people?', 'Two, one for each speaker, placed at a steady distance.'),
         ('Why does the sound jump when the picture cuts?', 'The cameras recorded different sound, or the levels changed. Use one audio master for the whole conversation.'),
         ('Should I edit the audio or the picture first?', 'Edit the audio first, then cut the picture to follow the finished sound.')])

add(slug='podcast-chapters-for-video-and-audio', cluster='trend-video-podcast', kw='how to add podcast chapters',
    title='How to Add Podcast Chapters for Video and Audio Episodes',
    desc='How to add podcast chapters for video and audio episodes: when they help, how to write clear titles, how to check automatic ones and stay consistent.',
    h1='How to Add Podcast Chapters for Video and Audio Episodes',
    answer='Add chapters at the points where the topic changes, give each one a clear title that names the subject, and check any automatic chapters against the episode. Consistent chapters help listeners jump to what they want, and they make clips and show notes easier to write.',
    body='''
<p>Chapters divide an episode into named sections, so listeners can see what is coming and jump to the part they came for. They have become more important as shows move between audio and video, and as listeners skip between episodes. A well-chaptered show is easier to navigate, easier to clip and easier to recommend.</p>
<p>This guide covers when chapters are worth the effort, how to write titles that help, how to check automatic suggestions, and how to keep the habit across a season.</p>
<h2>When chapters help</h2>
<p>Chapters help most in long episodes and in episodes with several distinct topics. An interview with three clear stages, or a solo episode that covers a process, benefits from chapters. A short episode that makes one point may not need them. Ask whether a listener would want to skip to a specific part, and add chapters where the answer is yes.</p>
<p>Chapters also help the people who do not hear the whole episode, such as those who search your show&rsquo;s notes for a particular subject.</p>
<h2>Write clear titles</h2>
<p>A good chapter title names the topic in plain words. &ldquo;Why the first draft failed&rdquo; tells a listener more than &ldquo;Part two&rdquo;. Keep titles short, usually under six words, and make them consistent in style across the episode. Avoid jokes in titles if the joke is not clear without the context.</p>
<p>Write the titles as the listener would search for them. A title that matches the words a listener would type is more useful than one that only the host understands.</p>
<h2>Use the transcript to find the breaks</h2>
<p>The transcript shows where the conversation changes direction. Read it once and mark each point where the topic moves on. Those marks are your chapter starts. A transcript also shows the exact words to use in the chapter title.</p>
<p>Chapters placed at the start of a topic, not in the middle of a sentence, feel natural. Check each start in the audio before publishing, because a transcript can be a few seconds out.</p>
<h2>Check automatic chapters</h2>
<p>Some phone systems and editing tools now suggest chapters automatically. Apple has added automatic chapter generation on recent versions of its software, and reports describe it as a way to make episodes easier to navigate. Automatic chapters are a starting point. They can mislabel a section, miss a turn in the conversation or create a chapter where none is needed.</p>
<p>Listen to each suggested chapter, check its start point and rename any title that is unclear. Remove chapters that add no value. A short list of accurate chapters beats a long list of vague ones.</p>
<h2>Keep the chapters consistent</h2>
<p>Use the same rules across the season. Choose a maximum number of chapters for each episode type, and use the same style of title. Consistent chapters let listeners learn how your show is organised, and they make it easier to compare episodes.</p>
<p>Keep the chapter list in the show notes too. Listeners who read the notes before listening can see the structure of the episode, which helps them decide.</p>
<h2>Chapters for video</h2>
<p>In a video episode, chapters can also point to a visual moment, such as a demonstration or a guest&rsquo;s answer to a question. Name the chapter so an audio listener understands it, even if they cannot see the picture. Describe the visual in words where it matters, so the chapter makes sense without the picture.</p>
<h2>Use chapters to plan the next episode</h2>
<p>Chapter titles reveal how a conversation is structured, and that structure can guide the next episode. If several chapters across a season are about the same question, the audience may want a whole episode on it. If a chapter always runs long and listeners skip it, the topic may need a tighter treatment. Review chapter lengths and titles each month alongside your completion data, and let them suggest the next topic.</p>
<p>Chapters also help the show notes. A list of chapter titles with times is a summary listeners can scan, and it can be reused in social posts.</p>
<h2>Give each chapter a single job</h2>
<p>A good chapter does one thing: it introduces a topic, tells a story, answers a question or marks a turn. A chapter that tries to do several things confuses the listener about where to go. If a section holds two distinct topics, split it into two chapters with clear titles.</p>
<p>Keep the number of chapters proportional to the episode. A thirty-minute show with twenty chapters is harder to use than one with six clear ones.</p>
<h2>Limits</h2>
<p>Chapters only help if they are accurate. A chapter that points to the wrong place frustrates listeners more than having no chapters at all. Check them after every episode, especially when you use automatic tools, and treat them as part of the editing process rather than an afterthought.</p>
<h2>Check the episode on a phone</h2>
<p>Once the chapters are in, play the episode on a phone and jump between them. Check that each one starts cleanly and that the level is steady across the section. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For how chapters fit into the wider change in listening, read the <a href="/tunedzy/blog/podcast-listener-habits-changing">listening habits post</a> in this series.</p>
''',
    faq=[('Do all episodes need chapters?', 'No. Add them to longer episodes or those with several distinct topics.'),
         ('Can I trust automatic chapters?', 'Only after checking. They can mislabel sections or miss turns in the conversation.'),
         ('How many chapters should an episode have?', 'As many as the topics need, and no more. Five to ten is common for an hour-long episode, but there is no fixed rule.'),
         ('Where do chapters appear?', 'That depends on the platform. Check the platform&rsquo;s help page for how it displays and uses them.')])

add(slug='video-ads-in-podcasts-what-creators-should-know', cluster='trend-video-podcast', kw='video ads in podcasts',
    title='Video Ads in Podcasts: What Creators Should Know Before Signing',
    desc='Video ads in podcasts: what creators should know before signing a deal, how video advertising differs from host reads, what to measure and what to ask.',
    h1='Video Ads in Podcasts: What Creators Should Know Before Signing',
    answer='Video ads in podcasts are a newer way to earn, with terms set by the platform and its advertising partners. Before you sign, read the current creator terms, ask how results are measured, and decide whether the ad suits your audience and your show.',
    body='''
<p>Advertising has been part of podcasting for a long time, mostly through host reads and pre-recorded spots. Video podcasts open a new route: advertising that runs inside a video episode, through partners and platforms that sell and place the spots. For creators, the attraction is clear, but so are the questions. This guide explains what to look for before you agree to anything.</p>
<p>The terms of any deal depend on the platform, the partner and your own agreement. This post explains the questions to ask rather than quoting rates or conditions, which change and should always be read in the current documents.</p>
<h2>How video ads differ from host reads</h2>
<p>A host read is spoken by you, in your voice, and placed within the episode. A video ad is a separate piece of content placed by a platform or partner, and it may be inserted at points you do not control. That difference matters for trust. Listeners know a host read is a recommendation from the host. A video ad may feel like it belongs to the platform, not to you.</p>
<p>Check whether the ad will be placed automatically, how often it appears and whether you can choose the points. A frequent ad can interrupt the flow of a conversation and damage the listening experience.</p>
<h2>Read the current creator terms</h2>
<p>Platforms set the rules for creators, including eligibility, payment, content standards and how long an agreement lasts. Those rules change. Read the current terms, not a summary from a blog, and note the date you read them. If something is unclear, ask the platform for a written answer before you rely on it.</p>
<p>Pay attention to what the terms say about ownership of your content and about changes made to the platform later. A short clause can change what you are agreeing to.</p>
<h2>Ask how results are measured</h2>
<p>Ask how the platform measures views, completion and the other numbers it reports. Ask whether the figures are independent or come only from the platform, and whether you can see the same data. A payment based on figures you cannot check carries more risk than one you can verify.</p>
<p>Compare the platform&rsquo;s numbers with your own. If they differ a lot, ask why, and keep a record of both.</p>
<h2>Decide whether the ad suits your audience</h2>
<p>An advert that suits a business audience may feel out of place for a hobby show, and the reverse is also true. Think about what your listeners expect and whether the ad fits. If in doubt, test a single episode and ask a few listeners what they thought.</p>
<p>Consider the brand as well. A sponsor whose product you would not recommend is a poor fit, even when the payment is good. The same test applied to host reads applies here.</p>
<h2>Protect the audio and the picture</h2>
<p>Ask whether the ad will change the loudness or the sound of your episode. An ad that is louder than the show will make listeners reach for the volume control, and they may leave. Check the level of the whole episode after the ad is placed, using the <a href="/tunedzy/tools/lufs-meter">LUFS meter</a>, and listen on a phone.</p>
<h2>Keep a record</h2>
<p>Keep copies of the terms you agreed, the dates, the placements and the numbers you received. A simple log makes it easier to compare deals, to resolve disputes and to decide whether to renew.</p>
<h2>Check the audience reaction after the first placement</h2>
<p>After the first placement, listen to your audience. Check the comments, the replies and any messages about the ad. Note whether listeners mention the placement, the timing or the product. A few clear reactions often tell you more than a dashboard, and they show whether the ad is becoming part of the experience or interrupting it.</p>
<p>If the reaction is strongly negative, ask the partner whether the placement can change before you agree to a longer run. A brief, honest conversation at this stage protects both the audience and the deal.</p>
<h2>Know your own break points</h2>
<p>Decide before you sign what would make you stop: a level of listener complaints, a change in the ad format, a payment that falls below a figure you have set, or a request to alter content. Write these points down in your own words. When the moment comes, you will be deciding from a plan rather than from the pressure of a deadline.</p>
<p>Review the agreement at each renewal, not only at the start. Terms and audiences both change, and a deal that suited the show a year ago may not suit it now.</p>
<h2>Limits</h2>
<p>This is general guidance and not financial or legal advice. Terms vary by platform, country and audience, and they change over time. For significant deals, ask a professional who understands contracts and advertising rules. Treat any figure you read about video ad income with care, because published estimates often differ widely.</p>
<h2>Start with the show you already have</h2>
<p>Video advertising works best for shows with a clear audience and a strong episode structure. Make sure the audio is ready first. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For how host reads compare, read the <a href="/tunedzy/blog/host-read-ads-explained-for-small-podcasts">host-read ads post</a> in this series.</p>
''',
    faq=[('Are video ads better than host reads?', 'They are different. Host reads are spoken by you and may build trust. Video ads are placed by the platform and may feel separate.'),
         ('Can I choose where ads appear?', 'Check the terms. Some placements are automatic, and you may have limited control.'),
         ('What should I ask before signing?', 'How the ad is placed, how results are measured, what the terms say about your content, and how the audio is affected.'),
         ('Where can I find current terms?', 'On the platform&rsquo;s creator pages. Read them directly, and note the date you checked.')])

add(slug='how-to-make-an-audiogram-for-social-posts', cluster='trend-video-podcast', kw='how to make an audiogram',
    title='How to Make an Audiogram for Social Posts',
    desc='How to make an audiogram for social posts: choosing a clip, building a simple waveform visual, adding captions, and checking the final file on a phone.',
    h1='How to Make an Audiogram for Social Posts',
    answer='An audiogram is a short video made from audio, with a waveform or simple visual and captions. Choose a clip that works alone, add a waveform and your show branding, caption every line, and check the sound and the first second on a phone before posting.',
    body='''
<p>An audiogram is a simple video made from an audio clip. It usually shows a waveform or a plain visual that moves with the sound, plus captions and a logo. For shows that have no camera, or that are not ready for full video, an audiogram is a light way to share a moment on video platforms and social feeds.</p>
<p>This guide covers the choices that make an audiogram work: the clip, the visual, the captions, the sound and the check on a phone.</p>
<h2>Choose a clip that stands alone</h2>
<p>As with any clip, the moment needs to make sense without the rest of the episode. Look for a clear point, a surprising answer or a line people will want to repeat. Keep the length short, usually under a minute, and cut any setup that does not help the point land.</p>
<p>An audiogram gives the viewer nothing to look at except the waveform and the words. A moment that depends on a gesture or a reaction will feel flat, so choose audio that carries its own weight.</p>
<h2>Keep the visual simple</h2>
<p>The most common audiogram uses a waveform that moves with the speech. Choose a shape and colour that match your show, and keep the background plain. Too much motion distracts from the words. A single static image behind a moving waveform is usually enough.</p>
<p>Put your show name and a small logo in a fixed place, so the viewer knows where the clip comes from. Avoid placing the logo where captions will sit.</p>
<h2>Caption every line</h2>
<p>Most people watch audiograms with the sound off at first. Captions are essential. Check every caption against the audio, because automatic captions make errors with names and technical words. Keep each caption short enough to read in the time it is on screen. The <a href="/tunedzy/how-to-export-captions-srt-and-vtt">caption export guide</a> explains the file formats for the platforms you use.</p>
<p>Use a readable font at a size that works on a small phone screen, and make sure the text contrasts with the background.</p>
<h2>Set the sound level</h2>
<p>An audiogram that is quieter than the feed around it will be scrolled past. Set the clip to a steady, clear level, without clipping the loudest words. Check the peaks, since a clip that peaks too high can sound harsh on a phone speaker. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can show the loudness of the final file.</p>
<p>Fade the start and end gently, so the clip does not begin or stop abruptly.</p>
<h2>Export and check it</h2>
<p>Export the file at the size and format the platform recommends. Check it on a phone, with the sound on and off. Confirm that the first second hooks the viewer, the captions are readable and the sound is clear. Make the changes before posting, not after.</p>
<h2>Link back to the episode</h2>
<p>Every audiogram should point back to the full episode. Use the same name and artwork, and include a short line in the caption that says where the full conversation can be heard. A clip that leads nowhere is a missed listener.</p>
<h2>Choose a shape for each platform</h2>
<p>The same audiogram can be shaped differently for different platforms. A square version with large captions suits a feed where most viewers scroll on a small screen. A vertical version works for short video. A wider version can suit a web page. Export each shape from the same master, and check the sound and captions on the device where each one will be seen.</p>
<p>Keep the caption style and the logo consistent across shapes, so viewers recognise the show wherever they find it.</p>
<h2>Use the audio as the main event</h2>
<p>An audiogram is a sound clip, so the sound must carry it. Choose audio with a clear voice and a clear point, and keep the visual as a frame around it. A bold waveform can draw the eye, but it should not hide the words or the speaker&rsquo;s name. If a viewer can follow the clip with the sound off and enjoy it with the sound on, the balance is right.</p>
<p>Test the clip with someone who has not heard the episode. Ask them what the clip is about after one viewing, and what they would do next. Their answer tells you whether the audio has done its job.</p>
<h2>Limits</h2>
<p>An audiogram is a light format, and it cannot carry a full episode. It works best as an introduction or a highlight. Do not expect it to replace video, and do not make it look like a finished film. Keep the audio as the star, because that is what the show is known for.</p>
<h2>Start with a clean episode</h2>
<p>An audiogram is only as good as the audio in it. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording in your browser. For clips that also use a picture, read the <a href="/tunedzy/blog/how-to-turn-a-podcast-episode-into-short-clips">short clips post</a> in this series.</p>
''',
    faq=[('What is an audiogram?', 'A short video made from audio, usually with a waveform, captions and a logo.'),
         ('How long should an audiogram be?', 'Usually under a minute. Cut for the single point and keep the setup short.'),
         ('Do audiograms need captions?', 'Yes. Most viewers watch with the sound off at first.'),
         ('Can I use music in an audiogram?', 'Only with the right to use it. Check the licence before you post.')])

add(slug='framing-a-two-person-podcast-shot', cluster='trend-video-podcast', kw='two person podcast framing',
    title='How to Frame a Two-Person Podcast Shot for Video',
    desc='How to frame a two-person podcast shot for video: eye line, spacing, headroom, the two-shot and the single-camera approach, with simple checks before recording.',
    h1='How to Frame a Two-Person Podcast Shot for Video',
    answer='Frame two people with their eyes near the upper third of the frame, similar headroom and enough space between them to avoid crowding. Place both people at a slight angle to the camera, keep the framing steady, and check the shot on a phone before recording the whole episode.',
    body='''
<p>Framing is how the viewer sees the conversation. Good framing makes both people feel present and gives the viewer a clear sense of who is speaking. Poor framing crops heads, places one speaker at the edge of the frame, or leaves a large empty space that draws the eye away from the faces. The good news is that a few simple rules fix most problems.</p>
<p>This guide covers a two-person shot for a single camera and for a simple two-camera setup, with the checks to make before the episode starts.</p>
<h2>Set the eye line</h2>
<p>The eyes are the most important part of the frame. Place each person&rsquo;s eyes roughly on the upper third of the picture, with the camera lens close to eye level. If the camera is far below the eyes, faces look distorted and the viewer feels looked down upon. Raise the camera or lower the chair until the lens is about level with the speakers&rsquo; eyes.</p>
<p>Check that both people&rsquo;s eyes sit at a similar height. A large difference in height makes one person look dominant, which may not be the effect you want.</p>
<h2>Give them room</h2>
<p>Leave a little headroom above each head, but not so much that the frame feels empty. Leave a small space at the sides, so faces do not touch the edges. Keep the two people close enough to feel like a pair, but with enough space that they do not crowd each other. A few centimetres of separation is often enough.</p>
<h2>Angle the chairs</h2>
<p>Place the two people at a slight angle to the camera, facing each other rather than the lens. A side-on arrangement with the faces turned toward one another looks natural. Facing the camera directly can feel stiff, and turning both chairs too far away can make the shot look disconnected.</p>
<h2>Choose the shot size</h2>
<p>A two-shot shows both people from the chest or waist up. It is the safest choice, and it keeps the conversation together. A closer shot on each person works well for cutting between them, but it needs more cameras or careful editing. Start with one wide two-shot, then add close shots only when you need them.</p>
<h2>Use one camera or two</h2>
<p>A single camera with a two-shot is simple and cheap, and it works well for a conversation. Two cameras, one on each person, give you more choice in editing and let you cut to the speaker. Two cameras need a sync point, as discussed in the <a href="/tunedzy/blog/multi-camera-podcast-audio-setup">multi-camera audio post</a>, and more time in editing. Choose the setup you can sustain.</p>
<h2>Keep the frame steady</h2>
<p>Lock the camera on a stable mount, and avoid touching it during the episode. A slowly drifting frame is distracting and can cut off a speaker&rsquo;s head. Mark the camera position on the floor or the stand, so you can return to it after a break.</p>
<h2>Check the frame before recording</h2>
<ol>
<li>Sit in the chairs as you would for the episode, and check the frame with each person in place.</li>
<li>Check that both faces are fully in frame, with eyes on the upper third.</li>
<li>Record a short test and watch it on a phone.</li>
<li>Adjust one thing at a time, and check again until the shot holds.</li>
</ol>
<h2>Recheck the frame after the first break</h2>
<p>People shift in their chairs over an hour, and the frame that worked at the start may not work at the end. Check the shot after the first break, and again after any change in position. A head that drifts toward the edge, or a face that sinks below the upper third, is easy to fix in the moment and very hard to fix in editing.</p>
<p>Ask the speakers to sit with their backs in the same place and their feet flat. A simple, comfortable seat is more stable than a chair that rolls or tilts, and it keeps the picture consistent from the first minute to the last.</p>
<h2>Frame for the audio-only listener</h2>
<p>Many viewers will switch to audio partway through an episode, so the framing should not be the only way the conversation makes sense. Check that each speaker is named early, and that the spoken content carries the point. A shot that shows a whiteboard or a product matters only if someone explains it in words.</p>
<p>Think of the picture as an addition to a good audio episode, not a replacement for one. The two should support each other, and neither should require the other to make sense.</p>
<h2>Limits</h2>
<p>Framing rules are guidelines, not laws. A shot that breaks them can still work if the conversation is strong. Adjust for the people in the shot, their height, their posture and the room. The aim is a comfortable, clear picture, not a perfect one.</p>
<h2>Keep the sound in the same shot</h2>
<p>A good frame does not help if the audio is poor. Use the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> to check clipping, noise and level in a test recording, and use the <a href="/tunedzy/go/">Tunedzy Go</a> page to see how cleaning works on a phone recording. For the lighting that goes with the framing, read the <a href="/tunedzy/blog/budget-lighting-for-podcast-video">budget lighting post</a>.</p>
''',
    faq=[('Where should the eyes sit in the frame?', 'Roughly on the upper third of the picture, with the camera close to eye level.'),
         ('Should people face the camera?', 'A slight angle toward each other usually looks more natural than facing the lens directly.'),
         ('How much space should I leave?', 'Enough headroom and side space that faces do not touch the edges, without an empty frame.'),
         ('Do I need two cameras?', 'No. A single two-shot works well for conversations. Add cameras only if you need the extra choice.')])

add(slug='video-podcast-audio-checklist', cluster='trend-video-podcast', kw='video podcast audio checklist',
    title='The Video Podcast Audio Checklist: Before, During and After Recording',
    desc='A video podcast audio checklist for before, during and after recording: microphones, levels, room tone, sync, export and a final check on a phone.',
    h1='The Video Podcast Audio Checklist: Before, During and After Recording',
    answer='Use a short audio checklist for each video podcast episode: set the microphones and levels before recording, watch the sound during the take, and check sync, loudness and the final file afterwards. A repeatable checklist protects the audio that viewers and listeners rely on.',
    body='''
<p>Video podcasts have more moving parts than audio ones. There are cameras to start, lights to check, a sync point to record and a second master to export. The audio is easy to forget in the rush, but it is what listeners hear first and what keeps viewers watching. A short checklist keeps the sound in order without slowing the session.</p>
<p>The checklist below is for a studio or a home setup. It is grouped into three parts, because the sound needs attention at each stage.</p>
<h2>Before recording</h2>
<ul>
<li>Check the room for fans, traffic, notifications and anything that rattles.</li>
<li>Place each microphone at a steady distance from its speaker, and mark the position.</li>
<li>Check the cables for hum, crackle and tension, and route them away from power.</li>
<li>Set the level on each microphone with a test, keeping the peaks well below the top.</li>
<li>Record a few seconds of room tone with nobody speaking.</li>
<li>Clap once in front of every camera to create a sync point.</li>
</ul>
<h2>During recording</h2>
<ul>
<li>Listen to the first minute on headphones, then check again after the first break.</li>
<li>Keep an eye on the level meter, and watch for peaks that touch the top.</li>
<li>Note the take numbers and any problems, with the time, so editing is faster.</li>
<li>Ask speakers to keep their distance and posture steady.</li>
<li>Check that the recording is still saving, especially on long sessions.</li>
</ul>
<h2>After recording</h2>
<ul>
<li>Stop the recording properly, and check that every file saved.</li>
<li>Copy the raw audio and video to a backup, as set out in the <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup post</a>.</li>
<li>Check the sync at the start, the middle and the end of each take.</li>
<li>Edit the audio master before cutting the picture.</li>
<li>Check the loudness and true peak of each exported file.</li>
<li>Listen to the final audio and video on a phone, with the sound on.</li>
</ul>
<h2>Why the order matters</h2>
<p>Checking the room and the levels before recording prevents problems that cannot be fixed later. Watching the sound during the take catches a microphone that has moved or a speaker who has drifted. Checking after the session confirms that the files are safe and in sync. Each stage catches a different type of error.</p>
<p>The checklist is short on purpose. A long list that nobody uses is worse than a short one that everyone follows.</p>
<h2>Export two masters, check both</h2>
<p>The audio version and the video version are separate exports, and each needs its own check. The audio version should match your usual loudness target, and the video version should sound the same level when people switch. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can measure the loudness of each file. Compare the two versions by listening, not only by numbers.</p>
<h2>Keep a log for each episode</h2>
<p>Record the microphone settings, the room, the level and any problems in a short log. A log lets you repeat a good setup and find the cause of a change later. Over a season, the log becomes the record of how the show sounds, and it answers questions about past episodes when a guest or an editor asks.</p>
<h2>Adapt the checklist to the episode type</h2>
<p>An interview, a solo show and a panel need different steps. An interview may need an extra check on the guest&rsquo;s microphone and a short introduction recorded for the edit. A solo show needs a check on the speaker&rsquo;s distance throughout, since nobody else is there to remind them. A panel needs more microphones, more levels and more care with crosstalk.</p>
<p>Write the variations as sub-lists under the main checklist, so the core steps stay the same and the extras are added only when needed.</p>
<h2>Make the checklist part of the schedule</h2>
<p>A checklist works only if it is used. Build it into the session calendar, so the setup starts with the list rather than with a search for it. Print it, pin it on the wall or keep it on the phone, and tick each line aloud if you work with a partner. Small rituals like this are what keep the audio consistent over a long season.</p>
<p>Review the checklist every few months. Remove the steps that never catch anything, and add the ones that caught a real problem. A checklist that changes with the show stays useful.</p>
<h2>Limits</h2>
<p>A checklist cannot make a poor room good, and it cannot replace listening. Use it to catch the routine mistakes, and keep your ears on the episode. Adapt the list to your setup, and remove any step that does not apply.</p>
<h2>Keep the sound as the priority</h2>
<p>Whatever the picture looks like, viewers judge the sound first. Use the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> to check clipping, noise and level in a recording before you export. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the decision about whether video suits your show, read the <a href="/tunedzy/blog/should-i-record-video-for-my-podcast">decision guide</a> in this series.</p>
''',
    faq=[('How long does the checklist take?', 'A few minutes before recording, and a few more after. It saves much more time in editing.'),
         ('Do I need to check the room every time?', 'Yes, quickly. Rooms change with the weather, the time of day and what is switched on.'),
         ('What is the most common audio mistake?', 'A microphone that moved during the take, or a level that was not checked before recording.'),
         ('Should the checklist be printed?', 'Keep it where you can see it while you set up, on paper or on your phone.')])
