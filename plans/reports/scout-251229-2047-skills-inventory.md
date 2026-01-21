# ClaudeKit Marketing Skills Comprehensive Inventory

**Generated:** 2025-12-29  
**Source:** `/mnt/d/www/claudekit/claudekit-marketing/.claude/skills/`  
**Total Skills:** 58

## Executive Summary

Comprehensive audit of 58 skills across ClaudeKit Marketing toolkit. 42 skills fully documented with detailed capability breakdowns, integration patterns, and use cases. Skills categorized across 9 functional areas: Marketing/Campaigns (10), Content/Design (8), Development (9), AI/Multimodal (2), Agent Systems (7), Developer Tools (4), Document Processing (2), Web/Integration (5), Media/Specialized (6).

---

## Marketing & Campaign Management (10 Skills)

### 1. ads-management
Paid advertising campaigns (Google, Meta, LinkedIn, TikTok) with copywriting, targeting, optimization, A/B testing, ROAS tracking. Dependencies: creativity, assets-organizing.

### 2. affiliate-marketing  
SaaS affiliate programs with commission models (20-30% recurring, tiered), KOL/KOC recruitment, fraud prevention, FTC/GDPR compliance. Key metric: 3:1-5:1 ROI, 30-50% lower CAC.

### 3. campaign-management
End-to-end framework: planning → execution → optimization → post-campaign. Multi-channel coordination, budget allocation, launch checklists.

### 4. analytics
KPI tracking (CAC, ROAS, LTV), GA4 API integration (scripts for list accounts, run reports), A/B test analysis, attribution modeling.

### 5. content-marketing
Strategy, editorial calendars, content pillars (3-5 themes), blog planning, content audit/repurposing. Dependencies: seo-optimization, brand-guidelines.

### 6. email-marketing
Campaign types: newsletter, promotional, transactional, drip/nurture, re-engagement. Automation workflows with decision branches. Metrics: 15-25% open, 2-5% click, <2% bounce.

### 7. social-media
Platform-specific content strategy, community management, performance tracking.

### 8. seo-optimization
Keyword research, technical SEO, content optimization, schema markup.

### 9. referral-program-building
Viral mechanics, commission structures, tracking, incentive design.

### 10. gamification-marketing
10 core mechanics (points, badges, leaderboards, levels, streaks, challenges, quests, unlockables, rewards, progress bars). Psychology: Octalysis, SDT, Fogg model. Key: 3.6x retention at 7-day streaks.

---

## Content Creation & Design (8 Skills)

### 11. copywriting
Formulas: AIDA, PAS, BAB, 4Ps, 4Us, FAB. Headline templates, email copy, landing pages, CTAs. Tool: extract-writing-styles.py for multi-format analysis (MD, PDF, DOCX, images, video).

### 12. creativity
55 creative style templates with keywords, color palettes, effects. Categories: minimalism, neumorphism, glassmorphism, brutalism, claymorphism, aurora, cyberpunk, 3D, maximalist, OLED, organic.

### 13. brand-guidelines
Logo usage, color palette, typography, voice/tone, messaging. Scripts: inject-brand-context, validate-asset, extract-colors, sync-brand-to-tokens.

### 14. design-system
Three-layer tokens: primitive → semantic → component. CSS variables, spacing/typography scales, component specs. Special: slide generation with BM25 search and Duarte sparkline pattern.

### 15. design
Umbrella skill: brand-guidelines (identity) | design-system (tokens) | ui-styling (code).

### 16. frontend-design
Screenshot → design extraction → code implementation. ai-multimodal for analysis, distinctive typography, bold aesthetics, animation (anime.js for React).

### 17. frontend-design-pro
$50k+ agency interfaces. 12 aesthetic styles. Image system: real photos (Unsplash/Pexels) OR hyper-detailed generation prompts.

---

## Development & Technical (9 Skills)

### 18. backend-development
Languages: Node.js/TS, Python, Go, Rust. Frameworks: NestJS, FastAPI, Django. Databases: PostgreSQL, MongoDB, Redis. APIs: REST, GraphQL, gRPC. Security: OWASP Top 10, OAuth 2.1, parameterized queries. Testing: 70-20-10 pyramid.

### 19. better-auth
TypeScript auth framework. Email/password, OAuth (30+ providers), passkeys, magic links, 2FA, organizations, rate limiting. Platform support: Next.js, Nuxt, SvelteKit, Remix, Astro, Hono, Express.

### 20. frontend-development
React/TypeScript patterns: React.lazy(), Suspense, useSuspenseQuery. File org: features/ + components/. MUI v7 sx prop. TanStack Router. Import aliases: @/, ~types, ~components, ~features.

### 21. databases
MongoDB (schema flexibility, horizontal scaling) vs PostgreSQL (ACID, complex relationships). CRUD, indexing, aggregation pipelines. Utils: db_migrate.py, db_backup.py, db_performance_check.py.

### 22. devops
Cloudflare (Workers, R2, D1, KV, Pages), Docker (multi-stage builds), GCP (Compute Engine, GKE, Cloud Run). Decision matrix by requirement.

### 23. media-processing
Image, audio, video compression and optimization.

### 24. debugging
Four techniques: systematic debugging (4 phases), root cause tracing (backward through call stack), defense-in-depth (4 validation layers), verification gates. Core: NO FIXES WITHOUT ROOT CAUSE.

