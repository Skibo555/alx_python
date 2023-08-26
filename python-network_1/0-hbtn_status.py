#!/usr/bin/python3
"""
Request Module.

This module provides functionality to fetch a URL using the urllib.request module.
"""

from requests import requests

# Define the URL to be fetched
url = 'https://alu-intranet.hbtn.io/status'

# Create a request object for the URL
request = urllib.request.Request(url)

# Open the URL and read the response
with urllib.request.urlopen(request) as response:
    site_content = response.read()

