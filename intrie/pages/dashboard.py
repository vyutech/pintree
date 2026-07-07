"""Dashboard page."""

import streamlit as st

from components.bento_grid import render_card
from components.dashboard import render_hero, render_strengths_and_gaps
from components.progress_ring import render_progress_ring
from components.score_card import render_score_card


def render() -> None:
    """Render the main dashboard."""
    state = st.session_state
    render_hero(
        "Prepare like the interview is tomorrow.",
        "Track setup, practice rounds, and targeted improvements from one focused workspace.",
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        render_score_card("Round 1 Score", state["scores"]["round1"], "Skill assessment performance")
    with col2:
        render_score_card("Round 2 Score", state["scores"]["round2"], "Technical interview performance")
    with col3:
        render_progress_ring(state["scores"]["confidence"], "Hiring Confidence")

    top_left, top_right = st.columns(2)
    with top_left:
        render_card("Interview Progress", state["progress_summary"], "progress")
        render_card("Next Steps", "\n".join(state["next_steps"]), "next_steps")
    with top_right:
        render_card("Resume Status", state["resume_status"], "resume_status")
        render_card("Current Round", state["current_round"], "current_round")

    render_strengths_and_gaps(state["strengths"], state["weak_areas"])
