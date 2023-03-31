#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print('{}'.format(resp.read().decode('utf-8')))
    except HTTPError as e:
        print('Error code:', e.code)
