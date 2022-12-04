numbers = ["3", "34", "64"]

# here numbers are there but in String type
# let if you want to add a number to a particular element, then it will give error as the element is String
# and you are adding integer

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers)


print()

# the above thing can be done in one line, using map unction
numbers1 = ["1", "2", "3", "4", "5"]
numbers1 = list(map(int, numbers1))  # together with map we use list or tuple if you want to return the same
print(numbers1)

print()

# let if you want to do the square of every element


def sq(a):
    return a*a


numbers1 = list(map(sq, numbers1))  # we can also use the lambda function, list(map(lambda x: x*x, numbers1))
print(numbers1)


def cube(a):
    return a*a*a


func = [sq, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)

