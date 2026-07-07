"""Scoring helpers for assessments and final confidence."""


def score_skill_assessment(assessment: dict, answer: str, profile: dict) -> dict:
    """Score round 1 using answer completeness heuristics."""
    del assessment, profile
    word_count = len(answer.split())
    score = min(100, 40 + (word_count // 4))
    return {
        "score": score,
        "ideal_answer": "A strong answer explains approach, assumptions, tradeoffs, and validation steps.",
        "mistakes": ["Answer was too short"] if word_count < 80 else ["Add more measurable outcomes"],
        "missing_concepts": ["Testing", "Edge cases"] if "test" not in answer.lower() else ["Deeper optimization discussion"],
        "time_feedback": "Pace was reasonable." if word_count > 60 else "Use the full time to add depth and examples.",
    }


def calculate_confidence_score(resume_match: int, round1: int, round2: int) -> int:
    """Aggregate scores into a single confidence score."""
    return min(100, int((resume_match * 0.25) + (round1 * 0.35) + (round2 * 0.4)))
