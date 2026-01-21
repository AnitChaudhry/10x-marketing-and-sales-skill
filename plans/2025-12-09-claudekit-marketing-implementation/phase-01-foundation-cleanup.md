# Phase 1: Foundation Cleanup

## Context Links

- [Plan Overview](./plan.md)
- [Research: Claude Code Marketing](./research/researcher-01-claude-code-marketing.md)
- [Source: ClaudeKit Marketing Overview](../../docs/overall/ClaudeKit-Marketing-Claude-Code-for-Sales-and-Marketing.md)

---

## Overview

| Field | Value |
|-------|-------|
| **Timeline** | Dec 9-15, 2025 |
| **Priority** | Critical |
| **Implementation Status** | Completed |
| **Review Status** | Approved |
| **Phase Status** | DONE (2025-12-09) |
| **Description** | Remove engineer-specific components, restructure for marketing focus |

---

## Key Insights

1. Current codebase contains 17 agents, 31 skills, 64+ commands from ClaudeKit Engineer
2. Many components reusable (copywriter, brainstormer, researcher, ui-ux-designer)
3. Engineer-specific components must be removed: fullstack-developer, tester, database-admin
4. Directory structure needs reorganization for marketing workflows
5. Documentation must be updated to reflect marketing focus

---

## Requirements

### Functional

- Remove all engineer-specific agents, skills, commands
- Retain marketing-relevant components
- Update CLAUDE.md for marketing context
- Clean up git history references to engineer toolkit
- Update package.json metadata

### Non-Functional

- Maintain existing file structure conventions
- Preserve working hooks system
- Keep MCP configuration framework intact
- Ensure no broken references after cleanup

---

## Architecture

### Component Retention Matrix

**Agents to KEEP (12):**
- copywriter, brainstormer, researcher, ui-ux-designer
- planner, project-manager, docs-manager, git-manager
- mcp-manager, scout, scout-external, journal-writer

**Agents to MODIFY (2):**
- code-reviewer -> content-reviewer
- debugger -> campaign-debugger

**Agents to REMOVE (3):**
- fullstack-developer
- tester
- database-admin

**Skills to KEEP (16):**
- ai-multimodal, chrome-devtools, media-processing
- ui-styling, ui-ux-pro-max, frontend-design, frontend-design-pro
- research, planning, problem-solving, sequential-thinking
- mcp-management, repomix, skill-creator, docs-seeker, payment-integration

**Skills to REMOVE (13):**
- backend-development, frontend-development, mobile-development
- databases, devops, web-frameworks, debugging, code-review
- better-auth, threejs, shopify, google-adk-python, mcp-builder

