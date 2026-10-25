"""Blog posts, batch 13 of 20: voice rights, consent and deepfake labels. Merged into content_blog.py.
Legal points are attributed to named analyses or official texts and are general guidance, not legal advice.
Where a date or rule was reported but not confirmed in the primary text, the post says so and points to the source.
No invented statistics. Funnel: each post ends with a link to Tunedzy Go and to the matching free tool."""

CLUSTERS = {
    'trend-voice-law': dict(tool='vocal-checker', label='Voice rights, consent and deepfake labels', tool_name='Vocal Checker'),
}

BLOGS = []


def add(**kw):
    BLOGS.append(kw)


add(slug='voice-cloning-laws-2026-overview', cluster='trend-voice-law', kw='voice cloning law 2026',
    title='Voice Cloning Laws in 2026: A Plain Overview for Creators',
    desc='Voice cloning laws in 2026 in plain words: what is changing in the UK, the US and the EU, why consent matters and what creators should check first.',
    h1='Voice Cloning Laws in 2026: A Plain Overview for Creators',
    answer='Voice cloning is covered by a patchwork of rules in 2026, not one clear law. Commentators in the UK say existing protections are not designed for AI cloning, US action has focused on fraud, and the EU is moving toward labelling requirements. Creators should get written consent and disclose any generated voice.',
    body='''
<p>Voice cloning has moved from a technical curiosity to a common production tool, and the law has been catching up unevenly. A creator who makes a podcast, a video or an audiobook may now be asked to use a generated voice, or to clone their own, or to work alongside someone whose voice has been copied. The rules that apply depend on where the speaker and the audience are, and they are changing.</p>
<p>This overview is written for creators, not lawyers. It explains the main threads of current debate, names the sources behind each claim, and gives practical steps. It is general guidance and not legal advice. For any real decision, check the official text and speak to a professional.</p>
<h2>What counts as voice cloning</h2>
<p>Voice cloning uses a model to produce new speech that sounds like a specific person, from samples of that person&rsquo;s voice. It is different from noise removal, which reduces what was already recorded. A cleaned recording is still the speaker saying what they said. A cloned voice can say things the speaker never said, which is why the legal questions are different.</p>
<p>The line can blur in practice. Some tools change a voice in subtle ways, such as altering the tone or the accent, and some generate speech from a short sample. Creators should ask what a tool actually does before using it, rather than relying on a label.</p>
<h2>The United Kingdom: a gap, according to commentators</h2>
<p>A July 2026 analysis from the law firm CMS, published after a news report in June raised concern, argues that UK law does not clearly protect people from unauthorised AI cloning of their voice. The analysis says the current legislation predates the technology, and that existing protection comes from several separate areas, such as copyright, data protection, trademarks and passing off. None of those was designed with AI cloning in mind, and the analysis describes no general right to own one&rsquo;s voice.</p>
<p>This is a commentary on the law, not the final word. Check the current position on the legislation website, and take advice on a specific case.</p>
<h2>The United States: fraud and calls first</h2>
<p>Federal activity in the United States has focused mainly on fraud and unwanted calls. Reports describe the Federal Trade Commission preparing to enforce parts of a new law against sexual deepfakes, and looking at ways to curb scams that use cloned voices. The Federal Communications Commission has rules on caller identification that followed a robocall which used a cloned voice of a politician.</p>
<p>Beyond federal action, state approaches vary, and some state laws touch on personal or biometric data, which can include voice. The detail varies from state to state, and some claims in circulation come from vendor blogs that could not be checked against primary texts. For the status of any specific law, check the official government site for that state or agency.</p>
<h2>The European Union: labelling is the main duty</h2>
<p>The EU AI Act sets transparency duties for AI-generated content. Reports and the Commission&rsquo;s draft guidance describe a duty to label deepfakes, which are content that resembles real people, objects, places or events and could falsely appear authentic. Several sources say these duties began to apply on 2 August 2026, subject to some transitional relief for technical marking. The final guidance and the relief should be checked in the official text, because the reports do not all agree.</p>
<p>The practical point is that a label must be visible or audible, and it must appear at the latest on first exposure. A creator who publishes a generated voice in the EU should plan for a clear disclosure from the start, rather than adding one later.</p>
<h2>Consent comes first everywhere</h2>
<p>Across all these systems, the strongest protection a creator can give is consent. Agree in writing, before any cloning begins, what the voice will be used for, where it will appear, how long it will be kept and whether it can be changed or withdrawn. A clear agreement protects the speaker and the creator, and it makes a later dispute much easier to resolve.</p>
<p>Consent should be specific. A general line that the speaker agrees to &ldquo;any use&rdquo; is weak. A list of the intended uses, with a clear limit on anything else, is much stronger.</p>
<h2>Practical steps for creators</h2>
<ol>
<li>Get written consent before recording or generating any voice, and keep a copy with the project files.</li>
<li>Label any generated or altered voice clearly in the episode, description or on screen.</li>
<li>Keep the raw recordings and the consent note together, so you can show them later.</li>
<li>Check the terms of any voice tool, including what it does with your audio.</li>
<li>Read the official text of the law where your audience is, not only summaries.</li>
</ol>
<h2>What to watch next</h2>
<p>Expect more guidance and more legislation over the next year. The areas most likely to change are labelling rules, consent standards for generated voices and the enforcement of fraud laws. Keep a note of the sources you rely on, and check them again before each major project, because the position may have moved.</p>
<h2>Limits</h2>
<p>This post draws on commentary, reports and vendor material, and some of those sources disagree or could not be checked against the primary text. It is not a statement of the law in any country. Treat it as a map of the debate, and verify each point before you act on it.</p>
<h2>Keep your recording clean and honest</h2>
<p>Even a real recording deserves a careful check before publishing. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the labelling side of the same issue, read the <a href="/tunedzy/blog/eu-ai-act-deepfake-labels-explained">EU labelling post</a> and the <a href="/tunedzy/blog/how-to-label-ai-generated-voice-in-content">labelling guide</a> in this series.</p>
''',
    faq=[('Is voice cloning illegal?', 'Not in every case. It depends on consent, use and location. Check the rules for where the speaker and the audience are.'),
         ('Do I need consent to clone my own voice?', 'It is your voice, but a clear record of what it will be used for is still sensible, and labelling is expected.'),
         ('Where can I find the current law?', 'On official legislation and regulator websites. Summaries from vendors may be out of date.'),
         ('What is the first step for a creator?', 'Get written consent, keep the raw files, and label any generated voice clearly.')])

