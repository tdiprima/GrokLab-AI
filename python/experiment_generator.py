"""
Prompt adapted from:
https://levelup.gitconnected.com/this-chatgpt-prompt-was-so-good-i-saved-it-in-3-places-6910bf07f3d2
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'README.md'

load_dotenv()

XAI_API_KEY = os.getenv('XAI_API_KEY')

if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY environment variable is not set")

try:
    with open(INPUT_FILE, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: {INPUT_FILE} file not found!")
    exit(1)

client = OpenAI(
  api_key=XAI_API_KEY,
  base_url="https://api.x.ai/v1",
)

prompt = f"""You are a world-class software engineer with deep expertise in Python, JavaScript, and systems design.
When I provide any raw developer resource (blog post, GitHub issue, discussion thread, or README), you will output exactly 6 sections:

1. TL;DR - A concise, technical summary, in bullet points, and simple language, with emojis.
2. Code Patterns / Gotchas Mentioned - Key idioms, anti-patterns, and warnings.
3. Things To Try Myself - 2-3 small hands-on project ideas inspired by the resource.
4. A good name for the new GitHub repository based on section 3.
5. Related Concepts I Should Look Into - A bullet list of 3-5 deeper topics.
6. Python Equivalents - If examples use another language, sketch the core concepts in Python (no full rewrites).

Be concise, use clear, example-driven language, and assume I already know the basics.

Here's the content:
{content}
"""

completion = client.chat.completions.create(
  model="grok-4-0709",
  messages=[
    {"role": "user", "content": prompt}
  ],
  max_tokens=4096,
  temperature=0.2
)

print("Response:", completion.choices[0].message.content)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(completion.choices[0].message.content)

print(f"\nResponse has been saved to '{OUTPUT_FILE}'")
