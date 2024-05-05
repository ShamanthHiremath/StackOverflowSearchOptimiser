import os
from openai import OpenAI

# Set the API key directly using the OpenAI class
OpenAI.api_key = "PUT YOUR OPENAI API KEY HERE"

# Create the OpenAI client
client = OpenAI()

def chatGPTConvo():
    search_input = input("ENTER THE QUESTION TO BE SEARCHED IN chatgpt: ")

    # Generate chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": search_input,
            }
        ],
        model="gpt-3.5-turbo"
    )

    return chat_completion.choices[0].message.content

print(chatGPTConvo())
