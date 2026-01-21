---
name: Cold DM
type: dm
max_length: 10000
description: Cold outreach via Twitter DM
tags: [cold, outreach, first-contact]
---
Hey {{ first_name | default(name | default("")) }}! 👋

{{ opening | default("I've been following your content and really appreciate your takes on") }} {{ topic | default("the industry") }}.

{{ custom_message | default("Wanted to reach out because I think we're working on similar things and could have an interesting conversation.") }}

{{ cta | default("Would love to connect if you're open to it!") }}

- {{ my_name }}
