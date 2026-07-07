"""Resume and job setup page."""

import streamlit as st

from components.upload_section import render_upload_inputs
from services.jd_parser import parse_job_description
from services.resume_parser import parse_resume
from services.roadmap_generator import build_interview_plan
from utils.file_handler import save_uploaded_file
from utils.validators import validate_setup_inputs


def render() -> None:
    """Render resume and job setup workflow."""
    st.title("Resume & Job Setup")
    uploaded_resume, company, role, job_description = render_upload_inputs()

    if st.button("Analyze profile", type="primary"):
        errors = validate_setup_inputs(uploaded_resume, company, role, job_description)
        if errors:
            for error in errors:
                st.error(error)
            return

        saved_path = save_uploaded_file(uploaded_resume, "resumes")
        resume_analysis = parse_resume(saved_path)
        job_analysis = parse_job_description(job_description, company, role)
        interview_plan = build_interview_plan(resume_analysis, job_analysis)

        st.session_state["candidate_profile"] = {
            "company": company,
            "role": role,
            "job_description": job_description,
            "resume_path": str(saved_path),
            "resume_analysis": resume_analysis,
            "job_analysis": job_analysis,
        }
        st.session_state["resume_status"] = "Resume analyzed and interview plan generated."
        st.session_state["progress_summary"] = "Setup completed. Round 1 is ready."
        st.session_state["current_round"] = "Round 1: Skill Assessment"
        st.session_state["roadmap"] = interview_plan["roadmap"]
        st.session_state["next_steps"] = interview_plan["next_steps"]
        st.success("Profile analysis complete.")

        st.subheader("Resume Analysis")
        st.json(resume_analysis)
        st.subheader("Job Analysis")
        st.json(job_analysis)
        st.subheader("Interview Plan")
        st.json(interview_plan)
