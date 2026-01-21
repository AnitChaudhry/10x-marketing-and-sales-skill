#!/usr/bin/env python3
"""
Create Comment Script
Create a comment thread on a Canva design
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Create a comment on a Canva design')
    parser.add_argument('design_id', help='Design ID')
    parser.add_argument('message', help='Comment message')
    parser.add_argument('--page', '-p', help='Page ID to attach comment to')
    parser.add_argument('--element', '-e', help='Element ID to attach comment to')
    parser.add_argument('--assignee', '-a', help='User ID to assign the comment to')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        # Build attached_to if specified
        attached_to = None
        if args.page or args.element:
            attached_to = {}
            if args.page:
                attached_to['page_id'] = args.page
            if args.element:
                attached_to['element_id'] = args.element

        result = client.create_comment_thread(
            design_id=args.design_id,
            message=args.message,
            attached_to=attached_to,
            assignee_id=args.assignee
        )

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            thread = result.get('comment', {})
            print(f"\nComment Created Successfully!")
            print("=" * 50)
            print(f"  Thread ID: {thread.get('id', 'N/A')}")
            print(f"  Design:    {args.design_id}")
            print(f"  Message:   {args.message[:50]}{'...' if len(args.message) > 50 else ''}")
            print(f"  Created:   {thread.get('created_at', 'N/A')}")

            if args.assignee:
                print(f"  Assigned:  {args.assignee}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
