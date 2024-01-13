#!/usr/bin/python3
"""
a script that adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

def add_item_to_the_list_and_save(args):
    try:
        existing_data = load_from_json_file("add_item.json")
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    existing_data.extend(args[1:])
    save_to_json_file(existing_data,"add_item.json")
