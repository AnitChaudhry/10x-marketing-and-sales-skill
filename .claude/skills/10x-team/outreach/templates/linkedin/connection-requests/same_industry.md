---
name: Same Industry
type: connection_request
max_length: 300
description: Connect with someone in the same industry
tags: [industry, peers, networking]
---
Hi {{ first_name }},

Fellow {{ industry | default("tech") }} professional here! I've been following your insights on {{ recent_post | default("the industry") }} and would love to connect with like-minded people.

{{ my_name }}
