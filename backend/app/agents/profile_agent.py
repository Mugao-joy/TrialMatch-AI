from app.services.llm_extractor import extract_patient_profile


def profile_agent(state):
    extracted_text = state["extracted_text"]

    patient_profile = extract_patient_profile(extracted_text)

    state["patient_profile"] = patient_profile
    return state