#!/usr/bin/python3
"""This module returns the JSON rep of an object"""
import json


def to_json_string(my_obj):
    """Function to return JSON representation of an object
    Args:
        my_obj (object): object to return JSON representation
    Return:
        JSON representation of my_obj
    """
    return json.dumps(my_obj)
