import numpy as np
print("2. ---> numpy array creation objects(arange, ones, zeros etc)")
zerosarray = np.zeros((2, 5), np.int8)
print(zerosarray)

arangearray = np.arange(15)  # this will generate 1D numpy array, from 0 to n-1
# arangearray = np.arange(start(included), end(excluded), interval)
print(arangearray)
linspacearray = np.linspace(1, 5, 12)  # it will divide the integers between 1 to 5 in equally spaced 12 numbers
print(linspacearray)

emptyarray = np.empty((4, 6))  # it will give the array with random values in the given space
print(emptyarray)

emptylikearray = np.empty_like(linspacearray)
# if there is any old array available, it copy the size of the array and make a new array with random values
print(emptylikearray)

identityarray = np.identity(8)  # it will give 8 x 8 identity matrix
print(identityarray)

print("---------------------------------------------------------------------------")
arr = np.arange(99)  # let i want to reshape this array in 3 rows and 33 column
arr = arr.reshape(3, 33)  # the given reshape value should be according to the number of data available in the array,
# so it can form matrix
print(arr)
print()
# to make 2D array in 1D array we use ravel function
arr = arr.ravel()
print(arr)
print("---------------------------------------------------------------------------")
