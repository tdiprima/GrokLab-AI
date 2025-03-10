"""
Retrieve a list of available models from the xAI API
https://docs.x.ai/docs/api-reference?api-key=c6fbf1f6-0480-4866-abe9-e07a090bc433&cluster=us-east-1#list-models
Author: tdiprima
"""
import os
from datetime import datetime

import pytz
import requests

# Define California timezone
california_tz = pytz.timezone('America/Los_Angeles')

api_key = os.getenv("GROK_API_KEY")
headers = {'Authorization': f'Bearer {api_key}'}

response = requests.get('https://api.x.ai/v1/models', headers=headers)

if response.status_code == 200:
    models = response.json()
    for model in models['data']:
        timestamp = model['created']
        # Convert to human-readable format
        # readable_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S UTC')

        # Local time instead of UTC
        # readable_date_local = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        # Convert UTC timestamp to local California time
        readable_date_local = datetime.fromtimestamp(timestamp, california_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
        print(f"Model ID: {model['id']}, Created At: {readable_date_local}")
else:
    print(f"Failed to retrieve models: {response.status_code} - {response.text}")
