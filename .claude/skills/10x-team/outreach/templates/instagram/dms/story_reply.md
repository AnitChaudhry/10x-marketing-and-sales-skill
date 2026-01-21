---
name: Story Reply DM
type: dm
max_length: 1000
description: Reply to someone's Instagram story
tags: [warm, story, engagement, ice-breaker]
---
{{ reaction | default("Omg") }} {{ story_content | default("this") }}! 🔥

{{ follow_up | default("Where was this?") }} {{ or_comment | default("") }}

{{ personal_connection | default("I've been wanting to try something similar!") }}
