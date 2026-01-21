# ClaudeKit Marketing - Quick Reference Card

**Start here:** `docs/kit-guide/00-overview.md`

## Core Commands

```bash
# Setup & Planning
/bootstrap "project requirements"      # Initialize project
/plan "your task"                      # Create implementation plan
/brainstorm "your question"            # Ideation & advice

# Content
/content:good "request"                # Write quality content
/content:blog "topic"                  # Create blog post
/content:cro "optimize"                # Improve conversions
/content:enhance "improve copy"        # Polish content

# Design
/design:good "create design"           # Design anything
/design:generate "create image"        # Generate images
/design:3d "3D visualization"          # 3D designs
/design:screenshot "capture design"    # Screenshot HTML
/design:video "video content"          # Create video

# Social Media
/social twitter post                   # Twitter content
/social linkedin post                  # LinkedIn content
/social instagram post                 # Instagram content
/social tiktok reel                    # TikTok video
/social youtube shorts                 # YouTube shorts

# Campaigns
/campaign create "campaign name"       # Start campaign
/campaign status "campaign name"       # Check progress
/campaign analyze "campaign name"      # Performance analysis

# SEO
/seo "keyword research"                # Find keywords
/seo "optimize page"                   # On-page SEO
/seo "technical audit"                 # Technical SEO

# Analysis
/scout "search codebase"               # Find files
/scout:ext "external search"           # External research
/analyze "analyze something"           # Deep analysis
```

## Quick Workflows

### Create Blog Post
```bash
1. /seo "keyword research for [topic]"
2. /content:blog "your topic"
3. /content:cro "optimize for conversions"
4. Output: assets/content/blog/
```

### Launch Social Campaign
```bash
1. /plan "social strategy"
2. /social twitter thread "topic"
3. /social linkedin post "topic"
4. /social instagram carousel "topic"
5. /social tiktok reel "topic"
```

### Run Marketing Campaign
```bash
1. /campaign create "campaign name"
2. /content:good "create email"
3. /design:generate "campaign images"
4. /social [platform] [type]
5. /campaign analyze "campaign name"
```

### Create Design
```bash
1. /design:good "design description"
2. /design:generate "image for [use]"
3. /design:screenshot "verify design"
```

## Key Files

**Brand Settings:**
- `docs/brand-guidelines.md` - Your brand identity
- `docs/design-guidelines.md` - Visual standards
- `docs/content-strategy.md` - Content pillars

**Assets:**
- `assets/campaigns/` - Campaign materials
- `assets/content/` - Blog, emails, pages
- `assets/social/` - Social content
- `assets/designs/` - Design files
- `assets/images/` - Generated images
- `assets/videos/` - Video content

**Documentation:**
- `docs/kit-guide/` - Complete guides
- `docs/seo-keywords.md` - Keyword research
- `docs/content-calendar.md` - Editorial calendar

## Scripts

```bash
# Brand Management
node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs
node .claude/skills/brand-guidelines/scripts/validate-asset.cjs <file>
node .claude/skills/brand-guidelines/scripts/extract-colors.cjs <file>
node .claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs
```

## Documentation Map

| Need | Read |
|------|------|
| Understand kit | 00-overview.md |
| Set up brand | 01-brand-system.md |
| Create designs | 02-image-generation.md |
| Make videos | 03-video-production.md |
| Write content | 04-content-creation.md |
| Social posts | 05-social-media.md |
| Run campaigns | 06-campaign-management.md |
| Rank in search | 07-seo-optimization.md |
| Initialize kit | 08-project-setup.md |
| Use scripts | 09-scripts-reference.md |

## Command Parameters

### /social
- Platforms: twitter, linkedin, instagram, tiktok, youtube
- Types: post, thread, carousel, story, reel, article

### /content
- Variants: good, fast, cro, enhance, blog
- Output: assets/content/

### /design
- Variants: good, generate, 3d, screenshot, slides, video
- Output: assets/designs/, assets/images/

## Output Locations

```
assets/
├── campaigns/{slug}/
├── content/{blog,emails,pages}
├── social/{platform}/
├── designs/
├── images/generated/
└── videos/
```

## Performance Metrics to Track

**Content:**
- Traffic
- Rankings
- Engagement rate
- Conversions

**Social:**
- Impressions
- Engagement rate
- Follower growth
- CTR

**Campaigns:**
- ROI
- Conversion rate
- Cost per acquisition
- Customer lifetime value

## Setup Checklist

- [ ] Run `/bootstrap` or `/marketing:init`
- [ ] Create `docs/brand-guidelines.md`
- [ ] Create `docs/design-guidelines.md`
- [ ] Create first blog post
- [ ] Create social content
- [ ] Run first campaign
- [ ] Monitor performance
- [ ] Iterate and optimize

## Common Issues

| Problem | Solution |
|---------|----------|
| Brand context missing | Check `docs/brand-guidelines.md` exists |
| Assets not saving | Verify `assets/` folder exists |
| Commands not found | Run `/ck-help` to list commands |
| Images low quality | Use `/design:generate` for AI or `/design:good` |
| Content not branded | Ensure brand guidelines defined |
| SEO not working | Verify keywords and title tags optimized |

## Resources

- **Full Guide:** docs/kit-guide/00-overview.md
- **All Commands:** /ck-help
- **Setup:** docs/kit-guide/08-project-setup.md
- **Examples:** Review existing files in assets/

## Tips

1. Always update `docs/brand-guidelines.md` first
2. Use `/seo` before creating content
3. Review templates before customizing
4. Run scripts regularly to sync brand
5. Track metrics weekly
6. Iterate based on performance

---

**Start:** `docs/kit-guide/00-overview.md`
**Questions:** Check relevant guide in `docs/kit-guide/`
