"""
Request Module.

This is the python defined module to fetch a URL.
"""
import sys
import requests

# Get the URL from the command-line arguments
url = sys.argv[1]

# Send a request and get the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the value of the X-Request-Id header
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print("X-Request-Id:", x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
else:
    print("Request was not successful. Status code:", response.status_code)
