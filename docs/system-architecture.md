# ClaudeKit Marketing - System Architecture

**Last Updated:** 2025-12-28
**Phase:** 6 - Workflow Orchestration & Hook System (Complete) | Dashboard Phase 5 - Brand Center (Complete)
**Status:** 27 agents (32 files), 73+ commands (118 files), 28+ skills (2,664 files), 6 workflow systems (10 files), 7 hooks active, 8 MCP servers operational, Marketing Dashboard production-ready (32 components, 5 Pinia stores, 6 views, 18+ API endpoints), 142 tests (88% pass rate), security hardened, human-in-the-loop controls enabled

---

## Architecture Overview

ClaudeKit Marketing uses a distributed agent orchestration architecture where a main Claude Code agent coordinates specialized sub-agents for different marketing functions. This design enables parallel execution of independent tasks and sequential chaining for dependent workflows.

```
┌─────────────────────────────────────────────────────────────┐
│                   Main Orchestrator                         │
│              (Claude Code Agent Runtime)                    │
│                                                             │
│  Responsibilities:                                          │
│  • User request parsing and routing                         │
│  • Agent delegation and coordination                        │
│  • Task result aggregation                                  │
│  • Report generation and storage                            │
└─────────────────────────┬───────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   ┌──────────┐      ┌──────────┐      ┌──────────┐
   │Copywriter│      │Brainstorm│      │Researcher│
   │          │      │          │      │          │
   │• Copy    │      │• Ideas   │      │• Market  │
   │• Voice   │      │• Strategy│      │• Compete │
   │• Optimize│      │• Concepts│      │• Trends  │
   └──────────┘      └──────────┘      └──────────┘
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   ┌────────────┐   ┌──────────────┐  ┌───────────┐
   │Content     │   │Campaign      │  │Project    │
   │Reviewer    │   │Debugger      │  │Manager    │
   │            │   │              │  │           │
   │• Quality   │   │• Performance │  │• Progress │
   │• Brand     │   │• Diagnostics │  │• Roadmap  │
   │• SEO       │   │• Optimization│  │• Reports  │
   └────────────┘   └──────────────┘  └───────────┘
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   ┌────────────┐   ┌───────────┐   ┌───────────┐
   │Docs Manager│   │Git Manager│   │Journal    │
   │            │   │           │   │Writer     │
   │• Docs      │   │• Commits  │   │• Learnings│
   │• Guidelines│   │• PRs      │   │• Insights │
   │• Playbooks │   │• Branches │   │• Stories  │
   └────────────┘   └───────────┘   └───────────┘
```

---

## Core Components

### 1. Orchestration Layer

**Main Claude Code Agent**
- Role: Central coordinator for all marketing tasks
- Responsibilities:
  - Parse user commands and natural language requests
  - Route requests to appropriate sub-agents
  - Manage parallel and sequential task execution
  - Aggregate results and generate reports
  - Store reports in `plans/reports/` with standardized naming

**Communication Pattern:**
```
User Request → Main Agent → Sub-agents → Reports → Aggregation → Output
```

---

### 2. Marketing Agent Tier

#### Core Marketing Agents (Hormozi Framework)

**TOFU (Top of Funnel) Agents**

**Attraction Specialist Agent** (Phase 2)
- Purpose: Lead generation and TOFU content creation
- Model: Claude 3.5 Sonnet
- Input: Target keywords, audience pain points, competitor analysis
- Output: Content strategy, landing pages, lead magnets
- Expertise:
  - Keyword research & gap analysis
  - Competitor content intelligence
  - Landing page generation
  - Programmatic SEO templates
  - Lead magnet ideation

**SEO Specialist Agent** (Phase 2)
- Purpose: SEO optimization and keyword strategy
- Model: Claude 3.5 Sonnet
- Input: Content, keywords, competitor URLs
- Output: SEO recommendations, optimized content
- Expertise:
  - Keyword research
  - On-page optimization
  - Technical SEO
  - Link strategy
  - Content optimization

**Lead Qualifier Agent** (Phase 2)
- Purpose: Lead scoring and qualification
- Model: Claude 3.5 Haiku (cost-optimized)
- Input: Lead signals, engagement data, behavior patterns
- Output: Lead scores, qualification rules, recommendations
- Expertise:
  - Behavioral signal analysis
  - Engagement pattern recognition
  - Sales readiness prediction
  - Next-best-action recommendations
  - Lead scoring models

**MOFU (Middle of Funnel) Agents**

**Email Wizard Agent** (Phase 2)
- Purpose: Email campaign orchestration
- Model: Claude 3.5 Sonnet
- Input: Campaign goals, audience segments, templates
- Output: Email sequences, subject lines, send schedules
- Expertise:
  - Sequence template generation
  - Dynamic content personalization
  - Send-time optimization
  - A/B test design & analysis
  - Drip campaign architecture

