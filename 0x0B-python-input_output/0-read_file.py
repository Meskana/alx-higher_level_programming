#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout
"""
def read_file(filename=""):
    with open(0-read_file,"r", encoding='utf-8') as file:
        content = file.read()
        print(content)