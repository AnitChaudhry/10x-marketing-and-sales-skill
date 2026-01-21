---
name: 10x-team
description: Unified marketing automation suite combining multi-platform outreach (LinkedIn, Twitter, Instagram, Gmail), Canva design automation, and landing page generation. Activate for automated outreach campaigns, visual workflow design, Canva integration, file editing (PDF/PPTX/DOCX/XLSX), or landing page creation across 5 tech stacks.
license: MIT
---

# 10x Team - Marketing & Sales Automation Suite

Unified skill combining outreach automation, design tools, and landing page generation.

## When to Use

- **Outreach Automation** - Automated LinkedIn, Twitter, Instagram, Gmail campaigns
- **Visual Workflow Design** - TLDraw canvas for multi-platform sequences
- **Canva Integration** - Design management, export, brand kits
- **File Editing** - PDF, PPTX, DOCX, XLSX manipulation
- **Landing Pages** - Multi-agent page generation (HTML/React/Next.js/Astro/Vue)

## Modules Overview

### Module 1: Outreach Automation
Load: `outreach/skills/*/SKILL.md`

| Skill | Purpose |
|-------|---------|
| `canvas-workflow` | Visual workflow designer (TLDraw) |
| `workflow-engine` | Multi-platform sequence execution |
| `linkedin-adapter` | LinkedIn automation |
| `twitter-adapter` | Twitter/X automation |
| `instagram-adapter` | Instagram automation |
| `gmail-adapter` | Gmail sending |
| `discovery-engine` | Find people with Exa AI |
| `team-manager` | Multi-user credentials |
| `rate-limiter` | Platform-safe rate limiting |

### Module 2: Canva & File Editing
Load: `canva/skills/*/SKILL.md`

| Skill | Purpose |
|-------|---------|
| `canva-manager` | Main Canva orchestrator |
| `canva-design` | Create/edit designs |
| `canva-export` | Export to formats |
| `canva-brand-kit` | Brand consistency |
| `local-pdf-editor` | PDF manipulation |
| `local-pptx-editor` | PowerPoint editing |
| `local-docx-editor` | Word editing |
| `local-xlsx-editor` | Excel editing |

### Module 3: Landing Page Generation
Load: `landing-page/SKILL.md`

| Agent | Phase | Output |
|-------|-------|--------|
| Discovery | 1 | `requirements/brief.json` |
| Copywriting | 2 | `copy/headlines.md`, `copy/page-copy.md` |
| Design | 3 | `design/strategy.md`, `colors.json` |
| Build | 4 | Tech-stack specific code |
| QA | 5 | `testing/test-kit.md` |
| Launch | 6 | `launch/checklist.md` |

## Clarifying Questions

When user invokes `/10x`, ask via `AskUserQuestion`:

**Question 1:** Which module do you want to use?
- Outreach Automation (LinkedIn, Twitter, Instagram, Email)
- Canva & Design
- Landing Page Generation

**Question 2 (Outreach):** What action?
- Start visual canvas
- Create workflow
- Execute outreach on specific platform
- Find people (discovery)

**Question 2 (Canva):** What action?
- Browse/manage designs
- Export design
- Edit local file (PDF/PPTX/DOCX/XLSX)

**Question 2 (Landing Page):** What action?
- New project
- Resume existing project
- List projects

## Rate Limits (Built-in Safety)

| Platform | Action | Daily Limit | Delay |
|----------|--------|-------------|-------|
| LinkedIn | Connections | 20 | 2-10 min |
| LinkedIn | Messages | 50 | 2-10 min |
| Twitter | Follows | 50 | 1-5 min |
| Twitter | DMs | 50 | 1-5 min |
| Instagram | Follows | 30 | 1.5-7 min |
| Instagram | DMs | 30 | 1.5-7 min |
| Gmail | Emails | 100 | 1-3 min |

## Tech Stacks (Landing Pages)

| Stack | Command | Run |
|-------|---------|-----|
| HTML | `generate-html.js` | Open in browser |
| React | `generate-react.js` | `npm run dev` |
| Next.js | `generate-nextjs.js` | `npm run dev` |
| Astro | `generate-astro.js` | `npm run dev` |
| Vue | `generate-vue.js` | `npm run dev` |

## Environment Setup

```env
# Outreach
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_secret
SENDER_EMAIL=your@gmail.com
EXA_API_KEY=your_exa_key

# Canva
CANVA_CLIENT_ID=your_client_id
CANVA_CLIENT_SECRET=your_client_secret
CANVA_ACCESS_TOKEN=your_token

# Rate Limits (optional)
LINKEDIN_CONNECTIONS_PER_DAY=20
TWITTER_FOLLOWS_PER_DAY=50
INSTAGRAM_FOLLOWS_PER_DAY=30
```

## References

| File | Purpose |
|------|---------|
| `outreach/templates/` | 85+ message templates |
| `outreach/workflows/examples/` | Pre-built workflow sequences |
| `canva/scripts/` | Canva API scripts |
| `landing-page/knowledge/` | Copywriting & design knowledge |
| `landing-page/agents/` | Specialist agent definitions |

## Agent Integration