**Sale Enabler Agent** (Phase 2)
- Purpose: Sales collateral and deal acceleration
- Model: Claude 3.5 Sonnet
- Input: Product info, customer objections, pricing
- Output: Sales proposals, pitch decks, objection responses
- Expertise:
  - Personalized pitch generation
  - Objection handling guides
  - Social proof matching
  - Deal acceleration workflows
  - Proposal templates

**Funnel Architect Agent** (Phase 2)
- Purpose: Funnel design and conversion optimization
- Model: Claude 3.5 Opus (complex reasoning)
- Input: Current funnel data, bottleneck analysis
- Output: Funnel redesigns, optimization roadmaps
- Expertise:
  - Funnel stage design
  - Conversion rate analysis
  - Bottleneck identification
  - A/B test recommendations
  - Attribution modeling

**BOFU (Bottom of Funnel) Agents**

**Upsell Maximizer Agent** (Phase 2)
- Purpose: Cross-sell and upsell strategy
- Model: Claude 3.5 Sonnet
- Input: Customer segments, product portfolio
- Output: Upsell strategies, offer recommendations
- Expertise:
  - Upsell opportunity identification
  - Offer sequencing (Hormozi model)
  - Cross-sell analytics
  - Customer lifetime value optimization
  - Retention strategy

**Continuity Specialist Agent** (Phase 2)
- Purpose: Customer retention and engagement
- Model: Claude 3.5 Sonnet
- Input: Customer lifecycle data, retention metrics
- Output: Retention campaigns, engagement plans
- Expertise:
  - Churn risk detection patterns
  - Re-engagement campaign design
  - NPS automation workflows
  - Customer health scoring
  - Lifecycle stage analysis

**Core Content & Optimization Agents**

**Copywriter Agent**
- Purpose: Create compelling marketing copy
- Model: Claude 3.5 Sonnet
- Input: Content briefs, target audience, brand voice guidelines
- Output: Copy drafts, subject lines, CTAs
- Expertise:
  - Landing page copy
  - Email marketing
  - Ad copy
  - Product descriptions
  - Brand voice consistency

**Brainstormer Agent**
- Purpose: Generate creative marketing ideas
- Model: Claude 3.5 Sonnet
- Input: Campaign objectives, target market, constraints
- Output: Concept ideas, angles, strategy recommendations
- Expertise:
  - Campaign concepts
  - Content ideas
  - Marketing angles
  - Strategy development
  - Innovation ideation

**Researcher Agent**
- Purpose: Market and competitive intelligence
- Model: Claude 3.5 Sonnet
- Input: Market segments, competitors, trends
- Output: Analysis reports, insights, recommendations
- Expertise:
  - Competitor analysis
  - Market research
  - Audience insights
  - Industry trends
  - Data-driven recommendations

**Content Reviewer Agent**
- Purpose: Quality assurance for marketing content
- Model: Claude 3.5 Sonnet
- Input: Marketing content (copy, email, landing pages)
- Output: Review reports, improvement suggestions
- Expertise:
  - Brand voice validation
  - SEO analysis
  - Conversion optimization
  - Compliance checking
  - Quality assessment

**Campaign Debugger Agent**
- Purpose: Campaign performance diagnostics
- Model: Claude 3.5 Sonnet
- Input: Campaign metrics, performance data, issues
- Output: Diagnostic reports, optimization recommendations
- Expertise:
  - Performance analysis
  - Bottleneck identification
  - A/B test analysis
  - Funnel diagnostics
  - Optimization strategy

**Content Creator Agent** (Phase 2)
- Purpose: Multi-format content creation
- Model: Claude 3.5 Sonnet
- Input: Content briefs, formats, channels
- Output: Blog posts, social content, videos, docs
- Expertise:
  - Blog content creation
  - Social media content
  - Video scripts
  - Whitepaper generation
  - Resource content

**Campaign Manager Agent** (Phase 2)
- Purpose: Campaign orchestration and management
- Model: Claude 3.5 Sonnet
- Input: Campaign plans, budget, channels
- Output: Campaign timelines, coordination, reporting
- Expertise:
  - Campaign planning
  - Cross-channel coordination
  - Budget management
  - Performance tracking
  - Campaign optimization

**Social Media Manager Agent** (Phase 2)
- Purpose: Social media strategy and content
- Model: Claude 3.5 Sonnet
- Input: Brand voice, platforms, audience
- Output: Social strategies, content calendars
- Expertise:
  - Platform strategy
  - Content calendar creation
  - Engagement optimization
  - Community management
  - Analytics and reporting

**Community Manager Agent** (Phase 2)
- Purpose: Community engagement and management
- Model: Claude 3.5 Sonnet
- Input: Community data, engagement metrics
- Output: Engagement strategies, member programs
- Expertise:
  - Community strategy
  - Member programs
  - Event planning
  - Engagement optimization
  - Growth strategies

#### Support Marketing Agents

**Planner Agent**
- Purpose: Strategic planning and roadmap creation
- Responsibilities: Campaign planning, content strategy, implementation roadmaps

**Project Manager Agent**
- Purpose: Progress tracking and task management
- Responsibilities: Status reports, milestone tracking, resource allocation

