# Adapted from: https://docs.x.ai/docs/tutorial
import base64
import os
from pathlib import Path

from xai_sdk import Client
from xai_sdk.chat import image, user

INPUT_FILE = "input.png"
OUTPUT_FILE = "output.md"
PROMPT = """
I have an image of a graph that I want you to analyze.

What are the key insights or implications about this graph?  Use simple language, bullet points, and emojis.
"""


client = Client(
    api_key=os.getenv("XAI_API_KEY"),
    timeout=3600,  # Override default timeout with longer timeout for reasoning models
)

# Read and encode the image as base64
with open(INPUT_FILE, "rb") as img_file:
    img_data = base64.b64encode(img_file.read()).decode("utf-8")
    img_url = f"data:image/png;base64,{img_data}"

chat = client.chat.create(model="grok-4")
chat.append(user(PROMPT, image(img_url)))

response = chat.sample()
# print(response.content)

# Save the response to a file
Path(OUTPUT_FILE).write_text(response.content)

print(f"Response saved to {OUTPUT_FILE}")
