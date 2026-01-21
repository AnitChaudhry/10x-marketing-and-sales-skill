#!/usr/bin/env python3
"""
Google Sheets Reader for 10x-Outreach-Skill
Reads recipient data from Google Sheets for email campaigns
"""

import os
import sys
import json
import pickle
from pathlib import Path
from typing import Optional, Dict, List, Any

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from dotenv import load_dotenv
    import pandas as pd
except ImportError as e:
    print(f"[X] Missing dependency: {e}")
    print("    Run: pip install -r requirements.txt")
    sys.exit(1)

load_dotenv(Path(__file__).parent.parent / '.env')

# Scopes for Sheets API
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',  # Read sheets
]


class SheetsReader:
    """
    Google Sheets Reader for fetching recipient data.

    Expected sheet format:
    | email | name | company | custom_field_1 | ... |
    |-------|------|---------|----------------|-----|

    The first row is treated as headers.
    'email' column is required.
    """

    def __init__(self, credentials_path: Optional[str] = None, token_path: Optional[str] = None):
        """
        Initialize Sheets reader.

        Args:
            credentials_path: Path to OAuth2 credentials
            token_path: Path to token storage
        """
        self.base_dir = Path(__file__).parent.parent
        self.credentials_path = credentials_path or self.base_dir / 'credentials' / 'credentials.json'
        self.token_path = token_path or self.base_dir / 'credentials' / 'sheets_token.pickle'

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
        Authenticate with Google Sheets API.

        Args:
            force_new: Force new authentication

        Returns:
            True if successful
        """
        self.creds = None

        # Try to load existing token
        if not force_new and Path(self.token_path).exists():
            try:
                with open(self.token_path, 'rb') as token:
                    self.creds = pickle.load(token)
                print("[i] Loaded existing Sheets credentials")
            except Exception as e:
                print(f"[!] Could not load token: {e}")

        # Check if credentials are valid
        if self.creds and self.creds.valid:
            print("[OK] Sheets credentials are valid")
        elif self.creds and self.creds.expired and self.creds.refresh_token:
            try:
                print("[i] Refreshing Sheets credentials...")
                self.creds.refresh(Request())
                print("[OK] Credentials refreshed")
            except Exception as e:
                print(f"[X] Failed to refresh: {e}")
                self.creds = None

        # Need new authentication
        if not self.creds:
            print("[i] Starting Sheets OAuth2 flow...")

            if Path(self.credentials_path).exists():
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_path), SCOPES
                )
            else:
                creds_dict = self._create_credentials_from_env()
                if not creds_dict:
                    print("[X] No credentials found!")
                    return False
                flow = InstalledAppFlow.from_client_config(creds_dict, SCOPES)

            try:
                self.creds = flow.run_local_server(port=8081)
                print("[OK] Sheets authentication successful!")
            except Exception as e:
                print(f"[X] OAuth flow failed: {e}")
                return False

        # Save token
        try:
            Path(self.token_path).parent.mkdir(parents=True, exist_ok=True)
            with open(self.token_path, 'wb') as token:
                pickle.dump(self.creds, token)
        except Exception as e:
            print(f"[!] Could not save token: {e}")

        # Build service
        try:
            self.service = build('sheets', 'v4', credentials=self.creds)
            print("[OK] Sheets service initialized")
            return True
        except Exception as e:
            print(f"[X] Failed to build Sheets service: {e}")
            return False

    def read_sheet(
        self,
        spreadsheet_id: str,
        range_name: str = 'Sheet1',
        has_header: bool = True
    ) -> Dict[str, Any]:
        """
        Read data from a Google Sheet.

        Args:
            spreadsheet_id: The ID of the spreadsheet (from URL)
            range_name: Sheet name or A1 notation range
            has_header: Whether first row contains headers

        Returns:
            Dict with 'success', 'data', 'headers', 'row_count'
        """
        if not self.service:
            return {
                'success': False,
                'error': 'Not authenticated. Call authenticate() first.',
                'data': []
            }

        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=range_name
            ).execute()

            values = result.get('values', [])

            if not values:
                return {
                    'success': True,
                    'data': [],
                    'headers': [],
                    'row_count': 0,
                    'message': 'Sheet is empty'
                }

            if has_header:
                headers = values[0]
                data_rows = values[1:]

                # Convert to list of dicts
                data = []
                for row in data_rows:
                    # Pad row if shorter than headers
                    padded_row = row + [''] * (len(headers) - len(row))
                    data.append(dict(zip(headers, padded_row)))

                return {
                    'success': True,
                    'data': data,
                    'headers': headers,
                    'row_count': len(data),
                    'spreadsheet_id': spreadsheet_id
                }
            else:
                return {
                    'success': True,
                    'data': values,
                    'headers': None,
                    'row_count': len(values),
                    'spreadsheet_id': spreadsheet_id
                }

        except HttpError as e:
            error_content = json.loads(e.content.decode()) if e.content else {}
            return {
                'success': False,
                'error': error_content.get('error', {}).get('message', str(e)),
                'status_code': e.resp.status,
                'data': []
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'data': []
            }

    def get_recipients(
        self,
        spreadsheet_id: str,
        range_name: str = 'Sheet1',
        email_column: str = 'email',
        filters: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Get email recipients from a sheet.

        Args:
            spreadsheet_id: The spreadsheet ID
            range_name: Sheet name or range
            email_column: Name of the email column
            filters: Optional filters like {'status': 'pending'}

        Returns:
            Dict with recipients list and metadata
        """
        result = self.read_sheet(spreadsheet_id, range_name)

        if not result['success']:
            return result

        data = result['data']

        # Validate email column exists
        if email_column not in result['headers']:
            return {
                'success': False,
                'error': f"Email column '{email_column}' not found. Available: {result['headers']}",
                'data': []
            }

        # Apply filters
        if filters:
            filtered_data = []
            for row in data:
                match = all(row.get(k, '') == v for k, v in filters.items())
                if match:
                    filtered_data.append(row)
            data = filtered_data

        # Filter out rows without valid email
        recipients = [
            row for row in data
            if row.get(email_column) and '@' in row.get(email_column, '')
        ]

        return {
            'success': True,
            'recipients': recipients,
            'total_count': len(recipients),
            'headers': result['headers'],
            'email_column': email_column
        }

    def get_spreadsheet_info(self, spreadsheet_id: str) -> Dict[str, Any]:
        """Get metadata about a spreadsheet."""
        if not self.service:
            return {'success': False, 'error': 'Not authenticated'}

        try:
            spreadsheet = self.service.spreadsheets().get(
                spreadsheetId=spreadsheet_id
            ).execute()

            sheets = [
                {
                    'title': sheet['properties']['title'],
                    'sheet_id': sheet['properties']['sheetId'],
                    'row_count': sheet['properties']['gridProperties']['rowCount'],
                    'column_count': sheet['properties']['gridProperties']['columnCount']
                }
                for sheet in spreadsheet.get('sheets', [])
            ]

            return {
                'success': True,
                'title': spreadsheet.get('properties', {}).get('title'),
                'spreadsheet_id': spreadsheet_id,
                'sheets': sheets,
                'url': spreadsheet.get('spreadsheetUrl')
            }
        except HttpError as e:
            return {
                'success': False,
                'error': str(e)
            }

    def to_dataframe(
        self,
        spreadsheet_id: str,
        range_name: str = 'Sheet1'
    ) -> Optional[pd.DataFrame]:
        """
        Read sheet data into a pandas DataFrame.

        Args:
            spreadsheet_id: The spreadsheet ID
            range_name: Sheet name or range

        Returns:
            DataFrame or None if failed
        """
        result = self.read_sheet(spreadsheet_id, range_name)

        if not result['success'] or not result['data']:
            return None

        return pd.DataFrame(result['data'])


