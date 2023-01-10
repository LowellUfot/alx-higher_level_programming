#!/usr/bin/python3
"""This module creates an Object from JSON file"""
import json


def load_from_json_file(filename):
    """Function to create an Object from a JSON file
    Args:
        filename (file): file to create Object from
    """
    with open(filename, encoding='utf-8') as a_file:
        return json.load(filename)
