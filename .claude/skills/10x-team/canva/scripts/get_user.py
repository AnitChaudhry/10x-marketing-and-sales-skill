#!/usr/bin/env python3
"""
Get User Info Script
Retrieve authenticated user information and profile from Canva
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Get Canva user information')
    parser.add_argument('--profile', '-p', action='store_true', help='Include profile details')
    parser.add_argument('--capabilities', '-c', action='store_true', help='Show API capabilities')
    parser.add_argument('--all', '-a', action='store_true', help='Show all user information')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        # Get basic user info
        user_info = client.get_user_info()

        result = {
            'user': user_info
        }

        # Get profile if requested
        if args.profile or args.all:
            profile = client.get_user_profile()
            result['profile'] = profile

        # Get capabilities if requested
        if args.capabilities or args.all:
            capabilities = client.get_user_capabilities()
            result['capabilities'] = capabilities

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            user = user_info.get('user', {})
            print(f"\nCanva User Information")
            print("=" * 50)
            print(f"  User ID:  {user.get('id', 'N/A')}")
            print(f"  Team ID:  {user.get('team_id', 'N/A')}")

            if 'profile' in result:
                profile = result['profile'].get('profile', {})
                print(f"\nProfile:")
                print(f"  Display Name: {profile.get('display_name', 'N/A')}")

            if 'capabilities' in result:
                caps = result['capabilities'].get('capabilities', [])
                print(f"\nAPI Capabilities ({len(caps)}):")
                for cap in caps:
                    print(f"  - {cap}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
