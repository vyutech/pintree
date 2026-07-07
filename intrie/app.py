"""Main Streamlit entry point for the Intrie app."""

from pathlib import Path

import streamlit as st

from components.sidebar import render_sidebar
from config.settings import get_settings
from pages import (
    dashboard,
    feedback,
    recommendations,
    resume_setup,
    roadmap,
    round1_skill_assessment,
    round2_technical_interview,
)
from utils.session_manager import initialize_session_state


PAGE_REGISTRY = {
    "Dashboard": dashboard.render,
    "Resume & Job Setup": resume_setup.render,
    "Round 1: Skill Assessment": round1_skill_assessment.render,
    "Round 2: Technical Interview": round2_technical_interview.render,
    "Feedback & Scores": feedback.render,
    "Roadmap": roadmap.render,
    "Recommended Companies": recommendations.render,
}


def load_css(stylesheet: Path) -> None:
    """Inject local stylesheet into the Streamlit app."""
    if stylesheet.exists():
        st.markdown(f"<style>{stylesheet.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def main() -> None:
    """Run the Intrie Streamlit application."""
    settings = get_settings()
    st.set_page_config(
        page_title=settings.app_name,
        page_icon="assets/logo.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    load_css(settings.stylesheet_path)
    initialize_session_state()

    selected_page = render_sidebar(list(PAGE_REGISTRY))
    PAGE_REGISTRY[selected_page]()


if __name__ == "__main__":
    main()
