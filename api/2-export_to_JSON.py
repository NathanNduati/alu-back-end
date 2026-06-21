#!/usr/bin/python3
"""
A script that uses a REST API to pull data regarding a given employee ID
and exports all their tasks into a structured JSON format file.
"""
import json
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
        
        # Format the task dictionaries to match required structural schema
        tasks_list = []
        for task in todos_res:
            tasks_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            })
            
        # Structure the top level wrapper dictionary
        json_data = {emp_id: tasks_list}
        
        # Write out to the dynamic JSON file name
        file_name = "{}.json".format(emp_id)
        with open(file_name, mode="w") as json_file:
            json.dump(json_data, json_file)

