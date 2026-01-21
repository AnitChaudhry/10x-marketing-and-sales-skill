---
name: Discount Offer
type: promotional
subject: "{{ subject | default((discount | default('20%')) + ' off for ' + (first_name | default('you'))) }}"
description: Send a discount or special offer
tags: [promotional, discount, offer, sales]
---
Hi {{ first_name }},

{{ opening | default("I wanted to share something special with you...") }}

**{{ offer_headline | default("Get " + (discount | default("20%")) + " off " + (product | default("[product/service]"))) }}**

{{ reason | default("As a thank you for " + (reason_detail | default("[being a subscriber/customer/etc]")) + ".") }}

**What you get:**
{{ details | default("- Full access to [product/service]\n- [Benefit 1]\n- [Benefit 2]") }}

**Use code: `{{ discount_code | default("SPECIAL20") }}`**

{{ urgency | default("⏰ Offer expires " + (expiry | default("[date]")) + ".") }}

{{ cta | default("[Claim your discount →](" + (link | default("[link]")) + ")") }}

{{ closing | default("Don't miss out!") }}

{{ my_name }}

{{ ps | default("P.S. This offer is exclusive to our email list - feel free to share with a friend!") }}
