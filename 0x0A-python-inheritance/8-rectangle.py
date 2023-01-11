#!/usr/bin/python3
"""Simple Rectangle class inheriting BaseGeometry()"""
BaseGeometry = __import__('7.base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Simple Rectangle class
    Args:
        width (int): positive integer, width
        height (int): positive integer, height
    """
    def __init__(self, width, height):
        """initialises the Rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
