"""Round 1 skill assessment page."""

import streamlit as st

from components.timer import render_round_timer
from services.assessment_generator import generate_assessment
from services.feedback_generator import generate_round_feedback
from services.scoring_engine import score_skill_assessment


def render() -> None:
    """Render the round 1 assessment experience."""
    st.title("Round 1: Skill Assessment")
    profile = st.session_state.get("candidate_profile")
    if not profile:
        st.warning("Complete Resume & Job Setup before starting the assessment.")
        return

    render_round_timer("round1_timer")
    assessment = generate_assessment(profile)
    st.subheader(assessment["title"])
    st.write(assessment["prompt"])
    answer = st.text_area("Submit your answer", height=220, key="round1_answer")

    if st.button("Score Round 1", type="primary"):
        result = score_skill_assessment(assessment, answer, profile)
        feedback = generate_round_feedback("round1", result, profile)
        st.session_state["round1_result"] = result | {"feedback": feedback}
        st.session_state["scores"]["round1"] = result["score"]
        st.session_state["strengths"] = feedback["strengths"]
        st.session_state["weak_areas"] = feedback["weaknesses"]
        st.session_state["current_round"] = "Round 2: Technical Interview"
        st.success("Round 1 scored.")
        st.json(st.session_state["round1_result"])
