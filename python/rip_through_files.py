#!/usr/bin/env python3
"""
Process multiple input files (i1.txt, i2.txt, etc.) and generate summaries.
"""

import re
import time
from pathlib import Path

from llm_processor import summarize_article


def main(directory: str):
    # Match files like i1.txt, i2.txt, etc.
    input_pattern = re.compile(r"i(\d+)\.txt$")

    for input_path in Path(directory).iterdir():
        match = input_pattern.match(input_path.name)
        if not match:
            continue

        index = match.group(1)
        output_path = input_path.with_name(f"o{index}.md")

        input_text = input_path.read_text(encoding="utf-8")
        output_text = summarize_article(input_text)
        output_path.write_text(output_text, encoding="utf-8")

        print(f"✅ {input_path.name} → {output_path.name}")
        time.sleep(2)


if __name__ == "__main__":
    # Change this if needed, or pass via CLI later
    target_directory = "."
    main(target_directory)
