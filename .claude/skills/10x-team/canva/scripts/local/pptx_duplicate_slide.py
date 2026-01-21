#!/usr/bin/env python3
"""
PPTX Duplicate Slide Script
Duplicate an existing slide to create a new one while PRESERVING ALL DESIGN ELEMENTS

This is the CORRECT way to add new slides - duplicating preserves:
- Background images and colors
- Theme formatting
- Layout structure
- Decorative elements (logos, shapes, lines)
- Font styles
- All positioning

NEVER create blank slides - always duplicate an existing one!
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
        description='Duplicate a slide preserving all design elements',
        epilog='This is the CORRECT way to add slides - it preserves the design theme.'
    )
    parser.add_argument('file', help='Path to PPTX file')
    parser.add_argument('--source', '-s', type=int, required=True,
                        help='Source slide number to duplicate (1-indexed)')
    parser.add_argument('--position', '-p', type=int,
                        help='Position to insert (1-indexed). Default: after source')
    parser.add_argument('--title', '-t', help='New title for duplicated slide')
    parser.add_argument('--content', '-c', help='New content for duplicated slide')
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
            output_file = str(output_dir / f"{file_path.stem}_modified{file_path.suffix}")

        # Duplicate slide
        editor = PPTXEditor(work_file)

        # Validate source slide
        if args.source < 1 or args.source > len(editor.prs.slides):
            print(f"Error: Invalid source slide {args.source}. "
                  f"Presentation has {len(editor.prs.slides)} slides.", file=sys.stderr)
            sys.exit(1)

        new_slide_num = editor.duplicate_slide(
            source_slide_num=args.source,
            insert_position=args.position
        )

        # Update content if provided
        if args.title or args.content:
            new_slide = editor.prs.slides[new_slide_num - 1]
            if args.title:
                editor._update_title(new_slide, args.title)
            if args.content:
                editor._update_content(new_slide, args.content)

        # Save
        editor.save(output_file)

        if args.json:
            print(json.dumps({
                'success': True,
                'source_slide': args.source,
                'new_slide_number': new_slide_num,
                'total_slides': len(editor.prs.slides),
                'output_file': output_file
            }, indent=2))
        else:
            print(f"Slide duplicated successfully!")
            print(f"  Source: Slide {args.source}")
            print(f"  New slide: {new_slide_num}")
            print(f"  Total slides: {len(editor.prs.slides)}")
            print(f"  Output: {output_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
