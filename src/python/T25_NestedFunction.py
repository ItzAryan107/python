x = 77


def anup():
    x = 90

    def nayan():
        global x  # whenever we use global keyword, it directly try to access
        # that particular variable which is even outside the nested function even
        x = 100

    print("before calling nayan() x is --->", x)
    nayan()
    print("after calling nayan() x is --->", x)

    """
    in above, x of anup will not get change
    let if u mention a global variable in a function, but that particular variable is not present
    in the global area, then it will directly fetch the data of that particular variable where the global keyword is 
    used with it, after the calling of that that particular function in which that particular variable 
    is there
    """


anup()
print("x --->", x)

