#!/usr/bin/env python3
"""
Reply to Comment Script
Reply to a comment thread on a Canva design
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Reply to a comment on a Canva design')
    parser.add_argument('design_id', help='Design ID')
    parser.add_argument('thread_id', help='Comment thread ID')
    parser.add_argument('message', help='Reply message')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        result = client.create_reply(
            design_id=args.design_id,
            thread_id=args.thread_id,
            message=args.message
        )

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            reply = result.get('reply', {})
            print(f"\nReply Added Successfully!")
            print("=" * 50)
            print(f"  Reply ID:  {reply.get('id', 'N/A')}")
            print(f"  Thread:    {args.thread_id}")
            print(f"  Message:   {args.message[:50]}{'...' if len(args.message) > 50 else ''}")
            print(f"  Created:   {reply.get('created_at', 'N/A')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
