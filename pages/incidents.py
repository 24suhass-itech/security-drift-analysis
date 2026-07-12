import streamlit as st
import pandas as pd


def show_incidents(df):

    st.title("🚨 Incident Explorer")

    st.markdown(
        "Search and filter security drift events across your infrastructure."
    )

    st.divider()

    # ----------------------------------------------------
    # FILTERS
    # ----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        severity = st.selectbox(
            "Severity",
            ["All"] + sorted(df["severity"].unique().tolist())
        )

    with col2:

        domain = st.selectbox(
            "Domain",
            ["All"] + sorted(df["domain"].unique().tolist())
        )

    col3, col4 = st.columns(2)

    with col3:

        environment = st.selectbox(
            "Environment",
            ["All"] + sorted(df["environment"].unique().tolist())
        )

    with col4:

        control = st.text_input(
            "Search Control ID"
        )

    # ----------------------------------------------------
    # APPLY FILTERS
    # ----------------------------------------------------

    filtered = df.copy()

    if severity != "All":
        filtered = filtered[
            filtered["severity"] == severity
        ]

    if domain != "All":
        filtered = filtered[
            filtered["domain"] == domain
        ]

    if environment != "All":
        filtered = filtered[
            filtered["environment"] == environment
        ]

    if control:
        filtered = filtered[
            filtered["control_id"].str.contains(
                control,
                case=False
            )
        ]

    st.divider()

    # ----------------------------------------------------
    # SUMMARY
    # ----------------------------------------------------

    st.metric(
        "Matching Incidents",
        len(filtered)
    )

    # ----------------------------------------------------
    # TABLE
    # ----------------------------------------------------

    st.dataframe(
        filtered,
        use_container_width=True,
        height=500
    )

    # ----------------------------------------------------
    # DOWNLOAD
    # ----------------------------------------------------

    csv = filtered.to_csv(index=False)

    st.download_button(
        "📥 Download Filtered Incidents",
        csv,
        "filtered_incidents.csv",
        "text/csv"
    )