**Docs Manager Agent**
- Purpose: Documentation and guideline management
- Responsibilities: Update docs, maintain brand guidelines, manage content repos

**Git Manager Agent**
- Purpose: Version control workflows
- Responsibilities: Clean commits, branch management, PR creation

**Journal Writer Agent**
- Purpose: Learning and insight documentation
- Responsibilities: Campaign post-mortems, success stories, learnings

**Scout Agent**
- Purpose: Internal content discovery
- Responsibilities: File finding, pattern matching, codebase navigation

**Scout External Agent**
- Purpose: External resource exploration
- Responsibilities: Competitor analysis, external codebase exploration

**UI/UX Designer Agent**
- Purpose: Visual design and interfaces
- Responsibilities: Landing page design, visual hierarchy, design system adherence

**MCP Manager Agent**
- Purpose: External tool integration
- Responsibilities: Tool discovery, server management, capability analysis

---

### 3. Skills Layer

Skills extend agent capabilities through specialized knowledge modules. Each skill can be used by multiple agents.

**AI & Content Generation Skills**
- `ai-multimodal` - Gemini image/video generation and analysis
- `media-processing` - FFmpeg/ImageMagick video and image editing
- `chrome-devtools` - Browser automation and performance analysis
- `document-skills` - PDF and document processing

**Design & UI Skills**
- `ui-styling` - Tailwind CSS and shadcn/ui implementation
- `ui-ux-pro-max` - Advanced design system with 50 styles
- `frontend-design` - Design patterns and best practices
- `frontend-design-pro` - Production-ready interfaces

**Strategy & Analysis Skills**
- `planning` - Solution architecture and implementation
- `research` - Technical research and discovery
- `problem-solving` - Systematic problem-solving
- `sequential-thinking` - Logical reasoning and analysis

**Integration & Utility Skills**
- `mcp-management` - MCP server integration
- `payment-integration` - Payment gateway integration
- `repomix` - Codebase analysis and packaging
- `docs-seeker` - Documentation discovery
- `claude-code` - Claude Code feature reference
- `skill-creator` - Custom skill creation guide

---

### 4. Commands Layer

Commands provide user-facing interfaces to agent capabilities through slash commands.

**Content Commands**
- `/content/good` - Create high-quality content (Copywriter)
- `/content/cro` - Optimize for conversions (Content Reviewer)
- `/content/enhance` - Improve existing content (Copywriter)

**Planning Commands**
- `/plan` - Create strategic plans (Planner)
- `/brainstorm` - Generate ideas (Brainstormer)

**Analysis Commands**
- `/scout` - Find files and content (Scout)
- `/ask` - Ask questions (Research)
- `/analyze` - Analyze data (Researcher)

**Utility Commands**
- `/fix` - Solve problems (Campaign Debugger)
- `/journal` - Document learnings (Journal Writer)
- `/use-mcp` - Use external tools (MCP Manager)
- `/ck-help` - Display command help (Project Manager)
- `/watzup` - Quick status (Project Manager)

---

### 5. Hooks Layer (Phase 6)

Automation triggers that execute at key lifecycle events. Context injection and workflow enforcement hooks provide quality gates and brand compliance.

**Session Lifecycle Hooks**
- `session-init.cjs` - Initialize session, load project context
- `subagent-init.cjs` - Inject subagent-specific context on agent startup

**Content Quality Hooks** (Phase 6)
- `brand-guidelines-reminder.cjs` - Enforce brand guidelines for content agents
  - Targets: content-creator, copywriter, social-media-manager, email-wizard, sale-enabler
  - Injects brand voice, messaging, and visual guidelines into agent context
  - Ensures consistent brand representation across all content workflows

**Campaign Tracking Hooks** (Phase 6)
- `campaign-tracking.cjs` - Monitor campaign metrics and conversions
  - Targets: campaign-manager, campaign-debugger, social-media-manager, email-wizard, content-creator, analytics-analyst
  - Logs campaign execution events and performance metrics
  - Provides audit trail for compliance and optimization

**Approval Workflow Hooks** (Phase 6)
- `approval-workflow.cjs` - Request human approval for publish actions
  - Targets: All subagents (*) on completion
  - Creates approval requests in `plans/approvals/` before sensitive actions
  - Actions requiring approval: publish, send_email, launch_campaign, post_social, go_live, deploy, activate_ads
  - Enables human-in-the-loop controls for risk mitigation

**Development Standards Hooks**
- `dev-rules-reminder.cjs` - Enforce development best practices
- `scout-block.cjs` - Validate file access permissions

---

### 6. Workflows Layer (Phase 6)

Structured workflow definitions enable predictable agent interactions and coordinated multi-agent orchestration across marketing domains.

**Marketing Domain Workflows**
- `marketing-workflow.md` - Campaign planning, execution, and optimization workflows
  - Campaign lifecycle orchestration
  - Multi-channel coordination
  - Performance monitoring and adjustment

