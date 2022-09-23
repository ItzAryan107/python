import random
value = random.random()  # .random() function as default give a number between 0 and 1

print("Always ranges between 0 and 1 --->", value)

print()

value1 = random.uniform(1, 10)
print("To take a random floating point values between any range --->", value1)

print()

value2 = random.randint(1, 10)  # here 1 and 10 is inclusive
print("To take a random integer values between any range --->", value2)

print()

value3 = random.randint(0, 1)
print("To get random 0 or 1 --->", value3)

print()

'''
.choice() method takes a random value from a list of values
'''
list1 = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
greeting = random.choice(list1)
print("To take a random value from a list of values --->", greeting, "Aryan!")

print()

list2 = ['Red', 'Black', 'Green', 'Yellow']
values = random.choices(list2, k=10)  # here a list got create
print("To get a multiple random values --->", values)

print()
# We can also give the weightage to every element of a list, while using .choices() method of random
list3 = ["Anup", "Ishika", "Nayan", "Vrushti", "Varnika", "Anshika"]
values1 = random.choices(list3, weights=[9, 10, 6, 6, 3, 8], k=15)  # ishika have 10/42 probability to get select
print("To print random values according to weightage --->", values1)

print()

list4 = list(range(1, 55))  # 1 is included but 55 is not included
print(list4)
random.shuffle(list4)
print("To randomly shuffle the values of list --->", list4)

print()

hand = random.sample(list4, k=5)
print("To get n unique value --->", hand)
