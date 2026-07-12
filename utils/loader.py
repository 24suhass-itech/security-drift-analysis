import pandas as pd


def load_drift_report():
    """
    Loads the drift report dataset.
    """

    df = pd.read_csv("data/drift_report.csv")
    return df