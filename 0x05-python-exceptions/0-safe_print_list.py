#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            num = num + my_list[i]
    except:
        pass
    print()
    return num