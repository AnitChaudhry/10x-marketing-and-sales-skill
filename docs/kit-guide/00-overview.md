# ClaudeKit Marketing Guide - Complete Overview

## What is ClaudeKit Marketing?

ClaudeKit Marketing is an AI-powered toolkit for sales and marketing automation built on Claude Code's subagent orchestration. It provides 32 specialized agents, 56 skills, and 106 slash commands for marketing workflows.

**Core Purpose:** Enable indie hackers, marketing teams, and SMBs to create professional marketing content through intelligent agent coordination.

## Kit Structure

```
.claude/
├── agents/          # 32 specialized marketing agents
├── commands/        # 106 slash commands
├── skills/          # 56 skills (references + scripts)
├── workflows/       # 10 workflow definitions
├── hooks/           # Session automation
└── scripts/         # Utility scripts
```

## Implementation Status

### Fully Tested & Working

| Component | Status | Description |
|-----------|--------|-------------|
| `/design:generate` | **Working** | Imagen 4 image generation with brand context |
| `/youtube:infographic` | **Working** | YouTube → infographic pipeline |
| `/test:workflow` | **Working** | Manual workflow testing framework |
| Marketing Dashboard | **Working** | Vue + Hono API, asset gallery, previews |
| Brand injection | **Working** | `inject-brand-context.cjs` |
| VidCap API | **Working** | Video info, summary, transcript extraction |
| youtube-transcript-api | **Working** | Python transcript extraction |

### Scripts with Actual Code

| Skill | Scripts |
|-------|---------|
| `ai-multimodal` | `gemini_batch_process.py` - Imagen 4 generation |
| `youtube-handling` | `vidcap.py` - VidCap API integration |
| `brand-guidelines` | `inject-brand-context.cjs`, `sync-brand-to-tokens.cjs` |
| `marketing-dashboard` | Full Vue app + Hono server |
| `test-orchestrator` | `scan-components.py` |
| `document-skills` | PDF, PPTX, DOCX manipulation |

### Reference-Only Skills (No Automation Scripts)

These skills provide knowledge/references for Claude but lack executable scripts:
- `copywriting` - Writing formulas and templates
- `seo-optimization` - SEO guidelines and checklists
- `campaign-management` - Campaign frameworks
- `analytics` - Metrics definitions
- `social-media` - Platform strategies
- `email-marketing` - Automation flow references

## Quick Command Reference

| Category | Tested Commands |
|----------|-----------------|
| **Design** | `/design:generate` ✓, `/design:good` ✓ |
| **YouTube** | `/youtube:infographic` ✓, `/youtube:blog` ✓, `/youtube:social` ✓ |
| **Content** | `/write:blog` ✓, `/write:cro` ✓, `/write:enhance` ✓ |
| **Copywriting** | `/copy:formula` ✓ |
| **Email** | `/email:sequence` ✓ |
| **Social** | `/social` ✓, `/social:schedule` (plan only) |
| **Testing** | `/test:workflow` ✓ |
| **Dashboard** | `/dashboard` ✓ |

## Marketing Dashboard

**URL:** `http://localhost:5174` (dev) | Port 3457 (API)

Features:
- Asset Gallery with category filtering
- Preview support: Images, Videos, Slides, Infographics, Transcripts
- Live scanner for `assets/` directory
- Brand Center integration

**Start:**
```bash
cd .claude/skills/marketing-dashboard && ./start-dashboard.sh
```

## Verified Workflows

### 1. On-Brand Image Generation
```bash
/design:generate "hero banner for landing page"
```
Flow: Brand context → AI prompt enhancement → Imagen 4 → assets/

### 2. YouTube to Infographic
```bash
/youtube:infographic "https://youtube.com/watch?v=xxx"
```
Flow: VidCap API → Summary extraction → HTML infographic → assets/infographics/

### 3. Copywriting with Formulas
```bash
/copy:formula PAS "email deliverability problems"
/copy:formula AIDA "SaaS product launch"
```
Flow: Brand context → Formula selection → 3 copy variants (short/medium/long) → assets/copy/formulas/

