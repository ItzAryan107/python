# reduce is the function of functools module

from functools import reduce
list1 = [1, 2, 3, 4, 5, 6, 7, 8]

num = reduce(lambda x, y: x + y, list1)
print(num)

# if you want to operate a operator for all the elements
# like here u have to add all the elements
