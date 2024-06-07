#!/usr/bin/python3
"""
Query reddit api and print hot post titles of a subreddit
"""
from json import JSONDecodeError
import requests


def top_ten(subreddit):
    """Print title of 10 hot posts."""
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "PersonalAgent/5.0"}
    params = {"limit": 10}
    print(None)
