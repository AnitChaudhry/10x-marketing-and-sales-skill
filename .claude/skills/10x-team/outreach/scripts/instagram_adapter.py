#!/usr/bin/env python3
"""
Instagram Adapter for 100X Outreach System

Provides Instagram automation actions using Browser-Use MCP.
Claude uses this adapter to generate Browser-Use tasks with rendered templates.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

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
class InstagramAction:
    """An Instagram action to be executed via Browser-Use"""
    action_type: str
    target_handle: str  # @username
    target_name: str
    target_url: str = ""
    message: Optional[str] = None
    template_path: Optional[str] = None
    template_vars: Optional[Dict] = None
    post_url: Optional[str] = None  # For likes/comments
    max_steps: int = 10


class InstagramAdapter:
    """
    Instagram automation adapter for Browser-Use MCP.

    Supported Actions:
    - follow: Follow a user
    - like_post: Like a post
    - comment: Comment on a post
    - dm: Send a direct message
    - story_reply: Reply to a story
    """

    ACTIONS = {
        'follow': {
            'description': 'Follow an Instagram user',
            'rate_limit_key': 'follows_per_day',
            'max_steps': 6
        },
        'like_post': {
            'description': 'Like an Instagram post',
            'rate_limit_key': 'likes_per_day',
            'max_steps': 6
        },
        'comment': {
            'description': 'Comment on a post',
            'rate_limit_key': 'comments_per_day',
            'max_steps': 8
        },
        'dm': {
            'description': 'Send a direct message',
            'rate_limit_key': 'dms_per_day',
            'max_steps': 10
        },
        'story_reply': {
            'description': 'Reply to a story',
            'rate_limit_key': 'dms_per_day',
            'max_steps': 10
        }
    }

    def __init__(self, data_dir: str = "."):
        self.data_dir = Path(data_dir)
        self.rate_limiter = RateLimiter() if RateLimiter else None
        self.template_loader = TemplateLoader() if TemplateLoader else None
        self.team_manager = TeamManager() if TeamManager else None

    def generate_task(self, action: InstagramAction, user_id: str = "default") -> Dict:
        """Generate a Browser-Use task for the given Instagram action."""

        # Check rate limits
        if self.rate_limiter:
            can_proceed, reason, wait_seconds = self.rate_limiter.can_proceed(
                user_id, 'instagram', action.action_type
            )
            if not can_proceed:
                return {
                    'task': None,
                    'can_proceed': False,
                    'reason': reason,
                    'wait_seconds': wait_seconds
                }

        # Get browser profile
        profile_id = None
        if self.team_manager:
            profile_id = self.team_manager.get_browser_profile(user_id, 'instagram')

        # Render message template
        message = action.message
        if action.template_path and self.template_loader:
            template_vars = action.template_vars or {}
            template_vars['first_name'] = action.target_name.split()[0] if action.target_name else ''
            template_vars['name'] = action.target_name
            template_vars['handle'] = action.target_handle
            result = self.template_loader.render_by_path(action.template_path, template_vars)
            message = result.get('content', message)

        # Generate browser task
        task = self._generate_browser_task(action, message)

        return {
            'task': task,
            'max_steps': action.max_steps or self.ACTIONS.get(action.action_type, {}).get('max_steps', 10),
            'profile_id': profile_id,
            'can_proceed': True,
            'message': message
        }

    def _generate_browser_task(self, action: InstagramAction, message: str = None) -> str:
        """Generate Browser-Use task description."""

        handle = action.target_handle.lstrip('@')
        profile_url = action.target_url or f"https://www.instagram.com/{handle}/"

        if action.action_type == 'follow':
            return f"""Follow {action.target_name} ({action.target_handle}) on Instagram.

Steps:
1. Navigate to {profile_url}
2. Wait for the profile page to load completely
3. Look for the "Follow" button (blue button)
4. Click the "Follow" button
5. Verify the button changes to "Following" (gray)

Success: The button now shows "Following" instead of "Follow"."""

        elif action.action_type == 'like_post':
            if action.post_url:
                return f"""Like a specific Instagram post from {action.target_name}.

Post URL: {action.post_url}

Steps:
1. Navigate to {action.post_url}
2. Wait for the post to load
3. Find the heart icon below the image/video
4. Click the heart icon to like
5. Verify the heart turns red/filled

Success: The heart icon is now red/filled."""
            else:
                return f"""Like a recent post from {action.target_name} ({action.target_handle}).

Steps:
1. Navigate to {profile_url}
2. Wait for profile and posts grid to load
3. Click on the most recent post (top-left of grid)
4. Wait for the post to open in a modal/page
5. Double-click the image OR click the heart icon to like
6. Verify the heart turns red

Success: The heart icon is red indicating the post is liked."""

        elif action.action_type == 'comment':
            comment_text = message or "Amazing! 🔥"
            if len(comment_text) > 2200:
                comment_text = comment_text[:2197] + "..."

            if action.post_url:
                return f"""Comment on an Instagram post from {action.target_name}.

Post URL: {action.post_url}
Comment: "{comment_text}"

Steps:
1. Navigate to {action.post_url}
2. Wait for the post to load
3. Click the comment icon (speech bubble) or the comment input field
4. Type the comment: "{comment_text}"
5. Press Enter or click "Post" to submit
6. Verify the comment appears

Success: Your comment is visible under the post."""
            else:
                return f"""Comment on a recent post from {action.target_name} ({action.target_handle}).

Comment: "{comment_text}"

