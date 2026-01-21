#!/usr/bin/env python3
"""
Twitter/X Adapter for 100X Outreach System

Provides Twitter automation actions using Browser-Use MCP.
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
class TwitterAction:
    """A Twitter action to be executed via Browser-Use"""
    action_type: str
    target_handle: str  # @username
    target_name: str
    target_url: str = ""  # Full URL if available
    message: Optional[str] = None
    template_path: Optional[str] = None
    template_vars: Optional[Dict] = None
    tweet_url: Optional[str] = None  # For replies/likes
    max_steps: int = 10


class TwitterAdapter:
    """
    Twitter automation adapter for Browser-Use MCP.

    Supported Actions:
    - follow: Follow a user
    - like_tweet: Like a specific tweet
    - retweet: Retweet a tweet
    - reply: Reply to a tweet
    - dm: Send a direct message
    - quote_tweet: Quote tweet with comment
    """

    ACTIONS = {
        'follow': {
            'description': 'Follow a Twitter user',
            'rate_limit_key': 'follows_per_day',
            'max_steps': 6
        },
        'like_tweet': {
            'description': 'Like a tweet',
            'rate_limit_key': 'likes_per_day',
            'max_steps': 5
        },
        'retweet': {
            'description': 'Retweet a tweet',
            'rate_limit_key': 'retweets_per_day',
            'max_steps': 5
        },
        'reply': {
            'description': 'Reply to a tweet',
            'rate_limit_key': 'tweets_per_day',
            'max_steps': 8
        },
        'dm': {
            'description': 'Send a direct message',
            'rate_limit_key': 'dms_per_day',
            'max_steps': 10
        },
        'quote_tweet': {
            'description': 'Quote tweet with your comment',
            'rate_limit_key': 'tweets_per_day',
            'max_steps': 8
        }
    }

    def __init__(self, data_dir: str = "."):
        self.data_dir = Path(data_dir)
        self.rate_limiter = RateLimiter() if RateLimiter else None
        self.template_loader = TemplateLoader() if TemplateLoader else None
        self.team_manager = TeamManager() if TeamManager else None

    def generate_task(self, action: TwitterAction, user_id: str = "default") -> Dict:
        """Generate a Browser-Use task for the given Twitter action."""

        # Check rate limits
        if self.rate_limiter:
            can_proceed, reason, wait_seconds = self.rate_limiter.can_proceed(
                user_id, 'twitter', action.action_type
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
            profile_id = self.team_manager.get_browser_profile(user_id, 'twitter')

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

    def _generate_browser_task(self, action: TwitterAction, message: str = None) -> str:
        """Generate Browser-Use task description."""

        handle = action.target_handle.lstrip('@')
        profile_url = action.target_url or f"https://x.com/{handle}"

        if action.action_type == 'follow':
            return f"""Follow {action.target_name} ({action.target_handle}) on Twitter/X.

Steps:
1. Navigate to {profile_url}
2. Wait for the profile page to load completely
3. Look for the "Follow" button
4. Click the "Follow" button
5. Verify the button changes to "Following"

Success: The Follow button now shows "Following" state."""

        elif action.action_type == 'like_tweet':
            tweet_url = action.tweet_url or profile_url
            return f"""Like a tweet from {action.target_name} ({action.target_handle}).

Steps:
1. Navigate to {tweet_url}
2. If this is a profile URL, scroll to find a recent tweet
3. Find the heart/like icon under the tweet
4. Click the like button
5. Verify the heart turns red/filled

Success: The like button is now filled/red."""

        elif action.action_type == 'retweet':
            tweet_url = action.tweet_url or profile_url
            return f"""Retweet a tweet from {action.target_name} ({action.target_handle}).

Steps:
1. Navigate to {tweet_url}
2. If this is a profile URL, scroll to find a recent tweet worth retweeting
3. Click the retweet icon (two arrows)
4. Select "Retweet" (not Quote Tweet)
5. Confirm the retweet

