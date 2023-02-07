import numpy as np
print("Creation of numpy array using different way ---> ")
print("1. ---> conversion from other python structures(lists, tuples)")
l1 = [1,2,3,4,54,6,7]
l2 = [4,5,7,8,9,56,6]
arrList = np.array([l1, l2], np.int32)
print(arrList)