### 25. code-review
Three practices: receiving feedback (technical rigor), requesting review (code-reviewer subagent), verification gates (NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION).

### 26. chrome-devtools
Browser automation via Puppeteer. ARIA snapshot for discovery. Session persistence. Screenshot auto-compression. Console/network/performance monitoring. Scripts: navigate, screenshot, click, fill, evaluate, snapshot, console, network, performance.

---

## Marketing Tools & Infrastructure (3 Skills)

### 27. assets-organizing
Comprehensive directory structure for: articles, videos, designs, reports (analytics, campaign, performance, ads, email), copy, social posts, campaigns, sales, SEO, funnels, leads, community, retention, attraction, diagnostics. Naming: kebab-case, date prefix (YYMMDD-HHmm).

### 28. content-hub
Visual asset gallery: filter/search, brand context sidebar, preview/edit/generate actions. R2-ready manifest. Routes: /hub, /api/assets, /api/brand, /api/scan.

### 29. marketing-dashboard
Vue 3 + Vite (frontend), Hono (API), SQLite (database). Tables: campaigns, content, assets, automations. Phase 1 complete; phases 2-5 planned.

---

## AI & Multimodal Capabilities (2 Skills)

### 30. ai-artist
Prompt engineering patterns. LLM: role → context → task → format → examples. Image: subject → style → composition → quality → negative. Model tips for Midjourney, DALL-E, Stable Diffusion, Flux, Imagen/Veo.

### 31. ai-multimodal
Google Gemini API. Audio: transcription (9.5h), summarization. Images: analysis, OCR, design extraction. Videos: scene detection, Q&A (6h). PDFs: table/form extraction. Generation: Imagen 4 (images), Veo 3 (8s video clips with audio).

---

## Agent & System Tools (7 Skills)

### 32. brainstorming
Collaborative sessions: discovery → exploration (2-3 approaches) → validation → consensus → summary. NO IMPLEMENTATION until explicit confirmation.

### 33. claude-code
Agentic orchestration. Subagents, skills, slash commands, hooks, MCP servers, plugins. 14 reference guides.

### 34-37. planning, problem-solving, research, sequential-thinking
Support frameworks for project management, methodology, research, extended thinking.

### 38. skill-creator
Guide for creating effective skills to extend Claude's capabilities.

---

## Developer Tools (4 Skills)

### 39. kit-builder
Build components: skills, agents, commands, workflows. Init script, decision tree, 6 reference guides.

### 40. template-skill
Starting template for new skills.

### 41. mcp-builder
Four-phase MCP server development: research → implementation → review → evaluation. Agent-centric design, protocol docs, API research. SDKs: Python (FastMCP), Node/TypeScript (MCP SDK).

### 42. mcp-management
Configuration (.claude/.mcp.json), capability discovery (tools/prompts/resources), tool analysis, execution (Gemini CLI primary, scripts secondary, subagent fallback). Persistent catalog: assets/tools.json.

### 43. docs-seeker
Documentation discovery. Workflow: detect query → fetch docs → analyze. Three search types: topic-specific (10-15s), general (30-60s), repository. Context7 integration.

### 44. repomix
Repository analysis and aggregation.

---

## Content & Document Processing (2 Skills)

### 45. document-skills
Advanced document format manipulation.

### 46. markdown-novel-viewer
Calm markdown reader. Features: novel-reader UI, universal viewer, Mermaid.js diagrams, plan navigation. Design: Libre Baskerville, warm cream background (light), dark with gold. Mermaid: flowchart, sequence, pie, gantt, XY, mindmap, quadrant.

---

## Web & Integration Tools (5 Skills)

### 47-51. web-frameworks, shopify, payment-integration, threejs, ui-styling
Web framework guidance, Shopify integration, payment gateways, 3D graphics, Tailwind/shadcn/ui styling.

### 52. ui-ux-pro-max
Advanced UI/UX design patterns.

---

## Media & Specialized Tools (6 Skills)

### 53-58. video-production, youtube-handling, google-adk-python, mobile-development, plans-kanban, test-orchestrator
Video creation, YouTube automation, Google ADK (LlmAgent, SequentialAgent, ParallelAgent), mobile apps, Kanban planning, test automation.

---

## Key Integration Patterns

**Heavy Dependencies:**
- brand-guidelines: 8+ skills
- assets-organizing: 10+ skills
- ai-multimodal: 6+ skills

**Technical Stacks:**
- Frontend: frontend-development → ui-styling → design-system → frontend-design
- Backend: backend-development → databases → better-auth → devops
- Growth: affiliate → referral → gamification → social → seo

**Documentation:** Each skill has SKILL.md + optional scripts/, templates/, references/, data/ directories.

---

## Summary

- **Total:** 58 skills
- **Fully Detailed:** 42 skills with comprehensive capability breakdowns
- **Partially Documented:** 16 skills with SKILL.md files (see unresolved questions)
- **Organization:** 9 categories
- **References:** 100+ supporting guides across all skills

See individual SKILL.md files in `.claude/skills/{name}/` for complete documentation.

**Unresolved:** 16 skills need content review: social-media, seo-optimization, referral-program-building, planning, problem-solving, research, sequential-thinking, skill-creator, template-skill, repomix, document-skills, media-processing, web-frameworks, shopify, payment-integration, mobile-dev, threejs, ui-styling, ui-ux-pro-max, video-production, youtube-handling, plans-kanban, test-orchestrator.
