---
name: Collaboration Request
type: dm
max_length: 10000
description: Propose collaboration via DM
tags: [collaboration, partnership, business]
---
Hey {{ first_name | default("") }}!

Big fan of your work on {{ their_work | default("this space") }}. {{ compliment | default("Your content really stands out.") }}

{{ proposal | default("I had an idea for something we could potentially work on together:") }}

{{ collaboration_details | default("- A Twitter Space discussion\n- A thread collaboration\n- Sharing each other's content") }}

{{ cta | default("Would you be interested in exploring this?") }}

- {{ my_name }}
