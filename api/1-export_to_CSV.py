#!/usr/bin/python3
"""
A script that uses a REST API to pull data regarding a given employee ID
and exports all their tasks into a CSV format file.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com/"
        
        # Fetch user details (specifically username)
        user_url = "{}/users/{}".format(base_url, emp_id)
        user_res = requests.get(user_url).json()
        username = user_res.get("username")
        
        # Fetch all tasks for this user
        todos_url = "{}/todos?userId={}".format(base_url, emp_id)
        todos_res = requests.get(todos_url).json()
        
        # Write to USER_ID.csv with full quoting enabled
        file_name = "{}.csv".format(emp_id)
        with open(file_name, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos_res:
                writer.writerow([
                    emp_id,
                    username,
                    task.get("completed"),
                    task.get("title")
                ])

