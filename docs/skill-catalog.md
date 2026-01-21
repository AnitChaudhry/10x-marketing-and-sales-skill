# Skill Catalog

This document provides a comprehensive reference for all skills available in ClaudeKit Marketing. Skills extend agent capabilities with specialized knowledge and tools.

## Core Marketing Skills

### AI Multimodal

**Directory:** `.claude/skills/ai-multimodal/`

Process and generate multimedia content using Google Gemini API.

**Capabilities:**
- Image analysis and generation (Imagen 4)
- Video understanding and generation (Veo 3)
- Audio transcription and analysis
- Document processing (PDFs, etc.)

**Use Cases:**
- Generate marketing images
- Analyze competitor visuals
- Create video content
- Process marketing documents

**Requirements:**
- `GEMINI_API_KEY` environment variable

### Media Processing

**Directory:** `.claude/skills/media-processing/`

Process multimedia files with FFmpeg and ImageMagick.

**Capabilities:**
- Video editing and conversion
- Image manipulation
- Audio processing
- Background removal (RMBG)

**Use Cases:**
- Resize images for social media
- Convert video formats
- Optimize media for web
- Create thumbnails

### Chrome DevTools

**Directory:** `.claude/skills/chrome-devtools/`

Browser automation and debugging using Puppeteer.

**Capabilities:**
- Screenshot capture
- Performance analysis
- Network monitoring
- Web scraping

**Use Cases:**
- Capture competitor pages
- Analyze page performance
- Generate visual reports
- Automate browser tasks

### Content Hub

**Directory:** `.claude/skills/content-hub/`

Visual asset gallery for managing marketing assets. Browse, filter, edit, and generate assets with brand awareness.

**Features:**
- Gallery grid with thumbnails
- Filter/search by type and keywords
- Brand context sidebar (colors, voice from brand-guidelines.md)
- Asset actions: Preview, Edit in Claude, Copy path, Generate
- AI Editor for in-browser asset editing
- R2-ready manifest schema for cloud sync

**API Routes:**
- `/hub` - Gallery HTML
- `/api/assets` - Asset list JSON
- `/api/brand` - Brand context JSON
- `/api/scan` - Trigger rescan
- `/file/*` - Serve local files

**Use Cases:**
- Browse marketing asset library
- Search and filter assets by category
- Edit assets with Claude AI assistance
- Generate brand-aligned assets
- Manage asset metadata and organization

**Scripts:**
- `scripts/server.cjs` - HTTP server entry
- `scripts/lib/scanner.cjs` - Asset directory scanning
- `scripts/lib/router.cjs` - HTTP routing
- `scripts/lib/brand-context.cjs` - Brand guideline extraction

**Command:** `/write:hub`

**Related Skills:** brand-guidelines, ai-multimodal, marketing-dashboard

## Design Skills

### UI Styling

**Directory:** `.claude/skills/ui-styling/`

Create beautiful interfaces with shadcn/ui and Tailwind CSS.

**Capabilities:**
- Component styling
- Responsive layouts
- Dark mode implementation
- Design system adherence

**Use Cases:**
- Style landing pages
- Create consistent components
- Implement brand colors
- Build responsive layouts

### UI/UX Pro Max

**Directory:** `.claude/skills/ui-ux-pro-max/`

Advanced UI/UX design intelligence.

**Capabilities:**
- 50 design styles
- 21 color palettes
- 50 font pairings
- 20 chart types

**Use Cases:**
- Design marketing pages
- Create dashboards
- Build e-commerce layouts
- Implement design systems

### Frontend Design

**Directory:** `.claude/skills/frontend-design/`

Frontend design patterns and implementation.

**Capabilities:**
- Component architecture
- Design patterns
- Visual hierarchy
- Animation guidance

### Frontend Design Pro

**Directory:** `.claude/skills/frontend-design-pro/`

Production-ready frontend interfaces with real images.

**Capabilities:**
- Jaw-dropping interfaces
- Unsplash/Pexels image matching
- Custom image generation prompts
- Zero AI slop, zero fake URLs

## Planning & Research Skills

### Planning

**Directory:** `.claude/skills/planning/`

Technical solution planning for scalable, secure projects.

**Capabilities:**
- Implementation planning
- Architecture design
- Trade-off analysis
- Resource planning

**Use Cases:**
- Plan campaign architecture
- Design content systems
- Create integration plans

### Research

**Directory:** `.claude/skills/research/`

