import requests
from requests.auth import HTTPBasicAuth

def fetch_commits(username, app_password, repo_owner, repo_slug, limit=10):
    """
    Fetches up to `limit` commits from the given Bitbucket repo.
    Returns a list of dicts: { hash, author, date, message }.
    """
    url = f"https://api.bitbucket.org/2.0/repositories/{repo_owner}/{repo_slug}/commits"
    params = { 'pagelen': limit }
    resp = requests.get(url, auth=HTTPBasicAuth(username, app_password), params=params)
    resp.raise_for_status()
    data = resp.json()

    commits = []
    for c in data.get('values', []):
        commits.append({
            'hash':    c['hash'][:7],
            'author':  c['author']['user']['display_name'],
            'date':    c['date'],
            'message': c['message'].splitlines()[0]
        })
    return commits
