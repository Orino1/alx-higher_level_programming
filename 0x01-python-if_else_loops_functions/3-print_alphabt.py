#!/usr/bin/python3

for char in 'abcdefghijklmnopqrstuvwxyz':
    if char == "q" or char == "e":
        continue
    else:
        print("{}".format(char), end='')
