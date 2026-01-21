# Phase 6: Workflows & Hooks

## Context Links

- [Plan Overview](./plan.md)
- [Phase 2: Core Marketing Agents](./phase-02-core-marketing-agents.md)
- [Phase 5: MCP Integrations](./phase-05-mcp-integrations.md)
- [Existing Workflows](../../.claude/workflows/)

---

## Overview

| Field | Value |
|-------|-------|
| **Timeline** | Dec 25-28, 2025 |
| **Priority** | High |
| **Implementation Status** | Complete |
| **Review Status** | Approved |
| **Completion Date** | 2025-12-11 |
| **Description** | Create marketing workflows + hooks for automation |

---

## Key Insights

1. Workflows orchestrate multi-agent collaboration
2. Hooks inject context at key lifecycle points
3. Plan Mode enables approval workflows (critical for marketing)
4. Brand guidelines hook ensures consistency across content
5. Campaign tracking hook enables performance measurement
6. Existing hooks (session-init, subagent-init, dev-rules-reminder) to keep

---

## Requirements

### Functional

- Marketing workflow (research -> content -> publish)
- Sales workflow (lead -> qualify -> nurture -> close)
- Campaign workflow (plan -> create -> launch -> measure)
- Brand guidelines injection hook
- Campaign tracking hook
- Approval workflow integration

### Non-Functional

- Workflow execution logging
- Hook performance (minimal latency)
- Error recovery in workflows
- Human-in-loop checkpoints

---

## Architecture

### Workflow Structure

```
.claude/workflows/
├── [KEEP] primary-workflow.md
├── [KEEP] development-rules.md
├── [KEEP] orchestration-protocol.md
├── [KEEP] documentation-management.md
├── [NEW] marketing-workflow.md
├── [NEW] sales-workflow.md
├── [NEW] campaign-workflow.md
├── [NEW] content-workflow.md
├── [NEW] seo-workflow.md
└── [NEW] analytics-workflow.md
```

### Hook Structure

```
.claude/hooks/
├── [KEEP] session-init.cjs
├── [KEEP] subagent-init.cjs
├── [KEEP] dev-rules-reminder.cjs
├── [NEW] brand-guidelines-reminder.cjs
├── [NEW] campaign-tracking.cjs
└── [NEW] approval-workflow.cjs
```

---

## Workflow Specifications

### 1. Marketing Workflow

**File:** `marketing-workflow.md`

**Purpose:** End-to-end marketing process orchestration

**Stages:**
```
1. Research & Insights
   ├── Spawn researcher agent
   ├── Competitive analysis
   ├── Audience research
   └── Output: research reports

2. Strategy & Planning
   ├── Spawn planner agent
   ├── Campaign objectives
   ├── Channel selection
   └── Output: marketing plan

3. Content Creation
   ├── Spawn content-creator
   ├── Generate assets
   ├── Brand compliance check
   └── Output: content drafts

4. Review & Approval
   ├── Spawn content-reviewer
   ├── Human approval checkpoint
   ├── Revision loop
   └── Output: approved content

5. Distribution
   ├── Schedule posts
   ├── Email campaigns
   ├── Publish content
   └── Output: published content

6. Measurement
   ├── Spawn analytics-analyst
   ├── Track performance
   ├── Generate reports
   └── Output: analytics reports
```

---

### 2. Sales Workflow

**File:** `sales-workflow.md`

**Purpose:** Lead-to-customer journey automation

**Stages:**
```
1. Lead Generation
   ├── Spawn attraction-specialist
   ├── Content distribution
   ├── Lead capture
   └── Output: new leads

2. Lead Qualification
   ├── Spawn lead-qualifier
   ├── Score leads
   ├── Segment by intent
   └── Output: qualified leads

3. Nurture Sequence
   ├── Spawn email-wizard
   ├── Personalized content
   ├── Drip campaigns
   └── Output: engaged leads

4. Sales Enablement
   ├── Spawn sale-enabler
   ├── Prepare collateral
   ├── Objection handling
   └── Output: sales materials

5. Upsell/Cross-sell
   ├── Spawn upsell-maximizer
   ├── Product recommendations
   ├── Expansion campaigns
   └── Output: upsell offers
```

---

### 3. Campaign Workflow

