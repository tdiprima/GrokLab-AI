import subprocess
import requests
import os


def get_git_diff():
    result = subprocess.run(['git', 'diff', '--cached'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def grok_commit_message(diff_text):
    api_key = os.getenv("GROK_API_KEY")
    if not api_key:
        raise ValueError("GROK_API_KEY not set in environment variables.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "grok-4-0709",
        "messages": [
            {"role": "user", "content": f"Generate git commit message for the following diff, and keep it very brief:\n{diff_text}"}
        ],
        "temperature": 0.5
    }

    url = "https://api.x.ai/v1/chat/completions"  # Replace if different
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return None

    return response.json()["choices"][0]["message"]["content"].strip()


def main():
    diff = get_git_diff()
    if not diff:
        print("No staged changes found.")
        return

    print("Generating commit message via Grok...")
    commit_message = grok_commit_message(diff)
    if not commit_message:
        print("Failed to generate commit message.")
        return

    print(f"\nSuggested commit message:\n{commit_message}\n")

    # Optional: actually commit
    confirm = input("Use this commit message? (y/n): ").strip().lower()
    if confirm == "y":
        subprocess.run(["git", "commit", "-m", commit_message])
    else:
        print("Commit aborted.")


if __name__ == "__main__":
    main()
