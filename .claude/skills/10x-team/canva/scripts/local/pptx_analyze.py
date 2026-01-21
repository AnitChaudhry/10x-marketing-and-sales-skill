#!/usr/bin/env python3
"""
PPTX Analyze Script
Analyze a PowerPoint presentation structure for safe editing

This script helps identify:
- Slide structure and layout types
- Text placeholders (safe to edit)
- Decorative elements (DO NOT edit)
- Images and their positions
"""

import argparse
import json
import sys
from pathlib import Path
from pptx_utils import PPTXAnalyzer, PPTXEditor


def analyze_for_editing(file_path: str) -> dict:
    """
    Analyze presentation for safe editing operations.
    Returns detailed structure information.
    """
    analyzer = PPTXAnalyzer(file_path)
    editor = PPTXEditor(file_path)

    metadata = analyzer.get_metadata()

    slides_analysis = []

    for i in range(len(analyzer.prs.slides)):
        slide_num = i + 1
        slide = analyzer.prs.slides[i]

        # Get basic info
        basic_info = analyzer.get_slide_info(slide_num)

        # Get structure analysis from editor
        structure = editor._analyze_slide_structure(slide)

        # Build editable elements list
        editable_elements = []

        # Title
        if structure['title_shape']:
            title_shape = structure['title_shape']
            if title_shape.has_text_frame:
                editable_elements.append({
                    'type': 'title',
                    'current_text': title_shape.text_frame.text,
                    'shape_id': title_shape.shape_id if hasattr(title_shape, 'shape_id') else None,
                    'editable': True
                })

        # Subtitle
        if structure['subtitle_shape']:
            subtitle_shape = structure['subtitle_shape']
            if subtitle_shape.has_text_frame:
                editable_elements.append({
                    'type': 'subtitle',
                    'current_text': subtitle_shape.text_frame.text,
                    'shape_id': subtitle_shape.shape_id if hasattr(subtitle_shape, 'shape_id') else None,
                    'editable': True
                })

        # Content shapes
        for j, shape in enumerate(structure['content_shapes']):
            if shape.has_text_frame:
                # Get all paragraphs text
                paras = []
                for para in shape.text_frame.paragraphs:
                    if para.text.strip():
                        paras.append(para.text)

                editable_elements.append({
                    'type': 'content',
                    'index': j,
                    'current_text': '\n'.join(paras),
                    'paragraph_count': len(paras),
                    'editable': True
                })

        # Decorative elements (DO NOT EDIT)
        decorative_count = len(structure['decorative_shapes'])
        image_count = len(structure['image_shapes'])

        slides_analysis.append({
            'slide_number': slide_num,
            'layout_type': structure['layout_type'],
            'layout_name': basic_info['layout'],
            'has_background': structure['has_background_image'],
            'editable_elements': editable_elements,
            'decorative_elements_count': decorative_count,
            'image_count': image_count,
            'word_count': basic_info['word_count'],
            'warnings': []
        })

        # Add warnings
        if decorative_count > 0:
            slides_analysis[-1]['warnings'].append(
                f"Contains {decorative_count} decorative element(s) - DO NOT MODIFY"
            )

    return {
        'metadata': metadata,
        'total_slides': len(slides_analysis),
        'slides': slides_analysis,
        'editing_guidelines': {
            'safe_operations': [
                'Replace text in title placeholders',
                'Replace text in content placeholders',
                'Replace text in subtitle placeholders',
                'Duplicate existing slides to create new ones',
                'Delete slides',
                'Reorder slides'
            ],
            'dangerous_operations': [
                'Adding new text boxes',
                'Adding new shapes',
                'Creating blank slides',
                'Changing fonts/colors/sizes',
                'Moving elements',
                'Modifying backgrounds'
            ]
        }
    }


def main():
    parser = argparse.ArgumentParser(
        description='Analyze PPTX for safe editing operations',
        epilog='This analysis identifies what can be safely edited without breaking the design.'
    )
    parser.add_argument('file', help='Path to PPTX file')
    parser.add_argument('--slide', '-s', type=int, help='Analyze specific slide only')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--brief', '-b', action='store_true', help='Brief output')

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    try:
        analysis = analyze_for_editing(str(file_path))

        if args.slide:
            # Filter to specific slide
            slide_data = None
            for s in analysis['slides']:
                if s['slide_number'] == args.slide:
                    slide_data = s
                    break

            if not slide_data:
                print(f"Error: Slide {args.slide} not found", file=sys.stderr)
                sys.exit(1)

            if args.json:
                print(json.dumps(slide_data, indent=2, default=str))
            else:
                print_slide_analysis(slide_data, args.brief)
            return

        if args.json:
            print(json.dumps(analysis, indent=2, default=str))
        else:
            print_analysis(analysis, args.brief)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def print_analysis(analysis: dict, brief: bool = False):
    """Print human-readable analysis"""
    meta = analysis['metadata']

    print("=" * 60)
    print("PPTX ANALYSIS FOR SAFE EDITING")
    print("=" * 60)
    print(f"File: {meta['file']}")
    print(f"Title: {meta['title']}")
    print(f"Total Slides: {meta['slides']}")
    print(f"Dimensions: {meta['slide_width']:.1f}\" x {meta['slide_height']:.1f}\"")

    print("\n" + "-" * 60)
    print("SLIDE-BY-SLIDE ANALYSIS")
    print("-" * 60)

    for slide in analysis['slides']:
        print_slide_analysis(slide, brief)
        print()

    if not brief:
        print("-" * 60)
        print("EDITING GUIDELINES")
        print("-" * 60)
        print("\n SAFE OPERATIONS:")
        for op in analysis['editing_guidelines']['safe_operations']:
            print(f"    {op}")

        print("\n DANGEROUS OPERATIONS (DO NOT DO):")
        for op in analysis['editing_guidelines']['dangerous_operations']:
            print(f"    {op}")


def print_slide_analysis(slide: dict, brief: bool = False):
    """Print single slide analysis"""
    print(f"\nSlide {slide['slide_number']} ({slide['layout_type']})")
    print(f"  Layout: {slide['layout_name']}")

    if slide['warnings']:
        for warn in slide['warnings']:
            print(f"  WARNING: {warn}")

    print(f"  Editable elements: {len(slide['editable_elements'])}")

    if not brief:
        for elem in slide['editable_elements']:
            text_preview = elem['current_text'][:50] + '...' if len(elem['current_text']) > 50 else elem['current_text']
            text_preview = text_preview.replace('\n', ' | ')
            print(f"    [{elem['type'].upper()}] \"{text_preview}\"")


if __name__ == '__main__':
    main()
