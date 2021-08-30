# 1. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

import numpy

integer = 10
matrix = numpy.empty([3, 4])

with numpy.nditer(matrix, op_flags=['readwrite']) as it:
    for x in it:
        x[...] = integer
        integer = integer + 1

print(matrix)
