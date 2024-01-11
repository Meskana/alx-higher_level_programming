#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8) and returns the number of characters written

Parameters:
    filename (str): The name of the file to be written.
    text (str): The string to be written to the file.

Returns:
    int: The number of characters written to the file.
"""
def write_file(filename="", text=""):


    """
    Writes the given text to the specified file in UTF-8 encoding.

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """

    with open("filename", 'w', encoding='UTF8') as file:
        content = file.write(text)
        return content
