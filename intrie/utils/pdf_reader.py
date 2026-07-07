"""PDF text extraction helpers."""

from pathlib import Path

from PyPDF2 import PdfReader


def read_pdf_text(file_path: Path) -> str:
    """Read text from a PDF file."""
    reader = PdfReader(str(file_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)
