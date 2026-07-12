import streamlit as st
from streamlit_option_menu import option_menu

from utils.loader import (
    load_baseline,
    load_change_events,
    load_control_metadata,
    load_drift_report
)

from utils.styles import load_css

from my_pages.dashboard import show_dashboard
from my_pages.drift_analysis import show_drift_analysis
from my_pages.incidents import show_incidents
from my_pages.compliance import show_compliance
from my_pages.reports import show_reports
from my_pages.settings import show_settings

st.set_page_config(
    page_title="Security Control Drift Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

baseline_df = load_baseline()
events_df = load_change_events()
metadata_df = load_control_metadata()
drift_df = load_drift_report()

with st.sidebar:

    st.title("Security Drift")
    st.caption("Enterprise Security Monitoring")
    st.markdown("---")

    selected = option_menu(
        menu_title=None,
        options=[
            "Dashboard",
            "Drift Analysis",
            "Incidents",
            "Compliance",
            "Reports",
            "Settings"
        ],
        icons=[
            "speedometer2",
            "graph-up-arrow",
            "exclamation-triangle",
            "shield-check",
            "file-earmark-bar-graph",
            "gear"
        ],
        default_index=0,
    )

    st.markdown("---")
    st.success("System Status : Online")
    st.caption("Version 1.0")

if selected == "Dashboard":
    show_dashboard(
        baseline_df,
        events_df,
        metadata_df,
        drift_df
    )

elif selected == "Drift Analysis":
    show_drift_analysis(
        baseline_df,
        events_df,
        metadata_df,
        drift_df
    )

elif selected == "Incidents":
    show_incidents(
        baseline_df,
        events_df,
        metadata_df,
        drift_df
    )

elif selected == "Compliance":
    show_compliance(
        baseline_df,
        events_df,
        metadata_df,
        drift_df
    )

elif selected == "Reports":
    show_reports(
        baseline_df,
        events_df,
        metadata_df,
        drift_df
    )

elif selected == "Settings":
    show_settings(
        baseline_df,
        events_df,
        metadata_df,
        drift_df
    )