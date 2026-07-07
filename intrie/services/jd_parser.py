"""Job description parsing service."""


def parse_job_description(job_description: str, company: str, role: str) -> dict:
    """Convert raw job input into a small structured summary."""
    lowered = job_description.lower()
    role_type = "coding challenge" if any(word in lowered for word in ["python", "backend", "software", "engineer"]) else "domain case study"
    return {
        "company": company,
        "role": role,
        "role_type": role_type,
        "required_skills": _pick_keywords(lowered),
        "company_expectations": f"{company} appears to value role-ready problem solving, communication, and execution.",
        "job_description_preview": job_description[:1200],
    }


def _pick_keywords(text: str) -> list[str]:
    library = ["python", "sql", "analytics", "product", "design", "security", "leadership", "communication"]
    return [skill for skill in library if skill in text] or ["communication", "problem solving", "ownership"]
