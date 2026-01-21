---
name: Cold DM
type: dm
max_length: 1000
description: Cold outreach via Instagram DM
tags: [cold, outreach, first-contact]
---
Hey {{ first_name | default("") }}! 👋

{{ opening | default("I came across your profile and love") }} {{ what_you_like | default("what you're creating") }}! {{ specific_compliment | default("Your content really stands out.") }}

{{ custom_message | default("Wanted to reach out because I think we have some things in common.") }}

{{ cta | default("Would love to connect!") }} ✨

- {{ my_name }}
