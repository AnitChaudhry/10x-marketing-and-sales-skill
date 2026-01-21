#!/usr/bin/env python3
"""
Discovery Engine for 100X Outreach System

Integrates with Exa AI MCP to find relevant people for outreach.
Supports LinkedIn search, company research, and cross-platform profile discovery.

NOTE: This script provides helper functions and data structures.
The actual Exa AI calls are made through Claude Code's MCP integration.
This script processes and stores the discovery results.
"""

import json
import re
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
class DiscoveredPerson:
    """A person discovered through Exa AI search"""
    id: str
    name: str
    title: str = ""
    company: str = ""
    location: str = ""
    linkedin_url: str = ""
    twitter_handle: str = ""
    instagram_handle: str = ""
    email: str = ""
    website: str = ""
    bio: str = ""
    interests: List[str] = field(default_factory=list)
    recent_activity: List[str] = field(default_factory=list)
    discovery_source: str = ""  # linkedin_search, company_research, web_search
    discovered_at: str = ""
    enriched: bool = False
    tags: List[str] = field(default_factory=list)
    notes: str = ""
    outreach_status: str = "not_contacted"  # not_contacted, contacted, replied, connected


@dataclass
class DiscoverySession:
    """A discovery session containing search results"""
    id: str
    query: str
    source: str
    created_at: str
    results: List[DiscoveredPerson] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)


