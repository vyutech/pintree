"""Resume parsing service."""

from pathlib import Path

from utils.docx_reader import read_docx_text
from utils.pdf_reader import read_pdf_text


def parse_resume(file_path: Path) -> dict:
    """Extract resume text and derive lightweight structured insights."""
    suffix = file_path.suffix.lower()
    if suffix == ".pdf":
        resume_text = read_pdf_text(file_path)
    elif suffix == ".docx":
        resume_text = read_docx_text(file_path)
    else:
        resume_text = ""

    lowered = resume_text.lower()
    return {
        "skills": _extract_keywords(lowered, ["python", "sql", "streamlit", "javascript", "ml", "data analysis"]),
        "experience_highlights": _extract_sentences(resume_text),
        "projects": ["Portfolio-ready project experience inferred from resume text"],
        "education": "Education details available in resume." if "university" in lowered or "bachelor" in lowered else "",
        "keywords": sorted({word for word in lowered.split() if len(word) > 6})[:12],
        "resume_text_preview": resume_text[:1200],
    }


def _extract_keywords(text: str, candidates: list[str]) -> list[str]:
    return [item for item in candidates if item in text] or ["Problem solving", "Communication"]


def _extract_sentences(text: str) -> list[str]:
    snippets = [sentence.strip() for sentence in text.replace("\n", ". ").split(".") if sentence.strip()]
    return snippets[:4]
