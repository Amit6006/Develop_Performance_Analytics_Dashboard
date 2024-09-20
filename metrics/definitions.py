COMMIT_FREQUENCY_DESC = "The number of commits made in a specific timeframe."
PR_MERGE_RATE_DESC = "The rate at which pull requests are merged relative to the number of commits."

METRIC_DEFINITIONS = {
    "commit_frequency": {
        "description": COMMIT_FREQUENCY_DESC,
        "unit": "commits",
    },
    "pr_merge_rate": {
        "description": PR_MERGE_RATE_DESC,
        "unit": "merges per commit",
    },
}
