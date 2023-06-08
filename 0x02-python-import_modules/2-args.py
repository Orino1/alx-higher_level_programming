#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    length = len(arguments)
    i = 1
    if length == 0:
        print("0 arguments.")
    else:
        print("{} argument:".format(length))
        for arg in arguments:
            print("{}: {}".format(i, arg))
            i = i + 1