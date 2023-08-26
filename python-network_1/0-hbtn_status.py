#!/usr/bin/python3
"""
Request Module.

This module provides functionality to fetch a URL using the urllib.request module.
"""

from requests import requests
"""
This is to request a url using py
"""
url = 'https://alu-intranet.hbtn.io/status'

request = urllib.request.Request(url)

with urllib.request.urlopen(request) as response:
    site_content = response.read()

