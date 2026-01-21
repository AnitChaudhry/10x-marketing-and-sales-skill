---
name: Referral Request
type: message
max_length: 8000
description: Ask for a referral or introduction
tags: [referral, networking, intro]
---
Hi {{ first_name }},

Hope you're doing well! I'm reaching out because I'm looking to connect with {{ target_role | default("decision makers") }} at {{ target_type | default("companies in the tech space") }}.

Given your network, I was wondering if you might know anyone who fits this profile:
{{ ideal_profile | default("- Someone interested in improving their operations") }}

I'd really appreciate any introductions you might be able to make. Of course, happy to return the favor anytime!

Thanks so much,
{{ my_name }}
