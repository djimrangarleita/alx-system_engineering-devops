#!/usr/bin/python3
"""Read data from API source"""


import csv
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
    keys = ['userId', 'username', 'completed', 'title']
    for task in todos:
        task['username'] = username
        item = {key: task.get(key) for key in keys}
        all_todos.append(item)
    return all_todos


def get_username():
    """Print user task"""
    r = requests.get(url_users)
    user = r.json()
    return user.get('username') if user else None


def write_csv():
    """Write all todos to a csv file"""
    all_todos = read_json()
    filename = f'{userId}.csv'
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=all_todos[0].keys(),
                                quoting=csv.QUOTE_ALL)
        writer.writerows(all_todos)


if __name__ == "__main__":
    userId = argv[1]
    url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={userId}'
    url_users = f'https://jsonplaceholder.typicode.com/users/{userId}'
    write_csv()
