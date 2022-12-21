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
        self.__size = size

    @property
    def size(self):
        """
        Args:
        size (int): The size of ``Square``.
            Default value is 0.

        Raises:
            TypeError: If ``size`` is not an integer
            ValueError: If ``size`` < 0
        """
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area method definition.
        Returns:
            int: The area of ``Square``.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square of `#`"""
        if self.size:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
