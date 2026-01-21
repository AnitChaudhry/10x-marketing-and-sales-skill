---
name: Value Add Comment
type: comment
max_length: 2200
description: Add valuable insight to a post
tags: [engagement, value, insight]
---
{{ insight | default("This is so true!") }} {{ addition | default("I'd also add that") }} {{ specific_point | default("consistency is key") }}. {{ emoji | default("") }}
