---
name: Founder Outreach DM
type: dm
max_length: 10000
description: DM to startup founders
tags: [founder, startup, outreach]
---
Hey {{ first_name }}!

Been following {{ company | default("your startup") }}'s journey - {{ compliment | default("really impressive what you're building") }}!

{{ context | default("As a fellow builder, I know how hard the founder journey is.") }}

{{ value_prop | default("Would love to chat about what you're working on.") }}

{{ cta | default("Open to a quick conversation?") }}
