#!/usr/bin/env python3
"""
Check Canva API authentication status and display account info
"""

import sys
import json
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from canva_client import get_client


def check_auth():
    """Verify API credentials and show account info"""

    print("=" * 50)
    print("CANVA API AUTHENTICATION CHECK")
    print("=" * 50)

    client = get_client()

    # Check if credentials are configured
    if not client.access_token:
        print("\n[X] ERROR: No access token configured")
        print("\nTo fix this:")
        print("1. Edit the .env file with your Canva credentials")
        print("2. Run the OAuth flow to get access tokens")
        print("3. Add CANVA_ACCESS_TOKEN to your .env file")
        return False

    try:
        # Get user info
        print("\n[*] Checking credentials...")
        user_info = client.get_user_info()

        print("\n[OK] Authentication successful!")
        print("\n[*] Account Information:")
        print(f"   User ID: {user_info.get('user', {}).get('id', 'N/A')}")
        print(f"   Team ID: {user_info.get('team', {}).get('id', 'N/A')}")

        # Get profile
        profile = client.get_user_profile()
        print(f"   Display Name: {profile.get('profile', {}).get('display_name', 'N/A')}")

        # Get capabilities
        print("\n[*] API Capabilities:")
        capabilities = client.get_user_capabilities()
        for cap in capabilities.get('capabilities', []):
            print(f"   • {cap}")

        # Save to output
        output_dir = Path(__file__).parent.parent / 'output' / 'auth'
        output_dir.mkdir(parents=True, exist_ok=True)

        auth_info = {
            'user': user_info,
            'profile': profile,
            'capabilities': capabilities
        }

        with open(output_dir / 'auth_info.json', 'w') as f:
            json.dump(auth_info, f, indent=2)

        print(f"\n[*] Auth info saved to: output/auth/auth_info.json")

        return True

    except Exception as e:
        print(f"\n[X] Authentication failed: {e}")
        print("\nPossible issues:")
        print("• Access token may be expired (try refreshing)")
        print("• Invalid client credentials")
        print("• Required scopes not configured")
        return False


if __name__ == '__main__':
    success = check_auth()
    sys.exit(0 if success else 1)
