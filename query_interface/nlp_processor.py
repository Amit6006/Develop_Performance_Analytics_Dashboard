def process_query(query, metrics):
    query = query.lower()

    if "commit frequency" in query:
        return f"Commit Frequency: {metrics['commit_frequency']}"

    if "pr merge rate" in query:
        return f"PR Merge Rate: {metrics['pr_merge_rate']}"

    return "Sorry, I couldn't find information related to your query."
