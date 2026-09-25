import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px
from config import DATABASE

st.set_page_config(
    page_title="GKE Log Monitor",
    layout="wide",
)

st.title("GKE Log Monitoring Dashboard")

st.caption(
    "Python + Google Cloud Logging + GKE"
)

@st.chache_data(ttl=30)
def load_data():
    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        "select * from logs",
        conn
    )

    conn.close()

    return df

df = load_data()

if df.empty:
    st.warning(
        "No Error Logs Found."
    )

    st.stop()


#--------------------------------
# Metrics
#--------------------------------

total_errors = len(df)

deployments = df["deployment"].nunique()
pods = df["pod"].nunique()
error_types = df["error_type"].nunique()

col1, col2, col3, col4, = st.columns(4)

col1.metric(
    "Total Errors",
    total_errors
)

col2.metric(
    "Deployments",
    deployments
)

col3.metric(
    "Affected Pods",
    pods
)

col4.metric(
    "Error Types",
    error_types
)


#-------------------------
# Deployment Filter
#-------------------------

selected_deployment = st.selectbox(
    "Select Deployment",

    ["All"]+
    sorted(
        df["deployment"].unique()

    )
)

if selected_deployment != "All":

    filtered_df = df[df["deployment"]
                     == selected_deployment
                    ]

else:
    filtered_df = df

#----------------------------
# Error Count by Deployment
#----------------------------

st.subheader(
    "Errors by Deployment"
)

deployment_counts = (
    filtered_df.groupby("deployment").size().reset_index(
        name="errors"
    )
)

fig = px.bar(
    deployment_counts,

    x="deployment",
    y="errors",
    title="Error Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


#----------------------------
# Error Types
#----------------------------

st.subheader(
    "Error Classification"
)

error_counts = (
    filtered_df.groupby("error_type").size().reset_index(
        name="count"
    )
)

fig2 = px.pie(
    error_counts,
    names="error_type",
    values="count",
    title="Error Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

#-------------------------
# Severity
#-------------------------

st.subheader(
    "Severity Distribution"
)

severity_counts = (
    filtered_df.groupby("severity").size().reset_index(
        name="count"
    )
)

fig3 = px.bar(
    severity_counts,
    x="severity",
    y="count",
    title="Logs by Severity"
)

#-------------------------
# Recent errors
#-------------------------

st.subheader(
    "Recent Errors"
)

display_df = filtered_df[
    [
        "timestamp",
        "deployment",
        "pod",
        "severity",
        "error_type",
        "message"
    ]
].sort_values(
    "timestamp",
    ascending=False
)

st.dataframe(
    display_df,
    use_container_width=True
)