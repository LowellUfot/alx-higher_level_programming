#!/usr/bin/python3
"""Square module definition.
This module defines a simple `Square` class
"""


class Square:
    """Square class definition

    Attributes:
        size (int): This is the size of ``Square``.
    """
    def __init__(self, size=0, postion=(0, 0)):
        """Class initalisation definition.

        Args:
            size (int): The size of ``Square``.
            position (tuple): where the square is
                i.e., the co-ordinate position(x, y)
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

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
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
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
        if isinstance(value, tuple) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """area method definition.
        Returns:
            int: The area of ``Square``.
        """
        return self.__size ** 2

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Prints a square in position"""
        print(self.pos_print(), end="")
