#!/usr/bin/python3
"""
Script to listthe  10 most recent commits
"""

import requests
import sys


if __name__ == "__main__":

    git_api = 'https://api.github.com/repos/{}/{}/commits'.format(
                sys.argv[2], sys.argv[1])

    r = requests.get(git_api)
    r_json = r.json()
    for i in range(10):
        print('{}: {}'.format(
            r_json[i].get('sha'),
            r_json[i].get('commit').get('author').get('name')))
