# Phase 5: MCP Integrations

## Context Links

- [Plan Overview](./plan.md)
- [Research: Claude Code Marketing](./research/researcher-01-claude-code-marketing.md)
- [Source: ClaudeKit Marketing Overview](../../docs/overall/ClaudeKit-Marketing-Claude-Code-for-Sales-and-Marketing.md)

---

## Overview

| Field | Value |
|-------|-------|
| **Timeline** | Dec 25-28, 2025 |
| **Priority** | High |
| **Implementation Status** | Complete |
| **Review Status** | Complete |
| **Description** | Setup MCP servers for external service integrations |

---

## Key Insights

1. Google GA4 MCP is official (July 2025) - enables natural language analytics
2. SendGrid MCP (Garoth) is mature and feature-rich
3. MCP servers require careful auth token management
4. Start with high-impact integrations, expand based on demand
5. All MCPs should work in read-only mode first before mutations
6. OAuth token refresh strategy critical for long-running workflows

---

## Requirements

### Functional

- Tier 1: GA4, Google Ads, Search Console
- Tier 2: Discord, Slack
- Tier 3: SendGrid, Resend
- Tier 4: YouTube, Meta Ads (future)

### Non-Functional

- OAuth 2.0 token management
- API rate limit handling
- Error recovery patterns
- Credential security

---

## Architecture

### MCP Server Hierarchy

```
.claude/.mcp.json
├── Tier 1: Analytics & Content Intelligence (Critical)
│   ├── reviewwebsite (Content scraping, SEO data, backlinks)
│   ├── google-analytics (GA4)
│   ├── google-ads
│   └── google-search-console
├── Tier 2: Communication (High)
│   ├── discord
│   └── slack
├── Tier 3: Email (High)
│   ├── sendgrid
│   └── resend
└── Tier 4: Future
    ├── youtube
    ├── meta-ads
    ├── tiktok
    ├── stripe
    └── canva
```

---

## MCP Server Specifications

### Tier 1: Analytics, Search & Content Intelligence

#### 1. ReviewWebsite (Content & SEO Intelligence)

**Source:** ClaudeKit Author (mrgoonie)
**URL:** https://github.com/mrgoonie/reviewwebsite-mcp-server

| Attribute | Value |
|-----------|-------|
| Auth | API Key |
| Env Vars | REVIEWWEBSITE_API_KEY |
| Agents | seo-specialist, attraction-specialist, content-creator, researcher |
| Maturity | Stable (from ClaudeKit author) |

**Capabilities:**
- URL-to-Markdown conversion (bypass captcha gates)
- SEO keyword research & difficulty scoring
- Domain traffic analysis
- Backlink data retrieval
- Web scraping & link extraction
- AI-powered content summarization
- Structured data extraction
- Competitor content analysis

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

**Key Use Cases for Marketing:**
- Analyze viral posts (X, Reddit) - converts URLs to markdown
- Competitor SEO analysis
- Content gap research
- Backlink prospecting
- Market intelligence gathering

**Rate Limits:** Per API plan

---

#### 2. Google Analytics 4

**Source:** Official Google (July 2025)
**URL:** https://github.com/googleanalytics/google-analytics-mcp

| Attribute | Value |
|-----------|-------|
| Auth | OAuth 2.0 |
| Env Vars | GA_ACCESS_TOKEN |
| Agents | analytics-analyst, funnel-architect, campaign-manager |
| Maturity | Experimental (official) |

**Capabilities:**
- Natural language data queries
- Property management
- Report generation
- Custom event queries
- Conversion tracking

**Configuration:**
```json
{
  "google-analytics": {
    "command": "npx",
    "args": ["-y", "@google/analytics-mcp"],
    "env": {
      "GA_ACCESS_TOKEN": "${GA_ACCESS_TOKEN}"
    }
  }
}
```

**Rate Limits:** Follow GA4 API quotas

---

#### 2. Google Ads

**Source:** Community
**URL:** https://github.com/cohnen/mcp-google-ads

| Attribute | Value |
|-----------|-------|
| Auth | Google Ads API |
| Env Vars | GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, etc. |
| Agents | campaign-manager, attraction-specialist |
| Maturity | Community |

**Capabilities:**
- Campaign metrics
- Keyword analysis
- Ad performance
- Budget tracking

**Configuration:**
```json
{
  "google-ads": {
    "command": "npx",
    "args": ["-y", "mcp-google-ads"],
    "env": {
      "GOOGLE_ADS_DEVELOPER_TOKEN": "${GOOGLE_ADS_DEVELOPER_TOKEN}",
      "GOOGLE_ADS_CLIENT_ID": "${GOOGLE_ADS_CLIENT_ID}",
      "GOOGLE_ADS_CLIENT_SECRET": "${GOOGLE_ADS_CLIENT_SECRET}",
      "GOOGLE_ADS_REFRESH_TOKEN": "${GOOGLE_ADS_REFRESH_TOKEN}"
    }
  }
}
```

