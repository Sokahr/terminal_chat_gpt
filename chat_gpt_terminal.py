import os
import openai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
openai.api_key = api_key

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.9,
    )
    message = response.choices[0].text.strip()
    return message

def main():
    print("Welcome to the Terminal ChatGPT!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("GPT: ", response)

if __name__ == "__main__":
    main()
