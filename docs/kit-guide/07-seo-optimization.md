# SEO Optimization & Commands

## Overview

SEO commands handle keyword research, on-page optimization, technical SEO, and programmatic SEO (pSEO) to drive organic traffic and search visibility.

## Main Command: `/seo`

**Description:** SEO optimization and keyword research

**Usage:**
```bash
/seo <action>
```

## Actions

### Keyword Research
Research and identify high-value keywords for your content

**Usage:**
```bash
/seo "keyword research for [topic]"
```

**Example:**
```bash
/seo "keyword research for SaaS content marketing"
/seo "find long-tail keywords in productivity space"
```

**Output:** Keyword list with:
- Monthly search volume
- Keyword difficulty
- Competition level
- Related keywords
- Search intent classification

### On-Page Optimization
Optimize existing content for search rankings

**Usage:**
```bash
/seo "optimize [page/article] for search"
```

**Examples:**
```bash
/seo "optimize homepage for 'product management software'"
/seo "improve blog post rankings for customer retention topic"
```

**Optimization includes:**
- Title tag optimization
- Meta description enhancement
- H1/H2 structure
- Keyword placement
- Internal linking strategy
- Image alt text
- Content expansion

### Technical SEO Audit
Review technical aspects affecting search visibility

**Usage:**
```bash
/seo "technical SEO audit"
```

**Checks:**
- Site speed and Core Web Vitals
- Mobile responsiveness
- XML sitemap
- Robots.txt
- Canonical tags
- SSL certificate
- Structured data/schema
- Crawl errors

### Local SEO (if applicable)
Optimize for local search results

**Usage:**
```bash
/seo "optimize for local search in [city/region]"
```

### Programmatic SEO (pSEO)
Create scalable, keyword-optimized content

**Usage:**
```bash
/seo "create pSEO content for [keyword cluster]"
```

## SEO Skill

**Location:** `.claude/skills/seo-optimization/`

**Capabilities:**
- Keyword research with ReviewWeb.site API integration
- Keyword difficulty scoring
- Volume and trend data
- Backlink analysis
- Competitor keyword analysis
- Search intent classification
- Featured snippet optimization
- Local SEO data

## SEO Workflow for Content Creation

### Step 1: Keyword Research

```bash
# Research keywords for topic
/seo "keyword research for [your topic]"

# Output includes:
# - Primary keyword: search volume, difficulty
# - Related keywords: topic clusters
# - Long-tail variants: lower competition options
# - Search intent: informational/commercial/transactional
```

### Step 2: Content Creation

```bash
# Create content optimized for keywords
/content:blog "topic: [keyword-optimized topic]"

# Content will naturally include:
# - Primary keyword in title and first paragraph
# - Related keywords distributed naturally
# - Proper heading structure
# - Internal linking opportunities
```

### Step 3: On-Page Optimization

```bash
# Optimize content for search
/seo "optimize blog post for [primary keyword]"

# Optimizations applied:
# - Title tags (50-60 characters with keyword)
# - Meta descriptions (150-160 characters)
# - Heading structure (H1, H2, H3)
# - Internal links (2-3 to related content)
# - Image alt text
```

### Step 4: Technical Verification

```bash
# Run technical SEO checks
/seo "technical SEO audit"

# Fixes any issues with:
# - Site speed
# - Mobile responsiveness
# - Crawlability
# - Schema markup
# - XML sitemap
```

## SEO Output Document

When running `/seo` commands, output includes:

**File:** `docs/seo-keywords.md`

