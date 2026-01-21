# /10x/discover - Find People with Exa AI

---

## Description

Discover and find people matching your target criteria using Exa AI search.

---

## Usage

```
/10x/discover [query]
```

---

## Prompt

Activate the discovery engine skill: `.claude/skills/10x-team/outreach/skills/discovery-engine/SKILL.md`

Parse query: `$ARGUMENTS`

### Discovery Process

1. **Parse Query**
   Extract: job titles, industries, locations, keywords

2. **Search with Exa AI**
   Use script: `.claude/skills/10x-team/outreach/scripts/discovery_engine.py`

3. **Compile Results**
   - LinkedIn profiles
   - Twitter handles
   - Company info
   - Recent activity

4. **Output Format**
   Save results to `output/discoveries/{query-slug}.json`

### Requirements
Needs `EXA_API_KEY` in `.env` file.

---

## Examples

```
/10x/discover "AI startup founders in San Francisco"
/10x/discover "Product managers at Series A companies"
/10x/discover "Tech influencers with 10k+ followers"
/10x/discover "SaaS founders building in public"
```

---

## Output

```json
{
  "query": "AI startup founders",
  "results": [
    {
      "name": "John Doe",
      "title": "Founder & CEO",
      "company": "AI Startup",
      "linkedin": "linkedin.com/in/johndoe",
      "twitter": "@johndoe",
      "recent_activity": ["Posted about AI trends"]
    }
  ]
}
```
