"""Groq API wrapper with a mock fallback for local development."""

from __future__ import annotations

import json

try:
    from groq import Groq
except ImportError:  # pragma: no cover - import guard for environments without dependency
    Groq = None

from config.settings import get_settings


class GroqService:
    """Thin Groq client wrapper."""

    def __init__(self) -> None:
        settings = get_settings()
        self.model = settings.groq_model
        self.api_key = settings.groq_api_key
        self.client = Groq(api_key=self.api_key) if self.api_key and Groq is not None else None

    def complete_text(self, system_prompt: str, user_prompt: str) -> str:
        """Return text completion or a deterministic fallback."""
        if not self.client:
            return f"Mock response for: {user_prompt[:120]}"

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content or ""

    def complete_json(self, system_prompt: str, user_prompt: str, fallback: dict) -> dict:
        """Return a parsed JSON response or the supplied fallback."""
        text = self.complete_text(system_prompt, user_prompt)
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return fallback