**File:** `campaign-workflow.md`

**Purpose:** Single campaign lifecycle management

**Stages:**
```
1. Campaign Brief
   ├── Spawn campaign-manager
   ├── Define objectives
   ├── Set KPIs
   └── Output: campaign brief

2. Creative Development
   ├── Spawn content-creator
   ├── Ad copy/visuals
   ├── Landing pages
   └── Output: creative assets

3. Funnel Setup
   ├── Spawn funnel-architect
   ├── Design conversion path
   ├── Setup tracking
   └── Output: funnel config

4. Launch
   ├── Publish content
   ├── Activate ads
   ├── Start email sequence
   └── Output: live campaign

5. Optimization
   ├── Monitor performance
   ├── A/B test results
   ├── Adjust targeting
   └── Output: optimized campaign

6. Post-Mortem
   ├── Spawn analytics-analyst
   ├── Performance analysis
   ├── Learnings capture
   └── Output: campaign report
```

---

### 4. Content Workflow

**File:** `content-workflow.md`

**Purpose:** 5-stage content production pipeline

**Stages:**
```
1. Draft
   ├── Content brief
   ├── Initial creation
   └── SEO foundation

2. Review
   ├── Content-reviewer check
   ├── Brand compliance
   └── Fact checking

3. Edit
   ├── Revisions
   ├── Optimization
   └── Final polish

4. Approved
   ├── Human sign-off
   ├── Schedule publication
   └── Asset preparation

5. Published
   ├── Go live
   ├── Distribution
   └── Performance tracking
```

---

### 5. SEO Workflow

**File:** `seo-workflow.md`

**Purpose:** SEO optimization process

**Stages:**
```
1. Audit
   ├── Technical audit
   ├── Content audit
   └── Competitor analysis

2. Keyword Research
   ├── Topic clusters
   ├── Search intent
   └── Gap analysis

3. On-Page Optimization
   ├── Meta optimization
   ├── Content updates
   └── Schema markup

4. Content Creation
   ├── New content
   ├── pSEO templates
   └── Link building

5. Monitoring
   ├── Rank tracking
   ├── Traffic analysis
   └── Iteration
```

---

### 6. Analytics Workflow

**File:** `analytics-workflow.md`

**Purpose:** Performance measurement and reporting

**Stages:**
```
1. Data Collection
   ├── GA4 queries
   ├── Search Console data
   └── Platform metrics

2. Analysis
   ├── Trend identification
   ├── Attribution modeling
   └── Funnel analysis

3. Reporting
   ├── Dashboard updates
   ├── Scheduled reports
   └── Stakeholder summaries

4. Insights
   ├── Recommendations
   ├── Action items
   └── Next steps
```

---

## Hook Specifications

### 1. brand-guidelines-reminder.cjs

**Purpose:** Inject brand context into content workflows

**Trigger:** Before content-creator, copywriter agents

