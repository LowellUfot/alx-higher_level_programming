#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8).
"""

import requests
import sys


if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], email)
    print('{}'.format(r.text))
