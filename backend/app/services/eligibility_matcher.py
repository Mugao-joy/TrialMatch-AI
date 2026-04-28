import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
)


def clean_json_response(content: str):
    content = re.sub(r"```json|```", "", content).strip()
    match = re.search(r"\[.*\]", content, re.DOTALL)

    if match:
        return match.group(0)

    return "[]"


def match_trials(patient_profile, trials, context):
    prompt = f"""
You are a clinical trial eligibility assistant.

Use the provided medical guidelines and protocol context to improve matching accuracy.

Guidelines Context:
{context}

Patient Profile:
{json.dumps(patient_profile, indent=2)}

Trials:
{json.dumps(trials[:3], indent=2)}

Analyze each trial against:
- diagnosis compatibility
- biomarker overlap
- mutation overlap
- age compatibility
- gender compatibility
- treatment compatibility

Assign a realistic match score from 0 to 100.

Scoring guide:
- 90–100 = highly compatible
- 70–89 = strong match
- 40–69 = partial match
- 0–39 = weak/no match

Return ONLY valid JSON:
[
  {{
    "trial_title": "trial title",
    "nct_id": "trial id",
    "match_score": <integer 0-100>,
    "reason": "brief explanation"
  }}
]
"""

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {
                "role": "system",
                "content": "You are a medical AI assistant that returns only JSON.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    content = response.choices[0].message.content
    cleaned = clean_json_response(content)

    return json.loads(cleaned)