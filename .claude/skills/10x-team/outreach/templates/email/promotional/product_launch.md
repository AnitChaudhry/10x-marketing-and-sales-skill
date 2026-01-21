---
name: Product Launch
type: promotional
subject: "{{ subject | default('Introducing ' + (product_name | default('[Product Name]'))) }}"
description: Announce a new product launch
tags: [promotional, launch, announcement]
---
Hi {{ first_name }},

{{ excitement | default("We're thrilled to announce something we've been working on for months...") }}

**Introducing {{ product_name | default("[Product Name]") }}** {{ emoji | default("🚀") }}

{{ description | default("[Brief description of what it does and why it matters]") }}

**Key Features:**
{{ features | default("- [Feature 1]\n- [Feature 2]\n- [Feature 3]") }}

{{ why_now | default("We built this because " + (reason | default("[reason]")) + ".") }}

**{{ offer | default("Special Launch Offer") }}:**
{{ offer_details | default("[Details of any launch pricing or exclusive access]") }}

{{ cta | default("[Check it out here](" + (link | default("[link]")) + ")") }}

{{ closing | default("We can't wait to hear what you think!") }}

{{ my_name }}
{{ my_company | default("") }}

{{ ps | default("") }}
