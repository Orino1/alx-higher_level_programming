#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for ithem in my_list:
        if ithem == search:
            new_list.append(replace)
        else:
            new_list.append(ithem)
    return new_list