#!/usr/bin/env python3
"""
PPTX Delete Slide Script
Delete one or more slides from a PowerPoint presentation
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
    parser = argparse.ArgumentParser(description='Delete slides from a PPTX')
    parser.add_argument('file', help='Path to PPTX file')
    parser.add_argument('--slides', '-s', type=int, nargs='+', required=True,
                        help='Slide numbers to delete (1-indexed)')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--confirm', '-y', action='store_true', help='Skip confirmation')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    # Sort in descending order to delete from end first (avoids index shifting)
    slides_to_delete = sorted(set(args.slides), reverse=True)

    if not args.confirm:
        print(f"This will delete slide(s): {sorted(slides_to_delete)}")
        response = input("Continue? [y/N]: ")
        if response.lower() != 'y':
            print("Cancelled.")
            return

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
        original_count = len(editor.prs.slides)

        # Validate slide numbers
        for slide_num in slides_to_delete:
            if slide_num < 1 or slide_num > original_count:
                print(f"Error: Invalid slide {slide_num}. "
                      f"Presentation has {original_count} slides.", file=sys.stderr)
                sys.exit(1)

        # Delete slides (in reverse order)
        deleted = []
        for slide_num in slides_to_delete:
            # Adjust for already deleted slides
            adjusted_num = slide_num
            for d in deleted:
                if d < slide_num:
                    adjusted_num -= 1

            editor.delete_slide(adjusted_num)
            deleted.append(slide_num)

        # Save
        editor.save(output_file)

        if args.json:
            print(json.dumps({
                'success': True,
                'deleted_slides': sorted(slides_to_delete),
                'original_count': original_count,
                'new_count': len(editor.prs.slides),
                'output_file': output_file
            }, indent=2))
        else:
            print(f"Slides deleted successfully!")
            print(f"  Deleted: {sorted(slides_to_delete)}")
            print(f"  Original count: {original_count}")
            print(f"  New count: {original_count - len(slides_to_delete)}")
            print(f"  Output: {output_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
