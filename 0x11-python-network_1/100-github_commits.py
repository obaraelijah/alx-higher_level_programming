#!/usr/bin/python3
"""Takes your github credentials and uses the github
API to display your id
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]

    res = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")

    try:
        res = res.json()
    except ValueError:
        pass
    else:
        for commit in res:
            id = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{id}: {author}")
