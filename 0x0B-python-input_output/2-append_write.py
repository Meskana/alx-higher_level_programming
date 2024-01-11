#!/usr/bin/python3

"""
A function that appends a string to a text file
and returns the number of characters appended.

Parameters:
    filename (str): The name of the file to which the text will be appended.
    text (str): The string to be appended to the file.
Returns:
    int: The number of characters appended to the file.
"""


def append_write(filename="", text=""):

    """
    Appends the given text to the specified file.
    Args:
    filename (str): The name of the file to which the
        text will be appended.
        text (str): The string to be appended to the file.
    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='UTF8') as file:
        content = file.write(text)
        return content
