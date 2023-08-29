"""
This module prints a module
"""

import sys
import requests

import sys
import requests

# Get the letter from the command-line argument, or set it to an empty string if not provided
if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

# Define the URL
url = "http://0.0.0.0:5000/search_user"

# Send a POST request with the letter as a parameter
response = requests.post(url, data={'q': letter})

try:
    # Try to parse the response content as JSON
    json_data = response.json()

    # Check if the response is a non-empty dictionary
    if isinstance(json_data, dict) and json_data:
        id_ = json_data.get('id', '')
        name = json_data.get('name', '')
        print("[{}] {}".format(id_, name))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
