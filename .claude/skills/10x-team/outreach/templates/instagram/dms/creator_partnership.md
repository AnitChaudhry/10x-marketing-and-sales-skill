---
name: Creator Partnership
type: dm
max_length: 1000
description: Partnership outreach to content creators
tags: [creator, partnership, content]
---
Hey {{ first_name | default("") }}!

{{ compliment | default("Your content is incredible") }} - especially {{ specific_content | default("your recent posts") }}!

I'm a {{ my_role | default("fellow creator") }} and I think our audiences would love a collab. {{ idea | default("Maybe a joint post or Instagram Live?") }}

{{ cta | default("Would you be down to chat about it?") }}

Let me know!
