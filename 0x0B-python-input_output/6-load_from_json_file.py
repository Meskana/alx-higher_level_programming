#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file
"""

import json
from io import StringIO

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file.

    Returns:
    - dict, list, or set: The Python object created from the JSON data.

    Raises:
    - FileNotFoundError: If the specified file does not exist.
    - json.JSONDecodeError: If the file does not contain valid JSON data.
    """
    with open(filename, 'r', encoding="UTF-8") as file:
       data =  json.load(file)
    return data
