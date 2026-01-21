#!/usr/bin/env python3
"""
PPTX Add Slides from Template Script
Add multiple new slides by duplicating a template slide

This is the CORRECT way to add multiple slides - each new slide:
- Copies the template slide's design exactly
- Preserves backgrounds, themes, decorative elements
- Only replaces text content

Input format (JSON):
[
    {"title": "First New Slide", "content": "Content here"},
    {"title": "Second Slide", "content_items": ["Bullet 1", "Bullet 2"]},
    {"title": "Third Slide", "content": "More content"}
]
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from safe_copy import safe_copy
from pptx_utils import add_slides_from_template, PPTXEditor


def main():
    parser = argparse.ArgumentParser(
        description='Add multiple slides from a template slide',
        epilog='The CORRECT way to add slides while preserving design.'
    )
    parser.add_argument('file', help='Path to PPTX file')
    parser.add_argument('--template', '-t', type=int, required=True,
                        help='Template slide number to duplicate (1-indexed)')
    parser.add_argument('--content', '-c', required=True,
                        help='JSON file or string with slide content')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    # Parse content
    try:
        content_path = Path(args.content)
        if content_path.exists():
            with open(content_path) as f:
                slides_content = json.load(f)
        else:
            slides_content = json.loads(args.content)
    except json.JSONDecodeError as e:
        print(f"Error parsing content JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(slides_content, list):
        print("Error: Content must be a JSON array", file=sys.stderr)
        sys.exit(1)

    try:
        # Create safe copy
        work_file = safe_copy(str(file_path), preserve_name=True)

        if args.output:
            output_file = args.output
        else:
            output_dir = Path('output/pptx')
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = str(output_dir / f"{file_path.stem}_expanded{file_path.suffix}")

        # Validate template slide
        editor = PPTXEditor(work_file)
        if args.template < 1 or args.template > len(editor.prs.slides):
            print(f"Error: Invalid template slide {args.template}. "
                  f"Presentation has {len(editor.prs.slides)} slides.", file=sys.stderr)
            sys.exit(1)

        original_count = len(editor.prs.slides)

        # Add slides
        added = add_slides_from_template(
            file_path=work_file,
            template_slide=args.template,
            slides_content=slides_content,
            output_path=output_file
        )

        if args.json:
            print(json.dumps({
                'success': True,
                'template_slide': args.template,
                'slides_added': added,
                'original_count': original_count,
                'new_count': original_count + added,
                'output_file': output_file
            }, indent=2))
        else:
            print(f"Slides added successfully!")
            print(f"  Template: Slide {args.template}")
            print(f"  Slides added: {added}")
            print(f"  Total slides: {original_count + added}")
            print(f"  Output: {output_file}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
