#!/usr/bin/env python3
"""
Campaign Email Sender for 10x-Outreach-Skill
Sends emails to recipients with rate limiting and logging
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from dotenv import load_dotenv
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
    from rich.table import Table
    from rich.panel import Panel
    from jinja2 import Template, Environment, FileSystemLoader
except ImportError as e:
    print(f"[X] Missing dependency: {e}")
    sys.exit(1)

from gmail_client import GmailClient
from sheets_reader import SheetsReader

load_dotenv(Path(__file__).parent.parent / '.env')
console = Console()


class CampaignSender:
    """
    Orchestrates sending email campaigns with:
    - Rate limiting (configurable delay between emails)
    - Template rendering with personalization
    - Progress tracking and logging
    - Dry run mode for testing
    """

    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.gmail = GmailClient()
        self.sheets = SheetsReader()

        # Configuration from environment
        self.delay_seconds = int(os.getenv('EMAIL_DELAY_SECONDS', 60))
        self.max_per_batch = int(os.getenv('MAX_EMAILS_PER_BATCH', 50))
        self.daily_limit = int(os.getenv('DAILY_EMAIL_LIMIT', 100))
        self.dry_run = os.getenv('DRY_RUN_MODE', 'false').lower() == 'true'
        self.save_copies = os.getenv('SAVE_SENT_COPIES', 'true').lower() == 'true'

        # Template environment
        self.template_env = Environment(
            loader=FileSystemLoader(self.base_dir / 'templates'),
            autoescape=True
        )

        # Tracking
        self.sent_count = 0
        self.failed_count = 0
        self.campaign_log = []

    def load_template(self, template_path: str) -> Optional[Dict[str, Template]]:
        """
        Load an email template.

        Template files should have format:
        ---
        subject: Your Subject with {{ name }}
        ---
        Body content with {{ variables }}

        Or just body content (subject provided separately).
        """
        full_path = self.base_dir / 'templates' / template_path

        if not full_path.exists():
            console.print(f"[red]Template not found: {template_path}[/red]")
            return None

        content = full_path.read_text(encoding='utf-8')

        # Check for frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                # Parse frontmatter
                frontmatter = parts[1].strip()
                body = parts[2].strip()

                subject = None
                for line in frontmatter.split('\n'):
                    if line.startswith('subject:'):
                        subject = line.split(':', 1)[1].strip()

                return {
                    'subject': Template(subject) if subject else None,
                    'body': Template(body),
                    'is_html': template_path.endswith('.html')
                }

        # No frontmatter, just body
        return {
            'subject': None,
            'body': Template(content),
            'is_html': template_path.endswith('.html')
        }

    def render_email(
        self,
        template: Dict[str, Template],
        recipient: Dict[str, str],
        default_subject: str = "Hello"
    ) -> Dict[str, str]:
        """
        Render an email template with recipient data.

        Args:
            template: Template dict from load_template()
            recipient: Dict with recipient data (email, name, etc.)
            default_subject: Subject to use if not in template

        Returns:
            Dict with 'subject', 'body', 'html_body' keys
        """
        # Merge recipient data with defaults
        context = {
            'email': recipient.get('email', ''),
            'name': recipient.get('name', recipient.get('email', '').split('@')[0]),
            'first_name': recipient.get('name', '').split()[0] if recipient.get('name') else '',
            'company': recipient.get('company', ''),
            **recipient  # Include all other fields
        }

        # Render subject
        if template['subject']:
            subject = template['subject'].render(**context)
        else:
            subject = default_subject

        # Render body
        body = template['body'].render(**context)

        result = {
            'subject': subject,
            'body': body if not template['is_html'] else '',
            'html_body': body if template['is_html'] else None
        }

        return result

    def send_campaign(
        self,
        recipients: List[Dict],
        template_path: str,
        subject: Optional[str] = None,
        dry_run: Optional[bool] = None,
        delay: Optional[int] = None,
        max_emails: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Send emails to a list of recipients.

        Args:
            recipients: List of recipient dicts with 'email' key
            template_path: Path to template file (relative to templates/)
            subject: Default subject if not in template
            dry_run: Override dry run setting
            delay: Override delay between emails
            max_emails: Override max emails to send

        Returns:
            Campaign result summary
        """
        dry_run = dry_run if dry_run is not None else self.dry_run
        delay = delay if delay is not None else self.delay_seconds
        max_emails = max_emails if max_emails is not None else self.max_per_batch

        # Load template
        template = self.load_template(template_path)
        if not template:
            return {'success': False, 'error': 'Template not found'}

        # Authenticate
        if not self.gmail.authenticate():
            return {'success': False, 'error': 'Gmail authentication failed'}

        # Limit recipients
        recipients = recipients[:max_emails]
        total = len(recipients)

        console.print(Panel(
            f"[bold]Campaign: {template_path}[/bold]\n\n"
            f"Recipients: {total}\n"
            f"Delay: {delay}s between emails\n"
            f"Mode: {'[yellow]DRY RUN[/yellow]' if dry_run else '[green]LIVE[/green]'}",
            title="Starting Campaign"
        ))

        # Campaign metadata
        campaign_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.campaign_log = []
        self.sent_count = 0
        self.failed_count = 0

        # Send emails with progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task = progress.add_task("Sending emails...", total=total)

            for i, recipient in enumerate(recipients):
                email = recipient.get('email', '')
                name = recipient.get('name', email.split('@')[0])

                progress.update(task, description=f"Sending to {name}...")

                # Render email
                rendered = self.render_email(template, recipient, subject or "Hello")

                # Send
                result = self.gmail.send_email(
                    to=email,
                    subject=rendered['subject'],
                    body=rendered['body'],
                    html_body=rendered['html_body'],
                    dry_run=dry_run
                )

                # Log result
                log_entry = {
                    'timestamp': datetime.now().isoformat(),
                    'email': email,
                    'name': name,
                    'subject': rendered['subject'],
                    'success': result['success'],
                    'message_id': result.get('message_id'),
                    'error': result.get('error'),
                    'dry_run': dry_run
                }
                self.campaign_log.append(log_entry)

                if result['success']:
                    self.sent_count += 1
                    if not dry_run:
                        console.print(f"  [green]OK[/green] {email}")
                else:
                    self.failed_count += 1
                    console.print(f"  [red]FAILED[/red] {email}: {result.get('error')}")

                progress.update(task, advance=1)

                # Delay between emails (except for last one)
                if i < total - 1 and not dry_run:
                    progress.update(task, description=f"Waiting {delay}s...")
                    time.sleep(delay)

        # Save campaign log
        self._save_campaign_log(campaign_id)

        # Summary
        summary = {
            'success': True,
            'campaign_id': campaign_id,
            'total': total,
            'sent': self.sent_count,
            'failed': self.failed_count,
            'dry_run': dry_run,
            'template': template_path,
            'log_file': f'output/logs/campaign_{campaign_id}.json'
        }

        console.print("\n" + "="*50)
        console.print(Panel(
            f"[bold]Campaign Complete[/bold]\n\n"
            f"Total: {total}\n"
            f"Sent: [green]{self.sent_count}[/green]\n"
            f"Failed: [red]{self.failed_count}[/red]\n"
            f"Mode: {'DRY RUN' if dry_run else 'LIVE'}\n\n"
            f"Log: {summary['log_file']}",
            title=f"Campaign {campaign_id}"
        ))

        return summary

    def send_from_sheet(
        self,
        spreadsheet_id: str,
        template_path: str,
        sheet_name: str = 'Sheet1',
        subject: Optional[str] = None,
        email_column: str = 'email',
        filters: Optional[Dict] = None,
        dry_run: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        Send campaign using recipients from a Google Sheet.

        Args:
            spreadsheet_id: Google Sheet ID
            template_path: Path to email template
            sheet_name: Name of the sheet to read
            subject: Default subject
            email_column: Name of email column
            filters: Optional filters for recipients
            dry_run: Override dry run mode

        Returns:
            Campaign result
        """
        # Authenticate with Sheets
        if not self.sheets.authenticate():
            return {'success': False, 'error': 'Sheets authentication failed'}

        # Get recipients
        console.print(f"[i] Reading recipients from sheet...")
        result = self.sheets.get_recipients(
            spreadsheet_id=spreadsheet_id,
            range_name=sheet_name,
            email_column=email_column,
            filters=filters
        )

        if not result['success']:
            return result

        recipients = result['recipients']
        console.print(f"[OK] Found {len(recipients)} recipients")

        if not recipients:
            return {'success': False, 'error': 'No recipients found'}

        # Show preview
        console.print("\n[bold]Preview (first 3):[/bold]")
        table = Table()
        for col in result['headers'][:5]:
            table.add_column(col)
        for r in recipients[:3]:
            table.add_row(*[str(r.get(h, ''))[:30] for h in result['headers'][:5]])
        console.print(table)

        # Send campaign
        return self.send_campaign(
            recipients=recipients,
            template_path=template_path,
            subject=subject,
            dry_run=dry_run
        )

    def _save_campaign_log(self, campaign_id: str):
        """Save campaign log to file."""
        log_dir = self.base_dir / 'output' / 'logs'
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f'campaign_{campaign_id}.json'

        log_data = {
            'campaign_id': campaign_id,
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total': len(self.campaign_log),
                'sent': self.sent_count,
                'failed': self.failed_count
            },
            'entries': self.campaign_log
        }

        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)

        # Also save sent emails for reference
        if self.save_copies:
            sent_dir = self.base_dir / 'output' / 'sent' / campaign_id
            sent_dir.mkdir(parents=True, exist_ok=True)

            for entry in self.campaign_log:
                if entry['success']:
                    email_file = sent_dir / f"{entry['email'].replace('@', '_at_')}.json"
                    with open(email_file, 'w', encoding='utf-8') as f:
                        json.dump(entry, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description='Campaign Email Sender')
    parser.add_argument('--sheet', metavar='SHEET_ID', help='Google Sheet ID with recipients')
    parser.add_argument('--template', required=True, help='Template file path (e.g., outreach/cold.txt)')
    parser.add_argument('--subject', help='Email subject (if not in template)')
    parser.add_argument('--sheet-name', default='Sheet1', help='Sheet name to read')
    parser.add_argument('--email-column', default='email', help='Email column name')
    parser.add_argument('--delay', type=int, help='Delay between emails in seconds')
    parser.add_argument('--max', type=int, help='Maximum emails to send')
    parser.add_argument('--dry-run', action='store_true', help='Simulate without sending')
    parser.add_argument('--live', action='store_true', help='Actually send emails')

    args = parser.parse_args()

    sender = CampaignSender()

    # Override dry run
    dry_run = args.dry_run or (not args.live and sender.dry_run)

    if args.sheet:
        result = sender.send_from_sheet(
            spreadsheet_id=args.sheet,
            template_path=args.template,
            sheet_name=args.sheet_name,
            subject=args.subject,
            email_column=args.email_column,
            dry_run=dry_run
        )
    else:
        console.print("[red]Please provide --sheet with Google Sheet ID[/red]")
        return False

    return result.get('success', False)


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
