#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    first_tuple = 0
    second_tuple = 0
    first_tuple_s = 0
    second_tuple_s = 0
    
    if len(tuple_a) >= 1:
        first_tuple = tuple_a[0]
        if len(tuple_a) >= 2:
            first_tuple_s = tuple_a[1]
    
    if len(tuple_b) >= 1:
        second_tuple = tuple_b[0]
        if len(tuple_b) >= 2:
            second_tuple_s = tuple_b[1]
    
    first_element = first_tuple + second_tuple
    second_element = first_tuple_s + second_tuple_s
    new_tuple = (first_element, second_element)
    return new_tuple