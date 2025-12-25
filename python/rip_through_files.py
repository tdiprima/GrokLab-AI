#!/usr/bin/env python3
"""
Process multiple input files (i1.txt, i2.txt, etc.) and generate summaries.
"""

import os
import re
import time

from llm_processor import summarize_article


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

        output_text = summarize_article(input_text)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_text)

        print(f"✅ {filename} → {output_filename}")
        time.sleep(2)


if __name__ == "__main__":
    # Change this if needed, or pass via CLI later
    target_directory = "."
    main(target_directory)
