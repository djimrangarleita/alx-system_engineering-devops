#!/usr/bin/python3
"""Read data from API source"""


import json
import requests
from sys import argv


def read_json():
    """Read and print json data from API"""
    username = get_username()
    if (not username):
        return
    r = requests.get(url_todos)
    todos = r.json()
    all_todos = []
    for task in todos:
        item = {}
        item['task'] = task.get('title')
        item['completed'] = task.get('completed')
        item['username'] = username
        all_todos.append(item)
    return {userId: all_todos}


def get_username():
    """Print user task"""
    r = requests.get(url_users)
    user = r.json()
    return user.get('username') if user else None


def write_json():
    """Write all todos to a csv file"""
    all_todos = read_json()
    filename = f'{userId}.json'
    with open(filename, mode='w') as json_file:
        json.dump(all_todos, json_file)


if __name__ == "__main__":
    userId = argv[1]
    url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={userId}'
    url_users = f'https://jsonplaceholder.typicode.com/users/{userId}'
    write_json()
