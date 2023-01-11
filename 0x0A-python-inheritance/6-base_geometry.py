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