- `sales-workflow.md` - Sales enablement and deal acceleration workflows
  - Proposal generation and customization
  - Objection handling and response
  - Sales collateral management

- `campaign-workflow.md` - Campaign execution and management workflows
  - Campaign kickoff and planning
  - Cross-team coordination
  - Performance tracking and reporting

**Content Domain Workflows**
- `content-workflow.md` - Multi-format content creation workflows
  - Blog post creation and optimization
  - Social media content calendar
  - Whitepaper and guide generation
  - Brand voice consistency

- `seo-workflow.md` - SEO optimization and keyword strategy workflows
  - Keyword research and gap analysis
  - On-page and technical SEO optimization
  - Content optimization for search
  - Link strategy and authority building

- `analytics-workflow.md` - Performance analytics and reporting workflows
  - Campaign performance analysis
  - Funnel diagnostics and optimization
  - A/B test design and analysis
  - ROI and conversion tracking

**System Workflows**
- `primary-workflow.md` - Main orchestration and command routing
- `development-rules.md` - Development standards and best practices
- `orchestration-protocol.md` - Agent coordination and communication rules
- `documentation-management.md` - Documentation procedures and standards

---

### 7. Data & Storage Layer

**Report Storage**
- Location: `plans/reports/`
- Naming: `{agent-name}-{date}-{topic-slug}.md`
- Example: `copywriter-251209-landing-page-copy.md`

**Documentation Storage**
- Location: `docs/`
- Core docs: Overview, catalogs, architecture, guidelines
- Strategic docs: Roadmap, PDR, architecture

**Configuration Storage**
- Location: `.claude/` directory
- Agent definitions, skill modules, command definitions
- Workflow specifications, hook automation

---

## Data Flow Patterns

### Pattern 1: Parallel Content Generation

```
User Request: "Create email campaign"
    │
    ├─→ Brainstormer: Generate email concepts
    │       → Report: concept-ideas.md
    │
    ├─→ Researcher: Analyze competitor emails
    │       → Report: competitor-analysis.md
    │
    ├─→ Copywriter: Write email sequences
    │       → Report: email-draft.md
    │
    └─→ Content Reviewer: Validate quality
            → Report: review-feedback.md
```

### Pattern 2: Sequential Content Improvement

```
Initial Content
    │
    ├→ Content Reviewer: Analyze quality
    │   └→ Issues Found? YES
    │       │
    │       └→ Copywriter: Revise based on feedback
    │           │
    │           └→ Content Reviewer: Re-validate
    │               └→ Approved? YES → Final Content
```

### Pattern 3: Campaign Optimization

```
Campaign Launched
    │
    └→ Campaign Debugger: Analyze performance
        │
        ├→ Issues Identified?
        │   │
        │   └→ Recommends changes
        │       │
        │       └→ Copywriter/Content Reviewer: Implement
        │           │
        │           └→ A/B test results
```

---

## Agent Communication Protocol

### Report Format

All agents produce standardized markdown reports:

```markdown
# [Task Title]

**Date:** YYYY-MM-DD
**Agent:** [agent-name]
**Status:** [Complete/In-Progress/Failed]

## Summary
[Brief overview of findings]

## Findings
[Detailed findings and analysis]

## Recommendations
[Specific recommendations for next steps]

## Artifacts
[Links to generated files or content]
```

### Handoff Protocol

When agents need to coordinate:

1. Agent A completes task → generates report
2. Main orchestrator reviews report
3. Orchestrator shares relevant insights with Agent B
4. Agent B reads previous report and continues work
5. New report references previous work

---

## Integration Points

### External Services

**AI/ML:**
- Google Gemini API - Image/video generation and analysis
- Claude 3.5 Sonnet - LLM backbone for all agents

**Tools:**
- Puppeteer - Browser automation
- FFmpeg - Video processing
- ImageMagick - Image manipulation
- Git - Version control

**Future Integrations (Phase 5):**
- Google Analytics 4 - Performance analytics
- Google Ads - Advertising platform
- Meta Ads - Social advertising
- SendGrid - Email delivery
- Discord/Slack - Team communication

---

## Scalability & Performance

### Parallel Execution

Independent tasks execute in parallel:
- Multiple agents can run simultaneously
- Reduces total execution time
- Maximizes resource utilization

### Sequential Coordination

Dependent tasks execute in sequence:
- Downstream agents receive upstream results
- Ensures data consistency
- Maintains workflow integrity

### Resource Management

- Agents use configurable model selection (Opus for complex tasks, Sonnet for standard)
- Skills are shared across agents to reduce duplication
- Reports cached in `plans/reports/` for reference

---

## Security Architecture

### Credential Management
- All API keys stored in `.env` (not committed)
- Environment variables used for secrets
- `.gitignore` prevents credential leaks

### Data Privacy
- Reports stored locally in project
- No automatic upload to external services
- User controls all data distribution

### Access Control
- All agents run within Claude Code sandbox
- File system access through designated directories
- MCP integrations require explicit configuration

---

## Monitoring & Observability

