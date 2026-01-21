#!/usr/bin/env python3
"""
Gmail Inbox Reader for 10x-Outreach-Skill
Read, search, and manage emails from Gmail inbox
"""

import os
import sys
import json
import base64
import re
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Any
from email.utils import parsedate_to_datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from dotenv import load_dotenv
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    import html2text
except ImportError as e:
    print(f"[X] Missing dependency: {e}")
    sys.exit(1)

from gmail_client import GmailClient

load_dotenv(Path(__file__).parent.parent / '.env')
console = Console()


class InboxReader:
    """
    Gmail Inbox Reader for reading and managing emails.

    Features:
    - List emails from inbox/any label
    - Search emails with Gmail queries
    - Read full email content
    - Get email statistics
    - Export emails to files
    """

    # Gmail API scopes for reading
    SCOPES = [
        'https://www.googleapis.com/auth/gmail.readonly',
        'https://www.googleapis.com/auth/gmail.labels',
        'https://www.googleapis.com/auth/gmail.modify',
    ]

    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.gmail_client = GmailClient()
        self.service = None

    def authenticate(self) -> bool:
        """Authenticate and get Gmail service."""
        if self.gmail_client.authenticate():
            self.service = self.gmail_client.service
            return True
        return False

    def list_labels(self) -> Dict[str, Any]:
        """
        List all Gmail labels (folders).

        Returns:
            Dict with labels list
        """
        if not self.service:
            return {'success': False, 'error': 'Not authenticated'}

        try:
            results = self.service.users().labels().list(userId='me').execute()
            labels = results.get('labels', [])

            formatted = []
            for label in labels:
                formatted.append({
                    'id': label['id'],
                    'name': label['name'],
                    'type': label.get('type', 'user')
                })

            return {
                'success': True,
                'labels': formatted,
                'count': len(formatted)
            }
        except HttpError as e:
            return {'success': False, 'error': str(e)}

    def list_emails(
        self,
        max_results: int = 10,
        label_ids: Optional[List[str]] = None,
        query: Optional[str] = None,
        include_body: bool = False
    ) -> Dict[str, Any]:
        """
        List emails from inbox.

        Args:
            max_results: Maximum emails to fetch
            label_ids: Filter by labels (default: INBOX)
            query: Gmail search query
            include_body: Include email body (slower)

        Returns:
            Dict with emails list
        """
        if not self.service:
            return {'success': False, 'error': 'Not authenticated'}

        try:
            # Build query
            params = {
                'userId': 'me',
                'maxResults': max_results,
            }

            if label_ids:
                params['labelIds'] = label_ids
            else:
                params['labelIds'] = ['INBOX']

            if query:
                params['q'] = query

            # List message IDs
            results = self.service.users().messages().list(**params).execute()
            messages = results.get('messages', [])

            if not messages:
                return {
                    'success': True,
                    'emails': [],
                    'count': 0,
                    'message': 'No emails found'
                }

            # Fetch details for each message
            emails = []
            for msg in messages:
                email_data = self._get_email_details(msg['id'], include_body)
                if email_data:
                    emails.append(email_data)

            return {
                'success': True,
                'emails': emails,
                'count': len(emails),
                'query': query
            }

        except HttpError as e:
            return {'success': False, 'error': str(e)}

    def _get_email_details(
        self,
        message_id: str,
        include_body: bool = False
    ) -> Optional[Dict]:
        """Get details for a single email."""
        try:
            msg = self.service.users().messages().get(
                userId='me',
                id=message_id,
                format='full' if include_body else 'metadata',
                metadataHeaders=['From', 'To', 'Subject', 'Date']
            ).execute()

            headers = {h['name']: h['value'] for h in msg.get('payload', {}).get('headers', [])}

            email_data = {
                'id': msg['id'],
                'thread_id': msg.get('threadId'),
                'snippet': msg.get('snippet', ''),
                'from': headers.get('From', ''),
                'to': headers.get('To', ''),
                'subject': headers.get('Subject', '(No Subject)'),
                'date': headers.get('Date', ''),
                'labels': msg.get('labelIds', []),
                'is_unread': 'UNREAD' in msg.get('labelIds', []),
            }

            # Parse date
            if email_data['date']:
                try:
                    dt = parsedate_to_datetime(email_data['date'])
                    email_data['date_parsed'] = dt.isoformat()
                    email_data['date_formatted'] = dt.strftime('%Y-%m-%d %H:%M')
                except:
                    email_data['date_parsed'] = None
                    email_data['date_formatted'] = email_data['date']

            # Get body if requested
            if include_body:
                email_data['body'] = self._extract_body(msg.get('payload', {}))

            return email_data

        except HttpError:
            return None

    def _extract_body(self, payload: Dict) -> str:
        """Extract email body from payload."""
        body = ""

        if 'body' in payload and payload['body'].get('data'):
            body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')
        elif 'parts' in payload:
            for part in payload['parts']:
                mime_type = part.get('mimeType', '')
                if mime_type == 'text/plain':
                    data = part.get('body', {}).get('data', '')
                    if data:
                        body = base64.urlsafe_b64decode(data).decode('utf-8')
                        break
                elif mime_type == 'text/html':
                    data = part.get('body', {}).get('data', '')
                    if data:
                        html_content = base64.urlsafe_b64decode(data).decode('utf-8')
                        # Convert HTML to plain text
                        h = html2text.HTML2Text()
                        h.ignore_links = False
                        body = h.handle(html_content)
                elif 'parts' in part:
                    # Nested parts
                    body = self._extract_body(part)
                    if body:
                        break

        return body.strip()

    def get_email(self, message_id: str) -> Dict[str, Any]:
        """
        Get full details of a single email.

        Args:
            message_id: Gmail message ID

        Returns:
            Dict with email details and body
        """
        if not self.service:
            return {'success': False, 'error': 'Not authenticated'}

        email_data = self._get_email_details(message_id, include_body=True)

        if email_data:
            return {'success': True, 'email': email_data}
        return {'success': False, 'error': 'Email not found'}

    def search_emails(
        self,
        query: str,
        max_results: int = 20,
        include_body: bool = False
    ) -> Dict[str, Any]:
        """
        Search emails using Gmail query syntax.

        Query examples:
        - "from:someone@example.com"
        - "subject:important"
        - "is:unread"
        - "after:2024/01/01 before:2024/12/31"
        - "has:attachment"

        Args:
            query: Gmail search query
            max_results: Maximum results
            include_body: Include email bodies

        Returns:
            Dict with matching emails
        """
        return self.list_emails(
            max_results=max_results,
            query=query,
            include_body=include_body,
            label_ids=None  # Search all labels
        )

    def get_emails_by_date_range(
        self,
        start_date: str,
        end_date: Optional[str] = None,
        max_results: int = 50
    ) -> Dict[str, Any]:
        """
        Get emails within a date range.

        Args:
            start_date: Start date (YYYY/MM/DD)
            end_date: End date (YYYY/MM/DD), defaults to today
            max_results: Maximum results

        Returns:
            Dict with emails in range
        """
        if not end_date:
            end_date = datetime.now().strftime('%Y/%m/%d')

        query = f"after:{start_date} before:{end_date}"
        return self.search_emails(query, max_results)

    def get_unread_emails(self, max_results: int = 20) -> Dict[str, Any]:
        """Get unread emails."""
        return self.search_emails("is:unread", max_results)

    def get_inbox_stats(self) -> Dict[str, Any]:
        """
        Get inbox statistics.

        Returns:
            Dict with inbox stats
        """
        if not self.service:
            return {'success': False, 'error': 'Not authenticated'}

        try:
            # Get profile
            profile = self.service.users().getProfile(userId='me').execute()

            # Count unread
            unread_result = self.service.users().messages().list(
                userId='me',
                q='is:unread',
                maxResults=1
            ).execute()
            unread_estimate = unread_result.get('resultSizeEstimate', 0)

            # Count today's emails
            today = datetime.now().strftime('%Y/%m/%d')
            today_result = self.service.users().messages().list(
                userId='me',
                q=f'after:{today}',
                maxResults=1
            ).execute()
            today_count = today_result.get('resultSizeEstimate', 0)

            return {
                'success': True,
                'email': profile.get('emailAddress'),
                'total_messages': profile.get('messagesTotal'),
                'total_threads': profile.get('threadsTotal'),
                'unread_count': unread_estimate,
                'today_count': today_count
            }

        except HttpError as e:
            return {'success': False, 'error': str(e)}

    def export_emails_to_json(
        self,
        emails: List[Dict],
        output_name: str
    ) -> str:
        """
        Export emails to JSON file.

        Args:
            emails: List of email dicts
            output_name: Output filename

        Returns:
            Path to saved file
        """
        output_dir = self.base_dir / 'output' / 'exports'
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / f"{output_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'exported_at': datetime.now().isoformat(),
                'count': len(emails),
                'emails': emails
            }, f, indent=2, ensure_ascii=False)

        return str(output_file)


