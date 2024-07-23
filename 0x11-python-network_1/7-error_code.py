#!/usr/bin/python3

"""
- Takes a URL as an argument.
- Sends a request to the URL,
- and displays the body of the response.
"""

import requests
import sys


if __name__ == '__main__':
    # Get the URL from commandline arguments
    url = sys.argv[1]

    # Sends a request to the URL
    response = requests.get(url)

    # Check if status code is greater than or equal to 400
    if response.status_code >= 400:
        print(f'Error code: {response.status_code}')

    else:
        # Display the body of the response
        print(response.text)
