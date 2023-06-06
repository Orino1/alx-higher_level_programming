#!/usr/bin/python3


def uppercase(str):
    for char in str:
        number = ord(char)
        if char >= 'a' and char <= 'z':
            number = ord(char) - 32
        print("{}".format(chr(number)), end='')
    print()
