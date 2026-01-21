# Phase 3c: SEO & Programmatic SEO

## Context Links

- [Plan Overview](./plan.md)
- [Phase 3: Marketing Skills](./phase-03-marketing-skills.md)
- [Research: SEO Implementation](../reports/seo-implementation-summary.md)
- [Research: pSEO Deep Dive](../reports/pseo-deep-dive.md)
- [Source: ClaudeKit Marketing Overview](../../docs/overall/ClaudeKit-Marketing-Claude-Code-for-Sales-and-Marketing.md#L320-348)

---

## Overview

| Field | Value |
|-------|-------|
| **Timeline** | Dec 21-24, 2025 (parallel with Phase 3) |
| **Priority** | HIGH (key differentiator) |
| **Implementation Status** | DONE (2025-12-11 13:56) |
| **Review Status** | Complete |
| **Description** | Implement comprehensive SEO skill with pSEO engine |
| **Estimated Hours** | 26-34 hours |

---

## Why pSEO is Critical

**Traditional pSEO:** $50k-500k + 6-12 months engineering
**pSEO with Claude Code:** $100-1,000 + AI agents + templates

**Market Gap:** Most marketing tools don't offer pSEO
**Competitive Advantage:** Multi-agent orchestration enables scale

---

## Architecture

### Capability Matrix

| Area | Capabilities | Count |
|------|--------------|-------|
| Technical SEO | Site crawl, Core Web Vitals, meta tags, canonicals, sitemaps, robots.txt, mobile | 7 |
| Content Optimization | Keyword research, content gap, on-page checklist, readability, semantics | 5 |
| Programmatic SEO | Templates, data integration, URL patterns, internal linking, scale | 5 |
| Link Building | Backlink analysis, outreach templates, tracking | 3 |
| Schema Markup | Auto-generation, validation | 2 |
| **Total** | | **22** |

### Skill 

#### Important
Use the existing `/skill:create <prompt>` slash command to create new skills.

#### Structure

```
.claude/skills/seo-optimization/
├── SKILL.md                              # Main skill definition
│
├── references/
│   ├── technical-seo-checklist.md        # 50+ audit items
│   ├── core-web-vitals-remediation.md    # LCP, FID, CLS fixes
│   ├── meta-tag-templates.md             # Title, description patterns
│   ├── canonical-url-strategy.md         # Canonical handling
│   ├── sitemap-best-practices.md         # XML sitemap guide
│   ├── robots-txt-best-practices-2025.md # Robots.txt patterns
│   ├── mobile-seo-checklist.md           # Mobile-first indexing
│   │
│   ├── keyword-research-workflow.md      # Research methodology
│   ├── keyword-clustering-methodology.md # Topic clustering
│   ├── content-gap-analysis-framework.md # Gap identification
│   ├── on-page-seo-checklist-2025.md     # 35+ optimization items
│   ├── readability-scoring-guide.md      # Flesch-Kincaid, etc.
│   ├── semantic-seo-framework.md         # Entity optimization
│   │
│   ├── pseo-template-syntax.md           # Template language guide
│   ├── pseo-best-practices.md            # Quality guidelines
│   ├── pseo-url-structure-guide.md       # URL patterns
│   ├── internal-linking-automation.md    # Link graph optimization
│   ├── pseo-scale-architecture.md        # 100k+ page handling
│   │
│   ├── backlink-analysis-framework.md    # Competitor analysis
│   ├── link-building-campaign-framework.md # Outreach strategy
│   ├── outreach-email-templates.md       # Email templates
│   ├── directory-submission-list.md      # Directory database
│   │
│   ├── google-search-console-api-guide.md # GSC integration
│   ├── search-console-query-patterns.md   # Query examples
│   │
│   └── schema-templates/
│       ├── article-schema.json
│       ├── product-schema.json
│       ├── faq-schema.json
│       ├── howto-schema.json
│       ├── organization-schema.json
│       └── localbusiness-schema.json
│
└── scripts/
    ├── generate-sitemap.cjs              # XML sitemap generator
    ├── analyze-keywords.cjs              # Keyword analysis
    ├── generate-schema.cjs               # JSON-LD generator
    ├── audit-core-web-vitals.cjs         # CWV checker
    ├── validate-schema.cjs               # Schema validator
    └── pseo-generator.cjs                # pSEO page generator
```

---

## Technical SEO Capabilities

### 1. Site Crawl Analysis

**Checks Performed:**
- Broken links (404, 500 errors)
- Redirect chains (301, 302 mapping)
- Duplicate content detection
- Missing meta tags
- Image optimization (alt text, file size)
- Page load performance

**Output:** Structured audit report with severity ratings

### 2. Core Web Vitals Integration

| Metric | Target | Measurement |
|--------|--------|-------------|
| LCP (Largest Contentful Paint) | <2.5s | PageSpeed API |
| FID (First Input Delay) | <100ms | CrUX data |
| CLS (Cumulative Layout Shift) | <0.1 | Lab testing |
| INP (Interaction to Next Paint) | <200ms | CrUX data |

**Remediation Patterns:**
- LCP: Image optimization, lazy loading, server response
- FID/INP: JavaScript optimization, code splitting
- CLS: Size attributes, font loading, ad containers

### 3. Meta Tag Optimization

**Title Tag Template:**
```
{Primary Keyword} - {Secondary Benefit} | {Brand}
Max: 60 characters
```

**Description Template:**
```
{Action verb} {benefit}. {Supporting detail}. {CTA with keyword}.
Target: 155-160 characters
```

### 4. Sitemap Generation

**Script:** `generate-sitemap.cjs`

**Features:**
- Crawl local/deployed site
- Exclude patterns (admin, api, etc.)
- Priority calculation
- Change frequency detection
- Image sitemap support
- News sitemap support

### 5. Robots.txt Optimization

**Best Practices 2025:**
```
User-agent: *
Disallow: /api/
Disallow: /admin/
Disallow: /*?*sort=
Disallow: /*?*filter=

# Crawl budget optimization
Crawl-delay: 1

# Sitemaps
Sitemap: https://example.com/sitemap.xml
Sitemap: https://example.com/sitemap-images.xml
```

---

## JSON+LD Schema Generation

### Supported Schema Types

| Type | Use Case | Auto-Detection |
|------|----------|----------------|
| Article | Blog posts | Content analysis |
| Product | E-commerce | Product data |
| FAQ | FAQ pages | Q&A pattern matching |
| HowTo | Tutorials | Step detection |
| Organization | Company info | About pages |
| LocalBusiness | Local SEO | Business data |

### Auto-Generation Flow

```
1. Analyze page content (Gemini)
2. Detect schema type (pattern matching)
3. Extract relevant data (NER)
4. Generate JSON-LD
5. Validate against Google's requirements
6. Output embeddable script
```

### Schema Template (Article)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title}",
  "description": "{meta_description}",
  "image": "{featured_image_url}",
  "author": {
    "@type": "Person",
    "name": "{author_name}"
  },
  "publisher": {
    "@type": "Organization",
    "name": "{brand_name}",
    "logo": {
      "@type": "ImageObject",
      "url": "{logo_url}"
    }
  },
  "datePublished": "{publish_date}",
  "dateModified": "{modified_date}"
}
```

---

## Programmatic SEO (pSEO)

### Overview

Generate thousands of SEO-optimized pages from data + templates.

**Use Cases:**
- Location pages (city landing pages)
- Product comparisons
- Tool/software directories
- Industry glossaries
- Data-driven content

### Template System

**Syntax (Nunjucks-like):**

```html
<!-- templates/location-page.html -->
<article>
  <h1>Best {{ service }} in {{ city }}, {{ state }}</h1>

  <p>Looking for {{ service }} in {{ city }}?
  {{ city }} has {{ population | formatNumber }} residents
  and {{ businesses_count }} {{ service }} providers.</p>

  <h2>Top {{ service }} Providers in {{ city }}</h2>
  <ul>
  {% for provider in providers %}
    <li>
      <strong>{{ provider.name }}</strong>
      - Rating: {{ provider.rating }}/5
      - {{ provider.reviews }} reviews
    </li>
  {% endfor %}
  </ul>

  <h2>Why Choose {{ city }} for {{ service }}?</h2>
  {{ generated_content }}

  <h2>Frequently Asked Questions</h2>
  {% for faq in faqs %}
    <h3>{{ faq.question }}</h3>
    <p>{{ faq.answer }}</p>
  {% endfor %}
