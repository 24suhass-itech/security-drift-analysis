import streamlit as st
import pandas as pd
import plotly.express as px


def show_blast_radius(df):

    st.title("Blast Radius Analysis")

    st.markdown(
        "Analyze the potential impact of security control drift across enterprise systems."
    )

    st.divider()

    # ======================================================
    # FILTERS
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:
        severity = st.selectbox(
            "Severity",
            ["All"] + sorted(df["severity"].unique().tolist())
        )

    with col2:
        system = st.selectbox(
            "System",
            ["All"] + sorted(df["system"].unique().tolist())
        )

    filtered = df.copy()

    if severity != "All":
        filtered = filtered[
            filtered["severity"] == severity
        ]

    if system != "All":
        filtered = filtered[
            filtered["system"] == system
        ]

    st.divider()

    # ======================================================
    # KPI CARDS
    # ======================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Incidents",
        len(filtered)
    )

    c2.metric(
        "Critical Incidents",
        len(filtered[filtered["severity"] == "CRITICAL"])
    )

    c3.metric(
        "Affected Systems",
        filtered["system"].nunique()
    )

    c4.metric(
        "Maximum Blast Radius",
        filtered["blast_radius"].max()
    )

    st.divider()

    # ======================================================
    # SEVERITY DISTRIBUTION
    # ======================================================

    left, right = st.columns(2)

    severity_count = (
        filtered
        .groupby("severity")
        .size()
        .reset_index(name="Count")
    )

    fig1 = px.pie(
        severity_count,
        names="severity",
        values="Count",
        hole=0.45,
        title="Severity Distribution"
    )

    left.plotly_chart(
        fig1,
        use_container_width=True
    )

    # ======================================================
    # TOP SYSTEMS
    # ======================================================

    system_count = (
        filtered
        .groupby("system")
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
    )

    fig2 = px.bar(
        system_count,
        x="system",
        y="Count",
        color="Count",
        title="Incidents by System"
    )

    right.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # BLAST RADIUS DISTRIBUTION
    # ======================================================

    left, right = st.columns(2)

    fig3 = px.histogram(
        filtered,
        x="blast_radius",
        nbins=10,
        title="Blast Radius Distribution",
        color="blast_radius"
    )

    left.plotly_chart(
        fig3,
        use_container_width=True
    )

    # ======================================================
    # TOP IMPACTED SYSTEMS
    # ======================================================

    exploded = filtered.explode("affected_systems")

    affected = (
        exploded
        .groupby("affected_systems")
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)
        .head(10)
    )

    fig4 = px.bar(
        affected,
        x="Count",
        y="affected_systems",
        orientation="h",
        color="Count",
        title="Top Impacted Systems"
    )

    right.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # BLAST RADIUS BY CONTROL
    # ======================================================

    control_radius = (
        filtered
        .sort_values(
            "blast_radius",
            ascending=False
        )
        .head(15)
    )

    fig5 = px.bar(
        control_radius,
        x="control_id",
        y="blast_radius",
        color="severity",
        title="Highest Blast Radius by Control"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # DETAILED TABLE
    # ======================================================

    st.subheader("Blast Radius Report")

    st.dataframe(
        filtered,
        use_container_width=True,
        height=500
    )