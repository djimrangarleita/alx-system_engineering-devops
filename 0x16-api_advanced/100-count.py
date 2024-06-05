#!/usr/bin/python3
"""
Query reddit api and return hot post titles of a subreddit
"""
import requests


def count_words(subreddit, word_list, next_elt=True, count={}):
    """Return title of all hot posts"""
    endpoint = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PersonalAgent/5.0"}
    params = {"after": next_elt}
    sanitized_list = get_sanitized_words(word_list)
    if not next_elt:
        return sort_and_print(count)
    else:
        response = requests.get(endpoint, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get("data")
        next_elt = data.get("after")
        children = data.get("children")
        for child in children:
            title = child.get("data").get("title")
            #hot_list.append(child.get("data").get("title"))
            for word in sanitized_list:
                if word in title.lower():
                    count[word] = count.get(word, 0) + 1
        return count_words(subreddit, word_list, next_elt, count)


def get_sanitized_words(words_list):
    """Return a sanitized list of the worlds"""
    words_list = [word.lower() for word in words_list]
    return words_list

def sort_and_print(count):
    """Sort and print"""
    sorted_data = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_data.items():
        print("{}: {}".format(key, value))
