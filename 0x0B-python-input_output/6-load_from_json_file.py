#!/usr/bin/python3
"""
This is a module is for creating an Object from a “JSON file”.
"""
import json

def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”.

    Args:
        filename (str) : file to be writting to

    Returns:
        the object representation from the filename file
    """
    with open(filename, "r", encoding="UTF8") as file:
        json_data = json.load(file)
    return json_data
