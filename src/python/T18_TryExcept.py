# try except

print("Enter num 1 ---> ", end="")
num1 = int(input())
print("Enter num 2 --->", end=" ")
num2 = int(input())
print("the sum of these two number is --->", num1 + num2)

try:
    print("Enter a ---> ", end="")
    num1 = int(input())
    print("Enter b --->", end=" ")
    num2 = int(input())

except Exception as e:
    print("Error!")