### 4. Email Sequence Generation
```bash
/email:sequence welcome
/email:sequence onboarding "project management SaaS"
```
Flow: Brand context → Sequence plan → Full email copy with subject lines → assets/copy/emails/

### 5. Video Transcription
```bash
# Via youtube-transcript-api (Python)
python3 -c "from youtube_transcript_api import YouTubeTranscriptApi; ..."
```

## Gap Analysis (vs task.md)

### Completed ✅

- [x] Content marketing skill (`compose-blog-post`, `content-audit`, `content-strategy-framework`, `editorial-calendar-template`)
- [x] Email marketing skill (`automation-flows`, `deliverability-checklist`, `email-templates`, `subject-line-formulas`)
- [x] Social media skill
- [x] Mini app (Dashboard with asset gallery, brand center)
- [x] `/dashboard` command
- [x] Image generation with brand context (`/design:generate`, `ai-multimodal`)
- [x] `/youtube:infographic` (VidCap → Gemini)
- [x] `/write:blog` (SEO-optimized articles)
- [x] `/write:cro`, `/write:enhance`
- [x] `/youtube:blog`, `/youtube:social`
- [x] Hook writing (references/hook-writing.md)
- [x] Copy writing styles
- [x] Story/Reel images (9:16 aspect ratio)

### In Progress 🔄

- [ ] **Design skill**
  - [ ] brand-guideline (partial - inject-brand-context.cjs exists)
  - [ ] design-system (basic - design-tokens.json exists)
  - [ ] replicate.com/qwen/qwen-image-layered integration

### High Priority Gaps ❌

1. **Slides creation** - `/slides:create` exists but interactive HTML/JS/CSS not fully implemented
2. **Social media posting APIs:**
   - X (Twitter)
   - Facebook Page
   - Threads
   - Instagram
   - YouTube
   - TikTok
3. **Copywriting skill** - References only, no automation scripts

### Medium Priority Gaps

4. **External integrations:**
   - Google Drive
   - Cloudflare R2
   - Email providers (Mailchimp, SendGrid, Resend)
5. **Campaign orchestration** - References only
6. **A/B testing automation**

### Lower Priority

7. **Analytics integrations** (GA4, Mixpanel)
8. **SEO tools** (Ahrefs, SEMrush)
9. **Multi-language content**
10. **Lead scoring automation**

## File Organization

```
assets/
├── banners/           # Hero images, headers
├── copy/              # Written content
│   ├── emails/        # Email sequences
│   ├── formulas/      # Formula-based copy
│   ├── headlines/     # Headline variants
│   └── landing-pages/ # Landing page copy
├── designs/           # Visual assets
├── images/            # General images
├── infographics/      # HTML/PNG infographics
├── logos/             # Brand logos
├── slides/            # HTML presentations
├── transcripts/       # VTT/SRT files
└── videos/            # Video files

docs/
├── brand-guidelines.md    # Brand source of truth
├── design-guidelines.md   # Visual standards
└── kit-guide/            # This documentation
```

## Documentation Structure

| File | Content |
|------|---------|
| 00-overview.md | This file - status & gaps |
| 01-brand-system.md | Brand guidelines workflow |
| 02-image-generation.md | Imagen 4, design commands |
| 03-video-production.md | Video scripts, storyboards |
| 04-content-creation.md | Writing workflows |
| 05-social-media.md | Platform strategies |
| 06-campaign-management.md | Campaign frameworks |
| 07-seo-optimization.md | SEO process |
| 08-project-setup.md | Kit initialization |
| 09-scripts-reference.md | Script documentation |
| 10-marketing-dashboard.md | Dashboard guide |

## Next Steps

1. **For Users:** Start with `/design:generate` - it's fully working
2. **For Contributors:** Add scripts to reference-only skills
3. **For Testing:** Use `/test:workflow` for manual verification
