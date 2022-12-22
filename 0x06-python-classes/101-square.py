#!/usr/bin/python3
"""Square module definition.
This module defines a simple `Square` class
"""


class Square:
    """Square class definition
    Attributes:
        size (int): This is the size of ``Square``.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Class initalisation definition.
        Args:
            size (int): The size of ``Square``.
            position (tuple): where the square is
                i.e., the co-ordinate position(x, y)
        """
        self.size = size
        self.position = position

    def __str__(self):
        res = ""
        if self.size:
            line = " " * self.position[0] + "#" * self.size
            res = "\n" * self.position[1]
            res += (line + "\n") * (self.size - 1)
            res += line
        return res

    @property
    def size(self):
        """Size as the len of a side of a square
        Raises:
            TypeError: If ``size`` is not an integer
            ValueError: If ``size`` < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """co-ordinate(x, y) defintion of ``Square``.
        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the co-ordinate(x, y) of ``Square``.
        Args: value as tuple of 2 positive integers
        Raises:
            TypeError: if value is nor a tuple of 2 positve integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area method definition.
        Returns:
            int: The area of ``Square``.
        """
        return self.size ** 2

    def my_print(self):
        """Prints a square with `#`"""
        print(self)
