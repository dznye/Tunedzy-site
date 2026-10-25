"""Blog posts, batch 24: sound design for video, games and brands (evergreen). Merged into content_blog.py.
Techniques are explained with their purpose and limits. Licence points are general guidance, not legal advice.
No invented statistics and no recommended sound libraries. Funnel: each post ends with a link to Tunedzy Go and to
the matching free tool."""

CLUSTERS = {
    'sound-design': dict(tool='vocal-checker', label='Sound design and sound effects', tool_name='Vocal Checker'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='sound-design-basics-for-video', cluster='sound-design', kw='sound design for video basics',
    title='Sound Design Basics for Video: What Each Sound Is Doing',
    desc='Sound design basics for video: dialogue, effects, ambience and music, what each layer does for the picture and how to balance them.',
    h1='Sound Design Basics for Video: What Each Sound Is Doing',
    answer='Sound design for video is the planning and shaping of every sound in the picture: dialogue, effects, ambience and music. Each layer has a job, from making the speech clear to placing the viewer in a space and carrying emotion. Good sound design makes the picture feel real and guides attention, and it is judged most when it goes unnoticed.',
    body='''
<p>Sound design is the craft of deciding what the listener hears alongside the picture. It covers the dialogue, the effects that match actions, the ambience that places the viewer in a space and the music that carries emotion. Many viewers never notice sound design when it is done well, and they notice immediately when it is missing or wrong. A clear, believable soundtrack can make a modest picture feel rich, while a careless one can undermine the strongest images.</p>
<p>This post introduces the four main layers, explains what each one does and sets out the basic balance that keeps the soundtrack clear. It is written for creators who make their own videos and want to understand the craft behind them.</p>
<h2>Dialogue comes first</h2>
<p>Dialogue carries the story in most videos, so it sits at the top of the hierarchy. The viewer must be able to understand every line without strain. Dialogue should be clean, close and consistent in level, and it should not be masked by effects or music. Many sound design problems are really dialogue problems in disguise, so start by making the speech clear.</p>
<p>A useful test is to watch the video with the effects and music turned down. If the story still makes sense, the dialogue is doing its job.</p>
<h2>Effects tie sound to action</h2>
<p>Effects are the sounds of things happening: a door closing, a glass set down, a footstep on gravel. They give the picture physical presence, and they help the viewer believe the action. Effects are often exaggerated slightly for clarity, because real sounds can be too quiet or too subtle for the screen. The art is in choosing the right size of sound for the moment, not the loudest one.</p>
<p>Effects should match the picture closely. A sound that arrives a fraction late or early makes the action feel wrong, even when the sound itself is good.</p>
<h2>Ambience places the viewer</h2>
<p>Ambience is the background sound of a place: wind in a park, traffic in a city, the hum of a room. It tells the viewer where they are and how big the space feels. A scene with no ambience can feel like a studio, while the right background makes the space believable. Ambience is usually kept low, because it should be felt rather than heard.</p>
<p>Keep the ambience consistent within a scene, and change it when the setting changes. A sudden change in background is a strong cue, and it should be intended.</p>
<h2>Music carries emotion</h2>
<p>Music shapes how the viewer feels about the scene. It can heighten tension, soften a moment or signal a change in tone. Music should be placed where it supports the emotion, and it should leave room for the dialogue and the effects. The most effective music is often the least obtrusive, because it guides feeling without drawing attention to itself.</p>
<h2>The basic balance</h2>
<p>A simple starting balance is dialogue at the top, effects close behind, ambience quieter and music adjusted to sit under the speech. Many soundtracks follow this order, and it keeps the speech clear. The exact levels depend on the scene, but the order helps you make decisions when the mix becomes crowded.</p>
<p>Check the balance on a phone speaker, where the lower layers are weaker and the dialogue must carry the scene.</p>
<h2>Planning the sound early</h2>
<p>Sound design works best when it is planned, not added at the end. Note the places where sound will matter: a key sound effect, a moment of silence, a transition, the start and end of music. Planning makes the soundtrack more deliberate, and it reduces the rush at the end of the edit. A simple sound plan, with a note for each scene, is enough for most short videos.</p>
<h2>Silence is a layer too</h2>
<p>Silence can be as powerful as sound. A brief moment without ambience or music can make the next sound feel stronger, or it can draw the viewer into a tense moment. Use silence on purpose, and avoid filling every second with sound. Many beginners find that removing a layer improves a scene more than adding one.</p>
<h2>Common mistakes</h2>
<ul>
<li>Letting music or effects mask the dialogue.</li>
<li>Using effects that are too quiet or too subtle to register on a phone.</li>
<li>Changing ambience without a reason, which confuses the sense of place.</li>
<li>Filling every moment with sound, so nothing stands out.</li>
<li>Adding sound at the end of the edit, rather than planning it.</li>
</ul>
<h2>An approach for short videos</h2>
<ol>
<li>Make the dialogue clear and consistent first.</li>
<li>Add ambience that matches each place, at a low level.</li>
<li>Add effects where the action happens, sized for the moment.</li>
<li>Add music that supports the emotion, and keep it under the speech.</li>
<li>Check the balance on a phone, and remove any layer that adds clutter.</li>
</ol>
<h2>Limits</h2>
<p>Sound design is a matter of judgement, and the right choices depend on the story, the genre and the audience. A horror film and a tutorial need very different soundtracks. Use the principles as a starting point, and let the scene tell you what it needs.</p>
<h2>Check the soundtrack on real devices</h2>
<p>A soundtrack that works on studio speakers may fail on a phone, where the dialogue must carry the scene. Listen to the finished video on a phone speaker and earbuds, and check that every key moment is clear. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the music side of the balance, read the <a href="/tunedzy/blog/how-to-mix-music-under-talking-in-a-video">music under talking post</a> in this series.</p>
''',
    faq=[('What is the most important layer in video?', 'Usually the dialogue, because the story depends on it being clear.'),
         ('Should I use a lot of effects?', 'Use effects where the action happens, sized for the moment. Too many make the soundtrack cluttered.'),
         ('How loud should ambience be?', 'Low enough to be felt rather than heard, and consistent within each scene.'),
         ('Why does silence matter?', 'It makes the next sound stronger and can draw the viewer into a tense moment.')])

add(slug='foley-explained-for-beginners', cluster='sound-design', kw='what is foley',
    title='What Is Foley? A Beginner Guide to Recreating Everyday Sounds',
    desc='What is foley? A beginner guide to recreating everyday sounds in the studio: what foley artists do, the basic kit and how creators can try it at home.',
    h1='What Is Foley? A Beginner Guide to Recreating Everyday Sounds',
    answer='Foley is the recreation of everyday sounds, such as footsteps, cloth movement and object handling, performed to match the picture. Foley artists use simple props and surfaces to create sounds that are more clear and controllable than the originals recorded on set. Creators can try foley at home with a few household objects and a close microphone.',
    body='''
<p>Foley is the art of recreating everyday sounds in sync with a picture. A footstep on a wooden floor, the rustle of a jacket, a cup set on a table, a door handle turned: these sounds are performed and recorded after filming, so they are clear, controlled and matched to the actions on screen. The name comes from the early film pioneer who developed the technique, and it is still a core part of film and video sound.</p>
<p>This post explains what foley is, why it is used, the basic approach and how a creator can try it at home without expensive equipment.</p>
<h2>Why foley is needed</h2>
<p>Sound recorded on set is often poor. Microphones pick up wind, traffic and other actors, and many small actions are too quiet to record well. Foley fills the gap by recreating those sounds in a controlled studio, where the artist can perform each action cleanly and repeat it until it matches the picture. The result is often richer and more precise than the original recording.</p>
<p>Foley also gives the director control over the detail of the soundtrack. A character can be made to feel heavier or lighter, and a scene can be given texture that the set did not provide.</p>
<h2>The basic approach</h2>
<p>A foley artist watches the scene, identifies each sound, and performs it in front of the microphone while watching the picture. The performance is recorded in layers: footsteps on one track, cloth on another, and objects on another still. The layers are then balanced and placed in the mix. The process is methodical, and the artist often performs each action several times to find the best take.</p>
<h2>The basic kit</h2>
<p>Foley studios use a range of surfaces and props. There are different floor materials for footsteps, cloth for movement, and everyday objects for handling. The props are chosen for the sound they make, not for their original purpose. A pair of shoes on gravel, a bag of crisps for crinkle, or a stack of paper for page turns are classic examples. Much of the art is in finding the right material for the right sound.</p>
<h2>Try foley at home</h2>
<p>Creators can try foley at home with household objects and a quiet room. Choose a clip with simple actions, such as someone walking, opening a door or picking up a cup. Play the clip on a loop, and perform the action while listening to the picture. Record several takes with a close microphone, then choose and place the best one.</p>
<p>Start with one action at a time. Footsteps are a good first project, because they are clear and easy to match. Experiment with different surfaces, such as a wooden board, a tile or a tray of dry rice, and listen to how each changes the sound.</p>
<h2>Recording technique</h2>
<p>Keep the microphone close and steady, and record in a dry, quiet space with soft surfaces around you. Use headphones so the playback does not bleed into the microphone. Record each sound separately, and keep the level steady so the layers can be balanced later. A clean, dry recording is easier to shape than a noisy one.</p>
<h2>Timing matters</h2>
<p>Foley depends on precise timing. A footstep that lands a fraction early or late looks wrong, even when the sound is good. Watch the clip carefully, and perform the action on the exact frame where it happens. Check the sync in the edit at normal speed, and adjust the placement until the sound and the action feel as one.</p>
<h2>Layering and balance</h2>
<p>Most foley is built from layers. A single footstep may combine a heel impact, a floor texture and a small rustle of cloth. Each layer is recorded separately, then balanced so the combined sound feels natural. Start with the strongest layer, and add the others gently until the result feels complete without being cluttered.</p>
<h2>Common mistakes</h2>
<ul>
<li>Recording with a distant microphone, so the sound feels thin.</li>
<li>Performing the action off the exact frame, so the sound lands late or early.</li>
<li>Using one layer where several are needed, which sounds flat.</li>
<li>Making each sound too loud, so it draws attention from the dialogue.</li>
<li>Forgetting to record a clean level, so the layers cannot be balanced.</li>
</ul>
<h2>Limits</h2>
<p>Foley is a skilled craft, and a beginner’s attempt will not match a professional studio. The aim is to learn the principle of matching sound to action, and to make small improvements to a video. Expect practice and patience, and treat each take as a lesson in listening.</p>
<h2>Keep the recording clean</h2>
<p>Clean recordings make layering easier. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps you judge a foley take. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the wider picture of how sound supports the picture, read the <a href="/tunedzy/blog/sound-design-basics-for-video">sound design basics post</a> in this series.</p>
''',
    faq=[('Is foley the same as sound effects?', 'Related but different. Foley is performed and recorded to match the picture, while effects may come from a library.'),
         ('What do I need to start foley?', 'A quiet room, a close microphone, headphones and a few household objects and surfaces.'),
         ('Why is foley timing so important?', 'A sound that lands a few frames off looks wrong, even when the sound itself is good.'),
         ('Why use several layers?', 'A single sound often sounds flat. Layers add texture and make the action feel real.')])

add(slug='ambience-and-room-tone-for-film', cluster='sound-design', kw='ambience for video',
    title='Ambience and Room Tone for Video: Making a Space Feel Real',
    desc='Ambience and room tone for video: how background sound places the viewer, how to record usable ambience and how to keep the sense of space consistent.',
    h1='Ambience and Room Tone for Video: Making a Space Feel Real',
    answer='Ambience is the background sound of a place, and room tone is the quiet, steady sound of a particular room. Together they make a space feel real and consistent. Record ambience and room tone on location, keep them at a low level under the speech, and match them between shots so the viewer stays in the same place.',
    body='''
<p>Every real space has a sound. A street has traffic and voices, a forest has wind and birds, a kitchen has a fridge and the clatter of crockery. When that sound is missing from a video, the space feels empty or artificial, even when the picture is convincing. Ambience and room tone are the layers that give a space its presence, and they are among the most useful tools in sound design.</p>
<p>This post explains the difference between ambience and room tone, how to record them, how to use them under speech and how to keep the sense of space consistent between shots.</p>
<h2>Ambience and room tone are different</h2>
<p>Ambience is the sound of a particular place with its activity: traffic, people, weather, machinery. Room tone is the steady, quiet sound of a room without any particular event, the hum that remains when nothing is happening. Ambience tells the viewer where they are, and room tone helps the edit feel continuous. Both are useful, and a good soundtrack often uses both.</p>
<h2>Why space matters</h2>
<p>The brain uses background sound to judge whether a space is large or small, quiet or busy, indoors or out. A scene with no background can feel like a studio set, while the right ambience makes the viewer believe the location. The space can also carry mood: a quiet room feels intimate, while a busy street feels energetic.</p>
<h2>Record ambience on location</h2>
<p>Record ambience at the location, at the time the scene is set. Use a recorder with a stereo or a single good microphone, placed in the position of the camera or the listener. Record several minutes of each space, so you have enough material to loop or to cover a scene. Note the time, the weather and any unusual events, so you can match the recording later.</p>
<h2>Record room tone</h2>
<p>Room tone is recorded with the room as quiet as possible, without any action. Stay still for thirty seconds or more, and let the room settle. Room tone is used to fill the gaps in an edit, to smooth joins and to keep the background consistent between takes. A short, clean sample from each room is one of the most valuable things a creator can collect.</p>
<h2>Keep ambience low</h2>
<p>Ambience should be felt rather than heard. Keep it well below the dialogue, and let it rise only when the scene needs more presence. A background that competes with the speech tires the viewer and makes the dialogue harder to follow. Check the level on a phone speaker, where the ambience may be almost lost, and adjust so the space is still audible.</p>
<h2>Match the sound between shots</h2>
<p>When the picture cuts between shots in the same place, the ambience should continue smoothly. A sudden change in background between shots breaks the sense of place, unless the change is intended. Use room tone to bridge the cuts, and match the level of the ambience across the scene.</p>
<h2>Looping and continuity</h2>
<p>Ambience recorded for a short scene may need to be looped to cover a longer one. Loops can reveal themselves through a repeated event, such as a single bird call returning at the same interval. Choose a loop point where nothing distinctive happens, and crossfade it smoothly. Vary the material with a second recording if the loop is long.</p>
<h2>Common mistakes</h2>
<ul>
<li>Leaving a scene with no background, so it feels like a studio.</li>
<li>Setting the ambience too loud, so it competes with the speech.</li>
<li>Changing the background between shots in the same place.</li>
<li>Looping a recording at an obvious repeated event.</li>
<li>Recording ambience in the wrong place or at the wrong time of day.</li>
</ul>
<h2>An approach for a short film or video</h2>
<ol>
<li>Record ambience and room tone at each location, with notes.</li>
<li>Place the ambience under the dialogue at a low, steady level.</li>
<li>Use room tone to smooth the cuts within a space.</li>
<li>Change the ambience only when the setting changes.</li>
<li>Check the space on a phone speaker and on headphones.</li>
</ol>
<h2>Limits</h2>
<p>Ambience and room tone depend on the location, the equipment and the weather, and some places are difficult to record cleanly. Recording in a busy city or a windy field requires patience and sometimes a second attempt. The goal is a believable space, not a perfect recording.</p>
<h2>Check the space on real devices</h2>
<p>Ambience can disappear on a phone, so test the finished video on a phone and earbuds. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps you judge a location recording. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the room tone technique in more depth, read the <a href="/tunedzy/blog/what-is-room-tone-and-how-to-record-it">room tone post</a> in this series.</p>
''',
    faq=[('What is room tone?', 'The steady, quiet sound of a room without any particular event, used to fill gaps and smooth cuts.'),
         ('How much ambience should I record?', 'Several minutes of each space, so there is enough to cover a scene or loop it.'),
         ('Why does the scene feel fake?', 'It may have no ambience, or the background changes between shots without a reason.'),
         ('How do I hide a loop?', 'Choose a loop point where nothing distinctive happens, and crossfade it smoothly.')])

add(slug='sound-effects-licences-explained', cluster='sound-design', kw='sound effects licence',
    title='Sound Effects Licences Explained: What You Can and Cannot Do',
    desc='Sound effects licences explained: the common types of licence, what they usually allow and restrict, and the checks to make before using a sound in a video.',
    h1='Sound Effects Licences Explained: What You Can and Cannot Do',
    answer='A sound effects licence sets out what you may do with a recorded sound, such as using it in a video, a game or an advert, and whether you can share or resell it. Licences differ widely, and some restrict commercial use, platform use or redistribution. Read the terms, keep a record of the licence, and check every sound before publishing.',
    body='''
<p>Sound effects are often bought, downloaded or found online, and many creators assume that anything they can access is free to use. That assumption can lead to takedowns, claims or a lost project. A sound effects licence is a set of terms, and each one decides what the creator may do with the sound. Understanding the common types of licence, and checking each one before use, is part of the professional habit of sound design.</p>
<p>This post explains the common licence types, what they usually allow and restrict, and the checks to make before a sound goes into a video. It is general guidance, not legal advice, and the terms of each licence matter more than any summary.</p>
<h2>Why licences matter</h2>
<p>A recorded sound is protected by copyright, and the person who recorded it may own the rights, even if the sound is short. Using it without permission can lead to a takedown, a claim or a demand for payment. A licence is the permission, and it defines the limits of that permission. Using a sound outside its licence is the same as using it without one.</p>
<h2>Common licence types</h2>
<ul>
<li><strong>Royalty-free:</strong> a one-off fee or subscription allows use across many projects, usually within limits set by the licence.</li>
<li><strong>Creative Commons:</strong> a family of licences with conditions, such as credit to the creator, and sometimes limits on commercial use.</li>
<li><strong>Editorial:</strong> use limited to news or commentary, without commercial endorsement.</li>
<li><strong>Personal or trial:</strong> use for learning or testing, not for publishing.</li>
<li><strong>Exclusive:</strong> the buyer alone may use the sound, which is usually expensive.</li>
</ul>
<h2>What licences often restrict</h2>
<p>Licences commonly restrict redistribution, which means you may not share or resell the raw sound. They may limit use in products, such as a sound library or a game asset. Some restrict use in adverts, political content or content that could be considered offensive. Some require credit, and some limit the number of projects or the platform. Read each restriction, and check it against your use.</p>
<h2>What to check before use</h2>
<ol>
<li>Confirm the licence covers your type of use, such as video, advert or game.</li>
<li>Check whether credit is required, and how it should be given.</li>
<li>Check any restriction on commercial use, platform or territory.</li>
<li>Keep a copy of the licence, with the date and the source of the sound.</li>
<li>Note the file name and the licence reference in the project, so you can find it later.</li>
</ol>
<h2>Keep a record</h2>
<p>A record is the best protection. Keep a folder of the licences, with each sound’s name, source and terms. When a question arises, the record shows what was agreed. Many creators lose track of licences over time, and a simple log prevents that. The same discipline applies to music, as covered in the <a href="/tunedzy/blog/podcast-intro-music-rules-and-safe-choices">intro music post</a>.</p>
<h2>Free does not mean unrestricted</h2>
<p>A sound offered for free may still have terms. It may require credit, forbid commercial use or restrict redistribution. Check the terms of every free sound, and treat “free” as the start of a check rather than the end of one.</p>
<h2>Recording your own sounds</h2>
<p>Recording your own sound effects removes the licence question entirely, because you own the recording. It is also a creative advantage, since your sounds are unlike anyone else’s. The next post in this series covers that approach, as set out in the <a href="/tunedzy/blog/making-your-own-sound-effects-at-home">home recording post</a>.</p>
<h2>Limits</h2>
<p>Licence terms vary widely, and this post cannot cover every licence. Where a project has significant value or risk, take advice from a professional who understands the local rules. Treat the terms as binding, and read them before you rely on a sound.</p>
<h2>Check every sound before publishing</h2>
<p>Before publishing, check the licence of each sound in the final mix. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the wider sound design context, read the <a href="/tunedzy/blog/sound-design-basics-for-video">sound design basics post</a> in this series.</p>
''',
    faq=[('Is a free sound safe to use?', 'Only if its licence allows your use. Check the terms, including any credit requirement.'),
         ('Does a short sound need a licence?', 'Yes. Length does not remove the rights, so check every sound, however short.'),
         ('What is the most common restriction?', 'Limits on commercial use, redistribution or the type of product the sound is used in.'),
         ('What should I keep on file?', 'The licence, the source, the date and the file name, linked to the project.')])

add(slug='making-your-own-sound-effects-at-home', cluster='sound-design', kw='make sound effects at home',
    title='Making Your Own Sound Effects at Home: A Practical Starting Point',
    desc='Making your own sound effects at home: recording everyday objects, building a personal library, avoiding rights questions and shaping sounds with care.',
    h1='Making Your Own Sound Effects at Home: A Practical Starting Point',
    answer='Making your own sound effects at home removes most licence questions, because you own the recordings, and it gives your work a distinctive sound. Record everyday objects and actions close and dry, label each file clearly, build a personal library over time and shape the sounds gently to suit the scene.',
    body='''
<p>Every sound effect starts as a real sound. A creator who records their own effects gains two advantages: the rights are simple, since the recording is their own, and the sounds are distinctive, because no one else has made them in quite the same way. Home recording is a practical way to build a library that suits your work, and it can be surprisingly rewarding.</p>
<p>This post explains how to start, what to record, how to record it well, how to build and label a library and how to shape sounds without losing their character.</p>
<h2>Why record your own</h2>
<p>A recording you make is yours to use, without the licence questions that come with a purchased or downloaded sound. It also avoids the problem of hearing the same effect in many other videos. A personal sound can become part of your signature, and it can be adjusted to fit your projects exactly. The effort is modest, and the benefits accumulate.</p>
<h2>What to record</h2>
<p>Start with everyday objects and actions that you can perform easily: a cup set down, a drawer closing, paper folded, keys dropped on a table, a zip pulled, a door opened and closed. Many effects that are used in film and video are simple objects performed with care. Work through the objects in your home, and note which ones produce interesting sounds.</p>
<h2>Set up the recording</h2>
<p>Record in a quiet, dry room with soft surfaces, such as a bedroom with curtains and a rug. Place the microphone close to the object, and keep the distance steady. Use headphones to monitor, and set the level with a short test, leaving room for the loudest moment. A clean, dry recording is much easier to shape later than a noisy or echoey one.</p>
<h2>Record several versions</h2>
<p>Perform each sound several times, varying the force, the speed and the surface. A door closing softly, normally and firmly gives you three useful sounds from one object. Record a few seconds of silence before and after each take, so the sound can be cut cleanly. Keep the best takes, and discard the rest.</p>
<h2>Label and organise</h2>
<p>Label each file with a clear name, the object, the action and the variation, for example “door_wood_close_soft”. Organise the files into folders by type, such as doors, paper or movement. A labelled library is easy to search, and it becomes more valuable as it grows. Record the date and the setup in the notes, so you can match new recordings to older ones.</p>
<h2>Shape the sounds gently</h2>
<p>Recorded sounds often need shaping: trimming the silence, adjusting the level, removing a little noise and sometimes adding a short fade. Keep the shaping gentle, so the sound remains natural. Heavy processing can make a sound artificial, which is the opposite of what a home recording is meant to achieve.</p>
<h2>Build the library over time</h2>
<p>A personal library grows slowly, one recording session at a time. Each project may reveal a need for a new sound, and each new sound makes the next project easier. Record when a need arises, and add the sound to the library with notes about where it worked. Over a year, the library becomes a resource that speeds up the work considerably.</p>
<h2>Common mistakes</h2>
<ul>
<li>Recording in an echoey room, which makes every sound sound far away.</li>
<li>Placing the microphone too far from the object, so the sound is thin.</li>
<li>Recording only one version of each sound.</li>
<li>Failing to label files, so the library becomes hard to search.</li>
<li>Processing the sounds so heavily that they lose their natural character.</li>
</ul>
<h2>A simple first session</h2>
<ol>
<li>Choose five objects that you can perform easily.</li>
<li>Set up a quiet, dry space, and test the level.</li>
<li>Record three versions of each action, with silence before and after.</li>
<li>Label the files and store them in a folder by type.</li>
<li>Use one of the sounds in a short video, and note how it worked.</li>
</ol>
<h2>Limits</h2>
<p>Home recordings will not match a professional library in every respect, and some sounds, such as large vehicles or explosions, are not practical to record at home. Focus on the sounds you can capture well, and use purchased or licensed sounds for the rest, with the licence checks described in the <a href="/tunedzy/blog/sound-effects-licences-explained">licences post</a>.</p>
<h2>Keep the recordings clean</h2>
<p>Clean source recordings make a library that is easy to use. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps you check each take. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the foley approach to making sounds, read the <a href="/tunedzy/blog/foley-explained-for-beginners">foley post</a> in this series.</p>
''',
    faq=[('Do I need expensive equipment?', 'Not to start. A quiet room, a close microphone and headphones are enough for many everyday sounds.'),
         ('Why record several versions?', 'The same object can give several useful sounds depending on how it is performed.'),
         ('How do I keep the library organised?', 'Label each file with the object, action and variation, and store it in folders by type.'),
         ('Can I use my own sounds commercially?', 'Yes, since you own the recordings, but check any people or trademarks that appear in them.')])

add(slug='whoosh-and-impact-sounds-explained', cluster='sound-design', kw='how to make a whoosh sound',
    title='Whoosh and Impact Sounds Explained: Making Motion and Hits Feel Real',
    desc='Whoosh and impact sounds explained: what they do in video, how they are built from layers and how to make motion and hits feel powerful without harshness.',
    h1='Whoosh and Impact Sounds Explained: Making Motion and Hits Feel Real',
    answer='Whoosh sounds suggest motion, and impact sounds suggest a hit or a landing. Both are usually built from layers: a source sound, a shaped tail and a bit of body. They work best when timed to the picture, matched to the speed of the action and kept at a level that adds force without harshness.',
    body='''
<p>Whoosh and impact sounds are among the most used effects in video. A whoosh suggests movement, such as a camera swing, a fast cut or a flying object. An impact suggests a hit, a landing or a sudden stop. Both are built to add energy to the picture, and both can sound harsh, thin or silly when they are done badly. A few principles make them feel powerful and believable.</p>
<p>This post explains how these sounds are usually built, what makes them work and how to avoid the common problems that make them feel cheap.</p>
<h2>What a whoosh does</h2>
<p>A whoosh gives the viewer a sense of speed and movement. It works because it follows the shape of the motion: it starts quietly, builds to a peak as the action passes the camera, and fades as the motion ends. The timing of the peak matters most, because the peak should coincide with the moment of fastest movement on screen.</p>
<h2>What an impact does</h2>
<p>An impact adds weight to a hit or a landing. It usually has a sharp attack, a body that carries the weight, and sometimes a tail that suggests the space around the hit. The attack gives the moment its punch, while the body and the tail make the sound feel solid. An impact that is only the attack can sound like a click, and one that is only the tail can sound like a wash.</p>
<h2>Building from layers</h2>
<p>Most convincing whooshes and impacts are built from layers. A whoosh may combine a rushing noise, a tonal swell and a small transient, each shaped separately. An impact may combine a short hit, a low body and a higher click. Build each layer to do one job, then balance them so the combined sound feels whole.</p>
<h2>Timing to the picture</h2>
<p>Timing is the most important factor. A whoosh that peaks before the motion looks early, while one that peaks after looks late. An impact that lands a few frames off the contact point looks wrong, even when the sound itself is good. Watch the clip at slow speed, mark the peak and the contact point, and align the sound precisely.</p>
<h2>Matching the speed</h2>
<p>A fast action needs a fast, sharp whoosh, and a slow action needs a longer, softer one. The length and the brightness of the sound should follow the speed of the motion. A slow, heavy movement with a bright whoosh can feel wrong, even when the timing is right.</p>
<h2>Keeping it powerful, not harsh</h2>
<p>Whooshes and impacts can easily become harsh, especially when they are boosted in the high frequencies. Keep the top end controlled, and listen on headphones and a phone for any edge that becomes unpleasant. A powerful sound has weight in the low and middle range, and its high frequencies serve the attack without dominating the mix.</p>
<h2>Using them in a mix</h2>
<p>Whooshes and impacts should sit clearly in the mix without masking the dialogue. Place them in the gaps between speech where possible, or lower them under the words. Check the balance with the dialogue playing, and ensure that the effect adds to the action rather than covering it.</p>
<h2>Common mistakes</h2>
<ul>
<li>Placing a whoosh so its peak misses the moment of fastest motion.</li>
<li>Using an impact with only an attack, which sounds like a click.</li>
<li>Making the top end so bright that the effect becomes harsh.</li>
<li>Using the same whoosh for very different speeds.</li>
<li>Letting an impact mask a line of dialogue.</li>
</ul>
<h2>A simple build for a whoosh</h2>
<ol>
<li>Start with a clean rushing sound, recorded or chosen for its texture.</li>
<li>Shape the level so it builds to a peak and fades out.</li>
<li>Add a tonal swell or a small transient to suggest the motion.</li>
<li>Align the peak with the fastest moment of the action.</li>
<li>Check the balance with the dialogue, and tame any harsh top end.</li>
</ol>
<h2>Limits</h2>
<p>These sounds are a matter of taste and of the picture, and what works for one edit may fail for another. A whoosh that suits a sci-fi scene may feel out of place in a documentary. Use the principles as a guide, and let the action tell you how big the effect should be.</p>
<h2>Check the impact on real devices</h2>
<p>An impact that feels powerful in studio headphones can sound thin or harsh on a phone. Listen on a phone speaker and earbuds before publishing. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping and level problems in a recording you own, which helps when an impact is recorded. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the layering approach, read the <a href="/tunedzy/blog/foley-explained-for-beginners">foley post</a> in this series.</p>
''',
    faq=[('What makes a whoosh convincing?', 'Timing the peak to the fastest moment of the motion, and matching its length to the speed.'),
         ('Why does my impact sound like a click?', 'It has only an attack. Add a body and, if needed, a tail to give it weight.'),
         ('How do I stop an effect sounding harsh?', 'Control the top end and check on headphones and a phone for any edge.'),
         ('Should I use one whoosh for every move?', 'No. Choose or build sounds that match the speed and weight of each action.')])

add(slug='sound-design-for-games-basics', cluster='sound-design', kw='game sound design basics',
    title='Sound Design for Games: The Basics of Interactive Audio',
    desc='Sound design for games: the basics of interactive audio, how sounds respond to the player, the role of variation and the balance that keeps play clear.',
    h1='Sound Design for Games: The Basics of Interactive Audio',
    answer='Game sound design is interactive: sounds respond to what the player does, and they must stay clear and varied over long play. Core tasks include planning sounds for actions, building variation so repeats do not tire, mixing so important cues always cut through, and keeping the overall balance comfortable for long sessions.',
    body='''
<p>Sound in a game is not fixed to a timeline, as it is in a film. It responds to the player. A footstep plays when the character moves, a weapon sounds when it is fired, and music changes when the situation changes. That interactivity makes game sound design a different discipline, with its own challenges: sounds must be clear, varied and balanced across hours of play, not just a few minutes of viewing.</p>
<p>This post introduces the basics of interactive audio, the main tasks a sound designer faces and the principles that keep a game’s sound working for the player.</p>
<h2>Sound responds to the player</h2>
<p>Each sound in a game is triggered by an event: a jump, a collision, a menu click, an enemy approaching. The designer plans the sound for each event, and the game decides when to play it. The sound should match the event clearly and promptly, because a delayed or missing sound can make the game feel unresponsive.</p>
<p>Planning a sound list early helps. Note each event, the sound it needs and the priority it has, so the design stays organised as the project grows.</p>
<h2>Variation keeps it fresh</h2>
<p>A sound that repeats exactly every time becomes tiring within minutes. Designers build variation by creating several versions of each common sound, and by changing pitch, timing and layers slightly from play to play. A footstep with four or five variations feels natural, while one repeated sound quickly feels mechanical.</p>
<p>Variation is one of the most important and most underestimated tasks, because it affects how the game feels over long sessions.</p>
<h2>Priority and cutting through</h2>
<p>Games can have many sounds at once, and the important ones must cut through. Designers set priorities, so a critical cue such as an alarm or a dialogue line is never masked by background effects. When many sounds play together, the system may reduce or stop lower-priority ones, and the design should plan for that.</p>
<h2>Music that responds</h2>
<p>Game music often changes with the situation, moving between calm and intense states. Designers plan transitions so the change feels musical, rather than abrupt. The music should support the gameplay, and it should not compete with the cues the player needs to hear.</p>
<h2>Mixing for long sessions</h2>
<p>A game may be played for hours, and the balance must stay comfortable throughout. Avoid harsh peaks, sudden loud effects and fatigue-inducing high frequencies. Test the mix over a long play session, not only a short clip, because problems that are tolerable for a minute can become tiring over an hour.</p>
<h2>Testing on the devices players use</h2>
<p>Players use headphones, speakers, televisions and laptops, and each reproduces sound differently. Test the mix on the common setups, and check that the important cues remain clear on the smallest speaker. A cue that cannot be heard on a laptop is a failed cue for many players.</p>
<h2>Common mistakes</h2>
<ul>
<li>Using one sound for an action that repeats often.</li>
<li>Letting background effects mask important cues.</li>
<li>Making music changes abrupt, which breaks immersion.</li>
<li>Mixing only for a short test, and missing fatigue over long play.</li>
<li>Forgetting to test on small speakers and laptops.</li>
</ul>
<h2>A simple planning routine</h2>
<ol>
<li>List each event that needs a sound, with its priority.</li>
<li>Create several variations for the sounds that repeat.</li>
<li>Set the priorities so the critical cues always cut through.</li>
<li>Plan music transitions for each change of state.</li>
<li>Test the mix over a long session, on several devices.</li>
</ol>
<h2>Limits</h2>
<p>Game audio tools and engines differ, and the techniques vary by genre and platform. This post describes the basic principles. A project with a large sound list will need a more detailed plan, and a specialist may be worth consulting for the technical implementation.</p>
<h2>Keep the sounds clean at the source</h2>
<p>Clean recordings are the starting point for every game sound. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps when you record voices or effects. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the effects side of the craft, read the <a href="/tunedzy/blog/whoosh-and-impact-sounds-explained">whoosh and impact post</a> in this series.</p>
''',
    faq=[('Why do game sounds need variation?', 'A repeated sound becomes tiring within minutes, especially in a long session.'),
         ('What is sound priority?', 'The rule that keeps the most important cues audible when many sounds play at once.'),
         ('How do I test a game mix?', 'Play a long session on several devices, including a laptop and a small speaker.'),
         ('Should music change abruptly?', 'No. Plan transitions that feel musical, so the change supports the moment.')])

add(slug='audio-branding-explained', cluster='sound-design', kw='audio branding',
    title='Audio Branding Explained: How Brands Use Sound to Be Recognised',
    desc='Audio branding explained: how brands use sound to be recognised, the elements of a sound identity and how creators can apply the idea.',
    h1='Audio Branding Explained: How Brands Use Sound to Be Recognised',
    answer='Audio branding is the use of sound to make a brand recognisable and consistent, through elements such as a logo sound, a theme, a voice and a set of recurring effects. A clear audio identity builds recognition across adverts, apps and videos, and it works best when the sounds are few, consistent and used with purpose.',
    body='''
<p>Many brands are known by their sound as well as their look. A short chime at the start of an app, a familiar musical phrase in an advert, or a particular voice on a phone line can be recognised in seconds. Audio branding is the deliberate design of these sounds, so that a brand is consistent across every place where people hear it. For creators and small businesses, the same ideas can make a show or a channel more recognisable.</p>
<p>This post explains what audio branding is, the elements that make up a sound identity, how the principles apply to a small creator and the limits that keep the approach honest.</p>
<h2>What audio branding is</h2>
<p>Audio branding is a system of sounds that represents a brand. It includes the sounds the brand uses for itself, such as a sonic logo, and the sounds that surround its products and services, such as the tones of an app or the voice of a phone system. The goal is consistency: each sound should feel like it belongs to the same brand, even when it appears in very different places.</p>
<p>The idea works because sound is memorable and quick to recognise. A few notes can be enough to bring a brand to mind, especially when they are heard often.</p>
<h2>The elements of a sound identity</h2>
<ul>
<li><strong>Sonic logo:</strong> a short, distinctive sound that identifies the brand at the start or end of a message.</li>
<li><strong>Theme or bed:</strong> a longer musical idea used in content, such as a podcast intro or a video background.</li>
<li><strong>Voice:</strong> the sound and tone of the brand’s spokesperson or narrator.</li>
<li><strong>Effects palette:</strong> a small set of recurring sounds, such as clicks, swooshes or notifications.</li>
<li><strong>Rules:</strong> guidance on where each sound is used, and how loud it should be.</li>
</ul>
<h2>Why consistency matters</h2>
<p>A sound identity works only when it is used consistently. A brand that changes its sonic logo often, or uses a different voice in every advert, weakens its recognition. Consistency builds familiarity, and familiarity builds trust. The rules that guide the sound identity are as important as the sounds themselves.</p>
<h2>A small creator can borrow the idea</h2>
<p>A podcast or video channel can have a simple audio identity too. A short intro sound, a consistent voice level, a recurring effect at the start of each segment and a steady loudness all make the show recognisable. None of these needs a large budget. They need a decision, written down, and the discipline to use them each time.</p>
<h2>Keep the identity simple</h2>
<p>A sound identity should be easy to remember and easy to produce. Too many sounds, or sounds that are too complex, make the identity hard to use consistently. A few well-chosen elements, used well, beat a large library used carelessly.</p>
<h2>Test the identity in context</h2>
<p>A sound identity must work in the places where people hear it: a phone speaker, a car, a laptop and a loud environment. Test each element in those conditions, and check that it is recognisable at a low level. A sonic logo that cannot be heard on a phone speaker will not do its job.</p>
<h2>Common mistakes</h2>
<ul>
<li>Changing the identity too often, so recognition never builds.</li>
<li>Using too many sounds, so none stands out.</li>
<li>Making sounds that are too loud or too long for their purpose.</li>
<li>Designing the identity without rules for its use.</li>
<li>Testing only in the studio, and not on the devices people use.</li>
</ul>
<h2>Limits</h2>
<p>Audio branding is a long-term investment, and its effect depends on how consistently it is used. It cannot rescue a poor product or a weak message. The sound should support the brand, not replace the qualities that make it worth hearing. Adapt the ideas to your scale, and keep the identity honest.</p>
<h2>Check the identity on real devices</h2>
<p>Test every sound on a phone and in a noisy place before fixing the identity. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps when you record the voice or the effects. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the short sonic element itself, read the <a href="/tunedzy/blog/sonic-logo-what-it-is">sonic logo post</a> in this series.</p>
''',
    faq=[('What is audio branding?', 'The deliberate design of sounds that make a brand recognisable and consistent.'),
         ('Do small creators need it?', 'A simple version helps: a consistent intro, a steady loudness and a recurring effect.'),
         ('How many sounds should an identity have?', 'A few, well chosen and used consistently, rather than a large library used carelessly.'),
         ('What makes an identity fail?', 'Frequent changes, too many sounds and no rules for how they are used.')])

add(slug='sonic-logo-what-it-is', cluster='sound-design', kw='sonic logo',
    title='What Is a Sonic Logo and How to Design One Simply',
    desc='What is a sonic logo and how to design one simply: the qualities of a memorable short sound, how it is used and how a creator can make a small version.',
    h1='What Is a Sonic Logo and How to Design One Simply',
    answer='A sonic logo is a short, distinctive sound that identifies a brand or show, usually heard at the start or end of a message. A good sonic logo is brief, memorable, easy to reproduce and recognisable at a low volume. It works best when it is used consistently and kept simple enough to survive on small speakers.',
    body='''
<p>A sonic logo is the audio equivalent of a visual logo: a short sound that brings a brand to mind. It can be a few notes, a single chord or a brief combination of tones and effects. Many brands use a sonic logo at the start of an advert or an app, and it becomes a signal that the listener recognises before they see anything else. For a creator, a simple sonic logo can serve as a clear and friendly opening for a show.</p>
<p>This post explains what makes a sonic logo work, how it is designed and used, and how a small creator can make one without a large budget.</p>
<h2>What makes a sonic logo work</h2>
<p>A good sonic logo is short, usually a few seconds or less. It is distinctive, so it does not sound like other sounds the listener knows. It is simple enough to remember after one or two hearings, and it sounds clear on small speakers. Most importantly, it is consistent: it appears in the same form each time, so the listener learns it.</p>
<h2>Keep it short and simple</h2>
<p>A long sonic logo asks too much of the listener. A short phrase, a small sequence of notes or a brief chime is easier to remember and to place. Test the length by playing it once, then asking yourself whether you could hum it after a minute. If not, shorten it.</p>
<h2>Make it recognisable at low volume</h2>
<p>Many sonic logos are heard on phones, in cars or in noisy places, where they may be quiet. Design the sound so its character survives at a low level, with a clear tone that does not depend on deep bass or very high frequencies. Test it on a phone speaker, and adjust until it is recognisable at a comfortable volume.</p>
<h2>Design the sound with care</h2>
<p>A sonic logo can be built from a musical phrase, from a short synthesised tone or from a recorded sound with a distinctive character. Choose a sound that suits the brand or show: bright and friendly for a light-hearted show, warm and gentle for a reflective one. Keep the number of elements low, so the sound is clean and easy to reproduce.</p>
<h2>Use it consistently</h2>
<p>Use the sonic logo in the same place each time, usually at the start or end of an episode or message. Keep the same version, with the same level and character. Changing it often prevents the listener from learning it. A sonic logo earns its recognition through repetition.</p>
<h2>A simple way to make one</h2>
<ol>
<li>Write down the feeling the sound should give: friendly, serious, playful or calm.</li>
<li>Create two or three short versions, each under three seconds.</li>
<li>Play each one on a phone speaker, at a low volume.</li>
<li>Choose the one that is memorable and clear, and remove any unnecessary part.</li>
<li>Use the chosen version consistently, and write the rule in your project notes.</li>
</ol>
<h2>Common mistakes</h2>
<ul>
<li>Making the sound too long for its purpose.</li>
<li>Designing it only for studio headphones.</li>
<li>Changing the sound before listeners have learned it.</li>
<li>Choosing a sound that is too close to a familiar one, so it is confused.</li>
<li>Using it so often that it becomes tiring.</li>
</ul>
<h2>Limits</h2>
<p>A sonic logo cannot make an unknown show famous, and it cannot replace good content. It works as a consistent signal, and its value grows with repetition and with the quality of what follows it. Keep the expectations realistic, and judge the sound by how well it serves the show.</p>
<h2>Test the sound before you commit</h2>
<p>Check the sonic logo on the devices your listeners use before committing to it. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping and level problems in a recording you own, which helps if the sound includes a voice. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the wider identity, read the <a href="/tunedzy/blog/audio-branding-explained">audio branding post</a> in this series.</p>
''',
    faq=[('How long should a sonic logo be?', 'Usually a few seconds or less, short enough to remember after a couple of hearings.'),
         ('Should it be loud?', 'It should be clear at a comfortable volume, and recognisable on a phone speaker.'),
         ('Can a podcast have a sonic logo?', 'Yes. A short, consistent sound at the start of each episode works well.'),
         ('How often should I change it?', 'Rarely. Repetition is what makes it recognisable, so keep the same version.')])

add(slug='sound-for-short-form-ads', cluster='sound-design', kw='sound for ads',
    title='Sound for Short-Form Ads: Getting Attention in the First Second',
    desc='Sound for short-form ads: how to grab attention in the first second, keep the message clear on small speakers and use music and effects without masking the offer.',
    h1='Sound for Short-Form Ads: Getting Attention in the First Second',
    answer='Sound for a short-form ad must grab attention quickly and keep the message clear on small speakers. Open with a clear voice or a strong sound in the first second, keep the music under the message, use effects sparingly to emphasise the offer, and check the result with the sound off and on, on a phone.',
    body='''
<p>A short-form ad has only seconds to win the viewer’s attention. Many people watch with the sound off, and many who listen do so on a phone speaker in a noisy place. The sound must work in those conditions, and it must support the message rather than compete with it. A good ad uses sound to make the first second count, to carry the offer clearly and to leave a memorable impression.</p>
<p>This post explains how to use sound in short-form advertising, from the opening second to the final call to action, with the checks that keep the message clear.</p>
<h2>Open with purpose</h2>
<p>The first second decides whether many viewers stay. A strong opening can be a clear voice, a distinctive sound or a surprising moment, but it must be purposeful. A sound that is pleasant but meaningless wastes the moment. Open with the element that tells the viewer what the ad is about, and let the sound support that message.</p>
<h2>Keep the voice clear</h2>
<p>In most short ads, the voice carries the message. It must be clear, close and easy to understand on a phone speaker. Record it in a quiet room with the microphone close, and check the level so the words are not lost under music or effects. Subtitles help viewers who watch with the sound off, but the voice must still work on its own.</p>
<h2>Music under the message</h2>
<p>Music in a short ad sets the mood and the pace, but it must sit under the voice. Choose a track with a clear rhythm and little vocal, and duck it when the message is spoken. Make sure the music is licensed for advertising, since advertising uses are often restricted more than general content use. The <a href="/tunedzy/blog/how-to-mix-music-under-talking-in-a-video">music under talking post</a> covers the balance.</p>
<h2>Use effects to emphasise the offer</h2>
<p>A well-placed effect can draw attention to the offer, such as a short chime when a price appears or a swoosh when a product arrives. Use effects sparingly, and place them exactly where the message needs emphasis. Too many effects make the ad feel busy and reduce the impact of each one.</p>
<h2>Plan for the sound off</h2>
<p>Many viewers watch without sound, so the message must work visually as well. Use captions for the key words, and make sure the picture alone tells the story. The sound then adds to the experience rather than being the only way the message gets through.</p>
<h2>End with a clear call to action</h2>
<p>The end of the ad is where the call to action lands. Use a clear voice, a short phrase and perhaps a final sound that signals the end. Keep the final moment simple and memorable, so the viewer knows what to do next. A rushed ending or a sudden cut can lose the action the ad was built to deliver.</p>
<h2>Check on a phone with the sound off and on</h2>
<p>Test the ad on a phone in both conditions: sound off, to check the picture and captions, and sound on, to check the voice and the balance. Listen in a noisy place if you can. An ad that works only in a quiet studio is not ready.</p>
<h2>Common mistakes</h2>
<ul>
<li>Opening with a sound that is pleasant but carries no message.</li>
<li>Letting music mask the voice or the offer.</li>
<li>Using too many effects, so none stands out.</li>
<li>Forgetting that many viewers watch with the sound off.</li>
<li>Ending abruptly, so the call to action is lost.</li>
</ul>
<h2>Limits</h2>
<p>Advertising rules differ by country and sector, and claims in an ad must be accurate and fair. Sound can make a claim feel stronger than the facts support, so check every line of the script against the rules that apply. This post covers the craft of sound, not the legal approval of the content. For an ad with significant spend, take advice on the rules.</p>
<h2>Check the ad on the screens people use</h2>
<p>Final checks should include the phone, where most short ads are watched. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording you own, which helps with the voice-over. The <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the wider sound design balance, read the <a href="/tunedzy/blog/sound-design-basics-for-video">sound design basics post</a> in this series.</p>
''',
    faq=[('What matters most in the first second?', 'A sound or voice that tells the viewer what the ad is about, placed purposefully.'),
         ('Should the music be loud?', 'No. It should sit under the voice and support the mood without masking the message.'),
         ('How do I reach viewers with the sound off?', 'Use captions for key words and make sure the picture alone tells the story.'),
         ('Can I use any track in an ad?', 'No. Advertising uses are often restricted, so check the licence for advertising specifically.')])
