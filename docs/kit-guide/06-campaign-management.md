# Campaign Management & Workflow

## Overview

Campaign commands orchestrate full marketing campaigns across multiple channels with coordinated messaging, asset generation, and performance tracking.

## Main Command: `/campaign`

**Description:** Create and manage marketing campaigns

**Usage:**
```bash
/campaign <action> [name]
```

## Actions

### `/campaign create`
Create a new marketing campaign from scratch

**Usage:**
```bash
/campaign create "<campaign-name>"
```

**Examples:**
```bash
/campaign create "Q1 Product Launch"
/campaign create "Black Friday Promotion"
/campaign create "Customer Awareness Campaign"
```

**Workflow:**
1. Gather campaign requirements via questions
2. Use `campaign-manager` agent to generate brief
3. Use `funnel-architect` agent to design funnel
4. Activate `campaign-management` skill
5. Create output structure at `assets/campaigns/{slug}/`

**Output:** Campaign brief + structured folders for assets

### `/campaign status`
Check campaign status and progress

**Usage:**
```bash
/campaign status "<campaign-name>"
```

**Output:** Campaign progress, milestones, current status, blockers

### `/campaign analyze`
Analyze campaign performance and diagnose issues

**Usage:**
```bash
/campaign analyze "<campaign-name>"
```

**Workflow:**
1. Use `analytics-analyst` agent to gather metrics
2. Use `campaign-debugger` agent to identify issues
3. Generate diagnostic report

**Output:** Performance analysis report with recommendations

## Campaign Structure

Each campaign creates this folder structure:

```
assets/
└── campaigns/
    └── {campaign-slug}/
        ├── briefs/
        │   ├── campaign-brief.md          # Campaign overview
        │   ├── target-audience.md         # Audience definition
        │   └── messaging-framework.md     # Key messages
        ├── strategy/
        │   ├── strategy.md                # Campaign strategy
        │   ├── channels.md                # Channel breakdown
        │   ├── timeline.md                # Launch timeline
        │   └── budget.md                  # Budget allocation
        ├── creatives/
        │   ├── email/                     # Email templates
        │   ├── social/                    # Social content
        │   ├── landing-pages/             # Landing page copy
        │   ├── images/                    # Campaign graphics
        │   ├── videos/                    # Video scripts/footage
        │   └── ads/                       # Ad copy variants
        ├── reports/
        │   ├── launch-report.md           # Launch summary
        │   ├── performance-weekly.md      # Weekly metrics
        │   ├── performance-final.md       # Final results
        │   └── learnings.md               # Lessons learned
        └── assets/
            ├── design-guidelines.md       # Campaign-specific visuals
            ├── messaging.md               # Campaign voice
            └── brand-checklist.md         # Brand compliance
```

## Campaign Brief Template

**File:** `briefs/campaign-brief.md`

```markdown
# Campaign Brief: [Campaign Name]

## Overview
- **Campaign Name:** [Full name]
- **Slug:** [URL-friendly slug]
- **Start Date:** [YYYY-MM-DD]
- **End Date:** [YYYY-MM-DD]
- **Budget:** $[amount]
- **Owner:** [Team member]
- **Status:** [Planning/Launching/Active/Closed]

## Objective
[What does this campaign aim to achieve?]

## Key Message
[Core message repeated across all channels]

## Target Audience
- **Primary:** [Demographic/psychographic]
- **Secondary:** [Alternative audience]
- **Pain Point:** [Main problem being solved]
- **Motivation:** [Why they should care]

## Goals & Success Metrics
- Goal 1: [Specific, measurable goal] - Target: [number]
- Goal 2: [Specific, measurable goal] - Target: [number]
- Goal 3: [Specific, measurable goal] - Target: [number]

## Channel Breakdown

| Channel | Format | Frequency | Responsible |
|---------|--------|-----------|------------|
| Email | Newsletter + sequence | 2x/week | [Name] |
| Social | Posts + reels | 5x/day | [Name] |
| Paid Ads | Google + Meta | Continuous | [Name] |
| Blog | Articles | 1x/week | [Name] |

## Campaign Funnel

### Awareness
[How will people learn about this?]

### Consideration
[How will we nurture interest?]

### Decision
[How will we drive action?]

### Retention
[How will we keep them engaged?]

## Key Messages
1. [Message 1]
2. [Message 2]
3. [Message 3]

## Timeline
- **Week 1:** [Activities]
- **Week 2:** [Activities]
- **Week 3:** [Activities]
- **Week 4:** [Activities]

## Budget Allocation
- Email/Nurture: [%] ($[amount])
- Social Media: [%] ($[amount])
- Paid Ads: [%] ($[amount])
- Content: [%] ($[amount])
- Total: $[amount]

## Success Criteria
- [Metric 1]: [Target]
- [Metric 2]: [Target]
- [Metric 3]: [Target]

## Risks & Contingencies
- Risk 1: [Mitigation]
- Risk 2: [Mitigation]

## Brand Compliance
- Voice: [Campaign-specific voice guidelines]
- Visuals: [Campaign visual style]
- Messaging: [Campaign messaging angle]
```

