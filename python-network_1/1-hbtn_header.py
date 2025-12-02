#!/usr/bin/python3
"""
Takes a URL, sends a request and displays the value of the X-Request-Id header.
"""

import urllib.request
import sys


def main():
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        request_id = headers.get('X-Request-Id')

    print(request_id)


if __name__ == "__main__":
    main()
