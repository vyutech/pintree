"""Timer UI component."""

import streamlit as st

from utils.timers import get_remaining_seconds, render_timer_text


def render_round_timer(timer_key: str, minutes: int = 10) -> None:
    """Render a simple timer display."""
    remaining = get_remaining_seconds(timer_key, minutes)
    st.info(f"Time remaining: {render_timer_text(remaining)}")
