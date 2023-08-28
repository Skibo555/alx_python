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
    if len(sys.argv) >= 1:
        url = sys.argv[-1]
        return url
    else:
        exit(1)

def get_the_positional_arg():
    """
    This module is to the the last argument on the command line.
    """
    method = resquests.get(url)
    view = method.header('X-Request-Id')
    return view
