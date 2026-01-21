---
name: Announcement
type: newsletter
subject: "{{ subject | default('📢 ' + (announcement_title | default('[Announcement]'))) }}"
description: Important announcement to subscribers
tags: [newsletter, announcement, important]
---
Hi {{ first_name }},

{{ opening | default("I have some exciting news to share with you today.") }}

---

**{{ announcement_title | default("[Announcement Title]") }}**

{{ announcement_body | default("[Main announcement content - what's happening, why it matters, how it affects them]") }}

---

**What This Means For You:**

{{ impact | default("- [Impact point 1]\n- [Impact point 2]\n- [Impact point 3]") }}

---

**What's Next:**

{{ next_steps | default("[Timeline or next steps]") }}

---

{{ cta | default("[Take action →](" + (link | default("[link]")) + ")") }}

---

{{ faq | default("**Have questions?** Reply to this email or [visit our FAQ](" + (faq_link | default("[link]")) + ").") }}

{{ closing | default("Thank you for being part of our community. We're excited about this next chapter!") }}

{{ my_name }}
{{ my_title | default("") }}
{{ my_company | default("") }}
