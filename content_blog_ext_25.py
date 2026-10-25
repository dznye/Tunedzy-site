"""Blog posts, batch 25: field recording and nature sounds (evergreen). Merged into content_blog.py.
Field recording advice is practical and cautious. Wildlife and location recording points note the need to respect
animals, places and people. No invented statistics. Funnel: each post ends with a link to Tunedzy Go and to the
matching free tool."""

CLUSTERS = {
    'nature-sounds': dict(tool='voice-recorder-noise-cancellation', label='Field recording and nature sounds', tool_name='Noise-Free Voice Recorder'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='field-recording-for-beginners', cluster='nature-sounds', kw='field recording for beginners',
    title='Field Recording for Beginners: Capturing Sound Where It Happens',
    desc='Field recording for beginners: what field recording is, the basic kit, how to choose a location and the habits that produce clean, usable sound outdoors.',
    h1='Field Recording for Beginners: Capturing Sound Where It Happens',
    answer='Field recording captures sound where it happens, outdoors or in real locations, for use in video, music, sound libraries and personal projects. Beginners need a portable recorder, a windscreen, headphones and a habit of listening before pressing record. Choose the location carefully, control wind and handling noise, and record generously so there is material to choose from.',
    body='''
<p>Field recording is the practice of capturing sound at the place where it happens. It might be a street market, a forest after rain, a workshop, a train station or a quiet morning in a garden. The recordings can be used in videos, music, sound design, documentary work or simply as a personal archive of places. The practice is accessible, and a beginner can start with a modest recorder and a pair of headphones.</p>
<p>This post introduces the basics: what field recording involves, the kit that matters most, how to choose a location, and the habits that produce clean, usable sound outdoors.</p>
<h2>What field recording is</h2>
<p>A field recording is a sound captured in its natural setting, without the controlled conditions of a studio. The sound carries the character of the place: its size, its activity and its weather. Because the environment is uncontrolled, field recording is partly a matter of patience, timing and careful listening, as much as technical skill.</p>
<p>The results can be surprisingly rich. A recording of a busy street, a rainstorm or a crackling fire can carry more atmosphere than a generated sound, because it is the real thing.</p>
<h2>The basic kit</h2>
<p>A portable recorder with a good microphone is the core of the kit. A pair of closed-back headphones lets you hear what you are capturing, and a windscreen is essential for almost every outdoor recording. Spare batteries or a power bank, and enough storage for long sessions, complete the basics. You do not need the most expensive equipment to start. A reliable, simple recorder used well will produce more useful sound than an elaborate setup used carelessly.</p>
<h2>Choose the location</h2>
<p>Location decides most of what you capture. Look for places where the sound you want is clear and the sound you do not want is limited. A park far from roads is better for birds than a park next to a main road. A harbour at dawn may be quieter than at midday. Visit the location before recording, listen at different times, and note the sounds that come and go.</p>
<h2>Control the wind</h2>
<p>Wind is the most common problem in field recording. Even a light breeze can roar across the microphone and bury the sound you came for. Use a windscreen, and for strong wind a furry cover. Shelter the microphone behind a bush, a wall or your own body, and keep it low to the ground if the wind is coming from above. A recording that is spoiled by wind cannot usually be repaired.</p>
<h2>Control handling noise</h2>
<p>Handling noise comes from touching the recorder or its cable. Use a stand, a mount or a shock mount where possible, and keep your hands off the recorder during the take. Set the recorder down on a soft surface, and keep the cable slack so it does not tug. Many beginners lose good material to a bump they did not notice.</p>
<h2>Listen before you record</h2>
<p>Stand still for a minute before recording, and listen. Note the sounds that dominate, the sounds that come and go and the sounds that are background. Move the microphone a little, and listen again. The best position is often a few metres from where you first stood, and listening is how you find it.</p>
<h2>Record generously</h2>
<p>Record longer than you think you need. A field session can produce a few minutes of usable material from an hour of recording, and the extra time lets you capture moments you did not expect. Start each recording with a few seconds of silence, and note the time, the place and the conditions.</p>
<h2>Common mistakes</h2>
<ul>
<li>Recording without a windscreen, so the wind dominates.</li>
<li>Touching the recorder during a take, so handling noise appears.</li>
<li>Recording in the middle of the busiest moment, and missing the quiet.</li>
<li>Forgetting to note the place, the time and the conditions.</li>
<li>Stopping too early, and missing the best moment of the session.</li>
</ul>
<h2>A first outing</h2>
<ol>
<li>Choose one place near home that has interesting sound.</li>
<li>Visit at two different times, and listen before recording.</li>
<li>Record for twenty minutes, with a windscreen and headphones.</li>
<li>Label the files with the place, the time and the conditions.</li>
<li>Listen back, and note what you would change next time.</li>
</ol>
<h2>Respect the place and the people</h2>
<p>Field recording often takes place in public, and it can involve other people and animals. Respect their privacy, avoid recording identifiable people without consent when you plan to publish, and do not disturb wildlife or sensitive habitats. Some locations have rules about recording, and some private spaces need permission. Check before you go.</p>
<h2>Limits</h2>
<p>Field recording depends on weather, season and luck. A session may be ruined by an unexpected plane or rain, and that is part of the practice. The aim is to learn to listen, to plan and to accept what the environment offers. Expect many recordings you will not use, and treat each one as practice.</p>
<h2>Clean the recordings gently</h2>
<p>Outdoor recordings often need light cleanup, such as reducing a steady background or removing a single click. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the wind side of the work, read the <a href="/tunedzy/blog/how-to-remove-wind-noise-from-a-recording">wind noise post</a> in this series.</p>
''',
    faq=[('What do I need to start?', 'A portable recorder, a windscreen, headphones and a few spare batteries and storage cards.'),
         ('What is the biggest problem outdoors?', 'Wind. A windscreen and sheltered positions prevent most of it.'),
         ('How long should I record?', 'Longer than you think. Record generously, since many minutes of a session may be unusable.'),
         ('Do I need permission to record?', 'Sometimes. Check the rules for the location and respect the people and animals there.')])

add(slug='recording-nature-sounds-at-home', cluster='nature-sounds', kw='record nature sounds',
    title='Recording Nature Sounds at Home: Bringing the Outdoors Indoors Safely',
    desc='Recording nature sounds at home: capturing birds, insects and weather from a window, garden or balcony, with tips for clean results and respect for neighbours.',
    h1='Recording Nature Sounds at Home: Bringing the Outdoors Indoors Safely',
    answer='You can record nature sounds at home from a window, a garden or a balcony. Choose a quiet time of day, place the microphone outside and sheltered from wind, keep the room sound low, and record generously. Respect neighbours, and avoid disturbing animals or nesting birds.',
    body='''
<p>Nature sounds are a rich resource for video, music and relaxation, and many can be recorded without travelling. A garden, a balcony or an open window can carry birdsong, insects, rain on leaves and the sound of a breeze. Recording at home is convenient, and it lets you return to the same place across the seasons, which gives you a sense of how a location changes over time.</p>
<p>This post explains how to record nature sounds from home, the equipment and placement that help, the common problems and how to respect neighbours and wildlife.</p>
<h2>Why record at home</h2>
<p>Home recording is practical. You can choose the time of day, return to the same spot and avoid the cost of travel. Over months, a single garden can produce a remarkable range of sounds, from the dawn chorus in spring to the quiet of winter. The familiarity also helps: you learn the sounds and know when they will occur.</p>
<h2>Choose the spot</h2>
<p>Place the microphone outside if you can, away from the house’s walls and windows. Sound reflected from walls and glass makes a recording sound indoors, which is rarely what you want for a nature recording. A corner of the garden, a balcony rail or a spot under a tree often works well. Test a few positions by listening on headphones before settling on one.</p>
<h2>Control the wind and the traffic</h2>
<p>Wind is the main enemy of outdoor recording, even at home. Use a windscreen and shelter the microphone behind a fence or a plant. Traffic, aircraft and neighbours can also dominate. Record at quieter times, such as early morning or late evening, and note the times when the background is lowest.</p>
<h2>Set the level</h2>
<p>Nature sounds can be very quiet, and then suddenly loud, as a bird calls close by or a gust passes. Set the level with a short test, leaving room for the loudest moment. A recording that clips on a sudden call cannot be repaired, so leave headroom.</p>
<h2>Record for long periods</h2>
<p>Nature sounds happen unpredictably, and a long recording gives you the best chance of capturing them. Record for an hour or more at a time, and choose the best moments later. Keep the battery and the storage in mind, and check the recorder at intervals during long sessions.</p>
<h2>Respect the neighbours</h2>
<p>Recording in a garden can involve neighbours, who may be heard on the recording or may be disturbed by the microphone. Be considerate: avoid recording private conversations, and let neighbours know if you plan a long session. A friendly word goes a long way, and it protects your ability to keep recording in the same place.</p>
<h2>Respect the wildlife</h2>
<p>Recording animals should never harm them. Keep a respectful distance, avoid disturbing nests, and do not use playback to attract birds in ways that could affect their behaviour. If an animal changes its behaviour because of you, stop. The best nature recordings are made quietly and patiently.</p>
<h2>Common mistakes</h2>
<ul>
<li>Recording next to a wall, so the sound seems indoors.</li>
<li>Forgetting the windscreen, so a light breeze spoils the take.</li>
<li>Setting the level by a quiet moment, then clipping on a sudden call.</li>
<li>Recording only briefly, and missing the moments that matter.</li>
<li>Disturbing animals or neighbours to get a better recording.</li>
</ul>
<h2>A first home session</h2>
<ol>
<li>Choose a spot outside, away from walls and windows.</li>
<li>Listen for a few minutes, and note the sounds and the background.</li>
<li>Set the level with a test, leaving headroom.</li>
<li>Record for an hour, with a windscreen in place.</li>
<li>Label the file with the date, the time and the weather.</li>
</ol>
<h2>Limits</h2>
<p>A home garden has limits: it may be noisy, small or dominated by a few species. Recordings made at home will not capture the full range of a wild landscape, and that is fine. The aim is to listen closely to the place you have, and to record it honestly.</p>
<h2>Clean the recordings with restraint</h2>
<p>Nature recordings should sound natural, so keep cleanup light. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the labelling habit that keeps a home archive useful, read the <a href="/tunedzy/blog/labelling-field-recordings">labelling post</a> in this series.</p>
''',
    faq=[('Where should I place the microphone?', 'Outside, away from walls and windows, and sheltered from the wind.'),
         ('When is the best time to record?', 'Often early morning or late evening, when the background is quieter.'),
         ('Should I use playback to attract birds?', 'No. It can change animal behaviour, so avoid it.'),
         ('Can I record without disturbing neighbours?', 'Mostly, by being considerate and telling them about long sessions.')])

add(slug='how-to-record-birdsong', cluster='nature-sounds', kw='how to record birdsong',
    title='How to Record Birdsong: Patience, Placement and Respect',
    desc='How to record birdsong: finding the right place and time, placing the microphone, handling the level and keeping the birds undisturbed.',
    h1='How to Record Birdsong: Patience, Placement and Respect',
    answer='Recording birdsong rewards patience. Find a place where birds are active, arrive early, keep still and place the microphone where it can hear the birds without the traffic or wind dominating. Record long sessions, keep your distance, and never disturb nests or change the birds’ behaviour.',
    body='''
<p>Birdsong is one of the most beautiful sounds in nature, and one of the most rewarding to record. A good recording can capture the dawn chorus, the call of a single species or the subtle chatter of a flock. It takes patience, careful placement and respect for the birds, but the results can be remarkable, and they can enrich videos, music and personal archives.</p>
<p>This post covers choosing a place and time, placing the microphone, setting the level and keeping the birds undisturbed.</p>
<h2>Choose the place and the time</h2>
<p>Birds are most active early in the morning, and again in the evening, so the dawn chorus is often the best time to record. Choose a place with trees, shrubs or water, where birds gather. A quiet park, a woodland edge or a garden with feeders can all be good. Visit the place several times before recording, and learn when the birds are most active.</p>
<h2>Arrive early and keep still</h2>
<p>Arrive before the birds become active, and set up quietly. Movement and voices scare birds away, so keep still once you have settled. Many experienced recordists wait for twenty minutes or more before the birds return to their normal behaviour. Patience is the most important skill in birdsong recording.</p>
<h2>Place the microphone</h2>
<p>Place the microphone where it can hear the birds clearly, usually a few metres from the trees they use. Too close can disturb the birds and capture every rustle, while too far can lose the detail. Test a few positions by listening on headphones, and move the microphone slowly to find the sweet spot.</p>
<h2>Handle the wind and the background</h2>
<p>Wind and distant traffic are the main problems. Use a windscreen, and choose a sheltered position if possible. Record early in the morning, when traffic is light, and note the background sounds that you cannot avoid. A recording with some background can still be beautiful, as long as the birds are clear.</p>
<h2>Set the level</h2>
<p>Birds can be quiet and then suddenly loud, and a close call can overload the recording. Set the level with a short test, leaving headroom for the loudest song. Use the peak meter, and watch for clipping during the first few minutes of activity.</p>
<h2>Record long sessions</h2>
<p>Birds do not sing on demand, and a long session gives you the best chance of capturing a full range of calls. Record for an hour or more, and choose the best moments later. Keep the battery and storage in mind, and check the recorder at intervals.</p>
<h2>Respect the birds</h2>
<p>Keep a respectful distance, especially during nesting season. Do not approach a nest, and do not play recordings of other birds to attract the birds you want, since this can change their behaviour and stress them. If a bird stops singing or moves away because of you, step back and wait. A recording that harms a bird is not worth making.</p>
<h2>Identify the species</h2>
<p>Note the species you hear, if you can identify them. A short note with the date, the time and the place adds value to the recording, especially if it is used in a video or an archive. Local birdwatching groups and identification apps can help, and you can learn the calls over time.</p>
<h2>Common mistakes</h2>
<ul>
<li>Arriving late, after the best activity has passed.</li>
<li>Moving about and frightening the birds away.</li>
<li>Recording too close to a nest, and disturbing the birds.</li>
<li>Playing other birds’ calls to attract the birds, which can harm them.</li>
<li>Recording without a windscreen, so the wind spoils the take.</li>
</ul>
<h2>A first birdsong session</h2>
<ol>
<li>Visit the place once, at the time you plan to record, and listen.</li>
<li>Arrive early, and set up quietly.</li>
<li>Test the microphone position on headphones, and set the level.</li>
<li>Record for an hour with a windscreen in place.</li>
<li>Label the file with the date, the time, the place and any species you identified.</li>
</ol>
<h2>Limits</h2>
<p>Birdsong recording depends on the season, the weather and the local birds. Some days will be quiet, and some species may be rare. The aim is to capture the place honestly, and to respect the birds throughout. A quiet session is still a session, and it teaches you the place.</p>
<h2>Keep the cleanup light</h2>
<p>Birdsong should sound natural, so keep cleanup gentle. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the outdoor sound basics, read the <a href="/tunedzy/blog/field-recording-for-beginners">field recording post</a> in this series.</p>
''',
    faq=[('When is the best time to record birdsong?', 'Early morning, around dawn, when birds are most active.'),
         ('How close should I put the microphone?', 'Close enough to hear the birds clearly, but not so close that you disturb them or their nests.'),
         ('Can I play other birds to attract them?', 'It is better not to. It can change behaviour and stress the birds.'),
         ('Do I need to identify the species?', 'It adds value to the recording, but a recording without identification is still useful.')])

add(slug='recording-rain-and-water-sounds', cluster='nature-sounds', kw='record rain sounds',
    title='Recording Rain and Water Sounds: Capturing Weather and Movement',
    desc='Recording rain and water sounds: placing the microphone for rain on different surfaces, capturing streams and waves, and managing wind and splash.',
    h1='Recording Rain and Water Sounds: Capturing Weather and Movement',
    answer='Recording rain and water sounds rewards attention to surface, distance and wind. Rain sounds differ on leaves, roofs, pavements and water, and each needs a different placement. Use a windscreen, keep the microphone sheltered from splash, and record long enough to capture the changing intensity of the weather.',
    body='''
<p>Rain and water sounds are among the most calming and atmospheric recordings a creator can make. A soft rain on leaves, a heavy downpour on a metal roof, a stream over stones or waves on a shore all carry character and mood. The sounds are also surprisingly varied, because the surface, the distance and the intensity of the water change the sound dramatically.</p>
<p>This post explains how to place the microphone for different kinds of rain and water, how to handle wind and splash and how to record for long enough to capture the full range of the weather.</p>
<h2>Rain on different surfaces</h2>
<p>Rain sounds differ greatly with the surface it falls on. Leaves produce a soft, broken patter, a roof produces a steady drum, a pavement produces a sharper hiss, and water produces a bright, gentle splash. Choose the surface you want, and place the microphone to capture it. Record several surfaces in the same storm, if you can, to hear the contrast.</p>
<h2>Place the microphone</h2>
<p>Place the microphone a little away from the main surface, so the sound is balanced rather than dominated by one drip or puddle. Angle it toward the rain, and keep it under cover if possible, since heavy drops on the microphone itself can be very loud and unpleasant. Test the position on headphones before the rain intensifies.</p>
<h2>Handle wind and splash</h2>
<p>Wind is the most common problem with outdoor rain recordings, as it can roar across the microphone. Use a windscreen, and shelter the microphone behind a wall or an overhang. Splash from nearby puddles and water can also be too loud, so keep the microphone above the splash line and away from direct spray.</p>
<h2>Water sounds: streams and waves</h2>
<p>Streams produce a continuous, changing sound that is pleasant to record. Place the microphone close enough to hear the water clearly, but not so close that it is overwhelmed by splash. Waves on a shore vary in rhythm, and a recording of several minutes captures the variation. Record away from the surf line, to avoid the strongest spray.</p>
<h2>Set the level</h2>
<p>Rain and water can be steady and then suddenly loud, as a gust or a large wave passes. Set the level with a short test, leaving room for the loudest moment. A sudden peak that clips cannot be repaired, so headroom matters even for steady-looking sounds.</p>
<h2>Record for long periods</h2>
<p>The weather changes, and so does the sound. A rainstorm may begin softly, build to a peak and ease off. Record for long enough to capture that arc, and for a long stream or sea recording, record for many minutes to capture the variation. Check the battery and the storage, since long recordings use both.</p>
<h2>Common mistakes</h2>
<ul>
<li>Placing the microphone under a single drip, so one sound dominates.</li>
<li>Recording without a windscreen, so the wind overwhelms the rain.</li>
<li>Letting splash hit the microphone directly.</li>
<li>Recording only briefly, and missing the changing intensity of the weather.</li>
<li>Setting the level by a quiet moment, then clipping on a heavy downpour.</li>
</ul>
<h2>A simple plan</h2>
<ol>
<li>Choose the surface or the water you want to capture.</li>
<li>Place the microphone sheltered and away from the splash line.</li>
<li>Use a windscreen, and set the level with a test.</li>
<li>Record for a long period, to capture the changes in intensity.</li>
<li>Label the file with the weather, the surface and the time.</li>
</ol>
<h2>Limits</h2>
<p>Weather is unpredictable, and a planned recording may be spoiled by a sudden gust or a change in the rain. Some storms are dangerous, and recording in them should never put you or your equipment at risk. Choose safe, sheltered positions, and accept that the weather decides the outcome.</p>
<h2>Keep the recording honest</h2>
<p>Rain and water recordings should sound natural, so keep cleanup minimal. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the windscreen and placement basics, read the <a href="/tunedzy/blog/field-recording-for-beginners">field recording post</a> in this series.</p>
''',
    faq=[('Which surface makes the best rain sound?', 'It depends on the mood. Leaves are soft, roofs are steady, and pavements are sharper.'),
         ('How do I stop the wind spoiling rain recordings?', 'Use a windscreen and shelter the microphone behind a wall or overhang.'),
         ('How long should I record rain?', 'Long enough to capture its changing intensity, often many minutes.'),
         ('Is it safe to record in a storm?', 'Only from a safe, sheltered position. Never put yourself or your equipment at risk.')])

add(slug='wildlife-recording-ethics', cluster='nature-sounds', kw='wildlife recording ethics',
    title='Wildlife Recording Ethics: Putting the Animals First',
    desc='Wildlife recording ethics: why animal welfare comes first, how to avoid disturbance, how to handle sensitive sites and how to be honest.',
    h1='Wildlife Recording Ethics: Putting the Animals First',
    answer='Wildlife recording ethics put the animals first. Avoid disturbing them, nests and sensitive habitats, do not use playback to attract them, and stop if your presence changes their behaviour. Be honest about how the recording was made, and check the rules for protected species and sites before you record or publish.',
    body='''
<p>Wildlife recording can produce some of the most extraordinary sounds in the natural world, but it carries a responsibility. An animal that is disturbed, frightened or displaced by a recordist has been harmed, even if the recording is excellent. The best recordists think about the animal first and the sound second, and they accept that some recordings are not worth the cost to the creature. This post sets out the principles that guide ethical wildlife recording.</p>
<p>It covers disturbance, playback, sensitive sites, honesty about the recording and the legal rules that may apply. It is general guidance, and local rules and protected species laws must always be checked.</p>
<h2>Disturbance comes first</h2>
<p>Disturbance is the most common harm caused by recordists. Approaching too close, moving suddenly, making noise or lingering near a nest can all frighten animals and change their behaviour. The principle is simple: if the animal changes what it is doing because of you, you are too close. Step back, wait, and accept a recording that does not include the animal.</p>
<p>Many birds and mammals are especially sensitive during breeding and when they are raising young. Keep a greater distance at these times, and avoid any site where a nest or a den may be present.</p>
<h2>Avoid playback</h2>
<p>Playing recordings of an animal’s calls to attract it is a common practice, but it can cause harm. It can stress the animal, draw it into dangerous places, or change how it behaves toward its own kind. Many recordists consider playback unacceptable in most situations. If you are considering it, check the rules and the impact first, and avoid it near sensitive species or during breeding.</p>
<h2>Sensitive sites and protected species</h2>
<p>Some species and sites are protected by law, and recording there may require permission or may be forbidden. Nature reserves, nesting colonies and rare species may have strict rules. Check the local regulations before you go, and respect any closure, path or notice. A recording made in a protected place without permission can cause legal trouble as well as harm.</p>
<h2>Respect the habitat</h2>
<p>Recording often involves walking, standing and sometimes disturbing vegetation. Stay on paths, avoid trampling plants and leave the place as you found it. Take your litter home, and avoid damaging the habitat to get a better position. The recording is less important than the health of the place it was made in.</p>
<h2>Be honest about the recording</h2>
<p>If a recording has been edited, combined from several sessions or made from playback, say so when you publish it. Listeners trust nature recordings because they are real, and a misleading presentation damages that trust. Label the place, the date and any edits, and avoid implying that a recording was captured in a way it was not.</p>
<h2>Know when to stop</h2>
<p>Stop recording if an animal is distressed, if a nest is threatened or if the environment is damaged. A recording is never worth an animal’s welfare. Accept that some sessions will produce nothing, and that the most ethical recordings are often the quietest.</p>
<h2>Protect sensitive locations in the notes</h2>
<p>Some species are at risk from collectors or disturbance, and publishing the exact location of a rare nest or a protected site can put it in danger. Consider leaving precise locations out of public notes, and keep the detail in private records. A general place name is often enough for listeners.</p>
<h2>Common mistakes</h2>
<ul>
<li>Getting closer to an animal to get a better recording.</li>
<li>Using playback to attract animals, especially rare or breeding ones.</li>
<li>Recording in protected places without checking the rules.</li>
<li>Presenting an edited recording as a single, unedited capture.</li>
<li>Publishing the exact location of a sensitive nest or rare species.</li>
</ul>
<h2>Limits</h2>
<p>Ethical guidance can differ between species, places and purposes, and it is not a substitute for local rules. Consult the relevant wildlife authority or a local expert when you are unsure. The principle that animals come first applies in every case.</p>
<h2>Keep the recording honest</h2>
<p>An ethical recording is also an honest one. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the practice of birdsong recording with care, read the <a href="/tunedzy/blog/how-to-record-birdsong">birdsong post</a> in this series.</p>
''',
    faq=[('Is playback acceptable?', 'Often not. It can stress animals, so avoid it, especially near breeding or rare species.'),
         ('What if the animal changes its behaviour?', 'Step back and wait. If you have changed what it is doing, you are too close.'),
         ('Do I need permission to record wildlife?', 'Sometimes, especially in protected places. Check the local rules before recording.'),
         ('Should I publish exact locations?', 'Not for sensitive or rare species. A general place name is often enough.')])

add(slug='recording-city-sounds', cluster='nature-sounds', kw='record city sounds',
    title='Recording City Sounds: Capturing Urban Life Responsibly',
    desc='Recording city sounds: choosing locations, managing traffic and crowds, placing the microphone, respecting people and the legal limits of public recording.',
    h1='Recording City Sounds: Capturing Urban Life Responsibly',
    answer='City sounds capture the life of a place: traffic, crowds, trams, markets and street performers. Record in public with care, choose quieter times when you can, place the microphone to balance the sounds, and respect people’s privacy. Check local rules on recording in public spaces before you publish anything identifiable.',
    body='''
<p>Cities have a sound of their own, made of traffic, footsteps, voices, machinery, trams, markets and music. A recording of a city can capture the energy of a place, the rhythm of a neighbourhood or the calm of a park in the middle of an urban whirl. Urban field recording is rich and challenging, because the sounds are dense and constantly changing, and the public nature of the work raises questions about privacy.</p>
<p>This post covers the choice of location and time, the microphone placement, the management of traffic and crowds, the respect for people and the legal limits that may apply to recording in public.</p>
<h2>Choose the location and the time</h2>
<p>Pick a place whose sound says something about the city: a market, a station, a quiet square, a canal or a busy junction. Visit at different times of day, since a street can sound very different at dawn, lunchtime and night. Early morning is often quieter, and a late evening can capture a different kind of life.</p>
<h2>Place the microphone</h2>
<p>Place the microphone where it can hear the sounds you want without being dominated by one source. A position on a quiet side street, under a canopy or in a sheltered doorway can balance the traffic with the voices. Test the position on headphones, and move slowly to find the balance you want.</p>
<h2>Manage the traffic</h2>
<p>Traffic is the constant background of most cities. You may not be able to remove it, so decide whether it is part of the sound you want. If it dominates, choose a quieter spot, record at quieter times, or accept it as a feature. A recording of a busy junction can be as honest as a recording of a park, as long as its character is clear.</p>
<h2>Handle the crowds</h2>
<p>Crowds create dense, shifting voices that can be beautiful and hard to control. Place the microphone away from the main flow, and let the crowd pass through the sound rather than standing in it. Recording a crowd from a small elevation can capture its shape better than standing at its edge.</p>
<h2>Set the level</h2>
<p>Cities can be loud, and sudden sounds such as sirens, brakes or shouts can overload a recording. Set the level with a test, leaving headroom for the loudest moments. Watch the peak meter during the first minutes, and adjust if needed.</p>
<h2>Respect people and privacy</h2>
<p>Recording in public is often allowed, but people have a right to privacy, and some recordings can identify individuals. Avoid capturing identifiable people in a way that could harm them, and avoid private conversations. If you plan to publish a recording, consider whether any person can be identified, and whether you need permission.</p>
<h2>Know the local rules</h2>
<p>The rules on recording in public places differ between countries and between cities. Some places restrict recording in certain buildings, stations or events, and some have rules about commercial use. Check the rules where you are, and take advice before publishing any recording that is likely to be used commercially.</p>
<h2>Common mistakes</h2>
<ul>
<li>Recording only at the busiest time, and missing the quieter character of the place.</li>
<li>Placing the microphone in the middle of a crowd, so the voices become a blur.</li>
<li>Capturing identifiable people in ways that could harm them.</li>
<li>Setting the level by a quiet moment, then clipping on a siren or a shout.</li>
<li>Assuming public recording is free of all rules.</li>
</ul>
<h2>A simple plan</h2>
<ol>
<li>Choose a location with a clear sound and visit it at two times.</li>
<li>Test the microphone position, and set the level.</li>
<li>Record for at least twenty minutes, and note the time and place.</li>
<li>Avoid identifiable people, and check the rules before publishing.</li>
<li>Label the file with the location, the time and the main sounds.</li>
</ol>
<h2>Limits</h2>
<p>City recordings are unpredictable, and a sudden event can spoil a take or raise a question. Expect some sessions to produce little, and treat each one as practice in listening. The aim is to capture the city honestly and respectfully.</p>
<h2>Clean lightly</h2>
<p>City recordings are often busy, and cleanup should keep the character of the place. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the general approach to outdoor sound, read the <a href="/tunedzy/blog/field-recording-for-beginners">field recording post</a> in this series.</p>
''',
    faq=[('When is the best time to record a city?', 'Early morning is often quieter. Visit at several times to hear the change.'),
         ('Can I record people in public?', 'Often, but avoid identifiable people in ways that could harm them, and check the local rules.'),
         ('How do I handle heavy traffic?', 'Choose a quieter spot, record at quieter times, or accept traffic as part of the character.'),
         ('Do I need permission to publish?', 'It depends on the people and the place. Check the rules, and take advice for commercial use.')])

add(slug='recording-outdoors-in-cold-weather', cluster='nature-sounds', kw='record outdoors cold weather',
    title='Recording Outdoors in Cold Weather: Protecting Gear and Hands',
    desc='Recording outdoors in cold weather: protecting batteries and storage, keeping your hands warm for handling, managing condensation and recording reliably.',
    h1='Recording Outdoors in Cold Weather: Protecting Gear and Hands',
    answer='Cold weather affects batteries, screens, cables and your own handling, and it can make recordings unreliable. Keep batteries warm, carry spares, protect the recorder from condensation when you move indoors, and use gloves that still let you operate the controls. Plan shorter sessions with breaks, and check the recording at intervals.',
    body='''
<p>Winter brings some of the most distinctive outdoor sounds: snow underfoot, frozen water, still air and the crack of ice. Recording in cold weather is rewarding, but it is harder on equipment and on the person holding it. Batteries drain faster, condensation can form when you move between cold and warm places, and gloves make controls hard to use. With a little preparation, cold-weather recording can be reliable and enjoyable.</p>
<p>This post covers the effects of cold on the gear and the recordist, how to protect the batteries, storage and recorder, and how to plan sessions that are comfortable and productive.</p>
<h2>How cold affects equipment</h2>
<p>Cold reduces battery capacity, sometimes sharply, so a battery that lasts for hours in summer may last much less in freezing conditions. Screens can slow or fail to respond, and some plastics and cables become brittle. Storage cards and electronics can also be affected by sudden temperature changes. Test the equipment in the conditions you expect before a long session.</p>
<h2>Keep batteries warm</h2>
<p>Keep spare batteries inside a warm pocket, close to your body, until you need them. A battery that has become cold will often recover some capacity when warmed. Carry more batteries than you think you need, and rotate them so one is always warm. A power bank can also help if the recorder supports charging from one.</p>
<h2>Handle condensation</h2>
<p>Condensation forms when cold equipment moves into a warm room, or when warm breath meets cold metal. It can damage electronics and fog the microphone. When you come indoors, seal the recorder in a bag and let it warm slowly before opening it. Check for moisture on the microphone and the connections before the next session.</p>
<h2>Keep your hands working</h2>
<p>Gloves make it hard to operate small controls. Choose thin gloves with fingertips that let you press buttons, or keep a pair of fingerless gloves for the controls. Set the recording level and the settings before you put on heavy gloves, so you do not need to adjust them in the cold. Keep a spare pair of dry gloves for breaks.</p>
<h2>Plan shorter sessions</h2>
<p>Cold tires people quickly, and tired hands make mistakes. Plan shorter sessions with breaks in a warm place, and check the recording at each break. A few minutes of warmth can make the next session much more productive, and it gives you a chance to check the battery and the level.</p>
<h2>Protect the microphone from wind</h2>
<p>Wind feels much colder, and it is also the main enemy of outdoor recordings. Use a windscreen, and shelter the microphone behind a wall, a hedge or your own body. A foam windscreen can be ineffective if it is frozen or wet, so keep it dry and check it before each session.</p>
<h2>Common mistakes</h2>
<ul>
<li>Running out of battery partway through a session.</li>
<li>Bringing cold equipment indoors without letting it warm slowly.</li>
<li>Wearing gloves that make the controls impossible to use.</li>
<li>Recording for too long without a break, and losing focus.</li>
<li>Forgetting that a wet or frozen windscreen will not protect the microphone.</li>
</ul>
<h2>A cold-weather checklist</h2>
<ol>
<li>Test the recorder and batteries in the expected temperature.</li>
<li>Carry spare batteries, kept warm close to the body.</li>
<li>Set the level and the settings before putting on heavy gloves.</li>
<li>Protect the recorder from condensation when you come indoors.</li>
<li>Plan breaks, and check the recording at each one.</li>
</ol>
<h2>Limits</h2>
<p>Extreme cold can damage equipment, and some recorders are not rated for low temperatures. Check the manufacturer’s operating range, and do not push equipment beyond it. Safety comes first: never stay out in dangerous conditions for the sake of a recording.</p>
<h2>Keep the recording reliable</h2>
<p>A reliable recording depends on preparation. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the wind side of the work, read the <a href="/tunedzy/blog/how-to-remove-wind-noise-from-a-recording">wind noise post</a> in this series.</p>
''',
    faq=[('Why does my battery die quickly in the cold?', 'Cold reduces battery capacity. Keep spares warm and carry more than you need.'),
         ('How do I avoid condensation?', 'Seal the recorder in a bag and let it warm slowly before opening it indoors.'),
         ('What gloves should I use?', 'Thin gloves with fingertips that let you operate the controls, or fingerless gloves for the settings.'),
         ('Can I record in freezing conditions?', 'Often yes, within the recorder’s rated range. Keep sessions shorter and check the equipment.')])

add(slug='field-recorder-battery-and-storage', cluster='nature-sounds', kw='field recorder battery life',
    title='Field Recorder Battery Life and Storage: Planning Long Sessions',
    desc='Field recorder battery life and storage: estimating power and space for long sessions, carrying spares, managing files and avoiding running out mid-recording.',
    h1='Field Recorder Battery Life and Storage: Planning Long Sessions',
    answer='Field recording sessions can fail through a flat battery or a full card as easily as through bad sound. Estimate the power and storage for each session, carry spares, format cards before the session and check the level of both at intervals. A simple plan prevents losing the best moment to a practical problem.',
    body='''
<p>The best field recording is worthless if the battery dies at the moment a bird begins to sing, or the card fills up as the rain reaches its peak. Power and storage are the practical limits of every session, and they are easy to forget when the excitement of the location takes over. A few minutes of planning, done before leaving home, prevents most of these problems.</p>
<p>This post explains how to estimate power and storage, how to carry spares, how to manage files on location and how to check the equipment during a long session.</p>
<h2>Estimate the power</h2>
<p>Battery life depends on the recorder, the settings, the phantom power, the display and the temperature. Check the manufacturer’s figure, but treat it as a best case. Test the battery life with your own settings, for a session of the length you plan. Record the result, so you can plan future sessions more accurately.</p>
<h2>Carry spares</h2>
<p>Carry at least one spare battery or a power bank, and charge everything fully the night before. A spare that is charged and ready is the simplest insurance against a dead recorder. If your recorder runs on removable batteries, carry fresh ones, and keep the spares in a case that protects their contacts.</p>
<h2>Estimate the storage</h2>
<p>Storage depends on the format, the sample rate and the length of the session. A high-quality format at a high sample rate fills cards quickly, and a long session can need several gigabytes. Calculate the space you need before the session, and carry more cards than you think you will use. Cards are cheap compared with a lost recording.</p>
<h2>Format the cards before the session</h2>
<p>Format each card in the recorder before the session, not on a computer, so the file system matches the device. Check that each card is empty and works. Keep a list of which card has which session, and label the cards clearly so they are never confused.</p>
<h2>Manage files on location</h2>
<p>Name files as you go, with the date, the time and the place. Create a new file for each take or each segment, so a fault affects only one file. Check the files during breaks, playing a short section to confirm that the recording is working. A file that has silently failed is the worst surprise to discover at home.</p>
<h2>Check during the session</h2>
<p>Check the battery and the storage at regular intervals, and watch the level indicator for any sign of trouble. A recorder that shows a warning may be about to stop, so act on it. Keep the device warm, as cold drains batteries, and turn off any display or function you do not need to save power.</p>
<h2>Common mistakes</h2>
<ul>
<li>Starting a long session with a partly charged battery.</li>
<li>Carrying only one card, which fills before the session ends.</li>
<li>Formatting cards on a computer rather than in the recorder.</li>
<li>Recording one enormous file, so a fault affects everything.</li>
<li>Never checking the recording until it is time to edit.</li>
</ul>
<h2>A session checklist</h2>
<ol>
<li>Charge all batteries and power banks the night before.</li>
<li>Format the cards in the recorder, and label them.</li>
<li>Estimate the power and storage for the session length.</li>
<li>Name files as you go, and check them at breaks.</li>
<li>Keep the device warm, and watch for warnings.</li>
</ol>
<h2>Limits</h2>
<p>Battery and storage estimates are approximate, and conditions vary. Plan with a margin, and accept that a long session may need an extra battery or card. The aim is to prevent avoidable failures, not to remove every risk.</p>
<h2>Keep the files safe</h2>
<p>Once a session is done, back up the files as soon as possible. The <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup post</a> in this series explains the routine, and the <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean a recording you own. For the planning side of field work, read the <a href="/tunedzy/blog/field-recording-for-beginners">field recording post</a>.</p>
''',
    faq=[('How many batteries should I carry?', 'At least one spare or a power bank, charged and ready, for any long session.'),
         ('How much storage do I need?', 'Calculate from the format, sample rate and length, then carry more cards than you expect to use.'),
         ('Should I format on a computer?', 'Better not. Format the cards in the recorder so the file system matches the device.'),
         ('Why use several files?', 'A fault affects only one file, not the whole session, so the rest of the recording survives.')])

add(slug='labelling-field-recordings', cluster='nature-sounds', kw='label field recordings',
    title='Labelling Field Recordings: A System That Keeps Your Archive Useful',
    desc='Labelling field recordings: a naming system with date, place and content, the metadata worth keeping and how to avoid losing track of an archive over time.',
    h1='Labelling Field Recordings: A System That Keeps Your Archive Useful',
    answer='A field recording archive is only useful if you can find what you need. Use a consistent naming pattern with the date, the place and the content, keep the metadata that matters, such as conditions and equipment, and store notes alongside the files. A simple system, applied every time, keeps an archive usable for years.',
    body='''
<p>Field recording produces a lot of files, and they quickly become impossible to use if they are not labelled. A file called recording_0042 tells you nothing six months later. A good label tells you what the sound is, where it was recorded, when, and under what conditions. A consistent system turns a pile of recordings into a library that can be searched and reused, and it is one of the most valuable habits a recordist can build.</p>
<p>This post sets out a naming system, the metadata worth keeping, how to store notes and how to keep the archive usable over time.</p>
<h2>Why labels matter</h2>
<p>Labels make recordings findable. When you need a particular sound for a project, a good label lets you find it in seconds rather than hours. Labels also protect the value of the work: a recording whose origin is unknown is harder to trust and harder to use, while a well-labelled one carries its context with it.</p>
<h2>A naming pattern</h2>
<p>Use a consistent pattern for every file, such as date, place, content and take number. For example, 2026-10-25_harbour_gulls_take02. Put the date first, so files sort in order, and avoid spaces and symbols. Keep the same pattern across all recordings, so the archive looks and behaves consistently.</p>
<h2>What metadata to keep</h2>
<p>Beyond the name, keep the details that help you use the sound later: the exact place, the time, the weather, the equipment and the settings, the microphone position and the distance. Note any species, people or events in the recording, and any permission or licence. Store this information in a text file or in the file’s metadata fields, if your recorder or software supports them.</p>
<h2>Keep notes beside the files</h2>
<p>A simple notes file for each session is one of the most useful records. Write down the place, the conditions, what you heard and what you intended. The note is much easier to write on the day than to reconstruct later, so make it part of the routine at the end of each session.</p>
<h2>Use folders carefully</h2>
<p>Folders help, but they can become a maze. A simple structure, such as one folder per location and one subfolder per date, works well for most people. Avoid deep nesting, which makes files hard to find. Keep the folder names consistent with the file names, so both can be searched.</p>
<h2>Keep the archive usable over time</h2>
<p>Review the archive every few months. Check that the names are consistent, that the notes match the files and that the backups are working. Fix any file that has lost its label, and add the missing details while you still remember them. An archive that is maintained stays useful for years.</p>
<h2>Common mistakes</h2>
<ul>
<li>Leaving the camera or recorder’s default file names in place.</li>
<li>Labelling only the date, so the place and content are lost.</li>
<li>Failing to write the notes at the end of each session.</li>
<li>Using inconsistent patterns, so searching becomes unreliable.</li>
<li>Letting the archive grow without review.</li>
</ul>
<h2>A simple routine</h2>
<ol>
<li>Rename every file with the date, place, content and take number.</li>
<li>Write a short session note with the conditions and the intent.</li>
<li>Record permissions and licences in the note.</li>
<li>Store the files and notes in a simple folder structure.</li>
<li>Review the archive every few months, and fix any gaps.</li>
</ol>
<h2>Limits</h2>
<p>A labelling system is only as good as its consistency. The best system is one you will actually use, so keep it simple enough to apply every time. Adjust the pattern if you find it awkward, but change it early, before the archive grows too large to rename.</p>
<h2>Keep the archive safe</h2>
<p>An archive is only useful if it survives. The <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup post</a> in this series sets out the routine, and the <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean a recording you own. For the field side of the work, read the <a href="/tunedzy/blog/field-recording-for-beginners">field recording post</a> in this series.</p>
''',
    faq=[('What should a file name include?', 'The date, the place, the content and the take number, in a consistent pattern.'),
         ('Why keep notes if the file is labelled?', 'Notes hold the conditions, the intent and any permission, which a file name cannot.'),
         ('How often should I review the archive?', 'Every few months, to fix gaps and check that the notes match the files.'),
         ('Should I use folders or file names?', 'Both, with a simple folder structure and consistent names, so either can be searched.')])

add(slug='building-a-sound-library', cluster='nature-sounds', kw='build a sound library',
    title='Building a Personal Sound Library From Your Recordings',
    desc='Building a personal sound library from your recordings: choosing what to keep, organising for search, licensing your own material and growing the library over time.',
    h1='Building a Personal Sound Library From Your Recordings',
    answer='A personal sound library grows from the recordings you make and keep. Choose which sounds to keep based on their quality and usefulness, organise them for fast search, label them clearly, record the rights you hold and grow the library steadily. A well-kept library saves time on every project and becomes a distinctive asset.',
    body='''
<p>A personal sound library is a collection of sounds that you have recorded, organised and kept for future use. Over time it becomes one of the most valuable things a creator owns: a source of sounds that no one else has, that suits your style and that you can use without searching for licences. Building one takes steady effort, but the rewards grow with every project.</p>
<p>This post covers how to choose what to keep, how to organise the library for search, how to record the rights you hold, and how to grow the library without letting it become a clutter.</p>
<h2>Why build a library</h2>
<p>A library saves time, because the sound you need may already exist. It gives your work a consistent character, since you draw from the same palette. It also simplifies rights, because the sounds are your own recordings. A library is a long-term investment, and it grows more useful as you use it.</p>
<h2>Choose what to keep</h2>
<p>Not every recording deserves a place in the library. Keep the sounds that are clean, distinctive and likely to be useful. A recording that is noisy, unclear or very similar to one you already have can be discarded. Be selective, because a library full of weak sounds is harder to search than a smaller, strong one.</p>
<p>Listen to each candidate on headphones and on a phone, and ask whether you would use it in a project. If the answer is no, let it go.</p>
<h2>Organise for search</h2>
<p>Organise the library so you can find a sound in seconds. Use folders by type, such as movement, water, voices and environments, and consistent names within them. Tag each sound with keywords, so you can search by feeling or use, such as calm, sharp or distant. A library that cannot be searched is a library that will not be used.</p>
<h2>Record the rights you hold</h2>
<p>For each sound, record that you made it, the date and the conditions. If the sound includes a person, a place or a trademark, note any permissions and any restrictions. This record protects you when you use the sound publicly, and it makes the library safe to share with collaborators.</p>
<p>The rights question is simpler for your own recordings than for purchased sounds, but the people and places in them still matter. The <a href="/tunedzy/blog/sound-effects-licences-explained">licences post</a> explains the wider context.</p>
<h2>Grow it steadily</h2>
<p>Add sounds regularly, perhaps once a month, rather than in large batches. Each new sound should fill a gap in the library or add a useful variation. Review the library every few months, removing duplicates and weak sounds, and adding notes where they are missing.</p>
<h2>Share with care</h2>
<p>A library can be useful to collaborators, but sharing it needs care. Share only the sounds you have the right to share, and keep the rights notes with the files. Consider sharing a selected set rather than the whole library, and check any permissions before sending a recording that includes people or places.</p>
<h2>Common mistakes</h2>
<ul>
<li>Keeping every recording, so the library becomes cluttered.</li>
<li>Failing to tag sounds, so they cannot be found by feeling or use.</li>
<li>Adding sounds in large batches, without review.</li>
<li>Forgetting the rights notes for sounds that include people or places.</li>
<li>Sharing the whole library without checking the rights.</li>
</ul>
<h2>A simple structure</h2>
<ol>
<li>Create folders by type, such as movement, water, voices and environments.</li>
<li>Name each file with a consistent pattern, including the date and content.</li>
<li>Tag each sound with two or three keywords describing its character.</li>
<li>Record the rights and conditions in a note for each sound.</li>
<li>Review the library every few months, and remove the weak sounds.</li>
</ol>
<h2>Limits</h2>
<p>A personal library will be smaller and more specific than a commercial one, and that is part of its value. It will not contain every sound you might need, and some sounds will still need to be bought or licensed. Use the library for what it does well, and fill the gaps with care.</p>
<h2>Keep the library clean at the source</h2>
<p>A library is only as good as its recordings. The <a href="/tunedzy/tools/voice-recorder-noise-cancellation">Noise-Free Voice Recorder</a> can clean background noise from a recording you own, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning phone recordings. For the naming habit that keeps a library usable, read the <a href="/tunedzy/blog/labelling-field-recordings">labelling post</a> in this series.</p>
''',
    faq=[('How many sounds should a library have?', 'As many as you will use well. A smaller, strong library is more useful than a large, weak one.'),
         ('How do I find a sound quickly?', 'Use folders by type, consistent names and two or three keyword tags for character.'),
         ('Can I share my library?', 'Share only what you have the right to share, and keep the rights notes with the files.'),
         ('How often should I add sounds?', 'Regularly, perhaps monthly, each one filling a gap or adding a useful variation.')])
