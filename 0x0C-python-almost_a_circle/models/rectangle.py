#!/usr/bin/python3
"""
A the class Rectangle that inherits from Base
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value >= 0:
            raise ValueError("width must be > 0")
        self.__width = value

     @property
    def height(self):
        return self.height

    @height.setter
    def height(self,value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value >= 0:
            raise ValueError("height must be > 0")
        self.__height = value

