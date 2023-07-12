#!/usr/bin/python3
"""
This is a module for printing content from a file.
"""
def write_file(filename="", text=""):
    """
    This function write to a file
    or creat it if dosnt exsist

    Args:
        filename (str): The name of the file.
        text (str): the content of the file

    Returns:
        Number of chars writting to the file
    """
    with open(filename, "w", encoding="UTF8") as my_file:
        my_file.write(text)
        my_file.seek(0)
        return len(my_file.read())