add(slug='eu-ai-act-deepfake-labels-explained', cluster='trend-voice-law', kw='eu ai act deepfake label',
    title='EU AI Act Deepfake Labels Explained for Podcasters and Video Makers',
    desc='The EU AI Act deepfake labels explained for podcasters and video makers: what must be labelled, when, how, and what the reports say about timing.',
    h1='EU AI Act Deepfake Labels Explained for Podcasters and Video Makers',
    answer='The EU AI Act requires people who publish AI-generated deepfakes to disclose them, with a visible or audible label at the latest on first exposure. Reports say these transparency duties began on 2 August 2026, with some transitional relief. Check the official Regulation and the final Commission guidance before relying on any detail.',
    body='''
<p>For podcasters and video makers in Europe, one of the most practical parts of the EU AI Act is the transparency rule for deepfakes. It asks people who publish synthetic content that resembles real people, objects, places or events to tell their audience. The rule is simple to state and easy to get wrong in practice, so it is worth reading the details carefully.</p>
<p>This post explains what the rule asks for, what has been reported about its timing, and how a creator can prepare. It draws on the Regulation, on the Commission&rsquo;s draft guidance and on commentary from several firms. Where those sources disagree, the post says so. It is general guidance, not legal advice.</p>
<h2>What counts as a deepfake</h2>
<p>The Act describes a deepfake as AI-generated or manipulated content that resembles existing people, objects, places, entities or events and could falsely appear authentic. A cloned voice that sounds like a real person saying something they did not say falls within that description. A clearly fantastical scene, such as a dragon or a person flying unaided, is reported to fall outside it, because it cannot be mistaken for real.</p>
<p>The test is whether the content could falsely appear authentic. That makes the question about the audience as well as the content. A voice that listeners would reasonably take as real is the risk the rule addresses.</p>
<h2>Who has the duty</h2>
<p>Commentary on the Act says the duty to disclose sits mainly with the deployer: the person or organisation that publishes the synthetic content. A podcaster who uses a generated voice in an episode, or a video maker who publishes a synthetic presenter, is likely to be the deployer. Providers of generative tools have separate duties, including making outputs detectable where technically feasible.</p>
<p>That split matters. A tool that adds a machine-readable mark does not, on the reports, replace the visible or audible label the creator must add.</p>
<h2>How the label must work</h2>
<p>According to a summary of the Commission&rsquo;s FAQ, the label must be visible or audible, and it must appear at the latest on first exposure. A machine-readable mark added by a provider does not satisfy that duty on its own. For a podcast, that suggests a spoken disclosure near the start of the episode, and a written note in the description. For a video, it suggests an on-screen label as well.</p>
<p>The label should be clear, not buried. A disclosure hidden in a long description will not meet the test of appearing at the latest on first exposure, because the listener may never read it.</p>
<h2>Artistic and satirical work</h2>
<p>Reports describe lighter treatment for artistic and satirical works, where the disclosure must fit the work without hampering its display or enjoyment. That is a narrower exception than many creators assume, and it does not remove the need for a disclosure. If you are relying on it, take advice on whether your work qualifies.</p>
<h2>What the timing reports say</h2>
<p>Several sources say the transparency obligations began to apply on 2 August 2026. Some of them mention targeted transitional relief for the marking and detection duties on providers, which was contemplated in an omnibus proposal. Whether that relief was adopted, and how it changes the timeline, is not settled in the sources reviewed. The Commission&rsquo;s draft guidance was published in May 2026, with a final version expected before the August date, but the final text was not confirmed in those sources.</p>
<p>Because these reports do not agree in every detail, check the Regulation itself and the Commission&rsquo;s final guidance before making any plan that depends on a date.</p>
<h2>Preparing your content</h2>
<ol>
<li>Decide whether any generated or altered voice or image could be taken as real.</li>
<li>Plan a visible or audible label for every such item, placed at the start of the content.</li>
<li>Write the disclosure into your production checklist, so it is never forgotten.</li>
<li>Keep records of the tools used and the consent obtained for any voice.</li>
<li>Check the final guidance for your sector and your country, and revisit your plan when it changes.</li>
</ol>
<h2>Check the official text for your situation</h2>
<p>A summary can tell you the general shape of a rule, but it cannot tell you how it applies to your show, your country or your audience. Read the Regulation itself, and then the Commission&rsquo;s final guidance for your sector. Note the version and the date you read them, because guidance can be revised. If your work involves a commercial deal or a public body, take advice from a professional who knows EU law.</p>
<p>Keep a short file of the sources you used and when you checked them. If a dispute arises later, a dated record of your reading shows that you made a reasonable effort to follow the rule.</p>
<h2>Limits</h2>
<p>This post relies on the Regulation as summarised in several sources and on the draft guidance. Some sources are blogs and vendor pages, and at least one describes its article numbering inconsistently with the others. Treat the summary as a starting point, and verify it against the official text before you rely on it.</p>
<h2>Protect your audio and your audience</h2>
<p>A disclosure protects trust, and the audio decides whether a listener stays. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the wider picture of voice rights, read the <a href="/tunedzy/blog/voice-cloning-laws-2026-overview">overview of voice cloning laws</a> in this series.</p>
''',
    faq=[('Does the rule apply to every AI voice?', 'Not every one. It applies to synthetic content that could falsely appear authentic. Check the definition in the Regulation.'),
         ('Is a machine-readable mark enough?', 'Reports say no. The label must be visible or audible for the audience.'),
         ('When did it start?', 'Several reports say 2 August 2026, with some transitional relief. Check the official text, because sources differ.'),
         ('Does it apply outside the EU?', 'It depends on where the content is published and reaches people. Check the scope in the Regulation for your situation.')])

