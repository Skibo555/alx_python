"""
This is a module that gets a request.
"""

import sys
import requests

url = sys.argv[-1]

req = requests.get(url)

print(req.text)

if req.status_code >= 400:
    print("Error code: {}".format(req.status_code))
