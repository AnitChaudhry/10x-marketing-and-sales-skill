# Phase 2: Core Marketing Agents

## Context Links

- [Plan Overview](./plan.md)
- [Phase 1: Foundation Cleanup](./phase-01-foundation-cleanup.md)
- [Research: Marketing Features](./research/researcher-02-marketing-features.md)
- [Subagents Framework](../../docs/overall/Attachments/Applying-Claude-Code-Subagents-to-Modern-Sales-and-Marketing-Frameworks.md)

---

## Overview

| Field | Value |
|-------|-------|
| **Timeline** | Dec 16-20, 2025 |
| **Priority** | Critical |
| **Implementation Status** | Complete |
| **Review Status** | Complete - Dec 9, 2025 |
| **Description** | Create 7 specialized marketing agents + 6 supporting agents |

---

## Key Insights

1. Subagents are for context control, NOT role personification
2. Each agent needs isolated context window + custom system prompt
3. Minimal permissions: grant only required tools
4. File-based communication prevents context pollution
5. Marketing agents should gather information, not just simulate roles
6. Hormozi framework (Attraction, Upsell, Downsell, Continuity) maps to agent design

---

## Requirements

### Functional

- 7 core marketing agents per source docs
- 6 additional supporting agents
- Each agent with specific tool permissions
- File-based report outputs
- MCP integration points defined

### Non-Functional

- Model selection per agent (Opus/Sonnet/Haiku)
- Token efficiency (Haiku for research)
- Response time optimization
- Error handling patterns

---

## Architecture

### Agent Hierarchy

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
    └── content-reviewer (modified from code-reviewer)
