#!/usr/bin/python3
"""Module to read text file in UTF8 encoding"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints to stdout"""
    with open('filename' encoding='utf-8') as a_file:
        for line in a_file:
            print(a_file.read())
