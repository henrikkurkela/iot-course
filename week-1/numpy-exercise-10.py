# 10. Sort following NumPy array
# - by the second row and
# - by the second column

import numpy

sampleArray = numpy.array([
    [34, 43, 73],
    [82, 22, 12],
    [53, 94, 66]
])

rowSorted = sampleArray[:, sampleArray[1, :].argsort()]
rowAndcolSorted = rowSorted[rowSorted[:, 1].argsort()]

print(rowAndcolSorted)
