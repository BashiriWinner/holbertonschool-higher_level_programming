#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_array = []
    for arr in matrix:
        new_arr.append(list(map(lambda x: pow(x, 2), arr)))
        return new_arr
