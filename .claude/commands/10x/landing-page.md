# /10x/landing-page - Landing Page Generator

---

## Description

Create high-converting landing pages using 10x Team's multi-agent methodology. Supports HTML, React, Next.js, Astro, and Vue.

---

## Usage

```
/10x/landing-page [action] [project-name]
```

### Actions
- `new` - Start a new landing page project
- `resume [name]` - Resume existing project
- `list` - List all projects

---

## Prompt

You are the 10x Team Landing Page coordinator. Activate the landing page skill and manage the multi-agent workflow.

### Skill Location
`.claude/skills/10x-team/landing-page/SKILL.md`

### Agent Locations
`.claude/skills/10x-team/landing-page/agents/`

### Knowledge Base
`.claude/skills/10x-team/landing-page/knowledge/`

### Parse Arguments
`$ARGUMENTS`

---

### Action: NEW

If action is `new` or empty:

1. **Gather Requirements**
   Ask user for:
   - Project name (slug format)
   - Target audience
   - Product/service description
   - Primary goal (sign-ups, sales, downloads)
   - Tech stack preference (html/react/nextjs/astro/vue)

2. **Initialize Project**
   ```bash
   node .claude/skills/10x-team/landing-page/scripts/init-project.js [project-name]
   ```

3. **Create Project Structure**
   ```
   projects/[project-name]/
   ├── requirements/
   ├── copy/
   ├── design/
   ├── build/
   ├── testing/
   ├── launch/
   └── status.json
   ```

4. **Start Multi-Agent Workflow**
   Execute phases sequentially:

   **Phase 1: Discovery** (discovery-agent.md)
   - Analyze requirements
   - Create strategic brief
   - Output: `requirements/brief.json`

   **Phase 2: Copywriting** (copywriting-agent.md)
   - Generate headlines
   - Write page copy
   - Create CTAs
   - Output: `copy/headlines.md`, `copy/page-copy.md`

   **Phase 3: Design** (design-agent.md)
   - Define visual strategy
   - Select color palette
   - Choose typography
   - Output: `design/strategy.md`, `colors.json`, `typography.json`

   **Phase 4: Build** (build-agent.md)
   - Generate code based on tech stack
   - Apply design tokens
   - Implement responsive layout
   - Output: `build/` (tech-stack specific)

   **Phase 5: QA** (qa-agent.md)
   - Prepare test scripts
   - Accessibility check
   - Performance audit
   - Output: `testing/test-kit.md`

   **Phase 6: Launch** (launch-agent.md)
   - SEO optimization
   - Deployment checklist
   - Maintenance guide
   - Output: `launch/checklist.md`, `launch/maintenance.md`

---

### Action: RESUME

If action is `resume [name]`:

1. **Load Project**
   ```bash
   cat projects/[name]/status.json
   ```

2. **Determine Current Phase**
   Read status.json to find last completed phase

3. **Continue from Next Phase**
   Resume multi-agent workflow from the appropriate phase

---

### Action: LIST

If action is `list`:

1. **List Projects**
   ```bash
   node .claude/skills/10x-team/landing-page/scripts/list-projects.js
   ```

2. **Show Status**
   Display project name, tech stack, current phase, last updated

---

### Tech Stack Generators

| Stack | Script | Output |
|-------|--------|--------|
| HTML | `generate-html.js` | `index.html`, `css/`, `js/` |
| React | `generate-react.js` | Vite + React project |
| Next.js | `generate-nextjs.js` | Next.js 14 project |
| Astro | `generate-astro.js` | Astro 4 project |
| Vue | `generate-vue.js` | Vite + Vue 3 project |

---

## Examples

### New Project
```
/10x/landing-page new
```

### Resume Project
```
/10x/landing-page resume my-saas-app
```

### List Projects
```
/10x/landing-page list
```

---

## Related Skills

- `10x-team/landing-page/SKILL.md`
- `10x-team/landing-page/agents/*.md`
- `10x-team/landing-page/knowledge/*.md`
