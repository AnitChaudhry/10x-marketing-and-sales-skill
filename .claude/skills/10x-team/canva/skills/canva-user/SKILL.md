---
name: canva-user
description: |
  User management skill for Canva account operations. Use this skill when user wants
  to check their account info, profile details, API capabilities, or authentication status.
  Handles user identity, team info, and available features.
---

# Canva User Management

Manage user account information and capabilities.

---

## Capabilities

1. **Get User Info** - User ID and team information
2. **Get Profile** - Display name and profile details
3. **Check Capabilities** - Available API features
4. **Verify Authentication** - Check token validity

---

## Available Scripts

### Get User Information
```bash
# Basic user info
.venv\Scripts\python.exe scripts/get_user.py

# Include profile details
.venv\Scripts\python.exe scripts/get_user.py --profile

# Include API capabilities
.venv\Scripts\python.exe scripts/get_user.py --capabilities

# Get everything
.venv\Scripts\python.exe scripts/get_user.py --all

# JSON output
.venv\Scripts\python.exe scripts/get_user.py --all --json
```

### Check Authentication
```bash
# Verify auth token is working
.venv\Scripts\python.exe scripts/auth_check.py
```

---

## User Information Returned

### Basic Info
- `user_id` - Unique user identifier
- `team_id` - Team the user belongs to

### Profile
- `display_name` - User's display name

### Capabilities
List of available API features:
- `design:content:read`
- `design:content:write`
- `design:meta:read`
- `asset:read`
- `asset:write`
- `folder:read`
- `folder:write`
- `profile:read`
- `comment:read`
- `comment:write`
- `brandtemplate:meta:read`
- `brandtemplate:content:read`

---

## Example Workflows

### Check Account Status
```bash
# 1. Get all user information
.venv\Scripts\python.exe scripts/get_user.py --all

# Output:
# Canva User Information
# ==================================================
#   User ID:  UAF...
#   Team ID:  TAF...
#
# Profile:
#   Display Name: John Smith
#
# API Capabilities (8):
#   - design:content:read
#   - design:content:write
#   - asset:read
#   ...
```

### Verify Before Operations
```bash
# Before performing operations, check capabilities
.venv\Scripts\python.exe scripts/get_user.py --capabilities --json

# Check if user has required scopes for intended operations
```

---

## Error Handling

### Invalid Token
```
Error: 401 Unauthorized
```
**Solution**: Re-run OAuth flow with `scripts/oauth_flow.py`

### Missing Scopes
If certain capabilities are missing, the user needs to re-authorize with additional scopes.

---

## Integration

This skill provides identity verification for other skills:
- Before creating designs, check `design:content:write`
- Before uploading assets, check `asset:write`
- Before folder operations, check `folder:write`
