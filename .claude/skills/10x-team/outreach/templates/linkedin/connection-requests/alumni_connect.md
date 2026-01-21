---
name: Alumni Connection
type: connection_request
max_length: 300
description: Connect with fellow alumni
tags: [alumni, university, networking]
---
Hi {{ first_name }},

I noticed we're both {{ school_name | default("alumni from the same school") }}! Always great to connect with fellow {{ degree_type | default("graduates") }}.

I'm currently {{ current_role | default("exploring new opportunities") }} and would love to expand my network with fellow alumni.

{{ my_name }}
