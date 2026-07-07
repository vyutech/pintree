"""Company recommendation service."""

from config.prompts import load_prompt
from services.groq_service import GroqService


def recommend_companies(profile: dict, final_report: dict | None) -> list[dict]:
    """Return role-aligned company suggestions."""
    role = profile["role"]
    skills = profile["resume_analysis"]["skills"][:3] or ["problem solving"]
    confidence = final_report["confidence_score"] if final_report else 65
    difficulty = "Medium" if confidence >= 65 else "Foundational"
    fallback = [
        {
            "company": "Atlassian",
            "role": role,
            "why_fit": f"Your background shows alignment with collaborative product delivery and {', '.join(skills)}.",
            "skills_to_improve": ["System design", "Interview storytelling"],
            "difficulty": difficulty,
        },
        {
            "company": "HubSpot",
            "role": role,
            "why_fit": "Your experience appears well suited to customer-focused, execution-heavy teams.",
            "skills_to_improve": ["Metrics communication", "Role-specific depth"],
            "difficulty": difficulty,
        },
        {
            "company": "Zoho",
            "role": role,
            "why_fit": "The profile suggests a practical match for generalist execution and hands-on ownership.",
            "skills_to_improve": ["Tradeoff framing", "Technical precision"],
            "difficulty": "Accessible",
        },
    ]
    groq = GroqService()
    prompt = load_prompt("company_recommendation.txt")
    user_prompt = (
        f"Role: {role}\n"
        f"Resume skills: {skills}\n"
        f"Confidence score: {confidence}\n"
        "Return JSON as a list of 3 objects with company, role, why_fit, skills_to_improve, and difficulty."
    )
    response = groq.complete_json(prompt, user_prompt, {"recommendations": fallback})
    return response.get("recommendations", fallback)
