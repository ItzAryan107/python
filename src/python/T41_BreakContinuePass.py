# let if you want to iterate the iterator till 10, but you want that it wont
# print the numbers after 7
print("break statement")
for i in range(1, 11):
    if i == 8:
        break
    print(i)

print()

print("Continue")
# let the question is print the odd numbers between 1 to 11
for i in range(1,12):
    if i % 2 == 0:
        continue
    print(i)

print()
print("Pass")
# let you have to print odd number between 0 to 21
"""
pass statement is used when you want a condition 
with no statement executing in it means empty block
as python will give error if here is an empty block
we use pass statement
"""
for i in range(1, 21):
    if i % 2 == 0:
        pass
    else:
        print(i)