</article>
```

### Data Source Integration

**Supported Sources:**
- CSV files
- JSON files
- Google Sheets (via API)
- Databases (PostgreSQL, SQLite)
- REST APIs

**Data Structure Example:**

```json
{
  "city": "Austin",
  "state": "Texas",
  "population": 1000000,
  "providers": [
    {"name": "Provider A", "rating": 4.8, "reviews": 250},
    {"name": "Provider B", "rating": 4.5, "reviews": 180}
  ]
}
```

### URL Structure Patterns

**Recommended Patterns:**
```
/{service}/{city}/                    # /plumber/austin/
/{service}/{state}/{city}/            # /plumber/texas/austin/
/{category}/{product}-vs-{product}/   # /tools/figma-vs-sketch/
/{topic}/{subtopic}/                  # /marketing/seo-basics/
```

**URL Generation Rules:**
- Lowercase, hyphenated slugs
- No special characters
- Descriptive, keyword-rich
- Consistent structure
- Under 75 characters

### Internal Linking Automation

**Algorithm:**
```
For each page P:
  1. Extract main topics/entities
  2. Find semantically related pages
  3. Score relevance (cosine similarity)
  4. Select top N links (5-10)
  5. Insert contextually in content
  6. Track link graph for orphan detection
```

**Quality Controls:**
- No excessive linking (max 100 internal links/page)
- Contextual relevance required
- Anchor text variation
- Deep link prioritization
- Orphan page alerts

### Scale Architecture

**Performance Benchmarks:**
- Generation: 100 pages/minute
- Validation: 200 pages/minute
- Publication: 50 pages/minute (with crawl delay)
- **Total 100k pages:** 16-24 hours

**Batch Processing:**
```
1. Load data in chunks (1000 rows)
2. Parallel generation (4-8 workers)
3. Quality validation per batch
4. Checkpoint every 5k pages
5. Resume capability on failure
```

### Quality Guardrails

| Check | Threshold | Action if Failed |
|-------|-----------|------------------|
| Word count | >300 words | Regenerate content |
| Readability | Flesch-Kincaid 8-12 | Simplify language |
| Keyword density | 1-3% | Adjust content |
| Duplicate detection | <20% similarity | Rewrite |
| Schema validation | Valid JSON-LD | Fix schema |
| Internal links | 5-10 per page | Add/remove links |

---

## Content Optimization

### Keyword Research Workflow

```
1. Seed keywords → Expand with LSI terms
2. Analyze search volume + difficulty
3. Cluster by topic/intent
4. Map to content pillars
5. Prioritize by opportunity score
```

**Opportunity Score:**
```
Score = (Volume × Intent Match) / (Difficulty + Competition)
```

### Content Gap Analysis

**Process:**
1. Crawl competitor content
2. Extract topics/keywords
3. Compare to own content
4. Identify gaps (topics they rank for, you don't)
5. Prioritize by potential traffic
6. Generate content briefs

### On-Page Checklist (35+ Items)

**Title & Meta:**
- [ ] Primary keyword in title (first 60 chars)
- [ ] Compelling meta description (155-160 chars)
- [ ] Unique title/description per page

**Content:**
- [ ] H1 contains primary keyword
- [ ] Logical heading hierarchy (H1→H2→H3)
- [ ] Keyword in first 100 words
- [ ] LSI keywords naturally integrated
- [ ] Minimum 1000 words (comprehensive content)
- [ ] Readable paragraphs (<300 words each)

**Technical:**
- [ ] Clean URL structure
- [ ] Canonical tag present
- [ ] Mobile-responsive
- [ ] Fast loading (<3s)
- [ ] Schema markup added

**Links:**
- [ ] Internal links (5-10 relevant)
- [ ] External links (2-3 authoritative)
- [ ] No broken links

**Media:**
- [ ] Images with alt text
- [ ] Compressed images (<100KB)
- [ ] Relevant featured image

### Readability Scoring

| Score | Grade Level | Target Audience |
|-------|-------------|-----------------|
| 90-100 | 5th grade | Very easy |
| 80-89 | 6th grade | Easy |
| 70-79 | 7th grade | Fairly easy |
| 60-69 | 8th-9th grade | **Standard (target)** |
| 50-59 | 10th-12th grade | Fairly difficult |
| <50 | College | Difficult |

---

## Link Building

### Backlink Analysis Framework

**Metrics to Analyze:**
- Domain Authority (DA)
- Referring domains count
- Link velocity (new links/month)
- Anchor text distribution
- Dofollow vs nofollow ratio
- Toxic link percentage

**Competitor Gap Analysis:**
```
1. Identify top 5 competitors
2. Extract their backlink profiles
3. Find domains linking to them, not you
4. Prioritize by authority
5. Generate outreach list
```

### Outreach Email Templates

**Guest Post Pitch:**
```
Subject: Content idea for {site_name}

