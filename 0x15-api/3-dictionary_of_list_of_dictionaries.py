#!/usr/bin/python3
"""Read data from API source"""


import json
import requests


def read_json():
    """Read and print json data from API"""
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    user = {}
    r = requests.get(url_todos)
    todos = r.json()
    all_todos = {}
    for task in todos:
        userId = task.get('userId')
        username = user.setdefault(userId, get_username(userId))
        item = {}
        item['username'] = username
        item['task'] = task.get('title')
        item['completed'] = task.get('completed')
        users_todos = all_todos.get(userId, [])
        users_todos.append(item)
        all_todos[userId] = users_todos
    return all_todos


def get_username(userId):
    """Print user task"""
    r = requests.get('https://jsonplaceholder.typicode.com/users/{userId}')
    user = r.json()
    return user.get('username') if user else None


def write_json():
    """Write all todos to a csv file"""
    all_todos = read_json()
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as json_file:
        json.dump(all_todos, json_file)


if __name__ == "__main__":
    write_json()
