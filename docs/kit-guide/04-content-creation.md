# Content Creation Commands

## Overview

Content commands generate and optimize marketing copy for blogs, landing pages, emails, and conversion-focused materials. All content is reviewed for brand compliance and conversion optimization.

**Note:** Actual commands use `/write:*` prefix (not `/content:*`).

## Main Command: `/write`

### `/write:good`
Write good, creative, and smart marketing copy

**Usage:**
```bash
/write:good <request>
```

**Examples:**
```bash
/write:good "write landing page copy for SaaS product"
/write:good "create email sequence for product launch"
/write:good "write blog post about [topic]"
```

**Workflow:**
1. Analyze request and context
2. Use `ai-multimodal` if screenshots/videos provided
3. Research relevant information with researcher agents
4. Use `/scout` or `/scout:ext` to find codebase files
5. Plan copy with planner agent
6. Write with copywriter agent
7. Review for brand compliance
8. Output to appropriate directory

### `/write:fast`
Create content quickly with less review iteration

**Usage:**
```bash
/write:fast <request>
```

**Examples:**
```bash
/write:fast "quick email subject line ideas"
/write:fast "social media post ideas"
```

### `/write:cro`
Optimize content for conversions (CRO - Conversion Rate Optimization)

**Usage:**
```bash
/write:cro <request>
```

**Examples:**
```bash
/write:cro "improve homepage for higher conversions"
/write:cro "optimize email subject lines for open rate"
```

**Workflow:**
1. Analyze existing content or context
2. Research CRO best practices
3. Identify conversion barriers
4. Suggest optimizations
5. Test multiple versions
6. Output A/B test variants

### `/write:enhance`
Enhance and improve existing content

**Usage:**
```bash
/write:enhance <request>
```

**Examples:**
```bash
/write:enhance "make email more compelling"
/write:enhance "improve headline for more clicks"
```

### `/write:blog`
Create blog post content with research and SEO optimization

**Usage:**
```bash
/write:blog <topic>
```

**Examples:**
```bash
/write:blog "top 10 SaaS marketing strategies"
/write:blog "how to build product roadmap"
```

**Workflow:**
1. Research topic with researcher agents
2. Gather keywords with SEO skill
3. Plan article structure with planner
4. Write content with content-creator agent
5. Optimize for SEO with seo-optimization skill
6. Review for brand voice with content-reviewer
7. Output to `assets/articles/`

### `/youtube:blog`
Convert YouTube video to SEO-optimized blog post

**Usage:**
```bash
/youtube:blog <youtube-url>
```

**Workflow:**
1. Extract transcript via VidCap API
2. Generate blog structure from video content
3. Optimize for SEO
4. Output to `assets/articles/`

## Content Subcommands

### Content Type: Blog

**Location:** `.claude/commands/write/`

Blog-specific commands:

```bash
/write:blog <topic>           # Full blog post
/write:audit                  # Audit content quality
/write:publish                # Finalize and publish
```

## Content Templates

### Blog Post Template
```markdown
---
title: [Compelling title]
description: [2-3 sentence summary]
author: [Author name]
date: [YYYY-MM-DD]
tags: [tag1, tag2, tag3]
featured_image: [image path]
---

# [Title]

## Introduction
[Hook + problem statement + promise of solution]

## Key Section 1
[Detailed content]

### Subsection
[Supporting points with examples]

## Key Section 2
[More content with data/proof]

## Key Section 3
[Additional value]

## Conclusion
[Summary + CTA]

## Call-to-Action
[Specific next step for reader]

---

## Additional Resources
- Link 1
- Link 2
```

### Email Copy Template
```markdown
---
type: email
campaign: [name]
segment: [audience]
template: [welcome/nurture/promotional/announcement]
subject_line: [40-60 characters]
preview_text: [50-100 characters]
---

# Email: [Name]

## Subject Line
[Main subject]

## Preview Text
[First 50-100 chars]

## Email Body

### Salutation
Dear [Name],

### Opening/Hook
[Why this email matters to them]

### Body
[Main message, benefits, social proof]

### Call-to-Action
[Primary action button]
Button text: [CTA]
Button link: [URL]

### Closing
[Sign-off]

---

## Notes
- Estimated send time: [day/time]
- A/B test: [version A vs B]
```

