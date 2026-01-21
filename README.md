# ClaudeKit Marketing

AI-powered marketing automation toolkit built on Claude Code subagent orchestration. Enables autonomous workflows for content creation, campaign management, SEO optimization, and lead generation.

**Status:** Phase 6 Complete (27 agents, 73+ commands, 28+ skills, 8 MCP integrations) | Production Ready
**Pricing:** $99 standalone | $149 bundled with ClaudeKit Engineer

## What is Claude Code?

Claude Code is Anthropic's official CLI that orchestrates AI agents for intelligent task automation. Learn more at [Claude Code](https://claude.com/product/claude-code).

## Quick Start

### Prerequisites
- Claude Code installed and configured
- Git and 4GB+ RAM
- macOS 10.15+, Ubuntu 20.04+, or Windows 10+ with WSL

### Installation

```bash
npm install -g claudekit-cli
ck new --dir my-project --kit marketing
cd my-project
claude
```

### Usage Examples

```bash
# Content creation
/plan "Q1 content strategy"
/content/good "landing page copy"
/content/cro "optimize for conversions"

# Campaign management
/campaign:email "Black Friday sequence"
/brainstorm "seasonal campaign ideas"

# SEO & analysis
/seo:keywords "target keyword research"
/scout "analyze competitor pages"
```

## Key Features

- **27 Specialized Agents** - TOFU, MOFU, BOFU funnel stages + core & support roles
- **73+ Commands** - Content, campaigns, SEO, social, email, analytics, design, fixes
- **28+ Skills** - AI/multimodal, design, strategy, marketing, integrations
- **8 MCP Integrations** - GA4, Google Ads, SendGrid, Discord, Slack, Resend, GSC, ReviewWeb
- **6 Workflow Systems** - Campaign, content, sales, SEO, analytics, orchestration
- **3 Automation Hooks** - Brand enforcement, campaign tracking, approvals
- **Marketing Dashboard** - Full-stack Vue 3 app (32 components, 5 stores, production-ready)

## Documentation

- **[Project Overview & PDR](./docs/project-overview-pdr.md)** - Requirements and roadmap
- **[Agent Catalog](./docs/agent-catalog.md)** - 27 agents by funnel stage
- **[Skill Catalog](./docs/skill-catalog.md)** - 28+ available skills
- **[Command Catalog](./docs/command-catalog.md)** - 73+ commands reference
- **[Code Standards](./docs/code-standards.md)** - Development guidelines
- **[System Architecture](./docs/system-architecture.md)** - Design and patterns
- **[Design Guidelines](./docs/design-guidelines.md)** - Brand and visual standards
- **[Project Roadmap](./docs/project-roadmap.md)** - Timeline and phases

## Marketing Agents (27 Total)

**TOFU:** Attraction Specialist, SEO Specialist, Lead Qualifier, Researcher
**MOFU:** Email Wizard, Sale Enabler, Funnel Architect, Content Creator, Continuity Specialist
**BOFU:** Upsell Maximizer
**Core:** Copywriter, Brainstormer, Content Reviewer, Campaign Debugger, Campaign Manager
**Community:** Social Media Manager, Community Manager
**Support:** Planner, Project Manager, Docs Manager, Git Manager, Journal Writer, Scout, Scout External, MCP Manager, UI/UX Designer

## Project Structure

```
.claude/
├── agents/          # 27 marketing agents
├── commands/        # 73+ slash commands (118 files)
├── skills/          # 28+ skills (2,664 files)
├── workflows/       # 10 workflow definitions
└── hooks/           # 7 automation hooks

docs/
├── Core documentation (6 files)
├── Reference catalogs (3 files)
├── Brand & design (2 files)
├── Integration guides (2 files)
└── Strategic docs (2+ files)
```

## Marketing Dashboard

Full-stack web application for campaign management and AI automation:

- **Frontend:** Vue 3 + Vite (32 components, 5 Pinia stores)
- **Backend:** Hono + SQLite (5 API routes, 18+ endpoints)
- **Features:** Campaign Kanban, content library, asset gallery, AI enhancement, brand center
- **Security:** API key auth, path traversal protection, XSS prevention
- **Performance:** 62 KB gzipped (68% under 200 KB target)
- **Status:** Production ready (88% test coverage)

**Quick Start:**
```bash
cd .claude/skills/marketing-dashboard
./start.sh              # Dev: localhost:5173 (frontend) + localhost:3457 (API)
./build.sh && ./start-production.sh  # Production
```

## Environment Configuration

Set up MCP integrations for advanced features:

```bash
cp .claude/.env.example .claude/.env

# Required for integrations:
GEMINI_API_KEY=...
GA_ACCESS_TOKEN=...
GOOGLE_ADS_DEVELOPER_TOKEN=...
SENDGRID_API_KEY=...
DISCORD_BOT_TOKEN=...
SLACK_USER_TOKEN=...
```

See [MCP Setup Guide](./docs/mcp-setup-guide.md) for detailed instructions.

## Best Practices

- **Brand Consistency** - Use brand guidelines enforcement hooks
- **Content Quality** - All outputs go through content reviewer
- **Data-Driven** - Track metrics via GA4 integration
- **Documentation** - Keep playbooks and learnings current
- **Testing** - Use /plan variants for scenario testing

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/name`)
3. Follow code standards in [CLAUDE.md](./CLAUDE.md)
4. Submit pull request

## Related Projects

- [ClaudeKit Website](https://github.com/claudekit/claudekit)
- [ClaudeKit Engineer](https://github.com/claudekit/claudekit-engineer)
- [ClaudeKit CLI](https://github.com/mrgoonie/claudekit-cli)
- [ClaudeKit Docs](https://docs.claudekit.cc)

## Support

- **Documentation:** See `./docs` folder
- **Issues:** GitHub Issues
- **Community:** [ClaudeKit Discord](https://claudekit.cc/discord)

## License

MIT License - see [LICENSE](LICENSE) file
