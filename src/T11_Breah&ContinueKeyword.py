print("To print number from 0 to n using while loop and break")
n = int(input("Enter number ---> "))
i = 0
while True:
    print(i)
    if i == n:
        break
    i += 1
i = 0
print()

print("To print Even Number using while loop and continue")

while True:
    if i >= n:
        break
    i += 1
    if i % 2 != 0:
        continue
    print(i)

print()

print("Taking input from the user until and unless the input won't become greater than 100")

while True:
    n = int(input("Enter Number ---> "))
    if n > 100:
        break
