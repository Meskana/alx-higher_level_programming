#!/usr/bin/python3
"""
a class Square that defines a square
"""


class Square:
    """
    privert instant attribut size
    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """this is a gtter """
    @property
    def size(self):
        return self.__size

    """this is a setter with value"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ area of a square"""
    def area(self):
        return self.__size ** 2

    """ print the square with #"""
    def my_print(self):
        for i in range(self.size):
            print("#" * self.size)


Square.__module__ = '3-square'
