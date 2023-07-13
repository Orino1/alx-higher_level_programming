#!/usr/bin/python3
import json
"""
This is a module for converting an obj to a json string.
"""
def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string).

    Args:
        my_obj : a python obj

    Returns:
        json string
    """
    return json.dumps(my_obj)
