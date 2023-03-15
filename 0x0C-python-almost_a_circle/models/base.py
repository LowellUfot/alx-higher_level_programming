#!/usr/bin/python3
"""Base Module definition"""


class Base:
    """Defines a Class called Base for other classes to inherit from
    Args:
        id (int): integer
        __nb_objects (int): private class attribute
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """initialises the Base class"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
