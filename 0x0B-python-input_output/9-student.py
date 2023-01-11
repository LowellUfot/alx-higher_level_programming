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

    def to_json(self):
        """function to return dict representation of Student instance"""
        return vars(self)
