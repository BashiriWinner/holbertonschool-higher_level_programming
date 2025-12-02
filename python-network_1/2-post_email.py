#!/usr/bin/python3
"""
Sends a POST request to the given URL with the email as a parameter
parameter and displays the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys


def send_post_email(url, email):
    # email parametrini POST gövdəsinə çeviririk
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # POST sorğusu yaradırıq
    req = urllib.request.Request(url, data=data, method='POST')

    # Sorğunu göndəririk və cavabı alırıq
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

    print(body)


if __name__ == "__main__":
    url = sys.argv[1]      # birinci arqument – URL
    email = sys.argv[2]    # ikinci arqument – email
    send_post_email(url, email)
