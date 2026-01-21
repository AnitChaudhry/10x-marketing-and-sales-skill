---
name: team-manager
description: |
  Manage team members and their platform credentials for multi-user outreach.
  Each team member can have their own authenticated accounts for LinkedIn, Twitter, Instagram, and Gmail.
  Use this skill when the user wants to add team members, configure platform accounts, or check team status.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - TodoWrite
  - AskUserQuestion
  - mcp__browser-use__list_browser_profiles
---

# Team Manager Skill

Manages team members and their platform credentials for the 100X Outreach System.

## When to Use This Skill

Use this skill when the user:
- Wants to add or remove team members
- Needs to configure platform credentials (LinkedIn, Twitter, Instagram, Gmail)
- Asks about team status or who is set up
- Wants to link Browser-Use profiles to team members
- Needs to check authentication status

## When NOT to Use This Skill

Do NOT use this skill for:
- Sending outreach → use `outreach-manager` or `workflow-engine`
- Finding people → use `discovery-engine`
- Reading emails → use `inbox-reader`

## Capabilities

1. **Add Team Members** - Add new team members with name, email, timezone
2. **Configure Platforms** - Enable/disable platforms per member
3. **Link Browser Profiles** - Connect Browser-Use authenticated profiles
4. **View Status** - Show team overview and auth status
5. **Manage Limits** - Set per-user rate limits

## Commands

### Add a Team Member

```bash
python .claude/scripts/team_manager.py add --name "John Doe" --email "john@example.com" --timezone "America/New_York"
```

### List Team Members

```bash
python .claude/scripts/team_manager.py list
```

### Get Team Status

```bash
python .claude/scripts/team_manager.py status
```

### Configure Platform for Member

```bash
python .claude/scripts/team_manager.py configure --id MEMBER_ID --platform linkedin --enable --handle "@johndoe" --profile-url "linkedin.com/in/johndoe"
```

### Link Browser-Use Profile

After listing browser profiles with `mcp__browser-use__list_browser_profiles`, link a profile:

```bash
python .claude/scripts/team_manager.py configure --id MEMBER_ID --platform linkedin --browser-profile "BROWSER_PROFILE_UUID"
```

### Set Rate Limits

```bash
python .claude/scripts/team_manager.py configure --id MEMBER_ID --platform linkedin --daily-limit 20 --hourly-limit 5
```

### Remove Team Member

```bash
python .claude/scripts/team_manager.py remove --id MEMBER_ID
```

## Browser-Use Integration

To authenticate a team member's platform account:

1. **List Browser Profiles:**
   Use `mcp__browser-use__list_browser_profiles` to see available authenticated profiles.

2. **Match Profile to Member:**
   Identify which browser profile belongs to which team member based on profile name.

3. **Link Profile:**
   ```bash
   python .claude/scripts/team_manager.py configure --id MEMBER_ID --platform linkedin --browser-profile "UUID"
   ```

4. **Verify Authentication:**
   ```bash
   python .claude/scripts/team_manager.py get --id MEMBER_ID
   ```

## Workflow: Setting Up a New Team Member

1. **Create the member:**
   ```
   Add team member "Sarah" with email sarah@company.com
   ```

2. **Configure platforms:**
   ```
   Enable LinkedIn for Sarah with handle @sarahsmith
   Enable Twitter for Sarah with handle @sarah_tweets
   ```

3. **Link authenticated browser profiles:**
   - List browser profiles
   - User selects which profile is Sarah's LinkedIn
   - Link the profile UUID to Sarah's LinkedIn

4. **Set rate limits if needed:**
   ```
   Set Sarah's LinkedIn daily limit to 25 connections
   ```

5. **Verify setup:**
   ```
   Show Sarah's configuration
   ```

## Data Storage

Team data is stored in:
- `credentials/team.json` - Team configuration
- `credentials/profiles/{member_id}/` - Per-member credential files

## Security Notes

- Browser profile IDs are stored but not exported
- Rate limit state is tracked per-user in `credentials/rate_limits_state.json`
- All credentials remain local, never transmitted

## Example Conversations

**User:** "Add my colleague Mike to the team"
**Assistant:**
1. Ask for Mike's email and timezone
2. Run: `team_manager.py add --name "Mike" --email "..." --timezone "..."`
3. Show Mike's profile
4. Ask which platforms to enable

**User:** "Set up Mike's LinkedIn"
**Assistant:**
1. Ask for LinkedIn profile URL/handle
2. Run: `team_manager.py configure --id MIKE_ID --platform linkedin --enable --handle "@mike"`
3. List browser profiles
4. Ask user to identify Mike's LinkedIn browser profile
5. Link the browser profile
6. Confirm setup complete
