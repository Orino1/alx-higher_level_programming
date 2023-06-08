#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    length = len(arguments)
    i = 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        for arg in arguments:
            print("{}: {}".format(i, arg))
            i = i + 1
    else:
        print("{} arguments:".format(length))
        for arg in arguments:
            print("{}: {}".format(i, arg))
            i = i + 1