add(slug='how-to-label-ai-generated-voice-in-content', cluster='trend-voice-law', kw='how to label ai voice',
    title='How to Label an AI-Generated Voice in Your Content',
    desc='How to label an AI-generated voice in your content: where to put the disclosure, what words to use, how to avoid a hidden label and how to keep it consistent.',
    h1='How to Label an AI-Generated Voice in Your Content',
    answer='Label an AI-generated voice early and plainly: a spoken line near the start, a written note in the description, and an on-screen caption for video. Use simple words that say what was generated, and keep the same label in every episode where the voice appears.',
    body='''
<p>Audiences are increasingly aware that voices can be generated, and many feel misled when they find out later. A clear label builds trust and, in some places, is required by law. The practical question for a creator is how to label well: where to put the disclosure, what to say, and how to keep it consistent without making the content feel like a warning label.</p>
<p>This guide covers the choices in order. It assumes the label is needed, and focuses on making it clear and honest without damaging the listening or viewing experience.</p>
<h2>Decide what needs a label</h2>
<p>Not every use of software changes the meaning of a voice. Cleaning background noise, levelling a recording or cutting a pause does not generally make the speech synthetic. A generated voice, a cloned voice, or a voice that has been changed to sound like someone else does. When in doubt, label. A short note costs little and a complaint costs much more.</p>
<p>Write down the rule you use, so the whole team applies it the same way. A simple rule, such as labelling any speech that was not spoken by the person shown or named, covers most cases.</p>
<h2>Put the label at the start</h2>
<p>A label at the very end of an episode is easy to miss, and a viewer or listener may stop before reaching it. Place a spoken or on-screen label near the beginning, before the first generated line. For a podcast, a short sentence after the intro works well. For a video, a caption that appears as the voice begins is clear.</p>
<p>Repeat the label if the generated voice returns in a later section, especially after a long gap. Listeners who join partway through should not miss it.</p>
<h2>Choose plain words</h2>
<p>Use words that say exactly what happened. &ldquo;The narration in this episode was generated by an AI voice model, based on a recording of the host&rdquo; is clear. &ldquo;Enhanced audio&rdquo; is vague and may mislead. Avoid technical jargon, and do not use a phrase that suggests the voice is real if it is not.</p>
<p>Where the voice is cloned from a real person, say so, and say whether that person agreed. That detail protects both the speaker and the audience.</p>
<h2>Add the note in the description</h2>
<p>A written note in the episode description or the video description is a useful second layer. It gives listeners a place to check details, and it helps search and transcripts record the disclosure. The written note should not replace the spoken or on-screen label, because many people will never read the description.</p>
<p>Keep the wording identical across episodes, so listeners learn to recognise it and trust it.</p>
<h2>Handle captions and transcripts</h2>
<p>If you publish a transcript or captions, make sure the label appears there too. Automatic captions may not mark the generated voice, so add the note by hand. A transcript that hides the label undermines the disclosure, even when the audio includes it.</p>
<p>Check the captions against the audio, since an error in a name can make a disclosure less clear.</p>
<h2>Keep the label consistent across formats</h2>
<p>A label used in an audio episode should match the label used in a video, a clip and a social post. If a clip is cut from an episode, the clip needs its own label, because the viewer may never hear the episode. Plan the label into every format from the start, rather than adding it at the end of the process.</p>
<h2>Review the label every season</h2>
<p>Check whether the label still matches what you do. If you change the tool, the voice or the way it is used, update the wording and the placement. Note the date of each change, so you can show when the disclosure began and what it said.</p>
<h2>Test the label with a listener</h2>
<p>Before you publish a series with a new label, ask someone who has not heard the episode to play it and tell you what they understood. If they miss the disclosure, or think the voice is real, the label is not clear enough. A short test catches the problem before it reaches the whole audience.</p>
<p>Test the label on a phone speaker as well. A line that is easy to read on a laptop can be hard to hear on a small speaker in a noisy room.</p>
<h2>Limits</h2>
<p>A label does not make a misleading use acceptable, and it does not replace consent. Some uses may be prohibited whatever the disclosure says, so check the rules that apply. This guide is general practice, not legal advice, and it does not describe any specific legal requirement in full.</p>
<h2>Keep your human recordings clear too</h2>
<p>Real voices need clean recordings just as much. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording in your browser. For the rules that may require the label in the EU, read the <a href="/tunedzy/blog/eu-ai-act-deepfake-labels-explained">EU labelling post</a> in this series.</p>
''',
    faq=[('Where should the label go?', 'Near the start, before the first generated line, and repeated if the voice returns after a gap.'),
         ('Is a description note enough?', 'No. Many listeners never read it. Use a spoken or on-screen label as well.'),
         ('What words should I use?', 'Plain words that say what was generated and, if relevant, whose voice it is based on.'),
         ('Do I need to label clean recordings?', 'No. Noise removal and levelling do not make the speech synthetic.')])

add(slug='uk-voice-rights-gap-what-it-means', cluster='trend-voice-law', kw='uk voice cloning law',
    title='The UK Voice Rights Gap: What Commentators Say It Means',
    desc='The UK voice rights gap explained: what a July 2026 analysis says about AI cloning, which protections apply today and what creators should do meanwhile.',
    h1='The UK Voice Rights Gap: What Commentators Say It Means',
    answer='A July 2026 analysis by the law firm CMS argues that UK law does not clearly protect people from unauthorised AI cloning of their voice. The protections that exist come from several areas not designed for the purpose. Creators in the UK should use written consent and label generated voices while the law is unsettled.',
    body='''
<p>In June 2026, a news report raised concern that UK law does not protect people from unauthorised AI cloning of their voice or face. A July 2026 analysis from the law firm CMS took up the question and concluded that the existing legislation predates the technology and is not clearly fit for the purpose. This post explains what that analysis says, what it does not say, and what a UK creator can do while the position is debated.</p>
<p>The post relies on the commentary and on the report it describes. It is not a statement of the law, and anyone with a specific question should take advice from a professional who knows the current position.</p>
<h2>What the analysis says</h2>
<p>According to the analysis, there is no general right in UK law to own one&rsquo;s voice in the way that some people might expect. Protection instead comes from several separate areas. Copyright can protect a recording, data protection can cover personal information including some voice data, trademarks can protect a name or brand, and the tort of passing off can apply where a person&rsquo;s reputation is used to sell something without permission.</p>
<p>The analysis argues that none of these was designed with AI cloning in mind, so each has gaps. A cloned voice may not be a copy of an existing recording, and a voice may not be personal data in every case. That is the heart of the argument.</p>
<h2>What it does not say</h2>
<p>The analysis does not say that cloning a voice is always lawful, and it does not describe the outcome of any case. It is a commentary on the existing framework, prompted by a news report. Claims that the law has already changed, or that a particular court has ruled, should be checked against the primary sources, because not every claim in circulation has been verified.</p>
<p>Legislation may change, and the government may respond. Check the current position on the official legislation website, and watch for any consultation or bill that touches on digital replicas or personal data.</p>
<h2>Why creators should care</h2>
<p>A UK creator who clones a voice, or who works with a person whose voice is cloned, may face a dispute even where the law is unclear. A dispute can be costly and damaging, even if the outcome is uncertain. The safer course is to rely on consent, a clear agreement and honest labelling, rather than on a reading of unsettled law.</p>
<p>The same applies to the speakers. A podcast guest whose voice might be copied has an interest in knowing how the recording will be used and kept. Agreeing that in writing protects both sides.</p>
<h2>Practical steps while the law is debated</h2>
<ol>
<li>Get written consent before recording or generating any voice, stating the intended uses.</li>
<li>Set a time limit on how long the voice files are kept, and delete them when it expires.</li>
<li>Label any generated or altered voice clearly in the content.</li>
<li>Keep the raw recordings and the consent note together, with a dated record.</li>
<li>Take advice before any commercial use, especially in advertising or sponsorship.</li>
</ol>
<h2>What to watch</h2>
<p>Watch for changes in legislation, consultations on digital replicas and any guidance from the bodies that regulate data and advertising. Each of these could change the practical position. Keep a short note of the sources you rely on and check them again before a major project.</p>
<h2>What a UK creator should document</h2>
<p>If you record or generate a voice in the UK, keep a short record that answers four questions: who the voice belongs to, what they agreed, what it will be used for, and when it will be deleted. A dated copy of the consent, the session notes and any licence should sit with the project files.</p>
<p>Document the tools too. Note which tool generated or altered the voice, what the terms said at the time, and whether the audio was uploaded. That record helps if a question arises about how the voice was made.</p>
<h2>Read the position for the country your audience is in</h2>
<p>A creator based in one country may publish to listeners in another, and the rules that apply can follow the audience as well as the speaker. A UK creator with a large audience abroad should check the rules in those places too, because a clip that is lawful at home may breach a different regime elsewhere. Map your main audiences before you publish, and note which rules you have checked for each.</p>
<p>When the position is unclear, the cautious choice is the one most creators would accept on reflection: consent in writing, a clear label and no use that could mislead. Those three habits satisfy most sensible readings of the law as it stands, while the debate continues.</p>
<h2>Limits</h2>
<p>This post summarises commentary and a news report, and it has not checked the underlying legal texts line by line. The analysis itself is a single view, and other lawyers may read the position differently. It is general guidance and not legal advice.</p>
<h2>Keep the recording honest and clean</h2>
<p>Whatever the legal position, a clean recording is the best starting point for any honest project. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the general overview of voice cloning rules, read the <a href="/tunedzy/blog/voice-cloning-laws-2026-overview">overview post</a> in this series.</p>
''',
    faq=[('Is there a UK law that protects my voice?', 'Commentators say protection comes from several separate areas, not one right. Check the current position with a professional.'),
         ('Can a cloned voice be copyright?', 'Copyright may protect a recording, but not always a generated voice. The position is unsettled.'),
         ('What should I do as a UK creator?', 'Get written consent, label generated voices, and take advice before any commercial use.'),
         ('Where do I check the latest position?', 'On the official legislation website and the websites of the regulators, not only in summaries.')])

