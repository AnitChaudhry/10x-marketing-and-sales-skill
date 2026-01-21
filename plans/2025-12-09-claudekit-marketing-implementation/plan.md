# ClaudeKit Marketing Implementation Plan

**Created:** 2025-12-09
**Target:** Beta Launch Dec 31, 2025
**Pricing:** $99 standalone | $149 bundled with Engineer

## Executive Summary

Transform ClaudeKit Engineer codebase into marketing-focused toolkit. Core differentiator: Claude Code subagent orchestration for autonomous marketing workflows. Target: indie hackers, small marketing teams, SMB managers.

## Phase Overview

| Phase | Name | Timeline | Status |
|-------|------|----------|--------|
| 1 | [Foundation Cleanup](./phase-01-foundation-cleanup.md) | Dec 9-15 | ✅ Complete (2025-12-09) |
| 2 | [Core Marketing Agents](./phase-02-core-marketing-agents.md) | Dec 16-20 | ✅ Complete (2025-12-09) |
| 3 | [Marketing Skills](./phase-03-marketing-skills.md) | Dec 21-24 | ✅ Complete (2025-12-09) |
| 3c | [SEO & pSEO](./phase-03c-seo-pseo.md) | Dec 21-24 | ✅ Complete (2025-12-11) |
| 4 | [Marketing Commands](./phase-04-marketing-commands.md) | Dec 21-24 | ✅ Complete (2025-12-10) |
| 5 | [MCP Integrations](./phase-05-mcp-integrations.md) | Dec 25-28 | ✅ Complete (2025-12-10) |
| 6 | [Workflows & Hooks](./phase-06-workflows-hooks.md) | Dec 25-28 | ✅ Complete (2025-12-11) |
| 7 | [Documentation & Testing](./phase-07-documentation-testing.md) | Dec 29-30 | Pending |
| 8 | [Beta Launch](./phase-08-beta-launch.md) | Dec 31 | Pending |

## Key Deliverables

### Phase 2 Complete (2025-12-09)
- **13 New Agents**: 7 core (attraction-specialist, email-wizard, lead-qualifier, continuity-specialist, sale-enabler, funnel-architect, upsell-maximizer) + 6 supporting (campaign-manager, content-creator, social-media-manager, community-manager, analytics-analyst, seo-specialist)
- **13 Agent Definition Files**: All created in `.claude/agents/` with system prompts, tool permissions, and MCP integration points
- **Directory Structure**: campaigns/, campaigns/email/, content/sales/, reports/ with all subdirectories created
- **Documentation**: agent-catalog.md fully updated with all agent specs and usage guidelines

### Phase 3 Complete (2025-12-09)
- **9 New Marketing Skills**: seo-optimization, content-marketing, social-media, email-marketing, analytics, campaign-management, brand-guidelines, video-production, ads-management
- **All SKILL.md Files**: Created for each skill (all under 100 lines)
- **Reference Files**: 37 comprehensive reference files with progressive disclosure
- **Scripts**: 4 automation scripts (generate-sitemap.cjs, analyze-keywords.cjs, generate-schema.cjs, validate-email-list.cjs)
- **Documentation**: skill-catalog.md fully updated with all marketing skill specs

### Remaining Phases
- **12+ Commands**: /campaign, /seo, /social, /email, /analyze, /content/blog, /content/video, /persona, /competitor
- **MCP Integrations**: GA4, Google Ads, SendGrid, Discord, Slack, Meta Ads

## Detailed Implementation Plans

### Phase 3 Sub-Plans (Deep Dives)

| Sub-Phase | Focus Area | Est. Hours | Status |
|-----------|------------|------------|--------|
| 3a | [Video Production](./phase-03a-video-production.md) | 32-40 | ✅ Complete |
| 3b | [Content Hub / Assets Management](./phase-03b-content-hub-assets.md) | 28-36 | ✅ Complete (2025-12-11) |
| 3c | [SEO & Programmatic SEO](./phase-03c-seo-pseo.md) | 26-34 | ✅ Complete |

**Note:** These sub-plans provide detailed specifications for the three high-complexity areas identified in the source document.

## Research Reports

### Original Research
- [Claude Code Marketing Analysis](./research/researcher-01-claude-code-marketing.md)
- [Marketing Features Analysis](./research/researcher-02-marketing-features.md)

### Additional Research (Dec 9, 2025)
- [Video Integration Summary](../reports/RESEARCH-SUMMARY-VIDEO-INTEGRATION.md) - Veo 3.1, Gemini, Platform Specs
- [SEO Implementation Summary](../reports/seo-implementation-summary.md) - 22 SEO capabilities + pSEO engine
- [pSEO Deep Dive](../reports/pseo-deep-dive.md) - Complete pSEO architecture
- [Content Hub Specification](../reports/researcher-20251209-content-hub-assets-management.md) - Asset management system

## Source Documents

- [ClaudeKit Marketing Overview](../../docs/overall/ClaudeKit-Marketing-Claude-Code-for-Sales-and-Marketing.md)
- [Subagents for Sales & Marketing](../../docs/overall/Attachments/Applying-Claude-Code-Subagents-to-Modern-Sales-and-Marketing-Frameworks.md)

## Critical Dependencies

1. Gemini API access (Imagen 4, Veo 3.1)
2. MCP server stability (GA4 experimental)
3. OAuth token management strategy
4. Brand guidelines injection system

## Success Metrics

- All engineer-specific code removed
- 7 marketing agents functional
- Core commands operational
- MCP integrations working
- Documentation complete
- Beta users onboarded

## Post-Launch (Jan 2026)

- User feedback integration
- Bug fixes and stability
- Feature expansion based on demand
- Community building
