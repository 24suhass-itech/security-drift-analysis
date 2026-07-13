import json
import pandas as pd


def load_drift_report():

    df = pd.read_csv("data/drift_report.csv")
    return df


def load_compliance_mapping():

    with open("data/compliance_mapping.json", "r") as f:
        return pd.DataFrame(json.load(f))


def load_blast_radius():

    with open("data/blast_radius_report.json", "r") as f:
        return pd.DataFrame(json.load(f))