add(slug='voice-clone-scam-calls-explained', cluster='trend-voice-law', kw='voice clone scam calls',
    title='Voice Clone Scam Calls Explained and How to Spot Them',
    desc='Voice clone scam calls explained: how they are made, the warning signs to listen for, what regulators and telecoms have done and a simple family safety plan.',
    h1='Voice Clone Scam Calls Explained and How to Spot Them',
    answer='Voice clone scam calls use a copied voice, often of a relative or a known person, to pressure someone into sending money or information. Warning signs include urgency, secrecy and requests for payment by unusual means. Agree a family code word and always call back on a known number before acting.',
    body='''
<p>A phone call that sounds exactly like someone you know, asking for urgent help, is one of the most frightening forms of fraud. Scammers can now copy a voice from a short sample, often taken from a public video or voice message, and use it to pressure a victim. The technology is easy to misuse, and the emotional pull of a familiar voice makes the scam effective. Knowing how it works is the first defence.</p>
<p>This post explains how these scams are commonly run, what to listen for, what has been done about them, and a simple plan that any family or small team can adopt. It is written for ordinary people and for anyone who handles payments in an organisation.</p>
<h2>How the scam usually works</h2>
<p>A scammer collects a short sample of a voice, often from a social media video, a voicemail or a podcast clip. They use a cloning tool to produce speech that sounds like that person, then call a relative, colleague or friend. The call usually creates urgency: an emergency, an arrest, a lost phone or a sudden payment that must be made now. The scammer asks for money, bank details or a code, and asks the victim not to tell anyone.</p>
<p>The voice may be imperfect, especially on a poor line, and the scammer may blame a bad connection. Familiarity and panic do the rest.</p>
<h2>Warning signs to listen for</h2>
<ul>
<li>Urgency that stops you from checking, such as a demand to act within minutes.</li>
<li>A request for secrecy, such as &ldquo;don&rsquo;t tell anyone&rdquo;.</li>
<li>A request for payment by gift card, cryptocurrency or a transfer to a new account.</li>
<li>A voice that sounds slightly flat, rushed or unusual, especially on a repeated phrase.</li>
<li>A caller who avoids answering a simple question that only the real person would know.</li>
</ul>
<h2>What has been done</h2>
<p>In the United States, reports describe federal action focused on fraud and on robocalls. The Federal Communications Commission has rules on caller identification, adopted after a robocall used a cloned voice of a politician. The Federal Trade Commission has been reported as looking at ways to curb scams that use cloned voices. Telecoms and banks have also introduced warnings and call screening in many places.</p>
<p>These measures help but do not stop every call. The most reliable protection is a habit that works whatever the technology does next.</p>
<h2>A family code word</h2>
<p>Agree a code word with your close family and friends, and do not write it anywhere or share it online. If a caller claims to be a relative in trouble, ask for the code word. A real relative will know it. A scammer will not. Change the word if it is ever shared. This simple step defeats most voice clone scams, because the scammer has the voice but not the secret.</p>
<h2>Always call back on a known number</h2>
<p>If a call asks for money or information, hang up and call the person back on the number you already have, not on a number the caller gives you. Do the same with a colleague who asks you to make an urgent payment. A real request will survive a short check. A scam will often fail when the check is made.</p>
<h2>For organisations</h2>
<p>Businesses should set a rule that payment requests above a set amount need a second check through a separate channel. Staff should know that a convincing voice is not proof of identity, and that a request to bypass normal process is itself a warning sign. Train staff to report suspected calls, and keep a record of what happened.</p>
<h2>If you have been targeted</h2>
<p>Stop contact with the caller, report the call to your bank and to the police or the relevant national agency, and keep any messages or call records. If money has been sent, contact your bank quickly, since fast action can sometimes help. Do not feel embarrassed. These scams are designed to work on careful people.</p>
<h2>Talk to older relatives and colleagues</h2>
<p>Scam calls often target people who are less familiar with the technology, including older relatives and staff who handle payments. Explain the pattern in plain words, and show them the code word and call-back habit before anything happens. A short conversation, repeated once or twice, is more useful than a long warning that is forgotten.</p>
<p>Make it easy to ask for help. Encourage anyone who is unsure to check with you or a colleague before acting, and reassure them that checking is the right thing to do, even when it turns out to be genuine.</p>
<h2>Limits</h2>
<p>No single tip stops every scam, and the technology will keep changing. This post describes common patterns and sensible habits, not guaranteed protection. If you are unsure whether a call is genuine, treat it as a scam until you have checked it.</p>
<h2>Protect the voices you publish</h2>
<p>Public recordings are one source of voice samples, so think about what you post. The <a href="/tunedzy/blog/protect-your-voice-from-cloning">voice protection post</a> in this series covers practical steps. For honest recordings that you publish, the <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording.</p>
''',
    faq=[('How do scammers get a voice sample?', 'Often from public videos, voicemails or podcast clips. Anything public can be a source.'),
         ('What is the best protection?', 'A family code word and a call back on a known number before any payment.'),
         ('What if the caller knows personal details?', 'Personal details can be found online. Use the code word and the call back, not your judgment of the voice.'),
         ('Who should I report it to?', 'Your bank and the police or the national agency for fraud where you live.')])

