#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda new: list(map(lambda j: j ** 2, new)), matrix))