Technical research and analysis.

**Capabilities:**
- Technology research
- Documentation analysis
- Best practices discovery
- Solution comparison

### Problem Solving

**Directory:** `.claude/skills/problem-solving/`

Systematic problem-solving techniques.

**Capabilities:**
- Complexity management
- Innovation techniques
- Pattern recognition
- Strategic thinking

### Sequential Thinking

**Directory:** `.claude/skills/sequential-thinking/`

Structured reasoning and analysis.

**Capabilities:**
- Step-by-step analysis
- Logical reasoning
- Decision trees
- Process mapping

## Documentation Skills

### Docs Seeker

**Directory:** `.claude/skills/docs-seeker/`

Search technical documentation and discover resources.

**Capabilities:**
- Documentation search
- Library documentation
- GitHub analysis
- Knowledge discovery

**Use Cases:**
- Find API documentation
- Research libraries
- Discover integrations

### Repomix

**Directory:** `.claude/skills/repomix/`

Package codebases for AI analysis.

**Capabilities:**
- Repository packaging
- AI-friendly output
- Token counting
- Structure analysis

**Use Cases:**
- Analyze competitor codebases
- Document project structure
- Prepare for AI review

## Integration Skills

### MCP Management

**Directory:** `.claude/skills/mcp-management/`

Manage Model Context Protocol server integrations.

**Capabilities:**
- Tool discovery
- Server management
- Capability filtering
- MCP execution

**Use Cases:**
- Connect analytics
- Integrate ad platforms
- Manage external tools

### Payment Integration

**Directory:** `.claude/skills/payment-integration/`

Payment gateway integrations.

**Capabilities:**
- SePay integration (Vietnamese)
- Polar integration (global SaaS)
- Subscription management
- Webhook handling

**Use Cases:**
- Implement checkout
- Manage subscriptions
- Process payments

## Utility Skills

### Markdown Novel Viewer

**Directory:** `.claude/skills/markdown-novel-viewer/`

Background HTTP server rendering markdown files with a calm, book-like reading experience.

**Capabilities:**
- Novel-themed UI with warm colors and serif fonts
- Dark/light theme toggle (persisted)
- Font size adjustment (S/M/L)
- Plan navigation sidebar for multi-phase plans
- Inline image rendering
- Keyboard shortcuts for navigation

**Scripts:**
- `server.cjs` - Main HTTP server for rendering markdown files
- `lib/port-finder.cjs` - Dynamic port allocation
- `lib/process-mgr.cjs` - PID file management
- `lib/http-server.cjs` - Core HTTP routing
- `lib/markdown-renderer.cjs` - Markdown to HTML conversion
- `lib/plan-navigator.cjs` - Plan detection and navigation

**References:**
- Template HTML with warm cream and dark themes
- CSS with Libre Baskerville headings, Inter body text, JetBrains Mono code
- Reader JavaScript for theme toggling and plan navigation

**Use Cases:**
- Preview markdown plans in a distraction-free environment
- View storyboards with navigation
- Read documentation with comfortable typography
- Navigate multi-phase plans with sidebar

**Slash Command:**
- `/preview <file-path>` - Quick preview markdown files
- `/preview --stop` - Stop running servers

**CLI Entry:**
```bash
node .claude/skills/markdown-novel-viewer/scripts/server.cjs --file <path> --open
```

**Features:**
- Warm cream background (light mode) with dark mode support
- Maximum 720px content width for comfortable reading
- Auto-detects plan directory structure and creates navigation
- Keyboard shortcuts: T (toggle theme), S (toggle sidebar), Left/Right (navigate phases)
- Auto-increments port if in use (3456-3500 range)

### Claude Code

**Directory:** `.claude/skills/claude-code/`

Claude Code feature documentation and guidance.

**Capabilities:**
- Slash command reference
- MCP server setup
- Hook configuration
- IDE integration

### Skill Creator

**Directory:** `.claude/skills/skill-creator/`

Guide for creating new skills.

**Capabilities:**
- Skill structure
- Best practices
- Integration patterns
- Documentation standards

### Document Skills

**Directory:** `.claude/skills/document-skills/`

Document processing utilities.

**Capabilities:**
- PDF handling
- Document conversion
- Text extraction
- Format management

### Common

**Directory:** `.claude/skills/common/`

Shared utilities and patterns.

### Template Skill

**Directory:** `.claude/skills/template-skill/`

Template for creating new skills.

## Platform & Application Skills

