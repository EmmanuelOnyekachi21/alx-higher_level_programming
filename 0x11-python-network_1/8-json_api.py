#!/usr/bin/python3

"""
- Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user,
- with the letter as a parameter.
"""

import requests
import sys


if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ''

    payload = {'q': q}

    r = requests.post('http://0.0.0.0:5000/search_user', param=payload)

    try:
        json_response = r.json()

        if len(json_response) <= 0:
            print('No result')
        else:
            r_id = r.get('id')
            r_name = r.get('name')

            if r_id is not None and r_name is not None:
                print(f"[{user_id}] {name}")
            else:
                print("No result")
    except ValueError:
        # Handle cases where the response is not a valid JSON
        print('Not a valid JSON')
