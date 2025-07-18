import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()


def main():
    # Initialize the client
    client = OpenAI(
        api_key=os.getenv("XAI_API_KEY"),
        base_url="https://api.x.ai/v1"
    )
    
    print("🤖 Grok4 Conversation")
    print("=" * 20)
    print("Type 'quit', 'exit', or 'q' to exit\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("OK, bye! 👋")
            break
            
        try:
            response = client.chat.completions.create(
                model="grok-4-0709",
                messages=[
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7
            )
            
            print(f"Grok4\n: {response.choices[0].message.content}\n")
            
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
