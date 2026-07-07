"""Technical interviewer service."""

from config.prompts import load_prompt
from services.groq_service import GroqService


def generate_next_question(profile: dict, history: list[dict[str, str]]) -> str:
    """Generate the next interview question based on conversation state."""
    fallback = _fallback_question(profile, history)
    groq = GroqService()
    prompt = load_prompt("technical_interview.txt")
    user_prompt = (
        f"Role: {profile['role']}\n"
        f"Company: {profile['company']}\n"
        f"Resume skills: {profile['resume_analysis']['skills']}\n"
        f"Conversation history: {history}\n"
        "Return only the next interviewer question."
    )
    response = groq.complete_text(prompt, user_prompt).strip()
    return response or fallback


def score_interview_transcript(history: list[dict[str, str]], profile: dict) -> dict:
    """Score the interview transcript using simple heuristics."""
    user_messages = [item["content"] for item in history if item["role"] == "user"]
    answer_length = sum(len(message.split()) for message in user_messages)
    score = min(100, 55 + (answer_length // 12))
    return {
        "score": score,
        "communication_feedback": "Answers were clear and structured." if answer_length > 80 else "Add more detail and examples.",
        "technical_feedback": f"Keep tying your answers back to {profile['role']} requirements.",
        "missed_points": ["Quantified outcomes", "Deeper tradeoff analysis"] if answer_length < 120 else ["Stronger system design detail"],
        "better_answer_examples": ["Use STAR framing plus technical tradeoffs."],
    }


def _fallback_question(profile: dict, history: list[dict[str, str]]) -> str:
    if len(history) < 2:
        return (
            f"Walk me through a project from your resume that best matches the {profile['role']} role at "
            f"{profile['company']}, and explain the technical decisions you made."
        )
    if history and history[-1]["role"] == "user" and len(history) < 6:
        return "What tradeoff did you make in that project, and what would you change if you rebuilt it today?"
    return "How would you communicate risk or uncertainty to your teammates during delivery?"
