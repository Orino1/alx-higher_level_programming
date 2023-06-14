#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    key = ''
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        if v > score:
            score = v
            key = k
    return key