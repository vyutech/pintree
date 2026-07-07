"""Simple bento-grid style layout helpers."""

import streamlit as st


def render_card(title: str, body: str, key: str) -> None:
    """Render a single expandable summary card."""
    with st.container(border=False):
        st.markdown(f"### {title}")
        with st.expander("Expand card", expanded=True):
            st.write(body)
        st.session_state.setdefault("expanded_cards", {})
        st.session_state["expanded_cards"][key] = True
