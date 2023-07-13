#!/usr/bin/python3

"""
This is a module for printing content from a file.
"""
def append_write(filename="", text=""):
    """
    This function append to a file
    or creat it if dosnt exsist

    Args:
        filename (str): The name of the file.
        text (str): the content of the file

    Returns:
        none
    """
    with open(filename, "a+", encoding="UTF8") as my_file:
        my_file.write(text)
