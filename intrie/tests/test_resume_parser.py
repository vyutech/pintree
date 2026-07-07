from pathlib import Path

from services.resume_parser import parse_resume


def test_parse_resume_handles_plain_missing_format(tmp_path: Path) -> None:
    file_path = tmp_path / "resume.txt"
    file_path.write_text("Python SQL Streamlit Bachelor University", encoding="utf-8")
    parsed = parse_resume(file_path)
    assert "skills" in parsed
    assert isinstance(parsed["skills"], list)
