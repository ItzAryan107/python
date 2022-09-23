var1 = int(input("Enter a number ---> "))
var2 = int(input("Enter another number ---> "))

if var1 > var2:
    print("Greater --->", var1)
elif var2 == var1:
    print("Both integers are Equal")
else:
    print("Greater --->", var2)

print()

list1 = [1, 2, 3, 4, 5, 6, 7]
if 5 in list1:
    print("Yes it is in the list")

if 60 not in list1:  # if the given condition gets true, then it move inside if
    print("No its not in the list")

print()

age = int(input("Enter your age ---> "))
if age < 18:
    print("You are not eligible for DL")
elif age>18:
    print("You are eligible for DL")
else:
    print("Come To Office and take DL")