**Commands to KEEP:**
- /plan, /brainstorm, /scout, /journal, /watzup, /ask
- /content/*, /design/*, /docs/*, /git/*

**Commands to REMOVE:**
- /cook*, /code*, /fix*, /test, /debug, /bootstrap*, /review/codebase

**Hooks to KEEP:**
- session-init.cjs, subagent-init.cjs, dev-rules-reminder.cjs

**Hooks to REMOVE:**
- scout-block.cjs (engineer-specific)

---

## Related Code Files

### Files to DELETE

```
.claude/agents/fullstack-developer.md
.claude/agents/tester.md
.claude/agents/database-admin.md
.claude/skills/backend-development/
.claude/skills/frontend-development/
.claude/skills/mobile-development/
.claude/skills/databases/
.claude/skills/devops/
.claude/skills/web-frameworks/
.claude/skills/debugging/
.claude/skills/code-review/
.claude/skills/better-auth/
.claude/skills/threejs/
.claude/skills/shopify/
.claude/skills/google-adk-python/
.claude/skills/mcp-builder/
.claude/commands/cook.md
.claude/commands/cook/
.claude/commands/code.md
.claude/commands/code/
.claude/commands/fix/test.md
.claude/commands/test.md
.claude/commands/debug.md
.claude/commands/bootstrap.md
.claude/commands/bootstrap/
.claude/commands/review/codebase.md
.claude/hooks/scout-block.cjs
.claude/hooks/scout-block/
```

### Files to MODIFY

```
.claude/agents/code-reviewer.md -> content-reviewer.md (rename + update content)
.claude/agents/debugger.md -> campaign-debugger.md (rename + update content)
CLAUDE.md (update for marketing context)
README.md (update project description)
package.json (update name, description, keywords)
.claude/settings.json (update if needed)
docs/project-overview-pdr.md (update)
docs/codebase-summary.md (update)
docs/system-architecture.md (update)
```

### Files to CREATE

```
docs/marketing-overview.md
docs/agent-catalog.md
docs/skill-catalog.md
docs/command-catalog.md
```

---

## Implementation Steps

### Step 1: Backup Current State
1. Create git branch `cleanup/remove-engineer-components`
2. Tag current state for reference

### Step 2: Remove Engineer-Specific Agents
1. Delete `.claude/agents/fullstack-developer.md`
2. Delete `.claude/agents/tester.md`
3. Delete `.claude/agents/database-admin.md`
4. Verify no broken agent references

### Step 3: Remove Engineer-Specific Skills
1. Delete skill directories listed above (13 total)
2. Update any skill references in remaining files
3. Verify skill catalog integrity

### Step 4: Remove Engineer-Specific Commands
1. Delete command files listed above
2. Remove command directory trees (/cook/, /code/, /bootstrap/)
3. Update command index if exists

### Step 5: Remove Engineer-Specific Hooks
1. Delete `.claude/hooks/scout-block.cjs`
2. Delete `.claude/hooks/scout-block/` directory
3. Verify hooks still chain correctly

### Step 6: Rename & Update Modified Agents
1. Rename `code-reviewer.md` to `content-reviewer.md`
   - Update system prompt for content review focus
   - Change tools from code analysis to content analysis
2. Rename `debugger.md` to `campaign-debugger.md`
   - Update for campaign troubleshooting context
   - Focus on analytics and campaign performance

### Step 7: Update Core Documentation
1. Update CLAUDE.md:
   - Change role description to marketing focus
   - Update workflow references
   - Remove engineer-specific instructions
2. Update README.md:
   - New project description
   - Marketing feature highlights
   - Updated installation instructions
3. Update package.json:
   - name: "claudekit-marketing"
   - description: "Claude Code toolkit for sales and marketing automation"
   - keywords: ["marketing", "ai", "automation", "claude", "sales"]

### Step 8: Create New Documentation Structure
1. Create `docs/marketing-overview.md`
2. Create `docs/agent-catalog.md`
3. Create `docs/skill-catalog.md`
4. Create `docs/command-catalog.md`

### Step 9: Clean Up References
1. Search for broken file references
2. Update any hardcoded paths
3. Verify all imports/requires work

### Step 10: Verify & Test
1. Run Claude Code to verify no errors
2. Test remaining agents function
3. Test remaining commands work
4. Verify hooks execute correctly

---

## Todo List

- [x] Create cleanup branch
- [x] Delete engineer-specific agents (3 files)
- [x] Delete engineer-specific skills (13 directories)
- [x] Delete engineer-specific commands
- [x] Delete engineer-specific hooks
- [x] Rename code-reviewer to content-reviewer
- [x] Rename debugger to campaign-debugger
- [x] Update CLAUDE.md
- [x] Update README.md
- [x] Update package.json
- [x] Create docs/marketing-overview.md
- [x] Create docs/agent-catalog.md
- [x] Create docs/skill-catalog.md
- [x] Create docs/command-catalog.md
- [x] Search and fix broken references
- [x] Verify all components work
- [x] Commit and push changes

---

## Success Criteria

1. All engineer-specific components removed
2. No broken file references
3. Remaining agents functional
4. Remaining commands operational
5. Hooks execute without errors
6. Documentation reflects marketing focus
7. Package metadata updated
8. Clean git history on cleanup branch

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Broken references after deletion | Medium | High | Thorough grep search before commit |
| Hooks chain broken | Low | High | Test hook execution post-cleanup |
| Lost useful functionality | Low | Medium | Create backup tag before cleanup |
| Documentation inconsistency | Medium | Low | Review all docs after changes |

---

## Security Considerations

- Ensure no credentials in deleted files
- Verify .gitignore still covers sensitive files
- Check for any exposed API keys in removed code
- Maintain security patterns in retained code

---

## Next Steps

After Phase 1 completion:
1. Proceed to Phase 2: Core Marketing Agents
2. Begin agent creation with attraction-specialist
3. Set up agent testing framework
4. Document agent communication patterns

---

## Unresolved Questions

1. Should we archive removed components separately for reference?
2. Any plans to port engineer skills back as optional add-ons?
3. Keep /fix commands but rename for marketing context (campaign fixes)?
