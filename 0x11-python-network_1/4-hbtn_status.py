#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using requests"""
import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    res = requests.get(url)
    data = res.text
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
