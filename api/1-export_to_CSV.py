#!/usr/bin/python3
import csv
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

        # Generate a dynamic filename
        filename = f"employee_{employee_id}_todos.csv"

        # Prepare data for CSV
        employee_name = user_data.get("name", "Unknown Employee")
        csv_data = []

        # Determine fieldnames from the first task
        if todo_data:
            first_task = todo_data[0]
            fieldnames = first_task.keys()
        else:
            fieldnames = ["employee_id",
                          "employee_name", "status", "task_title"]

        for task in todo_data:
            # Convert task status to "True" or "False"
            status = "True" if task["completed"] else "False"
            task_title = task["title"]
            csv_data.append([employee_id, employee_name, status, task_title])

        # Print the todo progress to the dynamically generated filename
        with open(filename, 'wt') as csvfile:
            my_writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            my_writer.writeheader()

            for row in csv_data:
                my_writer.writerow(
                    {key: value for key, value in zip(fieldnames, row)})
    else:
        print(
            f"Failed to retrieve employee {employee_id}'s information and TODO list.")


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
