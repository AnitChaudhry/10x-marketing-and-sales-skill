---
name: Expert Consultation Request
type: dm
max_length: 10000
description: Request expert consultation
tags: [expert, consultation, advice]
---
Hey {{ first_name }}!

Your expertise on {{ topic | default("this subject") }} is incredible. I've learned a lot from your tweets.

I'm currently working through {{ challenge | default("a specific challenge") }} and could really use expert guidance.

{{ ask | default("Would you be open to a paid consultation call?") }} I'd value 30 mins of your time to discuss {{ specific_topic | default("strategy") }}.

Let me know if you're interested!
