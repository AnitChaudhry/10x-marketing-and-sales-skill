---
name: Expertise Request
type: message
max_length: 8000
description: Request expert advice or insight
tags: [expert, advice, learning]
---
Hi {{ first_name }},

I've been following your work on {{ topic | default("the industry") }} and you clearly have deep expertise in this area.

I'm currently {{ my_situation | default("working on a project") }} and facing a challenge related to {{ challenge | default("scaling effectively") }}.

Would you have 15-20 minutes for a quick call? I'd love to get your perspective on {{ specific_question | default("how you've approached similar challenges") }}.

Happy to compensate for your time if that's more appropriate.

Thanks for considering!
{{ my_name }}