def get_reader() -> SheetsReader:
    """Factory function to get an authenticated Sheets reader."""
    reader = SheetsReader()
    return reader


# CLI for testing
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Google Sheets Reader CLI')
    parser.add_argument('--auth', action='store_true', help='Authenticate')
    parser.add_argument('--read', metavar='SHEET_ID', help='Read a sheet')
    parser.add_argument('--range', default='Sheet1', help='Range to read')
    parser.add_argument('--info', metavar='SHEET_ID', help='Get sheet info')

    args = parser.parse_args()

    reader = SheetsReader()

    if args.auth:
        reader.authenticate(force_new=True)

    elif args.read:
        if reader.authenticate():
            result = reader.read_sheet(args.read, args.range)
            if result['success']:
                print(f"\n[OK] Read {result['row_count']} rows")
                print(f"Headers: {result['headers']}")
                if result['data']:
                    print("\nFirst 3 rows:")
                    for row in result['data'][:3]:
                        print(f"  {row}")
            else:
                print(f"[X] Error: {result['error']}")

    elif args.info:
        if reader.authenticate():
            result = reader.get_spreadsheet_info(args.info)
            if result['success']:
                print(f"\nSpreadsheet: {result['title']}")
                print(f"URL: {result['url']}")
                print("\nSheets:")
                for sheet in result['sheets']:
                    print(f"  - {sheet['title']} ({sheet['row_count']} rows)")
            else:
                print(f"[X] Error: {result['error']}")

    else:
        parser.print_help()
