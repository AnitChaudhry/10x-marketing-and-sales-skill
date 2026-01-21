# Agent Catalog

This document provides a comprehensive reference for all AI agents available in ClaudeKit Marketing.

## Marketing Agent Hierarchy

```
Marketing Orchestrator (main Claude Code)
├── Attraction Agents (TOFU)
│   ├── attraction-specialist
│   ├── seo-specialist
│   └── lead-qualifier
├── Conversion Agents (MOFU)
│   ├── sale-enabler
│   ├── funnel-architect
│   └── email-wizard
├── Retention Agents (BOFU)
│   ├── continuity-specialist
│   └── upsell-maximizer
└── Supporting Agents
    ├── campaign-manager
    ├── content-creator
    ├── social-media-manager
    ├── community-manager
    ├── analytics-analyst
    └── content-reviewer
```

---

## Core Marketing Agents (Hormozi Framework)

### Attraction Specialist

**File:** `.claude/agents/attraction-specialist.md`
**Model:** Sonnet

Lead generation, top-of-funnel content, and competitor intelligence. Specializes in:
- Keyword research & gap analysis
- Competitor content intelligence
- Landing page content generation
- Programmatic SEO templates
- Lead magnet ideation

**Usage:**
```
Use the attraction-specialist agent to create TOFU content strategy.
```

---

### Email Wizard

**File:** `.claude/agents/email-wizard.md`
**Model:** Sonnet

Email campaign orchestration and optimization. Specializes in:
- Sequence template generation
- Dynamic content personalization
- Send-time optimization
- A/B test design & analysis
- Subject line generation
- Drip campaign architecture

**Usage:**
```
Use the email-wizard agent to design email nurture sequences.
```

---

### Lead Qualifier

**File:** `.claude/agents/lead-qualifier.md`
**Model:** Haiku (cost-optimized)

Intent detection, lead scoring, and behavioral analysis. Specializes in:
- Behavioral signal analysis
- Engagement pattern recognition
- Sales readiness prediction
- Next-best-action recommendations
- Lead scoring rules
- Qualification criteria definition

**Usage:**
```
Use the lead-qualifier agent to create lead scoring models.
```

---

### Continuity Specialist

**File:** `.claude/agents/continuity-specialist.md`
**Model:** Sonnet

Customer retention and engagement. Specializes in:
- Churn risk detection patterns
- Re-engagement campaign design
- NPS automation workflows
- Testimonial request sequences
- Customer health scoring
- Lifecycle stage analysis

**Usage:**
```
Use the continuity-specialist agent to analyze retention.
```

---

### Sale Enabler

**File:** `.claude/agents/sale-enabler.md`
**Model:** Sonnet

Sales collateral and deal acceleration. Specializes in:
- Personalized pitch generation
- Objection handling guides
- Social proof matching
- Deal acceleration workflows
- Proposal templates
- Case study generation

**Usage:**
```
Use the sale-enabler agent to create sales collateral.
```

---

### Funnel Architect

**File:** `.claude/agents/funnel-architect.md`
**Model:** Opus (complex reasoning)

Funnel design and conversion optimization. Specializes in:
- Funnel stage design
- Conversion rate analysis
- Bottleneck identification
- A/B test recommendations
- Offer sequencing (Hormozi model)
- Attribution modeling

**Usage:**
```
Use the funnel-architect agent to design high-converting funnels.
```

---

### Upsell Maximizer

**File:** `.claude/agents/upsell-maximizer.md`
**Model:** Sonnet

Revenue expansion and product recommendations. Specializes in:
- Upsell opportunity identification
- Product recommendation logic
- Expansion revenue forecasting
- Feature adoption tracking
- Cross-sell sequence design
- Pricing tier optimization

**Usage:**
```
Use the upsell-maximizer agent to increase average order value.
```

---

## Supporting Marketing Agents

### Campaign Manager

**File:** `.claude/agents/campaign-manager.md`
**Model:** Sonnet

Campaign orchestration across channels. Specializes in:
- Multi-channel campaign planning
- Performance tracking
- Budget allocation suggestions
- Timeline management
- Team coordination
- Campaign briefs

**Usage:**
```
Use the campaign-manager agent to plan multi-channel campaigns.
```

---

### Content Creator

**File:** `.claude/agents/content-creator.md`
**Model:** Sonnet

Generate marketing content across formats. Specializes in:
- Blog posts
- Social media posts
- Video scripts
- Ad copy
- Landing page copy
- Newsletter content

**Usage:**
```
Use the content-creator agent to write marketing content.
```

---

### Social Media Manager

**File:** `.claude/agents/social-media-manager.md`
**Model:** Sonnet

Social scheduling and analytics. Specializes in:
- Multi-platform post generation
- Content calendar management
- Engagement analysis
- Trend research
- Cross-posting optimization
- Platform-specific adaptation

**Usage:**
```
Use the social-media-manager agent to manage social presence.
```

---

### Community Manager

**File:** `.claude/agents/community-manager.md`
**Model:** Sonnet

Discord/Slack moderation and engagement. Specializes in:
- Sentiment analysis
- Response drafting
- Moderation alerts
- Engagement metrics
- Community insights
- FAQ generation

**Usage:**
```
Use the community-manager agent to manage Discord community.
```

---

### Analytics Analyst

**File:** `.claude/agents/analytics-analyst.md`
**Model:** Haiku (data processing)

Performance reporting and insights. Specializes in:
- Campaign performance reports
- Traffic analysis
- Conversion tracking
- Custom event analysis
- Dashboard data preparation
- Trend identification

**Usage:**
```
Use the analytics-analyst agent to generate performance reports.
```

---

### SEO Specialist

**File:** `.claude/agents/seo-specialist.md`
**Model:** Haiku

