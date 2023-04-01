#!/usr/bin/python3

import sys
import requests

if __name__ == "__main__":
    
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    res = requests.get(url)

    try:
        res = res.json()
    except ValueError:
        pass
    else:
        for commit in res:
            id = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{id}: {author}")
