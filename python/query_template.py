"""
Adapted from: https://docs.x.ai/docs/tutorial
Requires-Python >=3.10:
$ pip install xai-sdk
"""
import os

from xai_sdk import Client
from xai_sdk.chat import user, system

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=3600,  # Override default timeout with longer timeout for reasoning models
)

chat = client.chat.create(model="grok-4")
chat.append(system("You are Grok, a highly intelligent, helpful AI assistant."))
chat.append(user("What is the meaning of life, the universe, and everything?"))

response = chat.sample()
# print(response.content)

# Save the response to a file
with open("response.md", "w") as f:
    f.write(response.content)

print("Response saved to response.md")
