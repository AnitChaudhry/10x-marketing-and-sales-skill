#!/usr/bin/env python3
"""
Email Summarizer for 10x-Outreach-Skill
Generate summaries of emails using AI-powered analysis
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from dotenv import load_dotenv
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.markdown import Markdown
except ImportError as e:
    print(f"[X] Missing dependency: {e}")
    sys.exit(1)

from inbox_reader import InboxReader

load_dotenv(Path(__file__).parent.parent / '.env')
console = Console()


class EmailSummarizer:
    """
    Email Summarizer for generating email summaries.

    Features:
    - Summarize single emails
    - Summarize multiple emails (batch)
    - Summarize by date range
    - Generate daily/weekly digests
    - Export summaries to files
    """

    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.inbox_reader = InboxReader()

    def authenticate(self) -> bool:
        """Authenticate with Gmail."""
        return self.inbox_reader.authenticate()

    def extract_key_info(self, email: Dict) -> Dict[str, Any]:
        """
        Extract key information from an email for summary.

        Args:
            email: Email dict with body

        Returns:
            Dict with extracted info
        """
        body = email.get('body', email.get('snippet', ''))

        # Extract sender name from email
        from_field = email.get('from', '')
        sender_name = from_field.split('<')[0].strip().strip('"')
        if not sender_name:
            sender_name = from_field.split('@')[0]

        # Basic extraction
        info = {
            'id': email.get('id'),
            'from': from_field,
            'sender_name': sender_name,
            'subject': email.get('subject', '(No Subject)'),
            'date': email.get('date_formatted', ''),
            'is_unread': email.get('is_unread', False),
            'snippet': email.get('snippet', '')[:200],
            'body_length': len(body),
            'has_links': 'http' in body.lower(),
            'has_attachments': 'attachment' in str(email.get('labels', [])).lower(),
        }

        # Detect email type
        subject_lower = info['subject'].lower()
        if any(word in subject_lower for word in ['invoice', 'payment', 'receipt']):
            info['type'] = 'financial'
        elif any(word in subject_lower for word in ['meeting', 'calendar', 'schedule']):
            info['type'] = 'meeting'
        elif any(word in subject_lower for word in ['urgent', 'important', 'action required']):
            info['type'] = 'urgent'
        elif any(word in subject_lower for word in ['newsletter', 'digest', 'weekly']):
            info['type'] = 'newsletter'
        elif any(word in subject_lower for word in ['order', 'shipping', 'delivery']):
            info['type'] = 'order'
        else:
            info['type'] = 'general'

        # Extract action items (simple pattern matching)
        action_patterns = [
            'please reply', 'let me know', 'can you', 'could you',
            'action required', 'deadline', 'by tomorrow', 'asap'
        ]
        body_lower = body.lower()
        info['potential_actions'] = [p for p in action_patterns if p in body_lower]
        info['needs_response'] = len(info['potential_actions']) > 0

        return info

    def summarize_email(self, email: Dict) -> Dict[str, Any]:
        """
        Generate a summary for a single email.

        Args:
            email: Email dict with body

        Returns:
            Dict with summary
        """
        info = self.extract_key_info(email)

        # Build summary text
        summary_parts = []

        # Type indicator
        type_icons = {
            'financial': '💰',
            'meeting': '📅',
            'urgent': '🚨',
            'newsletter': '📰',
            'order': '📦',
            'general': '📧'
        }
        icon = type_icons.get(info['type'], '📧')

        summary_parts.append(f"{icon} **{info['type'].upper()}**")
        summary_parts.append(f"From: {info['sender_name']}")
        summary_parts.append(f"Subject: {info['subject']}")

        if info['needs_response']:
            summary_parts.append(f"⚠️ May need response: {', '.join(info['potential_actions'][:2])}")

        summary_parts.append(f"\nPreview: {info['snippet']}...")

        return {
            'id': info['id'],
            'subject': info['subject'],
            'from': info['from'],
            'sender_name': info['sender_name'],
            'date': info['date'],
            'type': info['type'],
            'needs_response': info['needs_response'],
            'summary_text': '\n'.join(summary_parts),
            'details': info
        }

    def summarize_multiple(
        self,
        max_emails: int = 10,
        query: Optional[str] = None,
        unread_only: bool = False
    ) -> Dict[str, Any]:
        """
        Summarize multiple emails.

        Args:
            max_emails: Number of emails to summarize
            query: Optional search query
            unread_only: Only summarize unread emails

        Returns:
            Dict with summaries and statistics
        """
        # Fetch emails
        if unread_only:
            result = self.inbox_reader.get_unread_emails(max_emails)
        elif query:
            result = self.inbox_reader.search_emails(query, max_emails, include_body=True)
        else:
            result = self.inbox_reader.list_emails(max_emails, include_body=True)

        if not result['success']:
            return result

        emails = result['emails']

        if not emails:
            return {
                'success': True,
                'summaries': [],
                'count': 0,
                'message': 'No emails found'
            }

        # Generate summaries
        summaries = []
        type_counts = {}
        needs_response_count = 0

        for email in emails:
            summary = self.summarize_email(email)
            summaries.append(summary)

            # Track statistics
            email_type = summary['type']
            type_counts[email_type] = type_counts.get(email_type, 0) + 1
            if summary['needs_response']:
                needs_response_count += 1

        return {
            'success': True,
            'summaries': summaries,
            'count': len(summaries),
            'statistics': {
                'total': len(summaries),
                'by_type': type_counts,
                'needs_response': needs_response_count,
                'unread': sum(1 for s in summaries if s['details'].get('is_unread'))
            }
        }

    def summarize_by_date_range(
        self,
        start_date: str,
        end_date: Optional[str] = None,
        max_emails: int = 50
    ) -> Dict[str, Any]:
        """
        Summarize emails within a date range.

        Args:
            start_date: Start date (YYYY/MM/DD)
            end_date: End date (YYYY/MM/DD)
            max_emails: Maximum emails

        Returns:
            Dict with summaries
        """
        result = self.inbox_reader.get_emails_by_date_range(
            start_date, end_date, max_emails
        )

        if not result['success']:
            return result

        # Re-fetch with body for summarization
        emails_with_body = []
        for email in result['emails'][:max_emails]:
            full_email = self.inbox_reader.get_email(email['id'])
            if full_email['success']:
                emails_with_body.append(full_email['email'])

        # Generate summaries
        summaries = [self.summarize_email(e) for e in emails_with_body]

        return {
            'success': True,
            'summaries': summaries,
            'count': len(summaries),
            'date_range': {
                'start': start_date,
                'end': end_date or 'today'
            }
        }

    def generate_digest(
        self,
        period: str = 'today',
        max_emails: int = 30
    ) -> Dict[str, Any]:
        """
        Generate an email digest for a period.

        Args:
            period: 'today', 'yesterday', 'week', or 'month'
            max_emails: Maximum emails to include

        Returns:
            Dict with digest
        """
        # Calculate date range
        today = datetime.now()

        if period == 'today':
            start_date = today.strftime('%Y/%m/%d')
            end_date = None
        elif period == 'yesterday':
            yesterday = today - timedelta(days=1)
            start_date = yesterday.strftime('%Y/%m/%d')
            end_date = today.strftime('%Y/%m/%d')
        elif period == 'week':
            week_ago = today - timedelta(days=7)
            start_date = week_ago.strftime('%Y/%m/%d')
            end_date = None
        elif period == 'month':
            month_ago = today - timedelta(days=30)
            start_date = month_ago.strftime('%Y/%m/%d')
            end_date = None
        else:
            return {'success': False, 'error': f'Unknown period: {period}'}

        result = self.summarize_by_date_range(start_date, end_date, max_emails)

        if not result['success']:
            return result

        # Build digest
        summaries = result['summaries']

        # Group by type
        by_type = {}
        for s in summaries:
            t = s['type']
            if t not in by_type:
                by_type[t] = []
            by_type[t].append(s)

        # Build digest text
        digest_lines = [
            f"# Email Digest: {period.capitalize()}",
            f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
            f"\nTotal Emails: {len(summaries)}",
            ""
        ]

        # Add urgent first
        if 'urgent' in by_type:
            digest_lines.append("## 🚨 Urgent")
            for s in by_type['urgent']:
                digest_lines.append(f"- **{s['subject']}** from {s['sender_name']}")
            digest_lines.append("")

        # Add needs response
        needs_response = [s for s in summaries if s['needs_response']]
        if needs_response:
            digest_lines.append("## ⚠️ May Need Response")
            for s in needs_response[:5]:
                digest_lines.append(f"- **{s['subject']}** from {s['sender_name']}")
            digest_lines.append("")

        # Add by category
        for category, items in by_type.items():
            if category != 'urgent':
                type_icons = {
                    'financial': '💰', 'meeting': '📅', 'newsletter': '📰',
                    'order': '📦', 'general': '📧'
                }
                icon = type_icons.get(category, '📧')
                digest_lines.append(f"## {icon} {category.capitalize()} ({len(items)})")
                for s in items[:5]:
                    digest_lines.append(f"- {s['subject']} ({s['sender_name']})")
                if len(items) > 5:
                    digest_lines.append(f"  *...and {len(items) - 5} more*")
                digest_lines.append("")

        digest_text = '\n'.join(digest_lines)

        return {
            'success': True,
            'digest': digest_text,
            'period': period,
            'email_count': len(summaries),
            'summaries': summaries,
            'statistics': {
                'by_type': {k: len(v) for k, v in by_type.items()},
                'needs_response': len(needs_response)
            }
        }

    def export_summary(
        self,
        summaries: List[Dict],
        format: str = 'markdown',
        filename: Optional[str] = None
    ) -> str:
        """
        Export summaries to a file.

        Args:
            summaries: List of summary dicts
            format: 'markdown', 'json', or 'text'
            filename: Output filename

        Returns:
            Path to saved file
        """
        output_dir = self.base_dir / 'output' / 'reports'
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        if not filename:
            filename = f"email_summary_{timestamp}"

        if format == 'markdown':
            content = "# Email Summary Report\n\n"
            content += f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"

            for i, s in enumerate(summaries, 1):
                content += f"## {i}. {s['subject']}\n"
                content += f"- **From:** {s['from']}\n"
                content += f"- **Date:** {s['date']}\n"
                content += f"- **Type:** {s['type']}\n"
                if s['needs_response']:
                    content += "- **⚠️ May need response**\n"
                content += f"\n{s['details'].get('snippet', '')}...\n\n---\n\n"

            filepath = output_dir / f"{filename}.md"
            filepath.write_text(content, encoding='utf-8')

        elif format == 'json':
            filepath = output_dir / f"{filename}.json"
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump({
                    'generated': datetime.now().isoformat(),
                    'count': len(summaries),
                    'summaries': summaries
                }, f, indent=2, ensure_ascii=False)

        else:  # text
            content = "EMAIL SUMMARY REPORT\n"
            content += "=" * 50 + "\n\n"

            for i, s in enumerate(summaries, 1):
                content += f"{i}. {s['subject']}\n"
                content += f"   From: {s['sender_name']}\n"
                content += f"   Date: {s['date']}\n"
                content += f"   Type: {s['type']}\n"
                content += f"   {s['details'].get('snippet', '')[:100]}...\n\n"

            filepath = output_dir / f"{filename}.txt"
            filepath.write_text(content, encoding='utf-8')

        return str(filepath)


def display_summaries(summaries: List[Dict]):
    """Display summaries in console."""
    type_icons = {
        'financial': '💰', 'meeting': '📅', 'urgent': '🚨',
        'newsletter': '📰', 'order': '📦', 'general': '📧'
    }

    for s in summaries:
        icon = type_icons.get(s['type'], '📧')
        status = "[yellow]NEEDS RESPONSE[/yellow]" if s['needs_response'] else ""

        console.print(Panel(
            f"[bold]{s['subject']}[/bold]\n"
            f"From: {s['sender_name']} | {s['date']}\n"
            f"Type: {icon} {s['type']} {status}\n\n"
            f"{s['details'].get('snippet', '')}...",
            title=f"Email {s['id'][:8]}..."
        ))


# CLI
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Email Summarizer')
    parser.add_argument('--summarize', type=int, metavar='N', help='Summarize N recent emails')
    parser.add_argument('--unread', action='store_true', help='Summarize unread only')
    parser.add_argument('--digest', choices=['today', 'yesterday', 'week', 'month'],
                        help='Generate digest for period')
    parser.add_argument('--search', metavar='QUERY', help='Summarize search results')
    parser.add_argument('--export', choices=['markdown', 'json', 'text'], help='Export format')

    args = parser.parse_args()

    summarizer = EmailSummarizer()

    if not summarizer.authenticate():
        console.print("[red]Authentication failed[/red]")
        sys.exit(1)

    if args.digest:
        result = summarizer.generate_digest(args.digest)
        if result['success']:
            console.print(Markdown(result['digest']))
            if args.export:
                path = summarizer.export_summary(
                    result['summaries'], args.export,
                    f"digest_{args.digest}"
                )
                console.print(f"\n[green]Exported to: {path}[/green]")

    elif args.summarize:
        result = summarizer.summarize_multiple(
            max_emails=args.summarize,
            unread_only=args.unread
        )
        if result['success']:
            console.print(f"\n[bold]Summarized {result['count']} emails[/bold]")
            console.print(f"Statistics: {result['statistics']}\n")
            display_summaries(result['summaries'])
            if args.export:
                path = summarizer.export_summary(result['summaries'], args.export)
                console.print(f"\n[green]Exported to: {path}[/green]")

    elif args.search:
        result = summarizer.summarize_multiple(query=args.search)
        if result['success']:
            console.print(f"\n[bold]Found {result['count']} emails matching: {args.search}[/bold]\n")
            display_summaries(result['summaries'])

    else:
        parser.print_help()
