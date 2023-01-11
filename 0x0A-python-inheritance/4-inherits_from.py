#!/usr/bin/python3
"""Module defines if object is an instance of a class"""


def inherits_from(obj, a_class):
    """Function to check if the object is an instance
    of a class that inherited (directly or indirectly) from a
    specified class
    Args:
        obj (object): object to check
        a_class (object): class object being checked against
    Return:
        True if object is exactly an instance of class
        False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
