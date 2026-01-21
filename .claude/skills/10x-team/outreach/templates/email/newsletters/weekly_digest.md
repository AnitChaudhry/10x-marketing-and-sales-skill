---
name: Weekly Digest
type: newsletter
subject: "{{ subject | default('Weekly Digest: ' + (date | default('[Date]'))) }}"
description: Weekly newsletter digest
tags: [newsletter, weekly, digest]
---
Hi {{ first_name }},

{{ opening | default("Here's what you might have missed this week:") }}

---

**📰 Top Stories**

{{ story_1 | default("**[Story 1 Title]**\n[Brief description]\n[Read more →]") }}

{{ story_2 | default("**[Story 2 Title]**\n[Brief description]\n[Read more →]") }}

{{ story_3 | default("**[Story 3 Title]**\n[Brief description]\n[Read more →]") }}

---

**💡 Insight of the Week**

{{ insight | default("[Key insight or tip that provides value]") }}

---

**🔗 Quick Links**

{{ links | default("- [Link 1]\n- [Link 2]\n- [Link 3]") }}

---

{{ closing | default("That's a wrap for this week. See you next time!") }}

{{ my_name }}

---

*{{ unsubscribe | default("You're receiving this because you subscribed at [website]. [Unsubscribe]") }}*
