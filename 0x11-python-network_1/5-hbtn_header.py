#!/usr/bin/python3

"""
- Takes in a URL,
- Sends a request to the URL,
- displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys


if __name__ == "__main__":

    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Send a GET request to the URL
    r = requests.get(url)

    # Get the value of the 'X-Request-Id' from the response headers
    value = r.headers.get('X-Request-Id')

    # Print the value of 'X-Request-Id'
    print(value)
