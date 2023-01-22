#!/usr/bin/python3
"Defines function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible
    Args:
        obj (any): object to add to an attribute to
        att 9any0: name of attribute to add to obj
        value (any): valu of obj
    Raises:
        TypeError: If the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
