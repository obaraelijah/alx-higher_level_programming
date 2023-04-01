#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': argv[2]}

    res = requests.post(url, email=email)
    print(res.text)