### Report Generation
- Every agent execution generates a timestamped report
- Reports stored in `plans/reports/` for audit trail
- Standardized naming enables easy searching

### Status Tracking
- Project Manager tracks milestone progress
- Journal Writer documents campaign learnings
- Git commits create version history

### Error Handling
- Failed tasks trigger diagnostic reports
- Campaign Debugger analyzes performance issues
- Recommendations provided for remediation

---

## Deployment Architecture

### Local Execution
- Runs on developer's machine via Claude Code
- All dependencies installed via npm
- Environment configuration via `.env` file

### Git Integration
- Commits follow conventional commit format
- PRs created through Git Manager
- Clean history maintained through hooks

### Documentation Sync
- Docs Manager keeps documentation current
- Changes tracked in git history
- Easy rollback if needed

---

## Phase 1 Architecture Changes

**Status:** ✅ Complete

### Removed Components
- 3 engineer agents (fullstack-developer, tester, database-admin)
- 13 engineer skills (backend, testing, devops, etc.)
- 5 engineer commands (/cook, /code, /bootstrap, /test, /debug)
- Engineer-specific hooks

### Added Components
- Content Reviewer Agent - Marketing content quality assurance
- Campaign Debugger Agent - Campaign performance analytics
- Enhanced Copywriter Agent - Marketing-focused copy generation
- Enhanced Brainstormer Agent - Marketing concept development

### Updated Components
- All workflows refocused on marketing context
- Command help updated with marketing examples
- Documentation restructured for marketing focus

---

## Phase 2 Architecture Changes

**Status:** ✅ Complete (2025-12-09)

### New Agents Added (13 Total)

**TOFU Agents:**
- Attraction Specialist - Lead generation & TOFU content creation
- SEO Specialist - SEO optimization & keyword research
- Lead Qualifier - Lead scoring & behavioral analysis

**MOFU Agents:**
- Email Wizard - Email campaign orchestration
- Sale Enabler - Sales collateral & deal acceleration
- Funnel Architect - Funnel design & optimization
- Content Creator - Multi-format content creation

**BOFU Agents:**
- Upsell Maximizer - Cross-sell & upsell strategies
- Continuity Specialist - Customer retention & engagement

**Operations Agents:**
- Campaign Manager - Campaign orchestration
- Social Media Manager - Social media strategy
- Community Manager - Community engagement
- brainstormer (support) - Brainstorming support

### New Data Structures
- `campaigns/` directory - Campaign templates and archives
- `content/sales/` directory - Sales content templates
- `content/social/` directory - Social media content
- `reports/` directory - Campaign reports and analytics

### New Documentation
- Brand Guidelines - Voice, tone, messaging framework
- Design Guidelines - Visual design system, colors, typography
- Updated Agent Catalog - 27 agents with full documentation
- Updated System Architecture - Hormozi framework integration

### Architecture Improvements
- Hormozi funnel framework integrated (TOFU/MOFU/BOFU)
- Agent model selection optimized (Haiku, Sonnet, Opus)
- Content organization by channel
- Report generation standardized
- Funnel stage-based agent coordination

---

## Future Architecture (Phase 3+)

### Planned Skill Expansion
- SEO Optimization - Keyword research and content optimization
- Content Marketing - Blog, landing pages, strategy
- Social Media - Multi-platform content
- Email Marketing - Campaign automation
- Analytics - GA4 integration and reporting
- Video Production - Script and video management

### Planned Integration Expansion
- GA4 for analytics
- Google Ads and Meta Ads
- SendGrid for email
- Discord and Slack for collaboration

---

## Architecture Best Practices

### Agent Design
- Single responsibility per agent
- Clear input/output contracts
- Consistent report format
- Error resilience

### Skill Management
- Focused functionality per skill
- Reusable across agents
- Well-documented with examples
- Tested before deployment

### Workflow Patterns
- Sequential for dependent tasks
- Parallel for independent tasks
- Feedback loops for iteration
- Clear handoff protocols

### Documentation
- Always in sync with code
- Examples for all features
- Regular review and updates
- Version history maintained

---

## Marketing Dashboard API Layer (Phase 2 - NEW)

**Status:** ✅ Complete (2025-12-23)

The Marketing Dashboard API Layer provides a REST interface for campaign and content management with AI integration. Built on Hono framework + better-sqlite3, designed to support the Vue.js frontend.

### API Architecture

```
Frontend (Vue.js)
    │
    └─→ [CORS Middleware]
        │
        ├─→ [API Key Auth]
        │
        ├─→ Routes Layer
        │   ├─ /api/campaigns   (Campaign CRUD)
        │   ├─ /api/content     (Content CRUD)
        │   ├─ /api/assets      (Asset Management + Scanner)
        │   └─ /api/ai          (AI Enhancement)
        │
        └─→ Database Layer
            └─ SQLite (marketing.db)
                ├─ campaigns table
                ├─ content table
                ├─ assets table
                └─ automations table
```

### 4 Core API Routes

