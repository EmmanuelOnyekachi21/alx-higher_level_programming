#!/usr/bin/python3

"""
Fetches https://alx-intranet.hbtn.io/status (using requests module).
"""

import requests


if __name__ == '__main__':
    # Send a GET request to the URL
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(f'Body response:')
    print(f'\t- type: {type(response.text)}')
    print("\t- content: {}".format(response.text))
