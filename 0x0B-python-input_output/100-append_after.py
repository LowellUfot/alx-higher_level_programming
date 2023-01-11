#!/usr/bin/python3
"""This module defines text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing search_string
    Args:
        filename (file): File name
        search_string (str): String to search for
        new_string (str): String to insert
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode='w') as w:
        w.write(text)
