#!/usr/bin/python3
"""
Query reddit api and return the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subcribers"""
    endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "PersonalAgent/4.0"}
    response = requests.get(endpoint, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    result = data.get("subscribers")
    return result
