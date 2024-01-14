#!/usr/bin/python3
"""
class: this is a Base class
"""
import unittest


class Base(unittest.TestCase):
    __nb_objects = 0
    """
    Parameters:
    - id (int): The name of the.
    """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
