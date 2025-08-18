"""
Prompt grok with "Summarize a recent PubMed article on Major Depression,"
measure the response time, and check for valid citations.
Display usage statistics like total tokens, etc.
author: tdiprima
"""

import os
import re
import time

import requests


# Grok API response
def call_grok_api(query):
    api_key = os.getenv("GROK_API_KEY")  # Get from console.x.ai
    if not api_key:
        raise ValueError("GROK_API_KEY environment variable is not set")

    url = "https://api.x.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"messages": [{"role": "user", "content": query}], "model": "grok-4"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        return {
            "summary": data["choices"][0]["message"]["content"],
            "usage_stats": data.get("usage", {}),
        }
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return {"summary": f"Error: {str(e)}", "usage_stats": {}}
    except (KeyError, IndexError, ValueError) as e:
        print(f"Error parsing API response: {e}")
        return {"summary": f"Error parsing response: {str(e)}", "usage_stats": {}}


# Function to check for valid citations in the response
def check_citations(text):
    # Look for PMID or journal references
    pmid_pattern = r"PMID:\s*\d+"
    journal_pattern = r"['\"][A-Za-z\s]+['\"]"
    pmids = re.findall(pmid_pattern, text)
    journals = re.findall(journal_pattern, text)
    return len(pmids) > 0 or len(journals) > 0, pmids, journals


# Main program
def run_experiment():
    query = "Find a recent PubMed article on Major Depression.  Summarize it in a way that an 10th grader can understand.  List citations and references."
    print(f"Query: {query}")

    # Measure response time
    start_time = time.time()
    response = call_grok_api(query)
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Extract summary and usage stats
    summary = response["summary"]
    usage_stats = response["usage_stats"]

    # Check for citations
    has_citations, pmids, journals = check_citations(summary)

    # Output results
    print("\nResults:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Summary: {summary}")

    print("\nReference Check:")
    if has_citations:
        print(f" - Valid references found: PMIDs {pmids}, Journals {journals}")
    else:
        print(" - No valid references detected")

    print("\nUsage Statistics:")
    for key, value in usage_stats.items():
        print(f" - {key.replace('_', ' ').title()}: {value}")


# Run the program
if __name__ == "__main__":
    run_experiment()
