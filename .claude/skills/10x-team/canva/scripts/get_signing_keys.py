#!/usr/bin/env python3
"""
Get Signing Keys Script
Get JSON Web Keys for webhook signature verification
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Get Canva signing keys for webhooks')
    parser.add_argument('--type', '-t', choices=['connect', 'app', 'oidc'], default='connect',
                       help='Key type: connect (webhooks), app (JWT), oidc (OIDC)')
    parser.add_argument('--app-id', help='App ID (required for --type app)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    if args.type == 'app' and not args.app_id:
        parser.error("--app-id is required when --type is 'app'")

    try:
        client = get_client()

        if args.type == 'connect':
            result = client.get_signing_public_keys()
        elif args.type == 'app':
            result = client.get_app_jwks(args.app_id)
        elif args.type == 'oidc':
            result = client.get_oidc_jwks()

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            keys = result.get('keys', [])
            print(f"\n{args.type.upper()} Signing Keys: {len(keys)} key(s)")
            print("=" * 50)

            for i, key in enumerate(keys, 1):
                print(f"\nKey {i}:")
                print(f"  Key ID (kid): {key.get('kid', 'N/A')}")
                print(f"  Algorithm:    {key.get('alg', 'N/A')}")
                print(f"  Key Type:     {key.get('kty', 'N/A')}")
                print(f"  Use:          {key.get('use', 'N/A')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
