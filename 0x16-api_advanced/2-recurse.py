#!/usr/bin/python3
"""
Query reddit api and return hot post titles of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], next_elt=True):
    """Return title of all hot posts"""
    endpoint = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PersonalAgent/5.0"}
    params = {"after": next_elt}
    if not next_elt:
        return hot_list
    else:
        response = requests.get(endpoint, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get("data")
        next_elt = data.get("after")
        children = data.get("children")
        for child in children:
            hot_list.append(child.get("data").get("title"))
        return recurse(subreddit, hot_list, next_elt)
