#!/usr/bin/python3
"""This module appends a string to a text file (UTF8)"""


def append_write(filename="", text=""):
    """Function to append string at end of file (UTF8)
    Args:
        filename (file): text file to append string
        text (str): string to append to filename
    Return:
        number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
