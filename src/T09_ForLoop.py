list1 = ["Harry", "Larry", "Carry", "Marie"]
for i in list1:
    print(i)

print()

list2 = [["Aryan", "Nayan", "Anup", "Sameer", "Shivansh", "Chetan"], ["Ishika", "Vurshti", "Subhangi", "Varnika", "Anshika"],
         ["Aryan", "Anshika", "Vrushti", "Nayan", "Subhangi"], ["Vrushti", "Varnika", "Aryan", "Subhangi", "Chetan"]]

for i in list2:
    for j in i:
        print(j, end=" ")
    print()

print()

list3 = [["Harry", 1], ["Larry", 2], ["Carry", 3], ["Marie", 250]]
for i, j in list3:
    print(i, j)

print()

# List3 can be converted into dictionary, bcz the data arranged in list3 is same as dictionary
dict1 = dict(list3)
for item in dict1:
    print(item)

print()

print("To print numbers from 1 to n")
n = int(input("Enter number ---> "))
print("[", end="")
for i in range(1, n+1):
    if i == n:
        print(i, end="")
        break
    print(i, end=" ")
print("]")

print()

print("To print number from n to 1")
print("[", end="")
for i in range(n, 0, -1):
    if i == 1:
        print(i, end="")
        break
    print(i, end=" ")
print("]")

print()

list4 = ["Aryan", int, float, 1, 2, 4, 5, 7]
for i in list4:
    if str(i).isnumeric() and i > 6:  # .isnumeric is a function of string class
        print(i)

