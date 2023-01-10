#!/usr/bin/python3
"""This module returns the object rep of a JSON string"""
import json


def from_json_string(my_str):
    """Function to return pbject representation of a JSON string
    Args:
        my_str (str): string to return JSON object representation
    Return:
        object representation of JSON string
    """
    return json.loads(my_str)
