import numpy as np
listArray = [[1,2,1],[4,0,6],[8,0,1]]
arr2 = np.array(listArray,np.int8)
print("arr2 --->")
print(arr2)

arr1 = np.array([[1,2,3],[4,5,6],[7,1,0]], np.int8)
print("arr1 --->")
print(arr1)

print()

print("Summation of two matrix --->")
print(arr1 + arr2)  # with list this is not possible

print()

print("multiplication of two matrix --->")
print(arr1 * arr2)

print()

print("Square root of a matrix --->")
print(np.sqrt(arr1))

print()

print("TO get sum of all the elements of the matrix --->")
print(arr1.sum())

print()

print("To get the minimum element of the matrix --->")
print(arr1.min())  # similarly for max

print()

temp = np.where(arr1>5)  # this will return the tuple of arrays and dtype
print(temp)
print(type(temp))

print()

print("To count non-zero element in the matrix --->")
print(np.count_nonzero(arr1))

print()
print("to get the position of all nonzero element in the matrix")
print(np.nonzero(arr1))  # it give the tuple of each axis

print()

print("if you want to convert numpy array to python list --->")
print(arr1.tolist())

# https://docs.scipy.org/doc/numpy-1.6.0/reference/generated/numpy.ndarray.html

