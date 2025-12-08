import os
from pathlib import Path

from halo import Halo
from openai import OpenAI

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.md"


def main():
    XAI_API_KEY = os.environ.get("XAI_API_KEY")

    if not XAI_API_KEY:
        raise ValueError("XAI_API_KEY environment variable is not set")

    try:
        content = Path(INPUT_FILE).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} file not found!")
        exit(1)

    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )

    prompt = f"""This article is too long for me to read through completely.
Can you give me the essential points in a way that's easy to scan and remember?
Do it without preamble.
Use simple language and and emojis.
Make sure you grab all code examples.
If a code example does not exist, make one up.
Prefer ```py block over single tick `.

Here's the article:
{content}
"""

    spinner = Halo(text="Generating response...", spinner="dots", color="magenta")
    spinner.start()

    try:
        completion = client.chat.completions.create(
            model="grok-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096,
            temperature=0.5,
        )

        result = completion.choices[0].message.content
        spinner.succeed("Response generated successfully!")
    except Exception as e:
        spinner.fail(f"Failed to generate response: {e}")
        raise

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\nResponse has been saved to '{OUTPUT_FILE}'")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        exit(0)
