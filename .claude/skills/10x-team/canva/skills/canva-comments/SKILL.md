---
name: canva-comments
description: |
  Collaboration and comments skill for Canva designs. Use this skill when user wants
  to add comments, feedback, or collaborate on designs. Handles comment threads,
  replies, and task assignments. Preview API feature.
---

# Canva Comments & Collaboration

Add comments, feedback, and collaborate on Canva designs.

---

## Capabilities

1. **Create Comments** - Add comment threads to designs
2. **Reply to Comments** - Respond to existing threads
3. **List Replies** - View conversation history
4. **Assign Tasks** - Assign comments to team members
5. **Attach to Elements** - Pin comments to specific pages/elements

---

## Available Scripts

### Create Comment
```bash
# Basic comment
.venv\Scripts\python.exe scripts/create_comment.py "DAFxxxxxxxxxx" "Great design! Let's adjust the colors."

# Attach to specific page
.venv\Scripts\python.exe scripts/create_comment.py "DAFxxxxxxxxxx" "Fix this slide" --page "page_123"

# Attach to element
.venv\Scripts\python.exe scripts/create_comment.py "DAFxxxxxxxxxx" "Update this text" --element "element_456"

# Assign to user
.venv\Scripts\python.exe scripts/create_comment.py "DAFxxxxxxxxxx" "Please review" --assignee "UAFuser123"

# JSON output
.venv\Scripts\python.exe scripts/create_comment.py "DAFxxxxxxxxxx" "Feedback" --json
```

### Reply to Comment
```bash
# Add reply
.venv\Scripts\python.exe scripts/reply_to_comment.py "DAFxxxxxxxxxx" "thread_abc" "I agree, let me update that."

# JSON output
.venv\Scripts\python.exe scripts/reply_to_comment.py "DAFxxxxxxxxxx" "thread_abc" "Done!" --json
```

### List Replies
```bash
# List replies in a thread
.venv\Scripts\python.exe scripts/list_comments.py "DAFxxxxxxxxxx" --thread "thread_abc"

# With limit
.venv\Scripts\python.exe scripts/list_comments.py "DAFxxxxxxxxxx" --thread "thread_abc" --limit 20

# JSON output
.venv\Scripts\python.exe scripts/list_comments.py "DAFxxxxxxxxxx" --thread "thread_abc" --json
```

---

## Comment Structure

### Comment Thread
```json
{
  "id": "thread_abc123",
  "message": "Main comment text",
  "author": {
    "user_id": "UAFxxx",
    "display_name": "John Smith"
  },
  "created_at": "2024-01-15T10:30:00Z",
  "attached_to": {
    "page_id": "page_123",
    "element_id": "element_456"
  },
  "assignee": {
    "user_id": "UAFyyy"
  }
}
```

### Reply
```json
{
  "id": "reply_xyz789",
  "message": "Reply text",
  "author": {
    "user_id": "UAFyyy",
    "display_name": "Jane Doe"
  },
  "created_at": "2024-01-15T11:00:00Z"
}
```

---

## Use Cases

### Design Review Workflow
```bash
# 1. Reviewer adds feedback
.venv\Scripts\python.exe scripts/create_comment.py "DAFxxxxxxxxxx" \
    "The headline needs to be more prominent. Consider increasing font size."

# 2. Designer responds
.venv\Scripts\python.exe scripts/reply_to_comment.py "DAFxxxxxxxxxx" "thread_123" \
    "Good point! I've increased it to 48pt. What do you think?"

# 3. Reviewer confirms
.venv\Scripts\python.exe scripts/reply_to_comment.py "DAFxxxxxxxxxx" "thread_123" \
    "Perfect, looks great now!"
```

### Task Assignment
```bash
# Assign task to team member
.venv\Scripts\python.exe scripts/create_comment.py "DAFxxxxxxxxxx" \
    "Please add the updated logo to slide 3" \
    --page "page_slide3" \
    --assignee "UAFteammember"
```

### Element-Specific Feedback
```bash
# Comment on specific element
.venv\Scripts\python.exe scripts/create_comment.py "DAFxxxxxxxxxx" \
    "This image needs to be replaced with the new product photo" \
    --element "element_image1"
```

---

## 3-Mode Workflow

### MODE 1: PLAN
1. Identify the design to comment on
2. Determine if comment is general or attached to element
3. Check if assignment is needed

### MODE 2: CLARIFY
Ask user:
- What feedback to provide?
- Should it be attached to a specific element?
- Should it be assigned to someone?

### MODE 3: IMPLEMENT
```bash
# Create the comment
.venv\Scripts\python.exe scripts/create_comment.py "DAFxxxxxxxxxx" "Your feedback here"

# Output:
# Comment Created Successfully!
# ==================================================
#   Thread ID: thread_abc123
#   Design:    DAFxxxxxxxxxx
#   Message:   Your feedback here
#   Created:   2024-01-15T10:30:00Z
```

---

## API Notes

### Preview API
Comments API is currently in Preview status:
- Functionality may change
- Some features may have limitations
- Enterprise customers have full access

### Thread IDs
Thread IDs are returned when:
- Creating a comment (returns new thread ID)
- Design metadata may include comment info

---

## Error Handling

### Design Not Found
```
Error: 404 - Design does not exist
```

### Thread Not Found
```
Error: 404 - Comment thread does not exist
```

### Permission Denied
```
Error: 403 - You don't have permission to comment on this design
```

### Missing Scopes
Requires `comment:write` scope for creating comments and `comment:read` for viewing.

---

## Integration with Review Workflows

### Automated Review Comments
```python
# Example: Add automated review feedback
comments = [
    "Please check spelling on slide 1",
    "Logo placement needs adjustment",
    "Color scheme approved"
]

for comment in comments:
    # Create comment via script
    pass
```

### Collect Feedback
```bash
# Get all replies to review
.venv\Scripts\python.exe scripts/list_comments.py "DAFxxxxxxxxxx" --thread "thread_review" --json
```
