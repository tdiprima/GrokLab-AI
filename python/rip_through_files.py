import os
import re
import time

from halo import Halo
from openai import OpenAI


def process_text(text: str) -> str:
    """
    Put your custom processing logic here.
    Example below just wraps text in Markdown.
    """
    content = text.strip()
    XAI_API_KEY = os.environ.get("XAI_API_KEY")

    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )

    prompt = f"""This article is too long for me to read through completely. 
    Can you give me the essential points in a way that's easy to scan and remember?
    Use bullet points and emojis.
    If there's code, include the code in markdown format.
    If the code is more than 3 lines long, give it a good filename.
    Give me a good filename for your respose.  Do not use the word 'summary' in the filename.

    Do this without preamble.

    Here's the article:
    {content}
    """

    spinner = Halo(text="Generating response...", spinner="dots", color="magenta")
    spinner.start()

    try:
        completion = client.chat.completions.create(
            model="grok-4-1-fast-reasoning",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=8192,
            temperature=0.7,
        )

        result = completion.choices[0].message.content
        spinner.succeed("Response generated successfully!")
    except Exception as e:
        spinner.fail(f"Failed to generate response: {e}")
        raise

    return result


def main(directory: str):
    # Match files like i1.txt, i2.txt, etc.
    input_pattern = re.compile(r"i(\d+)\.txt$")

    for filename in os.listdir(directory):
        match = input_pattern.match(filename)
        if not match:
            continue

        index = match.group(1)
        input_path = os.path.join(directory, filename)
        output_filename = f"o{index}.md"
        output_path = os.path.join(directory, output_filename)

        with open(input_path, "r", encoding="utf-8") as f:
            input_text = f.read()

        output_text = process_text(input_text)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_text)

        print(f"✅ {filename} → {output_filename}")
        time.sleep(2)


if __name__ == "__main__":
    # Change this if needed, or pass via CLI later
    target_directory = "."
    main(target_directory)
