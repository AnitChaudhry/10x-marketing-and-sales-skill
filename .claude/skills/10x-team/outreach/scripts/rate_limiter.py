#!/usr/bin/env python3
"""
Intelligent Rate Limiter for 100X Outreach System

Human-like rate limiting with platform awareness to avoid detection and bans.
Implements per-user, per-platform tracking with daily/hourly limits.
"""

import json
import random
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import threading

# Platform-specific rate limits (conservative to avoid detection)
PLATFORM_LIMITS = {
    "linkedin": {
        "connections_per_day": 20,
        "messages_per_day": 50,
        "profile_views_per_day": 100,
        "likes_per_day": 50,
        "comments_per_day": 20,
        "min_delay_seconds": 120,      # 2 minutes minimum
        "max_delay_seconds": 600,      # 10 minutes maximum
        "hourly_burst_limit": 10,
        "cool_down_after_burst": 1800, # 30 min after burst
        "active_hours": {"start": 8, "end": 20}  # 8 AM - 8 PM
    },
    "twitter": {
        "follows_per_day": 50,
        "dms_per_day": 50,
        "tweets_per_day": 20,
        "likes_per_day": 100,
        "retweets_per_day": 50,
        "min_delay_seconds": 60,
        "max_delay_seconds": 300,
        "hourly_burst_limit": 15,
        "cool_down_after_burst": 1200,
        "active_hours": {"start": 7, "end": 23}
    },
    "instagram": {
        "follows_per_day": 30,
        "dms_per_day": 30,
        "likes_per_day": 100,
        "comments_per_day": 30,
        "min_delay_seconds": 90,
        "max_delay_seconds": 400,
        "hourly_burst_limit": 8,
        "cool_down_after_burst": 2400,
        "active_hours": {"start": 9, "end": 21}
    },
    "gmail": {
        "emails_per_day": 100,
        "emails_per_hour": 20,
        "min_delay_seconds": 60,
        "max_delay_seconds": 180,
        "hourly_burst_limit": 15,
        "cool_down_after_burst": 900,
        "active_hours": {"start": 6, "end": 22}
    }
}

# Action type to limit mapping
ACTION_LIMITS = {
    "linkedin": {
        "connect": "connections_per_day",
        "message": "messages_per_day",
        "view_profile": "profile_views_per_day",
        "like": "likes_per_day",
        "comment": "comments_per_day"
    },
    "twitter": {
        "follow": "follows_per_day",
        "dm": "dms_per_day",
        "tweet": "tweets_per_day",
        "like": "likes_per_day",
        "retweet": "retweets_per_day"
    },
    "instagram": {
        "follow": "follows_per_day",
        "dm": "dms_per_day",
        "like": "likes_per_day",
        "comment": "comments_per_day"
    },
    "gmail": {
        "send": "emails_per_day",
        "send_campaign": "emails_per_day"
    }
}


@dataclass
class ActionRecord:
    """Record of a single action"""
    timestamp: str
    user_id: str
    platform: str
    action_type: str
    target: str
    success: bool
    details: Optional[str] = None


@dataclass
class UserPlatformStats:
    """Stats for a user on a specific platform"""
    user_id: str
    platform: str
    daily_counts: Dict[str, int]  # action_type -> count
    hourly_counts: Dict[str, int]
    last_action_time: Optional[str]
    in_cooldown: bool
    cooldown_until: Optional[str]

    @classmethod
    def empty(cls, user_id: str, platform: str) -> 'UserPlatformStats':
        return cls(
            user_id=user_id,
            platform=platform,
            daily_counts={},
            hourly_counts={},
            last_action_time=None,
            in_cooldown=False,
            cooldown_until=None
        )


