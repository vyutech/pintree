"""File storage helpers."""

from pathlib import Path
import shutil

from config.settings import get_settings


def save_uploaded_file(uploaded_file, target_dir: str) -> Path:
    """Persist a Streamlit uploaded file to a configured data directory."""
    destination = get_settings().data_dir / target_dir / uploaded_file.name
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as output:
        shutil.copyfileobj(uploaded_file, output)
    return destination