**Implementation:**
```javascript
// brand-guidelines-reminder.cjs
module.exports = async (context) => {
  const brandGuidelinesPath = './content/brand/guidelines.md';

  // Check if brand guidelines exist
  if (fs.existsSync(brandGuidelinesPath)) {
    const guidelines = fs.readFileSync(brandGuidelinesPath, 'utf8');

    // Inject into context
    context.systemPrompt += `\n\n## Brand Guidelines\n${guidelines}`;
  }

  return context;
};
```

**Configuration:**
```json
{
  "hook": "brand-guidelines-reminder",
  "trigger": "subagent-start",
  "agents": ["content-creator", "copywriter", "social-media-manager"]
}
```

---

### 2. campaign-tracking.cjs

**Purpose:** Log campaign actions for measurement

**Trigger:** After campaign-related actions

**Implementation:**
```javascript
// campaign-tracking.cjs
module.exports = async (context, action) => {
  const logPath = './campaigns/tracking.log';

  const entry = {
    timestamp: new Date().toISOString(),
    action: action.type,
    campaign: action.campaignId,
    agent: context.agent,
    details: action.details
  };

  fs.appendFileSync(logPath, JSON.stringify(entry) + '\n');

  return context;
};
```

**Tracked Actions:**
- Campaign created
- Content published
- Email sent
- Ad launched
- Report generated

---

### 3. approval-workflow.cjs

**Purpose:** Enforce human approval for publish actions

**Trigger:** Before publish/send actions

**Implementation:**
```javascript
// approval-workflow.cjs
module.exports = async (context, action) => {
  const requiresApproval = [
    'publish',
    'send_email',
    'launch_campaign',
    'post_social'
  ];

  if (requiresApproval.includes(action.type)) {
    // Create approval request
    const approvalPath = `./plans/approvals/${Date.now()}-${action.type}.md`;

    const request = `
# Approval Request

**Action:** ${action.type}
**Content:** ${action.content.substring(0, 500)}...
**Requested:** ${new Date().toISOString()}

## Approve?
- [ ] Approved
- [ ] Rejected
- [ ] Needs revision

## Notes:
`;

    fs.writeFileSync(approvalPath, request);

    // Block until approved
    context.pendingApproval = approvalPath;
  }

  return context;
};
```

---

## Related Code Files

### Files to CREATE

```
.claude/workflows/marketing-workflow.md
.claude/workflows/sales-workflow.md
.claude/workflows/campaign-workflow.md
.claude/workflows/content-workflow.md
.claude/workflows/seo-workflow.md
.claude/workflows/analytics-workflow.md
.claude/hooks/brand-guidelines-reminder.cjs
.claude/hooks/campaign-tracking.cjs
.claude/hooks/approval-workflow.cjs
plans/approvals/ (directory for approval requests)
campaigns/tracking.log (campaign action log)
```

### Files to MODIFY

```
.claude/settings.json (register new hooks)
.claude/workflows/primary-workflow.md (reference marketing workflows)
```

---

## Implementation Steps

### Step 1: Create Workflow Files
1. Create marketing-workflow.md
2. Create sales-workflow.md
3. Create campaign-workflow.md
4. Create content-workflow.md
5. Create seo-workflow.md
6. Create analytics-workflow.md

### Step 2: Create Hooks
1. Create brand-guidelines-reminder.cjs
2. Create campaign-tracking.cjs
3. Create approval-workflow.cjs
4. Test hook execution

### Step 3: Create Approval System
1. Create plans/approvals/ directory
2. Define approval request format
3. Document approval workflow

### Step 4: Register Hooks
1. Update .claude/settings.json
2. Configure hook triggers
3. Define agent associations

### Step 5: Test Workflows
1. Run each workflow end-to-end
2. Verify agent orchestration
3. Test approval checkpoints
4. Validate hook execution

### Step 6: Documentation
1. Document workflow usage
2. Create workflow examples
3. Troubleshooting guide

---

## Todo List

- [x] Create marketing-workflow.md
- [x] Create sales-workflow.md
- [x] Create campaign-workflow.md
- [x] Create content-workflow.md
- [x] Create seo-workflow.md
- [x] Create analytics-workflow.md
- [x] Create brand-guidelines-reminder.cjs
- [x] Create campaign-tracking.cjs
- [x] Create approval-workflow.cjs
- [x] Create plans/approvals/ directory
- [x] Update .claude/settings.json
- [ ] Test all workflows (Phase 7)
- [ ] Document workflows (Phase 7)

---

## Success Criteria

1. All 6 workflows created
2. All 3 hooks functional
3. Hooks registered in settings.json
4. Approval system working
5. Campaign tracking logging
6. Brand guidelines injecting
7. End-to-end workflow tests pass

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Workflow complexity | Medium | Medium | Start with simple flows |
| Hook performance | Low | High | Async processing, caching |
| Approval bottleneck | Medium | Medium | Timeout fallbacks |
| Tracking data loss | Low | Low | Backup logging |

---

## Security Considerations

- Approval requests should not contain sensitive data
- Campaign tracking logs may contain PII - handle appropriately
- Hooks should not have write access to production systems
- Audit trail for all approvals

---

## Next Steps

After Phase 6 completion:
1. Proceed to Phase 7: Documentation & Testing
2. Document all workflows
3. Create usage examples
4. Build test suite

---

## Unresolved Questions

1. Should approvals expire after a timeout?
2. Multiple approver support?
3. Workflow versioning strategy?
4. Hook priority/ordering?
5. Workflow state persistence between sessions?
6. Integration with external approval systems (Slack, email)?
