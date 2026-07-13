import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard(df):

    # ============================================
    # KPI CALCULATIONS
    # ============================================

    total_events = len(df)
    total_drifts = df["drift_detected"].sum()
    critical = len(df[df["severity"] == "CRITICAL"])
    healthy = len(df[df["drift_detected"] == False])

    compliance_score = round((healthy / total_events) * 100, 1)
    risk_score = round((critical / total_events) * 100, 1)

    # ============================================
    # TITLE
    # ============================================

    st.title(" Security Control Drift Detection Dashboard")

    st.markdown(
        "Real-time monitoring of security control drift across enterprise infrastructure."
    )

    st.divider()

    # ============================================
    # KPI CARDS
    # ============================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Events", total_events)
    c2.metric("Active Drift", total_drifts)
    c3.metric("Critical Alerts", critical)
    c4.metric("Healthy Controls", healthy)

    st.divider()

    # ============================================
    # EXECUTIVE SUMMARY
    # ============================================

    st.subheader(" Executive Summary")

    left, right = st.columns(2)

    with left:

        st.success(f"""
### Organization Health

✔ Compliance Score : **{compliance_score}%**

✔ Healthy Events : **{healthy}**

✔ Drift Events : **{total_drifts}**
""")

    with right:

        st.warning(f"""
### Current Risk

⚠ Critical Events : **{critical}**

⚠ Overall Risk Score : **{risk_score}%**

Immediate Investigation Recommended
""")

    st.divider()

    # ============================================
    # FIRST ROW
    # ============================================

    left, right = st.columns(2)

    severity = df["severity"].value_counts().reset_index()
    severity.columns = ["Severity", "Count"]

    fig1 = px.bar(
        severity,
        x="Severity",
        y="Count",
        color="Severity",
        title="Severity Distribution"
    )

    left.plotly_chart(fig1, use_container_width=True)

    drift = df["drift_detected"].value_counts().reset_index()
    drift.columns = ["Status", "Count"]

    drift["Status"] = drift["Status"].replace(
        {
            True: "Drift",
            False: "Healthy"
        }
    )

    fig2 = px.pie(
        drift,
        names="Status",
        values="Count",
        hole=0.45,
        title="Drift vs Healthy"
    )

    right.plotly_chart(fig2, use_container_width=True)

    # ============================================
    # SECOND ROW
    # ============================================

    left, right = st.columns(2)

    domain = df["domain"].value_counts().reset_index()
    domain.columns = ["Domain", "Count"]

    fig3 = px.bar(
        domain,
        x="Domain",
        y="Count",
        color="Domain",
        title="Domain-wise Events"
    )

    left.plotly_chart(fig3, use_container_width=True)

    env = df["environment"].value_counts().reset_index()
    env.columns = ["Environment", "Count"]

    fig4 = px.pie(
        env,
        names="Environment",
        values="Count",
        hole=0.45,
        title="Environment Distribution"
    )

    right.plotly_chart(fig4, use_container_width=True)

    st.divider()

    # ============================================
    # HEATMAP
    # ============================================

    st.subheader(" Control Health Heatmap")

    heat = (
        df[df["drift_detected"] == True]
        .groupby(["domain", "environment"])
        .size()
        .reset_index(name="Drifts")
    )

    pivot = heat.pivot(
        index="domain",
        columns="environment",
        values="Drifts"
    ).fillna(0)

    fig5 = px.imshow(
        pivot,
        text_auto=True,
        color_continuous_scale="RdYlGn_r",
        aspect="auto",
        title="Drift Density Across Domains"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.divider()

    # ============================================
    # TIMELINE
    # ============================================

    st.subheader(" Drift Timeline")

    temp = df.copy()

    temp["timestamp"] = pd.to_datetime(temp["timestamp"])

    temp["Date"] = temp["timestamp"].dt.date

    timeline = (
        temp[temp["drift_detected"] == True]
        .groupby("Date")
        .size()
        .reset_index(name="Drifts")
    )

    fig6 = px.line(
        timeline,
        x="Date",
        y="Drifts",
        markers=True,
        title="Daily Drift Trend"
    )

    st.plotly_chart(fig6, use_container_width=True)

    st.divider()

    # ============================================
    # LIVE ALERT PANEL
    # ============================================

    st.subheader(" Latest Critical Alerts")

    alerts = (
        df[df["severity"] == "CRITICAL"]
        .sort_values("timestamp", ascending=False)
        .head(10)
    )

    st.dataframe(
        alerts[
            [
                "timestamp",
                "control_id",
                "parameter",
                "severity",
                "changed_by",
                "environment"
            ]
        ],
        use_container_width=True
    )

    st.divider()

    # ============================================
    # TOP DRIFTED CONTROLS
    # ============================================

    st.subheader(" Top Drifted Controls")

    top_controls = (
        df[df["drift_detected"] == True]
        .groupby("parameter")
        .size()
        .reset_index(name="Drift Count")
        .sort_values("Drift Count", ascending=False)
        .head(10)
    )

    fig7 = px.bar(
        top_controls,
        x="parameter",
        y="Drift Count",
        color="Drift Count",
        title="Most Frequently Drifted Controls"
    )

    st.plotly_chart(fig7, use_container_width=True)

    st.divider()

    # ============================================
    # AI INSIGHTS (PLACEHOLDER)
    # ============================================

    st.subheader("AI Security Insights")

    st.info("""
### AI Recommendation Engine

The AI engine will analyze incoming configuration changes and provide:

- Predict likelihood of future configuration drift
- Recommend corrective actions
- Prioritize incidents by business risk
- Detect anomalous administrator behavior
- Forecast compliance degradation

*(This section will be connected to the Machine Learning backend after integration.)*
""")