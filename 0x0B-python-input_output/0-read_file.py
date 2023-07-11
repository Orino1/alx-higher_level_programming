#!/usr/bin/python3

"""
This is a module for printing content from a file.
"""

def read_file(filename=""):
    """
    This function prints the content of a file.

    Args:
        filename (str): The name of the file.

    Returns:
        None
    """

    with open(filename, "r", encoding="UTF8") as my_file:
        print(my_file.read)