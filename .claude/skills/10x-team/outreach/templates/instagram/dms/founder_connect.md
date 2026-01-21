---
name: Founder Connection
type: dm
max_length: 1000
description: Connect with startup founders on Instagram
tags: [founder, startup, networking]
---
Hey {{ first_name | default("") }}!

{{ opening | default("Saw your posts about") }} {{ company | default("your startup") }} - {{ compliment | default("love what you're building") }}!

{{ connection | default("As a fellow founder, I know the journey") }}. {{ value | default("Would love to connect and share experiences") }}.

{{ cta | default("Open to connecting?") }}

- {{ my_name }}