## Campaign Strategy Document

**File:** `strategy/strategy.md`

```markdown
# Campaign Strategy: [Campaign Name]

## Strategic Overview
[High-level campaign strategy and rationale]

## Positioning
[How are we positioning the offer/product?]

## Competitive Advantage
[Why should customers choose us?]

## Customer Journey

### Stage 1: Awareness
- Channels: [Which channels]
- Tactics: [Specific tactics]
- Content: [Type of content]

### Stage 2: Consideration
- Channels: [Which channels]
- Tactics: [Specific tactics]
- Content: [Type of content]

### Stage 3: Decision
- Channels: [Which channels]
- Tactics: [Specific tactics]
- Content: [Type of content]

### Stage 4: Retention
- Channels: [Which channels]
- Tactics: [Specific tactics]
- Content: [Type of content]

## Channel Strategy

### Email Marketing
- Goal: [Specific goal]
- Strategy: [Approach]
- Segments: [Who receives which messages]
- Frequency: [Send schedule]

### Social Media
- Goal: [Specific goal]
- Strategy: [Approach]
- Content pillars: [Main topics]
- Posting schedule: [Frequency per platform]

### Paid Advertising
- Goal: [Specific goal]
- Channels: [Google, Meta, LinkedIn]
- Budget: [Allocation]
- Targeting: [Audience definition]

### Content Marketing
- Goal: [Specific goal]
- Content types: [Blog, guides, etc.]
- Topic focus: [Main themes]
- SEO strategy: [Keyword targets]

## Timeline & Milestones

| Week | Activities | Milestones | Owner |
|------|-----------|-----------|-------|
| 1 | [Activities] | [Milestone] | [Person] |
| 2 | [Activities] | [Milestone] | [Person] |

## Success Metrics & Tracking

### Primary Metrics
- Metric 1: [Current] → [Target] (by [date])
- Metric 2: [Current] → [Target] (by [date])

### Secondary Metrics
- Metric 3: [Current] → [Target]
- Metric 4: [Current] → [Target]

## Risk Management
- Risk 1: [Impact] → [Mitigation]
- Risk 2: [Impact] → [Mitigation]
```

## Campaign Performance Report Template

**File:** `reports/performance-final.md`

```markdown
# Campaign Performance Report: [Campaign Name]

## Campaign Overview
- **Duration:** [Start date] to [End date] ([X days])
- **Budget Spent:** $[amount]
- **ROI:** [ROI percentage]

## Results by Goal

### Goal 1: [Goal description]
- **Target:** [Original target]
- **Actual:** [Actual result]
- **Status:** [Hit/Miss/Exceeded]
- **Variance:** [+/- amount/percentage]

### Goal 2: [Goal description]
- **Target:** [Original target]
- **Actual:** [Actual result]
- **Status:** [Hit/Miss/Exceeded]
- **Variance:** [+/- amount/percentage]

## Results by Channel

### Email Marketing
- Emails sent: [number]
- Open rate: [%]
- Click rate: [%]
- Conversions: [number]

### Social Media
- Total impressions: [number]
- Engagement rate: [%]
- Followers gained: [number]
- Conversions: [number]

### Paid Advertising
- Impressions: [number]
- Clicks: [number]
- CTR: [%]
- CPC: $[amount]
- Conversions: [number]
- CPA: $[amount]

### Content Marketing
- Articles published: [number]
- Traffic: [number]
- Leads: [number]
- Ranking improvements: [metrics]

## Key Insights

### What Worked
1. [Successful tactic/message]
2. [Successful tactic/message]
3. [Successful tactic/message]

### What Didn't Work
1. [Unsuccessful element]
2. [Unsuccessful element]

### Surprises
1. [Unexpected result]
2. [Unexpected finding]

## Recommendations for Next Campaign

1. [Recommendation based on learnings]
2. [Recommendation based on learnings]
3. [Recommendation based on learnings]

## Campaign Learnings

### Audience Insights
- [What we learned about audience]
- [What we learned about messaging]
- [What we learned about channels]

### Content Performance
- Best performing content: [Type/topic]
- Worst performing content: [Type/topic]
- Most shareable content: [Type/topic]

### Optimization Opportunities
- [Opportunity 1]
- [Opportunity 2]
- [Opportunity 3]
```

