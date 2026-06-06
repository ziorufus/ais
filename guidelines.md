### Adapted Autobiographical Interview (aAI) Scoring Manual

```
(Version: November 2022 )
```
```
From: Addis, DR, Wong, AT, Schacter, DL (2008). Age-related changes in the episodic simulation of future events.
Psychological Science, 19, 33–41.
Adapted from: Levine, B, Svoboda, E, Hay, J, Winocur, G, Moscovitch, M. (2002). Aging and autobiographical
memory: dissociating episodic from semantic retrieval. Psychology and Aging, 17, 677-689.
Software: Autobiographical Interview Scoring (AIS) available as part of SciToS
```
#### https://github.com/scientific-tool-set/scitos/releases

## Overview

The Adapted Autobiographical Interview (aAI) the number and types of details comprising descriptions of specific
events from a participant’s personal past and imagined events that may occur in their personal future. For more detailed
information on administration, please see the aAI Administration Manual.

When scoring events, the particular administration of the aAI should be considered.

- Instructions: Scoring considers which parts of the response are ‘on-task’ relative to the instructions (e.g.,
    generate past/future events that are specific to a particular time and place) and which parts are ‘off-task’.
- Cues: If participants are provided with word cues (e.g., “DOG”), event cues (e.g., “Moving house”) and/or a
    time period (e.g., “Next Few Weeks”), they may repeat these cues as they think of an event.
- Time limit: Time limits may influence transcription (see below); participants may also be cut off mid-sentence.

Standard aAI scoring typically involves first isolating the ‘main’ specific event (i.e., ‘on-task’ response), dividing the
transcript into small segments (details); and classifying details as either Internal or External to the main event.

## Transcription

The digital audio-recordings of the aAI trials are transcribed using a strict verbatim protocol. All utterances are
transcribed, including fillers and utterances that lack content (e.g., “umm”, etc.) Other suggestions and tips:

- It will help the transcriber if you provide a brief description of the task and the cue(s) used on each trial
- Ensure interviewer questions/comments are also transcribed (e.g., in square brackets prefixed with ‘INTV:’)
- If any speech is inaudible, insert a marker (e.g., time stamp) inside square brackets with the prefix ‘?’ and the
    best guess at what is being said; if it is completely inaudible, insert ‘??’ can also be inserted
- If trials are longer than 1 minute, consider inserting time stamps at each minute (for later use in analysis)
- If a time limit is used, have the transcriber insert ‘[END]’ either at the point where the audible signal/bell is
    heard (if used), or when the specified duration has elapsed. If the participant continues to speak past the end of
    the trial, consider transcribing this additional content if it could be useful as observational data.

## Randomization and de-identification

The following is the procedure followed in the Addis Lab:

- Remove any identifying information from the transcripts (e.g., names, places, businesses etc.) and replace with
    a marker indicating detail type (e.g., ‘[NAME]’ etc.)
