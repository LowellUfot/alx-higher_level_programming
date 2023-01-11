#!/usr/bin/python3
"""This module defines a simple class"""


class BaseGeometry:
    """Base Geometry Class"""
    def __init__(self):
        pass

    def area(self):
        """area function
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate value
        Args:
            name (str): name description of value
            value (int): integer
        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(self.name))
        pass
