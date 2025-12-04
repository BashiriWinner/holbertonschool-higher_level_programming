#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using the requests package
and displays the body response in the required format.
"""

import requests


def fetch_status():
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")


if __name__ == "__main__":
    fetch_status()
