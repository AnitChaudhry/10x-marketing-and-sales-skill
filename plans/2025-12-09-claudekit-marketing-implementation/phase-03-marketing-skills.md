# Phase 3: Marketing Skills

## Context Links

- [Plan Overview](./plan.md)
- [Phase 2: Core Marketing Agents](./phase-02-core-marketing-agents.md)
- [Research: Marketing Features](./research/researcher-02-marketing-features.md)
- [Existing Skills](../../.claude/skills/)

---

## Overview

| Field | Value |
|-------|-------|
| **Timeline** | Dec 21-24, 2025 |
| **Priority** | High |
| **Implementation Status** | ✅ Complete (2025-12-09) |
| **Review Status** | ✅ Complete (2025-12-09) |
| **Description** | Create 9 new marketing-specific skills |

---

## Important
Use the existing `/skill:create <prompt>` slash command to create new skills.

---

## Key Insights

1. Skills provide specialized capabilities and domain knowledge
2. Skills complement agents - agents use skills for specific tasks
3. Each skill needs `SKILL.md` (mandatory) + `references/` (optional) + `scripts/` (optional)
4. Skills should be vendor-agnostic where possible
5. Integration with ai-multimodal for image/video capabilities
6. pSEO (programmatic SEO) is high-priority differentiator

---

## Requirements

### Functional

- 9 new marketing skills
- Each skill self-contained with references
- Scripts for automation where applicable
- MCP integration documentation
- Agent-skill mapping

### Non-Functional

- Token-efficient skill prompts
- Clear activation triggers
- Reusable across agents
- Version tracking

---

## Architecture

### Skill Catalog

```
.claude/skills/
├── [KEEP] ai-multimodal/
├── [KEEP] chrome-devtools/
├── [KEEP] media-processing/
├── [KEEP] ui-styling/
├── [KEEP] ui-ux-pro-max/
├── [KEEP] frontend-design/
├── [KEEP] frontend-design-pro/
├── [KEEP] research/
├── [KEEP] planning/
├── [KEEP] problem-solving/
├── [KEEP] sequential-thinking/
├── [KEEP] mcp-management/
├── [KEEP] repomix/
├── [KEEP] skill-creator/
├── [KEEP] docs-seeker/
├── [KEEP] payment-integration/
├── [NEW] seo-optimization/
├── [NEW] content-marketing/
├── [NEW] social-media/
├── [NEW] email-marketing/
├── [NEW] analytics/
├── [NEW] campaign-management/
├── [NEW] brand-guidelines/
├── [NEW] video-production/
└── [NEW] ads-management/
```

---

## Skill Specifications

### 1. seo-optimization

**Purpose:** Keyword research, on-page SEO, programmatic SEO

| Attribute | Value |
|-----------|-------|
| Activation | SEO audit, keyword research, content optimization |
| Agents | seo-specialist, attraction-specialist, content-creator |
| MCP | Search Console |

**Capabilities:**
- Technical SEO audit workflows
- Keyword research methodology
- On-page optimization checklists
- JSON+LD schema generation
- Meta description templates
- Internal linking strategies
- pSEO template generation
- Content gap analysis

**References:**
- `references/technical-seo-checklist.md`
- `references/keyword-research-workflow.md`
- `references/pseo-templates.md`
- `references/schema-generation.md`

**Scripts:**
- `scripts/generate-sitemap.cjs`
- `scripts/analyze-keywords.cjs`
- `scripts/generate-schema.cjs`

---

### 2. content-marketing

**Purpose:** Content strategy, editorial calendar, content workflows

| Attribute | Value |
|-----------|-------|
| Activation | Content strategy, blog planning, editorial calendar |
| Agents | content-creator, campaign-manager |
| MCP | None |

**Capabilities:**
- Content strategy frameworks
- Editorial calendar templates
- Content pillar mapping
- Topic cluster design
- Content repurposing workflows
- Blog post structures
- Content audit methodology

**References:**
- `references/content-strategy-framework.md`
- `references/editorial-calendar-template.md`
- `references/blog-post-templates.md`
- `references/content-audit-checklist.md`

---

### 3. social-media

**Purpose:** Platform-specific posting, engagement, scheduling

| Attribute | Value |
|-----------|-------|
| Activation | Social posts, platform optimization, cross-posting |
| Agents | social-media-manager, content-creator |
| MCP | Discord, Slack, (Twitter future) |

**Capabilities:**
- Platform-specific content formats
- Optimal posting times
- Hashtag strategies
- Thread creation (X/Twitter)
- Carousel/slide design specs
- Engagement templates
- Cross-posting adaptation
- Viral content patterns

**References:**
- `references/platform-specs.md`
- `references/posting-best-practices.md`
- `references/thread-templates.md`
- `references/engagement-templates.md`

---

### 4. email-marketing

**Purpose:** Campaign design, A/B testing, automation sequences

