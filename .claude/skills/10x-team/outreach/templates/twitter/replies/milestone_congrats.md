---
name: Milestone Congratulations
type: reply
max_length: 280
description: Congratulate on achievements/milestones
tags: [congratulations, milestone, celebration]
---
Congrats {{ first_name | default("") }}! {{ milestone_comment | default("Huge milestone") }}. {{ personal_note | default("Been following the journey and this is well deserved") }}! {{ emoji | default("") }}
