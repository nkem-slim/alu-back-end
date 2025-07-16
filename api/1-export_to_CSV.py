#!/usr/bin/python3

"""This module downloads from an api (jsonplaceholder api)
and stores it in a csv file"""
import csv
import requests
import sys

if __name__ == "__main__":
    employer_number = sys.argv[1]
    raw_user_data = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={employer_number}")
    raw_todo_data = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employer_number}")
    user_json = raw_user_data.json()
    todo_json = raw_todo_data.json()

    username = user_json[0]["username"]

    filename = f"{employer_number}.csv"
    with open(filename, "w", newline="") as file:
        for todo in todo_json:
            file.write('"' + str(employer_number) + '",' +
                       '"' + str(username) + '",' +
                       '"' + str(todo['completed']) + '",' +
                       '"' + str(todo['title']) + '",' + '\n'
                       )
