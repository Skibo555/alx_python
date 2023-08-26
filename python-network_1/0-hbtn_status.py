"""
Request Module.

This is the python defined module to fetch a URL.
"""
from requests import requests
    """
    This module fetches a url using.

    Arg:
        urllib.request.Request module.

    Return:
        Response.
    """
work = urllib.request.Request('https://alu-intranet.hbtn.io/status')
with urllib.request.urlopen(work) as response:
    site = response.read()
