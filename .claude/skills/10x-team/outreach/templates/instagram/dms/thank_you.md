---
name: Thank You DM
type: dm
max_length: 1000
description: Thank someone after interaction
tags: [thank-you, gratitude, relationship]
---
Hey {{ first_name | default("") }}! 💫

Just wanted to say thank you for {{ reason | default("the support") }}! {{ impact | default("It really means a lot.") }}

{{ custom_message | default("People like you make this community amazing.") }} 🙏

{{ closing | default("Looking forward to more interactions!") }} ✨
