import streamlit as st


def load_css():

    st.markdown("""

<style>

/* Background */

.stApp{
    background-color:#0E1117;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background-color:#161B22;
}

/* Metric Cards */

div[data-testid="metric-container"]{

    background-color:#1F2937;

    border-radius:15px;

    padding:18px;

    border:1px solid #374151;

    box-shadow:0px 3px 8px rgba(0,0,0,0.4);

}

/* Metric Labels */

div[data-testid="metric-container"] label{

    color:#E5E7EB;

    font-weight:bold;

}

/* Tables */

[data-testid="stDataFrame"]{

    border-radius:10px;

}

/* Buttons */

.stButton>button{

    border-radius:10px;

    height:45px;

    font-weight:bold;

}

/* Download Button */

.stDownloadButton>button{

    border-radius:10px;

    height:45px;

}

/* Header */

h1{

    color:#4ADE80;

}

h2{

    color:#60A5FA;

}

h3{

    color:#FBBF24;

}

footer{

visibility:hidden;

}

</style>

""",unsafe_allow_html=True)