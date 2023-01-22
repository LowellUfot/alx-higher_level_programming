#!/usr/bin/python3
"""Module for Square definition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size):
        """initialises the Square class
        Args:
            size (int): positive integer
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
