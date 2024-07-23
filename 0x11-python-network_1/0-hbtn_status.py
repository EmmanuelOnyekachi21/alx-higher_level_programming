#!/usr/bin/python3

"""
Fetches https://alx-intranet.hbtn.io/status.
"""

import urllib.request


if __name__ == '__main__':
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')

    with urllib.request.urlopen(request) as response:
        the_page = response.read()

        print(f'Body response:$')
        print(f'\t- type: {type(the_page)}')
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode('utf-8')))
