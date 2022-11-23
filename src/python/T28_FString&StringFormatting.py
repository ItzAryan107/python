# string formatting

me = "Aryan"
a = "this is %s" % me
print(a)

# dot format
a1 = 20
a = "this is {} {}"
b = a.format(me, a1)
print(b)

# OR

a1 = 20
a = "this is {1} {0}"
b = a.format(me, a1)  # in bracket, its a tuple with indexing
print(b)

# F sting
import math

a = f"this is {me} {a1} {3 * 76} {math.sin(90)}"  # mathematical operations can also be performed
print(a)
