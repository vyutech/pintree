"""Chat interface components."""

import streamlit as st


def render_chat(history: list[dict[str, str]]) -> None:
    """Render chat messages from conversation history."""
    for message in history:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def render_chat_input(prompt: str = "Share your answer") -> str | None:
    """Render chat input box."""
    return st.chat_input(prompt)
