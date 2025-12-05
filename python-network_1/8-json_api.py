#!/usr/bin/python3
"""
Takes a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as parameter 'q'.
"""

import requests
import sys


if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data=payload)
        json_data = response.json()

        if not json_data:
            print("No result")
        else:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")

    except ValueError:
        print("Not a valid JSON")

