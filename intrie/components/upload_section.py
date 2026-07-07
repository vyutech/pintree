"""Upload section component."""

import streamlit as st


def render_upload_inputs() -> tuple:
    """Render the resume and job setup inputs."""
    uploaded_resume = st.file_uploader("Upload resume", type=["pdf", "docx"])
    company = st.text_input("Company name")
    role = st.text_input("Role or title")
    job_description = st.text_area("Paste the job description", height=220)
    return uploaded_resume, company, role, job_description