### Marketing Dashboard

**Directory:** `.claude/skills/marketing-dashboard/`

Local-first marketing command center for solopreneurs. Manage campaigns, content, and assets with Claude Code AI automation.

**Status:** PRODUCTION READY - All 5 phases complete

**Stack:**
- Frontend: Vue 3 + Vite + Tailwind CSS
- Backend: Hono (Node.js)
- Database: SQLite (better-sqlite3)
- Integration: Claude Code CLI

**Capabilities:**
- Campaign management with Kanban board (drag-drop status workflow)
- Content library with filters (type, campaign, status)
- Asset gallery with campaign linking
- Marketing automation panel (4 pre-built recipes)
- Dashboard with metrics and quick actions
- AI-powered content enhancement
- Markdown export with YAML frontmatter

**Database Tables:**
- `campaigns` - Marketing campaigns with status tracking
- `content` - Blog posts, social media, emails with scheduling
- `assets` - Images, videos, documents with metadata
- `automations` - AI automation recipes and execution history

**Quick Start (Development):**
```bash
# Single command start
./start.sh

# Or manual setup
cd .claude/skills/marketing-dashboard/server && npm install && npm run dev
cd .claude/skills/marketing-dashboard/app && npm install && npm run dev
```

Access at http://localhost:5173 (frontend) and http://localhost:3457 (API)

**Quick Start (Production):**
```bash
# Build
./build.sh

# Start production server
./start-production.sh

# Or manual
cd app && npm run build
cd ../server && NODE_ENV=production npm start
```

**Deployment:**
- 4 shell scripts: `start.sh`, `stop.sh`, `build.sh`, `start-production.sh`
- 1 slash command: `/dashboard [mode]` (dev, prod, build, stop)
- Single command orchestration

**Metrics (Phase 5 Complete):**
- Vue components: 26 (layout, views, features, common)
- Pinia stores: 4 (campaigns, content, assets, ai)
- API routes: 4 modules (campaigns, content, assets, ai)
- Bundle size: 56 KB gzipped (72% under 200 KB target)
- Build time: 684ms (Vite)
- Test coverage: 90% (119/132 tests passing)
- Security: Path traversal blocked, XSS protected, SQL injection prevented

**Completed Phases:**
- ✅ Phase 1: Foundation (Vue app, Hono server, SQLite schema)
- ✅ Phase 2: API Layer (CRUD routes, auth, security fixes)
- ✅ Phase 3: Vue Components (stores, views, components)
- ✅ Phase 4: Features (Kanban board, filters, automation panel)
- ✅ Phase 5: Integration (scripts, slash command, README)

**Use Cases:**
- Centralized marketing asset management
- Campaign performance monitoring
- Content automation and scheduling
- Multi-channel publishing coordination
- Marketing metrics dashboard
- Local-first content operations

**Scripts:**
- `start.sh` - Dev server with HMR (auto-installs dependencies)
- `stop.sh` - Graceful shutdown with PID cleanup
- `build.sh` - Production build verification
- `start-production.sh` - Production mode (NODE_ENV=production)
- `server/index.js` - Hono API server entry point
- `app/vite.config.js` - Frontend build configuration

**Command:**
- `/dashboard [mode]` - Launch dashboard with 4 modes (dev, prod, build, stop)

**Related Skills:** content-hub, ai-multimodal, brand-guidelines, seo-optimization, content-marketing

**Agents:** content-creator, campaign-manager, project-manager

## Marketing Skills (Phase 3 - Complete)

### SEO Optimization

**Directory:** `.claude/skills/seo-optimization/`

Complete SEO toolkit with keyword research via ReviewWeb.site API, technical SEO audits, on-page optimization, programmatic SEO, and JSON+LD schema generation. Production-ready with security fixes (XSS prevention, CSV injection protection, API key masking).

**Capabilities:**
- Technical SEO audit workflows with Core Web Vitals analysis
- Keyword research with ReviewWeb.site API (volume, difficulty, CPC, backlinks)
- Competitor domain analysis (traffic, top keywords, backlinks)
- JSON+LD schema generation (6 template types)
- Programmatic SEO (pSEO) template generation with Nunjucks
- Content gap analysis framework
- Semantic SEO implementation
- Meta tag optimization and OG tag generation
- Sitemap generation and validation
- Internal linking automation
- Mobile-first SEO checklist
- Google Search Console integration guide
- Canonical URL strategy

