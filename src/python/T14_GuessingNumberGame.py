import random

print("Guess a number between 1 and 20(included) --->")
a = int(input("Enter a max range to play ---> "))


def guessNumber():
    guessingNumber = random.randint(1, a)

    count = 1
    while True:
        n = int(input())
        if n > guessingNumber:
            count += 1
            print("Enter small number ---> ", end="")
            continue
        elif n < guessingNumber:
            count += 1
            print("Enter large number --->", end="")
            continue
        else:
            print()
            break

    return count


listCount = []

for i in range(1, 4):
    print("Chance of Player --->", i)
    listCount.append(guessNumber())

print(listCount)
