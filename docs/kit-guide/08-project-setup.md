# Project Setup & Initialization

## Overview

Initialize and configure your ClaudeKit Marketing project with brand guidelines, documentation, and basic setup.

## Quick Setup Commands

### `/bootstrap`
Bootstrap a new project from scratch

**Usage:**
```bash
/bootstrap <requirements>
```

**Examples:**
```bash
/bootstrap "set up SaaS marketing project"
/bootstrap "initialize e-commerce marketing kit"
```

**Workflow:**
1. Ask clarifying questions about project
2. Validate Git initialization
3. Research and tech stack selection
4. Create detailed implementation plan
5. Design guidelines if requested
6. Build infrastructure
7. Document and onboard

**Output:** Complete project structure with docs, plans, and initial setup

### `/marketing:init`
Initialize marketing kit specifically

**Usage:**
```bash
/marketing:init
```

**Creates:**
- Brand guidelines template
- Content strategy document
- Social media calendar
- SEO keyword research doc
- Campaign templates
- Asset folder structure

## Manual Setup Process

If not using `/bootstrap`:

### Step 1: Project Structure

Create basic folder structure:

```bash
mkdir -p docs assets plans
mkdir -p assets/{campaigns,content,social,designs,videos}
mkdir -p docs/kit-guide
```

### Step 2: Brand Guidelines

Create `docs/brand-guidelines.md`:

```markdown
# Brand Guidelines

## Brand Voice

### Personality Traits
- [Trait 1]
- [Trait 2]
- [Trait 3]

### Tone Spectrum
- Formal ↔ Casual: [Position]
- Simple ↔ Complex: [Position]
- Serious ↔ Playful: [Position]
- Reserved ↔ Expressive: [Position]

### Do's
- [Do 1]
- [Do 2]

### Don'ts
- [Don't 1]
- [Don't 2]

## Visual Identity

### Logo
- Primary logo: [Description]
- Secondary logo: [Description]
- Icon: [Description]

### Color Palette
- Primary: #[HEX] (RGB: [R,G,B])
- Secondary: #[HEX] (RGB: [R,G,B])
- Accent: #[HEX] (RGB: [R,G,B])
- Neutral: #[HEX] (RGB: [R,G,B])

### Typography
- Headlines: [Font family] ([Google Fonts link])
- Body: [Font family] ([Google Fonts link])

## Messaging Framework

### Value Proposition
[Your core value prop]

### Key Messages
1. [Message 1]
2. [Message 2]
3. [Message 3]

### Target Audience
- Primary: [Description]
- Secondary: [Description]
```

### Step 3: Project Overview PDR

Create `docs/project-overview-pdr.md`:

```markdown
# Project Overview & PDR

## Project Vision
[What are you building?]

## Key Features
- [Feature 1]
- [Feature 2]
- [Feature 3]

## Success Metrics
- [Metric 1]: [Target]
- [Metric 2]: [Target]
- [Metric 3]: [Target]

## Timeline
- Phase 1: [Dates]
- Phase 2: [Dates]
- Phase 3: [Dates]

## Team
- [Role]: [Person]
- [Role]: [Person]

## Budget
- Total: $[Amount]
- Allocation: [Breakdown]
```

### Step 4: Documentation Index

Create `docs/README.md`:

