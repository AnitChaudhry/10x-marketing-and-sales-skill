---
name: Warm Introduction
type: warm_email
subject: "{{ subject | default((mutual_connection | default('A friend')) + ' suggested I reach out') }}"
description: Email when you have a warm introduction
tags: [warm, referral, introduction]
---
Hi {{ first_name }},

{{ mutual_connection | default("[Mutual connection]") }} suggested I reach out to you. {{ context | default("They mentioned you might be interested in what we're working on.") }}

{{ about_me | default("I'm " + (my_name | default("[Name]")) + " from " + (my_company | default("[Company]")) + ".") }} {{ relevant_background | default("We specialize in " + (specialty | default("[area]")) + ".") }}

{{ reason_for_reaching_out | default("Based on what [mutual connection] shared, I think there could be some interesting synergies between what we're both doing.") }}

{{ cta | default("Would you have 15 minutes for a quick call this week or next?") }}

Looking forward to connecting!

Best,
{{ my_name }}
