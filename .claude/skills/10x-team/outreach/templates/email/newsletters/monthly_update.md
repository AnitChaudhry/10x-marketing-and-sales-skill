---
name: Monthly Update
type: newsletter
subject: "{{ subject | default((month | default('[Month]')) + ' Update from ' + (my_company | default('[Company]'))) }}"
description: Monthly company/product update
tags: [newsletter, monthly, update]
---
Hi {{ first_name }},

{{ opening | default("Hope your " + (month | default("month")) + " is going great! Here's what's been happening:") }}

---

**📊 {{ month | default("[Month]") }} Highlights**

{{ highlights | default("- [Highlight 1]\n- [Highlight 2]\n- [Highlight 3]") }}

---

**🚀 What's New**

{{ whats_new | default("[Description of new features, content, or updates]") }}

---

**📖 From the Blog**

{{ blog_posts | default("- [Post 1]\n- [Post 2]") }}

---

**🎯 Coming Up**

{{ coming_up | default("[Preview of what's coming next month]") }}

---

**💬 From the Community**

{{ community | default("[User testimonial, case study, or community highlight]") }}

---

{{ closing | default("Thanks for being part of our journey. As always, hit reply if you have any questions or feedback!") }}

{{ my_name }}
{{ my_title | default("") }}
{{ my_company | default("") }}

---

*{{ unsubscribe | default("[Unsubscribe] | [Update preferences]") }}*
