#!/usr/bin/python3
"""
Class representing a base object.

Attributes:
    __nb_objects (int): Class variable to track the last assigned id.
    id (int): The identifier assigned to an instance of the Base class.
"""


class Base:
    __nb_objects = 0
    """
    nitialize a new instance of the Base class.
    Args:
        id (int, optional): The identifier for the object.
        If not provided, the next available id will be assigned.
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
