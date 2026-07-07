from services.scoring_engine import calculate_confidence_score, score_skill_assessment


def test_score_skill_assessment_returns_bounded_score() -> None:
    result = score_skill_assessment({}, "This answer covers testing tradeoffs and metrics." * 10, {})
    assert 0 <= result["score"] <= 100


def test_calculate_confidence_score_returns_integer() -> None:
    assert calculate_confidence_score(70, 80, 90) == 82
