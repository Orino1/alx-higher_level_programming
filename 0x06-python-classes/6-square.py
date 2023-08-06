#!/usr/bin/python3
"""A module that contain a square class """


class Square:

    """Square class: with init method and a public method area
    and the following attributes:
        __size : size of the square (private)"""

    def __init__(self, size=0, position=(0, 0)):
        """inistialazation of square object with an optional private attribute
        size, while checking if size is int/and if greater than 0,and raising
        errors accordinlly"""
        self.size = size
        self.position = position

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

    def my_print(self):
        """my_print is a methode that prints in stdout the square with the
        character #.
        if size is equal to 0, print an empty line"""
        if self.size != 0:
            if self.position[1] > 0:
                for x in range(self.position[1]):
                    print()
            for i in range(self.size):
                for y in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end='')
                print()
        else:
            print()

    @property
    def position(self):
        """position is a property
            return value: position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """"position here is a methode that act as a setter for the property
        position"""
        if isinstance(value, tuple):
            if (len(value) == 2
                    and (isinstance(value[0], int) and value[0] >= 0)
                    and (isinstance(value[1], int) and value[1] >= 0)):
                self.__position = value
            else:
                raise TypeError(
                    "position must be a tuple of 2 positive integers"
                )
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
