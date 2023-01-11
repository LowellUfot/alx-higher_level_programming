#!/usr/bin/python3
"""This module returns dictionary representation"""


def class_to_json(obj):
    """Function to return dictionary description"""
    return vars(obj)
