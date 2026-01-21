# Command Catalog

This document provides a comprehensive reference for all slash commands available in ClaudeKit Marketing.

## Content Commands

### /content/good

Create high-quality marketing content with full quality checks.

```bash
/content/good "product landing page for SaaS tool"
/content/good "email nurture sequence for trial users"
```

### /content/fast

Quickly create marketing content without extensive checks.

```bash
/content/fast "social media post about new feature"
/content/fast "quick blog post draft"
```

### /content/cro

Optimize existing content for conversion rate optimization.

```bash
/content/cro "optimize homepage hero section"
/content/cro "improve email subject lines"
```

### /content/enhance

Analyze and enhance existing copy.

```bash
/content/enhance "improve landing page copy"
/content/enhance "strengthen call-to-actions"
```

### /content/blog

Create SEO-optimized blog content with keyword targeting.

```bash
/content/blog "best project management tools for startups"
/content/blog "AI marketing automation guide"
```

### /content/video

Create video scripts with storyboards and platform optimization.

```bash
/content/video youtube "complete guide to Claude Code"
/content/video reel "3 marketing automation tips"
/content/video explainer "product onboarding flow"
```

## Planning Commands

### /plan

Create comprehensive marketing plans with research.

```bash
/plan "Q1 content marketing strategy"
/plan "product launch campaign"
```

### /plan/fast

Quick planning without extensive research.

```bash
/plan/fast "weekly social media calendar"
/plan/fast "email sequence outline"
```

### /plan/hard

In-depth research and planning for complex initiatives.

```bash
/plan/hard "market entry strategy for new segment"
/plan/hard "competitive positioning analysis"
```

### /plan/two

Create plan with two alternative approaches.

```bash
/plan/two "lead generation strategy"
/plan/two "content distribution approach"
```

### /plan/parallel

Create plan with parallel execution phases.

```bash
/plan/parallel "multi-channel campaign launch"
/plan/parallel "content production workflow"
```

### /plan/cro

Create conversion rate optimization plan.

```bash
/plan/cro "optimize checkout funnel"
/plan/cro "improve landing page conversions"
```

### /plan/ci

Analyze CI/CD logs and create fix plan.

```bash
/plan/ci https://github.com/user/repo/actions/runs/123
```

## Design Commands

### /design/good

Create immersive, high-quality designs.

```bash
/design/good "hero section for product page"
/design/good "email template design"
```

### /design/fast

Quick design creation.

```bash
/design/fast "social media banner"
/design/fast "simple CTA button"
```

### /design/screenshot

Create design based on screenshot reference.

```bash
/design/screenshot /path/to/screenshot.png
```

### /design/video

Create design based on video reference.

```bash
/design/video /path/to/video.mp4
```

### /design/describe

Describe a design from screenshot or video.

```bash
/design/describe /path/to/image.png
```

### /design/3d

Create interactive 3D designs with Three.js.

```bash
/design/3d "product showcase animation"
```

## Brainstorming Commands

### /brainstorm

Generate creative ideas and concepts.

```bash
/brainstorm "email campaign ideas for Black Friday"
/brainstorm "content topics for developer audience"
```

## Research Commands

### /ask

Answer technical and strategic questions.

```bash
/ask "what are trending marketing strategies for SaaS?"
/ask "how to improve email deliverability?"
```

### /scout

Search the codebase for relevant files.

```bash
/scout "find all email templates"
/scout "locate landing page components"
```

### /scout:ext

Use external tools for comprehensive search.

```bash
/scout:ext "analyze competitor marketing structure"
/scout:ext "find all content files"
```

## Documentation Commands

### /docs:init

Initialize project documentation.

```bash
/docs:init
```

### /docs:update

Update documentation based on recent changes.

```bash
/docs:update
```

### /docs:summarize

Create documentation summary.

```bash
/docs:summarize "content strategy" true
```

## Fix Commands

### /fix

Analyze and fix issues (intelligent routing).

```bash
/fix "broken email template rendering"
/fix "landing page layout issues"
```

### /fix/fast

Quick fix for small issues.

```bash
/fix/fast "typo in homepage copy"
```

### /fix/hard

