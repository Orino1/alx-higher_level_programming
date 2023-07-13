#!/usr/bin/python3
"""
This is a module for writting 
Object to a text file, using a JSON representation
"""
import json

def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object) : a python object
        filename (str) : file to be writting to

    Returns:
        none
    """
    with open(filename, "w", encoding="UTF8") as file:
        json.dump(my_obj, file)
