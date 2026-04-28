import requests


def search_trials(condition: str):
    url = "https://clinicaltrials.gov/api/query/study_fields"

    params = {
        "expr": condition,
        "fields": "NCTId,BriefTitle,Condition",
        "min_rnk": 1,
        "max_rnk": 5,
        "fmt": "json",
    }

    response = requests.get(url, params=params)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text[:500])

    if response.status_code != 200:
        return []

    try:
        data = response.json()
        return data.get("StudyFieldsResponse", {}).get("StudyFields", [])
    except Exception:
        return []