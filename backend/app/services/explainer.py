import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
)


def explain_results(patient_profile, ranked_trials):
    prompt = f"""
You are a medical AI assistant.

Patient Profile:
{json.dumps(patient_profile, indent=2)}

Ranked Trials:
{json.dumps(ranked_trials, indent=2)}

Explain:
1. Why the top trial was ranked highest
2. Why lower-ranked trials scored lower
3. Any important risks or considerations

Return concise, doctor-friendly plain text.
"""

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {"role": "system", "content": "You explain clearly and concisely."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content