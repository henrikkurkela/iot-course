# 3. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.

import numpy

array = numpy.array([1, 7, 13, 105])

print('Array memory size: ', array.nbytes, ' bytes')
