import streamlit as st
from data_collection.github_api import fetch_github_data
from metrics.calculator import calculate_metrics
from visualization.charts import create_charts
from query_interface.nlp_processor import process_query

def main():
    st.title("Developer performance analytics dashboard")
    repo_url = st.text_input("Enter GitHub Repos URL:")
    if st.button("Fetch Data"):
        if repo_url:
            raw_data = fetch_github_data(repo_url)
            if raw_data:
                metrics = calculate_metrics(raw_data)
                st.session_state.metrics = metrics
                st.subheader("Performance Metrics")
                st.write(metrics)
                charts = create_charts(metrics)
                st.plotly_chart(charts)
            else:
                st.error("Failed to fetch data from the provided GitHub URL.")
        else:
            st.warning("Please enter a valid GitHub repository URL.")

    query = st.text_input("Ask a question about the metrics:")
    
    if st.button("Submit Query"):
        if 'metrics' in st.session_state:
            response = process_query(query, st.session_state.metrics)
            st.write(response)
        else:
            st.warning("Please fetch data first to ask questions.")
if __name__ == "__main__":
    main()
