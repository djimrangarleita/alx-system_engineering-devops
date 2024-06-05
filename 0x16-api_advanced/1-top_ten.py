#!/usr/bin/python3
"""Query reddit api and print hot post titles of a subreddit"""


import requests


def top_ten(subreddit):
    """Print title of 10 hot posts"""
    endpoint = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0\
) Gecko/20100101 Firefox/47.0"}
    params = {'limit': 10}
    r = requests.get(endpoint, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    r = r.json()
    children = r.get('data').get('children')
    for child in children:
        print(child.get('data').get('title'))
