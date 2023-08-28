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
    try:
        response = requests.get(url)
        response.raise_for_status()

        x_requests_id = response.headers.get('X-Request-Id')

        if x_requests_id is not None:
            return x_requests_id
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
def another():
    """
    This is a function that gets the argment from the command line.

    Arg:
        sys.argv[]

    Return:
        sys.argv[1]
    """
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_an_input(url)


    if x_request_id is not None:
        return x_request_id
