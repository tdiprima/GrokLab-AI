"""
Token Optimization:
  - The script estimates token count using a rough heuristic (1 token ≈ 4 characters, plus some overhead). If the text exceeds a
    configurable threshold (default: 100,000 tokens, well below Grok's 128k context window), it splits the text into chunks, summarizes
    each chunk individually, and then generates a final "summary of summaries" to avoid exceeding token limits and reduce costs.
  - Prompts are crafted to be concise, requesting summaries of a specific length (e.g., 200-300 words) to minimize output tokens.
  - Only essential text is sent in API requests.
"""
import sys
import os
import requests
import json

# Grok API endpoint and model
GROK_API_URL = "https://api.x.ai/v1/chat/completions"
GROK_MODEL = "grok-4-0709"

# Configurable token threshold (to avoid hitting context limits; Grok supports ~128k)
MAX_TOKENS = 100000


# Token estimation heuristic (rough: 1 token ≈ 4 chars + overhead)
def estimate_tokens(text):
    return len(text) // 4 + 50  # Add overhead for prompt


# Function to call Grok API for summarization
def summarize_with_grok(text, api_key, max_output_words=300, is_chunk=False):
    prompt = (
        f"Summarize the following article concisely in {max_output_words} words or fewer. "
        f"Focus on key points, main ideas, and conclusions. "
        f"{'(This is a chunk of a larger article; keep it brief.)' if is_chunk else ''}\n\n"
        f"Article: {text}"
    )
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": GROK_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_output_words * 2,  # Rough estimate: 1 word ≈ 1.5-2 tokens
        "temperature": 0.5  # Lower for more focused summaries
    }
    
    response = requests.post(GROK_API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        raise Exception(f"API error: {response.status_code} - {response.text}")


# Function to chunk text if too long
def chunk_text(text, max_chunk_tokens=MAX_TOKENS // 2):  # Smaller chunks for safety
    chunks = []
    current_chunk = ""
    for line in text.split('\n'):
        if estimate_tokens(current_chunk + line) > max_chunk_tokens:
            chunks.append(current_chunk.strip())
            current_chunk = line
        else:
            current_chunk += '\n' + line
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks


# Main function
def main(file_path):
    # Load API key from environment variable
    api_key = os.getenv("GROK_API_KEY")
    if not api_key:
        print("Error: GROK_API_KEY environment variable not set.")
        sys.exit(1)
    
    # Read the file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    total_tokens = estimate_tokens(text)
    print(f"Estimated tokens in article: {total_tokens}")
    
    if total_tokens > MAX_TOKENS:
        print("Article is long; chunking and summarizing in parts...")
        chunks = chunk_text(text)
        chunk_summaries = []
        for i, chunk in enumerate(chunks):
            print(f"Summarizing chunk {i+1}/{len(chunks)}...")
            summary = summarize_with_grok(chunk, api_key, max_output_words=100, is_chunk=True)
            chunk_summaries.append(summary)
        
        # Summarize the chunk summaries
        combined_summaries = "\n\n".join(chunk_summaries)
        print("Generating final summary from chunk summaries...")
        final_summary = summarize_with_grok(combined_summaries, api_key, max_output_words=300)
    else:
        print("Summarizing article...")
        final_summary = summarize_with_grok(text, api_key, max_output_words=300)
    
    print("\n--- Summary ---")
    print(final_summary)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python grok_article_summarizer.py <path_to_text_file>")
        sys.exit(1)
    
    main(sys.argv[1])
