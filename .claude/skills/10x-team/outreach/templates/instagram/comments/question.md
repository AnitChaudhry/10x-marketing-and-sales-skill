---
name: Question Comment
type: comment
max_length: 2200
description: Ask a question to start conversation
tags: [question, engagement, conversation]
---
{{ reaction | default("Love this!") }} {{ emoji | default("🔥") }} {{ question | default("Where was this taken?") }}

{{ follow_up | default("") }}
