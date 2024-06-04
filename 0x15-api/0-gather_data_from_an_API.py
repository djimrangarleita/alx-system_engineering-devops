#!/usr/bin/python3
"""Read data from API source"""


import requests
from sys import argv


def read_json():
    """Read and print json data from API"""
    name = get_user()
    if (not name):
        return
    completed_tasks = 0
    total = 0
    todos_list = ''
    r = requests.get(url_todos)
    todos = r.json()
    for task in todos:
        total += 1
        if task.get('completed'):
            completed_tasks += 1
            todos_list += ('\t' + task.get('title') + '\n')
    print(f"Employee {name} is done with tasks({completed_tasks}/{total}):")
    print(todos_list, end='')


def get_user():
    """Print user task"""
    r = requests.get(url_users)
    user = r.json()
    return user.get('name') if user else None


if __name__ == "__main__":
    url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    url_users = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    read_json()
