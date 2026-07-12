import streamlit as st
from streamlit_option_menu import option_menu

# ==============================
# IMPORTS
# ==============================

from utils.loader import load_drift_report
from utils.styles import load_css

from pages.dashboard import show_dashboard
from pages.drift_analysis import show_drift_analysis
from pages.incidents import show_incidents
from pages.compliance import show_compliance
from pages.reports import show_reports
from pages.settings import show_settings


# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Security Control Drift Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# LOAD CUSTOM CSS
# ==============================

load_css()

# ==============================
# LOAD DATA
# ==============================

df = load_drift_report()

# ==============================
# SIDEBAR
# ==============================

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/security-checked.png",
        width=80
    )

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

# ==============================
# PAGE ROUTING
# ==============================

if selected == "Dashboard":

    show_dashboard(df)

elif selected == "Drift Analysis":

    show_drift_analysis(df)

elif selected == "Incidents":

    show_incidents(df)

elif selected == "Compliance":

    show_compliance(df)

elif selected == "Reports":

    show_reports(df)

elif selected == "Settings":

    show_settings(df)