Deep investigation and fix for complex issues.

```bash
/fix/hard "email deliverability problems"
```

### /fix/ui

Analyze and fix UI issues.

```bash
/fix/ui "button alignment on mobile"
```

### /fix/parallel

Fix issues using parallel agents.

```bash
/fix/parallel "multiple broken links"
```

### /fix/logs

Analyze logs and fix issues.

```bash
/fix/logs "campaign tracking errors"
```

### /fix/ci

Fix CI/CD pipeline issues.

```bash
/fix/ci https://github.com/user/repo/actions/runs/123
```

### /fix/types

Fix TypeScript type errors.

```bash
/fix/types
```

## Git Commands

### /git:cm

Stage and commit all changes.

```bash
/git:cm
```

### /git:cp

Stage, commit, and push changes.

```bash
/git:cp
```

### /git:pr

Create a pull request.

```bash
/git:pr feature-branch main
```

### /git:merge

Merge branches.

```bash
/git:merge feature-branch main
```

## Integration Commands

### /use-mcp

Utilize MCP server tools.

```bash
/use-mcp "query GA4 for page views"
/use-mcp "create SendGrid email campaign"
```

### /integrate/polar

Implement Polar.sh payment integration.

```bash
/integrate/polar "subscription checkout"
```

### /integrate/sepay

Implement SePay payment integration.

```bash
/integrate/sepay "Vietnamese payment gateway"
```

## Skill Commands

### /skill/create

Create a new skill.

```bash
/skill/create "seo-optimization based on https://docs.example.com"
```

### /skill/add

Add references to existing skill.

```bash
/skill/add seo-optimization "new SEO guidelines"
```

### /skill/optimize

Optimize existing skill.

```bash
/skill/optimize seo-optimization "improve keyword research"
```

### /skill/optimize:auto

Auto-optimize skill based on usage.

```bash
/skill/optimize:auto seo-optimization
```

### /skill/fix-logs

Fix skill based on error logs.

```bash
/skill/fix-logs seo-optimization
```

## Dashboard Commands

### /dashboard

Launch the Marketing Dashboard web application with full-stack campaign management.

**Usage:**
```bash
/dashboard [mode]
```

**Modes:**
- `dev` (default): Development mode with Vue HMR and live reload
- `prod`: Production mode (requires build first)
- `build`: Build Vue app for production
- `stop`: Stop running servers gracefully

**Examples:**
```bash
# Start development mode
/dashboard
/dashboard dev

# Build for production
/dashboard build

# Start production server
/dashboard prod

# Stop all servers
/dashboard stop
```

**Features:**
- Campaign management with Kanban board (drag-drop workflow)
- Content library with filters (type, campaign, status)
- Asset gallery with AI enhancement
- Automation panel (Blog, Social Media, Campaign Brief, SEO Audit)
- Dashboard with metrics and quick actions
- AI-powered content enhancement
- Markdown export with YAML frontmatter

**Tech Stack:**
- Frontend: Vue 3 + Vite + Pinia + Tailwind CSS
- Backend: Hono + Node.js + SQLite
- Database: Better-SQLite3 (local)
- AI: Claude integration via API

**URLs:**
- Dev Frontend: http://localhost:5173
- Dev API: http://localhost:3457
- Dev Health: http://localhost:3457/health
- Prod: http://localhost:3457 (serves built app)

**Requirements:**
- Node.js 18+
- API key (set via Settings page or sessionStorage)

**Performance:**
- Bundle: 56 KB gzipped
- Build time: 684ms
- Tests: 90% coverage (119/132 passing)

**Related:**
- Skill: `.claude/skills/marketing-dashboard/`
- Scripts: `start.sh`, `build.sh`, `stop.sh`, `start-production.sh`
- Documentation: `.claude/skills/marketing-dashboard/README.md`

## Utility Commands

### /journal

Write journal entries for learnings and insights.

```bash
/journal
```

### /watzup

Review recent changes and project status.

```bash
/watzup
```

### /ck-help

Get help with ClaudeKit features.

```bash
/ck-help "how to create a campaign"
```

## Campaign Commands

### /campaign

Create and manage marketing campaigns.

