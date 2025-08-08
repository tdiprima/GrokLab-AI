import os
from dotenv import load_dotenv
from openai import OpenAI

# Configuration - modify these values as needed
INPUT_FILE = 'input.txt'  # Change this to your input file name
OUTPUT_FILE = 'output.md'  # Change this to your desired output file name

# Load environment variables
load_dotenv()

# Get API key from environment
XAI_API_KEY = os.getenv('XAI_API_KEY')

if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY environment variable is not set")

# Read the input file
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

# Create the prompt - modify this section based on your needs
prompt = f"""Please process the following content and provide a response based on the requirements:

Content to process:
{content}

Instructions:
- Provide a detailed and comprehensive response
- Format the output appropriately
- Include all necessary components as described in the content

Please provide your response below:"""

completion = client.chat.completions.create(
  model="grok-4",
  messages=[
    {"role": "user", "content": prompt}
  ],
  max_tokens=4096,  # Adjust based on expected response length
  temperature=0.2   # Adjust for creativity vs. focus (0.0-1.0)
)

# print("Response:", completion.choices[0].message.content)

# Save the response to output file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(completion.choices[0].message.content)

print(f"\nResponse has been saved to '{OUTPUT_FILE}'")