Success: The retweet icon turns green indicating it's been retweeted."""

        elif action.action_type == 'reply':
            tweet_url = action.tweet_url or profile_url
            reply_text = message or f"Great point, {action.target_handle}!"
            # Ensure under 280 chars
            if len(reply_text) > 280:
                reply_text = reply_text[:277] + "..."

            return f"""Reply to a tweet from {action.target_name} ({action.target_handle}).

Tweet URL: {tweet_url}
Reply text: "{reply_text}"

Steps:
1. Navigate to {tweet_url}
2. If this is a profile, find a recent tweet to reply to
3. Click the reply/comment icon under the tweet
4. In the reply box, type: "{reply_text}"
5. Click the "Reply" button to post

Success: Your reply is posted and visible in the thread."""

        elif action.action_type == 'dm':
            dm_text = message or f"Hey {action.target_name.split()[0] if action.target_name else 'there'}! I've been following your content and wanted to connect."
            # DMs can be longer but keep reasonable
            if len(dm_text) > 1000:
                dm_text = dm_text[:997] + "..."

            return f"""Send a direct message to {action.target_name} ({action.target_handle}) on Twitter/X.

Message: "{dm_text}"

Steps:
1. Navigate to {profile_url}
2. Click the "Message" or envelope icon on their profile
3. If prompted about message requests, continue
4. In the message input field, type: "{dm_text}"
5. Click the Send button (arrow icon)

Success: Message appears in the conversation thread as sent."""

        elif action.action_type == 'quote_tweet':
            tweet_url = action.tweet_url or profile_url
            quote_text = message or "This 👇"
            if len(quote_text) > 280:
                quote_text = quote_text[:277] + "..."

            return f"""Quote tweet from {action.target_name} ({action.target_handle}).

Tweet URL: {tweet_url}
Your comment: "{quote_text}"

Steps:
1. Navigate to {tweet_url}
2. Click the retweet icon (two arrows)
3. Select "Quote Tweet" option
4. In the text field, type: "{quote_text}"
5. Click "Tweet" to post

Success: Your quote tweet is posted with your comment above the original tweet."""

        else:
            return f"Unknown Twitter action: {action.action_type}"

    def record_action(self, user_id: str, action: TwitterAction, success: bool, details: str = None):
        """Record action for rate limiting."""
        if self.rate_limiter:
            self.rate_limiter.record_action(
                user_id, 'twitter', action.action_type,
                action.target_handle, success, details
            )

    def get_remaining_limits(self, user_id: str = "default") -> Dict[str, int]:
        """Get remaining action limits."""
        if self.rate_limiter:
            return self.rate_limiter.get_remaining_limits(user_id, 'twitter')
        return {}

    def calculate_delay(self, action_type: str) -> int:
        """Calculate delay before next action."""
        if self.rate_limiter:
            return self.rate_limiter.calculate_delay('twitter', action_type)
        return 60


# Helper functions for creating actions
def create_follow_action(handle: str, name: str = "") -> TwitterAction:
    return TwitterAction(action_type='follow', target_handle=handle, target_name=name, max_steps=6)

def create_dm_action(handle: str, name: str, template_path: str = None,
                     template_vars: Dict = None, message: str = None) -> TwitterAction:
    return TwitterAction(
        action_type='dm', target_handle=handle, target_name=name,
        message=message, template_path=template_path or 'twitter/dms/cold_dm',
        template_vars=template_vars, max_steps=10
    )

def create_reply_action(handle: str, name: str, tweet_url: str,
                        template_path: str = None, template_vars: Dict = None,
                        message: str = None) -> TwitterAction:
    return TwitterAction(
        action_type='reply', target_handle=handle, target_name=name,
        tweet_url=tweet_url, message=message,
        template_path=template_path or 'twitter/replies/value_add',
        template_vars=template_vars, max_steps=8
    )

def create_like_action(handle: str, name: str = "", tweet_url: str = None) -> TwitterAction:
    return TwitterAction(
        action_type='like_tweet', target_handle=handle, target_name=name,
        tweet_url=tweet_url, max_steps=5
    )


def main():
    """CLI for Twitter adapter."""
    import argparse

    parser = argparse.ArgumentParser(description="Twitter Adapter CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Generate task
    task_parser = subparsers.add_parser('task', help='Generate browser task')
    task_parser.add_argument('--action', required=True,
                             choices=['follow', 'like_tweet', 'retweet', 'reply', 'dm', 'quote_tweet'])
    task_parser.add_argument('--handle', required=True, help='Target @handle')
    task_parser.add_argument('--name', default='', help='Target name')
    task_parser.add_argument('--message', help='Message text')
    task_parser.add_argument('--template', help='Template path')
    task_parser.add_argument('--tweet-url', help='Tweet URL for replies/likes')
    task_parser.add_argument('--user', default='default', help='User ID')

    # Limits
    limits_parser = subparsers.add_parser('limits', help='Check rate limits')
    limits_parser.add_argument('--user', default='default')

    # Actions list
    subparsers.add_parser('actions', help='List available actions')

    args = parser.parse_args()
    adapter = TwitterAdapter()

    if args.command == 'task':
        action = TwitterAction(
            action_type=args.action,
            target_handle=args.handle,
            target_name=args.name,
            message=args.message,
            template_path=args.template,
            tweet_url=args.tweet_url
        )
        result = adapter.generate_task(action, args.user)
        print(json.dumps(result, indent=2))

    elif args.command == 'limits':
        limits = adapter.get_remaining_limits(args.user)
        print("Remaining Twitter limits:")
        for action, remaining in limits.items():
            print(f"  {action}: {remaining}")

    elif args.command == 'actions':
        print("Available Twitter Actions:")
        for action, info in TwitterAdapter.ACTIONS.items():
            print(f"  {action}: {info['description']}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
