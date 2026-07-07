"""Score card component."""

import streamlit as st


def render_score_card(label: str, score: int, help_text: str = "") -> None:
    """Render a styled metric card."""
    st.metric(label=label, value=f"{score}/100", help=help_text)
