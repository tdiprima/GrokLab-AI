#!/bin/bash
if [[ -z "$GROK_API_KEY" ]]; then
  echo "Error: GROK_API_KEY is not set."
  exit 1
fi

curl https://api.x.ai/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer $GROK_API_KEY" -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Testing. Just say hi and hello world and nothing else."
    }
  ],
  "model": "grok-2-latest",
  "stream": false,
  "temperature": 0
}'
