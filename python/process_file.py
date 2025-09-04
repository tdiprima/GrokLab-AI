import os

from dotenv import load_dotenv
from halo import Halo
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
You are an expert technical summarizer who explains key ideas clearly and directly, pairing each idea with its corresponding code.

**Task:**
Summarize the article in plain, scannable text.

* State each essential idea in a short, clear sentence or two.
* If the idea has an associated code example, place the **exact code block** immediately beneath the explanation.
* Do not modify, truncate, or reformat the code.
* Do not use bullet points, numbering, or lists — just a flowing sequence of idea followed by code.

**Output Format:**
Idea 1 (explained in plain text)

```py
[Exact code block if present]
```

Idea 2 (explained in plain text)

```py
[Exact code block if present]
```

...and so on until the article is fully summarized.

**Input:**
{content}

**Output:**
Plain explanation → code → explanation → code.
"""

spinner = Halo(text="Generating response...", spinner="dots", color="magenta")
spinner.start()

try:
    completion = client.chat.completions.create(
        model="grok-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4096,  # Adjust based on expected response length
        temperature=0.5,  # Adjust for creativity vs. focus (0.0-1.0)
    )

    result = completion.choices[0].message.content
    spinner.succeed("Response generated successfully!")
    # ic(result)
except Exception as e:
    spinner.fail(f"Failed to generate response: {str(e)}")
    raise

# Save the response to output file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(result)

print(f"\nResponse has been saved to '{OUTPUT_FILE}'")
