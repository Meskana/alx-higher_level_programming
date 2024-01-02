#!/usr/bin/python3

"""
a class Square that defines a square
"""


class Square:
    """
    Private instance attribute: size
    """
    def __init__(self, size=0):
        """
        size: must be an integer and
        size: must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size


Square.__module__ = '2-square'
