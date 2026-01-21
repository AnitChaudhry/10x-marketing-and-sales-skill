---
name: Thank You
type: message
max_length: 8000
description: Express gratitude after interaction
tags: [thank-you, gratitude, follow-up]
---
Hi {{ first_name }},

Just wanted to say thank you for {{ reason | default("taking the time to connect") }}.

{{ custom_message | default("Your insights were really valuable and gave me a lot to think about.") }}

I'll definitely {{ action | default("keep you posted on how things develop") }}. Looking forward to staying in touch!

Best,
{{ my_name }}
