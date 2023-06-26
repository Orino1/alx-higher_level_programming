#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for element in my_list:
            print(element)
            num = num + 1
    except:
        return num
    return num