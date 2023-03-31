#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) > 1:
        payload = {'q': sys.arg[1]}
    else:
        payload = {'q': ""}
    r = requests.get('http://0.0.0.0:5000/search_user', data=payload)
    try:
        r_json = r.json()
        if r_json is not NULL:
            print('[{}] {}'.format(r_json['id'], r_json['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