## Campaign Execution Workflow

### Phase 1: Planning (1-2 weeks before launch)

1. **Define Campaign**
   ```bash
   /campaign create "Campaign Name"
   ```

2. **Create Brief**
   - Complete `briefs/campaign-brief.md`
   - Define goals and success metrics
   - Identify target audience

3. **Develop Strategy**
   - Complete `strategy/strategy.md`
   - Map customer journey
   - Channel planning

4. **Get Approval**
   - Stakeholder review
   - Budget approval
   - Timeline confirmation

### Phase 2: Asset Creation (1-3 weeks)

1. **Email Content**
   ```bash
   /content:good "create email sequence for campaign"
   ```
   Save to: `creatives/email/`

2. **Social Content**
   ```bash
   /social [platform] [type] "campaign-specific content"
   ```
   Save to: `creatives/social/`

3. **Ads & Landing Pages**
   ```bash
   /content:cro "optimize landing page for conversions"
   /design:good "create ad designs"
   ```
   Save to: `creatives/ads/` and `creatives/landing-pages/`

4. **Design Assets**
   ```bash
   /design:generate "campaign visuals"
   ```
   Save to: `creatives/images/`

5. **Quality Review**
   - Brand compliance check
   - Content review
   - Performance optimization

### Phase 3: Launch (Day 1)

1. **Schedule Email**
   - Send initial email or first sequence
   - Document send metrics

2. **Publish Social**
   - Schedule all social posts
   - Set posting times

3. **Activate Ads**
   - Launch paid advertising
   - Set budget caps and schedules

4. **Publish Content**
   - Publish blog posts
   - Update landing pages
   - Go live

5. **Document Launch**
   - Create `reports/launch-report.md`
   - Record baseline metrics

### Phase 4: Monitoring (Throughout campaign)

1. **Daily Check-in**
   - Monitor key metrics
   - Watch for issues
   - Engage with audience

2. **Weekly Review**
   - Update `reports/performance-weekly.md`
   - Identify optimization opportunities
   - Make tactical adjustments

3. **Optimization**
   - A/B test underperforming content
   - Increase spend on winning channels
   - Pause low-performers

### Phase 5: Closing & Analysis (After campaign)

1. **Collect Final Data**
   - Final performance metrics
   - Customer feedback
   - Conversion data

2. **Generate Report**
   ```bash
   /campaign analyze "Campaign Name"
   ```
   Creates: `reports/performance-final.md`

3. **Document Learnings**
   - Complete `reports/learnings.md`
   - Identify best practices
   - Note opportunities

4. **Archive Campaign**
   - Save all assets
   - Backup performance data
   - Update knowledge base

## Campaign Agents

- **campaign-manager** - Orchestrates full campaign
- **funnel-architect** - Designs customer journey
- **content-creator** - Creates campaign content
- **copywriter** - Writes compelling copy
- **email-wizard** - Creates email sequences
- **social-media-manager** - Plans social strategy
- **campaign-debugger** - Analyzes performance
- **analytics-analyst** - Tracks metrics

## Campaign Management Best Practices

1. **Clear Objectives** - Define specific, measurable goals
2. **Integrated Approach** - Coordinate across all channels
3. **Consistent Messaging** - Same core message across channels
4. **Audience Focus** - Deeply understand target audience
5. **Data-Driven** - Track metrics and optimize based on data
6. **Timeline Clarity** - Clear launch and completion dates
7. **Resource Allocation** - Budget aligned with strategy
8. **Regular Monitoring** - Daily tracking of key metrics
9. **Quick Optimization** - Adjust based on performance daily
10. **Document Learnings** - Capture insights for future campaigns

## Next Steps

1. Define first campaign objective
2. Use `/campaign create "Campaign Name"` to generate brief
3. Complete campaign strategy documents
4. Create assets for all channels
5. Launch campaign with coordination
6. Monitor daily and optimize
7. Analyze and document learnings
