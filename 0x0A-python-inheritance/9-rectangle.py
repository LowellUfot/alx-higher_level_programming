#!/usr/bin/python3
"""Simple Rectangle class inheriting BaseGeometry()"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Simple Rectangle class"""

    def __init__(self, width, height):
        """Initialise the Rectangle class
        Args:
            width (int): positive integer, width
            height (int): positive integer, height
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
