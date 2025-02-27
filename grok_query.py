"""
Testing Grok API
author: tdiprima
"""
import requests
import json
import os

# API endpoint
url = "https://api.x.ai/v1/chat/completions"
GROK_API_KEY = os.getenv("GROK_API_KEY")

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + GROK_API_KEY
}

# Payload
data = {
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!  Who are you?"
        }
    ],
    "model": "grok-2-latest",
    "stream": False,
    "temperature": 0
}

# Make the request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Parse response JSON
if response.status_code == 200:
    response_json = response.json()
    
    # Extract and print the content
    # choices[0] > message > content
    content = response_json.get("choices", [{}])[0].get("message", {}).get("content", "")
    print(content)
else:
    print(f"Error: {response.status_code}, {response.text}")
