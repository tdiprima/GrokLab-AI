"""
Shared module for LLM text processing using the xAI API.
"""

import os

from halo import Halo
from openai import OpenAI


def get_client() -> OpenAI:
    """
    Create and return an OpenAI client configured for xAI.

    Raises:
        ValueError: If XAI_API_KEY environment variable is not set.
    """
    api_key = os.environ.get("XAI_API_KEY")

    if not api_key:
        raise ValueError("XAI_API_KEY environment variable is not set")

    return OpenAI(
        api_key=api_key,
        base_url="https://api.x.ai/v1",
    )


def call_llm(
    prompt: str,
    model: str = "grok-4-1-fast-reasoning",
    max_tokens: int = 8192,
    temperature: float = 0.7,
    show_spinner: bool = True,
) -> str:
    """
    Send a prompt to the LLM and return the response.

    Args:
        prompt: The prompt to send to the model.
        model: The model identifier to use.
        max_tokens: Maximum tokens in the response.
        temperature: Sampling temperature.
        show_spinner: Whether to show a loading spinner.

    Returns:
        The model's response text.

    Raises:
        ValueError: If API key is not configured.
        Exception: If the API call fails.
    """
    client = get_client()

    spinner = None
    if show_spinner:
        spinner = Halo(text="Generating response...", spinner="dots", color="magenta")
        spinner.start()

    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        result = completion.choices[0].message.content

        if spinner:
            spinner.succeed("Response generated successfully!")

        return result

    except Exception as e:
        if spinner:
            spinner.fail(f"Failed to generate response: {e}")
        raise


# def process_article_to_code(content: str, **kwargs) -> str:
#     """
#     Process an article and extract/reconstruct code snippets.

#     Args:
#         content: The article text to process.
#         **kwargs: Additional arguments passed to call_llm.

#     Returns:
#         The processed result with working code.
#     """
#     prompt = f"""Read the following article, and piece together the code snippets to make one working script.
#     Include code comments.
#     Give it a good filename.
#     If code is missing, do your best to fill it in.  I expect working code.

# Do this without preamble.

# Here's the article:
# {content}
# """
#     return call_llm(prompt, **kwargs)


def summarize_article(content: str, **kwargs) -> str:
    """
    Summarize an article with bullet points and emojis.

    Args:
        content: The article text to summarize.
        **kwargs: Additional arguments passed to call_llm.

    Returns:
        The summarized content.
    """
    prompt = f"""Please summarize this article in an ADHD-friendly way.
    Make it stupidly simple to understand.
    Write in clear, complete sentences with proper grammar; avoid shorthand or fragmented phrasing.
    Write using simple language and emojis.
    Include the hyperlink at the top.
    If there's code, include the code in markdown format.
    If the code is more than 3 lines long, give it a good filename.
    At the end, write a TL;DR in bullet points.
    Give me a good filename for your respose.
    Do not use the word 'summary' or 'cheatsheet' in the filename.

    Do this without preamble.

    Here's the article:
    {content}
    """
    return call_llm(prompt, **kwargs)
