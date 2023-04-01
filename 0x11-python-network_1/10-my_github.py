#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":

    git_api = 'https://api.github.com/user'

    r = requests.get(git_api, auth=(sys.argv[1], sys.argv[2]))
    r_json = r.json()
    if r_json == {}:
        print("None")
    else:
        print('{}'.format(r_json.get('id')))
