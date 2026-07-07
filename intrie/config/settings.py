"""Environment-backed application settings."""

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


@dataclass(frozen=True)
class AppSettings:
    """Typed settings shared across the app."""

    app_name: str
    groq_api_key: str
    groq_model: str
    base_dir: Path
    data_dir: Path
    prompt_dir: Path
    stylesheet_path: Path


@lru_cache(maxsize=1)
def get_settings() -> AppSettings:
    """Load settings once for the current process."""
    return AppSettings(
        app_name="Intrie",
        groq_api_key=os.getenv("GROQ_API_KEY", ""),
        groq_model=os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile"),
        base_dir=BASE_DIR,
        data_dir=BASE_DIR / "data",
        prompt_dir=BASE_DIR / "prompts",
        stylesheet_path=BASE_DIR / "assets" / "styles.css",
    )
