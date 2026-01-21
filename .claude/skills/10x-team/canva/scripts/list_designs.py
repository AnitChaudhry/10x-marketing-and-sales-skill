#!/usr/bin/env python3
"""
List all designs in Canva account
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from canva_client import get_client


def list_designs(args):
    """List designs with optional filters"""

    client = get_client()

    print("=" * 60)
    print("CANVA DESIGNS")
    print("=" * 60)

    if args.query:
        print(f"\nSearching for: '{args.query}'")

    all_designs = []
    continuation = None

    # Paginate through all designs
    while True:
        result = client.list_designs(
            limit=min(args.limit, 100),
            continuation=continuation,
            ownership=args.ownership,
            sort_by=args.sort,
            query=args.query
        )

        designs = result.get('designs', [])
        all_designs.extend(designs)

        continuation = result.get('continuation')

        if not continuation or len(all_designs) >= args.limit:
            break

    # Truncate to requested limit
    all_designs = all_designs[:args.limit]

    # Filter by type if specified
    if args.type:
        all_designs = [d for d in all_designs
                       if d.get('design_type', {}).get('type') == args.type]

    # Display results
    print(f"\nFound {len(all_designs)} designs")
    print("-" * 60)

    for i, design in enumerate(all_designs, 1):
        design_type = design.get('design_type', {}).get('type', 'unknown')
        title = design.get('title', 'Untitled')
        created = design.get('created_at', '')[:10]
        modified = design.get('updated_at', '')[:10]

        print(f"\n{i}. {title}")
        print(f"   ID: {design.get('id')}")
        print(f"   Type: {design_type}")
        print(f"   Created: {created} | Modified: {modified}")

        # Show URLs if verbose
        if args.verbose:
            urls = design.get('urls', {})
            print(f"   View: {urls.get('view_url', 'N/A')}")
            print(f"   Edit: {urls.get('edit_url', 'N/A')}")

    # Save to output
    if args.output:
        output_path = Path(args.output)
    else:
        output_dir = Path(__file__).parent.parent / 'output' / 'explorations'
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = output_dir / f'designs_{timestamp}.json'

    with open(output_path, 'w') as f:
        json.dump(all_designs, f, indent=2)

    print(f"\n[*] Data saved to: {output_path}")

    return all_designs


def main():
    parser = argparse.ArgumentParser(description='List Canva designs')
    parser.add_argument('--limit', type=int, default=50,
                        help='Maximum number of designs to retrieve (max: 100 per page)')
    parser.add_argument('--query', '-q', type=str,
                        help='Search query to filter designs (max 255 chars)')
    parser.add_argument('--type', type=str,
                        help='Filter by design type (e.g., presentation, instagram_post)')
    parser.add_argument('--ownership', type=str, choices=['owned', 'shared'],
                        help='Filter by ownership')
    parser.add_argument('--sort', type=str,
                        choices=['relevance', 'modified_descending', 'modified_ascending',
                                 'title_descending', 'title_ascending'],
                        help='Sort by field')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Show additional details')
    parser.add_argument('--output', '-o', type=str,
                        help='Output file path')

    args = parser.parse_args()
    list_designs(args)


if __name__ == '__main__':
    main()
