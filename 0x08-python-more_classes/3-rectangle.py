#!/usr/bin/python3
"""
    Rectangle class
"""


class Rectangle():

    """
    Initializes a new instance of the Rectangle class.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """
    Return the width of a rectangle
    """
    @property
    def width(self):
        return self.__width

    """
    Set the width of a rectangle
    Args:
        self: the object it self
        value: the new value for the width of the rectangle
    Raises:
        TypeEroor: if the value is not an Int
        VlaueError: when the value is less than 0
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
    Return the height of a rectangle
    """
    @property
    def height(self):
        return self.__height

    """
    Set the height of a rectangle
    Args:
        self: the object it self
        value: the new value for the height of the rectangle
    Raises:
        TypeEroor: if the value is not an Int
        VlaueError: when the value is less than 0
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

    """
    Returns the rectangle area.
    """
    def area(self):
        return self.width * self.height

    """
    Returns the rectangle perimeter.
    """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    """
    Return string representation of the instance
    """
    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        else:
            wd = '#' * self.width
            result = (wd + '\n') * (self.height - 1)
            result = result + wd
            return result
