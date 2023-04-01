#!/usr/bin/python3
"""Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    d = {}

    if len(argv) < 2:
        d["q"] = ""
    else:
        d["q"] = argv[1]

    data = requests.post("http://0.0.0.0:5000/search_user", data=d)

    try:
        data = data.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if data == {}:
            print("No result")
        else:
            id = data.get('id')
            name = data.get('name')
            print(f"[{id}] {name}")
