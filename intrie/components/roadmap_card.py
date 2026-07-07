"""Roadmap card renderer."""

import streamlit as st


def render_roadmap_card(title: str, items: list[str]) -> None:
    """Render roadmap list content in a card."""
    with st.container(border=True):
        st.subheader(title)
        for item in items:
            st.write(f"- {item}")
