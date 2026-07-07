"""Feedback page."""

import streamlit as st

from components.progress_ring import render_progress_ring
from services.feedback_generator import generate_final_report


def render() -> None:
    """Render final scores and feedback."""
    st.title("Feedback & Scores")
    round1 = st.session_state.get("round1_result")
    round2 = st.session_state.get("round2_result")
    profile = st.session_state.get("candidate_profile")

    if not (round1 and round2 and profile):
        st.warning("Finish both interview rounds to unlock the final feedback report.")
        return

    report = generate_final_report(profile, round1, round2)
    st.session_state["final_report"] = report

    render_progress_ring(report["confidence_score"], "Estimated Hiring Confidence")
    st.subheader("Summary")
    st.json(report)
