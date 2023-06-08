#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    reslut = 0
    for arg in arguments:
            reslut = reslut + int(arg)
    print("{}".format(reslut))