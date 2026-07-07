"""Interview flow generation service."""


def build_interview_context(profile: dict) -> dict:
    """Build shared context used across rounds."""
    return {
        "role": profile["role"],
        "company": profile["company"],
        "skills": profile["resume_analysis"]["skills"],
        "required_skills": profile["job_analysis"]["required_skills"],
    }
