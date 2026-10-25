"""Blog posts, batch 2 of 10: voiceover and narration cluster. Merged into content_blog.py.
Each post answers one search first, then explains it in plain steps, admits its limits, and links to a tool or guide.
No invented statistics, reviews, prices or benchmarks."""

CLUSTERS = {
    'voiceover': dict(tool='voice-recorder-noise-cancellation', label='Voiceover and narration', tool_name='Noise-Free Voice Recorder'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='how-to-time-a-voiceover-script-before-you-record', cluster='voiceover', kw='how to time a voiceover script',
    title='How to Time a Voiceover Script Before You Record',
    desc='Time a voiceover script before you record it: how many words per minute to plan for, how to mark pauses, and how to fit a script to a video.',
    h1='How to Time a Voiceover Script Before You Record',
    answer='Read the script aloud at your natural pace, time it with a stopwatch, and divide the word count by the minutes to get your speed. Plan pauses as part of the time, then trim the script until it fits the video or the slot you have.',
    body='''
<p>A voiceover that runs ten seconds over the picture, or finishes early and leaves dead air, is a common problem. It is cheaper to fix on paper than in the studio or the edit. Timing a script takes about ten minutes, and it tells you whether the words you have written will fit the time you have.</p>
<h2>Read it aloud at your normal pace</h2>
<p>Read the whole script out loud, as you would speak it to a viewer, not as fast as you can. Use a stopwatch or a phone timer. Note the total time. Do it twice, because the first read is usually faster or slower than the second, once you know the words.</p>
<h2>Work out your speaking speed</h2>
<p>Count the words in the script, then divide by the minutes it took. Most people speaking a narration settle somewhere in a similar range, but the exact speed depends on the subject, the audience and how formal the tone is. Your own number is more useful than any figure from a guide. Keep it on a sticky note for the next script.</p>
<h2>Plan the pauses as time</h2>
<p>Pauses take time too, and they are part of how a voiceover sounds natural. Mark the places where you want a breath, a beat before a point, or room for an on-screen image to land. Give each pause a length, such as half a second or a full second, and add it to the total. A script with no planned pauses always runs longer on the day.</p>
<h2>Trim to fit, not to speed up</h2>
<p>If the script is too long, cut words rather than asking yourself to speak faster. Speed makes a narration sound rushed and harder to follow. Cut filler phrases, repeated points and sentences that describe what the viewer can already see. Re-time after each cut.</p>
<h2>Mark the stress and the breaths</h2>
<p>Underline the words you want to stress, and put a slash where you will breathe. Breath marks stop you running out of air in the middle of a long sentence, which is one of the most common reasons for a bad take. Short sentences are easier to breathe in than long ones, so split any sentence that runs past one breath.</p>
<h2>Check against the picture</h2>
<p>If the voiceover goes over video, time it against the edit rather than your stopwatch. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone post</a> is useful when you record in a quiet room, but for timing, play the video and read along once. Adjust the script until the key words land on the key images.</p>
<h2>Limits</h2>
<p>Timing gives you a plan, not a guarantee. Real takes vary, and a nervous first read is almost always slower. Leave a little spare time at the end, so you can drop a line if the take runs long.</p>
''',
    faq=[('How many words per minute should I plan for?', 'Use your own speed. Read the script aloud, time it, and divide the word count by the minutes it took.'),
         ('Should I speed up if the script is too long?', 'No. Cut words instead. Faster speech sounds rushed and is harder to follow.'),
         ('Do pauses count toward the length?', 'Yes. Add planned pauses to the total time, or the final edit will run longer than the plan.'),
         ('What if the picture changes after I record?', 'Re-time the script against the new edit and record the lines that changed, rather than the whole script.')])

add(slug='what-microphone-to-use-for-voice-over-at-home', cluster='voiceover', kw='what microphone to use for voice over at home',
    title='What Microphone to Use for Voice-Over at Home',
    desc='Choosing a microphone for home voice-over: dynamic or condenser, USB or XLR, close placement, and how to decide before you spend money.',
    h1='What Microphone to Use for Voice-Over at Home',
    answer='For most home voice-over, a close-placed dynamic or a small-diaphragm condenser in a quiet room does the job. Choose by how you will connect it and how much the room is working against you, not by the highest price.',
    body='''
<p>Microphone choice matters, but for home voice-over the room and the distance usually matter more. A modest microphone in a soft room, placed close and steadily, will beat an expensive one in a bare room held at arm&rsquo;s length. Decide what you need from the microphone before you compare models.</p>
<h2>Dynamic or condenser</h2>
<p>Dynamic microphones are less sensitive to the room and to noise, which suits a home that is not treated. They reject more of the sound behind them, so they are forgiving of a small space. Condenser microphones are more sensitive and capture more detail, which suits a quiet room. They also pick up more background noise and echo, so they need a good space to shine.</p>
<h2>USB or XLR</h2>
<p>USB microphones plug straight into a computer and are simple to set up. XLR microphones need an audio interface, which adds cost and a step, but they can be upgraded later and give more control over the gain. For a first microphone, USB is usually the simplest route. Choose XLR when you know you want to grow your setup.</p>
<h2>Pick the pattern for your room</h2>
<p>A cardioid pattern picks up mostly what is in front of the microphone and rejects sound from the back and sides. That is the right choice for most voice-over, because it helps the room behind you stay quiet. Omnidirectional microphones pick up sound from every side and are better left for recording a room, not a voice.</p>
<h2>Placement matters more than the model</h2>
<p>Place the microphone a hand&rsquo;s width or two from your mouth, slightly off-axis to reduce breath pops, and keep the distance the same across takes. Put a pop filter in front, and a soft surface behind you. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can help with the background noise that remains in a home room.</p>
<h2>Budget and what to test first</h2>
<p>Before you buy, record a minute of your voice in your room with the phone or the computer you already own. Listen on headphones. If the sound is clear and the room is quiet, the next step is a better microphone. If the room is loud or echoey, the next purchase should be treatment, such as soft furnishings, not a microphone.</p>
<h2>Limits</h2>
<p>No single microphone suits every voice. Try a few if you can, using a return policy, and judge by your own recordings. Reviews and specification sheets help, but they cannot tell you how your voice sounds in your room.</p>
''',
    faq=[('Do I need an expensive microphone for voice-over?', 'Not usually. A good placement in a quiet, soft room matters more than the price of the microphone.'),
         ('Is USB good enough?', 'Yes, for most home voice-over. Choose XLR if you plan to build a larger setup later.'),
         ('Should I use a dynamic or a condenser?', 'A dynamic is more forgiving in an untreated room, while a condenser needs a quiet room to sound its best.'),
         ('What is the first thing to buy?', 'Often a pop filter and a stand or boom arm. Better placement is cheap and makes a visible difference.')])

add(slug='how-to-read-a-voiceover-script-so-it-sounds-natural', cluster='voiceover', kw='how to read a script naturally',
    title='How to Read a Voiceover Script So It Sounds Natural',
    desc='Read a voiceover script so it sounds natural rather than read: how to find the meaning, speak to one person, vary the pace and avoid the reading voice.',
    h1='How to Read a Voiceover Script So It Sounds Natural',
    answer='Read the script for meaning before you speak it. Decide what each sentence is for, speak to one listener, vary your pace on purpose, and record the lines in short sections. A natural read comes from understanding the words, not from a special voice.',
    body='''
<p>A voiceover that sounds read usually has the right words in the wrong order of importance. Every word gets the same weight, the pace is steady, and the voice stays in the same place. Listeners hear the effort and stop trusting the narrator. The fix is mostly reading the script with understanding, which you can practise at home.</p>
<h2>Read for meaning first</h2>
<p>Before you speak a line, say what the sentence is for. Is it a question, a promise, a joke, a warning? Mark the one or two words that carry the point. Those words get the emphasis, and the others stay quieter. A reader who knows what they are saying sounds like they mean it.</p>
<h2>Speak to one listener</h2>
<p>Imagine a single person who needs this information, and talk to them. A voiceover aimed at &ldquo;everyone&rdquo; sounds like a broadcast. A voice aimed at one person sounds closer and warmer, and it is easier for the listener to follow. Keep the same imagined person through the whole script.</p>
<h2>Vary the pace on purpose</h2>
<p>Slow down for the important point and the last word of a sentence, and speed up slightly through the simple connecting words. Do not change pace at random. Mark two or three places where you want to speed up or slow down, then rehearse those lines until they feel natural.</p>
<h2>Use short takes</h2>
<p>Record each paragraph separately, with a short pause between takes. A short take keeps your energy and your focus, and you can re-record one line without repeating the whole script. Listen back after the first few takes, then adjust your approach before you continue.</p>
<h2>Watch for the reading voice</h2>
<p>The reading voice has a clear sign: the pitch stays level, the stress falls on the wrong words, and the sentence ends with a flat drop. If you hear that, stop, re-read the sentence for meaning, and try again. A slight smile, or standing while you read, often helps.</p>
<h2>Limits</h2>
<p>Some scripts are dull, and no delivery will change that. Ask for a rewrite if the script itself has no point. A good read cannot rescue weak writing, but clear writing and a clear read together make a strong voiceover.</p>
''',
    faq=[('Should I act out the script?', 'Not usually. Clear meaning and a steady, friendly tone work better than a performance.'),
         ('How do I stop sounding like I am reading?', 'Read for meaning, speak to one listener, and vary your pace on the key words.'),
         ('Should I stand or sit?', 'Either works. Many people find standing gives them more energy and a steadier breath.'),
         ('How many takes should I do?', 'Enough to find the read you like. Keep the best take of each line and move on.')])

add(slug='how-to-choose-the-best-take-for-a-voiceover', cluster='voiceover', kw='how to choose the best voice over take',
    title='How to Choose the Best Take for a Voiceover',
    desc='Choosing the best voiceover take: how to listen for meaning, emotion and clean sound, how to compare takes fairly, and when to stop recording.',
    h1='How to Choose the Best Take for a Voiceover',
    answer='Listen to each take twice: once for meaning and feeling, and once for clean sound. Compare the top two or three takes against each other, not against your memory of the script, and stop when another take is not clearly better.',
    body='''
<p>Recording a voiceover often produces five or six takes of each line. Picking the right one is a skill, and it is easy to get wrong when you are tired. The temptation is to choose the most polished take, or the last one, when the best take is the one that sounds most like someone talking to a listener.</p>
<h2>Listen for meaning first</h2>
<p>On the first listen, ignore the sound quality and ask whether the take says what the line means. Does the stress fall on the right word? Does it sound like a real thought? A take with a small flaw but a clear meaning is usually better than a flawless take with no life in it.</p>
<h2>Listen again for clean sound</h2>
<p>On the second listen, check the sound. Look for clicks, mouth noise, breath pops, room noise and any change in distance from the microphone. Use headphones, and turn the volume up slightly, since problems that hide at normal level often show up quietly at a higher one.</p>
<h2>Compare two or three, not all of them</h2>
<p>Narrow the takes to the best two or three, then compare them one after another, with a few seconds between. Comparing many takes at once is tiring and leads to indecision. Mark your favourite, then listen to it again in the context of the lines before and after it.</p>
<h2>Keep the sound consistent</h2>
<p>When you have a favourite, check that it matches the other lines in level, distance and tone. A take that is clearer but noticeably quieter can stand out in the edit. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains the level targets that keep a series of lines consistent.</p>
<h2>Know when to stop</h2>
<p>If the next take is not clearly better, stop and use the current one. Perfectionism wastes time and drains the voice, and the listener will not hear the difference between the fifth and the sixth take. Keep a note of the take number, so you can find it again.</p>
<h2>Limits</h2>
<p>Your ear gets tired during long sessions, so choose takes in short bursts. If you are unsure, sleep on it and listen again the next morning. A fresh ear hears the difference more clearly.</p>
''',
    faq=[('How many takes is enough?', 'Usually three to five per line. Stop when the next take is not clearly better.'),
         ('Should I choose the most polished take?', 'Not always. Meaning and natural delivery matter more than a flawless but lifeless read.'),
         ('What if two takes are equal?', 'Choose the one that matches the lines around it in level and tone.'),
         ('Should I listen on speakers or headphones?', 'Headphones show the noise and mouth sounds most clearly. Check on a speaker too, if you can.')])

add(slug='how-to-remove-mouth-clicks-from-a-voiceover', cluster='voiceover', kw='remove mouth clicks from voice over',
    title='How to Remove Mouth Clicks From a Voiceover Recording',
    desc='Remove mouth clicks and saliva sounds from a voiceover: why they happen, how to prevent them while recording, and how to edit the few that remain.',
    h1='How to Remove Mouth Clicks From a Voiceover Recording',
    answer='Mouth clicks come from dry mouth, tongue movement and lip sounds. Drink water before you record, keep the mouth moist, and stop each take for a moment between phrases. Remove the few that remain by cutting or lightly reducing them in a clean section.',
    body='''
<p>Mouth clicks and saliva sounds are easy to miss while you speak and very obvious on playback. A close microphone picks up every tick of the tongue and every small smack of the lips. Most of them are prevented before the recording starts, and the few that remain can be edited with care.</p>
<h2>Why they happen</h2>
<p>A dry mouth makes the tongue stick and release, which makes a click. Some people produce more saliva when they speak for a long time, and the sound becomes a crackle. Tight lips and a clenched jaw add to the problem. A close microphone exaggerates all of it.</p>
<h2>Prevent them while recording</h2>
<p>Drink water before the session and keep a glass nearby, then sip between takes rather than during one. Some voice users avoid dairy before a long session because it can feel like it thickens saliva, so test whether it matters for you. Relax the jaw and tongue before you start, and speak from the throat and chest rather than tightening the mouth. Short breaks help more than any single trick.</p>
<h2>Move the microphone slightly</h2>
<p>A microphone placed directly in front of the mouth picks up more mouth sound. Angling it slightly off-axis, or moving it a few centimetres further away, can reduce the clicks without changing the voice too much. Keep the position the same once you find it.</p>
<h2>Edit the ones that remain</h2>
<p>Zoom in on the click and cut it, leaving a little room tone on each side, so the join does not sound abrupt. If a click sits in the middle of a word, a very short crossfade often hides it. Do not reduce the clicks so hard that the consonants lose their edge. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone guide</a> explains why a short sample of silence helps the edit.</p>
<h2>Limits</h2>
<p>Some people produce clicks no matter what they try, and a few cuts are normal in any voice. Do not chase perfection at the cost of a natural performance. A voice with a faint click is still easy to listen to, and a dry, tight read is not.</p>
''',
    faq=[('Do drinks help with mouth clicks?', 'Water helps. Avoid very sugary or dairy drinks just before a long session.'),
         ('Can I remove clicks completely?', 'Usually you can reduce most of them. Some natural mouth sounds will remain, which is normal.'),
         ('Should I use a lower gain to reduce clicks?', 'No. Lower gain reduces the voice, not the click. Move the microphone or relax your mouth instead.'),
         ('Do I need special software to remove clicks?', 'Basic editing is enough for a few clicks. A clean recording reduces the amount you need to fix.')])

add(slug='cheap-vocal-booth-for-voice-over-at-home', cluster='voiceover', kw='cheap vocal booth for voice over',
    title='A Cheap Vocal Booth for Voice-Over at Home',
    desc='Build a cheap vocal booth for voice-over at home: choosing a space, soft surfaces that cost little, a reflection filter and what a booth cannot fix.',
    h1='A Cheap Vocal Booth for Voice-Over at Home',
    answer='A cheap vocal booth is a soft, small space with the microphone close to a wall of clothes, blankets or foam. Pick the quietest spot, cover the hard surfaces around you, and test the result with a short recording before you commit.',
    body='''
<p>A vocal booth sounds like a serious project, but a home voice-over setup can be made dry and quiet for very little money. The aim is not a perfect studio. It is a space where the room adds less echo and less noise than the bare room would, so the voice sounds close and clear.</p>
<h2>Choose the space first</h2>
<p>Pick the smallest room that is away from traffic, appliances and people. A wardrobe, a cupboard or a corner of a bedroom with the door closed works well. Smaller spaces have fewer reflections, but they can also sound boxy, so test before you decide. Remove anything that rattles or hums.</p>
<h2>Soften the hard surfaces</h2>
<p>Hard walls, windows and floors reflect sound. Hang blankets, duvets or moving blankets on the surfaces nearest the microphone. A wardrobe full of clothes is one of the cheapest and most effective absorbers you own. Lay a rug or a thick mat on the floor. The aim is to soften the reflections, not to remove all sound.</p>
<h2>Place the microphone well</h2>
<p>Put the microphone close to the soft surfaces behind you, and keep the space in front open enough that you can read comfortably. A reflection filter, a small panel placed behind the microphone, can help, but it is not essential if the room is already soft. The <a href="/tunedzy/how-to-test-your-room-for-echo">clap test</a> helps you find the best spot before you spend money.</p>
<h2>Test with a short recording</h2>
<p>Record ten seconds of you reading a paragraph, then listen on headphones. Check for echo, boxy sound and background noise. Move the blankets, the microphone or yourself, then record again. Keep a note of the setup that sounds best, so you can repeat it.</p>
<h2>What a booth cannot fix</h2>
<p>A booth reduces echo and some noise. It does not remove the sound of a fridge, a bus outside or a neighbour&rsquo;s drill. Use a cleanup tool for what remains, and move your recording to a quieter time if you can. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can help with noise that you cannot remove by treatment alone.</p>
<h2>Limits</h2>
<p>Home booths are a compromise, and the sound will not match a professional studio. For a long audiobook or a commercial job, check the standards the client expects before you record. For most voice-over, a clean, dry, close sound is enough.</p>
''',
    faq=[('Do I need foam panels?', 'No. Blankets, clothes and rugs do much of the same work for much less money.'),
         ('Is a closet really good enough?', 'It often is, if it is soft inside and you test it first. Keep the door closed and the microphone close to the clothes.'),
         ('What about a reflection filter?', 'It helps a little in a bright room. It is not essential if the room is already soft.'),
         ('How do I know if the booth works?', 'Record a short test, listen on headphones, and compare it with a recording made in the bare room.')])

add(slug='how-to-record-voice-over-for-youtube-videos', cluster='voiceover', kw='how to record voice over for youtube',
    title='How to Record Voice-Over for YouTube Videos',
    desc='Record voice-over for YouTube videos: script and timing, a quiet room, clean takes, the right level and how to fit the narration to the edit.',
    h1='How to Record Voice-Over for YouTube Videos',
    answer='Write and time the script first, record it in a quiet room with the microphone close, and keep each line as a separate clean take. Level the narration to a steady target and fit it to the edit, then check it on a phone speaker before you publish.',
    body='''
<p>A voice-over is often the difference between a video people watch to the end and one they leave after a minute. The picture does a lot of the work, but a clear, steady narration carries the explanation. Recording it well is mostly a matter of preparation and a calm, consistent setup.</p>
<h2>Write for the ear, then time it</h2>
<p>Write short sentences, and say each one the way you would tell it to a friend. Read the script aloud and time it against your rough edit. The <a href="/tunedzy/blog/how-to-time-a-voiceover-script-before-you-record">timing guide</a> shows how to fit the words to the picture before you record.</p>
<h2>Record in a quiet, soft room</h2>
<p>Choose a room with soft surfaces and no fans or traffic. Record at a time when the house is quiet, and switch off notifications. Place the microphone close, with a pop filter, and keep the distance steady for every line. A consistent sound makes the edit easier.</p>
<h2>Record each line separately</h2>
<p>Record each sentence or short paragraph as its own take, with a gap of a second or two. Clear gaps make the takes easy to find and easy to edit. If you make a mistake, repeat the line from the start of the sentence, not in the middle of a word.</p>
<h2>Set the level and keep it steady</h2>
<p>Record with the peaks well below full scale, so the voice does not clip. Match the narration to a steady loudness target before you publish, so it sits at a comfortable level beside the music and effects. The <a href="/tunedzy/tools/lufs-meter">LUFS meter</a> can show the loudness of the finished file.</p>
<h2>Fit the narration to the edit</h2>
<p>Place each line on the timeline, then trim the gaps between lines so the voice and the picture match. Keep a short pause after a key point, so the viewer can take it in. If music plays under the narration, lower it so the words stay clear.</p>
<h2>Check on a phone</h2>
<p>Many viewers listen on a phone speaker. Play the finished video on your phone before you upload, and check that the voice is clear and the level is comfortable. Fix anything that is hard to hear before you publish.</p>
<h2>Limits</h2>
<p>A voice-over cannot fix a weak script or a dull edit. Use the narration to add what the picture cannot show, and let the video breathe where it can.</p>
''',
    faq=[('Should I record with my phone or a microphone?', 'A close microphone in a quiet room gives the clearest result. A phone can work well if you place it close and keep it steady.'),
         ('How loud should the voice-over be?', 'Keep it steady and comfortable beside the music. Use a loudness target rather than a single peak level.'),
         ('Should I re-record every line if I make one mistake?', 'No. Re-record only the line that needs it, from the start of the sentence.'),
         ('Can I use AI to read the script?', 'That is a separate choice with its own rules. Check the terms of any tool and be clear with viewers about how the voice was made.')])

add(slug='how-to-record-an-audiobook-narration-at-home', cluster='voiceover', kw='how to record an audiobook at home',
    title='How to Record Audiobook Narration at Home',
    desc='Record audiobook narration at home: a quiet room, steady pace, clean chapters, consistent sound across hours, and what to check before you submit.',
    h1='How to Record Audiobook Narration at Home',
    answer='Record audiobook narration in a quiet, soft room with a steady microphone position, one chapter at a time. Keep the sound and pace consistent across the whole book, and check each chapter for noise and clicks before you move on. Check any publisher or platform rules before you submit.',
    body='''
<p>Narrating a book is a long job, and the sound has to stay consistent for hours and often across several sessions. Listeners expect a steady, comfortable voice and clean audio from start to finish. A calm process matters more than the equipment, because fatigue and drifting sound are the two biggest problems.</p>
<h2>Check the rules before you start</h2>
<p>Audiobook platforms and publishers often have technical requirements for level, noise, file format and chapter structure. Read them before you record, because fixing a whole book after the fact is much harder than recording to the standard. Keep a short note of the requirements next to your setup.</p>
<h2>Set up a repeatable room</h2>
<p>Use the same soft, quiet room for every session. Mark the microphone position and your seat, and record a short test at the start of each day to confirm the sound has not changed. The <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone guide</a> explains how to capture a short sample of the room for editing.</p>
<h2>Record one chapter at a time</h2>
<p>Record a chapter, listen to it, and fix problems before you start the next one. Problems you ignore early tend to multiply over a book. Keep a checklist for each chapter, covering the opening, the close, any character voices, and the file name.</p>
<h2>Pace yourself</h2>
<p>Plan sessions of an hour or two, with short breaks. Fatigue changes the voice and the pace, and listeners notice the change. Drink water, keep the room comfortable, and stop when your voice tires, even if the chapter is not finished.</p>
<h2>Keep the sound consistent</h2>
<p>Record each chapter with the same microphone position, level and settings. Use the same room tone sample across the book, and check the loudness of each chapter against the others. The <a href="/tunedzy/loudness-for-youtube-podcasts-and-spotify">loudness guide</a> explains why steady levels matter across a series of files.</p>
<h2>Limits</h2>
<p>A home setup can meet many requirements, but it is not a studio, and some platforms have strict rules that a home room may not meet. Check the specification for each platform, and listen to a full chapter on headphones and a phone before you submit.</p>
''',
    faq=[('Do I need a studio to narrate an audiobook?', 'Not always, but you need a quiet, soft room and a consistent setup. Check the platform rules before you start.'),
         ('How long does a chapter take?', 'It depends on the chapter and your pace. Plan for editing time as well as recording time.'),
         ('What if I make a mistake in the middle of a chapter?', 'Re-record from the start of the sentence, then edit the join so it is clean.'),
         ('How do I keep my voice fresh?', 'Work in shorter sessions, drink water, and stop before your voice tires.')])

add(slug='how-to-match-a-voiceover-to-video-timing', cluster='voiceover', kw='match voice over to video timing',
    title='How to Match a Voiceover to Video Timing',
    desc='Match a voiceover to video timing: marking key moments, timing lines against the picture, handling lines that run long and keeping the sync after edits.',
    h1='How to Match a Voiceover to Video Timing',
    answer='Mark the key moments in the video first, then time each voiceover line to land on or before the moment it describes. If a line runs long, shorten the words rather than speeding up the read, and check the sync after every edit.',
    body='''
<p>A voiceover that drifts away from the picture feels careless, even when the words are good. The fix is planning the timing before the final edit, then checking the sync every time the picture changes. Most sync problems come from changing one part of the video without rechecking the rest.</p>
<h2>Mark the key moments first</h2>
<p>Watch the video once and mark the moments the narration must match: a product appears, a number is shown, a name is spelled on screen, a cut happens. These are the anchors. Everything else can flex around them.</p>
<h2>Time each line against its anchor</h2>
<p>Place each voiceover line so it starts just before the moment it describes. Leave a short gap before the next anchor, so the viewer has time to see the picture and the words. A line that starts too late makes the narration feel behind the video.</p>
<h2>Handle lines that run long</h2>
<p>If a line runs past its slot, shorten the words first. Cut filler, combine two sentences, or move part of the line to an earlier moment. Speeding up the read is the last resort, because speed makes narration harder to follow. The <a href="/tunedzy/blog/how-to-time-a-voiceover-script-before-you-record">script timing guide</a> covers this in more detail.</p>
<h2>Keep room for the picture</h2>
<p>Viewers need time to read on-screen text and take in an image. A narration that speaks over every second of a slow scene removes that time. Leave short silences where the picture needs them, and let the image lead at a few points.</p>
<h2>Check the sync after every change</h2>
<p>Each time you trim a shot, move a clip or add a title, check the lines around it. A change in one place often moves the rest by a fraction of a second, which is enough to notice. Play the whole video once after the final changes, not only the parts you edited.</p>
<h2>Limits</h2>
<p>Some edits need the narration to change, not the picture. If a line will never fit a shot, rewrite the line. A good sync comes from a good script and a patient edit, and both take time.</p>
''',
    faq=[('What should I do if a line is too long for its shot?', 'Shorten the words first. Speeding up the read is the last resort.'),
         ('Should narration always match every shot?', 'No. Leave room for the picture to speak on its own at key moments.'),
         ('How do I check sync quickly?', 'Play the whole video once after your final changes, and listen for any line that feels early or late.'),
         ('Can I fix sync at the end?', 'Only a little. It is easier to plan the timing before you record the final takes.')])

add(slug='how-to-edit-breaths-in-a-voiceover', cluster='voiceover', kw='how to edit breaths in voice over',
    title='How to Edit Breaths in a Voiceover Without Losing the Voice',
    desc='Edit breaths in a voiceover so the narration stays natural: when to keep a breath, when to shorten one, and how to avoid the flat, over-cleaned sound.',
    h1='How to Edit Breaths in a Voiceover Without Losing the Voice',
    answer='Keep most breaths, because they make a voice sound human. Shorten the loud or long ones that distract, and remove a breath only when it sits in the wrong place. Use a small fade or a crossfade rather than a hard cut, so the edit does not jump.',
    body='''
<p>Breaths are part of speech, and a voiceover with every breath removed sounds unnatural and tired in a different way. Listeners notice when a voice never seems to breathe. The job is to make the breaths quieter and better placed, not to remove them all.</p>
<h2>Why keep most breaths</h2>
<p>A breath tells the listener that a person is speaking, not a machine. It also marks a pause between ideas, which helps the listener follow. Removing every breath can make a narration sound rushed, with no room to think. Keep the ones that sound natural at normal volume.</p>
<h2>Shorten the loud or long ones</h2>
<p>Breaths that are much louder than the speech, or that last for a long time, distract the listener. Lower them by a few decibels, or shorten them so they sound like a quick intake. Make small changes, and listen at normal volume after each one.</p>
<h2>Remove a breath only when it is in the wrong place</h2>
<p>A breath in the middle of a short phrase, or one that cuts a word in two, should be removed. Do it carefully, by cutting in a quiet part of the breath and keeping the room tone behind it. A breath that starts a new sentence is usually fine to keep.</p>
<h2>Make the joins smooth</h2>
<p>A hard cut across a breath can make the voice jump. Use a short fade or a crossfade of a few milliseconds, and keep a little room tone under the join. The <a href="/tunedzy/how-to-crossfade-two-recordings">crossfade guide</a> shows the method, which works the same way for breath edits.</p>
<h2>Compare with the original</h2>
<p>After editing, play the edited section next to the original. If the edit sounds cleaner but less alive, you have removed too much. The best edit is the one that a listener cannot point to, because nothing sounds wrong.</p>
<h2>Limits</h2>
<p>Breath editing takes time, and it is easy to over-do. For a short voiceover, a few careful edits are enough. For long-form narration, consider a lighter approach, so the sound stays consistent across the whole recording.</p>
''',
    faq=[('Should I remove all breaths from a voiceover?', 'No. Keep most of them, because they make the voice sound human.'),
         ('How do I make a breath quieter?', 'Lower its level a few decibels, or shorten it so it sounds like a quick intake.'),
         ('Will listeners notice a breath edit?', 'Not if the join is smooth and the room tone matches. A hard cut is the most noticeable part.'),
         ('Should I edit breaths before or after cleaning the file?', 'Clean the file first, then edit the breaths, so the room noise is consistent when you make the changes.')])
