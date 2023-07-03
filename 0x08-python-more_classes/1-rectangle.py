#!/usr/bin/python3
"""
    declaring an empty class
"""
class Rectangle():
    def __init__(self, width=0, height=0):
    """
    Initializes a new instance of the Rectangle class.

    Args:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.
    """
    self.__width = width
    self.__height = height

def width(self):
    """
    Get the width of the rectangle.

    Returns:
        int: The width of the rectangle.
    """
    return self.__width

def width(self, value):
    """
    Set the width of the rectangle.

    Args:
        value (int): The new width value.

    Raises:
        ValueError: If the width value is less than 0.
        TypeError: If the width value is not an integer.
    """
    if isinstance(value, int):
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    else:
        raise TypeError("width must be an integer")

def height(self):
    """
    Get the height of the rectangle.

    Returns:
        int: The height of the rectangle.
    """
    return self.__height

def height(self, value):
    """
    Set the height of the rectangle.

    Args:
        value (int): The new height value.

    Raises:
        ValueError: If the height value is less than 0.
        TypeError: If the height value is not an integer.
    """
    if isinstance(value, int):
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    else:
        raise TypeError("height must be an integer")