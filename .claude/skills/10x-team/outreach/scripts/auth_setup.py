#!/usr/bin/env python3
"""
Authentication Setup for 10x-Outreach-Skill
Sets up OAuth2 authentication for Gmail and Google Sheets APIs
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from dotenv import load_dotenv
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
except ImportError as e:
    print(f"[X] Missing dependency: {e}")
    print("    Run: pip install -r requirements.txt")
    sys.exit(1)

# Import our clients
from gmail_client import GmailClient
from sheets_reader import SheetsReader

load_dotenv(Path(__file__).parent.parent / '.env')
console = Console()


def check_env_variables():
    """Check if required environment variables are set."""
    required = ['GOOGLE_CLIENT_ID', 'GOOGLE_CLIENT_SECRET']
    optional = ['SENDER_EMAIL', 'SENDER_NAME', 'GOOGLE_SHEET_ID']

    console.print("\n[bold]Checking Environment Variables[/bold]\n")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Variable")
    table.add_column("Status")
    table.add_column("Value")

    all_required_set = True

    for var in required:
        value = os.getenv(var, '')
        if value:
            # Mask sensitive values
            display_value = value[:10] + '...' if len(value) > 10 else value
            table.add_row(var, "[green]SET[/green]", display_value)
        else:
            table.add_row(var, "[red]MISSING[/red]", "-")
            all_required_set = False

    for var in optional:
        value = os.getenv(var, '')
        if value:
            display_value = value[:30] + '...' if len(value) > 30 else value
            table.add_row(var, "[green]SET[/green]", display_value)
        else:
            table.add_row(var, "[yellow]NOT SET[/yellow]", "(optional)")

    console.print(table)

    return all_required_set


def setup_gmail_auth():
    """Set up Gmail authentication."""
    console.print("\n[bold cyan]Setting up Gmail Authentication[/bold cyan]\n")

    client = GmailClient()

    console.print("[i] Starting OAuth2 flow for Gmail...")
    console.print("[i] A browser window will open for authentication.")
    console.print("[i] Please sign in and grant the requested permissions.\n")

    if client.authenticate(force_new=True):
        user_info = client.get_user_info()
        if user_info:
            console.print(Panel(
                f"[green]Gmail Authentication Successful![/green]\n\n"
                f"Email: {user_info['email']}\n"
                f"Messages: {user_info['messages_total']}\n"
                f"Threads: {user_info['threads_total']}",
                title="Gmail Connected"
            ))
            return True

    console.print("[red]Gmail authentication failed![/red]")
    return False


def setup_sheets_auth():
    """Set up Google Sheets authentication."""
    console.print("\n[bold cyan]Setting up Google Sheets Authentication[/bold cyan]\n")

    reader = SheetsReader()

    console.print("[i] Starting OAuth2 flow for Google Sheets...")
    console.print("[i] A browser window will open for authentication.\n")

    if reader.authenticate(force_new=True):
        console.print(Panel(
            "[green]Google Sheets Authentication Successful![/green]",
            title="Sheets Connected"
        ))

        # Test with provided sheet ID if available
        sheet_id = os.getenv('GOOGLE_SHEET_ID')
        if sheet_id:
            console.print(f"\n[i] Testing access to configured sheet...")
            info = reader.get_spreadsheet_info(sheet_id)
            if info['success']:
                console.print(f"[green]OK[/green] Sheet: {info['title']}")
                for sheet in info['sheets']:
                    console.print(f"    - {sheet['title']} ({sheet['row_count']} rows)")
            else:
                console.print(f"[yellow]Warning[/yellow]: Could not access sheet: {info['error']}")

        return True

    console.print("[red]Sheets authentication failed![/red]")
    return False


def test_send_email():
    """Test sending an email."""
    console.print("\n[bold cyan]Test Email Sending[/bold cyan]\n")

    sender_email = os.getenv('SENDER_EMAIL')
    if not sender_email:
        console.print("[yellow]SENDER_EMAIL not set in .env - skipping test[/yellow]")
        return True

    test = console.input(f"Send a test email to yourself ({sender_email})? [y/N]: ")

    if test.lower() != 'y':
        console.print("[i] Skipping email test")
        return True

    client = GmailClient()
    if not client.authenticate():
        console.print("[red]Could not authenticate[/red]")
        return False

    result = client.send_email(
        to=sender_email,
        subject="10x-Outreach-Skill Test Email",
        body=f"""Hello!

