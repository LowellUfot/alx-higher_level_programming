#!/usr/bin/python3
"""Module defines if object is an instance of a class"""


def is_same_class(obj, a_class):
    """Function to check if the object is exactly an instance
    of the specified class
    Args:
        obj (object): object to check
        a_class (object): class object being checked against
    Return:
        True if object is exactly an instance of class
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
