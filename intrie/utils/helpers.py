"""Generic helpers."""

from datetime import datetime
import re


def slugify(value: str) -> str:
    """Turn a string into a simple filesystem-safe slug."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def now_iso() -> str:
    """Return the current UTC timestamp in ISO format."""
    return datetime.utcnow().isoformat()
