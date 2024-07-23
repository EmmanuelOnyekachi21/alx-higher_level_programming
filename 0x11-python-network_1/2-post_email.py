#!/usr/bin/python3

"""
- Takes a URL,
- Sends a POST request to the passed URL with the email as a parameter,
- and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    # Create the data dictionary with the email parameter
    value = {'email': email}

    # Encode the data to be sent in the POST request
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')

    # Create a POST request with the encoded data
    request = urllib.request.Request(url, data)

    # Send the request and get the response
    with urllib.request.urlopen(request) as response:
        # Read the response body
        body = response.read()

        # Decode the response body
        body = body.decode('utf-8')

    # Print the response body
    print(body)
