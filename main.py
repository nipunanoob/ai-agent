import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse



def main():

    if len(sys.argv) == 1:
        raise ValueError("Please add a string argument when calling this function for generating gemini output")

    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

    parser = argparse.ArgumentParser()
    parser.add_argument("user_prompt", help="query which is going to be passed to Gemini API")
    parser.add_argument("--verbose", help="increase verbosity of output", action="store_true")
    args = parser.parse_args()
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model='gemini-2.0-flash-001',
                                            contents=messages,
                                            config=types.GenerateContentConfig(system_instruction=system_prompt))

    print(response.text)
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()