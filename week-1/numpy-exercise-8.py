# 8. Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10

import numpy

array = numpy.array([numpy.arange(100, 199 + 1, 10)])
array = array.reshape(5, 2)

print(array)