def display_emails(emails: List[Dict], show_body: bool = False):
    """Display emails in a table format."""
    table = Table(title="Emails", show_lines=True)
    table.add_column("Date", style="cyan", width=16)
    table.add_column("From", style="green", width=25)
    table.add_column("Subject", width=40)
    table.add_column("Status", width=8)

    for email in emails:
        status = "[yellow]UNREAD[/yellow]" if email.get('is_unread') else "[dim]read[/dim]"
        table.add_row(
            email.get('date_formatted', '')[:16],
            email.get('from', '')[:25],
            email.get('subject', '')[:40],
            status
        )

    console.print(table)

    if show_body and emails:
        console.print("\n[bold]First Email Body:[/bold]")
        console.print(Panel(emails[0].get('body', emails[0].get('snippet', ''))[:1000]))


# CLI for testing
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Gmail Inbox Reader')
    parser.add_argument('--list', type=int, metavar='N', help='List N recent emails')
    parser.add_argument('--search', metavar='QUERY', help='Search emails')
    parser.add_argument('--unread', action='store_true', help='Show unread emails')
    parser.add_argument('--stats', action='store_true', help='Show inbox stats')
    parser.add_argument('--labels', action='store_true', help='List labels')
    parser.add_argument('--read', metavar='ID', help='Read specific email by ID')
    parser.add_argument('--body', action='store_true', help='Include email body')
    parser.add_argument('--date-range', nargs=2, metavar=('START', 'END'), help='Emails in date range (YYYY/MM/DD)')

    args = parser.parse_args()

    reader = InboxReader()

    if not reader.authenticate():
        console.print("[red]Authentication failed[/red]")
        sys.exit(1)

    if args.stats:
        result = reader.get_inbox_stats()
        if result['success']:
            console.print(Panel(
                f"[bold]Inbox Statistics[/bold]\n\n"
                f"Email: {result['email']}\n"
                f"Total Messages: {result['total_messages']}\n"
                f"Total Threads: {result['total_threads']}\n"
                f"Unread: {result['unread_count']}\n"
                f"Today: {result['today_count']}",
                title="Stats"
            ))

    elif args.labels:
        result = reader.list_labels()
        if result['success']:
            table = Table(title="Gmail Labels")
            table.add_column("Name")
            table.add_column("Type")
            for label in result['labels']:
                table.add_row(label['name'], label['type'])
            console.print(table)

    elif args.list:
        result = reader.list_emails(max_results=args.list, include_body=args.body)
        if result['success']:
            display_emails(result['emails'], args.body)

    elif args.search:
        result = reader.search_emails(args.search, include_body=args.body)
        if result['success']:
            console.print(f"[i] Found {result['count']} emails matching: {args.search}")
            display_emails(result['emails'], args.body)

    elif args.unread:
        result = reader.get_unread_emails()
        if result['success']:
            console.print(f"[i] Found {result['count']} unread emails")
            display_emails(result['emails'])

    elif args.read:
        result = reader.get_email(args.read)
        if result['success']:
            email = result['email']
            console.print(Panel(
                f"[bold]From:[/bold] {email['from']}\n"
                f"[bold]To:[/bold] {email['to']}\n"
                f"[bold]Subject:[/bold] {email['subject']}\n"
                f"[bold]Date:[/bold] {email['date_formatted']}\n\n"
                f"{email.get('body', email['snippet'])}",
                title="Email"
            ))

    elif args.date_range:
        result = reader.get_emails_by_date_range(args.date_range[0], args.date_range[1])
        if result['success']:
            console.print(f"[i] Found {result['count']} emails in range")
            display_emails(result['emails'])

    else:
        parser.print_help()
