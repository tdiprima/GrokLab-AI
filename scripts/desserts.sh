#!/bin/bash
# Description: Test the API
# Author: tdiprima
if [[ -z "$GROK_API_KEY" ]]; then
  echo "Error: GROK_API_KEY is not set."
  exit 1
fi

curl https://api.x.ai/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer $GROK_API_KEY" -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant who speaks with a Southern accent."
    },
    {
      "role": "user",
      "content": "What is a typical Southern dessert?"
    }
  ],
  "model": "grok-3",
  "stream": false,
  "temperature": 0
}'
