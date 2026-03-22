#!/usr/bin/env bash
# Description: Get API models
# Author: tdiprima

curl https://api.x.ai/v1/models \
  -H "Authorization: Bearer $GROK_API_KEY"