---

#### 3. Google Search Console

**Source:** Community
**URL:** https://github.com/Shin-sibainu/google-search-console-mcp-server

| Attribute | Value |
|-----------|-------|
| Auth | OAuth 2.0 |
| Env Vars | GSC_ACCESS_TOKEN |
| Agents | seo-specialist, analytics-analyst |
| Maturity | Community |

**Capabilities:**
- Search performance data
- URL inspection
- Sitemap status
- Indexing status

**Configuration:**
```json
{
  "google-search-console": {
    "command": "npx",
    "args": ["-y", "google-search-console-mcp"],
    "env": {
      "GSC_ACCESS_TOKEN": "${GSC_ACCESS_TOKEN}"
    }
  }
}
```

---

### Tier 2: Communication

#### 4. Discord

**Source:** Community
**URL:** https://github.com/v-3/discordmcp

| Attribute | Value |
|-----------|-------|
| Auth | Bot Token |
| Env Vars | DISCORD_BOT_TOKEN |
| Agents | community-manager, social-media-manager |
| Maturity | Mature |

**Capabilities:**
- Read/send messages
- Channel management
- Server management
- Member queries
- Reaction handling

**Configuration:**
```json
{
  "discord": {
    "command": "npx",
    "args": ["-y", "discordmcp"],
    "env": {
      "DISCORD_BOT_TOKEN": "${DISCORD_BOT_TOKEN}"
    }
  }
}
```

---

#### 5. Slack

**Source:** Community (korotovsky)
**URL:** https://github.com/korotovsky/slack-mcp-server

| Attribute | Value |
|-----------|-------|
| Auth | User Token |
| Env Vars | SLACK_USER_TOKEN |
| Agents | community-manager, campaign-manager |
| Maturity | Mature |

**Capabilities:**
- Read/post messages
- Channel operations
- User lookups
- File sharing
- Reactions

**Configuration:**
```json
{
  "slack": {
    "command": "npx",
    "args": ["-y", "@korotovsky/slack-mcp-server"],
    "env": {
      "SLACK_USER_TOKEN": "${SLACK_USER_TOKEN}"
    }
  }
}
```

---

### Tier 3: Email

#### 6. SendGrid

**Source:** Community (Garoth)
**URL:** https://github.com/Garoth/sendgrid-mcp

| Attribute | Value |
|-----------|-------|
| Auth | API Key |
| Env Vars | SENDGRID_API_KEY |
| Agents | email-wizard, campaign-manager |
| Maturity | Mature |

**Capabilities:**
- Send emails
- Campaign management
- Contact list management
- Template management
- Statistics retrieval

**Configuration:**
```json
{
  "sendgrid": {
    "command": "npx",
    "args": ["-y", "@garoth/sendgrid-mcp"],
    "env": {
      "SENDGRID_API_KEY": "${SENDGRID_API_KEY}"
    }
  }
}
```

---

#### 7. Resend

**Source:** Community
**URL:** TBD (early-stage)

| Attribute | Value |
|-----------|-------|
| Auth | API Key |
| Env Vars | RESEND_API_KEY |
| Agents | email-wizard |
| Maturity | Early |

**Capabilities:**
- Transactional emails
- Marketing emails
- Domain management

**Configuration:**
```json
{
  "resend": {
    "command": "npx",
    "args": ["-y", "resend-mcp"],
    "env": {
      "RESEND_API_KEY": "${RESEND_API_KEY}"
    }
  }
}
```

---

### Tier 4: Future Integrations

#### 8. YouTube

**URL:** https://github.com/ZubeidHendricks/youtube-mcp-server

**Capabilities:**
- Video management
- Shorts creation
- Analytics
- Caption management

---

#### 9. Meta Ads

**URL:** https://github.com/pipeboard-co/meta-ads-mcp

**Capabilities:**
- Ad campaign management
- Audience targeting
- Performance metrics

---

#### 10. TikTok

**URL:** https://github.com/Seym0n/tiktok-mcp

**Capabilities:**
- Video posting
- Analytics
- Trend data

---

#### 11. Canva

**URL:** https://www.canva.dev/docs/apps/mcp-server/

**Capabilities:**
- Design creation
- Template access
- Asset management

---

## Related Code Files

### Files to CREATE

```
.claude/.mcp.json (main MCP configuration)
.claude/.env.example (environment variables template)
docs/mcp-setup-guide.md (setup documentation)
docs/mcp-troubleshooting.md (common issues)
```

### Files to MODIFY

