#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    check = 0
    for x in range(list_length):
        try:
            new_list.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            print("wrong type")
            check = 1
        except ZeroDivisionError:
            print("division by 0")
            check = 1
        except IndexError:
            print("out of range")
            check = 1
        finally:
            if check == 1:
                new_list.append(0)
                check = 0
    return new_list