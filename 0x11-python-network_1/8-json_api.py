#!usr/bin/python3
"""Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    a = {}
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        a["q"] = ""
        else:
        a["q"] = sys.argv[1]

        res = requests.post(url, data=a)

        try:
            data = res.json()
        except ValueError:
            print("Not a valid JSON")
        else:
            if data == {}:
            print("Not a valid JSON")
             else:
                id = data.get('id')
                name = data.get('name')
                print(f"{id} {name}")
