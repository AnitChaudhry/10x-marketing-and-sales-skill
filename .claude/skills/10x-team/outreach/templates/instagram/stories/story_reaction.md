---
name: Story Reaction Follow-up
type: dm
max_length: 1000
description: Follow up after reacting to their story
tags: [story, reaction, follow-up]
---
{{ opening | default("Had to react to that story") }} {{ emoji | default("😂") }}

{{ comment | default("That was too good!") }}

{{ question | default("Do you have more content like that?") }}
