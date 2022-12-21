#!/usr/bin/python3
"""Square module definition.
This module defines a simple `Square` class
"""


class Square:
    """Square class definition

    Attributes:
        size (int): This is the size of ``Square``.
    """
    def __init__(self, size):
        """Class initalisation definition.

        Args:
            size (int): The size of ``Square``.
        """
        self.__size = size
