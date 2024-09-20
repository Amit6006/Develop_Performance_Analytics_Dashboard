# import requests
# def fetch_github_data(repo_url):
#     try:
#         repo_path = repo_url.split('github.com/')[-1]
#         api_url = f"https://api.github.com/repos/{repo_path}"
#         repo_response = requests.get(api_url)
#         if repo_response.status_code != 200:
#             return None
#         commits = fetch_all_commits(repo_path)

#         return {
#             "repo_info": repo_response.json(),
#             "commits": commits
#         }
#     except Exception as e:
#         print(f"Error fetching data: {e}")
#         return None
# def fetch_all_commits(repo_path):
#     commits_url = f"https://api.github.com/repos/{repo_path}/commits"
#     commits = []
#     page = 1
#     try:
#         while True:
#             response = requests.get(f"{commits_url}?page={page}&per_page=100")
#             if response.status_code != 200 or not response.json():
#                 break
#             commits.extend(response.json())
#             page += 1
#         return commits
#     except Exception as e:
#         print(f"Error fetching commits: {e}")
#         return []


import requests

def fetch_github_data(repo_url):
    try:
        repo_path = repo_url.split('github.com/')[-1]
        api_url = f"https://api.github.com/repos/{repo_path}"

        # Fetch repository information
        repo_response = requests.get(api_url)
        if repo_response.status_code != 200:
            return None

        # Fetch commits and pull requests data (handle pagination)
        commits = fetch_all_commits(repo_path)
        pull_requests = fetch_all_pull_requests(repo_path)

        return {
            "repo_info": repo_response.json(),
            "commits": commits,
            "pull_requests": pull_requests
        }
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def fetch_all_commits(repo_path):
    commits_url = f"https://api.github.com/repos/{repo_path}/commits"
    commits = []
    page = 1
    try:
        while True:
            response = requests.get(f"{commits_url}?page={page}&per_page=100")
            if response.status_code != 200 or not response.json():
                break
            commits.extend(response.json())
            page += 1
        return commits
    except Exception as e:
        print(f"Error fetching commits: {e}")
        return []

def fetch_all_pull_requests(repo_path):
    pull_requests_url = f"https://api.github.com/repos/{repo_path}/pulls?state=all"
    pull_requests = []
    page = 1
    try:
        while True:
            response = requests.get(f"{pull_requests_url}?page={page}&per_page=100")
            if response.status_code != 200 or not response.json():
                break
            pull_requests.extend(response.json())
            page += 1
        return pull_requests
    except Exception as e:
        print(f"Error fetching pull requests: {e}")
        return []
