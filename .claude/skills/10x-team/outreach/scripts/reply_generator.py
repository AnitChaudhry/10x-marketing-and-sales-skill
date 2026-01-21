#!/usr/bin/env python3
"""
Reply Generator for 10x-Outreach-Skill
Generate, preview, and send email replies with approval workflow
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
    from rich.panel import Panel
    from rich.prompt import Prompt, Confirm
    from rich.markdown import Markdown
    from jinja2 import Template
except ImportError as e:
    print(f"[X] Missing dependency: {e}")
    sys.exit(1)

from gmail_client import GmailClient
from inbox_reader import InboxReader

load_dotenv(Path(__file__).parent.parent / '.env')
console = Console()


class ReplyGenerator:
    """
    Email Reply Generator with approval workflow.

    Workflow:
    1. ANALYZE - Read and understand the original email
    2. DRAFT - Generate a reply draft
    3. PREVIEW - Show draft to user for approval
    4. APPROVE - User approves/edits the draft
    5. SEND - Send the approved reply
    """

    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.gmail_client = GmailClient()
        self.inbox_reader = InboxReader()
        self.sender_name = os.getenv('SENDER_NAME', '')

        # Reply templates
        self.reply_templates = {
            'acknowledge': """Hi {{ sender_name }},

Thank you for your email regarding "{{ subject }}".

I have received your message and will get back to you shortly.

Best regards,
{{ my_name }}""",

            'confirm': """Hi {{ sender_name }},

Thank you for reaching out.

I confirm receipt of your email about "{{ subject }}". {{ custom_message }}

Please let me know if you need anything else.

Best regards,
{{ my_name }}""",

            'decline': """Hi {{ sender_name }},

Thank you for your email regarding "{{ subject }}".

{{ custom_message }}

I appreciate your understanding.

Best regards,
{{ my_name }}""",

            'followup': """Hi {{ sender_name }},

I wanted to follow up on your previous email about "{{ subject }}".

{{ custom_message }}

Looking forward to hearing from you.

Best regards,
{{ my_name }}""",

            'custom': """Hi {{ sender_name }},

{{ custom_message }}

