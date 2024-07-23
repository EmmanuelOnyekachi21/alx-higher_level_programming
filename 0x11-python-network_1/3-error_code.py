#!/usr/bin/python3

"""
- Takes in a URL,
- Sends a request to the URL,
- And displays the body of the response (decoded in utf-8)
"""

import urllib.request
import sys
import urllib.error.HTTPError

if __name__ == '__main__':

    # The URL
    url = sys.argv[1]

    # Sends a request
    request = urllib.request.Request(url)
    # Using try-except to catch exceptions
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
