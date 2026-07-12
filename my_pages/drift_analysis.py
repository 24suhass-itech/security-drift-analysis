import streamlit as st
import pandas as pd
import plotly.express as px


def show_drift_analysis(df):

    st.title("📊 Drift Analysis")

    st.markdown("Analyze security configuration drift across your infrastructure.")

    st.divider()

    # ======================================================
    # FILTERS
    # ======================================================

    col1, col2, col3 = st.columns(3)

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

    with col3:
        environment = st.selectbox(
            "Environment",
            ["All"] + sorted(df["environment"].unique().tolist())
        )

    filtered = df.copy()

    if severity != "All":
        filtered = filtered[filtered["severity"] == severity]

    if domain != "All":
        filtered = filtered[filtered["domain"] == domain]

    if environment != "All":
        filtered = filtered[filtered["environment"] == environment]

    st.divider()

    # ======================================================
    # KPI CARDS
    # ======================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Events", len(filtered))
    c2.metric("Drifts", filtered["drift_detected"].sum())
    c3.metric("Unique Controls", filtered["control_id"].nunique())
    c4.metric("Users", filtered["changed_by"].nunique())

    st.divider()

    # ======================================================
    # TOP DRIFTED CONTROLS
    # ======================================================

    left, right = st.columns(2)

    drift_controls = (
        filtered[filtered["drift_detected"] == True]
        .groupby("parameter")
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
        .head(10)
    )

    fig1 = px.bar(
        drift_controls,
        x="Count",
        y="parameter",
        orientation="h",
        title="Top Drifted Controls",
        color="Count"
    )

    left.plotly_chart(fig1, use_container_width=True)

    # ======================================================
    # TOP USERS
    # ======================================================

    users = (
        filtered[filtered["drift_detected"] == True]
        .groupby("changed_by")
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
        .head(10)
    )

    fig2 = px.bar(
        users,
        x="changed_by",
        y="Count",
        color="Count",
        title="Top Users Causing Drift"
    )

    right.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # ======================================================
    # CHANGE SOURCE
    # ======================================================

    left, right = st.columns(2)

    source = (
        filtered
        .groupby("change_source")
        .size()
        .reset_index(name="Count")
    )

    fig3 = px.pie(
        source,
        names="change_source",
        values="Count",
        hole=0.45,
        title="Change Source Distribution"
    )

    left.plotly_chart(fig3, use_container_width=True)

    # ======================================================
    # APPROVAL STATUS
    # ======================================================

    approval = (
        filtered
        .groupby("approval_status")
        .size()
        .reset_index(name="Count")
    )

    fig4 = px.bar(
        approval,
        x="approval_status",
        y="Count",
        color="approval_status",
        title="Approval Status Distribution"
    )

    right.plotly_chart(fig4, use_container_width=True)

    st.divider()

    # ======================================================
    # MAINTENANCE WINDOW
    # ======================================================

    maintenance = (
        filtered
        .groupby("maintenance_window")
        .size()
        .reset_index(name="Count")
    )

    maintenance["maintenance_window"] = maintenance[
        "maintenance_window"
    ].replace(
        {
            True: "Inside Maintenance",
            False: "Outside Maintenance"
        }
    )

    fig5 = px.pie(
        maintenance,
        names="maintenance_window",
        values="Count",
        hole=0.45,
        title="Maintenance Window Analysis"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.divider()

    # ======================================================
    # TABLE
    # ======================================================

    st.subheader("Detailed Drift Events")

    st.dataframe(
        filtered,
        use_container_width=True,
        height=500
    )