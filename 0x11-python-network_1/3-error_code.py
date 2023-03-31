#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print("Error code:", e.code)
    else:
        print(body.decode('utf-8'))

