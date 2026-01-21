---
name: Sales Introduction
type: message
max_length: 8000
description: Soft sales introduction message
tags: [sales, intro, b2b]
---
Hi {{ first_name }},

Great to be connected! I noticed {{ company }} is {{ company_situation | default("growing rapidly") }} - congrats on the momentum!

Quick question: {{ pain_point_question | default("Are you currently looking to improve your team's productivity?") }}

We've helped companies like {{ similar_company | default("others in your industry") }} achieve {{ result | default("significant improvements") }}, and I thought it might be relevant for you.

No pressure at all - just curious if it's something worth exploring.

{{ my_name }}
