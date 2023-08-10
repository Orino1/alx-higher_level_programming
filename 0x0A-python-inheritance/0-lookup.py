#!/usr/bin/python3
"""
an object/class attribute lookup function.
"""


def lookup(obj):
    """
    returns all attribute of an object/class.
    Args:
        obj(object/class): the object or the class.
    Return:
        all attribute in a list.
    """
    return (dir(obj))
