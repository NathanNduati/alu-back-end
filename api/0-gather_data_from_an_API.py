#!/usr/bin/python3
"""
A script that uses a REST API to pull data regarding a given employee ID
and displays information about their TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com/"
        
        # Fetch user information safely
        user_url = "{}/users/{}".format(base_url, emp_id)
        user_res = requests.get(user_url).json()
        employee_name = user_res.get("name")
        
        # Fetch todo items assigned to user
        todos_url = "{}/todos?userId={}".format(base_url, emp_id)
        todos_res = requests.get(todos_url).json()
        
        # Filter and count tasks
        completed_tasks = [task for task in todos_res if task.get("completed")]
        total_tasks = len(todos_res)
        done_count = len(completed_tasks)
        
        # Print results with correct formatting
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, done_count, total_tasks
        ))
        
        for task in completed_tasks:
            print("\t {}".format(task.get("title")))

