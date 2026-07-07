from services.feedback_generator import generate_final_report


def test_generate_final_report_contains_confidence() -> None:
    profile = {"resume_analysis": {"skills": ["python"]}}
    round1 = {"score": 70, "mistakes": [], "ideal_answer": "Ideal", "feedback": {"strengths": [], "weaknesses": []}}
    round2 = {
        "score": 80,
        "missed_points": [],
        "better_answer_examples": ["Example"],
        "feedback": {"strengths": ["Clarity"], "weaknesses": ["Depth"]},
    }
    report = generate_final_report(profile, round1, round2)
    assert "confidence_score" in report
