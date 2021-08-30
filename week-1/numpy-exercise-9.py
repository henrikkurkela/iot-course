# 9. Following is the 2-D array. Print max from axis 0 and min from axis 1

import numpy

sampleArray = numpy.array([
    [34, 43, 73],
    [82, 22, 12],
    [53, 94, 66]
])

print(numpy.max(sampleArray, 0), numpy.min(sampleArray, 1))
