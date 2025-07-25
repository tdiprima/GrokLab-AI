"""
Template for asking questions. Be sure to update the payload.
author: tdiprima
"""
import json
import os

import requests

# API endpoint
url = "https://api.x.ai/v1/chat/completions"
GROK_API_KEY = os.getenv("GROK_API_KEY")

# Headers
headers = {"Content-Type": "application/json", "Authorization": "Bearer " + GROK_API_KEY}

# TODO: Payload
data = {"messages": [
    # {"role": "system", "content": "You are..."},
    {"role": "user", "content": ""}],
    "model": "grok-4-0709", "stream": False, "temperature": 0}

# Make the request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Parse response JSON
if response.status_code == 200:
    response_json = response.json()

    # Extract and print the content
    content = response_json.get("choices", [{}])[0].get("message", {}).get("content", "")
    print(content)
else:
    print(f"Error: {response.status_code}, {response.text}")