| Attribute | Value |
|-----------|-------|
| Activation | Email campaigns, drip sequences, newsletters |
| Agents | email-wizard, campaign-manager |
| MCP | SendGrid, Resend |

**Capabilities:**
- Email campaign frameworks
- Subject line formulas
- Drip sequence templates
- A/B test design
- Segmentation strategies
- Personalization patterns
- Deliverability best practices
- Email compliance (CAN-SPAM, GDPR)

**References:**
- `references/email-campaign-types.md`
- `references/subject-line-formulas.md`
- `references/drip-sequence-templates.md`
- `references/compliance-checklist.md`

**Scripts:**
- `scripts/validate-email-list.cjs`

---

### 5. analytics

**Purpose:** GA4, Search Console, performance tracking

| Attribute | Value |
|-----------|-------|
| Activation | Analytics reports, performance analysis, KPIs |
| Agents | analytics-analyst, campaign-manager, funnel-architect |
| MCP | GA4, Search Console |

**Capabilities:**
- GA4 query patterns
- Custom event tracking
- Conversion tracking setup
- Dashboard design
- KPI definitions
- Attribution models
- Report templates
- Trend analysis methods

**References:**
- `references/ga4-query-patterns.md`
- `references/kpi-definitions.md`
- `references/report-templates.md`
- `references/attribution-models.md`

---

### 6. campaign-management

**Purpose:** Campaign planning, execution, measurement

| Attribute | Value |
|-----------|-------|
| Activation | Campaign planning, launch coordination, tracking |
| Agents | campaign-manager, funnel-architect |
| MCP | GA4, SendGrid, Slack |

**Capabilities:**
- Campaign brief templates
- Launch checklist workflows
- Multi-channel coordination
- Budget allocation frameworks
- Timeline management
- Post-campaign analysis
- ROI calculation methods

**References:**
- `references/campaign-brief-template.md`
- `references/launch-checklist.md`
- `references/roi-calculation.md`
- `references/post-mortem-template.md`

---

### 7. brand-guidelines

**Purpose:** Brand assets, style guides, consistency

| Attribute | Value |
|-----------|-------|
| Activation | Brand setup, style guide, asset management |
| Agents | content-creator, social-media-manager |
| MCP | Canva (future) |

**Capabilities:**
- Brand guideline templates
- Color palette management
- Typography specifications
- Voice and tone guides
- Logo usage rules
- Asset organization
- Brand audit checklists

**References:**
- `references/brand-guideline-template.md`
- `references/voice-tone-guide.md`
- `references/asset-organization.md`

**Hook Integration:**
- `brand-guidelines-reminder.cjs` injects brand context

---

### 8. video-production

**Purpose:** Script generation, storyboards, Veo 3.1 integration

| Attribute | Value |
|-----------|-------|
| Activation | Video scripts, storyboards, video creation |
| Agents | content-creator |
| MCP | YouTube (future) |

**Capabilities:**
- Video script templates
- Storyboard generation
- Veo 3.1 prompt engineering
- Platform-specific specs (Reels, TikTok, YouTube)
- Thumbnail design specs
- Video SEO optimization
- Caption/subtitle generation

**References:**
- `references/video-script-templates.md`
- `references/storyboard-format.md`
- `references/veo-prompt-guide.md`
- `references/platform-video-specs.md`

**Integration:**
- Uses `ai-multimodal` skill for Veo 3.1 access
- Uses `media-processing` for video editing

---

### 9. ads-management

**Purpose:** Meta Ads, Google Ads creation and optimization

| Attribute | Value |
|-----------|-------|
| Activation | Ad creation, campaign setup, ad optimization |
| Agents | campaign-manager, attraction-specialist |
| MCP | Meta Ads, Google Ads |

**Capabilities:**
- Ad copy frameworks (AIDA, PAS, etc.)
- Platform-specific ad specs
- Audience targeting strategies
- Budget optimization
- A/B testing frameworks
- Performance benchmarks
- Creative best practices

**References:**
- `references/ad-copy-frameworks.md`
- `references/platform-ad-specs.md`
- `references/targeting-strategies.md`
- `references/performance-benchmarks.md`

---

## Related Code Files

### Files to CREATE

