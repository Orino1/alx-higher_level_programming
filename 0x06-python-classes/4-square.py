#!/usr/bin/python3
"""A module that contain a square class """


class Square:

    """Square class: with init method and a public method area
    and the following attributes:
        __size : size of the square (private)"""

    def __init__(self, size=0):
        """inistialazation of square object with an optional private attribute
        size, while checking if size is int/and if greater than 0,and raising
        errors accordinlly"""
        self.size = size

    def area(self):
        """area is a public method
        args: None (other than the object it self)
            return value: the size attribute of the instance square"""
        return self.__size * self.__size

    @property
    def size(self):
        """size is a property
            return value: size attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """"size here is a methode that act as a setter for the property
        size"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