class RateLimiter:
    """
    Intelligent rate limiter with human-like behavior patterns.

    Features:
    - Per-user, per-platform tracking
    - Daily and hourly limits
    - Burst detection and cool-down
    - Randomized delays (gaussian distribution)
    - Time-of-day awareness
    - Persistent state storage
    """

    def __init__(self, data_dir: str = "credentials"):
        self.data_dir = Path(data_dir)
        self.limits_file = self.data_dir / "rate_limits_state.json"
        self.actions_log = self.data_dir / "actions_log.json"
        self._lock = threading.Lock()
        self._state: Dict[str, Dict[str, UserPlatformStats]] = {}  # user_id -> platform -> stats
        self._actions: List[ActionRecord] = []
        self._load_state()

    def _load_state(self):
        """Load rate limiter state from disk"""
        if self.limits_file.exists():
            try:
                with open(self.limits_file, 'r') as f:
                    data = json.load(f)
                    for user_id, platforms in data.get('state', {}).items():
                        self._state[user_id] = {}
                        for platform, stats in platforms.items():
                            self._state[user_id][platform] = UserPlatformStats(**stats)
            except Exception as e:
                print(f"Warning: Could not load rate limiter state: {e}")
                self._state = {}

        if self.actions_log.exists():
            try:
                with open(self.actions_log, 'r') as f:
                    data = json.load(f)
                    self._actions = [ActionRecord(**a) for a in data.get('actions', [])]
            except Exception:
                self._actions = []

    def _save_state(self):
        """Save rate limiter state to disk"""
        self.data_dir.mkdir(parents=True, exist_ok=True)

        state_data = {
            'state': {
                user_id: {
                    platform: asdict(stats)
                    for platform, stats in platforms.items()
                }
                for user_id, platforms in self._state.items()
            },
            'last_updated': datetime.now().isoformat()
        }

        with open(self.limits_file, 'w') as f:
            json.dump(state_data, f, indent=2)

        # Keep only last 1000 actions
        recent_actions = self._actions[-1000:] if len(self._actions) > 1000 else self._actions
        actions_data = {
            'actions': [asdict(a) for a in recent_actions],
            'last_updated': datetime.now().isoformat()
        }

        with open(self.actions_log, 'w') as f:
            json.dump(actions_data, f, indent=2)

    def _get_stats(self, user_id: str, platform: str) -> UserPlatformStats:
        """Get or create stats for user/platform"""
        if user_id not in self._state:
            self._state[user_id] = {}
        if platform not in self._state[user_id]:
            self._state[user_id][platform] = UserPlatformStats.empty(user_id, platform)
        return self._state[user_id][platform]

    def _reset_daily_counts_if_needed(self, stats: UserPlatformStats):
        """Reset daily counts if it's a new day"""
        if stats.last_action_time:
            last_action = datetime.fromisoformat(stats.last_action_time)
            if last_action.date() < datetime.now().date():
                stats.daily_counts = {}
                stats.hourly_counts = {}

    def _reset_hourly_counts_if_needed(self, stats: UserPlatformStats):
        """Reset hourly counts if it's a new hour"""
        if stats.last_action_time:
            last_action = datetime.fromisoformat(stats.last_action_time)
            if last_action.hour != datetime.now().hour:
                stats.hourly_counts = {}

    def calculate_delay(self, platform: str, action_type: str,
                        custom_min: int = None, custom_max: int = None) -> int:
        """
        Calculate human-like delay with randomization.

        Uses gaussian distribution centered between min and max delays,
        with adjustments based on time of day and approaching limits.
        """
        limits = PLATFORM_LIMITS.get(platform, PLATFORM_LIMITS['gmail'])

        min_delay = custom_min or limits["min_delay_seconds"]
        max_delay = custom_max or limits["max_delay_seconds"]

        # Gaussian distribution centered between min and max
        mean = (min_delay + max_delay) / 2
        std_dev = (max_delay - min_delay) / 4
        delay = random.gauss(mean, std_dev)

        # Clamp to valid range
        delay = max(min_delay, min(max_delay, delay))

        # Add time-of-day variation (slower during "lunch" and "evening")
        hour = datetime.now().hour
        if 12 <= hour <= 14:  # Lunch time - slower
            delay *= 1.3
        elif 17 <= hour <= 19:  # Evening - slower
            delay *= 1.2
        elif hour < 8 or hour > 21:  # Off hours - much slower
            delay *= 2.0

        # Add small random jitter (0-10%)
        jitter = delay * random.uniform(0, 0.1)
        delay += jitter

        return int(delay)

    def can_proceed(self, user_id: str, platform: str, action_type: str) -> Tuple[bool, str, int]:
        """
        Check if action is allowed within rate limits.

        Returns:
            Tuple of (allowed: bool, reason: str, suggested_wait_seconds: int)
        """
        with self._lock:
            stats = self._get_stats(user_id, platform)
            limits = PLATFORM_LIMITS.get(platform)

            if not limits:
                return True, "Platform not tracked", 0

            self._reset_daily_counts_if_needed(stats)
            self._reset_hourly_counts_if_needed(stats)

            # Check cooldown
            if stats.in_cooldown and stats.cooldown_until:
                cooldown_end = datetime.fromisoformat(stats.cooldown_until)
                if datetime.now() < cooldown_end:
                    wait_seconds = int((cooldown_end - datetime.now()).total_seconds())
                    return False, f"In cooldown period", wait_seconds
                else:
                    stats.in_cooldown = False
                    stats.cooldown_until = None

            # Check active hours
            active_hours = limits.get("active_hours", {"start": 0, "end": 24})
            current_hour = datetime.now().hour
            if not (active_hours["start"] <= current_hour < active_hours["end"]):
                # Calculate wait until active hours
                if current_hour >= active_hours["end"]:
                    wait_until_tomorrow = (24 - current_hour + active_hours["start"]) * 3600
                    return False, f"Outside active hours", wait_until_tomorrow
                else:
                    wait_seconds = (active_hours["start"] - current_hour) * 3600
                    return False, f"Outside active hours", wait_seconds

            # Get the limit key for this action
            action_limits = ACTION_LIMITS.get(platform, {})
            limit_key = action_limits.get(action_type)

            if limit_key:
                daily_limit = limits.get(limit_key, 100)
                current_count = stats.daily_counts.get(action_type, 0)

                if current_count >= daily_limit:
                    # Calculate wait until tomorrow
                    tomorrow = datetime.now().replace(hour=0, minute=0, second=0) + timedelta(days=1)
                    wait_seconds = int((tomorrow - datetime.now()).total_seconds())
                    return False, f"Daily {action_type} limit reached ({daily_limit})", wait_seconds

            # Check hourly burst limit
            hourly_count = sum(stats.hourly_counts.values())
            if hourly_count >= limits.get("hourly_burst_limit", 15):
                # Enter cooldown
                cooldown_seconds = limits.get("cool_down_after_burst", 1800)
                stats.in_cooldown = True
                stats.cooldown_until = (datetime.now() + timedelta(seconds=cooldown_seconds)).isoformat()
                self._save_state()
                return False, f"Hourly burst limit reached, entering cooldown", cooldown_seconds

            return True, "OK", 0

    def record_action(self, user_id: str, platform: str, action_type: str,
                      target: str, success: bool, details: str = None):
        """Record an action and update counters"""
        with self._lock:
            stats = self._get_stats(user_id, platform)

            # Update counts
            stats.daily_counts[action_type] = stats.daily_counts.get(action_type, 0) + 1
            stats.hourly_counts[action_type] = stats.hourly_counts.get(action_type, 0) + 1
            stats.last_action_time = datetime.now().isoformat()

            # Record action
            record = ActionRecord(
                timestamp=datetime.now().isoformat(),
                user_id=user_id,
                platform=platform,
                action_type=action_type,
                target=target,
                success=success,
                details=details
            )
            self._actions.append(record)

            self._save_state()

    def get_user_stats(self, user_id: str) -> Dict[str, Dict]:
        """Get all stats for a user across platforms"""
        with self._lock:
            if user_id not in self._state:
                return {}

            return {
                platform: {
                    'daily_counts': stats.daily_counts,
                    'hourly_counts': stats.hourly_counts,
                    'in_cooldown': stats.in_cooldown,
                    'cooldown_until': stats.cooldown_until,
                    'last_action': stats.last_action_time
                }
                for platform, stats in self._state[user_id].items()
            }

    def get_remaining_limits(self, user_id: str, platform: str) -> Dict[str, int]:
        """Get remaining actions for today"""
        with self._lock:
            stats = self._get_stats(user_id, platform)
            limits = PLATFORM_LIMITS.get(platform, {})
            action_limits = ACTION_LIMITS.get(platform, {})

            self._reset_daily_counts_if_needed(stats)

            remaining = {}
            for action_type, limit_key in action_limits.items():
                daily_limit = limits.get(limit_key, 100)
                current = stats.daily_counts.get(action_type, 0)
                remaining[action_type] = max(0, daily_limit - current)

            return remaining

    def wait_for_next_action(self, user_id: str, platform: str, action_type: str) -> int:
        """
        Calculate and wait for the appropriate delay.
        Returns the actual delay used.
        """
        can_proceed, reason, wait_seconds = self.can_proceed(user_id, platform, action_type)

        if not can_proceed:
            print(f"Rate limit: {reason}. Waiting {wait_seconds} seconds...")
            time.sleep(wait_seconds)
            return wait_seconds

        # Calculate human-like delay
        delay = self.calculate_delay(platform, action_type)
        time.sleep(delay)
        return delay

    def get_platform_limits(self, platform: str) -> Dict:
        """Get the rate limits for a platform"""
        return PLATFORM_LIMITS.get(platform, {})

    def reset_user_stats(self, user_id: str, platform: str = None):
        """Reset stats for a user (optionally for specific platform)"""
        with self._lock:
            if user_id in self._state:
                if platform:
                    if platform in self._state[user_id]:
                        self._state[user_id][platform] = UserPlatformStats.empty(user_id, platform)
                else:
                    self._state[user_id] = {}
            self._save_state()


