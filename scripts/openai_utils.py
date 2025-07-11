import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.x.ai/v1",
    api_key=os.getenv("GROK_API_KEY")
) 

response = client.chat.completions.create(model="grok-4-0709", messages=[{"role": "user", "content": "Hello, Grok!"}])
print(response.choices[0].message.content)
