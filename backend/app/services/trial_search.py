import requests


def search_trials(condition: str):
    url = "https://clinicaltrials.gov/api/query/full_studies"

    params = {
        "expr": condition,
        "min_rnk": 1,
        "max_rnk": 5,
        "fmt": "json",
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    try:
        data = response.json()
        studies = (
            data.get("FullStudiesResponse", {})
            .get("FullStudies", [])
        )
        return studies
    except Exception as e:
        print("Trial search error:", e)
        return []


# def search_trials(condition: str):
#     return [
#         {
#             "trial_title": "HER2 Positive Operable or Locally Advanced Breast Cancer Trial",
#             "nct_id": "NCT02003209",
#             "condition": "HER2+ Breast Cancer",
#             "eligibility": {
#                 "age_min": 18,
#                 "gender": "Female",
#                 "biomarkers": ["HER2 positive"],
#                 "stage": "Stage II"
#             },
#             "location": "United States"
#         }
#     ]