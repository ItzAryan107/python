grocery = ["Harpic", "Vim Baar", "deodrant", "Bhindi", "Lollypop", 56]
print(grocery)

# list contains heterogeneous types of data
# its indexing starts from zero
# negative index start from the end of the list

print()

print("To access an element of List --->", grocery[0])

print()

numbers = [17, 2, 3, 4, 53, 66, 75, 8, 9]
print(numbers[2])
numbers.sort()
print("After sorting the array --->", numbers)
numbers.reverse()
print("After reversing the array --->", numbers)

print()
# slicing won't change the original list, they return a new updated list
# slicing in list is same as String

numbers.append(9090)
print("Appending element at the end of list --->",numbers)

print()

numbers.insert(2,100)
print("To insert an element at given index --->", numbers)

print()

numbers.pop()  # it will remove the last element
print("to pop an element from the list --->", numbers)

print()

numbers[1] = 546738
print("List value can be modify at any time", numbers)

'''
Mutable --> can change
Immutable --> can not change
list is a mutable DS
Tuple is immutable
'''

print()

tp = (1, 2, 3)
print("Tuple -->", tp)

print()
tp1 = (1,)  # the way to make tuple while contain 1 element

# to swap two elements
a = 45
b = 85
a, b = b, a
print(a)
print(b)


tp2 = (43, 67, "Ashmit")  # once tuple got crete it can not add any more data to it, if you want to add then u can
# only add tuple to it
tp1 = tp1.__add__(tp2)  # after applying add function tuple won't get change, means here tp1 will not get change
# ( not add the other tuple) until and unless you won't assign the modified tuple to top1
for i in tp1:
    print(i)

"""
there is no method to add elements to data, if you want to add 
you can only take the elements to the list and convert to tuple and add it to the previous tuple
"""
tupl1 = ("Aryan", "Ashmit", "Anup", "Nayan")
# let if you want to add the list numbers to it
tuple2 = tuple(numbers)
tupl1 = tupl1.__add__(tuple2)
for i in tupl1:
    print(i)

# list functions ---> https://www.geeksforgeeks.org/list-methods-in-python/