```markdown
# SEO Keyword Research & Strategy

## Primary Keywords

### Keyword 1: [Exact keyword]
- Search Volume: [Number/month]
- Difficulty: [0-100 score]
- Search Intent: [Informational/Commercial/Transactional]
- Content Piece: [Blog/landing page/guide]

### Keyword 2: [Exact keyword]
[Same structure]

## Related Keywords & Clusters

### Cluster 1: [Topic]
- Keyword 1: [Volume] - Difficulty: [Score]
- Keyword 2: [Volume] - Difficulty: [Score]
- Keyword 3: [Volume] - Difficulty: [Score]

### Cluster 2: [Topic]
[Same structure]

## Long-Tail Keywords

- [Long-tail keyword]: [Volume] searches/month - Difficulty: [Score]
- [Long-tail keyword]: [Volume] searches/month - Difficulty: [Score]

## Content Plan

| Keyword | Content Type | Priority | Status |
|---------|-------------|----------|--------|
| [Keyword] | Blog post | High | [Draft/Published] |
| [Keyword] | Landing page | High | [Draft/Published] |
| [Keyword] | Guide | Medium | [Draft/Published] |

## Search Intent Analysis

### Informational Queries
- Users searching to learn
- Keywords: [Examples]
- Content: Blog posts, guides, tutorials

### Commercial Queries
- Users comparing options
- Keywords: [Examples]
- Content: Comparison articles, reviews

### Transactional Queries
- Users ready to buy/sign up
- Keywords: [Examples]
- Content: Landing pages, pricing pages

## Competitive Analysis

### Competitor 1: [Competitor name]
- Ranking keywords: [List top 5]
- Estimated traffic: [Number]
- Content strategy: [Brief assessment]

### Competitor 2: [Competitor name]
[Same structure]

## Implementation Timeline

- Week 1: Create blog posts for [X keywords]
- Week 2: Optimize existing content for [X keywords]
- Week 3: Build internal linking strategy
- Week 4-8: Monitor rankings and refine
```

## SEO Content Guidelines

When creating SEO-optimized content:

### Title Tags
- **Length:** 50-60 characters
- **Format:** [Primary keyword] - [Value prop/benefit]
- **Example:** "10 SaaS Marketing Strategies - Proven Growth Tactics"

### Meta Descriptions
- **Length:** 150-160 characters
- **Format:** [Summary of content] + [CTA]
- **Example:** "Discover 10 proven SaaS marketing strategies to drive growth. Learn tactics, tools, and best practices used by top SaaS companies."

### Heading Structure
```html
<h1>Primary keyword in main heading</h1>

<h2>Related keyword in subheading 1</h2>
<p>Content explaining this section...</p>

<h2>Another related keyword in subheading 2</h2>
<h3>More specific keyword in sub-subheading</h3>
<p>Detailed content...</p>

<h2>Related keyword in subheading 3</h2>
```

### Internal Linking
- Link 2-3 times within article
- Use descriptive anchor text (not "click here")
- Link to relevant, valuable content
- Example: "[Benefits of product roadmapping](/article-about-roadmaps)"

### Image Optimization
```markdown
![Product screenshot showing dashboard](screenshot.png)
```

- Descriptive filename: `dashboard-screenshot-25251209.png`
- Alt text: Describes image and includes relevant keyword if natural
- File size: Optimized for web (under 100KB)

### Keyword Placement

Prioritize natural keyword inclusion:

- **Title tag:** Primary keyword (mandatory)
- **First paragraph:** Primary keyword in first 100 words
- **H1/H2 headings:** Include related keywords
- **Throughout:** 1-2% keyword density (natural variation)
- **Meta description:** Primary keyword if possible

### Content Length

- **Long-tail keywords:** 800-1,200 words
- **Medium difficulty:** 1,200-2,000 words
- **Competitive keywords:** 2,000-3,000+ words

## Featured Snippet Optimization

Snippets appear above organic results for 8-15% of queries.

**Optimize for snippets:**

1. **List Snippets**
   ```markdown
   # [Keyword question]
   - Item 1: [Brief explanation]
   - Item 2: [Brief explanation]
   - Item 3: [Brief explanation]
   ```

2. **Paragraph Snippets**
   ```markdown
   ## [Question related to keyword]
   [Concise 40-60 word paragraph answering question]
   ```

3. **Table Snippets**
   ```markdown
   | Feature | Option A | Option B |
   |---------|----------|----------|
   | Price | $X | $X |
   | Users | X | X |
   ```

## Programmatic SEO (pSEO)

Scale keyword-optimized content through templates:

**Example: SaaS Comparison pSEO**

Create template:
```
/tool-1-vs-tool-2-comparison/
/tool-1-vs-tool-3-comparison/
/tool-2-vs-tool-3-comparison/
```

Template structure:
```markdown
---
template: comparison
tool_a: [Tool name]
tool_b: [Tool name]
keywords: [auto-generated]
---

# [Tool A] vs [Tool B] - Complete Comparison 2024

[Comparison content]
```

