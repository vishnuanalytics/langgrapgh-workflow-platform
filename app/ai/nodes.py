from app.ai.llm import llm
from app.ai.state import TicketState
from app.tools.incident_tool import create_incident
from app.tools.email_tool import send_auto_replay


def classify_issue(state: TicketState):
    message = state["message"]
    prompt = f"""
    You are a support ticket classifier.
    Classify this ticket into ONE category only:
    Categories:
    - payment_issue
    - menu_sync
    - sales_inquiry
    - onboarding
    - configuration_request
    - outage
    - unknown
    Ticket:
    {message}

    Return ONLY category name.
    """
    response = llm.invoke(prompt)
    issue_type = response.content.strip().lower()
    return {
        "issue_type": issue_type
    }


def calculate_severity(state: TicketState):
    issue_type = state["issue_type"]
    severity_map = {
        "payment_issue": "high",
        "outage": "critical",
        "menu_sync": "medium",
        "configuration_request": "low",
        "sales_inquiry": "low",
        "onboarding": "low",
        "unknown": "medium"
    }
    severity = severity_map.get(
        issue_type,
        "medium"
    )
    return {
        "severity": severity
    }

def escalation_node(state: TicketState):
    print("Escalating Tickat")
    incident = create_incident(
        issue_type=state["issue_type"],
        severity=state["severity"]

    )
    return {
        "response": "Incident is created",
        "Incident_id": incident["incident_id"]
    }

def auto_replay_node(state: TicketState):
    print("AUTO RESPONDING")

    send_auto_replay(state["customer_email"])


    return {
        "response": "Auto reply sent to customer."
        }

def router_ticket(state: TicketState):
    severity = state["severity"]

    if severity in ["high", "critical"]:
        return "escalation_node"
    
    return "auto_replay_node"
