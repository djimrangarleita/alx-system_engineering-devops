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
    try:
        r = requests.get(endpoint, headers=headers, params=params,
                         allow_redirects=False)
        r.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        print(None)
        return
    except requests.exceptions.RequestException as e:
        print(f"Request error occurred: {e}")
        print(None)
        return

    try:
        data = r.json()
        children = data.get("data", {}).get("children", [])
        for child in children:
            print(child.get("data").get("title"))
    except JSONDecodeError:
        print("Failed to decode JSON response")
        print(f"Response content: {r.text}")
        print(None)
    except Exception as e:
        print(f"An error occurred: {e}")
        print(None)
