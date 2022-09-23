var1 = "Hello World"
var2 = 4
var3 = 65.9
print(var1)
print("to get type of a variable --->", type(var2))

print()

print("while Adding two string it get concatenate")
var4 = "Aryan"
var5 = " Prajapati"
print(var4+var5)

print()

print("To print a line multiple times(without using for loop)")
print(5*"Aryan\n")

print("Type casting")
var6 = 76
print(var6, "Type --->", type(var6))
print(str(var6), "Type --->", type(str(var6)))

'''
input function as default takes string
if we want to take any number, then it eed to type cast
'''

a = int(input("Enter a number ---> "))  # it will take a number as input
a = input("Enter a String ---> ")
print(a)

# python is a interpreter, which interpret the code line by line
