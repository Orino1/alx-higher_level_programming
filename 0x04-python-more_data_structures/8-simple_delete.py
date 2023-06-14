#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    result = a_dictionary.get(key)
    if result == None:
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary