#!/usr/bin/python3
""" this is a class to test bass"""
from models.rectangle import Rectangle
import unittest

class Test_rectangle(unittest.TestCase):
    """
    this ia a test cases to test all the rectangle
    """
    def test_isEquals(self):
        """
        To check if all agument is in normal position
        """
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width,1)
        self.assertEqual(rect.height,2)
        self.assertEqual(rect.x,3)
        self.assertEqual(rect.y,4)
        self.assertEqual(rect.id,5)
        
    def test_setValueWidth(self):
        """
        use all possible case to test widt value
        """
        rect = Rectangle(1, 2, 3, 4, 5)

        with self.assertRaises(ValueError):
            rect.width = -1

        with self.assertRaises(TypeError):
            rect.width = "width"

    def test_setValueHeight(self):
       """
       use all possible case to test height value
       """
       rect = Rectangle(1, 2, 3, 4, 5)

       with self.assertRaises(ValueError):
           rect.height = -2

       with self.assertRaises(TypeError):
           rect.height = "width"

    def test_setValueX(self):
       """
       use all possible case to test x value
       """
       rect = Rectangle(1, 2, 3, 4, 5)

       with self.assertRaises(ValueError):
           rect.x = -3

       with self.assertRaises(TypeError):
           rect.x = "x"

    def test_setValueY(self):
       """
       use all possible case to test y value
       """
       rect = Rectangle(1, 2, 3, 4, 5)

       with self.assertRaises(ValueError):
           rect.y = -4

       with self.assertRaises(TypeError):
           rect.y = "y"
