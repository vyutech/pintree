"""Roadmap and interview plan generation."""

from config.prompts import load_prompt
from services.groq_service import GroqService


def build_interview_plan(resume_analysis: dict, job_analysis: dict) -> dict:
    """Create an initial personalized interview plan after setup."""
    overlapping_skills = sorted(set(resume_analysis["skills"]) & set(job_analysis["required_skills"]))
    return {
        "match_summary": f"Detected {len(overlapping_skills)} overlapping skill areas.",
        "roadmap": {
            "skills_to_improve": job_analysis["required_skills"][:4],
            "study_topics": ["Role fundamentals", "Project storytelling", "Tradeoff analysis"],
        },
        "next_steps": [
            "Complete Round 1 under the timer",
            "Practice concise, metric-backed answers",
            "Prepare one strong resume project story",
        ],
    }


def generate_learning_roadmap(profile: dict, final_report: dict | None) -> dict:
    """Generate a broader roadmap using available profile and report data."""
    weak_areas = final_report["key_weaknesses"] if final_report else ["Technical depth", "Communication clarity"]
    fallback = {
        "skills_to_improve": weak_areas,
        "topics_to_study": profile["job_analysis"]["required_skills"][:4] or ["Problem solving"],
        "practice_tasks": ["Timed mock interview", "One case study per week", "Rewrite project stories with metrics"],
        "suggested_timeline": ["Week 1: fundamentals", "Week 2: interview drills", "Week 3: targeted mock sessions"],
        "resume_improvements": ["Highlight role-relevant impact", "Surface technical ownership earlier"],
        "communication_tips": ["Lead with context, action, outcome", "State tradeoffs directly"],
    }
    groq = GroqService()
    prompt = load_prompt("roadmap.txt")
    user_prompt = (
        f"Role: {profile['role']}\n"
        f"Required skills: {profile['job_analysis']['required_skills']}\n"
        f"Weak areas: {weak_areas}\n"
        "Return JSON with skills_to_improve, topics_to_study, practice_tasks, suggested_timeline, "
        "resume_improvements, and communication_tips."
    )
    return groq.complete_json(prompt, user_prompt, fallback)