```

### Agent Specifications

#### 1. attraction-specialist

**Purpose:** Lead generation, top-of-funnel content, competitor intelligence

| Attribute | Value |
|-----------|-------|
| Model | Sonnet |
| Tools | Read, Glob, Grep, WebSearch, WebFetch |
| MCP Access | Google Ads, Search Console |
| Output | `reports/attraction-*.md` |

**Capabilities:**
- Keyword research & gap analysis
- Competitor content intelligence
- Landing page content generation
- Programmatic SEO templates
- Lead magnet ideation

---

#### 2. email-wizard

**Purpose:** Email campaign orchestration and optimization

| Attribute | Value |
|-----------|-------|
| Model | Sonnet |
| Tools | Read, Write, Edit, Glob, Grep |
| MCP Access | SendGrid, Resend |
| Output | `campaigns/email/*.md` |

**Capabilities:**
- Sequence template generation
- Dynamic content personalization
- Send-time optimization suggestions
- A/B test design & analysis
- Subject line generation
- Drip campaign architecture

---

#### 3. lead-qualifier

**Purpose:** Intent detection, lead scoring, behavioral analysis

| Attribute | Value |
|-----------|-------|
| Model | Haiku (cost-optimized) |
| Tools | Read, Glob, Grep |
| MCP Access | GA4 (read-only) |
| Output | `reports/leads/*.md` |

**Capabilities:**
- Behavioral signal analysis
- Engagement pattern recognition
- Sales readiness prediction
- Next-best-action recommendations
- Lead scoring rules
- Qualification criteria definition

---

#### 4. continuity-specialist

**Purpose:** Customer retention and engagement

| Attribute | Value |
|-----------|-------|
| Model | Sonnet |
| Tools | Read, Write, Glob, Grep, WebSearch |
| MCP Access | GA4, SendGrid |
| Output | `reports/retention/*.md` |

**Capabilities:**
- Churn risk detection patterns
- Re-engagement campaign design
- NPS automation workflows
- Testimonial request sequences
- Customer health scoring
- Lifecycle stage analysis

---

#### 5. sale-enabler

**Purpose:** Sales collateral and deal acceleration

| Attribute | Value |
|-----------|-------|
| Model | Sonnet |
| Tools | Read, Write, Edit, Glob, Grep |
| MCP Access | None (file-based) |
| Output | `content/sales/*.md` |

**Capabilities:**
- Personalized pitch generation
- Objection handling guides
- Social proof matching
- Deal acceleration workflows
- Proposal templates
- Case study generation

---

#### 6. funnel-architect

**Purpose:** Funnel design and conversion optimization

| Attribute | Value |
|-----------|-------|
| Model | Opus (complex reasoning) |
| Tools | Read, Write, Glob, Grep, WebSearch |
| MCP Access | GA4 |
| Output | `reports/funnels/*.md` |

**Capabilities:**
- Funnel stage design
- Conversion rate analysis
- Bottleneck identification
- A/B test recommendations
- Offer sequencing (Hormozi model)
- Attribution modeling

---

#### 7. upsell-maximizer

**Purpose:** Revenue expansion and product recommendations

| Attribute | Value |
|-----------|-------|
| Model | Sonnet |
| Tools | Read, Glob, Grep |
| MCP Access | GA4, Stripe (future) |
| Output | `reports/upsell/*.md` |

**Capabilities:**
- Upsell opportunity identification
- Product recommendation logic
- Expansion revenue forecasting
- Feature adoption tracking
- Cross-sell sequence design
- Pricing tier optimization

---

### Supporting Agents

#### 8. campaign-manager

**Purpose:** Campaign orchestration across channels

| Attribute | Value |
|-----------|-------|
| Model | Sonnet |
| Tools | Read, Write, Edit, Bash |
| MCP Access | GA4, SendGrid, Slack |
| Output | `campaigns/*.md` |

**Capabilities:**
- Multi-channel campaign planning
- Performance tracking
- Budget allocation suggestions
- Timeline management
- Team coordination
- Campaign briefs

---

#### 9. content-creator

**Purpose:** Generate marketing content

| Attribute | Value |
|-----------|-------|
| Model | Sonnet |
| Tools | Read, Write, Edit, Glob |
| MCP Access | None |
| Output | `content/*.md` |

**Capabilities:**
- Blog posts
- Social media posts
- Video scripts
- Ad copy
- Landing page copy
- Newsletter content

---

#### 10. social-media-manager

**Purpose:** Social scheduling and analytics

| Attribute | Value |
|-----------|-------|
| Model | Sonnet |
| Tools | Read, Write, Glob, WebSearch |
| MCP Access | Discord, Slack, (Twitter future) |
| Output | `content/social/*.md` |

**Capabilities:**
- Multi-platform post generation
- Content calendar management
- Engagement analysis
- Trend research
- Cross-posting optimization
- Platform-specific adaptation

---

#### 11. community-manager

**Purpose:** Discord/Slack moderation and engagement

| Attribute | Value |
|-----------|-------|
| Model | Sonnet |
| Tools | Read, Write, Glob, Grep |
| MCP Access | Discord, Slack |
| Output | `reports/community/*.md` |

**Capabilities:**
- Sentiment analysis
- Response drafting
- Moderation alerts
- Engagement metrics
- Community insights
- FAQ generation

---

#### 12. analytics-analyst

**Purpose:** Performance reporting and insights

| Attribute | Value |
|-----------|-------|
| Model | Haiku (data processing) |
| Tools | Read, Write, Glob, Grep |
| MCP Access | GA4, Search Console |
| Output | `reports/analytics/*.md` |

**Capabilities:**
- Campaign performance reports
- Traffic analysis
- Conversion tracking
- Custom event analysis
- Dashboard data preparation
- Trend identification

---

#### 13. seo-specialist

**Purpose:** SEO audit and optimization

| Attribute | Value |
|-----------|-------|
| Model | Haiku |
| Tools | Read, Write, Glob, Grep, WebFetch |
| MCP Access | Search Console |
| Output | `reports/seo/*.md` |

**Capabilities:**
- Technical SEO audit
- Content optimization
- Keyword analysis
- Link building strategy
- JSON+LD generation
- Competitor SEO analysis

---

## Related Code Files

### Files to CREATE

```
.claude/agents/attraction-specialist.md
.claude/agents/email-wizard.md
.claude/agents/lead-qualifier.md
.claude/agents/continuity-specialist.md
.claude/agents/sale-enabler.md
.claude/agents/funnel-architect.md
.claude/agents/upsell-maximizer.md
.claude/agents/campaign-manager.md
.claude/agents/content-creator.md
.claude/agents/social-media-manager.md
.claude/agents/community-manager.md
.claude/agents/analytics-analyst.md
.claude/agents/seo-specialist.md
```

### Files to MODIFY

```
.claude/agents/content-reviewer.md (already renamed in Phase 1)
.claude/agents/campaign-debugger.md (already renamed in Phase 1)
docs/agent-catalog.md (update with new agents)
```

### Directories to CREATE

```
campaigns/
campaigns/email/
content/sales/
reports/attraction/
reports/leads/
reports/retention/
reports/funnels/
reports/upsell/
reports/community/
reports/analytics/
reports/seo/
```

---

## Implementation Steps

### Step 1: Create Directory Structure
1. Create `campaigns/` and subdirectories
2. Create `content/sales/`
3. Create all `reports/` subdirectories

### Step 2: Create Core Agents (1-7)
For each agent:
1. Create markdown file with system prompt
2. Define allowed tools
3. Specify model (Opus/Sonnet/Haiku)
4. Document MCP dependencies
5. Add description for skill catalog

### Step 3: Create Supporting Agents (8-13)
Same process as core agents

### Step 4: Agent Template Structure
Each agent file follows:
```markdown
---
name: agent-name
model: claude-sonnet-4-20250514
description: Brief purpose description
allowedTools: [Read, Write, Edit, Glob, Grep]
---

# Agent Name

## Role
[Detailed role description]

## Capabilities
[List of specific capabilities]

## Output Format
[Expected output structure]

## Constraints
[Limitations and boundaries]

## MCP Integration
[Required MCP servers and usage]
```

### Step 5: Test Each Agent
1. Create test prompts per agent
2. Verify tool permissions work
3. Test MCP integration (where available)
4. Validate output format

### Step 6: Document Agent Interactions
1. Define orchestration patterns
2. Document file-based communication
3. Create agent collaboration examples

---

## Todo List

- [x] Create directory structure
- [x] Create attraction-specialist.md
- [x] Create email-wizard.md
- [x] Create lead-qualifier.md
- [x] Create continuity-specialist.md
- [x] Create sale-enabler.md
- [x] Create funnel-architect.md
- [x] Create upsell-maximizer.md
- [x] Create campaign-manager.md
- [x] Create content-creator.md
- [x] Create social-media-manager.md
- [x] Create community-manager.md
- [x] Create analytics-analyst.md
- [x] Create seo-specialist.md
- [x] Test each agent individually (structure validated)
- [x] Document agent interactions (in agent-catalog.md)
- [x] Update agent-catalog.md

**Completed - Dec 9, 2025:**
- [x] Directory structure created (campaigns/, content/sales/, reports/*)
- [x] References in docs/ are historical records, not broken references
- [x] All 13 agents created and validated
- [x] Documentation updated (brand-guidelines.md, design-guidelines.md created)

---

## Success Criteria

1. All 13 agents created and functional
2. Each agent has proper tool permissions
3. MCP integration points documented
4. Output directories created
5. Agent catalog documentation complete
6. Basic agent tests pass
7. Orchestration patterns documented

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Model cost overruns | Medium | Medium | Use Haiku for research-heavy agents |
| Context pollution | Medium | High | Enforce file-based communication |
| MCP auth issues | High | Medium | Build agents to work without MCP first |
| Overlapping responsibilities | Medium | Low | Clear capability boundaries per agent |

---

## Security Considerations

- Agents should not have direct database access
- MCP tokens managed centrally in .claude/.env
- Read-only permissions for analytics agents
- No PII in agent outputs
- Audit trail for agent actions

---

## Next Steps

After Phase 2 completion:
1. Proceed to Phase 3: Marketing Skills
2. Create skills that complement agents
3. Build agent-skill integration patterns
4. Document workflow examples

---

## Unresolved Questions

1. Should agents share a common base template?
2. How to handle agent versioning?
3. Rate limiting strategy for parallel agent execution?
4. Should agents have memory/context persistence?
5. Testing framework for agent quality assurance?