Steps:
1. Navigate to {profile_url}
2. Click on the most recent post
3. Click the comment icon or comment input field
4. Type: "{comment_text}"
5. Press Enter or click "Post"
6. Verify your comment appears

Success: Your comment is visible under the post."""

        elif action.action_type == 'dm':
            dm_text = message or f"Hey {action.target_name.split()[0] if action.target_name else 'there'}! 👋 Love your content!"
            if len(dm_text) > 1000:
                dm_text = dm_text[:997] + "..."

            return f"""Send a direct message to {action.target_name} ({action.target_handle}) on Instagram.

Message: "{dm_text}"

Steps:
1. Navigate to {profile_url}
2. Click the "Message" button on their profile
   - If no Message button, click the three dots menu and select "Send Message"
3. Wait for the message dialog to open
4. In the message input field, type: "{dm_text}"
5. Click Send or press Enter

Success: Message appears in the conversation as sent."""

        elif action.action_type == 'story_reply':
            reply_text = message or "This is amazing! 🔥"
            if len(reply_text) > 1000:
                reply_text = reply_text[:997] + "..."

            return f"""Reply to {action.target_name}'s ({action.target_handle}) Instagram story.

Reply: "{reply_text}"

Steps:
1. Navigate to {profile_url}
2. Click on their profile picture (has colorful ring if story is active)
3. Wait for the story to load
4. Click the "Send message" or reply input at the bottom
5. Type: "{reply_text}"
6. Press Send

Success: Reply sent (appears as a DM to them)."""

        else:
            return f"Unknown Instagram action: {action.action_type}"

    def record_action(self, user_id: str, action: InstagramAction, success: bool, details: str = None):
        """Record action for rate limiting."""
        if self.rate_limiter:
            self.rate_limiter.record_action(
                user_id, 'instagram', action.action_type,
                action.target_handle, success, details
            )

    def get_remaining_limits(self, user_id: str = "default") -> Dict[str, int]:
        """Get remaining action limits."""
        if self.rate_limiter:
            return self.rate_limiter.get_remaining_limits(user_id, 'instagram')
        return {}

    def calculate_delay(self, action_type: str) -> int:
        """Calculate delay before next action."""
        if self.rate_limiter:
            return self.rate_limiter.calculate_delay('instagram', action_type)
        return 90


# Helper functions
def create_follow_action(handle: str, name: str = "") -> InstagramAction:
    return InstagramAction(action_type='follow', target_handle=handle, target_name=name, max_steps=6)

def create_dm_action(handle: str, name: str, template_path: str = None,
                     template_vars: Dict = None, message: str = None) -> InstagramAction:
    return InstagramAction(
        action_type='dm', target_handle=handle, target_name=name,
        message=message, template_path=template_path or 'instagram/dms/cold_dm',
        template_vars=template_vars, max_steps=10
    )

def create_comment_action(handle: str, name: str, post_url: str = None,
                          template_path: str = None, template_vars: Dict = None,
                          message: str = None) -> InstagramAction:
    return InstagramAction(
        action_type='comment', target_handle=handle, target_name=name,
        post_url=post_url, message=message,
        template_path=template_path or 'instagram/comments/engagement',
        template_vars=template_vars, max_steps=8
    )

def create_like_action(handle: str, name: str = "", post_url: str = None) -> InstagramAction:
    return InstagramAction(
        action_type='like_post', target_handle=handle, target_name=name,
        post_url=post_url, max_steps=6
    )

def create_story_reply_action(handle: str, name: str, template_path: str = None,
                               template_vars: Dict = None, message: str = None) -> InstagramAction:
    return InstagramAction(
        action_type='story_reply', target_handle=handle, target_name=name,
        message=message, template_path=template_path or 'instagram/stories/story_reply',
        template_vars=template_vars, max_steps=10
    )


def main():
    """CLI for Instagram adapter."""
    import argparse

    parser = argparse.ArgumentParser(description="Instagram Adapter CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Generate task
    task_parser = subparsers.add_parser('task', help='Generate browser task')
    task_parser.add_argument('--action', required=True,
                             choices=['follow', 'like_post', 'comment', 'dm', 'story_reply'])
    task_parser.add_argument('--handle', required=True, help='Target @handle')
    task_parser.add_argument('--name', default='', help='Target name')
    task_parser.add_argument('--message', help='Message text')
    task_parser.add_argument('--template', help='Template path')
    task_parser.add_argument('--post-url', help='Post URL for likes/comments')
    task_parser.add_argument('--user', default='default', help='User ID')

    # Limits
    limits_parser = subparsers.add_parser('limits', help='Check rate limits')
    limits_parser.add_argument('--user', default='default')

    # Actions list
    subparsers.add_parser('actions', help='List available actions')

    args = parser.parse_args()
    adapter = InstagramAdapter()

    if args.command == 'task':
        action = InstagramAction(
            action_type=args.action,
            target_handle=args.handle,
            target_name=args.name,
            message=args.message,
            template_path=args.template,
            post_url=args.post_url
        )
        result = adapter.generate_task(action, args.user)
        print(json.dumps(result, indent=2))

    elif args.command == 'limits':
        limits = adapter.get_remaining_limits(args.user)
        print("Remaining Instagram limits:")
        for action, remaining in limits.items():
            print(f"  {action}: {remaining}")

    elif args.command == 'actions':
        print("Available Instagram Actions:")
        for action, info in InstagramAdapter.ACTIONS.items():
            print(f"  {action}: {info['description']}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
