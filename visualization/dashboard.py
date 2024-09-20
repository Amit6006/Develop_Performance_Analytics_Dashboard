import streamlit as st

def display_overall_metrics(metrics):
    st.subheader("Overall Performance Metrics")
    for key, value in metrics.items():
        st.metric(label=key.replace('_', ' ').title(), value=value)
def render_dashboard(metrics):
    st.title("Developer Performance Analytics Dashboard")
    display_overall_metrics(metrics)
