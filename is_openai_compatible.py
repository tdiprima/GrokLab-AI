import os
from openai import OpenAI


def get_chat_completion(model: str, user_message: str, api_key: str) -> str:
    # Initialize the client with the provided API key and base URL
    client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
    
    # Make the API call to get the chat completion
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Best on writing comment of LinkedIn posts."},
                {"role": "user", "content": user_message},
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


# Example usage
api_key = os.getenv("GROK_API_KEY")
response = get_chat_completion("grok-2-latest", "Hello Grok!", api_key)
print(response)
