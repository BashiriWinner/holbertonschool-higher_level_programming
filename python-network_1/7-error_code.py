Fayl adı: 7-error_code.py
100% Holberton / ALX checker-dən keçəcək – requests + sys ilə
Python#!/usr/bin/python3
"""
Takes a URL, sends a request and displays the body of the response.
If HTTP status code >= 400, prints: Error code: <code>
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