SEO audit and optimization. Specializes in:
- Technical SEO audit
- Content optimization
- Keyword analysis
- Link building strategy
- JSON+LD generation
- Competitor SEO analysis

**Usage:**
```
Use the seo-specialist agent to audit website SEO.
```

---

### Content Reviewer

**File:** `.claude/agents/content-reviewer.md`
**Model:** Sonnet

Reviews marketing content for quality and brand alignment. Specializes in:
- Content quality assessment
- Brand voice validation
- SEO analysis
- Conversion optimization
- Compliance checking

**Usage:**
```
Use the content-reviewer agent to validate content quality.
```

---

### Campaign Debugger

**File:** `.claude/agents/campaign-debugger.md`
**Model:** Sonnet

Analyzes campaign performance issues. Specializes in:
- Campaign performance analysis
- Conversion bottleneck identification
- A/B test analysis
- Funnel diagnostics
- Optimization recommendations

**Usage:**
```
Use the campaign-debugger agent to investigate issues.
```

---

## General Support Agents

### Copywriter

**File:** `.claude/agents/copywriter.md`
**Model:** Sonnet

Creates compelling marketing copy that converts. Specializes in:
- Landing page copy
- Email campaigns
- Ad copy
- Product descriptions
- Brand voice consistency

---

### Brainstormer

**File:** `.claude/agents/brainstormer.md`

Generates creative marketing ideas and campaign concepts.

**Usage:**
```bash
/brainstorm "email campaign ideas for product launch"
```

---

### Researcher

**File:** `.claude/agents/researcher.md`

Investigates market trends, competitors, and audience insights.

---

### Planner

**File:** `.claude/agents/planner.md`

Creates comprehensive marketing plans and strategies.

**Usage:**
```bash
/plan "Q1 content marketing strategy"
```

---

### Project Manager

**File:** `.claude/agents/project-manager.md`

Tracks marketing project progress and manages deliverables.

---

### Docs Manager

**File:** `.claude/agents/docs-manager.md`

Maintains marketing documentation and brand guidelines.

---

### Git Manager

**File:** `.claude/agents/git-manager.md`

Manages version control for marketing assets.

**Usage:**
```bash
/git:cm  # Commit changes
/git:cp  # Commit and push
/git:pr  # Create pull request
```

---

### Journal Writer

**File:** `.claude/agents/journal-writer.md`

Documents marketing learnings and campaign insights.

**Usage:**
```bash
/journal  # Write journal entry
```

---

### Scout / Scout External

**Files:** `.claude/agents/scout.md`, `.claude/agents/scout-external.md`

Quickly locates relevant files and content across the project.

**Usage:**
```bash
/scout "find all email templates"
/scout:ext "analyze competitor landing pages"
```

---

### MCP Manager

**File:** `.claude/agents/mcp-manager.md`

Manages Model Context Protocol server integrations.

**Usage:**
```bash
/use-mcp "GA4 analytics query"
```

---

### UI/UX Designer

**File:** `.claude/agents/ui-ux-designer.md`

Creates and reviews visual designs for marketing materials.

**Usage:**
```bash
/design/good "product landing page"
```

---

## Agent Communication

Agents communicate through file-based reports stored in designated directories:

| Agent Type | Output Directory |
|------------|------------------|
| attraction-specialist | `reports/attraction/` |
| lead-qualifier | `reports/leads/` |
| continuity-specialist | `reports/retention/` |
| funnel-architect | `reports/funnels/` |
| upsell-maximizer | `reports/upsell/` |
| community-manager | `reports/community/` |
| analytics-analyst | `reports/analytics/` |
| seo-specialist | `reports/seo/` |
| email-wizard | `campaigns/email/` |
| campaign-manager | `campaigns/` |
| sale-enabler | `content/sales/` |
| content-creator | `content/` |
| social-media-manager | `content/social/` |

Report naming convention:
```
{agent-name}-{date}-{topic-slug}.md
```

Example: `funnel-architect-251209-webinar-funnel.md`

---

## Agent Orchestration

The main Claude Code agent orchestrates sub-agents based on task requirements:

1. **Sequential Chaining**: Tasks with dependencies
2. **Parallel Execution**: Independent tasks
3. **Feedback Loops**: Iterative improvement

Example orchestration flow for a product launch:

```
User Request: "Create a product launch campaign"
    │
    ├── Brainstormer: Generate campaign concepts
    │
    ├── Researcher: Analyze market and competitors
    │       │
    │       └── [Reports back to orchestrator]
    │
    ├── Attraction Specialist: Keyword research & TOFU content
    │
    ├── Funnel Architect: Design conversion funnel
    │       │
    │       └── Email Wizard: Create nurture sequences
    │
    ├── Campaign Manager: Coordinate channels
    │       │
    │       ├── Content Creator: Write campaign content
    │       └── Social Media Manager: Plan social content
    │
    ├── Content Reviewer: Validate quality
    │       │
    │       └── [If issues] → Iterate
    │
    └── Project Manager: Track progress
```

---

## Adding Custom Agents

To create a custom marketing agent:

1. Create a new file in `.claude/agents/`
2. Use the standard frontmatter format:
   ```yaml
   ---
   name: agent-name
   description: When to use this agent
   model: sonnet  # or haiku, opus
   ---
   ```
3. Define the agent's role, responsibilities, and output format
4. Document in this catalog

---

## Agent Best Practices

1. **Be Specific**: Provide clear context when invoking agents
2. **Check Reports**: Review agent reports for insights
3. **Iterate**: Use feedback loops for quality improvement
4. **Document**: Keep agent learnings documented
5. **Combine**: Use multiple agents for complex tasks
6. **Model Selection**: Use Haiku for cost-sensitive tasks, Opus for complex reasoning