```
.claude/skills/seo-optimization/SKILL.md
.claude/skills/seo-optimization/references/technical-seo-checklist.md
.claude/skills/seo-optimization/references/keyword-research-workflow.md
.claude/skills/seo-optimization/references/pseo-templates.md
.claude/skills/seo-optimization/references/schema-generation.md
.claude/skills/seo-optimization/scripts/generate-sitemap.cjs
.claude/skills/seo-optimization/scripts/analyze-keywords.cjs
.claude/skills/seo-optimization/scripts/generate-schema.cjs

.claude/skills/content-marketing/SKILL.md
.claude/skills/content-marketing/references/content-strategy-framework.md
.claude/skills/content-marketing/references/editorial-calendar-template.md
.claude/skills/content-marketing/references/blog-post-templates.md
.claude/skills/content-marketing/references/content-audit-checklist.md

.claude/skills/social-media/SKILL.md
.claude/skills/social-media/references/platform-specs.md
.claude/skills/social-media/references/posting-best-practices.md
.claude/skills/social-media/references/thread-templates.md
.claude/skills/social-media/references/engagement-templates.md

.claude/skills/email-marketing/SKILL.md
.claude/skills/email-marketing/references/email-campaign-types.md
.claude/skills/email-marketing/references/subject-line-formulas.md
.claude/skills/email-marketing/references/drip-sequence-templates.md
.claude/skills/email-marketing/references/compliance-checklist.md
.claude/skills/email-marketing/scripts/validate-email-list.cjs

.claude/skills/analytics/SKILL.md
.claude/skills/analytics/references/ga4-query-patterns.md
.claude/skills/analytics/references/kpi-definitions.md
.claude/skills/analytics/references/report-templates.md
.claude/skills/analytics/references/attribution-models.md

.claude/skills/campaign-management/SKILL.md
.claude/skills/campaign-management/references/campaign-brief-template.md
.claude/skills/campaign-management/references/launch-checklist.md
.claude/skills/campaign-management/references/roi-calculation.md
.claude/skills/campaign-management/references/post-mortem-template.md

.claude/skills/brand-guidelines/SKILL.md
.claude/skills/brand-guidelines/references/brand-guideline-template.md
.claude/skills/brand-guidelines/references/voice-tone-guide.md
.claude/skills/brand-guidelines/references/asset-organization.md

.claude/skills/video-production/SKILL.md
.claude/skills/video-production/references/video-script-templates.md
.claude/skills/video-production/references/storyboard-format.md
.claude/skills/video-production/references/veo-prompt-guide.md
.claude/skills/video-production/references/platform-video-specs.md

.claude/skills/ads-management/SKILL.md
.claude/skills/ads-management/references/ad-copy-frameworks.md
.claude/skills/ads-management/references/platform-ad-specs.md
.claude/skills/ads-management/references/targeting-strategies.md
.claude/skills/ads-management/references/performance-benchmarks.md
```

### Files to MODIFY

```
docs/skill-catalog.md (update with new skills)
```

---

## Implementation Steps

### Step 1: Create Skill Directory Structure
For each of 9 skills:
1. Create skill directory
2. Create `SKILL.md` file
3. Create references/ subdirectory
4. Create scripts/ subdirectory (if applicable)

### Step 2: Create Skill Main Files
Each SKILL.md follows format:
```markdown
---
name: skill-name
description: Activation description for skill
license: MIT
---

# Skill Name

Purpose and overview.

## When to Use
- Trigger condition 1
- Trigger condition 2

## Core Capabilities
Load: `references/capability-file.md`

## Workflow
1. Step 1
2. Step 2

## Output Requirements
- Expected output format
```

### Step 3: Create Reference Files
1. Research best practices per domain
2. Create actionable templates
3. Include examples
4. Add checklists where applicable

### Step 4: Create Scripts (where applicable)
1. Node.js scripts for automation
2. Integration with existing tools
3. Error handling
4. Documentation

### Step 5: Test Each Skill
1. Activate skill via Skill tool
2. Verify reference loading
3. Test script execution
4. Validate outputs

### Step 6: Document Agent-Skill Mapping
1. Which agents use which skills
2. Skill activation patterns
3. Skill chaining examples

---

## Todo List

- [x] Create seo-optimization skill + references
- [x] Create content-marketing skill + references
- [x] Create social-media skill + references
- [x] Create email-marketing skill + references + scripts
- [x] Create analytics skill + references
- [x] Create campaign-management skill + references
- [x] Create brand-guidelines skill + references
- [x] Create video-production skill + references
- [x] Create ads-management skill + references
- [x] Test all skills
- [x] Update skill-catalog.md
- [x] Document agent-skill mappings

---

## Success Criteria

1. All 9 skills created with SKILL.md
2. All reference files populated
3. Scripts functional (where applicable)
4. Skills activate correctly
5. Agent-skill integration documented
6. Skill catalog updated

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Reference bloat | Medium | Low | Keep references focused, split if >500 lines |
| Skill overlap | Medium | Low | Clear capability boundaries |
| Script failures | Low | Medium | Error handling, fallback to manual |
| Outdated references | High | Medium | Version tracking, update schedule |

---

## Security Considerations

- No API keys in skill files
- Scripts use env vars for credentials
- Reference files are documentation only
- No executable code in references

---

## Next Steps

After Phase 3 completion:
1. Proceed to Phase 4: Marketing Commands
2. Create commands that leverage skills
3. Build skill-command integration
4. Document usage examples

---

## Unresolved Questions

1. How to handle skill versioning?
2. Should skills have automated tests?
3. Reference file update frequency?
4. Skill dependency management?
5. Should skills load external URLs for latest practices?
