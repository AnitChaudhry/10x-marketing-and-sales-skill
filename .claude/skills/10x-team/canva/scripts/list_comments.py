#!/usr/bin/env python3
"""
List Comments Script
List comment threads and replies on a Canva design
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='List comments on a Canva design')
    parser.add_argument('design_id', help='Design ID')
    parser.add_argument('--thread', '-t', help='Thread ID to list replies')
    parser.add_argument('--limit', '-l', type=int, default=50, help='Max results (max: 100)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        if args.thread:
            # List replies in a thread
            result = client.list_replies(
                design_id=args.design_id,
                thread_id=args.thread,
                limit=min(args.limit, 100)
            )

            if args.json:
                print(json.dumps(result, indent=2))
            else:
                replies = result.get('replies', [])
                print(f"\nReplies in Thread: {len(replies)}")
                print("=" * 70)

                for reply in replies:
                    reply_id = reply.get('id', 'N/A')
                    message = reply.get('message', '')
                    created = reply.get('created_at', 'N/A')
                    author = reply.get('author', {}).get('display_name', 'Unknown')

                    print(f"\n  [{reply_id}] {author}")
                    print(f"    {message[:100]}{'...' if len(message) > 100 else ''}")
                    print(f"    Posted: {created}")
        else:
            # Get a specific thread (API doesn't have list threads endpoint)
            print("\nNote: To view comments, you need a thread ID.")
            print("Thread IDs are typically obtained when creating comments or from design metadata.")
            print("\nUsage:")
            print(f"  .venv\\Scripts\\python.exe scripts/list_comments.py \"{args.design_id}\" --thread THREAD_ID")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
