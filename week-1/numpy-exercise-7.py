# 7. Add the following two NumPy arrays and modify a result array by calculating the square root of each element.

import numpy

arrayOne = numpy.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = numpy.array([[15, 33, 24], [4, 7, 1]])

array = numpy.add(arrayOne, arrayTwo)
array = numpy.sqrt(array)

print(array)
