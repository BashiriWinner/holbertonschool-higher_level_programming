#!/usr/bin/python3
"""
Sends a POST request to the given URL with the email as a parameter
parameter and displays the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys


def send_post_email(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

    print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_email(url, email)
