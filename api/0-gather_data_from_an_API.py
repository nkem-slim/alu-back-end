#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    
    # URLs for API endpoints
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )
    
    # Fetch data from API
    user_info = requests.get(user_url).json()
    todo_info = requests.get(todo_url).json()
    
    # Extract employee information
    employee_name = user_info.get("name")
    total_tasks = len(todo_info)
    
    # Filter completed tasks
    completed_tasks = [
        task for task in todo_info if task.get("completed") is True
    ]
    num_completed = len(completed_tasks)
    
    # Print results
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed, total_tasks
    ))
    
    # Print completed task titles with proper formatting
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
        