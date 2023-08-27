"""
Request Module.

This is the python defined module to fetch a URL.
"""
import sys
import requests

def get_an_input():
    """
    This Module is to get the a url from the command line using.

    Argument:
        sys.agrv[]: The positional argument from the command line.
    
    Return:
        sys.agrv[1].

    """
    if sys.argv != 2:
        url = sys.argv[1]
        return url

def get_the_url():
    """
    This module runs the positional arguement which is the url.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.raise_for_status == 200:
            x_request_id = response.headers.get('X-Request-Id')
            
            if x_request_id is not None:
                return ("X-Request-Id:", x_request_id)

    except requests.exceptions.RequestException as e:
        sys.exit(1)
    return(response.text)
