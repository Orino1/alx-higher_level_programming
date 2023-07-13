#!/usr/bin/python3
"""
This is a module is for creating an Object from a “JSON file”.
"""
import json as js

def load_from_json_file(filename):
    """
    a function that writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object) : a python object
        filename (str) : file to be writting to

    Returns:
        none
    """
    with open(filename, "r", encoding="UTF8") as file:
        return js.lead(filename, file)
