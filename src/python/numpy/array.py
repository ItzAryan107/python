import numpy as np

myarr = np.array([1, 2, 3, 4, 98696, 6, 7, 8])
# array which contain any size of numerical
print(f"array which can contain element of any size ---> {myarr}")

myarr1 = np.array([1, 2, 3, 4, 55, 6, 7], np.int8)  # int8, int32, int64, so here memory management gets easy
# array which contain till 8bit size element, else it will give the error of datatype
print(f"myarr1 ---> {myarr1}")

print(f"element at 0 index of the array ---> {myarr1[0]}")  # to access any element from numpy array


# print(myarr1[0, 1])  this line will give error bcz, the given statement is to access the element from 2-D array

myarr1 = np.array([[1, 2, 3, 4, 5, 6, 78], [3, 4, 5, 6, 7, 8, 9]], np.int8)  # the way to  make 2D array
print(f"element at [0, 1] index of the array, when the array is treated as 2-D ---> {myarr1[1, 1]}")
print(f"to find the size of the array(number of element present in the array) ----> {myarr1.size}")

# to know the shape of array
print(f"shape of the array ---> {myarr1.shape}")
print()
print(f"myarr1 ---> \n{myarr1}")

print()

print(f"to know the which data type of array is ---> {myarr1.dtype}")

print()

myarr1[0, 1] = 100
print(f"to change any particular element in numpy array ---> \n{myarr1}")

print()
print(f"to print any particular row ---> {myarr1[0]}")

