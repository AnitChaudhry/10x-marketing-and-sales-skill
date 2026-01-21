---
name: Mutual Follower
type: dm
max_length: 10000
description: Message someone who mutually follows
tags: [warm, mutual, networking]
---
Hey {{ first_name | default("") }}! 👋

Noticed we follow each other - {{ observation | default("seems like we're both into " + (topic | default("similar things"))) }}.

{{ custom_message | default("Would be cool to chat sometime about what we're both working on.") }}

{{ cta | default("What's keeping you busy these days?") }}
