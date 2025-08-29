import os

from dotenv import load_dotenv
from icecream import ic
from openai import OpenAI

# Configuration - modify these values as needed
INPUT_FILE = "input.txt"  # Change this to your input file name
OUTPUT_FILE = "output.md"  # Change this to your desired output file name

# Load environment variables
load_dotenv()

# Get API key from environment
XAI_API_KEY = os.getenv("XAI_API_KEY")

if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY environment variable is not set")

# Read the input file
try:
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: {INPUT_FILE} file not found!")
    exit(1)

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

# Create the prompt - modify this section based on your needs
prompt = f"""**Role:**
You are an expert technical summarizer who extracts key insights and organizes them into a concise, easy-to-scan format.

**Task:**
Summarize the given article into essential points that are quick to read and easy to remember.

* Highlight the main arguments, insights, and takeaways in **bullet points**.
* Always preserve section headers or themes if present.
* If the article contains **example code**, include the code exactly as written — do not truncate, shorten, or modify it.
* Clearly label code blocks and separate them from summary text.

**Output Format:**

* Title (if available)
* 5-10 key points (bulleted)
* All example code blocks, shown exactly as they appear in the text

**Input:**
{content}

**Output:**

* 📌 Essential points in bullets
* 💻 Code examples (verbatim, inside code blocks)
"""

completion = client.chat.completions.create(
    model="grok-4",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=4096,  # Adjust based on expected response length
    temperature=0.5,  # Adjust for creativity vs. focus (0.0-1.0)
)

result = completion.choices[0].message.content
# ic(result)

# Save the response to output file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(result)

print(f"\nResponse has been saved to '{OUTPUT_FILE}'")
