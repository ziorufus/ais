This is an Italian author description of a future event. I need to extract events from this text, following both the original guidelines for English.
Can you extract the events, marking the event label and the event span of text taken from the description? Please give me the data in JSON format following this template:

```
{
  [
    "text": "The span of text",
    "type": "The label"
  ],
  ...
}
```

Use these labels:
  * I_Eve -> Internal-Event
  * I_Pla -> Internal-Place
  * I_Tim -> Internal-Time
  * I_Per -> Internal-Perceptual
  * I_Em/T -> Internal-Emotion/Thought
  * E_GS -> External-General Semantics
  * E_PS -> External-Personal Semantics
  * E_Epi -> External-Event-Episodic
  * E_Gen -> External-Event-Generic
  * E_Rep -> External-Repetitions
  * E_Oth -> External-Other

To help you with this task, I'm attaching the guidelines.
Just answer me with the annotations JSON for this text:

{{TEXT}}

# GUIDELINES

{{GUIDELINES}}

