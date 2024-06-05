#!/usr/bin/python3
"""Query reddit api and return the number of subscribers of a subreddit"""


import requests


def number_of_subscribers(subreddit):
    """Return number of subcribers"""
    endpoint = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0\
) Gecko/20100101 Firefox/47.0"}
    r = requests.get(endpoint, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0
    r = r.json()
    data = r.get('data')
    return data.get('subscribers')
