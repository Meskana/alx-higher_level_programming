#!/usr/bin/python3
""" this is a class to test bass"""
from models.base import Base
import unittest

class Test_base(unittest.TestCase):
    """
    """
    def setUp(self):
        self.a = Base()
        self.b = Base()
        self.c = Base()
        self.d = Base()
        self.e = Base()
   
    """
    testing the Equals valu.
    """
    def test_isEquals(self):
        self.assertEqual(self.a.id,1)
        self.assertEqual(self.b.id,2)
        self.assertEqual(self.c.id,3)
        self.assertEqual(self.d.id,4)
        self.assertEqual(self.e.id,5)
        
    """
    testing the integer value.
    """
    def test_assertIsInstance(self):
        self.assertIsInstance(self.a,Base)
        self.assertIsInstance(self.b,Base)
        self.assertIsInstance(self.c,Base)
        self.assertIsInstance(self.d,Base)
        self.assertIsInstance(self.e,Base)        
