#!/usr/bin/python3
"""
    Module to add two integers
"""


def add_integer(a, b=98):
    """Function to add two integers

    Args:
        a (int or float): first parameter
        b (int or float): second parameter
    Raises:
        TypeError: If a and b are not integers or float
    Note:
        a and b will be casted to integers if they are float
    Return:
        the addition of a and b
    """
    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
