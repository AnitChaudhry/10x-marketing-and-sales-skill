---
name: Mention Tweet
type: tweet
max_length: 280
description: Tweet that mentions someone
tags: [mention, engagement, tag]
---
{{ handle }} {{ context | default("made a great point about") }} {{ topic | default("this") }}.

{{ your_addition | default("I'd add: [your insight]") }}

{{ cta | default("Thoughts?") }}