add(slug='protect-your-voice-from-cloning', cluster='trend-voice-law', kw='protect my voice from cloning',
    title='How to Protect Your Voice From Cloning: Practical Steps',
    desc='How to protect your voice from cloning: what to share publicly, how to keep raw recordings safe, what to ask platforms and how to respond if your voice is copied.',
    h1='How to Protect Your Voice From Cloning: Practical Steps',
    answer='You cannot make your voice impossible to copy, but you can reduce the risk. Limit how much clean audio you publish, keep raw recordings private, read the terms of voice tools, agree written rules with collaborators, and act quickly if a copy appears.',
    body='''
<p>Your voice is part of who you are, and it can now be copied with a few seconds of audio. Complete protection is not possible, because anything you publish can be recorded. What you can do is reduce the risk, make misuse harder and respond quickly if it happens. The steps below range from simple habits to agreements with the people you work with.</p>
<p>This guide is for creators, public speakers and anyone whose voice appears in public recordings. It is general practice, not legal advice, and the rules in each place differ.</p>
<h2>Think about what you publish</h2>
<p>Clean, long recordings of your voice are the most useful to someone who wants to copy it. Consider how much you publish, and whether the recordings need to be as clean as they are. A conversation with background noise is less useful to a copier than a studio-quality monologue. This is a trade-off, because clean audio helps your listeners, but it is worth deciding deliberately.</p>
<p>Keep a list of where your voice appears publicly. A list makes it easier to notice a copy and to check what you have already shared.</p>
<h2>Keep raw recordings private</h2>
<p>The raw files are the most sensitive part of your recordings. Store them in a private folder, with a backup, and limit who can access them. Share only the finished episode or the clip that is needed, not the full raw session, unless there is a clear reason and an agreement. The <a href="/tunedzy/blog/how-to-back-up-audio-recordings">backup post</a> in this series explains how to keep them safe.</p>
<h2>Read the terms of voice tools</h2>
<p>Before you upload your voice to a tool, read what it does with the file. Check whether it is stored, for how long, whether it is used to train models and whether you can delete it. A tool that is vague about these points is a risk. A tool that makes deletion easy and says clearly what it keeps is a better choice.</p>
<p>Use one tool for one purpose where you can, and delete the uploaded samples when the project ends.</p>
<h2>Agree rules with collaborators</h2>
<p>If you work with editors, guests or producers, agree in writing how your voice may be recorded, edited, stored and used. Include whether any generated speech is allowed, and what happens to the files when the project ends. A short agreement avoids most disputes, and it shows that you take your voice seriously.</p>
<h2>Keep a record of consent</h2>
<p>When you agree to a use of your voice, keep a dated record. The record is useful later if a question arises about what you approved. Store it with the project files, and include the scope, the duration and any limits.</p>
<h2>Watch for copies</h2>
<p>Search occasionally for your name and phrases you often use, and set alerts where a platform allows them. A copy may appear on a video or audio site with no credit. If you find one, save the link and the date before taking any action, because the content may disappear.</p>
<h2>What to do if a copy appears</h2>
<ol>
<li>Save the link, the date and any copy of the content.</li>
<li>Contact the platform through its reporting tool, and explain what the content is.</li>
<li>If the copy is used to sell something or to deceive people, take advice on the options available where you live.</li>
<li>Tell your audience, calmly, if the copy could mislead them.</li>
</ol>
<h2>Make a plan before a problem</h2>
<p>It is easier to act calmly if you have decided in advance what to do. Write a short plan that names who to contact, which platform reporting tools to use, who keeps the evidence and who speaks to the audience if needed. Keep the plan with your project files, and review it once a year.</p>
<p>A plan also helps you respond to a copy that looks harmless. Not every copy is a threat, and a measured response is often more effective than an angry one.</p>
<h2>Think about the voice in the archive</h2>
<p>Many creators have years of old recordings online, from early episodes, talks, interviews and videos made before anyone thought about voice copying. Those archives are a large source of samples. You do not need to delete them, but you can review them. Ask which recordings contain the cleanest, longest samples of your voice, and whether those are still the ones you want public.</p>
<p>Where an old recording no longer reflects your work, you may choose to make it private or to replace it with a cleaner, shorter version. Every change reduces the material available to a copier, and it costs little to make.</p>
<h2>Limits</h2>
<p>These steps reduce risk but do not remove it. Platforms and the law respond unevenly, and the position is still developing in many places. Expect to adjust your habits as the tools and the rules change.</p>
<h2>Publish honest, clean audio</h2>
<p>Clean recordings are good for listeners, and honest labelling protects you. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording in your browser. For what the law says about labelling, read the <a href="/tunedzy/blog/how-to-label-ai-generated-voice-in-content">labelling guide</a> in this series.</p>
''',
    faq=[('Can I stop my voice being copied completely?', 'No. Reduce the risk through habits and agreements, and act quickly if a copy appears.'),
         ('Should I stop publishing my voice?', 'Not necessarily. Think about how much clean audio you share, and keep raw files private.'),
         ('What if a tool keeps my voice?', 'Read the terms, ask for deletion, and avoid tools that are vague about storage and training.'),
         ('Who can help if my voice is copied?', 'The platform, a lawyer and, for fraud, the police or the national agency where you live.')])

