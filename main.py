import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    model_name = "gemini-2.0-flash-001"
    client = genai.Client(api_key=api_key)

    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

    if len(sys.argv) <= 1:
        print("Failure 1: No arguments")
        sys.exit(1)

    user_prompt = sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}\n"
              f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
              f"Response tokens: {response.usage_metadata.cached_content_token_count}"
        )
    print(response.text)

main()