- We recommend that transcripts are blinded and randomized at the level of trial across participants (unless there
    is a reason why trials of a given participant need to be scored together). Follow these instructions in Excel:
       1. Column D: Copy the transcript of each trial/event (each on a separate row) from every participant
       2. Columns B/C: Enter participant/trial number. **This is necessary for de-blinding the data after scoring**
       3. Column A: Paste sequence of random numbers (generate sequence of desired length at [http://www.random.org).](http://www.random.org).)
          This number will be the “blind code” for the trial.
       4. Highlight Columns A to D, and sort according to Column A; SAVE FILE as blinding key.
       5. Delete Columns B & C, leaving only Columns A & D. SAVE AS a copy for rater (they can copy/paste
          each transcript directly from Excel to AIS software). Events must be scored in the specified order.


## Isolating and defining the ‘main event’

```
Although participants are (typically) instructed to generate a specific event on each trial, many participants describe
more than one event, or describe events that are difficult to define (i.e., non-specific events). It is therefore necessary to
be clear on what constitutes the main event before any scoring takes place as this then determines if details are
classified as pertaining to the main event (Internal details) or not (E xternal details).
```
```
Isolating the main event: Participants are instructed to provide an event in which they were personally involved (not
just heard about), that is singular (not repeated) and thus is specific to a time and place. Thus, the main event should be
restricted in time, usually being no more than a few hours in duration. For future events, the imagined event should be
novel in some way (i.e., not a memory of a previously experienced event, or continuation of an already established
routine). The interviewer may have used general probing to redirect the participant to an event meeting these criteria.
```
- If an event extends over days or weeks (e.g., a vacation), the scorer must restrict scoring to the best time-
    restricted (< 1 day) event described.
- If more than one event meets the above criteria, choose the one that is described in the most detail.
- If an event meeting these criteria is slightly longer than 24 hours but this clearly reflects a direct continuation of
    the experience (e.g., in the same location) for a few hours or less, it can also be considered the main event (but
    this should be the exception not the rule)

No main event: One of the most difficult scoring situations is when the event is very impoverished or non-existent
(e.g., only factual information is given, the participant can only generate a repeated event, or the participant is unable to
imagine a novel future event). In such cases, it may be possible to select some details as probably specific to an event
and to score them as Internal accordingly. However, in such cases, the majority of details will be External.

## Text Segmentation

```
A segment, or detail, is an informational ‘bit’ or unit; it is a unique occurrence, observation, fact, statement, or thought.
This will usually be a grammatical clause – a sentence or part of a sentence that independently conveys information (i.e.,
a subject and a predicate), although a single clause may contain more than one detail. For each clause, consider whether
each constituent detail conveys additional information. If so, the parts can be separated and scored as separate details.
```
```
For example, the statement he had an old, brown fedora would be segmented into three details: brown
adds perceptual detail to fedora, and similarly, old adds further perceptual detail (e.g., it looks old/shabby). Note
that not all qualifiers/adjectives are considered to add distinct information (see Adjectives below).
```
Note: The Levine et al. (2002) protocol scores old brown fedora as two details. Therefore there are some
differences in how finely protocols are segmented across studies. It is important that only one segmentation protocol
(aAI, Addis; or AI, Levine) is applied consistently within a given study.

### Segmentation Rules

```
It is important to avoid over-segmenting the text (thus creating details with no informational content) or under-
segmenting the text (thus not capturing the detail generated). As described in the rules below, the type(s) of detail can,
at times, dictate how particular details are segmented (e.g., whether a detail conveys unique information and should
be a distinct detail, or whether it should be subsumed into another detail), and this is dependent on other details in the
transcript. Thus, many scorers will either read the transcript first before segmenting and/or segment as they score.
```
#### Partial details

- RULE: A word/phrase that does not convey any additional information in-of-itself (without the rest of the
    phrase/sentence) should be subsumed into an accompanying detail
- Verbs that (usually) don’t convey sufficient meaning
    e.g.: I felt [partial detail] vs. I felt blessed [1 detail]
    e.g.: They knew [partial detail] vs. They knew who I was [1 detail]
    e.g.: I went [partial detail] vs. I went to the market [1 detail]


```
e.g.: I saw [partial detail] vs. I saw the tower [1 detail]
In contrast, consider these verbs which do convey meaning and can stand-alone as a detail:
e.g.: actions I was sitting [1 detail] vs. I sat on my chair [2 details]
e.g., emotions I was happy [1 detail] vs. She was mad at him [2 details]
e.g.: metacognitions I remember [1 detail] vs. “I can imagine [1 detail]
```
- The participant’s own self cannot be counted as an entity
    e.g.: I [partial detail] vs. I went to the market [1 detail]
- Although a repeated noun (e.g., entity, location) cannot be re-scored, they but these don’t constitute a true
    repetition because the participant has to say which entity they are referring to (e.g., which entity is acting) to
    make sense. As such, they are also considered partial details and subsumed into an accompanying detail. Also
    see segmentation of Repeated Nouns and Repeated Phrases (below) and scoring of External-Repetitions.
- Once the maximum number of entities in an event have been reached (max. 5 individuals + 5 object
    exemplars/categories), any other newly introduced entities are NOT segmented separately but are subsumed into
    an accompany details (unless a “listing” strategy is being used). See Internal-Event for more information.

#### Adjectives that provide additional perceptual information

- RULE: If an adjective adds information in-of-itself, it can be segmented into a separate detail
- Although an adjective does not mean anything without the subject it is referring to, if the addition of the
    adjective adds more perceptual detail, then it should be segmented as an additional detail
- Perceptual qualifiers, such as quantities, amounts, sizes, degrees, colours* (*but see exception below). Note
    however that not all perceptual qualifiers will be scored as Internal-Perceptual details (e.g., low counts of
    entities that imply they are not referring to the ‘scene’ (wide view) but to individual entities; see Internal-Event)
       e.g.: There were dogs [1 detail] vs. There were all these dogs [2 details]
       vs. There were 500 dogs [2 details]
       e.g.: my mug [1 detail] vs. my blue mug [2 details]
- Exceptions: When adjectives are used as an integral part of the one detail (as underlined below) and thus does
    not constitute an additional detail.
       o Time: Approximations are common when localizing the event in time – but the participant is still only
          referring to one point in time and so it is scored one Internal-Time detail.
             e.g.: In a few weeks [1 detail], A couple years back [1 detail]
       o Colours: Qualifying a colour is not scored as a second perceptual qualifier as its still only one colour
          e.g.: My blue mug [2 details], My light blue mug [2 detail]
       o Emotions: A single emotion may be described in multiple words but is still only one Internal-Emotion
          detail (see segmentation of Multi-word descriptors below)
          e.g.: I’m livid [1 detail], I’m really really mad [1 detail]
             e.g.: it was happy [1 detail], it was quite sad [1 detail]
       o Relationships: Describing a relationship in multiple words is only still referring to one relationship (see
          segmentation of Multi-word descriptors below)
             e.g.: she’s my friend ... [1 detail], she’s my best friend [1 detail]
       o Weather: Describing one aspect of weather in multiple words is one detail, unless they are adding a
          further Internal-P erceptual detail (as italicized in these “2-detail” examples below)
             e.g.: it was drizzling [1 detail], it was raining lightly [1 detail]
             vs. it was raining [1 detail] and elsewhere, the rain was hard [1 detail]
             vs. it was raining loudly [2 detail], it was sunny and bright [2 detail]

#### Multi-word descriptors used for single vs. multiple details

- RULE: If you can substitute a multi-word phrase for a single word/concept/entity without changing the
    meaning of what is being conveyed, then it's likely ONE detail.
- Individuals: In conversations, people often refer to entities (people, objects) using a descriptor (e.g., if the name
    is unknown or is meaningless to the conversational partner).
       o Often, the relationship is used as a “pronoun” but other descriptions are also used
          e.g.: my boyfriend’s friend [1 detail]


```
e.g.: the person who did the baptizing [1 detail]
o The entity can only be scored once. If the same description is used repeatedly, then subsequent
mentions are considered partial details and are subsumed into the next detail. See Partial Details for
more information.
e.g.: my brother [1 detail] and later, my brother ... [partial detail]
o If the relationship is as a pronoun but later the name is used, score the name as the entity, and the
relationship as additional information (i.e., it is scored the same irrespective of which appears first).
e.g.: Donna ... [1 detail] and elsewhere, Donna is my sister [1 detail]
e.g.: Irene ... [1 detail] and elsewhere, my best friend Irene [1 detail]
```
- Multiple entities: Occasionally the descriptor phrase might refer to more than one entity.
    o Score this descriptor as one entity unless it is clear the participant is aware of the individuals as distinct
       entities AND only if not already scored individually elsewhere in the transcript
          e.g.: the Sullivan twins [2 details]
o Some descriptors treat the multiple entities as one single unit, such as large groups or crowds. Even
though this description is technically referring to more than 1 entity, score it as one entity (unless there
is evidence to suggest the participant is aware of the individuals). Also, because the individuals
comprising the group haven’t been counted as individuals, particular group members mentioned
elsewhere in the transcript can be scored as individual entities
e.g.: the congregation [1 detail]
- Sayings: People occasionally use a ‘turn of phrase’ or ‘figure of speech’ that actually only refers to one concept.
In such cases, these should be segmented and scored as one detail.
e.g.: it was quite a moment for me [meaning: “it was momentous” = 1 detail]
- Circumlocution: Patients who cannot access a name or concept may use a description to convey the same
meaning. Such phrases should be segmented and scored as one detail.
e.g.: the place where the dolphins swim [meaning: the ocean = 1 detail]
vs. I saw dolphins swimming [meaning: I saw dolphins + they were swimming = 2
details]

#### Dialogue/thought: Segmenting multiple lines of dialogue/thought (including “Other” dialogue/thought)

- RULE: Segment dialogue/thoughts by dividing the text reasonably into phrases or sentences, whether its
    dialogue/thoughts in the event (Internal) OR in the interview itself (External Other: dialogue with
    interviewer, meta-cognitive thoughts, editorializing comments).
- Sometimes dialogue with others or thoughts (inner dialogue) can be lengthy. It can be helpful to think of how
    you would break the text into distinct thought bubbles or speech bubbles in a comic strip; this effectively
    treats each thought or piece of speech as a separate entity or occurrence.
- Exceptions:
o Reflexive single-word responses to interviewer queries (“yes/no/okay”) are not scored.
o False starts are not scored as editorializing comments unless it contains content in of itself
e.g.: He ah, He ah ... He went to Italy [1 detail; “He ah” has no content]
vs.: They went to Italy ... oh no – she didn’t go, just him [2 details]

#### Repeated nouns: Segmenting and scoring a noun (entity, location, time etc.) mentioned more than once

- RULE: A noun is segmented and scored for its existence in the event only once. Other mentions of the
    noun are considered partial details (not repetitions), and subsumed into accompanying detail.
- A given noun (e.g., a particular entity such as a person/object; a particular location, a time period, etc.) can only
    be scored once (i.e., for it being in the event). This one ‘point’ can be assigned to any of the mentions of the
    noun - usually the first mention, or when a clear name or descriptor is first used, and all other mentions are
    scored as follows:
- Scoring other mentions of the entity:
    o Is it scored as a repetition? The noun (entity, location, etc.) in-of-itself is NOT a repetition because it
       has to be said to indicate which noun is referred to (e.g., which entity is acting) in order to make sense.
       However, if the entire phrase (e.g., entity + action) with the same meaning is repeated then it is a
       Repetition (see below).


```
o Is it scored again if different words are used to describe it? If a synonym or pronoun is used, this is
not scored again as it doesn’t add any additional information
e.g., the congregation is also referred to as: everyone, they, the church
[1 detail scored once]
o Would a subsequent mention of a noun ever be scored? Only if the pronoun or synonym is
sufficiently different or more elaborate so as to add new information.
e.g.: person referred to as Jon [1 detail] and then as, my friend [1 detail] = 2 details total
e.g.: pet referred to as my dog [1 detail] and as, my best dog [1 detail] = 2 details total
```
#### Repeat ed phrases: Segmenting and scoring a phrase mentioned more than once

- RULE: A phrase is only scored once for its meaning so if already segmented elsewhere, segment
    repetition as a whole phrase.
- If another phrase that means the same thing is used elsewhere in the transcript, it is scored only once and the
    other instances are scored as Repetitions
       e.g.: Crossed my fingers* is a repetition of hoped for the best
       [*In this example, the first phrase is also segmented as 1 detail as it is a multi-word descriptor,
       i.e., a turn of phrase. See Multi-Word Descriptors].

#### Other tips for segmentation

- Segmentation and scoring of fragmented sentences should allow for natural speech patterns even when they do
    not appear fluent in the transcription. The scorer should attempt to interpret and segment fragmented sentences
    in a way that would be transparent to others.
- If participants repeat the cue(s) at the start of the response:
    o If repetition of the cue is clearly reflexive, do not segment/score.
       e.g.: CUE=Dog, Hmmm DOG ... DOG ... [do not score]
    o If repetition of the cue is part of a meta-cognitive statement, score as usual.
       e.g.: CUE=Dog, Hmmm I can’t think of an event to do with DOG [1 detail]
    o If repetition of the cue is clearly part of the response, score as usual.
       e.g.: CUE=Dog, I have a DOG ... [1 detail]
       e.g.: CUE=Next few years, Okay, so in the next few years, I ... [1 detail]
- Segmentation should be consistent regardless of whether the details are Internal or External
    o An External event (external episodic event or repeated event) should be segmented as it would be if it
       were the main Internal event, i.e., segment it as finely as if it were Internal (although abide by rules for
       partial or repeated details as described above)
    o External dialogue/thoughts in the interview itself (e.g., responses to experimenter queries, meta-
       cognitions) should be segmented similarly to dialogue/thoughts Internal to the main event (i.e., divided
into reasonable phrases)

#### See Appendix A for the Segmentation Cheat-Sheet


## Classification of details: Internal vs. External

Each detail (segmented as above) is classified as Internal to the main event (isolated as defined above) or External to it.

AI scoring is an intense theory-of-mind exercise: the scorer has to simulate the participant’s mind to:

- Determine what the participant experienced/will experience during the main event, that they are p/re-
    experiencing during the interview (i.e., what they are seeing in their mind’s eye)
- What information is pre-existing or long-standing (e.g., back-story, reasoning or inferences after the event but
    before the interview) or added during the interview (e.g., meta-cognition, new inferences)

Getting yourself in the right mindset is crucial. The following ‘thought exercises’ are useful ways to do that, and can
help a scorer determine what is internal/external, and which subcategories to select.

Pretend you are directing a movie of that event. For each detail, consider:

- Does this detail add new information that changes something on set, or on film, for the current scene?
    (Internal). That is, does the detail specify:
       o an entity that has to come on set? (usually Internal-Event) If so, is that entity already on set (i.e.,
          previously mentioned/scored)?
       o action/movement of entities, or dialogue? (usually Internal-Event)
       o orientation of entities to each other (usually Internal-Perceptual)
       o edits to the costumes or hair/make-up or colour/size of objects (usually Internal-Perceptual)
       o edits to the scenery or backdrop? (usually Internal-Perceptual)
       o a monologue of the main character (usually Internal-Emotion/Thought)
       o subtitles that say where/when this happened (usually Internal-Time and/or Internal-Place)
- Does the detail add information that is not part of current scene? (External), i.e., does it specify:
    o an event played out in another scene (usually External-Event or External-Generic)
    o content for the back-story of the characters or the narrative (usually External-Semantic)
    o comments or reactions of the narrator/voice-over (usually External-Other)
- If none of the above apply, consider whether this is an incomplete detail that should be collapsed with another
    detail; this can help avoid over-segmentation

Substitution and switching exercises

- Does removing that detail change anything in the event? If so, what it removes from the event (or movie set)
    may indicate what type of detail it is.
- Switch the order in which details or entities are provided. Does this change anything about the event (or movie
    set)? Would you score the details differently or the same if they are in this new order?

SCORING RULE 1: ‘Benefit of the doubt’ rule – If it is still difficult to determine whether a detail is Internal or
External, then if a detail could reasonably be Internal then score it as Internal. This rule does not apply to all details
that could possibly be Internal; only those that could reasonably be Internal.

Note that the richness of description or number of details does not indicate whether details are Internal or
External; semantics can be richly described, and episodic details can be impoverished and sparse.

## Classification of details: Sub-Categories

For a scoring protocol that separates Internal details into event, place, spatial orientation, time, duration/sequence, visual
(non-spatial), perceptual (non-visual), emotion/thought subcategories, see Martin, V.C. (2013) Memory for the Future:

#### The Encoding and Phenomenology of Episodic Simulations. PhD Thesis, University of Auckland (available on request)


### Internal Sub-Categories

#### Internal-Event (I_Eve): Details that describe the unfolding of the event

- Entities:
    o A particular individual (person/pet) that can be identified/referred to in some way (e.g., by name,
       relationship, descriptor phrase); up to a maximum of 5 individuals can be scored
    o Particular exemplars (my blue cup) or a category of objects (there were chairs) that are
       involved in the event/action – up to a maximum of 5 object exemplars/categories can be scored
    o Absence of an entity, e.g., Bob didn’t attend; her hand was empty
    o The participant’s own clothing if it is part of the action, e.g., It tore my shirt
- Happenings:
    o Happenings, physical occurrences, actions of the speaker or others, e.g., I fell down; It was my
       birthday; He jumped out of the chair
    o Absence of an action or happening if this conveys information about what actually occurred, e.g., He
       didn’t hit the ground;
    o Reactions/emotions in other people, e.g., She was jealous; He thought I was awful
    o Dialogue – the participant’s own dialogue, and the dialogue of others e.g., Mary said hello
    o Temporal sequence of events, e.g., Mary got there later; Sam arrived next
    o Weather, e.g. It was sunny; it was stormy
- Exceptions:
    o The participant’s own self cannot be counted as an entity (e.g., I, me). It should be collapsed into
       whatever detail the pronoun refers to (e.g., an action, a perception) and scored accordingly
    o The participant’s own reactions/emotions are scored as Internal-Emotions/Thoughts
    o The participant’s own clothing that is not involved in the action is scored as Internal-Perceptual
    o Once the maximum number of entities has been reached, newly introduced individuals (6 and up) or
       objects (6 and up) are not segmented/scored separately but are subsumed into an accompanying detail.
       However, if they are clearly using a “listing” strategy that relies on semantics (e.g., listing all objects in a
       kitchen; listing all their family members) then individuals (6 and up) and/or objects (6 and up) can be
       scored as External-Semantic-Personal or External-Semantic-General as appropriate.
- SCORING RULE 2: If a detail qualifies to be in another category (e.g., Internal-P erceptual) priority is
    given to that more specific category

#### Internal-Place (I_Pla): Details providing orientation (of participant) in geographic space during the event

- Locale (e.g., country, body of water, province/state, city, street)
- Outside locations (e.g., a particular park, yard, sidewalk, restaurant patio) including distinct areas within a given
    location (e.g., the slope vs. the playground at the same park)
- Inside locations (e.g., a particular building, rooms, and locations within a room)
- Exceptions:
    o The participant’s own orientation in space (e.g., I was to the right of him) is scored as
       Internal-P erceptual

#### Internal-Time (I_Tim): Details that provide orientation of the participant in time during the event

- The participant’s chronological age at the time of the event, e.g., My twenties; I was 25 then
- The period of the participant’s life, e.g., When I worked at Walmart, or another person’s life, e.g.,
    This was after she had kids
- Calendar time (e.g., year, season, month, date, day of week, time of day, clock time); may provide more than
    one of these details, e.g., it was last Wednesday, in the morning [2 details]
- Information about sequences of events (e.g., Sam arrived next) are Internal-E vent details
- Note: People often infer this temporal information in relation to other events or occurrences (Tulving, 1972).
    Although inferences are typically scored as External-Other details, time-related inferences are scored as
    Internal-Time as this is a natural way of recovering temporal information.


#### Internal-Perceptual (I_Per): Details related directly to information perceived during the event

- The participant’s own physical self, e.g., I sounded hoarse; I looked tanned
- Visual details, including colours, entities (i.e., beings/objects including others’ clothing) that is part of the visual
    landscape/scene, e.g., There were lit candles everywhere; She wore a black lacey
    shirt; the park was full of dogs)
- Other sensory details (i.e., auditory, olfactory, tactile/pain, taste), e.g., I smelled lavender
- Spatial details about positions, distances, depths, and orientations in allocentric/egocentric space (i.e., one's own
    orientation in space) e.g., I was to the right of him; about a centimeter
- Temporal details about the perception of time during the event (i.e., duration), e.g., We were there for
    20 minutes; It took a long time
- Exceptions:
    o Temporal sequence of events are scored as Internal-Event
    o Objects directly involved in the unfolding of an event are scored as Internal-E vent
       (e.g., We lit the candles)

#### Internal-Emotion/Thought (I_Em/T): Details pertaining to the participant’s mental state during the event

- Mental content or states (feelings/emotions, thoughts, opinions, preferences, expectations, beliefs) experienced
    during the event (e.g., I thought he was lovely; I appreciated she was on time)
- If the participant’s own mental state refers to that of others during the event, it is scored as Internal-
    Emotion/Thought
       o If the participant assumes that their own mental state was also shared with others (e.g., we all
          thought ‘that’s enough!’; we were scared), score by applying RULE 2 (i.e., one’s
          own reaction is Emotion/Thought while the reactions of others are Event details, so default to the more
          specific category and score as Internal-Emotion/Thought)
       o If the participant’s own mental state at the time reflected an inference about someone else’s mental state
          (I thought he was angry with me), score as Internal-Emotion/Thought.
       o In either case, if the participant also describes an outward expression of others’ person’s mental state,
          the reaction itself is scored as Internal-Event
- Exceptions:
    o Inferences about other people's mental state at the time of the event (e.g., She was sad) are scored
       as Internal-Event unless these inferences reflect the participant’s own mental state at the time ("I
       thought he was angry with me"), in which case they are internal thought details.
    o Emotion/thoughts expressed in retrospect, either at the time of the interview (e.g., It makes me
       smile to think of it) or at any time after the event occurred (e.g., I was sad for ages;
       I found out later I was wrong) are scored as External-Metacognitive
    o Beliefs, opinions, or preferences that are long-standing (i.e., not specific to, or exist beyond, the
       duration of the event) are scored as External-Semantic. This pertains to the participant’s own beliefs and
opinions, e.g., I never believed in ghosts (External-Semantic-Personal), as well as the
long-standing beliefs/opinions of close others, e.g., Mum hates mushrooms (External-Semantic-
Personal) or distant/public others, e.g., Madonna has always hated jazz (External-
Semantic-General)

### External Sub-Categories

#### External-General Semantics (E_GS): Knowledge that is culturally-shared with others in the same community

- Concepts (e.g., introverts aren’t necessarily shy)
- Facts (e.g., Paris is the capital of France)
- Opinions/beliefs/attributes of people in the public domain (e.g., Madonna hates jazz)
- Shared by the same “community” refers to community at any level that is relevant (e.g., neighbourhood, city,
    country). The critical point is that the knowledge is not personal and thus it can generally assumed that strangers


```
will have this same knowledge by virtue of being exposed to the same information/experiences in that
community
```
- Usually reflects long-standing knowledge or state (i.e., exist beyond the duration of the event), and/or often do
    not have a clear beginning or end
- Can also include entities once maximum numbers have been reached (i.e., individuals 5 & up, objects 5 & up)
    IF the participant is clearly using a listing strategy reliant on general semantics (e.g., items found in a kitchen).
- Exceptions:
    o Even if the detail appears to be semantic according to the above criteria, if the detail is clearly
       integral to the main event, it is scored as Internal as per RULE 1 (‘benefit of the doubt’ rule)
    o e.g., Arizona is hot, it was 110F is Internal-Perceptual; We watched as Paris
       fell to the Germans is Internal-Event; I remember when the tour guide said
       that ... is Internal-Event)

#### External-Personal Semantics (E_PS): Knowledge that is specific to the participant and close others

- Self-knowledge: Personal about the participant’s own self
    o Includes self-descriptions/evaluations, traits, beliefs, preferences, opinions, etc.,
       e.g., I always hated that kind of thing
    o Long-standing knowledge (i.e., not tied to a specific event)
    o Usually only known to the participant themselves and/or close others they have shared this knowledge
       with (i.e., it is not widely known and certainly not culturally-shared)
- Autobiographical facts: Facts about the participant’s own self/life or the self/life of their close others
    o Details that are part of one’s personal time line or a skeletal framework of a life story
    o Includes names and dates of places lived, schooling, employment, major relationships, etc.
       e.g., I got an MSc in Psychology; I was an engineer; We married in 1980
    o This knowledge may be known to others beyond the self/close others (e.g., employers, associates)
- Close-Other: The above forms of knowledge but in reference to a close other (e.g., friends and family) rather
    than the self, following the same guidelines as above
       o e.g., Mum and Dad got married in 1980; My sister always hated dancing
- Can also include entities once maximum numbers have been reached (i.e., individuals 5 & up, objects 5 & up)
    IF the participant is clearly using a listing strategy reliant on general semantics (e.g., names of school friends).
- Note: It may be useful in some studies to modify coding labels to differentiate between these two forms of
    personal semantic knowledge (e.g., External-PS-SelfK; External-PS-AFacts; External-PS-Oth)

#### External-Event-Episodic (E_Epi): Details pertaining to specific episodic events other than the main event

- Details pertaining to any specific episodic events other than the main event
- Note: It may be useful in some studies to modify coding labels to distinguish any events additional to the main
    event and indicate the Internal sub-categories (e.g., External-Event2-Time)
- e.g., If the main event is imagining the birth of their child (code: Internal), but they also describe finding out
    they’re pregnant (External-Event2) and having an ultrasound (External-Event3) and so on.

#### External-Event-Generic (E_Gen): Internal details from non-specific events

- Details pertaining to events that are repeated over time such as routines, e.g., I always shop there; I
    usually drive this way to work
- Details pertaining to events that are extended in time, e.g., I had a 3-week vacation in Fiji
- Use of words such as always and usually are good indications that the event is generic
- Note: It may be useful in some studies to modify coding labels to distinguish the type of generic event (e.g.,
    External-Event-Repeated; External-Event-Extended). In this case, if an event is both repeated and extended
    (e.g., a week-long yacht race which the subject participated in every year) it should be coded as Repeated.


#### External-Repetitions (E_Rep): Details that are unsolicited repetitions of details given elsewhere in the event

- Any information contained in another detail given elsewhere in the response
- It does not have to be a verbatim repetition, but it should not add any new information to the other detail
    o e.g., I hoped for the best and I crossed my fingers convey the same information
    o e.g., They liked what I did and They liked my work convey the same information
    o e.g., My boss liked me and My boss was happy with me does not constitute a repetition
    o e.g., I helped them and They could depend on me does not constitute a repetition
- Exceptions:
    o Must be unsolicited. If a repetition is directly solicited or prompted by the experimenter (e.g., the
       repetition is provided in response to a question from the experimenter) it should not be scored as a
       repetition but as External-Other
    o Must convey information, i.e., individual words that are repeated are not scored as repetitions.
       Likewise, a repeated noun is not scored as repetition if the participant has to say which noun they are
       referring to (e.g., which entity is acting) in order to make sense. (These are treated as partial details).

#### External-Other (E_Oth): Details that are not related to memory/imagination and/or don’t fit another category

- Meta-cognitive statements reflecting current cognition, e.g., Let me see if I can remember that
- Editorializing comments, e.g., Oh actually that doesn't matter; That was a tangent!
- Inferences made in the present or since the event occurred, e.g., I must have been wearing a coat
    because it was winter
- Any other statements that convey verbosity but are not related to the main event
- Replies to a queries from the experimenter
- Exceptions:
    o Single-word reflexive responses to questions, e.g., No. These are not scored
    o Utterances that do not contain information, e.g., um. These are not scored
    o Inferences about when the event happened – these are scored as Internal-Time as this is a natural way of
       recovering temporal information about an event


## Appendix A:

## Segmentation Cheat-Sheet

#### SEGMENTATION RULE & DEFINITION THINGS TO NOTE

```
Partial
Details
```
```
RULE: If a word/phrase does not convey any additional information in-of-itself (without the rest
of the phrase/sentence), it should be subsumed into an accompanying detail
```
▪ A word/phrase that doesn’t convey additional information
in-of-itself and is subsumed into an accompanying detail

▪ Applies to verbs that (usually) don’t convey sufficient
meaning in-of-themselves
▪ Once max. numbers of entities are exceeded, other newly
introduced entities are NOT scored but subsumed into
accompanying detail

▪ Applies to 6th + individuals and to 6th^ + object
exemplars/categories introduced into event
▪ Exception: A semantic listing strategy is being used
(then segment each applicable entity separately)
▪ Participant’s own self is never segmented as an entity ▪ e.g., “I”, “me”, referring to self in 3rd person
▪ Repeated nouns (entities, locations) are usually
considered partial details – see below.

```
▪ See rule for Repeated Nouns below.
```
```
Adjectives RULE: If an adjective adds information in-of-itself, it can be segmented into a separate detail
```
▪ If an adjective adds perceptual detail, segment and score
as an additional detail

▪ Applies to perceptual qualifiers (e.g., quantities,
amounts, sizes, degrees, colours)
▪ Does NOT apply when adjective is used as an integral
part of the detail (and is not an additional detail)

```
▪ E.g., the following examples are all ONE detail:
```
- Time approximations (“few weeks”); Colours (“light
blue”); Emotions (“really very mad”); Relationships
(“best friend”); Weather (“light rain”)
Multi-word
descriptors

```
RULE: If you can substitute a multi-word phrase for a single word/concept/entity without
changing the meaning of what is being conveyed, then it's likely ONE detail.
```
▪ If a single word/concept/entity can substitute for a multi-
word phrase without changing the meaning, it's ONE
detail

```
▪ Applies to single OR multiple entities referred to by
descriptive phrases (segment number of entities
accordingly)
▪ Applies to sayings/turns of phrase, circumlocution
```
```
Dialogue /
Thoughts
```
```
RULE: Segment dialogue/thoughts by dividing the text reasonably into phrases or sentences,
whether its dialogue/thoughts in the event (Internal) OR in the interview itself (External Other:
dialogue with interviewer, meta-cognitive thoughts, editorializing comments)
```
▪ Segment runs of dialogue/thoughts by dividing the text
reasonably into phrases or sentences (e.g., thought/speech
bubbles)

```
▪ Applies to dialogue/thoughts in the event (Internal) OR
interview (External-Other: dialogue with interviewer,
meta-cognitive thoughts, editorializing comments)
Repeated
nouns
```
```
RULE: A repeated noun is segmented as a partial details (not a repetition) and subsumed into
accompanying detail UNLESS noun is sufficiently different so as to add new information
```
▪ A noun is only segmented once for scoring; if mentioned
elsewhere, then it is treated as a partial detail and
subsumed into an accompanying detail

```
▪ Applies when noun must be repeated to indicate what is
being referred to (thus not a true repetition)
▪ Exception: if another mention adds new information
(e.g., relationship; sufficient different name/pronoun)
Repeated
phrases
```
```
RULE: A phrase is only scored once for its meaning so if already mentioned elsewhere, segment
phrase and score as a Repetition.
```
▪ If a phrase means the same thing as another phrase used
elsewhere, score as a repetition

```
▪ Can include different sayings that convey same meaning
▪ Must contain information (otherwise might be partial)
Other segmentation tips
```
▪ If cue is repeated at start of response: Ignore if reflexive repetition; score if meta-cognitive or part of the response
▪ Segmentation should be consistent whether Internal or External (abiding by rules for partial/repeated details)


## Appendix B:

## AI Scoring Cheat-Sheet

#### INTERNAL DETAILS

```
RULE 1 Benefit of the doubt: If a detail can reasonably (not just possibly) refer to main event, score it as Internal
```
Subcategory Definition Things to note

Event
(who/what/ how)

```
How the event unfolds, including the
entities present and the happenings
(e.g., occurrences, actions)
```
```
▪ Includes temporal sequence of events, weather, etc.
▪ Each entity only scored once, up to a max. 5 individuals +
max. 5 object exemplars/categories; Additional entities treated
as partial details (unless listing strategy is used)
▪ Self can’t be counted as an entity
RULE 2 Classify in other Internal sub-category if possible
```
Place (where) Orientation (of participant) in
geographic space during the event

```
▪ Excludes participant’s own orientation in space
▪ Includes places within a location (e.g., particular area of park)
```
Time (when) Orientation (of participant)^ in time
during the event

```
▪ Includes inferences about when the event happened
▪ Excludes temporal sequence of events or durations
```
Perceptual

```
Participant’s own perceptions
(physical self, sensory, spatial,
temporal) during the event
```
```
▪ Includes perceived temporal durations
▪ Includes participant’s own orientation in space
▪ Excludes objects directly involved in the unfolding of event
```
Emotion /
Thought

```
Participant’s own mental state during
the event: feelings/emotions,
thoughts, opinions, preferences,
expectations, beliefs
```
```
▪ Includes participant’s own mental state even if it is shared with
others or it refers to the mental state of others;
▪ Excludes details related to outward expression of another’s
mental state (e.g., their reaction)
▪ Excludes emotions/thoughts at another time, or that are long-
standing and exist beyond the event
EXTERNAL DETAILS
```
Subcategory Definition Things to note

General
Semantics

```
General knowledge or facts that are
long-standing (not tied to a specific
event) and culturally-shared with
one’s in-group
```
```
▪ Includes knowledge about famous people in the public domain
(including facts about them, their opinions, preferences, etc.)
▪ Excludes details integral to main event (score as Internal)
▪ Can include individuals or objects (5 and up) if listing strategy
```
Personal
Semantics

```
Self-knowledge and facts about
participant’s self & close others
(family/friends) that are long-
standing and not culturally-shared
```
```
▪ Self-knowledge includes traits, beliefs, preferences, opinions
and other info only known privately to self and/or close-others
▪ Autobio facts comprise personal timeline or factual skeleton of
life story (names/dates of residences, work, relationships, etc.)
that may be known by other associates (e.g., boss)
▪ Can be coded to indicate type (External-PS -SelfK or -AFacts)
▪ Can include individuals or objects (5 and up) if listing strategy
```
Event-
Episodic

```
Events experienced by the participant
that are specific in time and place but
secondary to the main event
```
```
▪ Can additionally code according to Internal subcategories
▪ Can also distinguish separate events in your coding labels
(e.g., External-Event2-Time)
```
Event-
Generic

```
Non-specific events experienced by
the participant that are repeated or
extended
```
```
▪ Use of “always”, “usually”, “we would [always] go” can
indicate repeated event
▪ Can be coded to indicate type (e.g., -Repeated, - Extended)
```
Repetition

```
Repetition of information already
conveyed in another detail
```
```
▪ Unsolicited (score as Other if given in response to interviewer)
▪ Does not have to be verbatim if conveys the same meaning
```
Other

```
Details unrelated to memory /
simulation; don’t fit other categories
(e.g., meta-cognitive, editorializing,
inferences, replies to questions)
```
```
▪ These details must contain information
▪ Excludes meaningless utterances (um)
▪ Excludes simple reflexive responses (Yes/No)
▪ Excludes inferences about when the event happened
```

