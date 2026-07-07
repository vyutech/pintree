"""Company recommendations page."""

import streamlit as st

from services.recommendation_engine import recommend_companies


def render() -> None:
    """Render recommended companies."""
    st.title("Recommended Companies")
    profile = st.session_state.get("candidate_profile")
    final_report = st.session_state.get("final_report")

    if not profile:
        st.warning("Complete setup first to unlock recommendations.")
        return

    recommendations = recommend_companies(profile, final_report)
    for company in recommendations:
        with st.container(border=True):
            st.subheader(f"{company['company']} - {company['role']}")
            st.write(company["why_fit"])
            st.caption(f"Difficulty: {company['difficulty']}")
            st.write("Skills to improve:")
            for skill in company["skills_to_improve"]:
                st.write(f"- {skill}")
