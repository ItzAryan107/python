a = 8
b = 9


# built in function, to define custom function use def keyword
# sum function
c = sum((a, b))  # it showing warning bcz sum function accept list or tuple, means the given parameter should be
# iterable
print(c)


def function():
    print("Hello you are in function")


print(function())  # it will also print the none at the end, bcz the given function is not returning any value

# docstring ---> if the first line of the function have a commented line, then that line is called docstring


def function1(a, b):
    """This is the function which will calculate the sum of two function,
    this function won't run for 3 or more element"""
    return a+b


print(function1.__doc__)
