#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = set(set_1)
    b = set(set_2)
    new_set = a ^ b
    return new_set