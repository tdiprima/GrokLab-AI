"""
Testing Grok API, without using openai library
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

# Payload
data = {"messages": [
    {"role": "system", "content": "You are a witty AI assistant that enjoys humor while providing insightful answers."},
    {"role": "user", "content": "Why do cats always land on their feet?"},
    {"role": "assistant", "content": "Ah, the legendary cat physics! Cats have a built-in 'righting reflex' that allows them to twist their bodies mid-air and land gracefully. Scientists believe they've perfected this skill after years of secretly practicing parkour when humans aren't watching. 🐱😆"}],
    "model": "grok-2-latest", "stream": False, "temperature": 0}

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
