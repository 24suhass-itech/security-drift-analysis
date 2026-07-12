import pandas as pd
import json

def load_baseline():
    with open("backend/baseline_configs.json", "r") as f:
        return pd.DataFrame(json.load(f))

def load_change_events():
    with open("backend/change_events.json", "r") as f:
        return pd.DataFrame(json.load(f))

def load_control_metadata():
    with open("backend/control_metadata.json", "r") as f:
        return pd.DataFrame(json.load(f))

def load_drift_report():

    baseline = load_baseline()
    events = load_change_events()
    metadata = load_control_metadata()

    drift = pd.read_csv("backend/drift_report.csv")

    df = drift.merge(
        baseline[
            [
                "control_id",
                "domain",
                "system",
                "severity_if_drifted"
            ]
        ],
        on="control_id",
        how="left"
    )

    df = df.merge(
        metadata[
            [
                "control_id",
                "business_criticality",
                "control_owner",
                "asset_type"
            ]
        ],
        on="control_id",
        how="left"
    )

    df = df.merge(
        events[
            [
                "event_id",
                "changed_by",
                "change_source",
                "approval_status",
                "maintenance_window"
            ]
        ],
        on="event_id",
        how="left"
    )

    if "severity_if_drifted" in df.columns and "severity" not in df.columns:
        df["severity"] = df["severity_if_drifted"]

    return df