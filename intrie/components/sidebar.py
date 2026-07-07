"""Sidebar renderer."""

import streamlit as st


def render_sidebar(page_names: list[str]) -> str:
    """Render sidebar navigation and return the selected page."""
    with st.sidebar:
        st.image("assets/logo.png", width=88)
        st.title("Intrie")
        st.caption("Career-focused AI interview practice")
        st.markdown("### Navigate")
        return st.radio("Navigate", page_names, index=0, label_visibility="collapsed")
