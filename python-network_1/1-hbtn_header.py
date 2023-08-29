"""
Request Module.

This is the python defined module to fetch a URL.
"""
import sys
import requests

url = sys.argv[-1]
req = requests.get(url)
req.headers('X-Request-Id')
