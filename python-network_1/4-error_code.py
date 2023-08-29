"""
This is a module that gets a request.
"""

import sys
import requests

url = sys.argv[-1]

req = requests.get(url)

if req.status_code >= 400:
    print("Error code:{%d}", req.status_code)
