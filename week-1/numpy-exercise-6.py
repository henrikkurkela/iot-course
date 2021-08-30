# 6. Write a NumPy program (using numpy) to sum of all the multiples of 3 or 5 below 100.

import numpy

sum = 0
array = numpy.arange(1, 99 + 1)

for x in numpy.nditer(array):
    if x % 3 == 0 or x % 5 == 0:
        sum = sum + x[...]

print('Sum of all integers that are multiples of 3 or 5 in range 1-99: ', sum)
