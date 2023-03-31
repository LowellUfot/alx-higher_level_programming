#!/usr/bin/python3
"""Script to fetch URL"""
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as resp:
    html = resp.read()
    print('Body response: \n\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf8')))
