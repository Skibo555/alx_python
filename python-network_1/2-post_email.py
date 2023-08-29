"""
This is a module that posts e-mails to a server.
"""

import sys
import requests

url = sys.argv[-2]
email = sys.argv[-1]
data = {"email": email}

req = requests.post(url, data=data)

if req.status_code == 200:
    print(req.text)
