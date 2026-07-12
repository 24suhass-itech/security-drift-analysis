import json

def run():

    with open("drift_report.json", "r") as f:
        drift_report = json.load(f)

    with open("control_metadata.json", "r") as f:
        metadata = json.load(f)

    metadata_lookup = {m["control_id"]: m for m in metadata}

    severity_score = {
        "NONE": 0,
        "LOW": 10,
        "MEDIUM": 20,
        "HIGH": 30,
        "CRITICAL": 40
    }

    criticality_score = {
        "Low": 5,
        "Medium": 10,
        "High": 18,
        "Critical": 25
    }

    environment_score = {
        "development": 2,
        "testing": 5,
        "staging": 8,
        "production": 15
    }

    approval_score = {
        "approved": 0,
        "pending": 6,
        "rejected": 8,
        "emergency": 10,
        "expired": 10
    }

    risk_report = []

    for event in drift_report:

        meta = metadata_lookup.get(event["control_id"])

        if meta is None:
            continue

        sev = event["severity"].upper()
        bc = meta["business_criticality"]
        env = event["environment"].lower()
        approval = event["approval_status"].lower()

        score = severity_score.get(sev, 0)
        reasons = []

        if sev != "NONE":
            reasons.append(f"{sev} drift")

        score += criticality_score.get(bc, 0)

        if bc == "Critical":
            reasons.append("Critical business control")

        score += environment_score.get(env, 0)

        if env == "production":
            reasons.append("Production environment")

        score += approval_score.get(approval, 0)

        if approval != "approved":
            reasons.append(f"{approval.capitalize()} approval")

        if event["maintenance_window"] == False:
            score += 10
            reasons.append("Outside maintenance window")

        score = min(score, 100)

        if sev == "NONE":
            score = 0
            level = "Low"

        elif sev == "LOW":
            score = min(score, 25)
            level = "Low"

        elif sev == "MEDIUM":
            if score < 26:
                score = 26
            elif score > 50:
                score = 50
            level = "Medium"

        elif sev == "HIGH":
            if score < 51:
                score = 51
            elif score > 75:
                score = 75
            level = "High"

        elif sev == "CRITICAL":
            if score < 76:
                score = 76
            level = "Critical"

        if sev == "NONE":
            reasons = []

        risk_report.append({

            "event_id": event["event_id"],

            "control_id": event["control_id"],

            "drift_severity": sev,

            "business_criticality": bc,

            "risk_score": score,

            "risk_level": level,

            "risk_factors": reasons

        })

    with open("risk_report.json", "w") as f:
        json.dump(risk_report, f, indent=4)

    print("\nRisk Scoring Completed")
    print("Total Records :", len(risk_report))

    return "risk_report.json"

if __name__ == "__main__":
    output = run()
    print(f"\nGenerated: {output}")