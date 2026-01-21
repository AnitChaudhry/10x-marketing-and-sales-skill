#!/usr/bin/env python3
"""
LinkedIn Adapter for 100X Outreach System

Provides LinkedIn automation actions using Browser-Use MCP.
All actions are executed through authenticated browser profiles.

This adapter generates Browser-Use task descriptions that Claude
will execute using the mcp__browser-use__browser_task tool.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

# Import local modules
import sys
sys.path.insert(0, str(Path(__file__).parent))

try:
    from rate_limiter import RateLimiter
    from template_loader import TemplateLoader
    from team_manager import TeamManager
except ImportError:
    RateLimiter = None
    TemplateLoader = None
    TeamManager = None


@dataclass
class LinkedInAction:
    """A LinkedIn action to be executed"""
    action_type: str
    target_url: str
    target_name: str
    message: Optional[str] = None
    template_path: Optional[str] = None
    template_vars: Optional[Dict] = None
    browser_task: Optional[str] = None  # Generated browser task description
    max_steps: int = 10


class LinkedInAdapter:
    """
    LinkedIn automation adapter using Browser-Use MCP.

    Supported Actions:
    - view_profile: Visit a LinkedIn profile
    - like_post: Like a post on LinkedIn
    - comment: Comment on a post
    - connect: Send a connection request
    - message: Send a direct message
    - follow: Follow a person/company
    """

    ACTIONS = {
        'view_profile': {
            'description': 'View a LinkedIn profile',
            'rate_limit_key': 'profile_views_per_day',
            'max_steps': 5
        },
        'like_post': {
            'description': 'Like a LinkedIn post',
            'rate_limit_key': 'likes_per_day',
            'max_steps': 8
        },
        'comment': {
            'description': 'Comment on a LinkedIn post',
            'rate_limit_key': 'comments_per_day',
            'max_steps': 10
        },
        'connect': {
            'description': 'Send a connection request',
            'rate_limit_key': 'connections_per_day',
            'max_steps': 12
        },
        'message': {
            'description': 'Send a direct message',
            'rate_limit_key': 'messages_per_day',
            'max_steps': 12
        },
        'follow': {
            'description': 'Follow a person or company',
            'rate_limit_key': 'connections_per_day',
            'max_steps': 8
        }
    }

    def __init__(self, data_dir: str = "."):
        self.data_dir = Path(data_dir)
        self.rate_limiter = RateLimiter() if RateLimiter else None
        self.template_loader = TemplateLoader() if TemplateLoader else None
        self.team_manager = TeamManager() if TeamManager else None

    def generate_task(self, action: LinkedInAction, user_id: str = "default") -> Dict:
        """
        Generate a Browser-Use task for the given action.

        Returns a dict with:
        - task: The browser task description
        - max_steps: Recommended max steps
        - profile_id: Browser profile to use (if available)
        - can_proceed: Whether rate limits allow this action
        - wait_seconds: How long to wait if rate limited
        """
        # Check rate limits
        can_proceed = True
        wait_seconds = 0

        if self.rate_limiter:
            can_proceed, reason, wait_seconds = self.rate_limiter.can_proceed(
                user_id, 'linkedin', action.action_type
            )
            if not can_proceed:
                return {
                    'task': None,
                    'can_proceed': False,
                    'reason': reason,
                    'wait_seconds': wait_seconds
                }

        # Get browser profile if team manager available
        profile_id = None
        if self.team_manager:
            profile_id = self.team_manager.get_browser_profile(user_id, 'linkedin')

        # Render message template if provided
        message = action.message
        if action.template_path and self.template_loader:
            template_vars = action.template_vars or {}
            template_vars['first_name'] = action.target_name.split()[0] if action.target_name else ''
            template_vars['name'] = action.target_name
            result = self.template_loader.render_by_path(action.template_path, template_vars)
            message = result.get('content', message)

        # Generate browser task based on action type
        task = self._generate_browser_task(action, message)

        return {
            'task': task,
            'max_steps': action.max_steps or self.ACTIONS.get(action.action_type, {}).get('max_steps', 10),
            'profile_id': profile_id,
            'can_proceed': True,
            'message': message
        }

    def _generate_browser_task(self, action: LinkedInAction, message: str = None) -> str:
        """Generate the browser task description for Browser-Use MCP"""

        if action.action_type == 'view_profile':
            return f"""Go to LinkedIn profile: {action.target_url}

