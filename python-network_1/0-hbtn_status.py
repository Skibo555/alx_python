#!/usr/bin/python3
"""
request Module.

This module provides functionality to fetch a URL using the urllib.request module.
"""

from requests import requests


url = 'https://alu-intranet.hbtn.io/status'

request = urllib.request.Request(url)

with urllib.request.urlopen(request) as response:
    site_content = response.read()

