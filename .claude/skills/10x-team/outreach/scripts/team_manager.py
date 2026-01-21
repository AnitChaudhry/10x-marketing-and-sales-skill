#!/usr/bin/env python3
"""
Team Manager for 100X Outreach System

Manages team members and their platform credentials for multi-user outreach.
Each team member can have their own authenticated accounts for LinkedIn, Twitter, Instagram, and Gmail.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict, field
import uuid

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


@dataclass
class PlatformCredentials:
    """Credentials for a specific platform"""
    enabled: bool = False
    profile_url: str = ""
    handle: str = ""
    browser_profile_id: str = ""
    daily_limit: int = 50
    hourly_limit: int = 10
    authenticated: bool = False
    last_auth_check: Optional[str] = None


@dataclass
class TeamMember:
    """A team member with their platform credentials"""
    id: str
    name: str
    email: str
    created_at: str
    platforms: Dict[str, PlatformCredentials] = field(default_factory=dict)
    timezone: str = "UTC"
    active_hours: Dict[str, str] = field(default_factory=lambda: {"start": "09:00", "end": "18:00"})
    is_active: bool = True

    def __post_init__(self):
        # Ensure all platforms exist
        for platform in ['linkedin', 'twitter', 'instagram', 'gmail']:
            if platform not in self.platforms:
                self.platforms[platform] = PlatformCredentials()
            elif isinstance(self.platforms[platform], dict):
                self.platforms[platform] = PlatformCredentials(**self.platforms[platform])


@dataclass
class Team:
    """Team configuration"""
    team_name: str
    created_at: str
    members: List[TeamMember] = field(default_factory=list)

    def __post_init__(self):
        # Convert dicts to TeamMember objects
        self.members = [
            TeamMember(**m) if isinstance(m, dict) else m
            for m in self.members
        ]


class TeamManager:
    """
    Manages team members and their credentials.

    Features:
    - Add/remove team members
    - Configure platform credentials per member
    - Track authentication status
    - Browser-Use profile management
    """

    def __init__(self, data_dir: str = "credentials"):
        self.data_dir = Path(data_dir)
        self.team_file = self.data_dir / "team.json"
        self.profiles_dir = self.data_dir / "profiles"
        self._team: Optional[Team] = None
        self._load_team()

    def _load_team(self):
        """Load team configuration from disk"""
        if self.team_file.exists():
            try:
                with open(self.team_file, 'r') as f:
                    data = json.load(f)
                    self._team = Team(**data)
            except Exception as e:
                print(f"Warning: Could not load team config: {e}")
                self._team = None

        if self._team is None:
            self._team = Team(
                team_name="Default Team",
                created_at=datetime.now().isoformat(),
                members=[]
            )

    def _save_team(self):
        """Save team configuration to disk"""
        self.data_dir.mkdir(parents=True, exist_ok=True)

        team_data = {
            'team_name': self._team.team_name,
            'created_at': self._team.created_at,
            'members': [
                {
                    'id': m.id,
                    'name': m.name,
                    'email': m.email,
                    'created_at': m.created_at,
                    'platforms': {
                        platform: asdict(creds)
                        for platform, creds in m.platforms.items()
                    },
                    'timezone': m.timezone,
                    'active_hours': m.active_hours,
                    'is_active': m.is_active
                }
                for m in self._team.members
            ]
        }

        with open(self.team_file, 'w') as f:
            json.dump(team_data, f, indent=2)

    def add_member(self, name: str, email: str, timezone: str = "UTC") -> TeamMember:
        """Add a new team member"""
        member = TeamMember(
            id=str(uuid.uuid4())[:8],
            name=name,
            email=email,
            created_at=datetime.now().isoformat(),
            timezone=timezone
        )

        self._team.members.append(member)

        # Create profile directory
        profile_dir = self.profiles_dir / member.id
        profile_dir.mkdir(parents=True, exist_ok=True)

        self._save_team()
        return member

    def remove_member(self, member_id: str) -> bool:
        """Remove a team member"""
        for i, member in enumerate(self._team.members):
            if member.id == member_id:
                self._team.members.pop(i)
                self._save_team()
                return True
        return False

    def get_member(self, member_id: str) -> Optional[TeamMember]:
        """Get a team member by ID"""
        for member in self._team.members:
            if member.id == member_id:
                return member
        return None

    def get_member_by_name(self, name: str) -> Optional[TeamMember]:
        """Get a team member by name (case-insensitive)"""
        name_lower = name.lower()
        for member in self._team.members:
            if member.name.lower() == name_lower:
                return member
        return None

    def list_members(self) -> List[TeamMember]:
        """List all team members"""
        return self._team.members

    def configure_platform(self, member_id: str, platform: str,
                          enabled: bool = True,
                          profile_url: str = "",
                          handle: str = "",
                          browser_profile_id: str = "",
                          daily_limit: int = None,
                          hourly_limit: int = None) -> bool:
        """Configure a platform for a team member"""
        member = self.get_member(member_id)
        if not member:
            return False

        if platform not in member.platforms:
            member.platforms[platform] = PlatformCredentials()

        creds = member.platforms[platform]
        creds.enabled = enabled

        if profile_url:
            creds.profile_url = profile_url
        if handle:
            creds.handle = handle
        if browser_profile_id:
            creds.browser_profile_id = browser_profile_id
        if daily_limit is not None:
            creds.daily_limit = daily_limit
        if hourly_limit is not None:
            creds.hourly_limit = hourly_limit

        self._save_team()
        return True

    def set_browser_profile(self, member_id: str, platform: str, profile_id: str) -> bool:
        """Set the Browser-Use profile ID for a member's platform"""
        member = self.get_member(member_id)
        if not member or platform not in member.platforms:
            return False

        member.platforms[platform].browser_profile_id = profile_id
        member.platforms[platform].authenticated = True
        member.platforms[platform].last_auth_check = datetime.now().isoformat()

        self._save_team()
        return True

    def get_browser_profile(self, member_id: str, platform: str) -> Optional[str]:
        """Get the Browser-Use profile ID for a member's platform"""
        member = self.get_member(member_id)
        if not member or platform not in member.platforms:
            return None
        return member.platforms[platform].browser_profile_id or None

    def get_enabled_platforms(self, member_id: str) -> List[str]:
        """Get list of enabled platforms for a member"""
        member = self.get_member(member_id)
        if not member:
            return []
        return [p for p, c in member.platforms.items() if c.enabled]

    def get_authenticated_platforms(self, member_id: str) -> List[str]:
        """Get list of authenticated platforms for a member"""
        member = self.get_member(member_id)
        if not member:
            return []
        return [p for p, c in member.platforms.items() if c.enabled and c.authenticated]

    def set_team_name(self, name: str):
        """Set the team name"""
        self._team.team_name = name
        self._save_team()

    def get_team_status(self) -> Dict:
        """Get overall team status"""
        total_members = len(self._team.members)
        active_members = sum(1 for m in self._team.members if m.is_active)

        platform_counts = {
            'linkedin': 0,
            'twitter': 0,
            'instagram': 0,
            'gmail': 0
        }

        for member in self._team.members:
            if member.is_active:
                for platform, creds in member.platforms.items():
                    if creds.enabled and creds.authenticated:
                        platform_counts[platform] = platform_counts.get(platform, 0) + 1

        return {
            'team_name': self._team.team_name,
            'total_members': total_members,
            'active_members': active_members,
            'platform_accounts': platform_counts
        }

    def export_member_config(self, member_id: str) -> Optional[Dict]:
        """Export a member's configuration (for backup/transfer)"""
        member = self.get_member(member_id)
        if not member:
            return None

        return {
            'id': member.id,
            'name': member.name,
            'email': member.email,
            'platforms': {
                platform: {
                    'enabled': creds.enabled,
                    'profile_url': creds.profile_url,
                    'handle': creds.handle,
                    'daily_limit': creds.daily_limit,
                    'hourly_limit': creds.hourly_limit
                    # Note: browser_profile_id not exported for security
                }
                for platform, creds in member.platforms.items()
            },
            'timezone': member.timezone,
            'active_hours': member.active_hours
        }