Hi {editor_name},

I noticed your article on {topic} - great insights on {specific_point}.

I'd love to contribute a piece on "{proposed_topic}" covering:
- {point_1}
- {point_2}
- {point_3}

I've written for {publication_1} and {publication_2} on similar topics.

Would this be a fit for {site_name}?

Best,
{your_name}
```

### Directory Submission Tracking

**Database Fields:**
- Directory name
- URL
- Category
- Submission date
- Approval status
- Link type (dofollow/nofollow)
- DA score
- Notes

---

## MCP Integrations

### ReviewWebsite MCP (Primary SEO Intelligence)

**URL:** https://github.com/mrgoonie/reviewwebsite-mcp-server
**Source:** ClaudeKit Author (mrgoonie)

**SEO-Specific Capabilities:**

| Tool | Purpose | Use Case |
|------|---------|----------|
| `seo-keyword-ideas` | Keyword research | Seed expansion, related keywords |
| `seo-keyword-difficulty` | Competition analysis | Ranking difficulty scoring |
| `seo-traffic` | Domain traffic analysis | Competitor traffic estimation |
| `seo-backlinks` | Backlink data | Link profile analysis |
| `convert-to-markdown` | URL-to-Markdown | Analyze competitor content |
| `extract-links` | Link extraction | Internal/external link mapping |
| `summarize-url` | AI summarization | Content analysis |
| `extract-data` | Structured data | Extract any data from pages |
| `scrape-url` | Raw content | Full page content retrieval |

**Key Advantages:**
- Bypasses captcha gates (critical for analyzing X, Reddit, etc.)
- Built-in SEO data (no separate Ahrefs/SEMrush needed initially)
- From ClaudeKit author - guaranteed compatibility
- Single API for content + SEO intelligence

**Configuration:**
```json
{
  "reviewwebsite": {
    "command": "node",
    "args": ["/path/to/reviewwebsite-mcp-server/dist/index.js"],
    "env": {
      "REVIEWWEBSITE_API_KEY": "${REVIEWWEBSITE_API_KEY}"
    }
  }
}
```

**Example Usage Patterns:**
```javascript
// Keyword research for topic
seoKeywordIdeas({ keyword: "marketing automation", limit: 50 });

