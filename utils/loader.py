import pandas as pd
import streamlit as st

def load_drift_report():

    df = pd.read_csv("data/drift_report.csv")

    st.write(df.columns.tolist())

    return df