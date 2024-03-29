# How to Build Your Own ChatGPT Terminal App: A Beginner's Guide

Ever wanted to chat with AI directly from your command line,
regardless of whether you're on a Mac, Linux, or Windows machine?
This beginner-friendly guide will walk you through creating a ChatGPT terminal application, step by step.
It's designed to be straightforward and easy to follow, even if you're just dipping your toes into coding.

## Prerequisites

Before we dive into the coding part, make sure you have the following:
- Python installed on your system. This guide uses Python 3.8 or above.
- A code editor of your choice.
- An OpenAI API key. If you don't have one, you can get it by signing up at [OpenAI](https://openai.com/api/).

## Step 1: Kickstart Your Project

First, create a new directory for your project. Open your terminal and run:

```bash
mkdir terminal_chat_gpt
cd terminal_chat_gpt
```

Within this directory, we'll create a virtual environment. 
This environment is a self-contained directory that contains a Python installation for a particular version of Python, 
plus a number of additional packages.

```bash
# For Mac/Linux
python3 -m venv .venv

# For Windows
python -m venv .venv
```

Activate the virtual environment:

```bash
# For Mac/Linux
source .venv/bin/activate

# For Windows
.\.venv\Scripts\activate
```

## Step 2: Managing Dependencies

Create a `requirements.txt` file in your project directory and add the following line:

```
openai
python-dotenv
```

These are the Python packages we'll use: `openai` for interacting with the OpenAI API and `python-dotenv` for loading
our API key from an environment file.

Install the dependencies by running:

```bash
pip install -r requirements.txt
```

## Step 3: Keeping Your API Key Safe

Create a `.env` file in your project directory. Add your OpenAI API key like so:

```
OPENAI_API_KEY='Your-OpenAI-API-Key-Here'
```

**Important:** Never hard-code your API keys directly into your scripts. Always use environment variables or secure vaults.

## Step 4: Building the ChatGPT Application

Create a Python script named `chat_gpt_terminal.py`. Open it in your code editor and add the following code:

```python
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

```

## Step 5: Running Your Application

In your terminal, run:

```bash
python chat_gpt_terminal.py
```

You'll now be able to interact with ChatGPT directly from your terminal.
Type your questions or statements, and see how GPT responds.
To exit, simply type `exit`.

## Where to Find the Final Code

You can find the final code for this project at [https://github.com/Sokahr/terminal_chat_gpt](https://github.com/Sokahr/terminal_chat_gpt).
Feel free to download, explore, and modify it as you wish.

## Conclusion

Congratulations!
You've just built your own ChatGPT application for the terminal. 
This project not only gives you a direct line to one of the most powerful language models available
but also serves as a great starting point for more complex projects. 
Whether you're interested in integrating ChatGPT into other applications,
or simply exploring AI and natural language processing, the skills you've developed here will serve you well. 
Happy coding!
