#!/usr/bin/python3

def multiple_returns(sentence):
    char = None
    if len(sentence) != 0:
        char = sentence[0]
    new_tuble = (len(sentence), char)
    return new_tuble