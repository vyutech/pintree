"""Validation helpers."""


def validate_setup_inputs(uploaded_resume, company: str, role: str, job_description: str) -> list[str]:
    """Validate required setup inputs."""
    errors = []
    if uploaded_resume is None:
        errors.append("Please upload a resume in PDF or DOCX format.")
    if not company.strip():
        errors.append("Company name is required.")
    if not role.strip():
        errors.append("Role or title is required.")
    if not job_description.strip():
        errors.append("Job description is required.")
    return errors
