#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for elem in matrix:
        for i in elem:
            print("{}".format(i), end=' ' if i != elem[-1] else "")
        print()