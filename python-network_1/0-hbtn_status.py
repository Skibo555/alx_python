#!/usr/bin/python3
"""
request Module.

This module provides functionality to fetch a URL using the urllib.request module.
"""

import requests

response = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}\n"
      "\t- content: {}".format(type(response.text), response.text))
