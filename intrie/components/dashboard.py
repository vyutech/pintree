"""Dashboard header and summary components."""

import streamlit as st


def render_hero(title: str, description: str) -> None:
    """Render the app hero section."""
    st.markdown(
        f"""
        <section class="intrie-hero">
            <h1>{title}</h1>
            <p>{description}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_strengths_and_gaps(strengths: list[str], gaps: list[str]) -> None:
    """Render high-level strengths and weak areas."""
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Strengths")
        for item in strengths:
            st.write(f"- {item}")
    with col2:
        st.markdown("### Weak Areas")
        for item in gaps:
            st.write(f"- {item}")
