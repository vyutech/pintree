"""DOCX text extraction helpers."""

from pathlib import Path

from docx import Document


def read_docx_text(file_path: Path) -> str:
    """Read text from a DOCX file."""
    document = Document(str(file_path))
    return "\n".join(paragraph.text for paragraph in document.paragraphs)
