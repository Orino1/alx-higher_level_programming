#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for list_inmatrix in matrix:
        new_list_inmatrix = list(map(lambda x : x * x,list_inmatrix))
        new_matrix.append(new_list_inmatrix)
    return new_matrix