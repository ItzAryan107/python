import numpy as np
listForArray = [[1, 2, 3], [4, 5, 6], [7, 1, 0]]
arr = np.array(listForArray, np.int8)
print(arr)

print()

print("To get the Transpose of the array ---> ")
print(arr.T)

print()

print("To get all the items of the array --->")
for item in arr.flat:
    print(item)

print()

print("To get the number of dimension --->")
print(arr.ndim)  # in short number of axis

print()

print("To get the number of bytes consumed by the array --->")
print(arr.nbytes)

print()

print(f"it give the index of max value in an array ---> {arr.argmax()}")
# if the array is of higher order(like 2D, 3D), it will first make the
# array in 1D and then give the index of the particular value

print()

print(f"it give the index of min value in an array ---> {arr.argmin()}")

print()

print(arr.argsort())
"""
if the array is 1D than argsort() will give the indexes in the sorted value(in increasing order)
if the array is of higher order then the it will so the same thing but with particular row(every
row have there own sorted list)
"""
print()

print("index with max value according the axis --->")
print(arr.argmax(axis=1))

print()

print("sorting according the axis --->")
print(arr.argsort(axis=0))
"""
it will give the arrange the index in increasing value on the basis of index value
"""



