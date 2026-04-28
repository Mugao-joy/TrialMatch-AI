from app.services.trial_search import search_trials


def trial_agent(state):
    diagnosis = state["patient_profile"].get("diagnosis", "")

    trials = search_trials(diagnosis)

    state["trials"] = trials
    return state