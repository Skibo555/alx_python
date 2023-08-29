"""
Request Module.

This is the python defined module to fetch a URL.
"""
import sys
import requests

# Get the URL from the command-line arguments
url = sys.argv[-1]

# Send a request and get the response
response = requests.get(url)

# Check if the request was successful

if response.status_code == 200:
    print(response.headers.get('X-Request-Id'))