```markdown
# Project Documentation

## Core Documentation

- **[Brand Guidelines](./brand-guidelines.md)** - Brand voice, visuals, messaging
- **[Content Strategy](./content-strategy.md)** - Editorial calendar, pillars
- **[Design Guidelines](./design-guidelines.md)** - Visual standards
- **[SEO Keywords](./seo-keywords.md)** - Keyword research and strategy

## Guides

- **[Kit Guide](./kit-guide/)** - Complete ClaudeKit Marketing guide
  - [Overview](./kit-guide/00-overview.md)
  - [Brand System](./kit-guide/01-brand-system.md)
  - [Image Generation](./kit-guide/02-image-generation.md)
  - [Video Production](./kit-guide/03-video-production.md)
  - [Content Creation](./kit-guide/04-content-creation.md)
  - [Social Media](./kit-guide/05-social-media.md)
  - [Campaign Management](./kit-guide/06-campaign-management.md)
  - [SEO Optimization](./kit-guide/07-seo-optimization.md)
  - [Project Setup](./kit-guide/08-project-setup.md)
  - [Scripts Reference](./kit-guide/09-scripts-reference.md)

## Project Plans

- **[Project Roadmap](./project-roadmap.md)** - High-level timeline
- **[Phase Plans](../plans/)** - Detailed phase-by-phase plans

## Quick Links

- **Start first content:** `/content:blog "topic"`
- **Generate images:** `/design:good "design description"`
- **Social posts:** `/social [platform] [type]`
- **Manage campaign:** `/campaign create "campaign name"`
```

### Step 5: Content Strategy

Create `docs/content-strategy.md`:

```markdown
# Content Strategy

## Content Pillars

### Pillar 1: [Topic]
Content categories:
- [Subtype 1]
- [Subtype 2]
- [Subtype 3]

### Pillar 2: [Topic]
[Same structure]

### Pillar 3: [Topic]
[Same structure]

## Content Calendar

| Date | Platform | Content Type | Topic | Status |
|------|----------|-------------|-------|--------|
| 2024-01-08 | Blog | Guide | [Topic] | Draft |
| 2024-01-10 | Email | Newsletter | [Topic] | Draft |

## Content Goals

- Monthly blog posts: [Number]
- Weekly social posts: [Number]
- Monthly email: [Frequency]
- Quarterly whitepapers: [Number]

## Target Keywords

- [Primary keyword]
- [Primary keyword]
- [Primary keyword]

See `seo-keywords.md` for full keyword research.

## Distribution Channels

### Email
- Frequency: [X/week]
- Segment strategy: [Description]

### Blog
- Publishing frequency: [X/week]
- Target audience: [Description]

### Social Media
- Twitter: [Frequency/day]
- LinkedIn: [Frequency/week]
- Instagram: [Frequency/day]
- TikTok: [Frequency/day]

### Paid
- Google Ads: [Budget]
- Meta Ads: [Budget]
```

### Step 6: Asset Organization

Create `.claude/skills/brand-guidelines/scripts/init-assets.sh`:

```bash
#!/bin/bash

# Create asset folder structure
mkdir -p assets/{campaigns,content,designs,images,social,videos}
mkdir -p assets/social/{twitter,linkedin,instagram,tiktok,youtube}
mkdir -p assets/campaigns/{active,archived}
mkdir -p assets/content/{blog,landing-pages,emails}
mkdir -p assets/designs/{templates,components}
mkdir -p .assets/{manifest,versions,metadata}

# Create manifest template
cat > .assets/manifest.json << 'EOF'
{
  "version": "1.0.0",
  "assets": [],
  "lastUpdated": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "totalAssets": 0
}
EOF

echo "✓ Asset directories created"
```

## Configuration Files

### .claude/.ck.json

Kit configuration:

```json
{
  "version": "1.0.0",
  "name": "Your Project Name",
  "description": "Your marketing project",
  "kit": "marketing",
  "planDateFormat": "YYYYMMDD-HHmm",
  "hooks": {
    "enabled": true,
    "autoSync": true,
    "onBrandUpdate": true
  },
  "skills": {
    "active": [
      "brand-guidelines",
      "content-marketing",
      "copywriting",
      "seo-optimization"
    ]
  }
}
```

### .claude/.env.example

Environment variables:

```bash
# Gemini API for image generation
GEMINI_API_KEY=your_key_here

# Claude API
ANTHROPIC_API_KEY=your_key_here

# Brand context
BRAND_GUIDELINES_PATH=./docs/brand-guidelines.md
DESIGN_GUIDELINES_PATH=./docs/design-guidelines.md

# Output paths
ASSETS_PATH=./assets
PLANS_PATH=./plans
DOCS_PATH=./docs
```

