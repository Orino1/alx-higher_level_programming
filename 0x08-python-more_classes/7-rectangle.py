#!/usr/bin/python3
"""
    Represents a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""
class Rectangle:
    """
    number of instances created
    """
    number_of_instances = 0
    """
    Used as symbol for string representation
    """
    print_symbol = "#"
    """
    Initializes a new instance of the Rectangle class.

    Args:
    width (int): The width of the rectangle. Defaults to 0.
    height (int): The height of the rectangle. Defaults to 0.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
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
    """
    Calculates the area of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    def area(self):
        return (self.height * self.width)
    """
    Calculates the perimeter of the rectangle.

    Returns:
        int: The perimeter of the rectangle.
    """
    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)
    """
    Returns a string representation of the rectangle.

    Returns:
        str: A string representing the rectangle shape.
    """
    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        multiply_widt = ( str(self.print_symbol) * self.width ) + "\n"
        multiply_higt = multiply_widt * (self.height - 1)
        rectangle_shape = multiply_higt + ( str(self.print_symbol) * self.width )
        return rectangle_shape
    """
    Returns a string representation of the Rectangle object.

    Returns:
        str: A string representing the Rectangle object in the
        format "Rectangle(width, height)".
    """
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    """
    Performs cleanup tasks before the object is destroyed.

    This method is automatically called when the object is about
    to be garbage-collected.
    It can be used to release resources, close files, or perform
    any necessary finalization tasks.

    Returns:
        None
    """
    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")