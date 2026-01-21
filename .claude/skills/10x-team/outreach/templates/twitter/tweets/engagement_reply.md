---
name: Engagement Reply
type: reply
max_length: 280
description: Reply to engage with someone's tweet
tags: [engagement, reply, visibility]
---
{{ response | default("This is spot on") }} {{ first_name | default("") }}! {{ insight | default("") }}

{{ additional | default("Would add: " + (point | default("[your insight]"))) }}
