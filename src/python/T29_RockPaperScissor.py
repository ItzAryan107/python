"""
1 = rock
2 = paper
3 = scissor
"""
computer = 0
player = 0


def rock(choice):
    global computer
    global player
    if choice == "Scissor" or choice == "Scissor":
        computer += 1
    elif choice == "Paper" or choice == "Paper":
        player += 1


def paper(choice):
    global computer
    global player
    if choice == "Rock" or choice == "rock":
        computer += 1
    elif choice == "Scissor" or choice == "scissor":
        player += 1


def scissor(choice):
    global computer
    global player
    if choice == "Paper" or choice == "paper":
        computer += 1
    elif choice == "Rock" or choice == "rock":
        player += 1


def game(n):
    if n == 0:
        return
    import random
    value = random.randint(1, 3)

    choice = input("Play your Chance ---> ")
    if choice != "Rock" and choice != "rock" and choice != "Paper" \
            and choice != "paper" and choice != "Scissor" and choice != "scissor":
        print()
        print("ERROR! _ ENTER THE VALID INPUT")
        return game(n)
    print()
    if value == 1:
        rock(choice)
    elif value == 2:
        paper(choice)
    else:
        scissor(choice)
    n -= 1
    return game(n)


print("\t\tROCK PAPER SCISSOR ")
game(2)
if computer > player:
    print("YOU LOST THE GAME")
elif player > computer:
    print("HURRAY! -- YOU WON THE GAME")
else:
    print("YOU PLAYED DRAW")

