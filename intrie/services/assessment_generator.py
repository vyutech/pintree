"""Round 1 assessment generation."""

from config.prompts import load_prompt
from services.groq_service import GroqService


def generate_assessment(profile: dict) -> dict:
    """Generate a role-aware assessment prompt with a Groq-backed fallback."""
    role = profile["role"]
    role_type = profile["job_analysis"]["role_type"]
    fallback = _fallback_assessment(role, role_type)
    groq = GroqService()
    prompt = load_prompt("skill_assessment.txt")
    user_prompt = (
        f"Role: {role}\n"
        f"Company: {profile['company']}\n"
        f"Required skills: {profile['job_analysis']['required_skills']}\n"
        f"Resume skills: {profile['resume_analysis']['skills']}\n"
        "Return valid JSON with title, prompt, and ideal_answer."
    )
    return groq.complete_json(prompt, user_prompt, fallback)


def _fallback_assessment(role: str, role_type: str) -> dict:
    task_map = {
        "coding challenge": (
            "Build a small API design outline and explain how you would implement it.",
            "Outline the endpoint design, data model, tradeoffs, and how you would validate correctness.",
        ),
        "domain case study": (
            "Analyze a realistic business or product scenario relevant to the role.",
            "Explain your approach, assumptions, and the metrics you would use to evaluate success.",
        ),
    }
    title, prompt = task_map.get(role_type, task_map["domain case study"])
    return {"title": f"{role} Assessment", "prompt": prompt, "ideal_answer": title}
