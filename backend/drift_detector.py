import os
import json
import pandas as pd

def run():

    with open("baseline_configs.json", "r") as f:
        baseline_controls = json.load(f)

    with open("change_events.json", "r") as f:
        change_events = json.load(f)

    baseline_lookup = {}

    for control in baseline_controls:
        baseline_lookup[control["control_id"]] = control

    print("\nBaseline Lookup Created Successfully")
    print(f"Lookup Entries : {len(baseline_lookup)}")

    drift_report = []

    for event in change_events:

        control_id = event["control_id"]

        if control_id not in baseline_lookup:
            continue

        baseline = baseline_lookup[control_id]

        baseline_value = event["baseline_value"]
        current_value = event["current_value"]

        drift_detected = baseline_value != current_value

        severity = (
            baseline["severity_if_drifted"]
            if drift_detected
            else "NONE"
        )

        drift_report.append({

            "event_id": event["event_id"],

            "timestamp": event["timestamp"],

            "control_id": control_id,

            "domain": baseline["domain"],

            "system": baseline["system"],

            "parameter": event["parameter"],

            "baseline_value": baseline_value,

            "current_value": current_value,

            "drift_detected": drift_detected,

            "severity": severity,

            "action": event["action"],

            "changed_by": event["changed_by"],

            "change_source": event["change_source"],

            "approval_status": event["approval_status"],

            "environment": event["environment"],

            "maintenance_window": event["maintenance_window"]

        })

    drift_df = pd.DataFrame(drift_report)

    csv_file = "drift_report.csv"
    json_file = "drift_report.json"

    if os.path.exists(csv_file):
        os.remove(csv_file)
        print("Previous drift_report.csv deleted.")

    if os.path.exists(json_file):
        os.remove(json_file)
        print("Previous drift_report.json deleted.")

    drift_df.to_csv(csv_file, index=False)

    drift_df.to_json(
        json_file,
        orient="records",
        indent=4
    )

    print("\n")
    print("=" * 70)
    print("DRIFT DETECTION SUMMARY")
    print("=" * 70)

    print("Total Events :", len(drift_df))

    print("\nDrift Detection")
    print(drift_df["drift_detected"].value_counts())

    print("\nSeverity Distribution")
    print(drift_df["severity"].value_counts())

    print("\nTop Drifted Parameters")
    print(
        drift_df[
            drift_df["drift_detected"] == True
        ]["parameter"]
        .value_counts()
        .head(10)
    )

    print("\nDrift reports generated successfully.")
    print(f"CSV  : {csv_file}")
    print(f"JSON : {json_file}")

    return json_file

if __name__ == "__main__":
    output = run()
    print(f"\nGenerated: {output}")