**Scripts (8 total):**
- `analyze-keywords.cjs` - Keyword research and competitor analysis (ReviewWeb.site API)
- `validate-schema.cjs` - JSON-LD schema validation
- `pseo-generator.cjs` - pSEO page generation with template support
- `audit-core-web-vitals.cjs` - Core Web Vitals auditing (LCP, INP, CLS)
- `generate-sitemap.cjs` - XML sitemap generation
- `generate-schema.cjs` - JSON+LD schema generator
- Plus 2 additional production utilities

**References (26 files):**
- Keyword research: research workflow, clustering methodology, content gap analysis
- Technical SEO: checklist, Core Web Vitals remediation, sitemap best practices, robots.txt config, canonical URLs, mobile SEO
- On-page SEO: comprehensive checklist, meta tags, semantic SEO, readability scoring, internal linking
- Programmatic SEO: templates, best practices, template syntax, URL structure, 100k+ page architecture
- Link building: backlink analysis, campaign planning, outreach templates, directory list
- Search Console: API guide, query patterns
- Schema: generation guide, 6 JSON+LD templates (article, product, FAQ, how-to, organization, local business)

**Use Cases:**
- SEO audit and optimization
- Keyword research and strategy with real data
- Competitor analysis (traffic, keywords, backlinks)
- Programmatic SEO engine for 100k+ pages
- Technical SEO implementation
- Core Web Vitals optimization
- Schema markup implementation
- On-page SEO optimization

**API Requirements:**
- `REVIEWWEB_API_KEY` environment variable for keyword research

### Content Marketing

**Directory:** `.claude/skills/content-marketing/`

Content strategy, editorial calendar, and content workflows.

**Capabilities:**
- Content strategy frameworks
- Editorial calendar templates
- Content pillar mapping
- Topic cluster design
- Content repurposing workflows
- Blog post structures

**Use Cases:**
- Content strategy development
- Editorial planning
- Blog content creation
- Content audit and optimization

### Social Media

**Directory:** `.claude/skills/social-media/`

Platform-specific posting, engagement, and scheduling strategies.

**Capabilities:**
- Platform-specific content formats
- Optimal posting times research
- Hashtag strategies
- Thread creation (X/Twitter)
- Engagement templates
- Cross-posting adaptation
- Viral content patterns

**Use Cases:**
- Social media content creation
- Multi-platform posting strategy
- Engagement optimization
- Cross-platform content adaptation

### Email Marketing

**Directory:** `.claude/skills/email-marketing/`

Campaign design, A/B testing, and automation sequences.

**Capabilities:**
- Email campaign frameworks
- Subject line formulas
- Drip sequence templates
- A/B test design
- Segmentation strategies
- Email compliance (CAN-SPAM, GDPR)

**Scripts:**
- `validate-email-list.cjs`

**Use Cases:**
- Email campaign design
- Drip sequence automation
- Deliverability optimization
- Compliance management

### Analytics

**Directory:** `.claude/skills/analytics/`

GA4 analysis, reporting, and performance tracking.

**Capabilities:**
- GA4 query patterns
- Custom event tracking
- Conversion tracking setup
- Dashboard design
- KPI definitions
- Attribution models
- Report templates

**Use Cases:**
- Analytics setup and configuration
- Performance analysis
- KPI tracking and reporting
- Attribution modeling

### Campaign Management

**Directory:** `.claude/skills/campaign-management/`

Campaign planning, execution, and measurement.

**Capabilities:**
- Campaign brief templates
- Launch checklist workflows
- Multi-channel coordination
- Budget allocation frameworks
- Timeline management
- ROI calculation methods

**Use Cases:**
- Campaign planning and strategy
- Multi-channel execution
- Budget optimization
- Post-campaign analysis

### Brand Guidelines

**Directory:** `.claude/skills/brand-guidelines/`

Comprehensive brand identity, asset management, and consistency enforcement system.

**Capabilities:**
- Brand guideline templates and documentation
- Color palette management and accessibility compliance
- Typography specifications with CSS variables
- Voice and tone frameworks
- Asset directory structure and naming conventions
- Asset validation and approval workflows
- Brand context injection for content generation
- Color extraction and compliance checking

**Scripts:**
- `inject-brand-context.cjs` - Extract brand context for prompt injection
- `validate-asset.cjs` - Validate asset naming, size, format compliance
- `extract-colors.cjs` - Extract colors and compare against brand palette

