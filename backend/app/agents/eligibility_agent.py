from app.services.eligibility_matcher import match_trials


def eligibility_agent(state):
    ranked_trials = match_trials(
        state["patient_profile"],
        state["trials"]
    )

    state["ranked_trials"] = ranked_trials
    return state