#!/usr/bin/python3
"""
a function that raises a name exception with a message.
"""

def raise_exception_msg(message=""):
    raise NameError(message)
try:
    raise_exception_msg("This is a custom name exception")
except:
    pass