class DiscoveryEngine:
    """
    Manages people discovery and enrichment.

    This engine:
    1. Stores and organizes discovery results from Exa AI
    2. Deduplicates and merges profiles
    3. Tracks outreach status
    4. Exports to various formats
    """

    def __init__(self, data_dir: str = "output/discovery"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.sessions_file = self.data_dir / "sessions.json"
        self.people_file = self.data_dir / "people.json"
        self._sessions: List[DiscoverySession] = []
        self._people: Dict[str, DiscoveredPerson] = {}  # id -> person
        self._load_data()

    def _load_data(self):
        """Load discovery data from disk"""
        if self.sessions_file.exists():
            try:
                with open(self.sessions_file, 'r') as f:
                    data = json.load(f)
                    self._sessions = [
                        DiscoverySession(
                            **{**s, 'results': [DiscoveredPerson(**p) for p in s.get('results', [])]}
                        )
                        for s in data.get('sessions', [])
                    ]
            except Exception as e:
                print(f"Warning: Could not load sessions: {e}")

        if self.people_file.exists():
            try:
                with open(self.people_file, 'r') as f:
                    data = json.load(f)
                    self._people = {
                        pid: DiscoveredPerson(**p)
                        for pid, p in data.get('people', {}).items()
                    }
            except Exception as e:
                print(f"Warning: Could not load people: {e}")

    def _save_data(self):
        """Save discovery data to disk"""
        sessions_data = {
            'sessions': [
                {
                    **asdict(s),
                    'results': [asdict(p) for p in s.results]
                }
                for s in self._sessions
            ],
            'last_updated': datetime.now().isoformat()
        }

        with open(self.sessions_file, 'w') as f:
            json.dump(sessions_data, f, indent=2)

        people_data = {
            'people': {pid: asdict(p) for pid, p in self._people.items()},
            'last_updated': datetime.now().isoformat()
        }

        with open(self.people_file, 'w') as f:
            json.dump(people_data, f, indent=2)

    def create_session(self, query: str, source: str) -> DiscoverySession:
        """Create a new discovery session"""
        session = DiscoverySession(
            id=str(uuid.uuid4())[:8],
            query=query,
            source=source,
            created_at=datetime.now().isoformat()
        )
        self._sessions.append(session)
        self._save_data()
        return session

    def add_person(self, session_id: str, person_data: Dict) -> DiscoveredPerson:
        """Add a discovered person to a session"""
        # Find session
        session = next((s for s in self._sessions if s.id == session_id), None)
        if not session:
            raise ValueError(f"Session not found: {session_id}")

        # Create person
        person = DiscoveredPerson(
            id=str(uuid.uuid4())[:8],
            name=person_data.get('name', ''),
            title=person_data.get('title', ''),
            company=person_data.get('company', ''),
            location=person_data.get('location', ''),
            linkedin_url=person_data.get('linkedin_url', ''),
            twitter_handle=self._extract_twitter_handle(person_data.get('twitter', '')),
            instagram_handle=self._extract_instagram_handle(person_data.get('instagram', '')),
            email=person_data.get('email', ''),
            website=person_data.get('website', ''),
            bio=person_data.get('bio', ''),
            interests=person_data.get('interests', []),
            recent_activity=person_data.get('recent_activity', []),
            discovery_source=session.source,
            discovered_at=datetime.now().isoformat(),
            tags=person_data.get('tags', [])
        )

        # Check for duplicates
        existing = self._find_duplicate(person)
        if existing:
            # Merge data
            self._merge_person(existing, person)
            session.results.append(existing)
            return existing

        # Add new person
        session.results.append(person)
        self._people[person.id] = person
        self._save_data()
        return person

    def _extract_twitter_handle(self, text: str) -> str:
        """Extract Twitter handle from URL or text"""
        if not text:
            return ""
        # Handle URLs
        match = re.search(r'(?:twitter\.com|x\.com)/(@?\w+)', text, re.I)
        if match:
            handle = match.group(1)
            return handle if handle.startswith('@') else f'@{handle}'
        # Already a handle
        if text.startswith('@'):
            return text
        return f'@{text}' if text else ''

    def _extract_instagram_handle(self, text: str) -> str:
        """Extract Instagram handle from URL or text"""
        if not text:
            return ""
        match = re.search(r'instagram\.com/(@?\w+)', text, re.I)
        if match:
            handle = match.group(1)
            return handle if handle.startswith('@') else f'@{handle}'
        if text.startswith('@'):
            return text
        return f'@{text}' if text else ''

    def _find_duplicate(self, person: DiscoveredPerson) -> Optional[DiscoveredPerson]:
        """Find a duplicate person based on LinkedIn URL, email, or name+company"""
        for existing in self._people.values():
            # Match by LinkedIn URL
            if person.linkedin_url and existing.linkedin_url:
                if self._normalize_linkedin(person.linkedin_url) == self._normalize_linkedin(existing.linkedin_url):
                    return existing

            # Match by email
            if person.email and existing.email:
                if person.email.lower() == existing.email.lower():
                    return existing

            # Match by name + company
            if person.name and existing.name and person.company and existing.company:
                if (person.name.lower() == existing.name.lower() and
                    person.company.lower() == existing.company.lower()):
                    return existing

        return None

    def _normalize_linkedin(self, url: str) -> str:
        """Normalize LinkedIn URL for comparison"""
        url = url.lower().strip().rstrip('/')
        match = re.search(r'linkedin\.com/in/([^/?]+)', url)
        return match.group(1) if match else url

    def _merge_person(self, existing: DiscoveredPerson, new: DiscoveredPerson):
        """Merge new data into existing person"""
        # Update empty fields
        if not existing.title and new.title:
            existing.title = new.title
        if not existing.company and new.company:
            existing.company = new.company
        if not existing.location and new.location:
            existing.location = new.location
        if not existing.twitter_handle and new.twitter_handle:
            existing.twitter_handle = new.twitter_handle
        if not existing.instagram_handle and new.instagram_handle:
            existing.instagram_handle = new.instagram_handle
        if not existing.email and new.email:
            existing.email = new.email
        if not existing.bio and new.bio:
            existing.bio = new.bio

        # Merge lists
        existing.interests = list(set(existing.interests + new.interests))
        existing.tags = list(set(existing.tags + new.tags))
        existing.recent_activity = (new.recent_activity + existing.recent_activity)[:10]

        existing.enriched = True
        self._save_data()

    def get_session(self, session_id: str) -> Optional[DiscoverySession]:
        """Get a discovery session by ID"""
        return next((s for s in self._sessions if s.id == session_id), None)

    def get_person(self, person_id: str) -> Optional[DiscoveredPerson]:
        """Get a person by ID"""
        return self._people.get(person_id)

    def search_people(self, query: str = None, tags: List[str] = None,
                     has_linkedin: bool = None, has_twitter: bool = None,
                     has_email: bool = None, status: str = None) -> List[DiscoveredPerson]:
        """Search people with filters"""
        results = list(self._people.values())

        if query:
            query_lower = query.lower()
            results = [p for p in results if (
                query_lower in p.name.lower() or
                query_lower in p.company.lower() or
                query_lower in p.title.lower() or
                query_lower in p.bio.lower()
            )]

        if tags:
            results = [p for p in results if any(t in p.tags for t in tags)]

        if has_linkedin is not None:
            results = [p for p in results if bool(p.linkedin_url) == has_linkedin]

        if has_twitter is not None:
            results = [p for p in results if bool(p.twitter_handle) == has_twitter]

        if has_email is not None:
            results = [p for p in results if bool(p.email) == has_email]

        if status:
            results = [p for p in results if p.outreach_status == status]

        return results

    def update_outreach_status(self, person_id: str, status: str, notes: str = None) -> bool:
        """Update outreach status for a person"""
        person = self._people.get(person_id)
        if not person:
            return False

        person.outreach_status = status
        if notes:
            person.notes = notes
        self._save_data()
        return True

    def add_tags(self, person_id: str, tags: List[str]) -> bool:
        """Add tags to a person"""
        person = self._people.get(person_id)
        if not person:
            return False

        person.tags = list(set(person.tags + tags))
        self._save_data()
        return True

    def export_to_json(self, people: List[DiscoveredPerson], output_path: str) -> str:
        """Export people to JSON file"""
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        data = {
            'exported_at': datetime.now().isoformat(),
            'count': len(people),
            'people': [asdict(p) for p in people]
        }

        with open(output, 'w') as f:
            json.dump(data, f, indent=2)

        return str(output)

    def export_to_csv(self, people: List[DiscoveredPerson], output_path: str) -> str:
        """Export people to CSV file"""
        import csv

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        headers = ['name', 'title', 'company', 'location', 'email',
                   'linkedin_url', 'twitter_handle', 'instagram_handle',
                   'outreach_status', 'tags']

        with open(output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for p in people:
                writer.writerow({
                    'name': p.name,
                    'title': p.title,
                    'company': p.company,
                    'location': p.location,
                    'email': p.email,
                    'linkedin_url': p.linkedin_url,
                    'twitter_handle': p.twitter_handle,
                    'instagram_handle': p.instagram_handle,
                    'outreach_status': p.outreach_status,
                    'tags': ','.join(p.tags)
                })

        return str(output)

    def get_stats(self) -> Dict:
        """Get discovery statistics"""
        total_people = len(self._people)
        total_sessions = len(self._sessions)

        status_counts = {}
        platform_counts = {'linkedin': 0, 'twitter': 0, 'instagram': 0, 'email': 0}

        for person in self._people.values():
            status = person.outreach_status
            status_counts[status] = status_counts.get(status, 0) + 1

            if person.linkedin_url:
                platform_counts['linkedin'] += 1
            if person.twitter_handle:
                platform_counts['twitter'] += 1
            if person.instagram_handle:
                platform_counts['instagram'] += 1
            if person.email:
                platform_counts['email'] += 1

        return {
            'total_people': total_people,
            'total_sessions': total_sessions,
            'status_breakdown': status_counts,
            'platform_availability': platform_counts
        }

    def parse_exa_linkedin_results(self, exa_response: Dict) -> List[Dict]:
        """
        Parse Exa AI LinkedIn search results into person dictionaries.

        Expected Exa response structure:
        {
            "results": [
                {
                    "url": "https://linkedin.com/in/...",
                    "title": "John Doe - CEO at Company",
                    "text": "Bio/about text...",
                    "highlights": [...]
                }
            ]
        }
        """
        people = []

        for result in exa_response.get('results', []):
            url = result.get('url', '')
            title = result.get('title', '')
            text = result.get('text', '')

            # Parse name and title from LinkedIn title format
            # "John Doe - CEO at Company | LinkedIn"
            name_title_match = re.match(r'^([^-]+)\s*-\s*(.+?)(?:\s*\|\s*LinkedIn)?$', title)

            if name_title_match:
                name = name_title_match.group(1).strip()
                role_company = name_title_match.group(2).strip()

                # Parse role and company
                if ' at ' in role_company:
                    parts = role_company.split(' at ', 1)
                    role = parts[0].strip()
                    company = parts[1].strip()
                else:
                    role = role_company
                    company = ''
            else:
                name = title
                role = ''
                company = ''

            person = {
                'name': name,
                'title': role,
                'company': company,
                'linkedin_url': url,
                'bio': text[:500] if text else '',
                'tags': ['exa_linkedin_search']
            }

            people.append(person)

        return people

    def parse_exa_company_results(self, exa_response: Dict, company_name: str) -> Dict:
        """
        Parse Exa AI company research results.

        Returns company information that can be used to enrich person profiles.
        """
        company_info = {
            'name': company_name,
            'website': '',
            'description': '',
            'industry': '',
            'size': '',
            'location': '',
            'social_links': {}
        }

        for result in exa_response.get('results', []):
            url = result.get('url', '')
            text = result.get('text', '')

            # Extract company website
            if not company_info['website'] and company_name.lower() in url.lower():
                company_info['website'] = url

            # Extract description
            if text and not company_info['description']:
                company_info['description'] = text[:500]

            # Look for social links
            if 'twitter.com' in url or 'x.com' in url:
                company_info['social_links']['twitter'] = url
            elif 'linkedin.com/company' in url:
                company_info['social_links']['linkedin'] = url

        return company_info


def print_rich_output(engine: DiscoveryEngine, output_type: str, data=None):
    """Print formatted output"""
    if not RICH_AVAILABLE:
        print(json.dumps(data if data else engine.get_stats(), indent=2))
        return

    console = Console()

    if output_type == 'stats':
        stats = engine.get_stats()
        console.print(Panel(
            f"[bold]Total People:[/bold] {stats['total_people']}\n"
            f"[bold]Total Sessions:[/bold] {stats['total_sessions']}\n\n"
            f"[bold]Status Breakdown:[/bold]\n" +
            '\n'.join([f"  {k}: {v}" for k, v in stats['status_breakdown'].items()]) +
            f"\n\n[bold]Platform Availability:[/bold]\n" +
            '\n'.join([f"  {k}: {v}" for k, v in stats['platform_availability'].items()]),
            title="Discovery Statistics",
            border_style="green"
        ))

    elif output_type == 'people' and data:
        table = Table(title=f"Discovered People ({len(data)})")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Title")
        table.add_column("Company")
        table.add_column("LI", style="blue")
        table.add_column("TW", style="cyan")
        table.add_column("Status")

        for person in data[:50]:  # Limit to 50
            table.add_row(
                person.id,
                person.name[:20],
                person.title[:20] if person.title else "-",
                person.company[:15] if person.company else "-",
                "[green]Yes[/green]" if person.linkedin_url else "[red]No[/red]",
                "[green]Yes[/green]" if person.twitter_handle else "[red]No[/red]",
                person.outreach_status
            )

        console.print(table)

    elif output_type == 'person' and data:
        person = data
        console.print(Panel(
            f"[bold cyan]Name:[/bold cyan] {person.name}\n"
            f"[bold cyan]Title:[/bold cyan] {person.title or 'N/A'}\n"
            f"[bold cyan]Company:[/bold cyan] {person.company or 'N/A'}\n"
            f"[bold cyan]Location:[/bold cyan] {person.location or 'N/A'}\n"
            f"[bold cyan]Email:[/bold cyan] {person.email or 'N/A'}\n\n"
            f"[bold]Platforms:[/bold]\n"
            f"  LinkedIn: {person.linkedin_url or 'N/A'}\n"
            f"  Twitter: {person.twitter_handle or 'N/A'}\n"
            f"  Instagram: {person.instagram_handle or 'N/A'}\n\n"
            f"[bold]Status:[/bold] {person.outreach_status}\n"
            f"[bold]Tags:[/bold] {', '.join(person.tags) or 'None'}",
            title=f"Person: {person.name}",
            border_style="blue"
        ))


def main():
    """CLI interface for discovery engine"""
    import argparse

    parser = argparse.ArgumentParser(description="Discovery Engine CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Stats
    subparsers.add_parser('stats', help='Show discovery statistics')

    # List people
    list_parser = subparsers.add_parser('list', help='List discovered people')
    list_parser.add_argument('--query', help='Search query')
    list_parser.add_argument('--tags', nargs='+', help='Filter by tags')
    list_parser.add_argument('--has-linkedin', action='store_true')
    list_parser.add_argument('--has-twitter', action='store_true')
    list_parser.add_argument('--status', help='Filter by status')

    # Get person
    get_parser = subparsers.add_parser('get', help='Get person details')
    get_parser.add_argument('--id', required=True, help='Person ID')

    # Update status
    status_parser = subparsers.add_parser('status', help='Update person status')
    status_parser.add_argument('--id', required=True, help='Person ID')
    status_parser.add_argument('--status', required=True,
                               choices=['not_contacted', 'contacted', 'replied', 'connected'])
    status_parser.add_argument('--notes', help='Notes')

    # Export
    export_parser = subparsers.add_parser('export', help='Export people')
    export_parser.add_argument('--format', choices=['json', 'csv'], default='json')
    export_parser.add_argument('--output', required=True, help='Output file path')
    export_parser.add_argument('--query', help='Filter query')

    # Create session
    session_parser = subparsers.add_parser('session', help='Create discovery session')
    session_parser.add_argument('--query', required=True, help='Search query')
    session_parser.add_argument('--source', required=True,
                                choices=['linkedin_search', 'company_research', 'web_search'])

    args = parser.parse_args()

    engine = DiscoveryEngine()

    if args.command == 'stats':
        print_rich_output(engine, 'stats')

    elif args.command == 'list':
        people = engine.search_people(
            query=args.query,
            tags=args.tags,
            has_linkedin=args.has_linkedin if args.has_linkedin else None,
            has_twitter=args.has_twitter if args.has_twitter else None,
            status=args.status
        )
        print_rich_output(engine, 'people', people)

    elif args.command == 'get':
        person = engine.get_person(args.id)
        if person:
            print_rich_output(engine, 'person', person)
        else:
            print("Person not found")

    elif args.command == 'status':
        if engine.update_outreach_status(args.id, args.status, args.notes):
            print(f"Updated status for {args.id} to {args.status}")
        else:
            print("Person not found")

    elif args.command == 'export':
        people = engine.search_people(query=args.query) if args.query else list(engine._people.values())
        if args.format == 'csv':
            path = engine.export_to_csv(people, args.output)
        else:
            path = engine.export_to_json(people, args.output)
        print(f"Exported {len(people)} people to {path}")

    elif args.command == 'session':
        session = engine.create_session(args.query, args.source)
        print(f"Created session: {session.id}")
        print(f"Query: {session.query}")
        print(f"Source: {session.source}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
