def casual_prompt(query: str) -> str:
    return f"Explain this like you're chatting with a friend: {query}"

def formal_prompt(query: str) -> str:
    return f"Provide a detailed, formal explanation of the following topic: {query}"
