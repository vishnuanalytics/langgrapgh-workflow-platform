from langgraph.graph import START
from langgraph.graph import END
from langgraph.graph import StateGraph


from app.ai.nodes import (
    classify_issue,
    calculate_severity,
    escalation_node,
    auto_replay_node,
    router_ticket
)

from app.ai.state import TicketState


builder = StateGraph(TicketState)

builder.add_node("classify_issue", classify_issue)
builder.add_node("calculate_severity", calculate_severity)
builder.add_node("escalation_node", escalation_node)
builder.add_node("auto_replay_node", auto_replay_node)


builder.add_edge(START, "classify_issue")
builder.add_edge("classify_issue", "calculate_severity")
builder.add_conditional_edges("calculate_severity", router_ticket)
builder.add_edge("escalation_node", END)
builder.add_edge("auto_replay_node", END)

graph = builder.compile()