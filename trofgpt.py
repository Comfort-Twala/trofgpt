import openai
import prompt_toolkit
from decouple import config

# Initialize the API key
openai.api_key = config("API_KEY")

def chat_with_gpt(prompt):
    """
    Sends the user's prompt to the ChatGPT model and returns the model's response
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response["choices"][0]["text"]

while True:
    # Create an interactive prompt for the user to input text
    user_prompt = prompt_toolkit.prompt("You: ")

    if user_prompt in ["exit", "quit"]:
        break

    # Send the user's input to the ChatGPT model and display the response
    response = chat_with_gpt(user_prompt)
    print(f"ChatGPT: {response}")
