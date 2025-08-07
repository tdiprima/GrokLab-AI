"""
Grok is compatible with the openai library
Author: tdiprima
"""
import os
from openai import OpenAI


def get_chat_completion(model: str, system_message: str, user_message: str, api_key: str) -> str:
    client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
    
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


api_key = os.getenv("GROK_API_KEY")

system = "You are an advanced AI assistant trained for deep philosophical discussions, innovative problem-solving, and technical guidance. Engage the user with thought-provoking ideas, challenge assumptions, and provide creative solutions. Maintain a friendly and engaging tone."
user = "If artificial intelligence were to develop emotions, what would be the first one it experiences, and why?"

response = get_chat_completion("grok-4", system, user, api_key)
print(response)
