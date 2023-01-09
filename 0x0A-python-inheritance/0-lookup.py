#!/usr/bin/python3
"""
    This module defines the lookup function
"""


def lookup(obj):
    """Function that returns list of available attributes
        and method of an object
        Args:
            obj (object): python object
        Return:
            list of attributes an method in obj
    """
    return dir(obj)