**1. Campaigns API (`/api/campaigns`)**
- CRUD operations for campaign management
- Validation: name (required), status (draft|active|completed)
- Data: goal, start_date, end_date, brand_context, notes
- Tests: 23 passing

**2. Content API (`/api/content`)**
- CRUD with type/status filtering
- Types: blog | social | email | landing | other
- Statuses: draft | review | published
- Queryable by: campaign_id, type, status
- Tests: 29 passing

**3. Assets API (`/api/assets`)**
- Asset management + Content Hub scanner integration
- Live scan of assets folder with DB merge
- File serving with 6-layer path traversal protection
- Asset rescanning and database synchronization
- Tests: 24 passing (security: 21 passing)

**4. AI API (`/api/ai`)**
- Claude Code CLI bridge for content enhancement
- Status check endpoint for availability
- POST /enhance - Improve existing content
- POST /generate - Create new content
- Brand context injection support
- Tests: 35 passing

### Security Implementation

**Authentication:** API Key (X-API-Key header)
- Required in production
- Bypassed in development (SKIP_AUTH=true)
- Returns 401 for missing/invalid keys

**Path Traversal Defense (6 Layers):**
1. URL decoding validation
2. Windows backslash normalization
3. Null byte filtering
4. Symbolic link rejection
5. Directory boundary enforcement
6. Whitelist path validation

**Additional Security:**
- CORS restricted to configured origins
- Command injection prevention (Claude CLI sanitization)
- Database: foreign keys enabled, prepared statements
- .gitignore excludes database file

### Test Coverage

**Total Tests:** 132 (90% passing)

| Module | Tests | Status |
|--------|-------|--------|
| Campaigns | 23 | ✅ Passing |
| Content | 29 | ✅ Passing |
| Assets | 24 | ✅ Passing |
| AI | 35 | ✅ Passing |
| Security | 21 | ✅ Passing |

### Database Schema

**campaigns table:**
- id (PK), name, status, goal, start_date, end_date
- brand_context (JSON), notes, created_at, updated_at

**content table:**
- id (PK), campaign_id (FK), type, status, title
- body, metadata (JSON), created_at, updated_at

**assets table:**
- id (PK), path, type, size, mime
- metadata (JSON), created_at, updated_at

**automations table:**
- id (PK), name, enabled, configuration (JSON)
- created_at, updated_at

### Environment Configuration

**Required:**
- PORT (default: 3457)
- NODE_ENV (development/production)
- API_KEY (required in production)

