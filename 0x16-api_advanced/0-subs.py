import json
import urllib.request
import urllib.error
"""A comment"""


def number_of_subscribers(subreddit):
    """Return number of subscribers"""
    endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "PersonalAgent/4.0"}

    try:
        req = urllib.request.Request(endpoint, headers=headers)
        with urllib.request.urlopen(req, allow_redirects=False) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data['data']['subscribers']
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Subreddit not found")
        else:
            print("Error:", e)
    except Exception as e:
        print("Error:", e)
    return 0
