#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib"""

if __name__ == "__main__":
    from urllib import request
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        data = response.read()
        print('Body response:')
        print(f'\t- type: {type(data)}')
        print(f'\t- content: {data}')
        print(f'\t- utf8 content: {data.decode("UTF-8")}')
