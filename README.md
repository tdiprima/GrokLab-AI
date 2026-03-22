# GrokLab-AI

Python toolkit for experimenting with xAI's Grok API — chat, vision, article summarization, and AI-generated git commits via the OpenAI-compatible SDK.

## The xAI API Has a Learning Curve

Getting started with Grok means figuring out which SDK to use (`xai-sdk` vs `openai`), which endpoints support which models, how the Responses API differs from Chat Completions, and how to handle multimodal inputs like images.

## Working Examples Across Major Use Cases

Each script is self-contained and demonstrates one capability: interactive chat, image analysis, batch file summarization, AI-generated commit messages, and model listing. A shared `llm_processor` module handles client setup and prompt dispatch so nothing is duplicated across scripts.

## Example: Generate a Git Commit Message from a Staged Diff

```bash
git add my_changes.py
python src/git_commit.py
```

Grok reads your staged diff and suggests a commit message under 50 characters. You confirm before anything is committed.

## Usage

### Prerequisites

```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set your API key:

```bash
export XAI_API_KEY=your_key_here
```

### Scripts

| Script | What it does |
|---|---|
| `hello_grok.py` | Minimal "Hello, Grok!" via the OpenAI-compatible client |
| `conversation.py` | Interactive terminal chat loop with Grok |
| `query_template.py` | Single-turn prompt using the native `xai-sdk` |
| `analyze_graph_image.py` | Multimodal: sends a PNG to Grok for visual analysis |
| `process_file.py` | Summarizes a single article (`input.txt` → `output.md`) |
| `rip_through_files.py` | Batch summarizes `i1.txt`, `i2.txt`, ... → `o1.md`, `o2.md`, ... |
| `wow.py` | Rewrites text and suggests a filename via Chat Completions |
| `rewrite_and_title.py` | Same task using the Responses API |
| `git_commit.py` | Generates a git commit message from your staged diff |
| `get_api_models.py` | Lists all available models from the xAI API |

### Run any script

```bash
cd src
python conversation.py
```

For image analysis, place your image at `src/input.png` before running `analyze_graph_image.py`.  
For file processing scripts, place your content in `src/input.txt`.

<br>
