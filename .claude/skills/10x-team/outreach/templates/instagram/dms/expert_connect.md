---
name: Expert Connection
type: dm
max_length: 1000
description: Connect with industry experts
tags: [expert, networking, professional]
---
Hi {{ first_name | default("") }}!

{{ opening | default("Your expertise in") }} {{ field | default("this field") }} {{ compliment | default("is really impressive") }}. I've learned so much from your content!

{{ my_situation | default("I'm working on something similar and would love to connect") }}.

{{ ask | default("Any chance you'd be open to a quick chat?") }}

Thanks!
- {{ my_name }}
