# 10x Marketing & Sales Skill

<div align="center">

**The Ultimate Marketing & Sales Automation Suite for Claude Code**

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet?style=for-the-badge)](https://claude.ai/code)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-103+-blue?style=for-the-badge)](#skills-included)
[![Commands](https://img.shields.io/badge/Commands-127+-orange?style=for-the-badge)](#commands)

[Installation](#-installation) • [Quick Start](#-quick-start) • [Features](#-features) • [Documentation](#-documentation)

</div>

---

## What is This?

**10x Marketing & Sales Skill** is a comprehensive Claude Code skill that combines:

1. **🚀 Multi-Platform Outreach** - Automated campaigns on LinkedIn, Twitter, Instagram, Gmail
2. **🎨 Canva Integration** - Design automation + local file editing (PDF/PPTX/DOCX/XLSX)
3. **📄 Landing Page Generation** - Multi-agent workflow for 5 tech stacks
4. **🖼️ Visual Workflow Canvas** - TLDraw-powered drag-and-drop sequence designer

---

## 🚀 Installation

### One-Line Install (Recommended)

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/AnitChaudhry/10x-marketing-and-sales-skill/main/.claude/skills/10x-team/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/AnitChaudhry/10x-marketing-and-sales-skill/main/.claude/skills/10x-team/install.ps1 | iex
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/AnitChaudhry/10x-marketing-and-sales-skill.git

# Copy the skill to your Claude Code project
cp -r 10x-marketing-and-sales-skill/.claude/skills/10x-team ~/.claude/skills/

# Install canvas dependencies (optional, for visual workflow)
cd 10x-marketing-and-sales-skill/canvas
npm install
```

---

## ⚡ Quick Start

### 1. Start Claude Code
```bash
claude
```

### 2. Use the Skill
```
/10x
```

Claude will ask clarifying questions to determine what you need:
- **Outreach Automation** → LinkedIn, Twitter, Instagram, Gmail campaigns
- **Canva & Design** → Canva API, file editing
- **Landing Page** → Generate full landing pages

### 3. Direct Commands
```
/10x start              # Launch visual workflow canvas
/10x linkedin connect   # LinkedIn outreach
/10x twitter dm         # Twitter DMs
/10x canva export       # Export Canva designs
/10x lp                 # Create landing page
```

---

## ✨ Features

### 🎯 Outreach Automation

| Platform | Capabilities |
|----------|-------------|
| **LinkedIn** | Connect, message, like, comment, InMail |
| **Twitter/X** | Follow, DM, like, reply, retweet, quote |
| **Instagram** | Follow, DM, like, comment, story reply |
| **Gmail** | Send, reply, campaigns, newsletters |

**Built-in Safety:**
- Intelligent rate limiting (won't get you banned)
- Max 2 touches per person per day
- 24+ hour gaps between platforms
- Automatic stop on response

### 🎨 Canva & File Editing

| Feature | Description |
|---------|-------------|
| **Canva Cloud** | Browse, create, export, brand kits |
| **PDF Editor** | Read, modify, merge, split, extract |
| **PowerPoint** | Edit slides, text, images, notes |
| **Word** | Modify documents, tables, formatting |
| **Excel** | Update cells, formulas, sheets |

**File Safety:** Original files are NEVER modified - all edits on copies.

### 📄 Landing Page Generation

| Tech Stack | Description |
|------------|-------------|
| **HTML** | Static HTML/CSS/JS (no build step) |
| **React** | React 18 with Vite |
| **Next.js** | Next.js 14 App Router |
| **Astro** | Astro 4 - fast static sites |
| **Vue** | Vue 3 with Vite |

**Multi-Agent Workflow:**
1. **Discovery** → Requirements analysis
2. **Copywriting** → Headlines, copy, CTAs
3. **Design** → Visual strategy, colors, typography
4. **Build** → Code generation
5. **QA** → Testing preparation
6. **Launch** → Deployment & SEO

### 🖼️ Visual Workflow Canvas

A drag-and-drop infinite canvas (TLDraw) for designing outreach sequences:

```
/10x start
```

- **Add nodes** for Discovery, LinkedIn, Twitter, Instagram, Email, Delay
- **Connect nodes** by dragging
- **Export workflows** as JSON
- **Execute** with `/10x workflow run`

---

## 📊 Skills Included

**103 skills** organized into modules:

### Core Marketing Skills
- `copywriting` - Conversion formulas, headlines, CTAs
- `email-marketing` - Campaigns, drip sequences
- `social-media` - Platform-specific content
- `seo-optimization` - Keyword research, audits
- `campaign-management` - Campaign briefs, tracking
- `analytics` - GA4 analysis, KPIs
- `brand-guidelines` - Asset management, consistency

### 10x-Team Module (40+ sub-skills)
- `outreach/*` - LinkedIn, Twitter, Instagram, Gmail adapters
- `canva/*` - Canva API integration
- `landing-page/*` - Multi-agent page generation

### Development Skills
- `frontend-development` - React, TypeScript, Vite
- `backend-development` - Node.js, Python, APIs
- `databases` - MongoDB, PostgreSQL
- `devops` - Docker, CI/CD

[Full skill catalog →](docs/skill-catalog.md)

---

## 🎮 Commands

**127 commands** available:

### 10x Commands
| Command | Description |
|---------|-------------|
| `/10x` | Interactive module selection |
| `/10x start` | Launch visual canvas |
| `/10x workflow` | Create/run workflows |
| `/10x linkedin` | LinkedIn automation |
| `/10x twitter` | Twitter automation |
| `/10x instagram` | Instagram automation |
| `/10x canva` | Canva & file editing |
| `/10x lp` | Landing page generation |
| `/10x discover` | Find people with Exa AI |

### Other Commands
| Command | Description |
|---------|-------------|
| `/email` | Email content generation |
| `/social` | Social media content |
| `/write/blog` | SEO blog posts |
| `/campaign` | Campaign management |
| `/design/good` | High-quality designs |

[Full command catalog →](docs/command-catalog.md)

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file:

```env
# Outreach (Gmail)
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_secret
SENDER_EMAIL=your@gmail.com
SENDER_NAME=Your Name

# Discovery (Exa AI)
EXA_API_KEY=your_exa_key

# Canva
CANVA_CLIENT_ID=your_client_id
CANVA_CLIENT_SECRET=your_client_secret
CANVA_ACCESS_TOKEN=your_token

# AI (for multimodal features)
GEMINI_API_KEY=your_gemini_key

# Rate Limits (optional)
LINKEDIN_CONNECTIONS_PER_DAY=20
TWITTER_FOLLOWS_PER_DAY=50
INSTAGRAM_FOLLOWS_PER_DAY=30
```

### Prerequisites

- **Claude Code** - [claude.ai/code](https://claude.ai/code)
- **Node.js 18+** - For visual canvas and landing pages
- **Python 3.9+** - For automation scripts
- **Browser-Use MCP** - For platform automation (included in Claude Code)

---

## 📁 Project Structure

```
10x-marketing-and-sales-skill/
├── .claude/
│   ├── skills/
│   │   ├── 10x-team/              # Main unified skill
│   │   │   ├── SKILL.md           # Skill definition
│   │   │   ├── README.md          # This file
│   │   │   ├── outreach/          # Outreach module
│   │   │   │   ├── skills/        # 17 sub-skills
│   │   │   │   ├── scripts/       # Python automation
│   │   │   │   ├── templates/     # 85+ message templates
│   │   │   │   └── workflows/     # Pre-built sequences
│   │   │   ├── canva/             # Canva module
│   │   │   │   ├── skills/        # 24 sub-skills
│   │   │   │   └── scripts/       # Canva API + file utils
│   │   │   └── landing-page/      # Landing page module
│   │   │       ├── agents/        # 7 specialist agents
│   │   │       ├── knowledge/     # Reference docs
│   │   │       └── scripts/       # Generator scripts
│   │   └── ... (60+ other skills)
│   └── commands/
│       ├── 10x.md                 # Main command
│       ├── 10x/                   # Sub-commands
│       └── ... (100+ other commands)
├── canvas/                        # TLDraw visual workflow app
├── projects/                      # Landing page outputs
├── input/                         # Input files
├── output/                        # Generated outputs
└── docs/                          # Documentation
```

---

## 📖 Documentation

- [Skill Catalog](docs/skill-catalog.md) - All 103 skills
- [Command Catalog](docs/command-catalog.md) - All 127 commands
- [Agent Catalog](docs/agent-catalog.md) - All agents
- [Outreach Templates](docs/templates.md) - 85+ message templates
- [API Reference](docs/api-reference.md) - Script documentation

---

## 🔐 Safety & Best Practices

### Outreach Safety
- ✅ Never exceed platform rate limits
- ✅ Warm up accounts before bulk outreach
- ✅ Stop sequences when prospect responds
- ✅ Use templates as starting points, personalize

### File Safety
- ✅ Original files are NEVER modified
- ✅ All edits work on copies
- ✅ Full audit trail maintained

### Platform Rate Limits

| Platform | Action | Daily Limit | Delay |
|----------|--------|-------------|-------|
| LinkedIn | Connections | 20 | 2-10 min |
| LinkedIn | Messages | 50 | 2-10 min |
| Twitter | Follows | 50 | 1-5 min |
| Instagram | Follows | 30 | 1.5-7 min |
| Gmail | Emails | 100 | 1-3 min |

---

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

```bash
# Fork the repo
# Create feature branch
git checkout -b feature/amazing-feature

# Commit changes
git commit -m "Add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
```

---

## 📄 License

MIT License - Free to use, modify, and distribute.

---

## 🙏 Credits

- **ClaudeKit Marketing** - Base framework
- **TLDraw** - Visual canvas
- **Browser-Use MCP** - Platform automation

---

<div align="center">

**Built with ❤️ for Claude Code**

[Report Bug](https://github.com/AnitChaudhry/10x-marketing-and-sales-skill/issues) • [Request Feature](https://github.com/AnitChaudhry/10x-marketing-and-sales-skill/issues)

</div>
