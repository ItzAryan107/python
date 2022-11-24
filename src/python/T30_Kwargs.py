def function(a, *b, **c):  # now no matter you are giving
    # one argument or all the arguments, the function will work only on the given argument
    print(a)
    for i in b:
        print(i)
    print()
    for key, value in c.items():
        print(f"{key} is the key of {value}")


kw = {"Aryan": "The Coder", "Harry": "MilkMan", "Ashmit": "Brother Of Aryan"}
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

function("Harry", *l, **kw)
print()
function("Ashmit")