This is a test email from 10x-Outreach-Skill.

If you're reading this, your email setup is working correctly!

Sent at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---
10x-Outreach-Skill
""",
        html_body=f"""
<html>
<body>
<h2>Hello!</h2>
<p>This is a test email from <strong>10x-Outreach-Skill</strong>.</p>
<p>If you're reading this, your email setup is working correctly!</p>
<p><em>Sent at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</em></p>
<hr>
<p style="color: gray;">10x-Outreach-Skill</p>
</body>
</html>
"""
    )

    if result['success']:
        console.print(f"[green]Test email sent successfully![/green]")
        console.print(f"Message ID: {result['message_id']}")
        return True
    else:
        console.print(f"[red]Failed to send test email: {result['error']}[/red]")
        return False


def save_auth_report():
    """Save authentication report to output."""
    output_dir = Path(__file__).parent.parent / 'output' / 'auth'
    output_dir.mkdir(parents=True, exist_ok=True)

    report = {
        'setup_date': datetime.now().isoformat(),
        'gmail_configured': os.path.exists(
            Path(__file__).parent.parent / 'credentials' / 'token.pickle'
        ),
        'sheets_configured': os.path.exists(
            Path(__file__).parent.parent / 'credentials' / 'sheets_token.pickle'
        ),
        'sender_email': os.getenv('SENDER_EMAIL', ''),
        'sender_name': os.getenv('SENDER_NAME', ''),
    }

    with open(output_dir / 'auth_status.json', 'w') as f:
        json.dump(report, f, indent=2)

    console.print(f"\n[i] Auth report saved to {output_dir / 'auth_status.json'}")


def main():
    console.print(Panel.fit(
        "[bold]10x-Outreach-Skill Authentication Setup[/bold]\n\n"
        "This script will set up OAuth2 authentication for:\n"
        "- Gmail API (sending emails)\n"
        "- Google Sheets API (reading recipient data)",
        border_style="cyan"
    ))

    # Check environment variables
    if not check_env_variables():
        console.print("\n[red]Please set the required environment variables in .env file[/red]")
        console.print("\nSteps:")
        console.print("1. Go to https://console.cloud.google.com/")
        console.print("2. Create a project and enable Gmail API + Sheets API")
        console.print("3. Create OAuth 2.0 credentials (Desktop App)")
        console.print("4. Copy Client ID and Client Secret to .env file")
        return False

    # Setup Gmail
    gmail_ok = setup_gmail_auth()

    # Setup Sheets
    sheets_ok = setup_sheets_auth()

    # Test email
    if gmail_ok:
        test_send_email()

    # Save report
    save_auth_report()

    # Summary
    console.print("\n" + "="*50)
    console.print("[bold]Setup Summary[/bold]")
    console.print("="*50)
    console.print(f"Gmail API:   {'[green]Ready[/green]' if gmail_ok else '[red]Failed[/red]'}")
    console.print(f"Sheets API:  {'[green]Ready[/green]' if sheets_ok else '[red]Failed[/red]'}")

    if gmail_ok and sheets_ok:
        console.print("\n[green bold]All authentication complete![/green bold]")
        console.print("\nNext steps:")
        console.print("1. Prepare your Google Sheet with recipient data")
        console.print("2. Create email templates in templates/ folder")
        console.print("3. Use /outreach command in Claude Code")
        return True
    else:
        console.print("\n[yellow]Some services failed to authenticate.[/yellow]")
        console.print("Please check the errors above and try again.")
        return False


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
