#!/usr/bin/python3
"""Square module definition.
This module defines a simple `Square` class
"""


class Square:
    """Square class definition

    Attributes:
        size (int): This is the size of ``Square``.
    """
    def __init__(self, size=0):
        """Class initalisation definition.

        Args:
            size (int): The size of ``Square``.

        Raises:
            TypeError: If ``size`` is not an integer.
            ValueError: If ``size`` < 0
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            reise ValueError("size ust be >= 0")
        else:
            self.__size = size
