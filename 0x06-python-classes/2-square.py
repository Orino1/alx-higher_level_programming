#!/usr/bin/python3
#!/usr/bin/python3

"""defining the class"""

class Square:
    """a square that with a private size attribute"""

    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be an integer")
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")