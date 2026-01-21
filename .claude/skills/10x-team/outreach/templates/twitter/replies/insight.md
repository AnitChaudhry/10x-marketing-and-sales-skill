---
name: Insight Reply
type: reply
max_length: 280
description: Share a unique insight or perspective
tags: [insight, perspective, thought-leadership]
---
{{ framing | default("Another angle:") }} {{ insight | default("[Your unique perspective]") }}

{{ supporting_point | default("") }}
