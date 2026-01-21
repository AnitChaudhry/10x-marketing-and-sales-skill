---
name: Influencer Outreach
type: dm
max_length: 1000
description: Outreach to influencers for collaboration
tags: [influencer, collaboration, partnership]
---
Hey {{ first_name | default("") }}!

{{ opening | default("I've been following your content and") }} {{ compliment | default("love what you're creating") }}! Your {{ content_type | default("posts") }} about {{ topic | default("lifestyle") }} really stand out.

I'm with {{ company | default("a brand") }} and we think you'd be a perfect fit for {{ opportunity | default("a collaboration") }}.

{{ cta | default("Would you be interested in learning more?") }}

- {{ my_name }}
