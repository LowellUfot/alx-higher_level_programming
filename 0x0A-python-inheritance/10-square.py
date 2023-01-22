#!/usr/bin/python3
"""Module for Square definition"""


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size):
        """initialises the Square class
        Args:
            size (int): positive integer
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of the square"""
        return self.size ** 2
