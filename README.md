# Mental Health Adviser Chatbot - GPT-3.5 Turbo

This repository contains a Python script that sets up a chatbot using the OpenAI GPT-3.5 Turbo language model to act as a mental health adviser. The chatbot responds to user messages about stress, anxiety, depression symptoms, and other mental health issues by generating appropriate strategies for coping and improvement.

## Prerequisites

Before running the chatbot script, you need to have the following:

1. Python: Make sure you have Python 3.x installed on your system.

2. OpenAI API Key: You will need a valid API key from OpenAI to access the GPT-3.5 Turbo model. The API key can be hardcoded in the script or stored as an environment variable. Please ensure you have the necessary permissions to interact with the GPT-3.5 Turbo model.

3. Required Libraries: Install the required libraries using the following command:

```
cd textbase
poetry install
```

## Setting Up the API Key

In the chatbot.py script, look for the following section:

```
# Load your OpenAI API key
models.OpenAI.api_key = "API KEY"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")
```

Replace the placeholder API key with your actual API key or uncomment the os.getenv line and set the API key as an environment variable.

## Running the Chatbot

To run the mental health adviser chatbot, simply execute the main.py script using Python:

```
poetry run python textbase/textbase_cli.py test main.py
```

The chatbot will start interacting with you based on the initial system prompt and generate responses using the GPT-3.5 Turbo model.

## Customizing the Chatbot

If you wish to customize the behavior of the chatbot or modify the system prompt, you can do so in the main.py script.

To change the system prompt, modify the SYSTEM_PROMPT variable:

```
SYSTEM_PROMPT = """Please act as a mental health adviser. I will provide you with a patient looking for guidance and advice on managing their stress, anxiety and other mental health issues. You should use your knowledge of all mental issues and their respective solutions in order to create strategies that the individual can implement for overall improvement. Your tone should be precise, soothing and easy to understand. My first response is "I need your help to cope up with my depression symptoms".
"""
```

## Important Notes

- The chatbot's responses are generated using the GPT-3.5 Turbo model, and the quality of responses depends on the model's training and the accuracy of the initial system prompt.

- The chatbot maintains context by using the last two messages in the conversation history.

- Please use this chatbot responsibly and avoid sharing sensitive or personal information.

- Make sure to comply with OpenAI's terms of service and usage policies when using the GPT-3.5 Turbo model.

## License

This project is licensed under the MIT License.

Feel free to use and modify this chatbot for your own purposes. If you encounter any issues or have suggestions for improvements, please feel free to create an issue or pull request. Happy chatting!
