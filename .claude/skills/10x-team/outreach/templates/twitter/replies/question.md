---
name: Question Reply
type: reply
max_length: 280
description: Ask a thoughtful question
tags: [question, engagement, curiosity]
---
{{ context | default("Interesting take!") }} {{ question | default("Curious - how do you see this playing out for [specific scenario]?") }}
