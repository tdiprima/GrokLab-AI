# GrokLab-AI

This repository came out of wanting a cleaner, more practical way to experiment with Grok and OpenAI APIs across different environments without rebuilding the same setup every time. It pulls together simple, reusable examples in Python, JavaScript, and Bash to show how I approach API integration work: keep the structure clear, reduce friction, and make it easy to move from quick testing to something production-minded.

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/tdiprima/GrokLab-AI.git
cd GrokLab-AI
```

### 2. Set Up Environment Variables

```sh
export GROK_API_KEY=your_api_key_here
export XAI_API_KEY=your_openai_key_here
```

### 3. Install Dependency

```sh
pip install openai
```

### 4. Running Scripts

#### Python

```sh
python python/query_template.py
```

#### JavaScript

```sh
node javascript/grok_api.js
```

#### Bash

```sh
bash bash/get_api_models.sh
```

## Features
- ✅ Integration with OpenAI and Grok AI APIs
- ✅ Secure API key handling with environment variables
- ✅ Organized folder structure for better maintainability
- ✅ Support for multiple languages (Python, JavaScript, Bash)

## Contribution Guidelines
- Fork the repo and create a new branch (`git checkout -b feature-name`).
- Commit changes (`git commit -m "Added new feature"`).
- Push to the branch (`git push origin feature-name`).
- Open a Pull Request.

## License
This project is licensed under the [MIT License](LICENSE).
