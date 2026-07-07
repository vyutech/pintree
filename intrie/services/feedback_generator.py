"""Feedback generation service."""

from services.scoring_engine import calculate_confidence_score


def generate_round_feedback(round_name: str, result: dict, profile: dict) -> dict:
    """Create structured per-round feedback."""
    del profile
    score = result["score"]
    return {
        "round": round_name,
        "strengths": ["Structured thinking", "Role relevance"] if score >= 70 else ["Good baseline understanding"],
        "weaknesses": ["Add deeper technical detail", "Use more concrete examples"],
        "improvement_tips": ["Practice concise frameworks", "Mention metrics and tradeoffs"],
    }


def generate_final_report(profile: dict, round1: dict, round2: dict) -> dict:
    """Combine both rounds into a final summary report."""
    resume_match = 72 if profile["resume_analysis"]["skills"] else 58
    confidence = calculate_confidence_score(resume_match, round1["score"], round2["score"])
    return {
        "round1_score": round1["score"],
        "round2_score": round2["score"],
        "confidence_score": confidence,
        "estimated_hire_chance": f"{confidence}%",
        "key_strengths": round2["feedback"]["strengths"],
        "key_weaknesses": round2["feedback"]["weaknesses"],
        "mistakes_across_rounds": round1["mistakes"] + round2["missed_points"],
        "corrected_answers": [round1["ideal_answer"]] + round2["better_answer_examples"],
        "preparation_plan": ["Review role fundamentals", "Practice mock interviews", "Tighten resume storytelling"],
    }