Copy to `.env` and fill in actual values:

```bash
cp .claude/.env.example .env
# Edit .env with your API keys
```

## Initial Content Setup

### First Blog Post

```bash
# 1. Research keywords
/seo "keyword research for [your main topic]"

# 2. Create blog post
/content:blog "first blog post about [topic]"

# 3. Optimize for SEO
/content:cro "optimize blog post for [primary keyword]"

# 4. Output location
# assets/content/blog/[slug].md
```

### Email Welcome Sequence

```bash
# 1. Plan sequence
/plan "3-email welcome sequence"

# 2. Create emails
/content:good "write 3-email welcome sequence"

# 3. Output location
# assets/emails/welcome-sequence/
```

### Social Media Kickoff

```bash
# Create week 1 of content
/social twitter post "intro post"
/social linkedin post "professional intro"
/social instagram post "visual intro"

# Output locations
# assets/social/twitter/
# assets/social/linkedin/
# assets/social/instagram/
```

## Git Setup

Initialize Git repository:

```bash
# Initialize Git
git init

# Add .gitignore
cat > .gitignore << 'EOF'
# Environment
.env
.env.local
.env.*.local

# API keys
*.key
*.pem

# Dependencies
node_modules/
.venv/

# Build output
dist/
build/

# Temporary files
*.tmp
*.log
.DS_Store

# Large files
*.mp4
*.mov
*.zip

# API credentials
.aws/
credentials.json
EOF

# Initial commit
git add .
git commit -m "Initial project setup"
```

## Team Onboarding

### Onboarding Checklist

- [ ] Clone repository
- [ ] Copy `.env.example` to `.env`
- [ ] Add API keys to `.env`
- [ ] Read `docs/brand-guidelines.md`
- [ ] Review `docs/content-strategy.md`
- [ ] Understand command structure
- [ ] Create first piece of content
- [ ] Review with brand reviewer

### Team Resources

**For new team members, share:**
1. `docs/README.md` - Documentation index
2. `docs/brand-guidelines.md` - Brand reference
3. `docs/kit-guide/00-overview.md` - Kit overview
4. Quick command reference card

## Verification Checklist

After setup, verify:

- [ ] `.claude/` folder exists with agents, commands, skills
- [ ] `docs/brand-guidelines.md` filled out
- [ ] `docs/content-strategy.md` created
- [ ] `docs/project-overview-pdr.md` created
- [ ] Asset folders created in `assets/`
- [ ] `.env` file configured with API keys
- [ ] Git repository initialized
- [ ] First test command runs successfully: `/content:good "test"`

## Commands for Verification

```bash
# Test brand context injection
node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs

# List available commands
/ck-help

# Quick test content generation
/content:good "test piece"

# Create first blog
/content:blog "your topic"
```

## Troubleshooting Setup

**Commands not recognized?**
- Verify `.claude/commands/` folder exists
- Check Claude Code is properly installed
- Run `/ck-help` to list available commands

**Brand context not injecting?**
- Check `docs/brand-guidelines.md` exists
- Verify file format is valid Markdown
- Run: `node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs --json`

**API keys not working?**
- Verify `.env` file created (not `.env.example`)
- Check API keys are valid
- For Gemini: https://aistudio.google.com/apikey
- For Claude: https://console.anthropic.com/

**Assets not saving?**
- Verify `assets/` folder structure exists
- Check write permissions on folder
- Verify full path in output settings

## Next Steps

1. Complete brand guidelines
2. Run `/bootstrap` or `/marketing:init`
3. Create first content piece with `/content:blog`
4. Generate social content with `/social`
5. Set up content calendar
6. Launch first campaign with `/campaign create`
7. Monitor performance and iterate
