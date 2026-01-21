#!/usr/bin/env python3
"""
PPTX Update Content Script
Update slide content while STRICTLY PRESERVING ALL DESIGN ELEMENTS

This script allows updating:
- Title text (preserves formatting)
- Content/body text (preserves formatting)
- Bullet points (preserves formatting)

This script NEVER:
- Creates new text boxes
- Adds new shapes
- Changes font sizes, colors, or families
- Moves any elements
- Modifies backgrounds
- Changes decorative elements
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
        description='Update slide content while preserving all design elements',
        epilog='Only text content changes - NO design modifications.'
    )
    parser.add_argument('file', help='Path to PPTX file')
    parser.add_argument('--slide', '-s', type=int, required=True,
                        help='Slide number to update (1-indexed)')
    parser.add_argument('--title', '-t', help='New title text')
    parser.add_argument('--content', '-c', help='New content text (single paragraph)')
    parser.add_argument('--bullets', '-b', nargs='+', help='New bullet points (multiple items)')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    if not args.title and not args.content and not args.bullets:
        parser.error("At least one of --title, --content, or --bullets is required")

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

        editor = PPTXEditor(work_file)

        # Validate slide number
        if args.slide < 1 or args.slide > len(editor.prs.slides):
            print(f"Error: Invalid slide {args.slide}. "
                  f"Presentation has {len(editor.prs.slides)} slides.", file=sys.stderr)
            sys.exit(1)

        slide = editor.prs.slides[args.slide - 1]
        changes = []

        # Update title
        if args.title:
            editor._update_title(slide, args.title)
            changes.append(f"Title updated to: \"{args.title[:50]}...\"" if len(args.title) > 50 else f"Title updated to: \"{args.title}\"")

        # Update content
        if args.content:
            editor._update_content(slide, args.content)
            changes.append(f"Content updated")
        elif args.bullets:
            editor._update_content_bullets(slide, args.bullets)
            changes.append(f"Bullets updated ({len(args.bullets)} items)")

        # Save
        editor.save(output_file)

        if args.json:
            print(json.dumps({
                'success': True,
                'slide': args.slide,
                'changes': changes,
                'output_file': output_file
            }, indent=2))
        else:
            print(f"Slide {args.slide} updated successfully!")
            for change in changes:
                print(f"  - {change}")
            print(f"  Output: {output_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
