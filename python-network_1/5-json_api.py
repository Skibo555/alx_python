"""
This module prints a module
"""

import sys
import requests

# Get the letter from the command-line argument, or set it to an empty string if not provided
if len(sys.argv) > 1:
    letter = sys.argv[1]
if len(sys.argv) < 1:
    letter = ""

# Define the URL
url = "http://0.0.0.0:5000/search_user"

# Send a POST request with the letter as a parameter
response = requests.post(url, data={'q': letter})

# Check if the response body is properly JSON formatted
if response.text.strip() and response.text.strip()[0] == "{" and response.text.strip()[-1] == "}":
    # Parse the JSON-like response manually
    response_parts = response.text.strip()[1:-1].split(",")
    id_ = ""
    name = ""
    for part in response_parts:
        key, value = part.split(":")
        if key.strip() == '"id"':
            id_ = value.strip('" ')
        elif key.strip() == '"name"':
            name = value.strip('" ')

    if id_ and name:
        print("[{}] {}".format(id_, name))
    else:
        print("No result")
else:
    if not response.text.strip():
        print("No result")
    else:
        print("Not a valid JSON")
