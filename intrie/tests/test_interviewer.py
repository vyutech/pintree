from services.interviewer import generate_next_question, score_interview_transcript


def test_generate_next_question_references_role() -> None:
    profile = {"role": "Backend Engineer", "company": "Intrie"}
    question = generate_next_question(profile, [])
    assert "Backend Engineer" in question


def test_score_interview_transcript_returns_feedback() -> None:
    profile = {"role": "Backend Engineer"}
    history = [{"role": "user", "content": "I built APIs and improved reliability across services."}]
    result = score_interview_transcript(history, profile)
    assert "technical_feedback" in result
