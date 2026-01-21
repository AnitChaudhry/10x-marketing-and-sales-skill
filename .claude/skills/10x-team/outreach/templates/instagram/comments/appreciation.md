---
name: Appreciation Comment
type: comment
max_length: 2200
description: Show appreciation for content
tags: [appreciation, support, engagement]
---
{{ appreciation | default("This is amazing") }}! {{ specific | default("Love the way you explained this") }}. {{ action | default("Definitely saving this for later") }}. {{ emoji | default("") }}
