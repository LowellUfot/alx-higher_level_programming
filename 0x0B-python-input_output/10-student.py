#!/usr/bin/python3
"""This module defines a Student Class"""


class Student:
    """Student Class definition
    Args:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function to return dict representation of Student instance
        If attrs is a list of strings, return only the string attr
        in the list
        Args:
            attrs (list): the attributes to return
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return vars(self)
