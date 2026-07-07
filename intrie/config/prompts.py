"""Prompt loading helpers."""

from pathlib import Path

from config.settings import get_settings


def load_prompt(filename: str) -> str:
    """Load a prompt file from the prompts directory."""
    prompt_path = get_settings().prompt_dir / filename
    if not prompt_path.exists():
        return ""
    return prompt_path.read_text(encoding="utf-8").strip()


def load_prompt_map() -> dict[str, str]:
    """Return every prompt file as a filename-to-text mapping."""
    prompt_dir: Path = get_settings().prompt_dir
    return {
        path.name: path.read_text(encoding="utf-8").strip()
        for path in sorted(prompt_dir.glob("*.txt"))
    }
