import array as arr
# to make an empty array
arr1 = arr.array('i', [])

n = int(input("Enter Number of values you want to add in the array ----> "))

i = 0
while i < n:
    arr1.append(int(input(f"Enter value for {i} index ---> ")))
    i += 1

print(arr1)

print()

# if you want to print the index of a given value
val = int(input("Enter value to search ---> "))
print(f"Index of {val} is --->", arr1.index(val))

# if interpreter wont the the search value in the array it will throw error, when the index function is used
