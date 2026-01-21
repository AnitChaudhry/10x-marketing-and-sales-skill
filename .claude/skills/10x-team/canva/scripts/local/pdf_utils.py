#!/usr/bin/env python3
"""
PDF Utilities
Core module for local PDF manipulation
"""

import os
import json
from pathlib import Path
from typing import Optional, List, Dict, Any

try:
    import PyPDF2
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("PyPDF2 not installed. Run: pip install PyPDF2")
    PyPDF2 = None

try:
    import pdfplumber
except ImportError:
    print("pdfplumber not installed. Run: pip install pdfplumber")
    pdfplumber = None

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
except ImportError:
    print("reportlab not installed. Run: pip install reportlab")
    canvas = None


class PDFAnalyzer:
    """Analyze PDF files"""

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"PDF not found: {file_path}")

    def get_metadata(self) -> Dict[str, Any]:
        """Get PDF metadata"""
        with open(self.file_path, 'rb') as f:
            reader = PdfReader(f)
            info = reader.metadata or {}

            return {
                'file': str(self.file_path),
                'pages': len(reader.pages),
                'title': info.get('/Title', 'N/A'),
                'author': info.get('/Author', 'N/A'),
                'subject': info.get('/Subject', 'N/A'),
                'creator': info.get('/Creator', 'N/A'),
                'encrypted': reader.is_encrypted
            }

    def get_page_info(self, page_num: int) -> Dict[str, Any]:
        """Get info for specific page"""
        with open(self.file_path, 'rb') as f:
            reader = PdfReader(f)
            if page_num < 1 or page_num > len(reader.pages):
                raise ValueError(f"Invalid page number: {page_num}")

            page = reader.pages[page_num - 1]
            media_box = page.mediabox

            return {
                'page': page_num,
                'width': float(media_box.width),
                'height': float(media_box.height),
                'has_text': bool(page.extract_text()),
                'rotation': page.get('/Rotate', 0)
            }

    def extract_text(self, page_num: Optional[int] = None) -> str:
        """Extract text from PDF"""
        if pdfplumber is None:
            # Fallback to PyPDF2
            with open(self.file_path, 'rb') as f:
                reader = PdfReader(f)
                if page_num:
                    return reader.pages[page_num - 1].extract_text() or ""
                return "\n\n".join(
                    page.extract_text() or "" for page in reader.pages
                )

        with pdfplumber.open(self.file_path) as pdf:
            if page_num:
                return pdf.pages[page_num - 1].extract_text() or ""
            return "\n\n".join(
                page.extract_text() or "" for page in pdf.pages
            )

    def get_word_count(self, page_num: Optional[int] = None) -> Dict[str, int]:
        """Get word count"""
        text = self.extract_text(page_num)
        words = text.split()

        if page_num:
            return {'page': page_num, 'words': len(words)}

        # Per-page word count
        with pdfplumber.open(self.file_path) as pdf:
            counts = {'total': len(words), 'pages': {}}
            for i, page in enumerate(pdf.pages, 1):
                page_text = page.extract_text() or ""
                counts['pages'][i] = len(page_text.split())
            return counts

    def analyze(self) -> Dict[str, Any]:
        """Full PDF analysis"""
        metadata = self.get_metadata()
        word_counts = self.get_word_count()

        analysis = {
            **metadata,
            'word_count': word_counts['total'],
            'pages_detail': []
        }

        with open(self.file_path, 'rb') as f:
            reader = PdfReader(f)
            for i in range(len(reader.pages)):
                page_info = self.get_page_info(i + 1)
                page_info['word_count'] = word_counts['pages'].get(i + 1, 0)
                analysis['pages_detail'].append(page_info)

        return analysis


class PDFEditor:
    """Edit PDF files"""

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"PDF not found: {file_path}")

    def merge(self, other_files: List[str], output_path: str) -> str:
        """Merge multiple PDFs"""
        writer = PdfWriter()

        # Add pages from main file
        with open(self.file_path, 'rb') as f:
            reader = PdfReader(f)
            for page in reader.pages:
                writer.add_page(page)

        # Add pages from other files
        for file_path in other_files:
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    writer.add_page(page)

        # Write output
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, 'wb') as f:
            writer.write(f)

        return str(output)

    def split(self, page_ranges: str, output_dir: str) -> List[str]:
        """
        Split PDF by page ranges

        Args:
            page_ranges: Comma-separated ranges like "1-5,10-15"
            output_dir: Output directory
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        outputs = []

        with open(self.file_path, 'rb') as f:
            reader = PdfReader(f)

            for range_str in page_ranges.split(','):
                range_str = range_str.strip()

                if '-' in range_str:
                    start, end = map(int, range_str.split('-'))
                else:
                    start = end = int(range_str)

                writer = PdfWriter()
                for i in range(start - 1, end):
                    if i < len(reader.pages):
                        writer.add_page(reader.pages[i])

                out_file = output_path / f"pages_{start}-{end}.pdf"
                with open(out_file, 'wb') as out:
                    writer.write(out)
                outputs.append(str(out_file))

        return outputs

    def extract_pages(self, pages: List[int], output_path: str) -> str:
        """Extract specific pages to new PDF"""
        writer = PdfWriter()

        with open(self.file_path, 'rb') as f:
            reader = PdfReader(f)
            for page_num in pages:
                if 0 < page_num <= len(reader.pages):
                    writer.add_page(reader.pages[page_num - 1])

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, 'wb') as f:
            writer.write(f)

        return str(output)

    def rotate_pages(self, pages: List[int], rotation: int, output_path: str) -> str:
        """Rotate specific pages"""
        writer = PdfWriter()

        with open(self.file_path, 'rb') as f:
            reader = PdfReader(f)
            for i, page in enumerate(reader.pages, 1):
                if i in pages:
                    page.rotate(rotation)
                writer.add_page(page)

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, 'wb') as f:
            writer.write(f)

        return str(output)


def analyze_pdf(file_path: str) -> Dict[str, Any]:
    """Quick analysis function"""
    analyzer = PDFAnalyzer(file_path)
    return analyzer.analyze()


def extract_text(file_path: str, page: Optional[int] = None) -> str:
    """Quick text extraction"""
    analyzer = PDFAnalyzer(file_path)
    return analyzer.extract_text(page)


def merge_pdfs(files: List[str], output_path: str) -> str:
    """Merge multiple PDFs"""
    if not files:
        raise ValueError("No files to merge")

    editor = PDFEditor(files[0])
    return editor.merge(files[1:], output_path)


def split_pdf(file_path: str, page_ranges: str, output_dir: str) -> List[str]:
    """Split PDF by page ranges"""
    editor = PDFEditor(file_path)
    return editor.split(page_ranges, output_dir)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python pdf_utils.py <pdf_file>")
        sys.exit(1)

    result = analyze_pdf(sys.argv[1])
    print(json.dumps(result, indent=2))
