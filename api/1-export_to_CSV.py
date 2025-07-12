#!/usr/bin/python3
"""
Python script that exports data in the CSV format
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    """
    Request user info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    )
    
    """
    Convert json to dictionary
    """
    user = json.loads(request_employee.text)
    
    """
    Extract username
    """
    username = user.get("username")
    
    """
    Request user's TODO list
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1])
    )
    
    """
    Convert json to list of dictionaries
    """
    user_todos = json.loads(request_todos.text)
    
    """
    Export to CSV
    """
    with open('{}.csv'.format(argv[1]), mode='w', newline='') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        
        """
        Loop through todos and write each task as a row
        """
        for todo in user_todos:
            file_editor.writerow([
                argv[1],  # User ID
                username,  # Username
                str(todo.get("completed")).lower(),  # Task status (true/false)
                todo.get("title")  # Task title
            ])
