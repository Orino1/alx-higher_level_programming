#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dec = {}
    for k, v in a_dictionary.items():
        new_dec[k] = v * 2
    return new_dec