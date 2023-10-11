#!/usr/bin/python3
import requests
import sys

# The base URL
base_url = "https://jsonplaceholder.typicode.com"

"""
GET: Making a get request from a romote API
"""
employee_id = len(sys.argv) - 1


def get_items(employee_id):
    """
    This is a function to get resources online.
    """
    response = requests.get("{}/users/{}".format(base_url, employee_id))

    # Making a GET request to retrieve employee's TODE list

    todo_list = requests.get("{}/users/{}/todos".format(base_url, employee_id))

    # Checking if the requests was successful.
    if response.status_code == 200:
        # Storing the response as a JSON file
        user_data = response.json()
        todo_data = todo_list.json()

        employee_name = user_data.get("name", "Unknown Employee")
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task["cpmpleted"])
        task_titles = [task["title"]
                       for task in todo_data if task["completed"]]

        """
        This is to print the todo progress
        """
        print("Employee {} is done with tasks ({}/{}):".format(employee_name,
              completed_tasks, total_tasks))
        for title in completed_tasks:
            print("/t{}".format(title))
        else:
            print("Failed to retrieve employee information and TODO list.")


if __name__ == "__main__":
    get_items(employee_id)
