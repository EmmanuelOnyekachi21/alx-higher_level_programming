#!/usr/bin/python3

"""
- Takes a URL,
- Sends a request to the URL and displays the value of 'X-Request_Id'
"""

import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        headers = response.info()
        x_Request_Id = headers.get('X-Request-Id')
        print(x_Request_Id)
