import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()

if len(sys.argv) == 1:
    raise ValueError("Please add a string argument when calling this function for generating gemeni output")

query = sys.argv[1]

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(model='gemini-2.0-flash-001',
                                          contents=query)

print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")