def main():
    """Test the rate limiter"""
    import argparse

    parser = argparse.ArgumentParser(description="Rate Limiter CLI")
    parser.add_argument('--user', default='default', help='User ID')
    parser.add_argument('--platform', required=True, choices=['linkedin', 'twitter', 'instagram', 'gmail'])
    parser.add_argument('--action', required=True, help='Action type')
    parser.add_argument('--check', action='store_true', help='Check if action is allowed')
    parser.add_argument('--record', action='store_true', help='Record an action')
    parser.add_argument('--target', default='unknown', help='Target for recording')
    parser.add_argument('--stats', action='store_true', help='Show user stats')
    parser.add_argument('--remaining', action='store_true', help='Show remaining limits')
    parser.add_argument('--delay', action='store_true', help='Calculate delay')
    parser.add_argument('--limits', action='store_true', help='Show platform limits')

    args = parser.parse_args()

    limiter = RateLimiter()

    if args.check:
        allowed, reason, wait = limiter.can_proceed(args.user, args.platform, args.action)
        print(json.dumps({
            'allowed': allowed,
            'reason': reason,
            'wait_seconds': wait
        }, indent=2))

    elif args.record:
        limiter.record_action(args.user, args.platform, args.action, args.target, True)
        print(f"Recorded: {args.action} on {args.platform} for {args.user}")

    elif args.stats:
        stats = limiter.get_user_stats(args.user)
        print(json.dumps(stats, indent=2))

    elif args.remaining:
        remaining = limiter.get_remaining_limits(args.user, args.platform)
        print(json.dumps(remaining, indent=2))

    elif args.delay:
        delay = limiter.calculate_delay(args.platform, args.action)
        print(f"Calculated delay: {delay} seconds")

    elif args.limits:
        limits = limiter.get_platform_limits(args.platform)
        print(json.dumps(limits, indent=2))


if __name__ == "__main__":
    main()
