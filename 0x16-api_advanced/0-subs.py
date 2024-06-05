#!/usr/bin/python3
"""Query reddit api and return the number of subscribers of a subreddit"""


import requests


def number_of_subscribers(subreddit):
    """Return number of subcribers"""
    endpoint = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(endpoint, allow_redirects=False)
    if r.status_code != 200:
        return 0
    r = r.json()
    data = r.get('data')
    return data.get('subscribers')
