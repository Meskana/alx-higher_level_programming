#!/usr/bin/python3
"""
a function that raises a type exception.
"""


def raise_exception():
    raise TypeError("This is a custom type exception")
try:
    raise_exception()
except:
    pass