### Landing Page Template
```markdown
---
type: landing-page
campaign: [name]
goal: [conversion goal]
audience: [target segment]
---

# [Page Title]

## Hero Section
- Headline: [Main promise]
- Subheadline: [Supporting statement]
- CTA: [Primary action]
- Visual: [Hero image description]

## Problem Section
[Describe customer pain point]

## Solution Section
[Introduce your solution]

## Features Section
- Feature 1: [Benefit]
- Feature 2: [Benefit]
- Feature 3: [Benefit]

## Social Proof
- Testimonial 1: "[Quote]" - [Customer name]
- Testimonial 2: "[Quote]" - [Customer name]

## Pricing/Offer
[Clear pricing or offer]

## FAQ
- Q: [Common question]
  A: [Answer]

## Final CTA
[Strong closing call-to-action]
```

## Content Skills Used

### copywriting
- Headline formulas
- Email copy patterns
- Landing page structures
- CTA optimization
- A/B testing variations

### content-marketing
- Content strategy
- Editorial calendars
- Topic clustering
- Content pillars
- Distribution planning

### seo-optimization
- Keyword research
- On-page optimization
- Meta tag creation
- Internal linking
- Content structure for SEO

### brand-guidelines
- Voice consistency checking
- Messaging alignment
- Tone verification
- Style guide compliance

### content-hub
- Asset management
- File organization
- Metadata tracking
- Version control

## Output Locations

```
assets/
├── content/
│   ├── blog/
│   │   ├── [slug].md
│   │   └── [slug]/
│   │       ├── content.md
│   │       ├── assets/
│   │       └── metadata.json
│   ├── landing-pages/
│   │   ├── [slug].html
│   │   └── [slug].md
│   ├── emails/
│   │   ├── campaigns/
│   │   ├── templates/
│   │   └── sequences/
│   ├── pages/
│   │   ├── about.md
│   │   ├── features.md
│   │   └── pricing.md
│   └── copy/
│       ├── headlines.md
│       ├── subject-lines.md
│       └── ctas.md

docs/
├── content-calendar.md       # Editorial calendar
├── content-strategy.md       # Content strategy doc
└── seo-keywords.md          # Keyword research
```

## Content Naming Convention

```
{type}_{campaign}_{description}_{timestamp}.{ext}

Examples:
- blog_product-launch_5-strategies_20251209.md
- email_nurture_sequence-01_20251209.md
- page_pricing_annual-discount_20251209.html
- subject-line_promotion_black-friday_20251209.txt
```

## Content Workflow Examples

### Blog Post Creation
```bash
# 1. Generate blog post
/write:blog "top 10 marketing automation strategies"

# 2. Audit quality
/write:audit

# 3. Enhance with SEO optimization
/write:cro "improve headline for search rankings"

# 4. Publish
/write:publish
```

### YouTube to Blog
```bash
# Convert video to article
/youtube:blog "https://youtube.com/watch?v=xxx"
```

### Email Sequence
```bash
# 1. Plan sequence
/plan "5-email nurture sequence for new users"

# 2. Write sequence
/write:good "create 5-email onboarding sequence"

# 3. Optimize subject lines
/write:cro "optimize subject lines for 40%+ open rate"
```

### Landing Page
```bash
# 1. Plan page
/plan "product launch landing page"

# 2. Create copy
/write:good "write compelling landing page copy"

# 3. Optimize for conversions
/write:cro "improve CTA button placement and messaging"

# 4. Design layout
/design:good "create beautiful landing page design"
```

## Copywriting Formulas

Use these proven formulas when requesting copy:

### Headlines
- **Power Word + Benefit:** "The Only [Adjective] [Noun] That [Benefit]"
- **Curiosity Gap:** "[Surprising Fact] - [Explanation/Benefit]"
- **How To:** "How to [Achieve Desired Outcome] in [Time]"
- **Problem + Solution:** "[Problem] - [Solution] [Proof]"

### Email Subject Lines
- **Open Rate Increase:** "[Statistic or Curiosity] Inside"
- **Personalization:** "[First Name], [Specific offer]"
- **Urgency:** "Last Chance: [Offer] Ends [Date]"
- **Benefit:** "Get [Benefit] in [Time Frame]"

