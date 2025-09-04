"""
Adapted from: https://docs.x.ai/docs/tutorial
Requires-Python >=3.10:
$ pip install xai-sdk
"""

import os

from halo import Halo
from xai_sdk import Client
from xai_sdk.chat import system, user

client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=3600,  # Override default timeout with longer timeout for reasoning models
)

PROMPT = """
What is the meaning of life, the universe, and everything?
"""

chat = client.chat.create(model="grok-4")
chat.append(system("You are Grok, a highly intelligent, helpful AI assistant."))
chat.append(user(PROMPT))

spinner = Halo(text="Generating response...", spinner="dots", color="magenta")
spinner.start()

try:
    response = chat.sample()
    spinner.succeed("Response generated successfully!")
except Exception as e:
    spinner.fail(f"Failed to generate response: {str(e)}")
    raise
# print(response.content)

filename = "response.md"

# Save the response to a file
with open(filename, "w") as f:
    f.write(response.content)

print(f"Response saved to {filename}")
