#!/usr/bin/python3

def max_integer(my_list=[]):
    big = None
    if len(my_list) != 0:
        big = my_list[0]
        for i in my_list[1:]:
            if i > big:
                big = i
    return big