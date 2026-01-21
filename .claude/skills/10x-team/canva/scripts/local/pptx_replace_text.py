#!/usr/bin/env python3
"""
PPTX Replace Text Script
Find and replace text in a PowerPoint presentation while PRESERVING ALL FORMATTING

This script guarantees:
- Font styles are preserved (bold, italic, underline)
- Font sizes are preserved
- Font colors are preserved
- Font families are preserved
- Text alignments are preserved
- No new elements are created
- No existing elements are moved or resized
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
        description='Replace text in PPTX while preserving all formatting',
        epilog='This tool guarantees that only text content changes - no design modifications.'
    )
    parser.add_argument('file', help='Path to PPTX file')
    parser.add_argument('--find', '-f', required=True, help='Text to find')
    parser.add_argument('--replace', '-r', required=True, help='Replacement text')
    parser.add_argument('--slide', '-s', type=int, help='Specific slide number (default: all)')
    parser.add_argument('--output', '-o', help='Output file path (default: output/pptx/)')
    parser.add_argument('--in-place', action='store_true', help='Modify file in place (DANGER)')
    parser.add_argument('--dry-run', '-n', action='store_true', help='Show what would change without modifying')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    try:
        if args.dry_run:
            # Just count occurrences
            editor = PPTXEditor(str(file_path))
            count = 0
            occurrences = []

            slides = [editor.prs.slides[args.slide - 1]] if args.slide else editor.prs.slides

            for i, slide in enumerate(slides):
                slide_num = args.slide if args.slide else i + 1
                for shape in slide.shapes:
                    if shape.has_text_frame:
                        for para in shape.text_frame.paragraphs:
                            for run in para.runs:
                                if args.find in run.text:
                                    count += run.text.count(args.find)
                                    occurrences.append({
                                        'slide': slide_num,
                                        'text': run.text[:100]
                                    })

            if args.json:
                print(json.dumps({
                    'dry_run': True,
                    'find': args.find,
                    'replace': args.replace,
                    'occurrences_found': count,
                    'locations': occurrences
                }, indent=2))
            else:
                print(f"DRY RUN - No changes made")
                print(f"Find: \"{args.find}\"")
                print(f"Replace with: \"{args.replace}\"")
                print(f"Occurrences found: {count}")
                if occurrences:
                    print(f"\nLocations:")
                    for occ in occurrences[:10]:  # Show first 10
                        print(f"  Slide {occ['slide']}: ...{occ['text'][:50]}...")
            return

        # Create safe copy unless in-place
        if args.in_place:
            work_file = str(file_path)
            output_file = str(file_path)
        else:
            work_file = safe_copy(str(file_path), preserve_name=True)
            if args.output:
                output_file = args.output
            else:
                output_dir = Path('output/pptx')
                output_dir.mkdir(parents=True, exist_ok=True)
                output_file = str(output_dir / f"{file_path.stem}_modified{file_path.suffix}")

        # Perform replacement
        editor = PPTXEditor(work_file)
        count = editor.replace_text(
            find=args.find,
            replace=args.replace,
            slide_num=args.slide,
            preserve_formatting=True
        )

        # Save
        editor.save(output_file)

        if args.json:
            print(json.dumps({
                'success': True,
                'find': args.find,
                'replace': args.replace,
                'replacements_made': count,
                'output_file': output_file
            }, indent=2))
        else:
            print(f"Text replacement complete!")
            print(f"  Find: \"{args.find}\"")
            print(f"  Replace: \"{args.replace}\"")
            print(f"  Replacements: {count}")
            print(f"  Output: {output_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