// Check keyword difficulty
seoKeywordDifficulty({ keyword: "email marketing software" });

// Analyze competitor content
convertToMarkdown({ url: "https://competitor.com/blog/seo-guide" });

// Get backlink data
seoBacklinks({ domain: "competitor.com", limit: 100 });

// Analyze viral Reddit post
convertToMarkdown({ url: "https://reddit.com/r/marketing/comments/..." });
```

---

### Google Search Console MCP

**URL:** github.com/Shin-sibainu/google-search-console-mcp-server

**Capabilities:**
- Search performance data (queries, clicks, impressions, CTR, position)
- URL inspection (indexed status, issues)
- Sitemap status
- Coverage reports

**Query Patterns:**
```javascript
// Top performing queries
getSearchAnalytics({
  siteUrl: 'https://example.com',
  startDate: '2025-01-01',
  endDate: '2025-12-09',
  dimensions: ['query'],
  rowLimit: 100
});

// Pages with high impressions, low CTR
getSearchAnalytics({
  siteUrl: 'https://example.com',
  dimensions: ['page'],
  filters: [{ dimension: 'ctr', operator: 'lessThan', value: 0.02 }]
});
```

---

### Chrome DevTools MCP (Existing)

**Use Cases:**
- Lighthouse audits (programmatic)
- Core Web Vitals measurement
- JavaScript error detection
- Network waterfall analysis

---

## Commands (Phase 4)

### SEO Commands

```
/seo audit [url]
  Full technical SEO audit
  - Crawl analysis
  - Meta tag review
  - Core Web Vitals
  - Schema validation
  Output: reports/seo/audit-{domain}-{date}.md

