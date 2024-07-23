#!/usr/bin/python3

"""
- Takes a URL, and an email address,
- Sends a POST request to the passed URL with the email as a parameter,
- And fiinally displays the body of the response.
"""

import requests
import sys


if __name__ == '__main__':

    # Creating payload with the email
    payload = {'email': sys.argv[2]}

    # Sends a POST request to the URL with the email as a parameter
    r = requests.post(sys.argv[1], data=payload)

    # Display the body of the response (decoded in utf-8)
    print(r.text)
