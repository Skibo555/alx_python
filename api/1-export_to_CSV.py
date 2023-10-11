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

        employee_name = user_data.get("name", "Unknown Employee")
        employee_username = user_data.get("username", "Unknown Username")

        # Create a list to store the CSV rows
        csv_data = []

        for task in todo_data:
            task_status = "Completed" if task["completed"] else "Not Completed"
            task_title = task["title"]
            csv_data.append([employee_id, employee_name,
                            employee_username, task_status, task_title])

        # Print the todo progress
        print("Employee {} is done with tasks({}/{}):".format(employee_name +
              len(todo_data), len(todo_data)))
        for task in csv_data:
            print("\t {}, {}, {}, {}".format(
                task[0], task[1], task[3], task[4]))

        # Write the data to a CSV file
        with open('{}_tasks.csv'.format(employee_id), 'w', newline='') as csvfile:
            my_writer = csv.writer(csvfile)
            my_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            my_writer.writerows(csv_data)
    else:
        print("Failed to retrieve employee information and TODO list.")


if __name__ == "__main":
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
