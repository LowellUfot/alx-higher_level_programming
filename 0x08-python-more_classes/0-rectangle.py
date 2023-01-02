#!/usr/bin/python3
"""Rectangle module definition
This module defines a `Rectangle` class
"""


class Rectangle:
    '''This defines the Rectangle Object
    Attributes:
        width: width of the Rectangle
        height: height of the Rectangle
    '''
    def __init__(self, width=0, height=0):
        """Initialises the Rectangle object
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
                default values of 0
        Raises:
            TypeError: if width, height is not an integer
            ValueError: if width, height is < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
