---
name: Influencer Outreach
type: dm
max_length: 10000
description: Outreach to influencers for collaboration
tags: [influencer, collaboration, partnership]
---
Hey {{ first_name }}!

Love your content on {{ topic | default("X") }}. {{ specific_compliment | default("Your engagement with the community is amazing") }}.

I'm working on {{ my_project | default("something") }} that I think would resonate with your audience:
{{ value_prop | default("A new way to help people achieve their goals.") }}

{{ collaboration_ask | default("Would you be interested in exploring a collaboration?") }}

Happy to share more details!
