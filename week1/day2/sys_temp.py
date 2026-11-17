import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role = "user"
prompt = "Hello bro what are you doing today?"

# Using a system role to provide context for the model
mes_system = {
    "role": "system",
    "content": "You are my rude office boss."
}

message = {
    "role": role,
    "content": prompt,
}

messages = [mes_system, message]

# Setting temperature by default is 0. You can set it to any value between 0 and 2 to control the randomness of the output.
response = client.chat.completions.create(model=model, messages=messages, temperature=1)
print(response.choices[0].message.content)