add(slug='using-a-famous-voice-in-a-video-legal-basics', cluster='trend-voice-law', kw='celebrity voice in video legal',
    title='Using a Famous Voice in a Video: Legal Basics',
    desc='Using a famous voice in a video: why an imitation can still be risky, what permission usually means, and the safer alternatives for creators.',
    h1='Using a Famous Voice in a Video: Legal Basics',
    answer='Using a famous voice, real or generated, in a video can create legal and reputational risk, even without a clip from the original. Permission is usually needed for a recognisable voice in advertising or endorsement. Safer options include an original voice, a licensed voice actor and a clear disclosure.',
    body='''
<p>Creators sometimes want a recognisable voice for a parody, a tribute or a sponsored video, and AI tools now make it easy to try. A voice that listeners instantly identify can carry a lot of meaning, and it can also cause real problems. The law and the platforms treat the use of a recognisable person as a serious matter, and the safe choice is usually to avoid it.</p>
<p>This post explains the main risks, why imitation is not always safe, and what creators can do instead. It is general guidance, not legal advice, and the position varies by country and by the kind of use.</p>
<h2>Why imitation can still be risky</h2>
<p>Many creators assume that copying a voice is safe if they never use the original recording. That is not a reliable assumption. A generated or imitated voice can still suggest that the person took part, approved a product or said something they did not say. The risk comes from the impression created, not only from the copying of a file.</p>
<p>Where a voice is used to sell something, the risk grows. A false endorsement can mislead customers and harm the person whose voice is used. That is the situation where legal claims, platform action and reputational damage are most likely.</p>
<h2>What permission usually means</h2>
<p>Permission should be specific. It should say who is giving it, what the voice will be used for, where it will appear, for how long and whether it can be edited or generated. A general statement of approval is weak protection. For a commercial use, the agreement should be written and reviewed by a professional.</p>
<p>Permission from a voice owner or an agent may not cover every right, especially where a recording or a composition is also involved. Check each element separately.</p>
<h2>Parody and commentary</h2>
<p>Parody and commentary are treated differently in many places, and they can be strong forms of expression. Even so, they are not a blanket excuse. A parody that is clearly a parody, does not mislead, and makes a point about the public figure is in a stronger position than one that could pass as real. If you are relying on this, take advice on the specific work.</p>
<h2>Advertising and endorsement</h2>
<p>An advertisement that uses a recognisable voice is one of the riskiest uses. Advertising rules often require honesty about endorsements, and a voice that suggests a real person approved a product may breach them. Do not use a recognisable voice in an advertisement without written permission and professional advice.</p>
<h2>Safer alternatives</h2>
<ol>
<li>Use your own voice, or the voice of a person who has agreed in writing.</li>
<li>Hire a voice actor with a clear licence for the intended use.</li>
<li>Use a generic, clearly non-identifiable voice, with a visible label where it is generated.</li>
<li>Create a fictional character with its own name and personality.</li>
</ol>
<h2>What to do before publishing</h2>
<p>Ask whether a viewer would reasonably think the person took part or approved the content. If the answer is yes, get permission or change the approach. Keep a record of any permission, and label any generated voice clearly, as covered in the <a href="/tunedzy/blog/how-to-label-ai-generated-voice-in-content">labelling guide</a> in this series.</p>
<h2>When a parody becomes a risk</h2>
<p>A parody can cross a line when it stops being obviously a parody. A short clip with no context, shared on a platform where people scroll quickly, can be taken as a real endorsement. Add a clear frame at the start, such as a title card that says the piece is satirical, and avoid a product or an offer that a viewer could mistake for a real one.</p>
<p>If the parody uses a recognisable voice to make a point about a public figure&rsquo;s conduct, the point should be clear in the piece itself. A viewer who needs the description to understand the joke may not reach it.</p>
<h2>Check the platform rules as well</h2>
<p>Even where the law is unclear, platforms set their own rules for impersonation, deceptive content and synthetic media. A video that breaks those rules may be removed, demonetised or restricted, whatever its legal status. Read the platform&rsquo;s policy before you publish, and check whether it asks for a label on generated or altered content. Rules change, so read the current version rather than relying on memory.</p>
<p>Platform rules can be a practical guide even when the law is uncertain. If a platform asks for a label, add one. If it prohibits a use, do not publish the video there, however strong the case seems to you.</p>
<h2>Limits</h2>
<p>The law on voice use varies, and it is changing. Some uses that seem obviously safe may be risky, and some that seem risky may be permitted. This post cannot cover every case. For a commercial project, take advice before publishing.</p>
<h2>Keep your own voice clean and honest</h2>
<p>Your own voice is the safest one to use, and it should sound its best. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording in your browser. For the wider picture, read the <a href="/tunedzy/blog/voice-cloning-laws-2026-overview">voice cloning overview</a> in this series.</p>
''',
    faq=[('Is a voice imitation safe if it is not a copy?', 'Not necessarily. An imitation can suggest endorsement or approval, which creates risk.'),
         ('Do I need permission for parody?', 'Parody is treated differently in many places, but it is not a blanket exception. Take advice on the specific work.'),
         ('Can I use a voice actor who sounds like someone?', 'Only with a licence for the intended use. Imitation for advertising is especially risky.'),
         ('What is the safest option?', 'Your own voice, a licensed voice actor, or a clearly fictional character with a label.')])

