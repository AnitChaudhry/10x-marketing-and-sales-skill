#!/usr/bin/env python3
"""
PPTX Batch Update Script
Update multiple slides at once while PRESERVING ALL DESIGN ELEMENTS

Input format (JSON):
[
    {
        "slide_num": 1,
        "title": "New Title",
        "content": "New content text"
    },
    {
        "slide_num": 2,
        "content_items": ["Bullet 1", "Bullet 2", "Bullet 3"],
        "replacements": {"old text": "new text"}
    }
]

This script NEVER modifies design - only text content.
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from safe_copy import safe_copy
from pptx_utils import PPTXEditor


def main():
    parser = argparse.ArgumentParser(
        description='Batch update multiple slides while preserving design',
        epilog='All updates preserve formatting - no design changes.'
    )
    parser.add_argument('file', help='Path to PPTX file')
    parser.add_argument('--updates', '-u', required=True,
                        help='JSON file with updates or JSON string')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    # Parse updates
    try:
        updates_path = Path(args.updates)
        if updates_path.exists():
            with open(updates_path) as f:
                updates = json.load(f)
        else:
            updates = json.loads(args.updates)
    except json.JSONDecodeError as e:
        print(f"Error parsing updates JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(updates, list):
        print("Error: Updates must be a JSON array", file=sys.stderr)
        sys.exit(1)

    try:
        # Create safe copy
        work_file = safe_copy(str(file_path), preserve_name=True)

        if args.output:
            output_file = args.output
        else:
            output_dir = Path('output/pptx')
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = str(output_dir / f"{file_path.stem}_batch_modified{file_path.suffix}")

        editor = PPTXEditor(work_file)

        # Apply batch updates
        updated_count = editor.batch_update_slides(updates)

        # Save
        editor.save(output_file)

        if args.json:
            print(json.dumps({
                'success': True,
                'updates_requested': len(updates),
                'updates_applied': updated_count,
                'output_file': output_file
            }, indent=2))
        else:
            print(f"Batch update complete!")
            print(f"  Updates requested: {len(updates)}")
            print(f"  Updates applied: {updated_count}")
            print(f"  Output: {output_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
