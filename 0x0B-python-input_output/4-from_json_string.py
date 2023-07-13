#!/usr/bin/python3
#!/usr/bin/python3
"""
This is a module for converting a json string to an object.
"""
import json

def from_json_string(my_str):
    """
    Function that returns the obj representation of a json string.

    Args:
        my_str (str) : a json string

    Returns:
        python object
    """
    return json.loads(my_str)
