import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse
from functions.get_files_info import schema_get_files_info


def main():

    if len(sys.argv) == 1:
        raise ValueError("Please add a string argument when calling this function for generating gemini output")


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

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
    )


    response = client.models.generate_content(model='gemini-2.0-flash-001',
                                            contents=messages,
                                            config=types.GenerateContentConfig(
                                                tools=[available_functions], system_instruction=system_prompt
                                            ))

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"Response: {response.text}")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()