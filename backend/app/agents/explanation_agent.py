from app.services.explainer import explain_results


def explanation_agent(state):
    explanation = explain_results(
        state["patient_profile"],
        state["ranked_trials"]
    )

    state["explanation"] = explanation
    return state