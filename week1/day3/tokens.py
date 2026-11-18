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

prompt1 = "Hii"
prompt2 = "Tell me about yourself in 100 tokens"
prompt3 = "Describe the future of AI in 1000 tokens"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role": role,
        "content": prompt,
    }

    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages, max_tokens=500)
    usage = response.usage

    print(f"Prompt: {prompt} -> Prompt tokens: {usage.prompt_tokens} -> Completion tokens: {usage.completion_tokens} -> Total tokens: {usage.total_tokens} -> Finish Reason: {response.choices[0].finish_reason}")
    print(response.choices[0].message.content)