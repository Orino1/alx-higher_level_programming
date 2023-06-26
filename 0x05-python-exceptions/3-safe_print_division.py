#!/usr/bin/python3
def safe_print_division(a, b):
    num = None
    try:
        num = a / b
    except ZeroDivisionError:
        num = None
    finally:
        if num is not None:
            print("Inside result: {:.1f}".format(num))
        else:
            print("Inside result: None")
    return num



a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))