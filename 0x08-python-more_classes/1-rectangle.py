#!/usr/bin/python3
"""
    Represents a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""
class Rectangle:
    """
    Initializes a new instance of the Rectangle class.

    Args:
    width (int): The width of the rectangle. Defaults to 0.
    height (int): The height of the rectangle. Defaults to 0.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """
    Get the width of the rectangle.

    Returns:
        int: The width of the rectangle.
    """
    @property
    def width(self):
        return self.__width
    """
    Set the width of the rectangle.

    Args:
        value (int): The new width value.

    Raises:
    ValueError: If the width value is less than 0.
    TypeError: If the width value is not an integer.
    """
    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")
    """
    Get the height of the rectangle.

    Returns:
    int: The height of the rectangle.
    """
    @property
    def height(self):
        return self.__height
    """
    Set the height of the rectangle.

    Args:
        value (int): The new height value.

    Raises:
        ValueError: If the height value is less than 0.
        TypeError: If the height value is not an integer.
    """
    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
