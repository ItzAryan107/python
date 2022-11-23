l = 10  # its a global variable


def function1(n):
    """
    every function first see the variable in local area, and if didn't get
    then see in global area, and still if it won't get its throw error

    local variable will not be accessible in global area
    """
    l = 5  # it is local variable, it will not affect global variable(which have same name)
    print(l)
    print(n + " function1()")


function1("This is")
print(l)