```
.gitignore (ensure .env excluded)
.claude/settings.json (MCP references)
```

---

## Implementation Steps

### Step 1: Environment Setup
1. Create `.claude/.env.example` with all required env vars
2. Document each variable's purpose
3. Add `.env` to `.gitignore`

### Step 2: Create MCP Configuration
1. Create `.claude/.mcp.json`
2. Add Tier 1 servers (GA4, Google Ads, Search Console)
3. Add Tier 2 servers (Discord, Slack)
4. Add Tier 3 servers (SendGrid, Resend)

### Step 3: Install MCP Servers
For each server:
1. Test npx installation
2. Verify authentication
3. Test basic operations
4. Document any issues

### Step 4: Create Setup Documentation
1. Step-by-step OAuth setup for Google services
2. Bot token setup for Discord
3. API key generation for SendGrid
4. Troubleshooting guide

### Step 5: Agent Integration
1. Update agent files with MCP access
2. Test agent-MCP communication
3. Error handling for MCP failures

### Step 6: Rate Limit Handling
1. Document API limits per service
2. Implement caching where appropriate
3. Add retry logic

---

## MCP Configuration Template

```json
{
  "mcpServers": {
    "google-analytics": {
      "command": "npx",
      "args": ["-y", "@google/analytics-mcp"],
      "env": {
        "GA_ACCESS_TOKEN": "${GA_ACCESS_TOKEN}"
      }
    },
    "google-ads": {
      "command": "npx",
      "args": ["-y", "mcp-google-ads"],
      "env": {
        "GOOGLE_ADS_DEVELOPER_TOKEN": "${GOOGLE_ADS_DEVELOPER_TOKEN}",
        "GOOGLE_ADS_CLIENT_ID": "${GOOGLE_ADS_CLIENT_ID}",
        "GOOGLE_ADS_CLIENT_SECRET": "${GOOGLE_ADS_CLIENT_SECRET}",
        "GOOGLE_ADS_REFRESH_TOKEN": "${GOOGLE_ADS_REFRESH_TOKEN}"
      }
    },
    "google-search-console": {
      "command": "npx",
      "args": ["-y", "google-search-console-mcp"],
      "env": {
        "GSC_ACCESS_TOKEN": "${GSC_ACCESS_TOKEN}"
      }
    },
    "discord": {
      "command": "npx",
      "args": ["-y", "discordmcp"],
      "env": {
        "DISCORD_BOT_TOKEN": "${DISCORD_BOT_TOKEN}"
      }
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "@korotovsky/slack-mcp-server"],
      "env": {
        "SLACK_USER_TOKEN": "${SLACK_USER_TOKEN}"
      }
    },
    "sendgrid": {
      "command": "npx",
      "args": ["-y", "@garoth/sendgrid-mcp"],
      "env": {
        "SENDGRID_API_KEY": "${SENDGRID_API_KEY}"
      }
    }
  }
}
```

---

## Todo List

- [x] Create .claude/.env.example
- [x] Create .claude/.mcp.json
- [x] Setup GA4 MCP
- [x] Setup Google Ads MCP
- [x] Setup Search Console MCP
- [x] Setup Discord MCP
- [x] Setup Slack MCP
- [x] Setup SendGrid MCP
- [x] Test all MCP connections
- [x] Create docs/mcp-setup-guide.md
- [x] Create docs/mcp-troubleshooting.md
- [x] Update agents with MCP access
- [x] Document rate limits

---

## Success Criteria

1. All Tier 1-3 MCPs configured
2. Authentication working for each
3. Basic operations tested
4. Error handling implemented
5. Documentation complete
6. Agents connected to MCPs
7. Rate limits documented

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| OAuth token expiry | High | High | Token refresh automation |
| API rate limits | Medium | Medium | Caching, request batching |
| MCP server instability | Medium | High | Fallback to manual mode |
| Breaking API changes | Low | High | Pin MCP versions |
| Credential exposure | Low | Critical | Env vars, .gitignore |

---

## Security Considerations

- Store all credentials in .env (never commit)
- Use minimal permission scopes
- Rotate tokens quarterly
- Audit MCP server code before use
- Read-only mode first, mutations with approval
- Log all MCP operations
- PII redaction in reports

---

## Next Steps

After Phase 5 completion:
1. Proceed to Phase 6: Workflows & Hooks
2. Create marketing workflows using MCPs
3. Build approval chains
4. Test end-to-end pipelines

---

## Unresolved Questions

1. Does GA4 MCP support custom dimensions/metrics?
2. Token refresh strategy for OAuth services?
3. Multi-account support (multiple GA properties)?
4. MCP caching layer needed?
5. How to handle MCP server updates?
6. Monitoring/alerting for MCP failures?
