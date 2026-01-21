---
name: Brand Collaboration
type: dm
max_length: 1000
description: Propose brand collaboration
tags: [brand, collaboration, business]
---
Hi {{ first_name | default("") }}!

{{ opening | default("Your brand aesthetic is amazing") }}! I'm reaching out from {{ company | default("a company") }} about a potential collaboration.

{{ value_prop | default("We have a product/service that aligns perfectly with your audience") }}.

{{ offer | default("We'd love to explore a partnership - sponsored post, story feature, or giveaway") }}.

{{ cta | default("Interested in discussing details?") }}

- {{ my_name }}
