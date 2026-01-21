---
name: Investor Introduction
type: dm
max_length: 10000
description: DM to potential investors
tags: [investor, funding, startup]
---
Hi {{ first_name }},

I'm the founder of {{ company | default("a startup") }} - we're {{ traction | default("building something exciting in the space") }}.

I noticed you invest in {{ investment_thesis | default("companies like ours") }} and thought there might be a fit.

{{ ask | default("Would you be open to learning more?") }}

Happy to send over a deck or jump on a quick call.

- {{ my_name }}
