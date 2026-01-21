#!/usr/bin/env python3
"""
PPTX Reorder Slides Script
Reorder slides in a PowerPoint presentation
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
    parser = argparse.ArgumentParser(description='Reorder slides in a PPTX')
    parser.add_argument('file', help='Path to PPTX file')
    parser.add_argument('--order', '-r', type=int, nargs='+', required=True,
                        help='New slide order (e.g., --order 1 3 2 4 5)')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    try:
        # Create safe copy
        work_file = safe_copy(str(file_path), preserve_name=True)

        if args.output:
            output_file = args.output
        else:
            output_dir = Path('output/pptx')
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = str(output_dir / f"{file_path.stem}_reordered{file_path.suffix}")

        editor = PPTXEditor(work_file)
        slide_count = len(editor.prs.slides)

        # Validate order
        if sorted(args.order) != list(range(1, slide_count + 1)):
            print(f"Error: Invalid order. Must include all slides 1-{slide_count}.", file=sys.stderr)
            print(f"Got: {sorted(args.order)}", file=sys.stderr)
            print(f"Expected: {list(range(1, slide_count + 1))}", file=sys.stderr)
            sys.exit(1)

        # Reorder
        editor.reorder_slides(args.order)

        # Save
        editor.save(output_file)

        if args.json:
            print(json.dumps({
                'success': True,
                'new_order': args.order,
                'slide_count': slide_count,
                'output_file': output_file
            }, indent=2))
        else:
            print(f"Slides reordered successfully!")
            print(f"  New order: {args.order}")
            print(f"  Output: {output_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
