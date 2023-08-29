"""
This is a module that posts e-mails to a server.
"""

import sys
import requests

url = sys.argv[-2]
email = sys.argv[-1]

req = requests.post(url, data=email)

if requests.status_codes == 200:
    print(req.text)
