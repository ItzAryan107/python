"""
In array all the elements should of same data type

one advantage is here, it dynamic
means we can change the size of array at any time according our requirement
"""

"""
Different Types to import a module ---
import array
import array as arr
from array import (give function name) or * if u want to apply all the functions of array(from array import *)
"""

from array import *

"""
Every data type have a unique code
'b' --- signed char ---- int --- 1
'B' --- unsigned char --- int --- 1
'u' --- Py_UNICODE --- Unicode character --- 2
'h' --- signed short --- int --- 2
'H' --- unsigned short --- int ---2 
'i' --- signed int --- int --- 2
'I' --- unsigned int --- int ---2 
'l' --- signed long --- int --- 4
'L' --- unsigned long --- int --- 4 
'f' --- float --- float --- 4
'd' --- double --- float --- 8 

unsigned means ---> a variable can contain number in negative and positive (0 to n)
signed means ---> a variable can only contain positive numbers
"""

vals = array("i", [5, 9, 8, 4, 2, -2])
print(vals)  # it will print the whole line what is written in vals

print()

# to print just the values, printing values one by one
for i in vals:
    print(i)

print()

# to get the size of array, use function buffered_info
"""
buffered_info will return a tuple with two things
first one is Address
second one is size

so to get just the size, u need type buffered_info[1]
"""
print(vals.buffer_info())

print()

print("Size --->",vals.buffer_info()[1])

print()

# to know the type --- () it will return the code of the datatype used
print(vals.typecode)

print()

# to add a value
vals.append(89)
print(vals)

print()

# to remove a value
vals.remove(5)  # u can only remove the element which is present in the array, else it will show error
print(vals)

print()

# if you want to reverse the the array
vals.reverse()  # this will modify the array
print(vals)

print()

# let if you want to print just starting 3 index of the array
for i in range(3):  # 0 index is included but index 3 is excluded
    print(vals[i])  # a proper indentation should be there

print()

# another way to find the length ods array is:
print(len(vals))

# let if you want to copy the array to another array
newArr = array(vals.typecode, (i for i in vals))
print("newArr --->", newArr)

print()

# if you want to assign the square of every element to a new array
newArr2 = array(newArr.typecode, (i*i for i in newArr))
print("newArr2 --->", newArr2)

print()

newArr3 = array(newArr2.typecode, [])
i = 0
while i < len(newArr2):
    newArr3.append(newArr2[i])
    i += 1
print("newArr3 --->", newArr3)
