#!/usr/bin/python3
"""
A script that uses a REST API to pull data regarding all employees
and exports their full TODO list history into a single grouped JSON file.
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch all users to gather user IDs and usernames
    users_res = requests.get("{}/users".format(base_url)).json()
    
    all_employees_data = {}
    
    for user in users_res:
        user_id = str(user.get("id"))
        username = user.get("username")
        
        # Fetch tasks specifically filtered for this user
        todos_url = "{}/todos?userId={}".format(base_url, user_id)
        todos_res = requests.get(todos_url).json()
        
        # Format individual tasks per required structural layout
        tasks_list = []
        for task in todos_res:
            tasks_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })
            
        # Map formatting to corresponding user ID key
        all_employees_data[user_id] = tasks_list

    # Export completely generated dictionary into the exact required file name
    file_name = "todo_all_employees.json"
    with open(file_name, mode="w") as json_file:
        json.dump(all_employees_data, json_file)

