def function_name_print(a, b, c, d):
    print(a, b, c, d)


function_name_print("Aryan", "Nayan", "Anup", "Chetan")


# like if we wont to add more name, in real life it is like where people are in huge
# then it is not possible to add that many number of variable

print()
print("*args ---> ")


# here the if you have a normal argument also with args
# then keep normal argument first then keep *args
def funArgs(*args):  # here argument get in as a tuple
    """it is not necessary to write *args we can also write *aryan
     the necessary condition is * should be present"""
    for i in args:
        print(i)


l = ["Aryan", "Nayan", "Anup", "Chetan"]
funArgs(*l)