/seo keywords [topic]
  Keyword research + clustering
  - Seed expansion
  - Volume/difficulty analysis
  - Topic clustering
  Output: reports/seo/keywords-{topic}-{date}.md

/seo schema [page-path]
  Auto-generate JSON-LD schema
  - Content analysis
  - Schema type detection
  - Validation
  Output: Schema code block + validation result

/seo optimize [content-path]
  On-page optimization recommendations
  - Checklist validation
  - Improvement suggestions
  - Score before/after
  Output: Inline recommendations

/seo pseo [template] [data-source]
  Programmatic SEO generation
  - Template rendering
  - Quality validation
  - Batch output
  Output: generated-pages/

/seo links [competitor-url]
  Backlink analysis + outreach
  - Competitor profile
  - Gap identification
  - Outreach templates
  Output: reports/seo/links-{competitor}-{date}.md

/seo gap [niche]
  Content gap analysis
  - Competitor content crawl
  - Topic extraction
  - Opportunity scoring
  Output: reports/seo/gap-{niche}-{date}.md

/seo report [domain]
  Comprehensive SEO health report
  - All audit areas
  - Trends over time
  - Priority recommendations
  Output: reports/seo/report-{domain}-{date}.md
```

---

## Implementation Steps

### Phase 3c-1: Core Technical SEO (Day 1)

1. Create skill directory structure
2. Write SKILL.md definition
3. Create technical-seo-checklist.md
4. Create core-web-vitals-remediation.md
5. Implement generate-sitemap.cjs
6. Create robots-txt-best-practices-2025.md
7. Create meta-tag-templates.md

### Phase 3c-2: Content & Schema (Day 2)

8. Create keyword-research-workflow.md
9. Create on-page-seo-checklist-2025.md
10. Create readability-scoring-guide.md
11. Create semantic-seo-framework.md
12. Implement generate-schema.cjs
13. Create all schema templates (6 types)
14. Implement validate-schema.cjs

### Phase 3c-3: Programmatic SEO (Day 3)

15. Create pseo-template-syntax.md
16. Create pseo-best-practices.md
17. Create pseo-url-structure-guide.md
18. Create internal-linking-automation.md
19. Create pseo-scale-architecture.md
20. Implement pseo-generator.cjs
21. Test batch generation

### Phase 3c-4: Link Building & Analytics (Day 4)

22. Create backlink-analysis-framework.md
23. Create outreach-email-templates.md
24. Create directory-submission-list.md
25. Create google-search-console-api-guide.md
26. Create search-console-query-patterns.md
27. Integration testing
28. Documentation updates

---

## Todo List

- [x] Create seo-optimization skill directory
- [x] Write SKILL.md main definition
- [x] Create technical-seo-checklist.md (50+ items)
- [x] Create core-web-vitals-remediation.md
- [x] Create meta-tag-templates.md
- [x] Create canonical-url-strategy.md
- [x] Create sitemap-best-practices.md
- [x] Create robots-txt-best-practices-2025.md
- [x] Create mobile-seo-checklist.md
- [x] Create keyword-research-workflow.md
- [x] Create keyword-clustering-methodology.md
- [x] Create content-gap-analysis-framework.md
- [x] Create on-page-seo-checklist-2025.md
- [x] Create readability-scoring-guide.md
- [x] Create semantic-seo-framework.md
- [x] Create pseo-template-syntax.md
- [x] Create pseo-best-practices.md
- [x] Create pseo-url-structure-guide.md
- [x] Create internal-linking-automation.md
- [x] Create pseo-scale-architecture.md
- [x] Create backlink-analysis-framework.md
- [x] Create link-building-campaign-framework.md
- [x] Create outreach-email-templates.md
- [x] Create directory-submission-list.md
- [x] Create google-search-console-api-guide.md
- [x] Create search-console-query-patterns.md
- [x] Create all schema templates (6 files)
- [x] Implement generate-sitemap.cjs
- [x] Implement analyze-keywords.cjs
- [x] Implement generate-schema.cjs
- [x] Implement validate-schema.cjs
- [x] Implement pseo-generator.cjs
- [x] Implement audit-core-web-vitals.cjs
- [x] Integration testing
- [x] Update skill-catalog.md

**Completion Date:** 2025-12-11 14:30

---

## Success Criteria

1. seo-optimization skill loads correctly
2. Technical audit identifies real issues
3. Schema generation passes Rich Results test
4. Keyword research provides actionable clusters
5. pSEO generates valid HTML at scale
6. Internal linking prevents orphan pages
7. Search Console integration returns data
8. All reference files comprehensive

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| pSEO thin content penalty | Medium | High | Quality guardrails, manual review |
| Search Console API limits | Low | Medium | Caching, batch queries |
| Schema validation failures | Low | Low | Validation before publish |
| Keyword data accuracy | Medium | Medium | Multiple sources, manual verification |
| Scale performance | Medium | Medium | Batch processing, checkpointing |

---

## API Dependencies

### Required (Phase 3)

| API | Purpose | Cost |
|-----|---------|------|
| ReviewWebsite MCP | Keywords, backlinks, content scraping | Per API plan |
| PageSpeed Insights | Core Web Vitals | Free |
| Chrome DevTools MCP | Lighthouse audits | Free |

**Note:** ReviewWebsite MCP provides keyword research, difficulty scoring, traffic analysis, and backlinks - reducing/eliminating need for expensive Ahrefs/SEMrush subscriptions.

### Recommended (Phase 3)

| API | Purpose | Cost |
|-----|---------|------|
| Search Console API | Search performance | Free (OAuth) |

### Optional (Phase 4+)

| API | Purpose | Cost |
|-----|---------|------|
| Ahrefs API | Advanced backlink data | $99+/month |
| SEMrush API | Advanced keyword data | $119+/month |
| SerpStack | SERP results | $29+/month |

**Cost Savings with ReviewWebsite MCP:** By using ReviewWebsite for basic SEO intelligence, teams can delay or avoid $200+/month in third-party SEO tool subscriptions.

---

## Agent Integration

### Primary: seo-specialist agent

- Technical SEO audits
- Keyword research
- Content optimization
- pSEO template design

### Secondary: attraction-specialist agent

- Link building campaigns
- Outreach automation
- pSEO scaling

### Tertiary: content-creator agent

- Content gap filling
- Schema markup for content
- Readability improvement

---

## Security Considerations

- OAuth tokens secured
- API keys in environment
- No PII in reports
- Rate limit compliance
- Credential rotation

---

## Next Steps

After Phase 3c completion:
1. Create /seo commands in Phase 4
2. Integrate with campaign workflows
3. Build pSEO dashboard (future)
4. Add Ahrefs/SEMrush integrations (optional)

---

## Unresolved Questions

1. Ahrefs vs SEMrush API preference?
2. pSEO content uniqueness threshold?
3. Link building automation ethics?
4. Schema validation frequency?
5. Keyword data freshness requirements?
6. pSEO publication cadence limits?