Best regards,
{{ my_name }}"""
        }

    def authenticate(self) -> bool:
        """Authenticate with Gmail."""
        return self.gmail_client.authenticate() and self.inbox_reader.authenticate()

    def analyze_email(self, message_id: str) -> Dict[str, Any]:
        """
        Analyze an email for reply generation.

        Args:
            message_id: Gmail message ID

        Returns:
            Dict with analysis results
        """
        console.print("\n[bold cyan]Step 1/5: ANALYZE[/bold cyan] - Reading original email...")

        result = self.inbox_reader.get_email(message_id)

        if not result['success']:
            return result

        email = result['email']

        # Extract sender info
        from_field = email.get('from', '')
        sender_email = ''
        sender_name = ''

        if '<' in from_field:
            sender_name = from_field.split('<')[0].strip().strip('"')
            sender_email = from_field.split('<')[1].rstrip('>')
        else:
            sender_email = from_field
            sender_name = from_field.split('@')[0]

        # Analyze content
        body = email.get('body', email.get('snippet', ''))
        subject = email.get('subject', '')

        # Detect tone and intent
        body_lower = body.lower()
        analysis = {
            'is_question': '?' in body,
            'is_request': any(w in body_lower for w in ['please', 'could you', 'can you', 'would you']),
            'is_urgent': any(w in body_lower for w in ['urgent', 'asap', 'immediately']),
            'is_followup': any(w in body_lower for w in ['follow up', 'checking in', 'reminder']),
            'mentions_meeting': any(w in body_lower for w in ['meeting', 'call', 'schedule']),
            'mentions_deadline': any(w in body_lower for w in ['deadline', 'due', 'by end of']),
        }

        # Suggest reply type
        if analysis['is_urgent'] or analysis['is_request']:
            suggested_type = 'confirm'
        elif analysis['is_question']:
            suggested_type = 'custom'
        elif analysis['is_followup']:
            suggested_type = 'followup'
        else:
            suggested_type = 'acknowledge'

        return {
            'success': True,
            'original_email': {
                'id': message_id,
                'from': from_field,
                'sender_email': sender_email,
                'sender_name': sender_name,
                'subject': subject,
                'date': email.get('date_formatted', ''),
                'body': body,
                'thread_id': email.get('thread_id')
            },
            'analysis': analysis,
            'suggested_reply_type': suggested_type
        }

    def generate_draft(
        self,
        original_email: Dict,
        reply_type: str = 'acknowledge',
        custom_message: str = '',
        include_original: bool = True
    ) -> Dict[str, Any]:
        """
        Generate a reply draft.

        Args:
            original_email: Original email dict
            reply_type: Type of reply template
            custom_message: Custom message content
            include_original: Include original email in reply

        Returns:
            Dict with draft content
        """
        console.print("\n[bold cyan]Step 2/5: DRAFT[/bold cyan] - Generating reply...")

        template_str = self.reply_templates.get(reply_type, self.reply_templates['custom'])
        template = Template(template_str)

        # Render template
        reply_body = template.render(
            sender_name=original_email['sender_name'],
            subject=original_email['subject'],
            custom_message=custom_message,
            my_name=self.sender_name
        )

        # Add original email if requested
        if include_original:
            reply_body += f"\n\n---\nOn {original_email['date']}, {original_email['from']} wrote:\n"
            reply_body += f"> {original_email['body'][:500]}..."

        # Generate subject
        orig_subject = original_email['subject']
        if not orig_subject.lower().startswith('re:'):
            reply_subject = f"Re: {orig_subject}"
        else:
            reply_subject = orig_subject

        draft = {
            'to': original_email['sender_email'],
            'subject': reply_subject,
            'body': reply_body,
            'reply_type': reply_type,
            'thread_id': original_email.get('thread_id')
        }

        return {
            'success': True,
            'draft': draft,
            'original_email': original_email
        }

    def preview_draft(self, draft: Dict) -> None:
        """
        Display draft for user preview.

        Args:
            draft: Draft dict with to, subject, body
        """
        console.print("\n[bold cyan]Step 3/5: PREVIEW[/bold cyan] - Review the draft reply...\n")

        console.print(Panel(
            f"[bold]To:[/bold] {draft['to']}\n"
            f"[bold]Subject:[/bold] {draft['subject']}\n"
            f"[bold]Type:[/bold] {draft['reply_type']}\n\n"
            f"[bold]Body:[/bold]\n{draft['body']}",
            title="📧 Draft Reply",
            border_style="cyan"
        ))

    def get_approval(self, draft: Dict) -> Dict[str, Any]:
        """
        Get user approval for the draft.

        Args:
            draft: Draft dict

        Returns:
            Dict with approval status and possibly edited draft
        """
        console.print("\n[bold cyan]Step 4/5: APPROVE[/bold cyan] - Confirm or edit the draft...\n")

        console.print("[bold]Options:[/bold]")
        console.print("  1. Send as-is")
        console.print("  2. Edit message")
        console.print("  3. Change reply type")
        console.print("  4. Cancel")

        choice = Prompt.ask("Choose option", choices=["1", "2", "3", "4"], default="1")

        if choice == "1":
            return {
                'approved': True,
                'draft': draft,
                'action': 'send'
            }

        elif choice == "2":
            console.print("\n[i] Enter your custom message (press Enter twice when done):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            custom_body = '\n'.join(lines)

            draft['body'] = custom_body
            return {
                'approved': True,
                'draft': draft,
                'action': 'send',
                'edited': True
            }

        elif choice == "3":
            console.print("\n[bold]Reply types:[/bold]")
            for t in self.reply_templates.keys():
                console.print(f"  - {t}")
            new_type = Prompt.ask("Choose type", default="custom")
            return {
                'approved': False,
                'action': 'regenerate',
                'new_type': new_type
            }

        else:
            return {
                'approved': False,
                'action': 'cancel'
            }

    def send_reply(self, draft: Dict, dry_run: bool = False) -> Dict[str, Any]:
        """
        Send the approved reply.

        Args:
            draft: Approved draft dict
            dry_run: Simulate without sending

        Returns:
            Dict with send result
        """
        console.print("\n[bold cyan]Step 5/5: SEND[/bold cyan] - Sending reply...")

        if dry_run:
            console.print("[yellow]DRY RUN - Email not actually sent[/yellow]")
            return {
                'success': True,
                'dry_run': True,
                'message_id': 'DRY_RUN',
                'to': draft['to'],
                'subject': draft['subject']
            }

        result = self.gmail_client.send_email(
            to=draft['to'],
            subject=draft['subject'],
            body=draft['body']
        )

        if result['success']:
            console.print(f"[green]Reply sent successfully![/green]")
            console.print(f"Message ID: {result['message_id']}")

            # Log the sent reply
            self._log_reply(draft, result)

        else:
            console.print(f"[red]Failed to send: {result['error']}[/red]")

        return result

    def _log_reply(self, draft: Dict, result: Dict):
        """Log sent reply for records."""
        log_dir = self.base_dir / 'output' / 'sent' / 'replies'
        log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = log_dir / f"reply_{timestamp}.json"

        log_data = {
            'timestamp': datetime.now().isoformat(),
            'to': draft['to'],
            'subject': draft['subject'],
            'body': draft['body'],
            'message_id': result.get('message_id'),
            'thread_id': draft.get('thread_id')
        }

        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)

    def reply_workflow(
        self,
        message_id: str,
        reply_type: Optional[str] = None,
        custom_message: str = '',
        dry_run: bool = False,
        auto_approve: bool = False
    ) -> Dict[str, Any]:
        """
        Complete reply workflow with all steps.

        Args:
            message_id: ID of email to reply to
            reply_type: Reply template type (or auto-suggest)
            custom_message: Custom message content
            dry_run: Simulate without sending
            auto_approve: Skip approval step

        Returns:
            Dict with workflow result
        """
        console.print(Panel(
            "[bold]Email Reply Workflow[/bold]\n\n"
            "Steps:\n"
            "1. ANALYZE - Read original email\n"
            "2. DRAFT - Generate reply\n"
            "3. PREVIEW - Review draft\n"
            "4. APPROVE - Confirm or edit\n"
            "5. SEND - Send reply",
            title="🔄 Workflow",
            border_style="blue"
        ))

        # Step 1: Analyze
        analysis = self.analyze_email(message_id)
        if not analysis['success']:
            return analysis

        original_email = analysis['original_email']

        console.print(Panel(
            f"[bold]From:[/bold] {original_email['from']}\n"
            f"[bold]Subject:[/bold] {original_email['subject']}\n"
            f"[bold]Date:[/bold] {original_email['date']}\n\n"
            f"[bold]Content:[/bold]\n{original_email['body'][:500]}...",
            title="📨 Original Email"
        ))

        console.print(f"\n[i] Analysis: {analysis['analysis']}")
        console.print(f"[i] Suggested reply type: {analysis['suggested_reply_type']}")

        # Use suggested type or provided type
        if not reply_type:
            reply_type = analysis['suggested_reply_type']

        # Step 2: Generate draft
        draft_result = self.generate_draft(
            original_email,
            reply_type=reply_type,
            custom_message=custom_message
        )

        if not draft_result['success']:
            return draft_result

        draft = draft_result['draft']

        # Step 3: Preview
        self.preview_draft(draft)

        # Step 4: Approval
        if auto_approve:
            console.print("\n[yellow]Auto-approve enabled - skipping approval[/yellow]")
            approval = {'approved': True, 'draft': draft, 'action': 'send'}
        else:
            approval = self.get_approval(draft)

        if approval['action'] == 'cancel':
            console.print("\n[yellow]Reply cancelled by user[/yellow]")
            return {'success': False, 'cancelled': True}

        if approval['action'] == 'regenerate':
            # Regenerate with new type
            return self.reply_workflow(
                message_id,
                reply_type=approval.get('new_type', 'custom'),
                custom_message=custom_message,
                dry_run=dry_run
            )

        if not approval['approved']:
            return {'success': False, 'reason': 'Not approved'}

        # Step 5: Send
        final_draft = approval.get('draft', draft)
        return self.send_reply(final_draft, dry_run=dry_run)

    def save_as_draft(self, draft: Dict) -> Dict[str, Any]:
        """
        Save reply as Gmail draft instead of sending.

        Args:
            draft: Draft dict

        Returns:
            Dict with draft save result
        """
        console.print("\n[i] Saving as draft...")

        result = self.gmail_client.create_draft(
            to=draft['to'],
            subject=draft['subject'],
            body=draft['body']
        )

        if result['success']:
            console.print(f"[green]Draft saved![/green]")
            console.print(f"Draft ID: {result['draft_id']}")
        else:
            console.print(f"[red]Failed to save draft: {result['error']}[/red]")

        return result


# CLI
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Email Reply Generator')
    parser.add_argument('--reply', metavar='MSG_ID', help='Reply to email by message ID')
    parser.add_argument('--type', choices=['acknowledge', 'confirm', 'decline', 'followup', 'custom'],
                        help='Reply type')
    parser.add_argument('--message', help='Custom message content')
    parser.add_argument('--dry-run', action='store_true', help='Simulate without sending')
    parser.add_argument('--save-draft', action='store_true', help='Save as draft instead of sending')

    args = parser.parse_args()

    generator = ReplyGenerator()

    if not generator.authenticate():
        console.print("[red]Authentication failed[/red]")
        sys.exit(1)

    if args.reply:
        result = generator.reply_workflow(
            message_id=args.reply,
            reply_type=args.type,
            custom_message=args.message or '',
            dry_run=args.dry_run
        )

        if args.save_draft and result.get('success'):
            # Save as draft instead
            draft = result.get('draft', {})
            if draft:
                generator.save_as_draft(draft)
    else:
        parser.print_help()
