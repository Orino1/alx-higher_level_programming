#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = None
    for x in range(list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
            new_list.append(result)
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(0)
    return new_list