add(slug='voice-actors-and-ai-what-is-changing', cluster='trend-voice-law', kw='voice actors and ai',
    title='Voice Actors and AI: What Is Changing and What To Do About It',
    desc='Voice actors and AI: what is changing in voice work, how contracts are responding, what consent and fair pay look like, and how producers can act responsibly.',
    h1='Voice Actors and AI: What Is Changing and What to Do About It',
    answer='AI is changing voice work, with some routine jobs automated and new questions about consent, pay and reuse of voices. Voice actors and producers can respond with clear contracts that define each use, fair pay for any reuse and written consent for any generated voice. Responsible producers label generated speech.',
    body='''
<p>Voice acting has always been shaped by technology, from recording studios to remote sessions. AI now raises a sharper question: can a voice be captured once and reused in ways the performer never agreed? That question is changing contracts, expectations and the way producers plan their work. This post explains the changes, the questions they raise and the steps that make the work fairer for everyone.</p>
<p>It draws on the general direction of the industry and on public debate, rather than on any single report. Where a specific claim depends on a particular case or a law, it is marked as such, and the reader should check the current position.</p>
<h2>What is changing</h2>
<p>Some routine voice tasks, such as simple narration, reading of short prompts or basic dubbing, are being automated in some projects. Producers may use generated voices for drafts, for prototypes or for lower-budget content. Voice actors report being asked to record a session that could later be used to train or generate a model, which raises questions about what the performance is worth.</p>
<p>At the same time, new work is appearing. Some voice actors license their voices for specific uses, and some producers use generated speech for accessibility or for versions in other languages. The change is not only a loss, but a shift in what a voice is licensed to do.</p>
<h2>The contract question</h2>
<p>The most important question is the contract. A voice actor should know what the recording may be used for, whether it can be used to build a model, for how long, in which territories and for which fees. A vague clause that allows any future use is a risk. A clear clause that limits the use, and requires a new agreement for anything else, protects the performer.</p>
<p>Producers who want a generated version of a performer&rsquo;s voice should ask for a separate agreement, and pay fairly for it. Reuse is a use, and it should be priced as one.</p>
<h2>Consent and fair pay</h2>
<p>Consent should be specific and revocable where possible. A performer should be able to see how their voice is used and to stop future use where the contract allows. Fair pay for reuse means that a performance is not treated as a one-off fee when it is used again and again. The details vary by contract, but the principle is that the performer shares in the value they help create.</p>
<h2>What producers can do</h2>
<ol>
<li>Write contracts that name each permitted use, and require a new agreement for anything else.</li>
<li>Pay separately for any model training or generated voice, and say so in the contract.</li>
<li>Label generated speech clearly in the finished work, as covered in the <a href="/tunedzy/blog/how-to-label-ai-generated-voice-in-content">labelling guide</a>.</li>
<li>Keep records of consent, sessions and payments, and share them with the performer on request.</li>
<li>Offer performers a way to decline a generated use without losing other work.</li>
</ol>
<h2>What voice actors can do</h2>
<p>A performer can ask for a clear contract before a session, read the clauses on reuse and training, and keep a copy of what was agreed. They can negotiate a limit on the uses, ask for a fee for each new use, and say no to a session that seems designed for a model rather than a project. Joining a professional body or union can help with shared standards and advice.</p>
<h2>Building a fair working relationship</h2>
<p>A fair relationship between a producer and a voice actor starts before the session. Explain the project, the expected uses and the timetable. Ask what the performer needs, and listen to their concerns about reuse. A performer who understands the plan is more likely to give a strong, committed performance.</p>
<p>Keep the relationship open after the session. Tell the performer when the work is used, share the finished version, and pay promptly. Trust built this way makes future work easier for both sides.</p>
<h2>Plan for the long term</h2>
<p>A voice actor&rsquo;s career depends on repeat work and a reputation for reliability. A contract that trades a long-term future for a single fee may look attractive now but can damage that career. Before signing, think about how the recording could be used in five years, and whether the fee reflects that use. A producer who asks for a fair long-term deal often finds it easier to hire the same performer again.</p>
<p>For producers, the long view means building a library of consented voices with clear terms. A well-documented library is easier to manage, easier to audit and more valuable than a collection of recordings with unclear rights.</p>
<h2>Limits</h2>
<p>The industry is changing quickly, and practice varies by country, by union and by sector. This post describes the main questions rather than the rules in any one market. Anyone signing a contract should take advice from a professional who knows the local position.</p>
<h2>Keep the work honest and the audio clean</h2>
<p>Whether a voice is human or generated, the finished audio should sound its best. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For how consent and labelling fit together, read the <a href="/tunedzy/blog/voice-cloning-laws-2026-overview">voice cloning overview</a> in this series.</p>
''',
    faq=[('Will AI replace voice actors?', 'It is changing some routine work. Demand for clear, skilled performance remains, but contracts and pay are being reshaped.'),
         ('What should a voice contract say?', 'Each permitted use, the territory, the duration, any training or model use, and the fee for each use.'),
         ('Can a producer reuse a recording later?', 'Only where the contract allows it. A new use needs a new agreement, and usually new payment.'),
         ('Should generated speech be labelled?', 'Yes, where it could be taken as real. Labelling is good practice and in some places a legal duty.')])

add(slug='disclosing-ai-voices-in-podcasts', cluster='trend-voice-law', kw='disclose ai voice podcast',
    title='Disclosing AI Voices in Podcasts: What to Say and Where',
    desc='How to disclose AI voices in podcasts: when disclosure is needed, what to say on air, where to put the note and how to keep listeners trusting the show.',
    h1='Disclosing AI Voices in Podcasts: What to Say and Where',
    answer='Disclose any AI-generated or cloned voice in a podcast clearly, near the start of the episode, with a plain sentence that says what was generated and whose voice it is based on. Repeat the note in the description, and keep the same wording across the show so listeners learn to trust it.',
    body='''
<p>Podcasts are built on trust between a host and a listener. A voice that listeners think is human, and that turns out to be generated, can break that trust quickly. Disclosure is the simple way to protect it. Done well, it takes a few seconds and makes the show more credible. Done badly, it reads like a warning label and makes listeners uneasy.</p>
<p>This guide covers when disclosure is needed, how to word it, where to place it and how to keep it consistent across a season. It is practical advice for podcasters, and it sits alongside the legal points covered elsewhere in this series.</p>
<h2>When disclosure is needed</h2>
<p>Disclose any voice that is generated, cloned or altered so that it could be taken as real. A narration voice generated from text, a host voice created from a recording and a guest voice produced by a tool all count. Cleaning noise, levelling speech or cutting a pause does not generally need a disclosure, because the speech is still the person&rsquo;s own.</p>
<p>When you are unsure, disclose. A short note is cheap, and it prevents a complaint that could damage the show far more.</p>
<h2>Say it in plain words</h2>
<p>Use words that describe what happened. A sentence such as &ldquo;the narration in this episode was generated by an AI voice model, based on a recording of the host&rdquo; is clear and honest. Avoid vague phrases such as &ldquo;enhanced audio&rdquo;, which can mislead, and avoid jargon. The listener should understand the disclosure the first time they hear it.</p>
<p>If the voice is cloned from a real person, say so, and say whether that person agreed. That detail protects both the speaker and the listener.</p>
<h2>Place it at the start</h2>
<p>Put the disclosure near the beginning, after the intro and before the first generated line. A listener who joins late, or who skips the intro, should still hear it before the generated voice matters. If the generated voice returns after a long gap, repeat a short reminder.</p>
<p>A disclosure at the very end of an episode is easy to miss, and many listeners never reach it.</p>
<h2>Add it to the description</h2>
<p>A written note in the episode description gives listeners a place to check, and it helps the transcript and search record the disclosure. Use the same words as the spoken note. The written note supports the spoken one, but it should not replace it, because many listeners never read the description.</p>
<h2>Keep the wording the same</h2>
<p>Use the same disclosure across every episode where the voice appears. Listeners learn to recognise it, and that recognition builds trust. Change the wording only if the tool, the voice or the way it is used changes, and say so on air when you do.</p>
<h2>Check the transcript and captions</h2>
<p>Automatic transcripts may not mark the generated voice. Add the disclosure to the transcript and captions by hand, and check the names and terms against the audio. A transcript that hides the disclosure undermines the note, even when the audio includes it.</p>
<h2>Keep clips honest too</h2>
<p>A clip cut from an episode may reach people who never hear the full show. If the clip contains a generated voice, add the disclosure to the clip itself, in the audio or in a caption. The <a href="/tunedzy/blog/how-to-turn-a-podcast-episode-into-short-clips">short clips post</a> covers the wider practice.</p>
<h2>Make the disclosure part of the template</h2>
<p>Write the disclosure into your episode template, so it is added every time without a decision. Include the exact words, the place in the episode where they appear and the matching description note. A template removes the risk that a busy week leads to a missed label.</p>
<p>Review the template when the voice, the tool or the way it is used changes. Update the wording on the same day, so the old disclosure does not outlast the change.</p>
<h2>Explain the disclosure to listeners</h2>
<p>Listeners often accept a disclosure more easily when they understand why it is there. A short line such as &ldquo;we label generated voices so you always know what you are hearing&rdquo; explains the purpose without a lecture. Tell listeners what the voice does in the show, such as reading a summary or translating a segment, so they can judge the use for themselves.</p>
<p>If the voice is a version of a real person, say whether that person agreed and how they are credited. Honesty about the process builds the trust that the disclosure is meant to protect, and it gives the audience a reason to keep listening.</p>
<h2>Limits</h2>
<p>A disclosure does not make a misleading use acceptable, and it does not replace consent from the person whose voice is used. Some uses may be restricted whatever the disclosure says. This is general practice, not legal advice.</p>
<h2>Keep the recordings clean and honest</h2>
<p>Real voices deserve the same care as generated ones. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a recording, and the <a href="/tunedzy/go/">Tunedzy Go</a> page covers cleaning a phone recording. For the labelling rules that apply in the EU, read the <a href="/tunedzy/blog/eu-ai-act-deepfake-labels-explained">EU labelling post</a> in this series.</p>
''',
    faq=[('Do I always need to disclose AI voices?', 'Disclose any voice that could be taken as real. When in doubt, disclose.'),
         ('Is a note in the description enough?', 'No. Use a spoken note near the start, and add the written note to the description.'),
         ('What if I only clean my own recording?', 'Cleaning noise and levelling do not usually need a disclosure, because the speech is still yours.'),
         ('Do I need to disclose in clips?', 'Yes, if a clip contains a generated voice, since viewers may never hear the full episode.')])

