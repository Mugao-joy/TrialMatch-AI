import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
)


def chat_with_context(message, context):
    prompt = f"""
You are TrialMatch AI, a clinical trial assistant.

Context:
{json.dumps(context, indent=2)}

User question:
{message}

Answer clearly and accurately.
"""

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {"role": "system", "content": "You are a helpful medical AI."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content