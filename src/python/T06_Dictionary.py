# Dictionary is nothing but key value pairs
d1 = {}  # declaration of dictionary
print(type(d1))

print()

d2 = {"Harry": "Burger", "Aryan": "Chicken", "Ashmit": "Chicken", "Anup": "Panner", "OXFord": {1: 2, 3: 4, 5: 6}}
print("printing a value using key --->", d2["Ashmit"])
print(d2["OXFord"][5])

# the value of any key in a dictionary can be dictionary, list, tuple or any data Structure
'''
keys are immutable
values are mutable
'''

print()

# adding an element in dictionary

d2["Ankit"] = "Kebab"
print("Added an element --->", d2)

print()

del d2["Harry"]
print("Deleting an element from the dictionary using key --->", d2)

print()

d3 = d2.copy()  # .copy used bcz, if we directly copied the d2 in d3...like if there be any change in d3 it will
# get reflect in d2 also, so we used the .copy function

del d3["Ankit"]
print("Deleted an element in which d2 dictionary is copied(d3) ---> ", d3)
print("d2 --->", d2)

print()

d2.update({"Lenna":"Toffee"})
print("Adding an element to d2 using .update method --->", d2)

print()

print("To print all the keys of dictionary --->", d2.keys())

print()

print("To print all the values of dictionary --->", d2.values())

print()

print("To print all key value pair using .item method --->", d2.items())