def print_rich_output(manager: TeamManager, output_type: str, data: any = None):
    """Print formatted output using rich library"""
    if not RICH_AVAILABLE:
        print(json.dumps(data, indent=2) if data else "No data")
        return

    console = Console()

    if output_type == "status":
        status = manager.get_team_status()
        console.print(Panel(
            f"[bold blue]{status['team_name']}[/bold blue]\n\n"
            f"Total Members: {status['total_members']}\n"
            f"Active Members: {status['active_members']}\n\n"
            f"[bold]Authenticated Accounts:[/bold]\n"
            f"  LinkedIn: {status['platform_accounts']['linkedin']}\n"
            f"  Twitter: {status['platform_accounts']['twitter']}\n"
            f"  Instagram: {status['platform_accounts']['instagram']}\n"
            f"  Gmail: {status['platform_accounts']['gmail']}",
            title="Team Status",
            border_style="green"
        ))

    elif output_type == "list":
        table = Table(title="Team Members")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Email")
        table.add_column("LinkedIn", style="blue")
        table.add_column("Twitter", style="cyan")
        table.add_column("Instagram", style="magenta")
        table.add_column("Gmail", style="red")
        table.add_column("Active")

        for member in manager.list_members():
            table.add_row(
                member.id,
                member.name,
                member.email,
                "[green]Yes[/green]" if member.platforms['linkedin'].authenticated else "[red]No[/red]",
                "[green]Yes[/green]" if member.platforms['twitter'].authenticated else "[red]No[/red]",
                "[green]Yes[/green]" if member.platforms['instagram'].authenticated else "[red]No[/red]",
                "[green]Yes[/green]" if member.platforms['gmail'].authenticated else "[red]No[/red]",
                "[green]Yes[/green]" if member.is_active else "[red]No[/red]"
            )

        console.print(table)

    elif output_type == "member" and data:
        member = data
        platforms_info = "\n".join([
            f"  [bold]{p.upper()}[/bold]: {'[green]Authenticated[/green]' if c.authenticated else '[red]Not set up[/red]'}"
            f"{' - ' + c.handle if c.handle else ''}"
            for p, c in member.platforms.items()
        ])

        console.print(Panel(
            f"[bold cyan]ID:[/bold cyan] {member.id}\n"
            f"[bold cyan]Name:[/bold cyan] {member.name}\n"
            f"[bold cyan]Email:[/bold cyan] {member.email}\n"
            f"[bold cyan]Timezone:[/bold cyan] {member.timezone}\n"
            f"[bold cyan]Active Hours:[/bold cyan] {member.active_hours['start']} - {member.active_hours['end']}\n\n"
            f"[bold]Platforms:[/bold]\n{platforms_info}",
            title=f"Team Member: {member.name}",
            border_style="blue"
        ))


