from app.services.extract_text import extract_text


def intake_agent(state):
    file_path = state["file_path"]
    extracted_text = extract_text(file_path)

    state["extracted_text"] = extracted_text
    return state