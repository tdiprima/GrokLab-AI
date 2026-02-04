#!/usr/bin/env python3
"""
Process a single input file and extract/reconstruct code from an article.
"""

from pathlib import Path

from llm_processor import summarize_article  #, process_article_to_code

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.md"


def main():
    try:
        content = Path(INPUT_FILE).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} file not found!")
        exit(1)

    result = summarize_article(content)
    # result = process_article_to_code(content)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\nResponse has been saved to '{OUTPUT_FILE}'")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        exit(0)