def main():
    """CLI interface for team management"""
    import argparse

    parser = argparse.ArgumentParser(description="Team Manager CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Add member
    add_parser = subparsers.add_parser('add', help='Add a team member')
    add_parser.add_argument('--name', required=True, help='Member name')
    add_parser.add_argument('--email', required=True, help='Member email')
    add_parser.add_argument('--timezone', default='UTC', help='Timezone')

    # Remove member
    remove_parser = subparsers.add_parser('remove', help='Remove a team member')
    remove_parser.add_argument('--id', required=True, help='Member ID')

    # List members
    subparsers.add_parser('list', help='List all team members')

    # Get member
    get_parser = subparsers.add_parser('get', help='Get member details')
    get_parser.add_argument('--id', help='Member ID')
    get_parser.add_argument('--name', help='Member name')

    # Configure platform
    config_parser = subparsers.add_parser('configure', help='Configure platform for member')
    config_parser.add_argument('--id', required=True, help='Member ID')
    config_parser.add_argument('--platform', required=True,
                               choices=['linkedin', 'twitter', 'instagram', 'gmail'])
    config_parser.add_argument('--enable', action='store_true', help='Enable platform')
    config_parser.add_argument('--disable', action='store_true', help='Disable platform')
    config_parser.add_argument('--profile-url', help='Profile URL')
    config_parser.add_argument('--handle', help='Username/handle')
    config_parser.add_argument('--browser-profile', help='Browser-Use profile ID')
    config_parser.add_argument('--daily-limit', type=int, help='Daily action limit')
    config_parser.add_argument('--hourly-limit', type=int, help='Hourly action limit')

    # Team status
    subparsers.add_parser('status', help='Show team status')

    # Set team name
    name_parser = subparsers.add_parser('set-name', help='Set team name')
    name_parser.add_argument('--name', required=True, help='New team name')

    # Export
    export_parser = subparsers.add_parser('export', help='Export member config')
    export_parser.add_argument('--id', required=True, help='Member ID')

    args = parser.parse_args()

    manager = TeamManager()

    if args.command == 'add':
        member = manager.add_member(args.name, args.email, args.timezone)
        print(f"Added member: {member.name} (ID: {member.id})")
        print_rich_output(manager, 'member', member)

    elif args.command == 'remove':
        if manager.remove_member(args.id):
            print(f"Removed member: {args.id}")
        else:
            print(f"Member not found: {args.id}")

    elif args.command == 'list':
        print_rich_output(manager, 'list')

    elif args.command == 'get':
        member = None
        if args.id:
            member = manager.get_member(args.id)
        elif args.name:
            member = manager.get_member_by_name(args.name)

        if member:
            print_rich_output(manager, 'member', member)
        else:
            print("Member not found")

    elif args.command == 'configure':
        enabled = True
        if args.disable:
            enabled = False

        success = manager.configure_platform(
            args.id,
            args.platform,
            enabled=enabled,
            profile_url=args.profile_url or "",
            handle=args.handle or "",
            browser_profile_id=args.browser_profile or "",
            daily_limit=args.daily_limit,
            hourly_limit=args.hourly_limit
        )

        if success:
            print(f"Configured {args.platform} for member {args.id}")
            member = manager.get_member(args.id)
            print_rich_output(manager, 'member', member)
        else:
            print("Failed to configure platform")

    elif args.command == 'status':
        print_rich_output(manager, 'status')

    elif args.command == 'set-name':
        manager.set_team_name(args.name)
        print(f"Team name set to: {args.name}")

    elif args.command == 'export':
        config = manager.export_member_config(args.id)
        if config:
            print(json.dumps(config, indent=2))
        else:
            print("Member not found")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
