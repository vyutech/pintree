"""Streamlit session state defaults."""

import streamlit as st


def initialize_session_state() -> None:
    """Create all session state keys used across pages."""
    defaults = {
        "candidate_profile": {},
        "scores": {"round1": 0, "round2": 0, "confidence": 0},
        "resume_status": "Awaiting resume upload.",
        "progress_summary": "Setup not started.",
        "current_round": "Resume & Job Setup",
        "strengths": ["Upload your resume to begin personalized analysis."],
        "weak_areas": ["Skill gaps will appear after the first round."],
        "next_steps": ["Upload resume", "Paste job description", "Start Round 1"],
        "roadmap": {},
        "expanded_cards": {},
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)
