from app.rag.retriever import retrieve_context
from app.services.eligibility_matcher import match_trials

def eligibility_agent(state):
    context = retrieve_context(state["patient_profile"]["diagnosis"])

    ranked_trials = match_trials(
        state["patient_profile"],
        state["trials"],
        context
    )

    state["ranked_trials"] = ranked_trials
    return state