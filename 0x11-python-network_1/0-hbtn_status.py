#!/usr/bin/python3
"""Fetches data from a url and displays in the body response using a urllib
package
"""

import urllib.request

if __name__ == "main":
    url="https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
    data = response.read()
    print('Body response')
    print(f'\t- type:", {type(data)}')
    print(f'\t- content: {data}')
    print(f'\t- utf8 content: {data.decode("UTF-8")}')

