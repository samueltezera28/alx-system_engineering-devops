#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            if task.get('completed'):
                completed += 1

    print('Employee {:s} is done with tasks({:d}/{20}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t" + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
