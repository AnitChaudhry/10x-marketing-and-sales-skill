# Phase 4: Marketing Commands

## Context Links

- [Plan Overview](./plan.md)
- [Phase 2: Core Marketing Agents](./phase-02-core-marketing-agents.md)
- [Phase 3: Marketing Skills](./phase-03-marketing-skills.md)
- [Existing Commands](../../.claude/commands/)

---

## Overview

| Field | Value |
|-------|-------|
| **Timeline** | Dec 21-24, 2025 |
| **Priority** | High |
| **Implementation Status** | ✅ Complete (2025-12-10) |
| **Review Status** | ✅ Complete (2025-12-10) |
| **Description** | Create marketing commands + modify existing for marketing context |

---

## Key Insights

1. Commands are user-facing entry points to agent workflows
2. Commands can chain multiple agents and skills
3. Existing /content/* commands partially suitable
4. New commands needed for campaign, SEO, social, email, analytics
5. Commands should support arguments for flexibility
6. Approval workflows critical for marketing content

---

## Requirements

### Functional

- 12+ new marketing commands
- Modify existing /content/* for marketing
- Support command arguments
- Multi-agent orchestration
- Approval workflow integration

### Non-Functional

- Clear command naming
- Consistent argument patterns
- Help text for each command
- Error handling

---

## Architecture

### Command Organization

```
.claude/commands/
├── [KEEP] plan.md
├── [KEEP] plan/
├── [KEEP] brainstorm.md
├── [KEEP] scout.md
├── [KEEP] scout/
├── [KEEP] journal.md
├── [KEEP] watzup.md
├── [KEEP] ask.md
├── [MODIFY] content/ (enhance for marketing)
├── [KEEP] design/
├── [KEEP] docs/
├── [KEEP] git/
├── [NEW] campaign.md
├── [NEW] campaign/
├── [NEW] seo.md
├── [NEW] seo/
├── [NEW] social.md
├── [NEW] social/
├── [NEW] email.md
├── [NEW] email/
├── [NEW] analyze.md
├── [NEW] analyze/
├── [NEW] persona.md
├── [NEW] competitor.md
└── [NEW] funnel.md
```

---

## Command Specifications

### New Commands

#### 1. /campaign [action] [name]

**Purpose:** Create and manage marketing campaigns

| Attribute | Value |
|-----------|-------|
| Agents | campaign-manager, funnel-architect |
| Skills | campaign-management |
| Arguments | action: create/status/analyze, name: campaign name |

**Actions:**
- `/campaign create "Q1 Product Launch"` - Create new campaign
- `/campaign status "Q1 Product Launch"` - Get campaign status
- `/campaign analyze "Q1 Product Launch"` - Analyze campaign performance

**Workflow:**
1. Gather campaign requirements
2. Generate campaign brief
3. Create tracking setup
4. Output to `campaigns/` directory

---

#### 2. /campaign/email [action]

**Purpose:** Email campaign management

| Attribute | Value |
|-----------|-------|
| Agents | email-wizard, campaign-manager |
| Skills | email-marketing |
| MCP | SendGrid, Resend |

**Actions:**
- `/campaign/email create` - Create email campaign
- `/campaign/email sequence` - Design drip sequence
- `/campaign/email test` - A/B test design

---

#### 3. /seo [action]

**Purpose:** SEO audit and optimization

| Attribute | Value |
|-----------|-------|
| Agents | seo-specialist, attraction-specialist |
| Skills | seo-optimization |
| MCP | Search Console |

**Actions:**
- `/seo audit [url]` - Technical SEO audit
- `/seo keywords [topic]` - Keyword research
- `/seo optimize [content]` - Content optimization
- `/seo schema [page]` - Generate JSON+LD

**Workflow:**
1. Analyze target (URL/topic/content)
2. Generate audit report
3. Provide actionable recommendations
4. Output to `reports/seo/`

---

#### 4. /seo/pseo [template]

**Purpose:** Programmatic SEO template generation

| Attribute | Value |
|-----------|-------|
| Agents | seo-specialist, content-creator |
| Skills | seo-optimization, content-marketing |

**Workflow:**
1. Define data source structure
2. Create page template
3. Generate sample pages
4. SEO optimization per template

---

#### 5. /social [platform] [type]

**Purpose:** Social media content generation

| Attribute | Value |
|-----------|-------|
| Agents | social-media-manager, content-creator |
| Skills | social-media |
| MCP | Discord, Slack |

**Platforms:** twitter, linkedin, instagram, tiktok, youtube

**Types:** post, thread, carousel, story, reel

**Examples:**
- `/social twitter thread` - Create Twitter thread
- `/social linkedin post` - Create LinkedIn post
- `/social instagram carousel` - Create carousel slides

---

#### 6. /social/schedule

**Purpose:** Schedule social media posts

| Attribute | Value |
|-----------|-------|
| Agents | social-media-manager |
| Skills | social-media |

**Workflow:**
1. Gather posts to schedule
2. Suggest optimal times
3. Create calendar entry
4. Output schedule to `content/social/schedule.md`

---

#### 7. /email [type]

**Purpose:** Generate email content

| Attribute | Value |
|-----------|-------|
| Agents | email-wizard, copywriter |
| Skills | email-marketing |

**Types:** newsletter, cold, followup, launch, nurture

**Examples:**
- `/email newsletter` - Create newsletter
- `/email cold [prospect-type]` - Cold email
- `/email launch [product]` - Product launch email

---

#### 8. /analyze [type]

**Purpose:** Analytics and performance reports

| Attribute | Value |
|-----------|-------|
| Agents | analytics-analyst, funnel-architect |
| Skills | analytics |
| MCP | GA4, Search Console |

**Types:** traffic, campaigns, conversions, funnel, content

**Examples:**
- `/analyze traffic` - Traffic analysis report
- `/analyze campaigns` - Campaign performance
- `/analyze funnel` - Funnel conversion analysis

---

#### 9. /analyze/report [period]

**Purpose:** Generate periodic reports

| Attribute | Value |
|-----------|-------|
| Agents | analytics-analyst |
| Skills | analytics, campaign-management |
| MCP | GA4 |

**Periods:** daily, weekly, monthly, quarterly

---

#### 10. /persona [action]

**Purpose:** Customer persona management

| Attribute | Value |
|-----------|-------|
| Agents | lead-qualifier, researcher |
| Skills | content-marketing |

**Actions:**
- `/persona create` - Create new persona
- `/persona analyze` - Analyze audience data
- `/persona update` - Update existing persona

**Output:** `content/personas/`

---

#### 11. /competitor [action]

**Purpose:** Competitive analysis

| Attribute | Value |
|-----------|-------|
| Agents | researcher, attraction-specialist |
| Skills | research, seo-optimization |

**Actions:**
- `/competitor analyze [url]` - Analyze competitor
- `/competitor content [url]` - Content gap analysis
- `/competitor seo [url]` - SEO comparison

---

#### 12. /funnel [action]

**Purpose:** Funnel design and optimization

| Attribute | Value |
|-----------|-------|
| Agents | funnel-architect, sale-enabler |
| Skills | campaign-management, analytics |

**Actions:**
- `/funnel design [type]` - Design new funnel
- `/funnel analyze` - Analyze existing funnel
- `/funnel optimize` - Optimization recommendations

**Types:** lead-magnet, webinar, product-launch, evergreen

---

### Modified Commands

#### /content/blog [topic]

**Enhance for marketing:**
- Add SEO optimization step
- Include keyword targeting
- Meta description generation
- Internal linking suggestions
- Output structured for CMS

---

#### /content/video [type]

**Enhance with video-production skill:**
- Script templates per platform
- Storyboard generation
- Veo 3.1 prompt generation
- Thumbnail suggestions
- Caption generation

**Types:** youtube, reel, tiktok, explainer, tutorial

---

#### /content/cro [page]

**Conversion rate optimization:**
- Analyze current page
- Identify friction points
- Generate copy variants
- A/B test recommendations

---

### Commands to KEEP (unchanged)

```
/plan - Strategy and planning
/plan/* - All plan variants
/brainstorm - Ideation sessions
/scout - Codebase/project scouting
/scout/* - Scout variants
/journal - Journey documentation
/watzup - Status updates
/ask - Q&A
/design/* - All design commands
/docs/* - Documentation commands
/git/* - Git operations
```

---

## Related Code Files

### Files to CREATE

```
.claude/commands/campaign.md
.claude/commands/campaign/email.md
.claude/commands/campaign/status.md
.claude/commands/campaign/analyze.md
.claude/commands/seo.md
.claude/commands/seo/audit.md
.claude/commands/seo/keywords.md
.claude/commands/seo/pseo.md
.claude/commands/social.md
.claude/commands/social/schedule.md
.claude/commands/email.md
.claude/commands/email/sequence.md
.claude/commands/analyze.md
.claude/commands/analyze/report.md
.claude/commands/persona.md
.claude/commands/competitor.md
.claude/commands/funnel.md
```

### Files to MODIFY

```
.claude/commands/content/blog.md (add SEO integration)
.claude/commands/content/video.md (add video-production skill)
.claude/commands/content/cro.md (enhance optimization)
docs/command-catalog.md (update with new commands)
```

---

## Implementation Steps

### Step 1: Create Command Directories
1. Create `campaign/` subdirectory
2. Create `seo/` subdirectory
3. Create `social/` subdirectory
4. Create `email/` subdirectory (if not exists)
5. Create `analyze/` subdirectory

### Step 2: Create Main Command Files
Each command.md follows format:
```markdown
# Command: /command-name

Brief description.

## Arguments
- `arg1`: Description
- `arg2`: Description

## Workflow
1. Step 1
2. Step 2

## Agents Used
- agent-1: Purpose
- agent-2: Purpose

## Skills Used
- skill-1
- skill-2

## Output
Description of outputs

## Examples
\`\`\`
/command-name arg1 arg2
\`\`\`
```

### Step 3: Create Subcommand Files
Same format as main commands, with parent reference

### Step 4: Modify Existing Commands
1. Update /content/blog.md with SEO
2. Update /content/video.md with video-production
3. Update /content/cro.md

### Step 5: Test Commands
1. Test each command individually
2. Test argument parsing
3. Verify agent invocation
4. Check output locations

### Step 6: Document Command Usage
1. Update command-catalog.md
2. Create usage examples
3. Document common workflows

---

## Todo List

- [x] Create campaign command + subcommands
- [x] Create seo command + subcommands
- [x] Create social command + subcommands
- [x] Create email command + subcommands
- [x] Create analyze command + subcommands
- [x] Create persona command
- [x] Create competitor command
- [x] Create funnel command
- [x] Modify content/blog.md
- [x] Modify content/video.md
- [x] Modify content/cro.md
- [x] Test all commands
- [x] Update command-catalog.md

---

## Success Criteria

1. All new commands functional
2. Arguments parsed correctly
3. Agents invoked properly
4. Skills loaded as expected
5. Outputs in correct directories
6. Modified commands enhanced
7. Command catalog updated

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Command naming conflicts | Low | Medium | Check existing commands first |
| Agent orchestration issues | Medium | High | Test multi-agent flows thoroughly |
| MCP dependency failures | Medium | Medium | Commands work without MCP |
| Argument parsing errors | Low | Low | Clear argument documentation |

---

## Security Considerations

- Commands should not expose credentials
- User confirmation for publish actions
- Rate limiting awareness for MCP calls
- PII handling in analysis commands

---

## Next Steps

After Phase 4 completion:
1. Proceed to Phase 5: MCP Integrations
2. Connect commands to MCP servers
3. Test end-to-end workflows
4. Document integration patterns

---

## Unresolved Questions

1. Should commands have --dry-run option?
2. Interactive vs non-interactive command modes?
3. Command aliasing support?
4. Command chaining syntax?
5. Should commands support piping output?
