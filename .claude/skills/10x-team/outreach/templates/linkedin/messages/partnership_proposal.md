---
name: Partnership Proposal
type: message
max_length: 8000
description: Propose a partnership after connecting
tags: [partnership, business, proposal]
---
Hi {{ first_name }},

Thanks for connecting! I've been following {{ company }}'s journey and I'm impressed by {{ achievement | default("what you've built") }}.

I'm reaching out because I believe there's a strong synergy between our work:

{{ partnership_details | default("We both serve similar audiences and could create significant value together.") }}

{{ specific_ask | default("Would you be open to a quick call to explore this?") }}

Looking forward to hearing your thoughts!

Best,
{{ my_name }}
