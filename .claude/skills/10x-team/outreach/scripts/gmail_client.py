#!/usr/bin/env python3
"""
Gmail API Client for 10x-Outreach-Skill
Handles OAuth2 authentication and email sending via Gmail API
"""

import os
import sys
import base64
import json
import pickle
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import Optional, Dict, List, Any

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from dotenv import load_dotenv
except ImportError as e:
    print(f"[X] Missing dependency: {e}")
    print("    Run: pip install -r requirements.txt")
    sys.exit(1)

# Load environment variables
load_dotenv(Path(__file__).parent.parent / '.env')

# Gmail API scopes - only request what's needed
SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',           # Send emails
    'https://www.googleapis.com/auth/gmail.compose',        # Create drafts
    'https://www.googleapis.com/auth/gmail.readonly',       # Read emails (for verification)
]


class GmailClient:
    """
    Gmail API Client for sending emails programmatically.

    Uses OAuth2 for authentication - safer than app passwords.
    Supports:
    - Sending plain text and HTML emails
    - Attachments
    - Draft creation
    - Rate limiting
    """

    def __init__(self, credentials_path: Optional[str] = None, token_path: Optional[str] = None):
        """
        Initialize Gmail client.

        Args:
            credentials_path: Path to OAuth2 credentials JSON file
            token_path: Path to store/load access tokens
        """
        self.base_dir = Path(__file__).parent.parent
        self.credentials_path = credentials_path or self.base_dir / 'credentials' / 'credentials.json'
        self.token_path = token_path or self.base_dir / 'credentials' / 'token.pickle'

        self.sender_email = os.getenv('SENDER_EMAIL', '')
        self.sender_name = os.getenv('SENDER_NAME', '')

        self.service = None
        self.creds = None

    def _create_credentials_from_env(self) -> Dict:
        """Create credentials dict from environment variables."""
        client_id = os.getenv('GOOGLE_CLIENT_ID')
        client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
        redirect_uri = os.getenv('GOOGLE_REDIRECT_URI', 'http://localhost:8080/oauth/callback')

        if not client_id or not client_secret:
            return None

        return {
            "installed": {
                "client_id": client_id,
                "client_secret": client_secret,
                "redirect_uris": [redirect_uri],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        }

    def authenticate(self, force_new: bool = False) -> bool:
        """
        Authenticate with Gmail API using OAuth2.

        Args:
            force_new: Force new authentication even if token exists

        Returns:
            True if authentication successful, False otherwise
        """
        self.creds = None

        # Try to load existing token
        if not force_new and Path(self.token_path).exists():
            try:
                with open(self.token_path, 'rb') as token:
                    self.creds = pickle.load(token)
                print("[i] Loaded existing credentials from token file")
            except Exception as e:
                print(f"[!] Could not load token: {e}")

        # Check if credentials are valid
        if self.creds and self.creds.valid:
            print("[OK] Credentials are valid")
        elif self.creds and self.creds.expired and self.creds.refresh_token:
            # Refresh expired credentials
            try:
                print("[i] Refreshing expired credentials...")
                self.creds.refresh(Request())
                print("[OK] Credentials refreshed")
            except Exception as e:
                print(f"[X] Failed to refresh credentials: {e}")
                self.creds = None

        # Need new authentication
        if not self.creds:
            print("[i] Starting new OAuth2 flow...")

            # Try credentials file first, then environment variables
            if Path(self.credentials_path).exists():
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_path), SCOPES
                )
            else:
                # Create from environment variables
                creds_dict = self._create_credentials_from_env()
                if not creds_dict:
                    print("[X] No credentials found!")
                    print("    Either:")
                    print("    1. Place credentials.json in credentials/ folder")
                    print("    2. Set GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET in .env")
                    return False

                flow = InstalledAppFlow.from_client_config(creds_dict, SCOPES)

            # Run local server for OAuth callback
            try:
                self.creds = flow.run_local_server(port=8080)
                print("[OK] Authentication successful!")
            except Exception as e:
                print(f"[X] OAuth flow failed: {e}")
                return False

        # Save credentials for future use
        try:
            Path(self.token_path).parent.mkdir(parents=True, exist_ok=True)
            with open(self.token_path, 'wb') as token:
                pickle.dump(self.creds, token)
            print(f"[OK] Token saved to {self.token_path}")
        except Exception as e:
            print(f"[!] Could not save token: {e}")

        # Build the Gmail service
        try:
            self.service = build('gmail', 'v1', credentials=self.creds)
            print("[OK] Gmail service initialized")
            return True
        except Exception as e:
            print(f"[X] Failed to build Gmail service: {e}")
            return False

    def get_user_info(self) -> Optional[Dict]:
        """Get authenticated user's email profile."""
        if not self.service:
            print("[X] Not authenticated. Call authenticate() first.")
            return None

        try:
            profile = self.service.users().getProfile(userId='me').execute()
            return {
                'email': profile.get('emailAddress'),
                'messages_total': profile.get('messagesTotal'),
                'threads_total': profile.get('threadsTotal'),
                'history_id': profile.get('historyId'),
            }
        except HttpError as e:
            print(f"[X] Failed to get user info: {e}")
            return None

    def create_message(
        self,
        to: str,
        subject: str,
        body: str,
        html_body: Optional[str] = None,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        reply_to: Optional[str] = None,
        attachments: Optional[List[str]] = None
    ) -> Dict:
        """
        Create an email message.

        Args:
            to: Recipient email address
            subject: Email subject
            body: Plain text body
            html_body: Optional HTML body
            cc: Optional CC recipients
            bcc: Optional BCC recipients
            reply_to: Optional reply-to address
            attachments: Optional list of file paths to attach

        Returns:
            Message dict ready to send
        """
        # Determine sender
        if self.sender_name:
            sender = f"{self.sender_name} <{self.sender_email}>"
        else:
            sender = self.sender_email

        if html_body or attachments:
            # Create multipart message
            message = MIMEMultipart('alternative')
            message['to'] = to
            message['from'] = sender
            message['subject'] = subject

            if cc:
                message['cc'] = ', '.join(cc)
            if bcc:
                message['bcc'] = ', '.join(bcc)
            if reply_to:
                message['reply-to'] = reply_to

            # Attach plain text
            message.attach(MIMEText(body, 'plain'))

            # Attach HTML if provided
            if html_body:
                message.attach(MIMEText(html_body, 'html'))

            # Attach files
            if attachments:
                for file_path in attachments:
                    self._attach_file(message, file_path)
        else:
            # Simple plain text message
            message = MIMEText(body)
            message['to'] = to
            message['from'] = sender
            message['subject'] = subject

            if cc:
                message['cc'] = ', '.join(cc)
            if bcc:
                message['bcc'] = ', '.join(bcc)
            if reply_to:
                message['reply-to'] = reply_to

        # Encode message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        return {'raw': raw_message}

    def _attach_file(self, message: MIMEMultipart, file_path: str):
        """Attach a file to the message."""
        path = Path(file_path)
        if not path.exists():
            print(f"[!] Attachment not found: {file_path}")
            return

        with open(path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())

        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename="{path.name}"'
        )
        message.attach(part)

    def send_email(
        self,
        to: str,
        subject: str,
        body: str,
        html_body: Optional[str] = None,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        reply_to: Optional[str] = None,
        attachments: Optional[List[str]] = None,
        dry_run: bool = False
    ) -> Dict[str, Any]:
        """
        Send an email via Gmail API.

        Args:
            to: Recipient email address
            subject: Email subject
            body: Plain text body
            html_body: Optional HTML body
            cc: Optional CC recipients
            bcc: Optional BCC recipients
            reply_to: Optional reply-to address
            attachments: Optional list of file paths
            dry_run: If True, don't actually send

        Returns:
            Dict with 'success', 'message_id', 'error' keys
        """
        if not self.service:
            return {
                'success': False,
                'error': 'Not authenticated. Call authenticate() first.',
                'message_id': None
            }

        try:
            message = self.create_message(
                to=to,
                subject=subject,
                body=body,
                html_body=html_body,
                cc=cc,
                bcc=bcc,
                reply_to=reply_to,
                attachments=attachments
            )

            if dry_run:
                return {
                    'success': True,
                    'message_id': 'DRY_RUN',
                    'to': to,
                    'subject': subject,
                    'dry_run': True
                }

            # Send the message
            result = self.service.users().messages().send(
                userId='me',
                body=message
            ).execute()

            return {
                'success': True,
                'message_id': result.get('id'),
                'thread_id': result.get('threadId'),
                'to': to,
                'subject': subject
            }

        except HttpError as e:
            error_details = json.loads(e.content.decode())
            return {
                'success': False,
                'error': error_details.get('error', {}).get('message', str(e)),
                'status_code': e.resp.status,
                'to': to,
                'message_id': None
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'to': to,
                'message_id': None
            }

    def create_draft(
        self,
        to: str,
        subject: str,
        body: str,
        html_body: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a draft email.

        Args:
            to: Recipient email
            subject: Email subject
            body: Plain text body
            html_body: Optional HTML body

        Returns:
            Dict with 'success', 'draft_id', 'error' keys
        """
        if not self.service:
            return {
                'success': False,
                'error': 'Not authenticated',
                'draft_id': None
            }

        try:
            message = self.create_message(to, subject, body, html_body)
            draft = self.service.users().drafts().create(
                userId='me',
                body={'message': message}
            ).execute()

            return {
                'success': True,
                'draft_id': draft.get('id'),
                'message_id': draft.get('message', {}).get('id')
            }
        except HttpError as e:
            return {
                'success': False,
                'error': str(e),
                'draft_id': None
            }


def get_client() -> GmailClient:
    """Factory function to get an authenticated Gmail client."""
    client = GmailClient()
    return client


# CLI for testing
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Gmail Client CLI')
    parser.add_argument('--auth', action='store_true', help='Authenticate with Gmail')
    parser.add_argument('--info', action='store_true', help='Show user info')
    parser.add_argument('--send', nargs=2, metavar=('TO', 'SUBJECT'), help='Send test email')

    args = parser.parse_args()

    client = GmailClient()

    if args.auth:
        success = client.authenticate(force_new=True)
        if success:
            info = client.get_user_info()
            if info:
                print(f"\n[OK] Authenticated as: {info['email']}")

    elif args.info:
        if client.authenticate():
            info = client.get_user_info()
            if info:
                print(f"\nEmail: {info['email']}")
                print(f"Messages: {info['messages_total']}")
                print(f"Threads: {info['threads_total']}")

    elif args.send:
        to, subject = args.send
        if client.authenticate():
            result = client.send_email(
                to=to,
                subject=subject,
                body=f"This is a test email sent via 10x-Outreach-Skill.\n\nRegards,\n{client.sender_name}"
            )
            if result['success']:
                print(f"[OK] Email sent! Message ID: {result['message_id']}")
            else:
                print(f"[X] Failed: {result['error']}")

    else:
        parser.print_help()
