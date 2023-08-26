#!/usr/bin/python3
"""
request Module.

This module provides functionality to fetch a URL using the urllib.request module.
"""

from requests import requests
    """
    Fetches content from the specified URL.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        bytes: The content fetched from the URL as bytes.
    """
url = 'https://alu-intranet.hbtn.io/status'

request = urllib.request.Request(url)

with urllib.request.urlopen(request) as response:
    site_content = response.read()

