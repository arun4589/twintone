from backend.prompt_engineering import casual_prompt, formal_prompt

def test_prompt_formatting():
    q = "What is AI?"
    assert "chatting" in casual_prompt(q)
    assert "formal" in formal_prompt(q)
