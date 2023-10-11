#!/usr/bin/python3
import requests
import sys

# The base URL
base_url = "https://jsonplaceholder.typicode.com"


def get_items(employee_id):
    # Make a GET request to retrieve employee details
    response = requests.get("{}/users/{}".format(base_url, employee_id))

    # Make a GET request to retrieve employee's TODO list
    todo_list = requests.get("{}/users/{}/todos".format(base_url, employee_id))

    # Check if the requests were successful
    if response.status_code == 200 and todo_list.status_code == 200:
        # Store the responses as JSON
        user_data = response.json()
        todo_data = todo_list.json()

        employee_name = user_data.get("name", "Unknown Employee")
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task["completed"])
        task_titles = [task["title"]
                       for task in todo_data if task["completed"]]

        # Print the todo progress
        print("Employee {} is done with tasks({}/{}):".format(employee_name,
              completed_tasks, total_tasks))
        for title in task_titles:
            print("\t {}".format(title))
    else:
        print("Failed to retrieve employee information and TODO list.")


if __name__ == "__main__":
    # Check if an employee ID was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Get the employee ID from the command-line argument
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_items(employee_id)
