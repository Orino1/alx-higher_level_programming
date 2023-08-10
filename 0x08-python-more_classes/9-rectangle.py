#!/usr/bin/python3
"""
    Rectangle class
"""


class Rectangle():

    """
    symbol for string representation
    """
    print_symbol = '#'

    """
    number of instances created
    """
    number_of_instances = 0

    """
    Initializes a new instance of the Rectangle class.
    Args:
        width: width of the instance.
        height: height of the instance.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            # TODO: i dont knwo why Rectangle.print_symbol
            # dosnt return the whole list byt only the first char!!!
            wd = str(self.print_symbol) * self.width
            result = (wd + '\n') * (self.height - 1)
            result = result + wd
            return result

    """
    Return a string representation that lest us recreat the object
    from the string via eval() function
    """
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    """
    priting a message when ever the garbeg collector delet my object
    """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """
    returns the biggest rectangle(object) based on the area
    Args:
        rect_1: instance of the class Rectangle
        rect_2: instance of the class Rectangle
    Raises:
        TypeError: if rect_1/rect2 sint a Rectangle instance
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    """
    Returns a new Rectangle instance with width == height == size
    Args:
        cls: class literal
        size: represent the width and height
    """
    @staticmethod
    def square(cls, size=0):
        new_instance = cls(size, size)
        return new_instance