**Primary Agents:**
- `email-wizard` - Email strategy (uses outreach module)
- `social-media-manager` - Social automation (uses outreach module)
- `ui-ux-designer` - Visual design (uses canva module)
- `content-creator` - Landing page content (uses landing-page module)

**Skill Dependencies:**
- `copywriting` - For message templates
- `email-marketing` - For email best practices
- `social-media` - For platform specs
- `brand-guidelines` - For brand consistency

## Differentiation from Existing Skills

| Existing Skill | Creates | 10x-Team | Does |
|----------------|---------|----------|------|
| `email-marketing` | Email content | `outreach/gmail-adapter` | SENDS emails |
| `social-media` | Social posts | `outreach/linkedin-adapter` | SENDS on LinkedIn |
| `social-media` | Social posts | `outreach/twitter-adapter` | SENDS on Twitter |
| `social-media` | Social posts | `outreach/instagram-adapter` | SENDS on Instagram |
| `creativity` | Design ideas | `canva/canva-*` | Creates in Canva |
| `frontend-design` | UI mockups | `landing-page/*` | Generates full code |

## Folder Mapping

All modules use standardized folder structure for inputs, outputs, and resources:

### Root-Level Folders

| Folder | Purpose | Used By |
|--------|---------|---------|
| `input/` | Input files for processing | Canva file editors, workflow engine |
| `output/` | Generated outputs | All modules |
| `output/workflows/` | Saved workflow JSONs | Outreach module |
| `output/canva/` | Canva exports | Canva module |
| `output/discoveries/` | Discovery results | Outreach discovery |
| `projects/` | Landing page projects | Landing page module |
| `projects/{name}/` | Individual project | Landing page agents |
| `credentials/` | OAuth tokens, API keys | Gmail, Canva adapters |
| `user-preferences/` | User configs, saved settings | All modules |
| `assets/` | Marketing assets | Brand, design skills |
| `campaigns/` | Campaign definitions | Campaign workflows |
| `canvas/` | TLDraw visual workflow app | Outreach canvas |

### Skill-Internal Folders

| Path | Purpose |
|------|---------|
| `outreach/templates/` | 85+ message templates (LinkedIn, Twitter, Instagram, Email) |
| `outreach/templates/linkedin/` | LinkedIn connection, message, InMail templates |
| `outreach/templates/twitter/` | Twitter DM, reply, tweet templates |
| `outreach/templates/instagram/` | Instagram DM, comment, story templates |
| `outreach/templates/email/` | Email outreach, follow-up, newsletter templates |
| `outreach/workflows/examples/` | Pre-built workflow sequences (B2B, Influencer, Investor) |
| `outreach/scripts/` | Python automation scripts |
| `canva/scripts/` | Canva API client and utilities |
| `canva/scripts/local/` | Local file editors (PDF, PPTX, DOCX, XLSX) |
| `landing-page/agents/` | 7 specialist agent definitions |
| `landing-page/knowledge/` | 9 reference docs (headlines, colors, typography, etc.) |
| `landing-page/scripts/` | Generator scripts for 5 tech stacks |

### Output Paths by Module

**Outreach Module:**
```
output/
├── workflows/           # Saved workflow JSONs
│   └── {name}.json
├── discoveries/         # Discovery results
│   └── {date}-{query}.json
├── campaigns/           # Campaign execution logs
│   └── {name}/
└── reports/             # Outreach reports
    └── {date}-{type}.md
```

**Canva Module:**
```
output/
├── canva/              # Canva exports
│   ├── exports/        # Exported designs (PNG, PDF, etc.)
│   └── working/        # Working copies for file editing
└── files/              # Edited local files
    └── {original-name}/
```

**Landing Page Module:**
```
projects/
└── {project-name}/
    ├── requirements/   # Phase 1: Discovery output
    │   └── brief.json
    ├── copy/           # Phase 2: Copywriting output
    │   ├── headlines.md
    │   └── page-copy.md
    ├── design/         # Phase 3: Design output
    │   ├── strategy.md
    │   ├── colors.json
    │   └── typography.json
    ├── build/          # Phase 4: Generated code
    │   └── {tech-stack-specific}
    ├── testing/        # Phase 5: QA output
    │   └── test-kit.md
    ├── launch/         # Phase 6: Launch output
    │   ├── checklist.md
    │   └── maintenance.md
    └── status.json     # Project status tracking
```

### Samples & References

| Folder | Contains |
|--------|----------|
| `assets/writing-styles/` | User writing style samples |
| `docs/brand-guidelines.md` | User brand guidelines |
| `campaigns/` | Campaign configuration files |
| `guide/` | User guides and documentation |

### File Safety

**Input Protection:**
- Original files in `input/` are NEVER modified
- All edits work on copies in `output/working/`
- Final results saved to `output/`

**Credential Security:**
- OAuth tokens stored in `credentials/`
- Never committed to git (in .gitignore)
- Encrypted where possible

## Best Practices

1. Always warm up accounts before bulk outreach
2. Never exceed platform rate limits
3. Stop sequences when prospect responds
4. Use templates as starting points, personalize
5. Test landing pages on all devices
6. Original files never modified (copies only)
7. Keep credentials in `credentials/` folder
8. Use `input/` for source files, `output/` for results
