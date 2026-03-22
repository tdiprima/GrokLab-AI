import os
from pathlib import Path

from halo import Halo
from openai import OpenAI

INPUT_FILE = "Wow.txt"
OUTPUT_FILE = "output.md"


def extract_text_from_response(response) -> str:
    """
    Responses API may return structured output.
    This helper safely extracts the text content.
    """
    chunks = []

    # Newer SDK style: response.output is a list of items,
    # each may contain content blocks of different types.
    if getattr(response, "output", None):
        for item in response.output:
            for block in getattr(item, "content", []) or []:
                if getattr(block, "type", None) == "output_text":
                    chunks.append(getattr(block, "text", ""))

    # Fallback: some SDK versions provide convenience `output_text`
    if not chunks and getattr(response, "output_text", None):
        return response.output_text

    return "\n".join([c for c in chunks if c]).strip()


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

    prompt = f"""Read the following text and give it a good filename.
Write a simple version of the chat.
Do this without preamble.

Here's the text:
{content}
"""

    spinner = Halo(text="Generating response...", spinner="dots", color="magenta")
    spinner.start()

    try:
        response = client.responses.create(
            model="grok-4-1-fast-reasoning",
            input=prompt,
            max_output_tokens=4096,
            temperature=0.7,
        )

        result = extract_text_from_response(response)
        if not result:
            raise RuntimeError("Empty response from model (no output_text found).")

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
