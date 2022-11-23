# lambda/anonymous function is only for convince
# its a one liner function


def add(a, b):  # this we created a function
    return a + b


# the above add function can be converted to lambda(to convert a function in one line) function


addition = lambda x, y: x + y  # this same as the above add function we wrote


a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=lambda x: x[1])  # ort function of list also accept lambda function or function
print(a)