```bash
/campaign create "Q1 Product Launch"
/campaign status "Q1 Product Launch"
/campaign analyze "Q1 Product Launch"
```

### /campaign/email

Email campaign management for drip sequences and newsletters.

```bash
/campaign/email create
/campaign/email sequence
/campaign/email test
```

### /campaign/status

Get campaign status overview.

```bash
/campaign/status "Q1 Product Launch"
```

### /campaign/analyze

Analyze campaign performance with recommendations.

```bash
/campaign/analyze "Q1 Product Launch"
```

## SEO Commands

### /seo

SEO audit and optimization.

```bash
/seo audit https://example.com
/seo keywords "project management software"
/seo optimize ./content/blog/post.md
/seo schema ./pages/product.tsx
```

### /seo/audit

Technical SEO audit for websites.

```bash
/seo/audit https://example.com
/seo/audit https://example.com/pricing
```

### /seo/keywords

Keyword research for topics.

```bash
/seo/keywords "AI writing tools"
/seo/keywords "project management software"
```

### /seo/pseo

Programmatic SEO template generation.

```bash
/seo/pseo location
/seo/pseo comparison
/seo/pseo "best {tool} for {usecase}"
```

## Social Media Commands

### /social

Generate social media content.

```bash
/social twitter thread
/social linkedin post
/social instagram carousel
/social tiktok reel
```

### /social/schedule

Schedule social media posts.

```bash
/social/schedule week
/social/schedule month
/social/schedule campaign "Product Launch"
```

## Email Commands

### /email

Generate email content.

```bash
/email newsletter
/email cold "SaaS founders"
/email launch "New Feature"
/email nurture
```

### /email/sequence

Design email drip sequences.

```bash
/email/sequence welcome
/email/sequence "Product Onboarding"
/email/sequence nurture
```

## Analytics Commands

### /analyze

Analytics and performance reports.

```bash
/analyze traffic
/analyze campaigns
/analyze conversions
/analyze content
```

### /analyze/report

Generate periodic marketing reports.

```bash
/analyze/report daily
/analyze/report weekly
/analyze/report monthly
```

## Persona & Audience Commands

### /persona

Customer persona management.

```bash
/persona create
/persona analyze
/persona update "Tech Startup Founder"
/persona list
```

### /competitor

Competitive analysis.

```bash
/competitor analyze https://competitor.com
/competitor content https://competitor.com
/competitor seo https://competitor.com
```

### /funnel

Funnel design and optimization.

```bash
/funnel design lead-magnet
/funnel design webinar
/funnel analyze
/funnel optimize
```

## Command Best Practices

1. **Be Specific**: Provide clear context with commands
2. **Use Arguments**: Include relevant details in quotes
3. **Chain Commands**: Combine commands for workflows
4. **Check Output**: Review results before proceeding
5. **Iterate**: Refine with follow-up commands

## Command Workflows

### Content Creation Workflow

```bash
# 1. Brainstorm topics
/brainstorm "blog post ideas for SaaS launch"

# 2. Plan the content
/plan "write blog post about [selected topic]"

# 3. Create the content
/content/good "execute the blog post plan"

# 4. Commit changes
/git:cm
```

### Campaign Planning Workflow

```bash
# 1. Research and brainstorm
/brainstorm "Q4 marketing campaign ideas"

# 2. Create campaign
/campaign create "Black Friday Sale"

# 3. Design funnel
/funnel design product-launch

# 4. Create email sequence
/campaign/email sequence

# 5. Create social content
/social twitter thread
/social linkedin post

# 6. Analyze performance
/campaign/analyze "Black Friday Sale"
```

### SEO Content Workflow

```bash
# 1. Keyword research
/seo/keywords "AI marketing tools"

# 2. Create blog content
/content/blog "AI marketing automation guide"

# 3. Optimize for SEO
/seo optimize ./content/blog/ai-marketing.md

# 4. Generate schema
/seo schema ./content/blog/ai-marketing.md
```

### Quick Fix Workflow

```bash
# 1. Identify the issue
/scout "find broken component"

# 2. Fix quickly
/fix/fast "the identified issue"

# 3. Commit
/git:cp
```
