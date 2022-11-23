# let if you want to change the value of global variable
# we use keyword global
l = 45


def function1(n):
    global l
    l = l + 56  # this will change the value of global keyword
    print(n + "Function1()")




