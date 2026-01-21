# ClaudeKit Marketing - Manual Test Guide

Quick hands-on guide to test all major features.

---

## Prerequisites

```bash
cd /Applications/MAMP/htdocs/claudekit-marketing/claudekit-marketing
```

Ensure `docs/brand-guidelines.md` exists with your brand info.

---

## 1. Dashboard (Mini App)

**Start:**
```bash
/dashboard
```

**Test:**
- [ ] Opens at http://localhost:5173
- [ ] Brand Center shows colors, typography, logos
- [ ] Asset Gallery lists files from `assets/`
- [ ] Can upload a logo (PNG/SVG)

---

## 2. Design Commands

### 2.1 Image Generation
```bash
/design:generate "hero banner for SaaS landing page with dark gradient"
```
**Expect:** Imagen 4 generates image → `assets/images/generated/`

### 2.2 Full Design Workflow
```bash
/design:good "create a modern pricing section with 3 tiers"
```
**Expect:** Research → design → HTML output

### 2.3 Slides
```bash
/slides:create "5-slide investor pitch for AI marketing tool"
```
**Expect:** Interactive HTML slides → `assets/designs/slides/`

**Verify slides work:**
```bash
open assets/designs/slides/*.html
```
- [ ] Arrow keys navigate
- [ ] Progress bar updates
- [ ] Charts render (Chart.js)

---

## 3. YouTube Content Repurposing

Use any YouTube video URL. Example:
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### 3.1 YouTube → Infographic
```bash
/youtube:infographic "https://www.youtube.com/watch?v=VIDEO_ID"
```
**Expect:** HTML infographic → `assets/infographics/`

### 3.2 YouTube → Blog Post
```bash
/youtube:blog "https://www.youtube.com/watch?v=VIDEO_ID"
```
**Expect:** SEO article → `assets/articles/`

### 3.3 YouTube → Social Posts
```bash
/youtube:social "https://www.youtube.com/watch?v=VIDEO_ID"
```
**Expect:** Multi-platform posts (Twitter, LinkedIn, Instagram, TikTok) → `assets/posts/`

---

## 4. Content Writing

### 4.1 Blog Post
```bash
/write:blog "10 AI marketing trends for 2025"
```
**Expect:** SEO-optimized article with headings, keywords → `assets/articles/`

### 4.2 Content Enhancement
```bash
/write:enhance "make this headline more compelling: 'Our Product Features'"
```
**Expect:** Multiple improved variants

### 4.3 CRO Optimization
```bash
/write:cro "optimize this CTA: 'Click here to learn more'"
```
**Expect:** A/B test variants with conversion focus

---

## 5. Copywriting Formulas

### 5.1 AIDA Formula
```bash
/copy:formula AIDA "project management SaaS"
```
**Expect:** Short/Medium/Long versions → `assets/copy/`

### 5.2 PAS Formula
```bash
/copy:formula PAS "email deliverability problems"
```

### 5.3 BAB Formula
```bash
/copy:formula BAB "fitness transformation"
```

---

## 6. Social Media

### 6.1 Platform-Specific Post
```bash
/social twitter thread "5 tips for startup marketing"
/social linkedin post "thought leadership on AI"
/social instagram carousel "product features showcase"
```

### 6.2 Schedule Planning
```bash
/social:schedule week
```
**Expect:** 7-day posting calendar → `assets/posts/schedule-week.md`

---

## 7. Email Marketing

### 7.1 Email Sequence
```bash
/email:sequence welcome
/email:sequence onboarding "SaaS product"
```
**Expect:** Multi-email sequence with subject lines → `assets/copy/emails/`

---

## 8. Brand System Scripts

### 8.1 Brand Context Injection
```bash
node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs --json
```
**Expect:** JSON with colors, typography, voice

### 8.2 Sync Brand to Tokens
```bash
node .claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs
```
**Expect:** Updates `assets/design-tokens.json` and `.css`

### 8.3 Slide Search
```bash
python3 .claude/skills/design-system/scripts/search-slides.py "investor pitch" -d strategy
```
**Expect:** Deck structures with emotion arcs

### 8.4 Background Image
```bash
python3 .claude/skills/design-system/scripts/fetch-background.py hero --css
```
**Expect:** Pexels URL + overlay CSS with brand colors

---

## 9. Verification Checklist

| Feature | Command | Output Location |
|---------|---------|-----------------|
| Dashboard | `/dashboard` | http://localhost:5173 |
| Image Gen | `/design:generate` | `assets/images/generated/` |
| Slides | `/slides:create` | `assets/designs/slides/` |
| Infographic | `/youtube:infographic` | `assets/infographics/` |
| Blog | `/write:blog` | `assets/articles/` |
| Social | `/youtube:social` | `assets/posts/` |
| Copy | `/copy:formula` | `assets/copy/` |
| Email | `/email:sequence` | `assets/copy/emails/` |

---

## 10. Quick Power Demo

Run these 5 commands in sequence to see full pipeline:

```bash
# 1. Generate brand-aware hero image
/design:generate "dark mode SaaS dashboard hero with blue accents"

# 2. Create investor pitch slides
/slides:create "7-slide seed pitch for AI marketing automation tool"

# 3. Convert YouTube video to multi-format content
/youtube:social "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 4. Generate copy with proven formula
/copy:formula AIDA "AI-powered marketing automation"

# 5. Create email welcome sequence
/email:sequence welcome "marketing SaaS for indie hackers"
```

**Result:** 5 different asset types generated with brand consistency.

---

## Troubleshooting

**Dashboard won't start?**
```bash
cd .claude/skills/marketing-dashboard/server && npm run dev
# In another terminal:
cd .claude/skills/marketing-dashboard/app && npm run dev
```

**Brand context empty?**
- Check `docs/brand-guidelines.md` exists
- Run `sync-brand-to-tokens.cjs` to regenerate tokens

**Slides don't render charts?**
- Open HTML in browser (not preview)
- Check Chart.js CDN loads

**YouTube commands fail?**
- Verify VidCap API key in environment
- Check video is public