Steps:
1. Navigate to {action.target_url}
2. Wait for the profile page to fully load
3. Scroll down slightly to view the profile summary
4. Take note of their current role and company

Success: The profile page is displayed with the person's information visible."""

        elif action.action_type == 'like_post':
            return f"""Like a recent post from {action.target_name} on LinkedIn.

Steps:
1. Go to {action.target_url}
2. Scroll down to find their recent posts/activity section
3. Find a recent post (within the last week)
4. Click the "Like" button on the post
5. Confirm the like was registered (button changes state)

Success: A post has been liked (the Like button shows as active/filled)."""

        elif action.action_type == 'comment':
            comment_text = message or "Great insights! Thanks for sharing."
            return f"""Comment on a post from {action.target_name} on LinkedIn.

Comment text: "{comment_text}"

Steps:
1. Go to {action.target_url}
2. Find their recent posts/activity section
3. Click on a recent post to expand it
4. Click the "Comment" button
5. Type the comment: "{comment_text}"
6. Click "Post" to submit the comment

Success: The comment is posted and visible under the post."""

        elif action.action_type == 'connect':
            note = message or f"Hi {action.target_name.split()[0] if action.target_name else 'there'}, I'd love to connect!"
            # Truncate to 300 chars for connection notes
            if len(note) > 300:
                note = note[:297] + "..."

            return f"""Send a LinkedIn connection request to {action.target_name}.

Profile URL: {action.target_url}
Connection note: "{note}"

Steps:
1. Navigate to {action.target_url}
2. Wait for the profile to load completely
3. Look for the "Connect" button (may be under "More" dropdown)
4. Click "Connect"
5. If prompted, click "Add a note"
6. Enter the connection note: "{note}"
7. Click "Send" or "Send invitation"

Success: Connection request sent (confirmation message appears or button changes to "Pending")."""

        elif action.action_type == 'message':
            msg = message or f"Hi {action.target_name.split()[0] if action.target_name else 'there'}, I wanted to reach out..."
            return f"""Send a LinkedIn direct message to {action.target_name}.

Profile URL: {action.target_url}
Message: "{msg}"

Steps:
1. Navigate to {action.target_url}
2. Click the "Message" button on their profile
3. Wait for the message dialog to open
4. Type the message: "{msg}"
5. Click "Send"

Success: Message sent (appears in the chat thread)."""

        elif action.action_type == 'follow':
            return f"""Follow {action.target_name} on LinkedIn.

Profile URL: {action.target_url}

Steps:
1. Navigate to {action.target_url}
2. Look for the "Follow" button (may be under "More" dropdown)
3. Click "Follow"
4. Confirm the follow was successful

Success: Now following (button changes to "Following" or similar)."""

        else:
            return f"Unknown action type: {action.action_type}"

    def record_action(self, user_id: str, action: LinkedInAction, success: bool, details: str = None):
        """Record an action for rate limiting"""
        if self.rate_limiter:
            self.rate_limiter.record_action(
                user_id,
                'linkedin',
                action.action_type,
                action.target_url,
                success,
                details
            )

    def get_remaining_limits(self, user_id: str = "default") -> Dict[str, int]:
        """Get remaining action limits for today"""
        if self.rate_limiter:
            return self.rate_limiter.get_remaining_limits(user_id, 'linkedin')
        return {}

    def calculate_delay(self, action_type: str) -> int:
        """Calculate delay before next action"""
        if self.rate_limiter:
            return self.rate_limiter.calculate_delay('linkedin', action_type)
        return 120  # Default 2 minutes