**References:**
- `brand-guideline-template.md` - Comprehensive template for brand documentation
- `asset-organization.md` - Directory structure and naming conventions
- `color-palette-management.md` - Color systems and accessibility
- `typography-specifications.md` - Fonts, scales, CSS implementation
- `logo-usage-rules.md` - Logo variants and placement rules
- `approval-checklist.md` - Asset review and approval process
- Plus existing voice, visual identity, messaging, and consistency docs

**Templates:**
- `brand-guidelines-starter.md` - Complete starter template for new brands

**Asset Structure:**
```
.assets/           # Git-tracked metadata (manifest, tags, versions)
assets/            # Raw files (designs, banners, logos, videos, infographics, generated)
```

**Integration:**
- Uses `ai-multimodal` skill for Imagen 4 brand-aligned image generation
- Integrates with `content-marketing` for voice consistency
- Works with all content-generating agents

**Use Cases:**
- Brand guideline creation and documentation
- Style guide development
- Asset organization and management
- Brand compliance validation
- Automated brand context injection
- Asset approval workflows
- Color palette enforcement

### Video Production

**Directory:** `.claude/skills/video-production/`

AI-powered video marketing with script generation, storyboards, Veo 3.1/Imagen 4 integration, and platform optimization.

**Capabilities:**
- Video script generation (6 template formats)
- Storyboard creation with keyframes (Imagen 4)
- Veo 3.1 video generation and prompt engineering
- Video analysis and quality review (Gemini)
- Platform-specific optimization (YouTube, TikTok, Reels, LinkedIn)
- Automatic caption extraction and transcription
- Thumbnail design and generation
- Video SEO optimization
- Multi-platform repurposing workflows

**Scripts:**
- `generate-video.cjs` - Veo 3.1 video generation with template support
- `create-storyboard.cjs` - Imagen 4 storyboard with keyframes
- `analyze-video.cjs` - Gemini video understanding and quality review
- `optimize-for-platform.cjs` - FFmpeg aspect ratio conversion
- `extract-captions.cjs` - Automatic caption extraction

**Templates:**
- `product-demo.json` - Product showcase and feature demos
- `explainer.json` - Educational and how-to content
- `testimonial.json` - Customer success stories
- `short-form.json` - TikTok/Reels/Shorts optimized

**References:**
- Video type and platform specifications (16:9, 9:16, durations)
- Veo 3.1 prompt engineering best practices
- Storyboard format with timing and visuals
- Audio directive guide for music/SFX
- Thumbnail design principles and templates
- Video SEO optimization guide
- Production workflow templates

**Integration:**
- Uses `ai-multimodal` skill for Veo 3.1 and Imagen 4 APIs
- Uses `media-processing` skill for FFmpeg optimization
- Integrates with `content-marketing` for strategy
- Integrates with `social-media` for distribution

**Use Cases:**
- Product demo videos for websites
- Educational explainer content
- Customer testimonial videos
- Short-form social content (Reels, TikTok, Shorts)
- Video SEO optimization for YouTube
- Multi-platform video repurposing
- Thumbnail A/B testing strategies

**Cost & Performance:**
- Per-video cost: $3-6 (Veo, Imagen, Gemini)
- Generation time: 15-25 minutes per video
- Supported video lengths: 30 seconds to 12 hours (platform dependent)

### Ads Management

**Directory:** `.claude/skills/ads-management/`

Meta Ads and Google Ads creation and optimization.

**Capabilities:**
- Ad copy frameworks (AIDA, PAS, etc.)
- Platform-specific ad specs
- Audience targeting strategies
- Budget optimization
- A/B testing frameworks
- Performance benchmarks

**Use Cases:**
- Ad campaign creation
- Ad copy development
- Audience targeting optimization
- Performance optimization

## Skill Activation

Skills are automatically activated when relevant to the task. To manually activate:

```
Use the {skill-name} skill to {task description}.
```

Example:
```
Use the ai-multimodal skill to generate a product hero image.
```

## Creating Custom Skills

1. Copy `.claude/skills/template-skill/`
2. Rename to your skill name
3. Update the skill description in `skill.md`
4. Add reference files as needed
5. Add scripts if automation required
6. Document in this catalog

## Skill Best Practices

1. **Keep Focused**: One skill = one domain
2. **Document Well**: Clear description and examples
3. **Include Examples**: Show common use cases
4. **Test Thoroughly**: Verify skill functionality
5. **Stay Current**: Update with new capabilities
