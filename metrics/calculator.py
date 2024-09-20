# import pandas as pd
# def calculate_metrics(raw_data):
#     commits = raw_data.get('commits', [])
#     commit_frequency = len(commits)
#     pr_merge_rate = 0  
#     return {
#         "commit_frequency": commit_frequency,
#         "pr_merge_rate": pr_merge_rate,
#     }

def calculate_metrics(raw_data):
    commits = raw_data.get('commits', [])
    pull_requests = raw_data.get('pull_requests', [])

    commit_frequency = len(commits)
    pr_merge_count = len([pr for pr in pull_requests if pr.get('merged_at')])
    pr_merge_rate = pr_merge_count / max(len(commits), 1)  # Avoid division by zero

    return {
        "commit_frequency": commit_frequency,
        "pr_merge_rate": pr_merge_rate,
    }
