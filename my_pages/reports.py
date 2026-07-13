import streamlit as st
import pandas as pd
import json


def show_reports(df):

    st.title(" Reports & Export")

    st.markdown("Generate and export drift analysis reports.")

    st.divider()

    # =====================================================
    # SUMMARY
    # =====================================================

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Records", len(df))

    c2.metric(
        "Detected Drifts",
        df["drift_detected"].sum()
    )

    c3.metric(
        "Unique Controls",
        df["control_id"].nunique()
    )

    st.divider()

    # =====================================================
    # DOWNLOADS
    # =====================================================

    st.subheader("📥 Export Reports")

    csv = df.to_csv(index=False)

    st.download_button(
        "📄 Download Complete Drift Report (CSV)",
        csv,
        "drift_report.csv",
        "text/csv"
    )

    json_data = df.to_json(
        orient="records",
        indent=4
    )

    st.download_button(
        "📄 Download Complete Drift Report (JSON)",
        json_data,
        "drift_report.json",
        "application/json"
    )

    high = df[df["severity"] == "HIGH"]

    st.download_button(
        "📄 Download High Risk Report",
        high.to_csv(index=False),
        "high_risk.csv",
        "text/csv"
    )

    critical = df[df["severity"] == "CRITICAL"]

    st.download_button(
        "📄 Download Critical Report",
        critical.to_csv(index=False),
        "critical.csv",
        "text/csv"
    )

    st.divider()

    # =====================================================
    # REPORT STATISTICS
    # =====================================================

    st.subheader("📊 Report Statistics")

    left, right = st.columns(2)

    with left:

        st.write("### Top Drifted Controls")

        top = (
            df[df["drift_detected"] == True]
            .groupby("parameter")
            .size()
            .sort_values(ascending=False)
            .head(10)
        )

        st.dataframe(top)

    with right:

        st.write("### Severity Summary")

        severity = df["severity"].value_counts()

        st.dataframe(severity)

    st.divider()

    st.subheader("🌐 Environment Summary")

    env = df["environment"].value_counts()

    st.dataframe(env)