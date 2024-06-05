#!/usr/bin/python3
"""
Query reddit api and print hot post titles of a subreddit
"""
import requests


def top_ten(subreddit):
    """Print title of 10 hot posts"""
    endpoint = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PersonalAgent/5.0"}
    params = {"limit": 10}
    r = requests.get(endpoint, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    try:
        data = r.json()
        children = data.get("data", {}).get("children", [])
        for child in children:
            print(child.get("data").get("title"))
    except Exception:
        pass
