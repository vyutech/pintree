"""Roadmap page."""

import streamlit as st

from components.roadmap_card import render_roadmap_card
from services.roadmap_generator import generate_learning_roadmap


def render() -> None:
    """Render personalized roadmap."""
    st.title("Roadmap")
    profile = st.session_state.get("candidate_profile")
    final_report = st.session_state.get("final_report")

    if not profile:
        st.warning("Complete setup first to generate a roadmap.")
        return

    roadmap = generate_learning_roadmap(profile, final_report)
    st.session_state["roadmap"] = roadmap
    for title, items in roadmap.items():
        render_roadmap_card(title.replace("_", " ").title(), items)
