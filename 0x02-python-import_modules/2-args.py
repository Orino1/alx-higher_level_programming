#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv
    length = len(arguments)
    i = 0
    if length == 1:
        print("0 arguments.")
    else:
        print("{} argument:".format(length - 1))
        for arg in arguments:
            if i != 0:
                print("{}: {}".format(i, arg))
            i = i + 1