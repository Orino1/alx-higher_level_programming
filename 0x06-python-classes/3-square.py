#!/usr/bin/python3
"""defining the class"""

class Square:
    """a square that with a private size attribute"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """method: def area(self): that returns the current square area"""

    def area(self):
        return self.__size * self.__size