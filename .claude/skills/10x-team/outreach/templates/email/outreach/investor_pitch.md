---
name: Investor Pitch
type: fundraising
subject: "{{ subject | default((my_company | default('[Company]')) + ' - ' + (stage | default('Seed')) + ' Round') }}"
description: Reach out to investors about funding
tags: [investor, fundraising, pitch, startup]
---
Hi {{ first_name }},

{{ opening | default("I'm reaching out because your investments in " + (investment_focus | default("[space]")) + " align with what we're building.") }}

**{{ my_company | default("[Company Name]") }}**: {{ one_liner | default("[One-line description of what you do]") }}

**Traction:**
{{ traction | default("- [Key metric 1]\n- [Key metric 2]\n- [Key metric 3]") }}

**The Opportunity:**
{{ opportunity | default("[Brief description of market opportunity]") }}

**The Ask:**
{{ ask | default("We're raising a " + (round_size | default("$X")) + " " + (stage | default("seed")) + " round to " + (use_of_funds | default("[use of funds]")) + ".") }}

{{ why_this_investor | default("Your experience with [relevant portfolio company or expertise] would be invaluable as we scale.") }}

{{ cta | default("Would you have 20 minutes for an intro call? I'd love to share our deck and learn if there's potential for a conversation.") }}

Best,
{{ my_name }}
Founder, {{ my_company | default("[Company]") }}

{{ calendar_link | default("") }}
