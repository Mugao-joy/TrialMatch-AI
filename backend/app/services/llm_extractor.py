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
    # remove markdown code fences
    content = re.sub(r"```json|```", "", content).strip()

    # find first JSON object
    match = re.search(r"\{.*\}", content, re.DOTALL)

    if match:
        return match.group(0)

    return "{}"


def extract_patient_profile(text: str):
    prompt = f"""
Extract the following patient information from the medical report.

Return ONLY valid JSON.

Required fields:
{{
  "diagnosis": "",
  "age": "",
  "gender": "",
  "biomarkers": [],
  "mutations": [],
  "current_medications": [],
  "location": ""
}}

Medical report:
{text}
"""

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {
                "role": "system",
                "content": "You are a medical document extraction system that returns only JSON.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    content = response.choices[0].message.content
    cleaned = clean_json_response(content)

    return json.loads(cleaned)