#!/usr/bin/python3


def uppercase(str):
    for char in str:
        c = char
        if char >= 'a' and char <= 'z':
            c = chr(ord(char) - 32)
        print(c, end='')
    print("\n")