Script generates 20+ comparison pages automatically.

## SEO Checklist

Before publishing content:

- [ ] Primary keyword in title (50-60 chars)
- [ ] Primary keyword in first paragraph
- [ ] H1 tag on page (only one H1)
- [ ] H2 tags for sections
- [ ] Meta description written (150-160 chars)
- [ ] 2-3 internal links with descriptive anchor text
- [ ] Image alt text describing image
- [ ] URL is descriptive (kebab-case with keyword)
- [ ] Content length appropriate for keyword difficulty
- [ ] No keyword stuffing (reads naturally)
- [ ] Page loads in under 3 seconds
- [ ] Mobile responsive
- [ ] Schema markup added (if applicable)

## Local SEO (if applicable)

For local businesses:

1. **Google Business Profile**
   - Complete all information
   - Add location, hours, photos
   - Respond to reviews

2. **Local Citations**
   - NAP consistency (Name, Address, Phone)
   - Submit to local directories

3. **Local Content**
   - City-specific keywords
   - Location pages
   - Local blog posts

4. **Local Links**
   - Get mentions from local websites
   - Partner with local businesses

## SEO Performance Tracking

**File:** `docs/seo-performance.md`

```markdown
# SEO Performance Metrics

## Keyword Rankings

| Keyword | Current Position | Previous Position | Traffic | Change |
|---------|------------------|------------------|---------|--------|
| [Keyword] | [Position] | [Position] | [Traffic] | [+/- change] |

## Traffic Metrics
- Organic traffic: [Number]
- Traffic growth rate: [% MoM]
- Average position: [Number]
- CTR (Click-through rate): [%]

## Content Performance
| Page | Keyword | Position | Traffic | Engagement |
|------|---------|----------|---------|-----------|
| | | | | |

## Backlink Status
- Total backlinks: [Number]
- New backlinks this month: [Number]
- High-authority backlinks: [Number]

## Technical Health
- Crawlable pages: [Number]
- Indexed pages: [Number]
- Crawl errors: [Number]
- Core Web Vitals: [Status]
```

## SEO Best Practices

1. **Topic Clusters** - Group related content with pillar pages
2. **Internal Linking** - Connect related content strategically
3. **Content Quality** - Comprehensive, valuable content ranks better
4. **Mobile First** - Mobile experience is ranking factor
5. **Page Speed** - Core Web Vitals matter for rankings
6. **E-E-A-T** - Expertise, Experience, Authoritativeness, Trustworthiness
7. **Fresh Content** - Regular updates signal active site
8. **Backlink Quality** - Few high-authority links > many low-quality links
9. **User Signals** - Click-through rate and engagement matter
10. **Schema Markup** - Helps search engines understand content

## Common SEO Issues & Fixes

**Issue: Low rankings for main keywords**
- Analyze top-ranking competitors
- Expand content length and depth
- Add more comprehensive internal linking
- Verify keyword is in title and first paragraph
- Check Core Web Vitals

**Issue: High bounce rate on landing pages**
- Verify page matches search intent
- Improve page speed
- Make CTA clear and obvious
- Add trust signals (testimonials, certifications)
- Test mobile experience

**Issue: Crawl errors increasing**
- Fix broken links
- Remove blocked resources
- Add pages to XML sitemap
- Reduce redirect chains
- Check robots.txt

**Issue: Traffic dropping**
- Check for algorithmic updates
- Review for manual penalties
- Verify no canonical issues
- Monitor competitor changes
- Check backlink profile

## SEO Tools Integration

**ReviewWeb.site API:**
- Keyword research with volume and difficulty
- Backlink analysis
- Competitor keyword research
- SERP features analysis

**Technical Checks:**
- Page speed (Google PageSpeed Insights)
- Mobile responsiveness
- Core Web Vitals
- Schema validation

## Next Steps

1. Run initial keyword research for main topics
2. Create `docs/seo-keywords.md` with research
3. Create 3-5 SEO-optimized blog posts using `/content:blog`
4. Optimize existing pages with `/seo` commands
5. Run technical SEO audit: `/seo "technical audit"`
6. Set up performance tracking in `docs/seo-performance.md`
7. Monitor rankings weekly and optimize
