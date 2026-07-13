import streamlit as st
import pandas as pd
import plotly.express as px


def show_compliance(df):

    st.title("Compliance Mapping")

    st.markdown("Analyze security controls mapped across enterprise compliance frameworks.")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        framework = st.selectbox(
            "Framework",
            ["All"] + sorted(df["framework"].unique().tolist())
        )

    with col2:
        control = st.selectbox(
            "Control",
            ["All"] + sorted(df["control"].unique().tolist())
        )

    with col3:
        parameter = st.selectbox(
            "Parameter",
            ["All"] + sorted(df["parameter"].unique().tolist())
        )

    filtered = df.copy()

    if framework != "All":
        filtered = filtered[
            filtered["framework"] == framework
        ]

    if control != "All":
        filtered = filtered[
            filtered["control"] == control
        ]

    if parameter != "All":
        filtered = filtered[
            filtered["parameter"] == parameter
        ]

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Compliance Rules",
        len(filtered)
    )

    c2.metric(
        "Frameworks",
        filtered["framework"].nunique()
    )

    c3.metric(
        "Controls",
        filtered["control"].nunique()
    )

    c4.metric(
        "Parameters",
        filtered["parameter"].nunique()
    )

    st.divider()

    left, right = st.columns(2)

    framework_count = (
        filtered
        .groupby("framework")
        .size()
        .reset_index(name="Count")
    )

    fig1 = px.pie(
        framework_count,
        names="framework",
        values="Count",
        hole=0.45,
        title="Compliance Framework Distribution"
    )

    left.plotly_chart(
        fig1,
        use_container_width=True
    )

    control_count = (
        filtered
        .groupby("control")
        .size()
        .reset_index(name="Count")
        .sort_values(
            "Count",
            ascending=False
        )
    )

    fig2 = px.bar(
        control_count,
        x="control",
        y="Count",
        color="Count",
        title="Controls by Framework"
    )

    right.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    left, right = st.columns(2)

    parameter_count = (
        filtered
        .groupby("parameter")
        .size()
        .reset_index(name="Count")
        .sort_values(
            "Count",
            ascending=False
        )
        .head(10)
    )

    fig3 = px.bar(
        parameter_count,
        x="Count",
        y="parameter",
        orientation="h",
        color="Count",
        title="Top Security Parameters"
    )

    left.plotly_chart(
        fig3,
        use_container_width=True
    )

    description_count = (
        filtered
        .groupby("description")
        .size()
        .reset_index(name="Count")
        .sort_values(
            "Count",
            ascending=False
        )
        .head(10)
    )

    fig4 = px.bar(
        description_count,
        x="Count",
        y="description",
        orientation="h",
        color="Count",
        title="Top Compliance Requirements"
    )

    right.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.divider()

    st.subheader("Compliance Matrix")

    matrix = (
        filtered
        .pivot_table(
            index="framework",
            columns="control",
            values="parameter",
            aggfunc="count",
            fill_value=0
        )
    )

    fig5 = px.imshow(
        matrix,
        text_auto=True,
        color_continuous_scale="Blues",
        aspect="auto",
        title="Framework vs Control Mapping"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    st.divider()

    st.subheader("Compliance Mapping Details")

    st.dataframe(
        filtered,
        use_container_width=True,
        height=500
    )