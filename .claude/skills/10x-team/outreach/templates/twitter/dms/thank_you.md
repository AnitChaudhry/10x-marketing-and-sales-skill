---
name: Thank You DM
type: dm
max_length: 10000
description: Thank someone after interaction
tags: [thank-you, gratitude, relationship]
---
Hey {{ first_name | default("") }}!

Just wanted to say thanks for {{ reason | default("the interaction") }}. {{ impact | default("Really appreciated your perspective.") }}

{{ custom_message | default("It's great connecting with thoughtful people on here.") }}

{{ closing | default("Looking forward to more conversations!") }} 🙏
