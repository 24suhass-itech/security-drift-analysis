import json
import pandas as pd

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

    with open("backend/drift_report.json", "r") as f:
        drift = pd.DataFrame(json.load(f))

    df = (
        drift
        .merge(
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
        .merge(
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
        .merge(
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
    )

    return df