def create_view_profile_action(profile_url: str, name: str = "") -> LinkedInAction:
    """Helper to create a view profile action"""
    return LinkedInAction(
        action_type='view_profile',
        target_url=profile_url,
        target_name=name,
        max_steps=5
    )


def create_connect_action(profile_url: str, name: str, template_path: str = None,
                          template_vars: Dict = None, message: str = None) -> LinkedInAction:
    """Helper to create a connection request action"""
    return LinkedInAction(
        action_type='connect',
        target_url=profile_url,
        target_name=name,
        message=message,
        template_path=template_path or 'linkedin/connection-requests/cold_outreach',
        template_vars=template_vars,
        max_steps=12
    )


def create_message_action(profile_url: str, name: str, template_path: str = None,
                          template_vars: Dict = None, message: str = None) -> LinkedInAction:
    """Helper to create a message action"""
    return LinkedInAction(
        action_type='message',
        target_url=profile_url,
        target_name=name,
        message=message,
        template_path=template_path or 'linkedin/messages/intro_after_connect',
        template_vars=template_vars,
        max_steps=12
    )


def create_like_action(profile_url: str, name: str = "") -> LinkedInAction:
    """Helper to create a like post action"""
    return LinkedInAction(
        action_type='like_post',
        target_url=profile_url,
        target_name=name,
        max_steps=8
    )


def create_comment_action(profile_url: str, name: str, comment: str = None,
                          template_path: str = None, template_vars: Dict = None) -> LinkedInAction:
    """Helper to create a comment action"""
    return LinkedInAction(
        action_type='comment',
        target_url=profile_url,
        target_name=name,
        message=comment,
        template_path=template_path,
        template_vars=template_vars,
        max_steps=10
    )


def main():
    """CLI interface for LinkedIn adapter"""
    import argparse

    parser = argparse.ArgumentParser(description="LinkedIn Adapter CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Generate task
    task_parser = subparsers.add_parser('task', help='Generate browser task')
    task_parser.add_argument('--action', required=True,
                             choices=['view_profile', 'like_post', 'comment', 'connect', 'message', 'follow'])
    task_parser.add_argument('--url', required=True, help='Target LinkedIn URL')
    task_parser.add_argument('--name', default='', help='Target name')
    task_parser.add_argument('--message', help='Message or comment text')
    task_parser.add_argument('--template', help='Template path')
    task_parser.add_argument('--user', default='default', help='User ID')

    # Check limits
    limits_parser = subparsers.add_parser('limits', help='Check rate limits')
    limits_parser.add_argument('--user', default='default', help='User ID')

    # Calculate delay
    delay_parser = subparsers.add_parser('delay', help='Calculate delay')
    delay_parser.add_argument('--action', required=True, help='Action type')

    # List actions
    subparsers.add_parser('actions', help='List available actions')

    args = parser.parse_args()

    adapter = LinkedInAdapter()

    if args.command == 'task':
        action = LinkedInAction(
            action_type=args.action,
            target_url=args.url,
            target_name=args.name,
            message=args.message,
            template_path=args.template
        )
        result = adapter.generate_task(action, args.user)
        print(json.dumps(result, indent=2))

    elif args.command == 'limits':
        limits = adapter.get_remaining_limits(args.user)
        print("Remaining LinkedIn limits for today:")
        for action, remaining in limits.items():
            print(f"  {action}: {remaining}")

    elif args.command == 'delay':
        delay = adapter.calculate_delay(args.action)
        print(f"Recommended delay for {args.action}: {delay} seconds")

    elif args.command == 'actions':
        print("Available LinkedIn Actions:")
        for action, info in LinkedInAdapter.ACTIONS.items():
            print(f"  {action}: {info['description']}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