add(slug='how-to-spot-a-deepfake-voice', cluster='trend-voice-law', kw='how to spot a deepfake voice',
    title='How to Spot a Deepfake Voice: Practical Checks for Listeners',
    desc='How to spot a deepfake voice: checks on the source, the context and the claim, which audio cues help and which do not, and why no single test is reliable.',
    h1='How to Spot a Deepfake Voice: Practical Checks for Listeners',
    answer='No single test reliably spots a deepfake voice, because generated speech keeps improving. Check the source, search for the same claim in trusted outlets, look for a disclosure, and be most careful when a voice asks for money or urgent action. Treat audio cues as clues, not proof.',
    body='''
<p>Generated voices are getting harder to tell apart from real ones, and many listeners now hear a voice online that they cannot quickly judge. The temptation is to rely on a single sign, such as an odd pause or a flat tone. That approach fails, because the sign can be missing or can be faked. A better habit is to check the context, the source and the claim, and to slow down when the stakes are high.</p>
<p>This guide is for listeners, not for experts. It explains the checks that help, the ones that mislead, and what to do when you are unsure. It does not offer a guaranteed test, because none exists.</p>
<h2>Start with the source</h2>
<p>Ask who published the audio and how they came to have it. A verified account on a platform you trust is a better starting point than an anonymous page or a message forwarded from a stranger. Check whether the channel has a history of posting original material, and whether it links to a named person or organisation that you can contact.</p>
<p>Be careful with recordings that arrive without context. A clip with no date, no location and no speaker name should raise your guard, especially if it is shared with strong emotion and urgency.</p>
<h2>Search for the same claim</h2>
<p>A real event usually leaves traces. Search for the key claim, the quoted words or the event, and see whether reputable outlets, official sources or the people named have reported it. If the claim appears only in one place, and nobody else can confirm it, treat it with caution. Reverse searches for images and clips can also show where a recording first appeared.</p>
<p>When a voice seems to say something surprising about a public figure, check the figure&rsquo;s own channels. Official statements are often the fastest way to confirm or refute a claim.</p>
<h2>Listen for cues, but do not rely on them</h2>
<p>Some listeners notice unnatural breathing, odd emphasis, a flat emotional tone, repeated phrasing or a room sound that does not match the setting. These cues can be useful clues. They are not proof. A real recording can sound odd on a poor line, and a generated voice can be made to sound natural. Use the cues to decide where to look next, not to settle the question.</p>
<p>Notice whether the audio sounds too clean for the setting. A voice recorded outdoors with no wind, traffic or echo is worth checking, although many real recordings are also clean.</p>
<h2>Look for a disclosure</h2>
<p>Creators who use generated voices are increasingly expected to disclose them, as covered in the <a href="/tunedzy/blog/disclosing-ai-voices-in-podcasts">disclosure post</a> in this series. A disclosure near the start, or a written note in the description, is a good sign. The absence of a disclosure does not prove a deepfake, because many people publish without one, but it is a reason to check further.</p>
<h2>Ask what you would lose if you believed it</h2>
<p>Consider the stakes. A voice that asks you to send money, share a password, make a payment or take an urgent action deserves the most care. Scammers use urgency to stop you checking. If the message pushes you to act now and tell no one, that pressure is itself a warning. Pause, check, and contact the person on a number you already know.</p>
<h2>Use a code word and a call back</h2>
<p>For calls from people you know, agree a family or team code word that is never written down. A real relative will know it. Always call back on a known number before any payment, even when the voice sounds exactly right. The <a href="/tunedzy/blog/voice-clone-scam-calls-explained">scam calls post</a> explains these steps in more detail.</p>
<h2>Detection tools have limits</h2>
<p>Some tools claim to detect generated speech. Their results vary, they can be wrong in both directions, and they may not work on compressed or re-recorded audio. Do not rely on a single score, and do not treat a tool as the final judge. Use it as one more input alongside the source, the context and a search for the claim.</p>
<h2>What creators can do to help</h2>
<p>If you publish audio, make it easy for people to check. Keep the raw recordings, publish a clear source note for each episode, and label any generated voice. Consistent provenance makes your real recordings easier to trust, and it makes fakes that copy your show easier to spot.</p>
<h2>Limits</h2>
<p>These checks reduce risk but do not remove it. A convincing fake can pass many tests, and a real recording can fail some of them. The safest habit is to verify before you act, especially when money or private information is involved.</p>
<h2>Keep your own recordings verifiable</h2>
<p>A clean, documented recording is easier to trust than one that has been heavily processed without a record. The <a href="/tunedzy/tools/vocal-checker">Vocal Checker</a> shows clipping, noise and level problems in a file you own. It does not detect generated speech, so do not read its results as proof of authenticity. For a clean phone recording, the <a href="/tunedzy/go/">Tunedzy Go</a> page covers the steps in your phone&rsquo;s browser.</p>
''',
    faq=[('Is there a reliable test for deepfake voices?', 'No single test is reliable. Combine checks on the source, the context and the claim.'),
         ('Are odd pauses a sure sign?', 'No. They are clues at most, and real recordings can sound odd too.'),
         ('What should I do if a voice asks for money?', 'Stop, call the person back on a number you know, and check with a family or team code word.'),
         ('Can I trust detection tools?', 'Use them as one input only. Their results vary and they can be wrong.')])
