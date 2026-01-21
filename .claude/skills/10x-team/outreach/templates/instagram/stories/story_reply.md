---
name: Story Reply
type: story_reply
max_length: 1000
description: Reply to someone's story
tags: [story, engagement, ice-breaker]
---
{{ reaction | default("Okay this is fire") }} {{ emoji | default("🔥🔥") }}

{{ question_or_comment | default("Where is this??") }}
