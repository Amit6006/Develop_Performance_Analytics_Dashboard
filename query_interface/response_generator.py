from metrics.definitions import METRIC_DEFINITIONS
def generate_response(query, metrics):
    query = query.lower()
    if "commit frequency" in query:
        return f"Commit Frequency: {metrics['commit_frequency']} ({METRIC_DEFINITIONS['commit_frequency']['unit']}) - {METRIC_DEFINITIONS['commit_frequency']['description']}"
    if "pr merge rate" in query:
        return f"PR Merge Rate: {metrics['pr_merge_rate']} ({METRIC_DEFINITIONS['pr_merge_rate']['unit']}) - {METRIC_DEFINITIONS['pr_merge_rate']['description']}"
    return "Sorry, I couldn't find information related to your query."
