import os

from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)
messages = []


def chat_with_gpt(prompt):
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=150,
        n=1,
        temperature=0.5
    )
    # Storing the response in the list of massages so the chat will remember what was said in the conversation before.
    messages.append(response.choices[0].message)
    return response.choices[0].message.content


def main():
    print("Welcome to the Terminal ChatGPT, please enter exit if you had enough!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        message = chat_with_gpt(user_input)
        print(f"GPT: {message}")


if __name__ == "__main__":
    main()
