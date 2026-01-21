---
name: After Follow DM
type: dm
max_length: 10000
description: Message after following someone
tags: [warm, follow-up, introduction]
delay_after_follow: 2-4 hours
---
Hey {{ first_name | default("") }}!

Just followed you - {{ reason | default("your content on " + (topic | default("this space")) + " is great") }}.

{{ custom_message | default("Looking forward to your future posts!") }}

{{ question | default("What got you interested in this area?") }}