**Optional:**
- ALLOWED_ORIGINS (default: http://localhost:5173)
- SKIP_AUTH (development only)
- DATABASE_PATH (custom location)

### Technology Stack

- **Framework:** Hono 4.0+ (lightweight HTTP server)
- **Database:** SQLite 3 (better-sqlite3)
- **Testing:** Vitest + Supertest
- **Runtime:** Node.js (ES modules)

### Integration Points

**Frontend:**
- Vue.js dashboard consumes API endpoints
- CORS enabled for localhost:5173 (configurable)
- Credentials mode enabled for auth headers

**Content Hub Scanner:**
- Live asset scanning with `scanner.cjs`
- DB merge with scanned assets
- Manifest generation

**Claude Code CLI:**
- AI bridge (`ai-bridge.cjs`) integration
- Brand context injection (`brand-context.cjs`)
- Async content enhancement/generation

### Error Handling

Standardized error responses:
```json
{
  "error": "Error type",
  "message": "Human-readable description",
  "details": "Technical details (dev mode only)"
}
```

HTTP Status Codes:
- 200/201 - Success
- 400 - Validation failed
- 401 - Unauthorized
- 403 - Forbidden (security violation)
- 404 - Not found
- 500 - Server error

### Monitoring & Logging

**Health Endpoint:** `GET /health`
- Returns: status, timestamp, environment

**Log Levels:**
- INFO: Server startup, request routing
- WARN: Auth bypassed, missing config
- ERROR: Database errors, API failures

**Startup Output:**
```
🚀 Marketing Dashboard API
   Server: http://localhost:3457
   Health: http://localhost:3457/health
   Environment: development
   CORS: http://localhost:5173

   Endpoints:
   • /api/campaigns - Campaign CRUD
   • /api/content   - Content CRUD
   • /api/assets    - Assets + Scanner
   • /api/ai        - AI Enhancement
```

### Graceful Shutdown

Server implements signal handlers:
- SIGTERM - Graceful shutdown
- SIGINT - Graceful shutdown
- Closes database connections before exit

### Documentation References

Full API documentation: `docs/marketing-dashboard-api.md`
- Complete endpoint reference
- Request/response examples
- Error scenarios
- cURL examples

---

## Marketing Dashboard Vue Frontend (Phase 3 - NEW)

**Status:** ✅ Complete (2025-12-23)

The Marketing Dashboard Frontend provides a modern Vue 3 UI for managing campaigns, content, and assets with real-time API connectivity.

### Frontend Architecture

```
Browser (Vue 3)
    │
    └─→ [Pinia Store Layer]
        │
        ├─→ campaigns.js    (Campaign state & actions)
        ├─→ content.js      (Content management)
        ├─→ assets.js       (Asset browser)
        └─→ ai.js           (AI enhancement pipeline)
            │
            └─→ [HTTP Client]
                │
                ├─→ [Auth Interceptor - API Key]
                │
                └─→ REST API Layer (Phase 2)
                    ├─ /api/campaigns
                    ├─ /api/content
                    ├─ /api/assets
                    └─ /api/ai
```

### 16 Vue Components Created

**Layout Components (3):**
- `AppHeader.vue` - Top navigation bar with branding
- `AppSidebar.vue` - Collapsible sidebar navigation
- `AppLayout.vue` - Main layout wrapper with responsive grid

**Campaign Components (3):**
- `CampaignCard.vue` - Campaign card display with meta info
- `CampaignList.vue` - Paginated campaign listing
- `CampaignForm.vue` - Campaign creation/editing form

**Content Components (3):**
- `ContentCard.vue` - Content item preview
- `ContentGrid.vue` - Grid-based content browser
- `ContentEditor.vue` - Rich text content editor

**Asset Components (3):**
- `AssetCard.vue` - Asset preview with metadata
- `AssetGrid.vue` - Asset gallery with filters
- `AssetPreview.vue` - Full-screen asset viewer

**Common Components (4):**
- `Modal.vue` - Reusable modal dialog
- `Toast.vue` - Notification toasts
- `LoadingSpinner.vue` - Loading indicator
- Utility components & mixins

### 4 Pinia Store Modules

**campaigns.js**
- State: campaigns list, selected campaign, filters
- Actions: fetchCampaigns, createCampaign, updateCampaign, deleteCampaign
- Getters: filteredCampaigns, campaignById

**content.js**
- State: content library, filters, editor state
- Actions: fetchContent, createContent, updateContent, deleteContent
- Getters: contentByType, contentByCampaign, publishedContent

**assets.js**
- State: assets list, asset scanner status, metadata
- Actions: scanAssets, filterAssets, updateAssetMetadata
- Getters: assetsByType, assetsByTag

**ai.js**
- State: enhancement queue, generation status
- Actions: enhanceContent, generateContent, checkStatus
- Getters: queueStatus, completedTasks

### 5 Application Views

**DashboardView** (/)
- Analytics overview
- Key performance indicators
- Recent activity feed
- Quick actions

**CampaignsView** (/campaigns)
- Campaign list with filters
- Campaign creation wizard
- Status tracking
- Performance metrics

**ContentView** (/content)
- Content library browser
- Type-based filtering
- Content editor
- Publishing workflow

**AssetsView** (/assets)
- Asset gallery
- Asset scanner integration
- Metadata management
- Asset preview

**SettingsView** (/settings)
- Configuration options
- API key management
- Preferences
- Integration setup

### Vue Router Configuration

```javascript
// src/router/index.js
routes: [
  { path: '/', component: DashboardView },
  { path: '/campaigns', component: CampaignsView },
  { path: '/content', component: ContentView },
  { path: '/assets', component: AssetsView },
  { path: '/settings', component: SettingsView }
]
```

### Technology Stack (Phase 3)

| Technology | Version | Purpose |
|-----------|---------|---------|
| Vue | 3.5.24 | Frontend framework |
| Pinia | 3.0.4 | State management |
| Vue Router | 4.6.4 | Client-side routing |
| Tailwind CSS | 4.1.18 | Utility-first styling |
| Vite | 7.2.4 | Build tooling |
| @vueuse/core | 14.1.0 | Composition utilities |

### Build Optimization

**Development:**
```bash
npm run dev          # Start vite dev server with HMR
npm run preview      # Preview production build
```

**Production:**
```bash
npm run build        # Build for production
# Output: dist/
```

**Bundle Metrics:**
- Production bundle: 162.78 kB
- Gzipped size: 53.44 kB
- Build time: 657ms
- Tree-shakable modules
- Lazy-loaded routes

### API Integration Pattern

**In Pinia Store:**
```javascript
// Example: campaigns.js
async fetchCampaigns() {
  const response = await fetch(`${API_URL}/campaigns`, {
    headers: { 'X-API-Key': this.apiKey }
  })
  const data = await response.json()
  this.campaigns = data
}
```

**In Component:**
```javascript
// Example: CampaignList.vue
import { useCampaignStore } from '@/stores/campaigns'

const campaignStore = useCampaignStore()
await campaignStore.fetchCampaigns()
```

### Authentication Flow

1. API key configured in `.env`
2. Auth interceptor adds `X-API-Key` header
3. Backend validates token on all requests
4. 401 response triggers re-authentication
5. Secure credential storage (no localStorage secrets)

### State Management Patterns

**Normalized State:**
- Campaigns stored as array with ID keys
- Reduce duplicates and consistency issues
- Simple update/delete operations

**Action Patterns:**
- All API calls in actions
- Error handling with try-catch
- Loading states during requests

**Getter Patterns:**
- Computed filtering by type/status
- Count aggregations
- Sorted/paginated results

### Component Communication

**Parent to Child:** Props
```javascript
<CampaignCard :campaign="campaign" :active="isActive" />
```

**Child to Parent:** Emits
```javascript
emit('update:campaign', updatedData)
```

**Cross-Component:** Pinia Store
```javascript
const store = useStore()
store.updateData(newValue)
```

### Styling Architecture

**Tailwind CSS 4.1:**
- Utility-first approach
- PostCSS integration
- Custom theme configuration
- Dark mode support (optional)

**Component Scoping:**
- Scoped styles per component
- Tailwind utilities in templates
- No CSS-in-JS overhead

### Testing Strategy (Phase 4)

Planned test coverage:
- Unit tests for components
- Integration tests for stores
- E2E tests for workflows
- Performance benchmarks
- Accessibility testing

### Development Workflow

**Local Development:**
1. Install dependencies: `npm install`
2. Start dev server: `npm run dev`
3. Opens `http://localhost:5173`
4. HMR enabled for instant updates

**Component Development:**
- Create in `src/components/`
- Define props and emits
- Use Pinia stores for state
- Style with Tailwind

**Store Development:**
- Create in `src/stores/`
- Define state, actions, getters
- Test API integration
- Document patterns

### Environment Configuration

**Files:**
- `.env` - Local secrets (not committed)
- `.env.example` - Template for dev setup
- `src/config.js` - App configuration

**Variables:**
```javascript
// src/config.js
export const API_BASE_URL =
  import.meta.env.VITE_API_URL || 'http://localhost:3457'
```

### Security Measures

**Frontend Security:**
- CSP headers configuration
- No sensitive data in localStorage
- API key from environment only
- Input validation on forms
- XSS prevention via Vue auto-escape

**API Integration Security:**
- HTTPS in production
- API key in request headers
- CORS validation
- Token rotation support

### Performance Optimization

**Code Splitting:**
- Route-based code splitting
- Lazy-loaded components
- Dynamic imports for heavy modules

**Asset Optimization:**
- Image lazy-loading
- Webp format support
- Minified production build
- Gzip compression ready

**State Optimization:**
- Normalized store state
- Computed getters avoid recalculation
- Selective reactivity

### Integration Checklist (Phase 4)

- [ ] API endpoints tested end-to-end
- [ ] Authentication flow validated
- [ ] Error handling verified
- [ ] Loading states working
- [ ] Asset scanner integrated
- [ ] Content editor functional
- [ ] Campaign creation flow complete
- [ ] UI responsive on mobile/tablet
- [ ] Accessibility validated
- [ ] Performance optimized

### Documentation References

- Frontend code: `./.claude/skills/marketing-dashboard/app/src/`
- API documentation: `docs/marketing-dashboard-api.md`
- Component catalog: `./.claude/skills/marketing-dashboard/app/COMPONENTS.md` (Phase 4)
- State management: `./.claude/skills/marketing-dashboard/app/STORES.md` (Phase 4)

---

## Marketing Dashboard Brand Center (Phase 5 - NEW)

**Status:** ✅ Complete (2025-12-24)

### New Components (7)

**Brand Center View (1):**
- `BrandView.vue` - Brand Center dashboard with design system showcases

**Brand System Components (6):**
- `ColorPalette.vue` - Display brand color tokens with contrast checker
- `TypographyPreview.vue` - Font family and size scale showcase
- `SpacingScale.vue` - Spacing/layout scale visualization
- `ComponentShowcase.vue` - Component library preview gallery
- `LogoGallery.vue` - Brand logo management with upload capability
- `VoiceSummary.vue` - Brand voice and tone guidelines

### New Store Module (1)

**brand.js**
- State: design tokens, logos, voice guidelines
- Actions: fetchTokens, fetchLogos, fetchVoice, fetchAll, uploadLogo
- Getters: tokensByCategory, logosByType, voiceData

### New API Routes (1)

**Brand Center API** (`/api/brand`)
- `GET /api/brand/tokens` - Load design tokens (colors, fonts, spacing)
- `GET /api/brand/voice` - Load brand voice guidelines
- `GET /api/brand/logos` - List all brand logos with metadata
- `POST /api/brand/logos` - Upload new logo file with validation

### Security Features (New)
- File upload validation (MIME type, file size 5MB max)
- Filename sanitization (path traversal prevention)
- Design token read-only access
- Logo management with category organization

### Updated Views (1)

**AppSidebar.vue**
- Added Brand Center navigation link

### Stripped Features

**Removed from Dashboard (Phase 5 Refocus):**
- Campaign automation recipes
- Blog post generator
- Social media pack generator
- Campaign brief generator
- SEO audit automation

**Focus:** Reoriented dashboard to Brand Center management, design system showcase, and asset management

---

**Architect:** Frontend Engineering Team
**Last Review:** 2025-12-24 (Phase 5 Brand Center Completion)
**Next Review:** Phase 6 Integration & Deployment (Q1 2026)
