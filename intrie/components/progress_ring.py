"""Progress ring substitute for Streamlit."""

import streamlit as st


def render_progress_ring(score: int, label: str) -> None:
    """Render confidence score using a progress bar and metric."""
    st.markdown(f"### {label}")
    st.progress(max(0, min(score, 100)) / 100)
    st.metric("Confidence Score", f"{score}%")
