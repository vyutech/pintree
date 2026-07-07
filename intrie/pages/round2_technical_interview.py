"""Round 2 conversational interview page."""

import streamlit as st

from components.chat_interface import render_chat, render_chat_input
from components.timer import render_round_timer
from services.feedback_generator import generate_round_feedback
from services.interviewer import generate_next_question, score_interview_transcript


def render() -> None:
    """Render the round 2 interview chat flow."""
    st.title("Round 2: Technical Interview")
    profile = st.session_state.get("candidate_profile")
    if not profile:
        st.warning("Complete Resume & Job Setup before starting the technical interview.")
        return

    render_round_timer("round2_timer")
    st.session_state.setdefault("chat_history", [])

    if not st.session_state["chat_history"]:
        opening = generate_next_question(profile, [])
        st.session_state["chat_history"].append({"role": "assistant", "content": opening})

    render_chat(st.session_state["chat_history"])
    user_reply = render_chat_input("Answer the interviewer")

    if user_reply:
        st.session_state["chat_history"].append({"role": "user", "content": user_reply})
        follow_up = generate_next_question(profile, st.session_state["chat_history"])
        st.session_state["chat_history"].append({"role": "assistant", "content": follow_up})
        st.rerun()

    if st.button("End interview and score", type="primary"):
        result = score_interview_transcript(st.session_state["chat_history"], profile)
        feedback = generate_round_feedback("round2", result, profile)
        st.session_state["round2_result"] = result | {"feedback": feedback}
        st.session_state["scores"]["round2"] = result["score"]
        st.session_state["scores"]["confidence"] = min(
            100, int((st.session_state["scores"]["round1"] * 0.4) + (result["score"] * 0.6))
        )
        st.session_state["progress_summary"] = "Both interview rounds completed."
        st.session_state["current_round"] = "Feedback & Scores"
        st.success("Round 2 scored.")
        st.json(st.session_state["round2_result"])
