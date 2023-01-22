#!/usr/bin/python3
"""Defines MyInt Module"""


class MyInt(int):
    """class to revert == and != operators"""
    def __eq__(self, value):
        """changes == behaviour to !="""
        return self.real != value

    def __ne__(self, value):
        """changes != behaviour to =="""
        return self.real == value
