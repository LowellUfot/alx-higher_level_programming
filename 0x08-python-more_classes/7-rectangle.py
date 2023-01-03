#!/usr/bin/python3

"""Rectangle module definition
This module defines a `Rectangle` class
"""


class Rectangle:
    '''This defines the Rectangle Object
    Attributes:
        width: width of the Rectangle
        height: height of the Rectangle
        number_of_instances: number of Rectangle instance
        print_symbol: symbol used to print Rectangle object
    '''
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __del__(self):
        """defines deleting the Rectangle object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of the Rectangle
        Returns:
            int: the area of Reactangle
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the Rectangle
        Returns:
            int: the perimeter of Rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """prints the rectangle in `#`"""
        hsh = ""
        if self.width == 0 or self.height == 0:
            return ("")
        for i in range(self.height):
            for j in range(self.width):
                try:
                    hsh += str(self.print_symbol)
                except Exception:
                    hsh += type(self.print_symbol)
            if i < self.height - 1:
                hsh += "\n"
        return hsh

    def __repr__(self):
        """prints the __repr__ method"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
