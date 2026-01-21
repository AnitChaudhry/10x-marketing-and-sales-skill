---
name: Partnership Proposal
type: partnership
subject: "{{ subject | default('Partnership idea: ' + (my_company | default('[Your Company]')) + ' + ' + (company | default('[Their Company]'))) }}"
description: Propose a partnership or collaboration
tags: [partnership, collaboration, b2b]
---
Hi {{ first_name }},

{{ opening | default("I've been following " + (company | default("[company]")) + "'s growth and am impressed by " + (impressive_thing | default("what you've achieved")) + ".") }}

{{ partnership_context | default("At " + (my_company | default("[company]")) + ", we work with companies in " + (industry | default("your space")) + " and I see a potential fit.") }}

**Partnership Idea:**
{{ partnership_proposal | default("I'm thinking we could explore:\n\n- [Partnership option 1]\n- [Partnership option 2]\n- [Partnership option 3]") }}

**Why This Makes Sense:**
{{ why_partnership | default("- Our audiences complement each other\n- We have non-competing offerings\n- There's potential for mutual value creation") }}

{{ cta | default("Would you be interested in exploring this? I'd be happy to jump on a quick call to discuss.") }}

Best regards,
{{ my_name }}
{{ my_title | default("") }}
{{ my_company | default("") }}
