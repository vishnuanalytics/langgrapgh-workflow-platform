


def create_incident(
        issue_type: str,
        severity: str
):
    print(f"creating incidents")

    incident = {
        "incident_id": "INC-001",
        "issue_type": issue_type,
        "severity": severity
    }

    return incident