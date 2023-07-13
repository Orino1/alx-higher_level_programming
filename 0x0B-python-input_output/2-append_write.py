#!/usr/bin/python3

"""
This is a module for printing content from a file.
"""
def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
    """
    with open(filename, "a", encoding="UTF8") as my_file:
        my_file.write(text)
