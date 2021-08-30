# 2. Write a NumPy program to test whether none of the elements of a given array is zero.

import numpy

nozeros = True
array = numpy.array([0, 1, 2, 3, 4])

for x in numpy.nditer(array):
    if x == 0:
        nozeros = False

if nozeros == True:
    print('There are no zeros in array ', array)
else:
    print('There are zeros in array ', array)
