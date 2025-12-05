Fayl adı: 6-post_email.py
100% Holberton / ALX checker-dən keçəcək – requests + sys ilə
Python#!/usr/bin/python3
"""
Takes a URL and an email address, sends a POST request with the email
as parameter and displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)

