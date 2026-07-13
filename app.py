import streamlit as st
from streamlit_option_menu import option_menu

from utils.loader import (
    load_drift_report,
    load_compliance_mapping,
    load_blast_radius
)

from utils.styles import load_css

from my_pages.dashboard import show_dashboard
from my_pages.drift_analysis import show_drift_analysis
from my_pages.incidents import show_incidents
from my_pages.compliance import show_compliance
from my_pages.reports import show_reports
from my_pages.settings import show_settings
from my_pages.blast_radius import show_blast_radius

st.set_page_config(
    page_title="Security Control Drift Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

drift_df = load_drift_report()
compliance_df = load_compliance_mapping()
blast_df = load_blast_radius()

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
            "Blast Radius",
            "Reports",
            "Settings"
        ],
        icons=[
            "speedometer2",
            "graph-up-arrow",
            "exclamation-triangle",
            "shield-check",
            "bullseye",
            "file-earmark-bar-graph",
            "gear"
        ],
        default_index=0,
    )

    st.markdown("---")

    st.success("System Status : Online")

    st.caption("Version 1.0")

if selected == "Dashboard":

    show_dashboard(drift_df)

elif selected == "Drift Analysis":

    show_drift_analysis(drift_df)

elif selected == "Incidents":

    show_incidents(drift_df)

elif selected == "Compliance":

    show_compliance(compliance_df)

elif selected == "Blast Radius":

    show_blast_radius(blast_df)

elif selected == "Reports":

    show_reports(drift_df)

elif selected == "Settings":

    show_settings(drift_df)