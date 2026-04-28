from langgraph.graph import StateGraph, END

from app.agents.intake_agent import intake_agent
from app.agents.profile_agent import profile_agent
from app.agents.trial_agent import trial_agent
from app.agents.eligibility_agent import eligibility_agent


def build_graph():
    workflow = StateGraph(dict)

    workflow.add_node("intake", intake_agent)
    workflow.add_node("profile", profile_agent)
    workflow.add_node("trial", trial_agent)
    workflow.add_node("eligibility", eligibility_agent)

    workflow.set_entry_point("intake")

    workflow.add_edge("intake", "profile")
    workflow.add_edge("profile", "trial")
    workflow.add_edge("trial", "eligibility")
    workflow.add_edge("eligibility", END)

    return workflow.compile()