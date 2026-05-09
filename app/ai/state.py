from typing import TypedDict

class TicketState(TypedDict):
    incident_id: str
    message: str
    issue_type: str
    severity: str
    respond: str
    customer_email: str
