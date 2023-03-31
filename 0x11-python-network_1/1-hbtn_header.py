#!/usr/bin/python3
"""
akes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "main":

    url=sys.argv[1]
    with urllib.request.urlopen(url) as response:
        data = response.headers.get('X-Request-Id')
        print(data)
