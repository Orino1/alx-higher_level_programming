#!/usr/bin/python3
"""
takes your GitHub credentials (username and token)
and uses the GitHub API to display your id.
"""
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]
    url = f"https://api.github.com/users/{user}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    with requests.get(url, headers=headers) as response:
        data = response.json()
        print(data.get("id"))
