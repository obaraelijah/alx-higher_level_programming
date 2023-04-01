#!/usr/bin/python3
"""Takes your github credentials and uses the github
API to display your id
"""
import sys
import requests

if __name__ == '__main__':
 
    repo_owner =sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_owner}/commits"
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
