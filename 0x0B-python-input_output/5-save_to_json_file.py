#!/usr/bin/python3
"""This module writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Function to write an Object to a text file using JSON rep
    Args:
        my_obj (object): object to be written using JSON representation
        filename (file): file to be written to
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
