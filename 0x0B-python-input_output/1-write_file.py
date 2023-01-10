#!/usr/bin/python3
"""This module writes to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Function to write string to text file (UTF8)
    Return:
        number of characters written to text file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
