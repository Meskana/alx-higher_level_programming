#!/usr/bin/python3

"""
a class Square that defines a square
"""


class Square:
    """
    Private instance attribute: size
    """
    def __init__(self, size=0):
        if isinstance(size, int) and size >= 0:
            self.__size = size


Square.__module__ = '2-square'
