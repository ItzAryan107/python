"""
in numpy indexing of axis start from 0

1D array have ---> 1 Axis [0-axis]
2D array have ---> 2 Axis [0-axis, 1-axis]
"""
import numpy as np
listForArray = [[1, 2, 3], [4, 5, 6], [7, 1, 0]]
arr = np.array(listForArray, np.int8)
print(arr)
print("summation of data of axis=0")
print(arr.sum(axis=0))
print("summation of data of axis=1")
print(arr.sum(axis=1))


