"""Sidebar renderer."""

from pathlib import Path
import streamlit as st


def render_sidebar(page_names: list[str]) -> str:
    """Render sidebar navigation and return the selected page."""
    with st.sidebar:
        logo_path = Path(__file__).resolve().parent.parent / "assets" / "logo.png"
        if logo_path.exists():
            st.image(str(logo_path), width=88)
        else:
            st.warning("Logo not found")
        st.title("Intrie")
        st.caption("Career-focused AI interview practice")
        st.markdown("### Navigate")
        return st.radio("Navigate", page_names, index=0, label_visibility="collapsed")
