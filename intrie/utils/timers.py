"""Timer utilities for Streamlit pages."""

from __future__ import annotations

from datetime import datetime, timedelta

import streamlit as st


def get_remaining_seconds(timer_key: str, minutes: int) -> int:
    """Return remaining seconds for a session-scoped timer."""
    end_key = f"{timer_key}_ends_at"
    if end_key not in st.session_state:
        st.session_state[end_key] = datetime.utcnow() + timedelta(minutes=minutes)
    delta = st.session_state[end_key] - datetime.utcnow()
    return max(0, int(delta.total_seconds()))


def render_timer_text(seconds: int) -> str:
    """Format timer seconds as MM:SS."""
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"
