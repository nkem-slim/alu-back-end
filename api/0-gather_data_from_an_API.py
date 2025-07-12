#!/usr/bin/python3
"""Gathering data from an API"""

import sys
import requests

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_info = requests.get(url).json()
    todo_info = requests.get(todo_url).json()

    employee_name = user_info.get("name")
    total_tasks = len(todo_info)
    completed_tasks = [task for task in todo_info if task.get("completed") is True]
    num_completed = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
