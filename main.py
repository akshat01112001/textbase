import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "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"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """Please act as a mental health adviser. I will provide you with a patient looking for guidance and advice on managing their stress, anxiety and other mental health issues. You should use your knowledge of all mental issues and their respective solutions in order to create strategies that the individual can implement for overall improvement. Your tone should be precise, soothing and easy to understand. My first response is "I need your help to cope up with my depression symptoms".
"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history[-2:],
        model="gpt-3.5-turbo",
    )

    return bot_response, state