### CTAs
- **Action-Oriented:** "Get Started", "Start Free Trial"
- **Benefit-Focused:** "See Results", "Unlock [Benefit]"
- **Urgency-Based:** "Claim Your Spot", "Join Now"
- **Curiosity-Based:** "Show Me", "Learn How"

## A/B Testing Templates

When using `/content:cro`, request A/B test variants:

```markdown
# A/B Test: [Element]

## Version A (Control)
[Original or current version]

## Version B (Test)
[Optimized variation]

## Expected Improvement
[Predicted metric improvement]

## How to Test
- Sample size: [number]
- Duration: [days]
- Success metric: [metric]
```

## Content Review Checklist

All content goes through these checks:

- [ ] Brand voice consistent
- [ ] Messaging aligned with strategy
- [ ] Grammar and spelling correct
- [ ] Tone appropriate for audience
- [ ] CTAs clear and compelling
- [ ] Factual accuracy verified
- [ ] SEO keywords included naturally
- [ ] Length appropriate for format
- [ ] No competitor mentions (unless intentional)
- [ ] Includes proof/social proof where relevant

## SEO Content Guidelines

When using `/content:blog` or `/content:cro`:

1. **Primary Keyword** - Mentioned in title, H1, first paragraph
2. **Secondary Keywords** - 3-5 related keywords naturally distributed
3. **Internal Links** - 2-3 links to related content
4. **Meta Description** - 150-160 characters with primary keyword
5. **Headings** - H1 for title, H2/H3 for sections
6. **Readability** - Short paragraphs, bullet points, varied sentence length
7. **Word Count** - 1,500+ words for competitive keywords, 800+ for long-tail
8. **Images** - At least 3-5 images with descriptive alt text

## Email Marketing Best Practices

### Sequence Types

**Welcome Sequence (3-5 emails)**
1. Welcome + first value
2. Address common objection
3. Share social proof
4. Advanced tips
5. CTA + offer

**Nurture Sequence (7-10 emails)**
1. Problem identification
2. Educational content
3. Alternative solutions
4. Your solution benefits
5. Case study/proof
6. Limited offer
7. Final CTA

**Promotional Sequence (3-5 emails)**
1. Announcement + big picture
2. Specific features/benefits
3. Social proof
4. Limited time emphasis
5. Final urgent CTA

### Email Performance Metrics

Track these to optimize future emails:

- Open rate (target: 20-25%+)
- Click-through rate (target: 3-5%+)
- Conversion rate (depends on goal)
- Bounce rate (target: <5%)
- Unsubscribe rate (target: <0.5%)

## Content Distribution

After creating content:

1. **Publish to primary channel** (blog, email, etc.)
2. **Repurpose for social media** - `/social` commands
3. **Create variations** - Different formats/platforms
4. **Update content hub** - Register in manifest
5. **Promote** - Share via email, social, partnerships

## Best Practices

1. **Brand Voice First** - All content reflects brand personality
2. **Benefit-Focused** - Focus on reader value, not features
3. **Proof Required** - Back claims with data or testimonials
4. **Clear CTAs** - Every piece should guide to next step
5. **SEO Smart** - Optimize for search naturally
6. **Mobile Ready** - Assume mobile-first reading
7. **Scannable** - Use short paragraphs and lists
8. **Edit Ruthlessly** - Remove unnecessary words

## Common Issues & Solutions

**Content doesn't reflect brand voice?**
- Ensure brand guidelines defined in `docs/brand-guidelines.md`
- Request `/write:enhance` for voice adjustment
- Review with `/write:good` using brand context

**Low email open rates?**
- Use `/write:cro` to optimize subject lines
- Test personalization (first name, segment)
- Analyze send time and frequency

**Blog post not ranking?**
- Use `/write:blog` with keyword research
- Apply `/write:cro` for on-page optimization
- Create internal linking strategy

## Next Steps

1. Define content strategy in `docs/content-strategy.md`
2. Create editorial calendar in `docs/content-calendar.md`
3. Write first blog post with `/write:blog`
4. Create email sequence with `/write:good`
5. Optimize landing page with `/write:cro`
6. Monitor performance metrics
