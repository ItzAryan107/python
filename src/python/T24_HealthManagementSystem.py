"""
Health Management System
3 clients - Aryan, Nayan and Anup
total 6 files need to make

write a function, which execute as input clint name
"""


def getDate():
    import datetime
    return datetime.datetime.now()


def createTextFiles(name):
    file = open("T24_DietFiles\\" + name + ".txt", "a")
    file.close()

    file = open("T24_ExerciseFiles\\" + name + ".txt", "a")
    file.close()


def lockDiet(name, diet):
    with open("T24_DietFiles\\" + name + ".txt", "a") as file:
        file.write(diet + " ---> " + str(getDate()) + "\n\n")


def lockExercise(name, exercise):
    with open("T24_ExerciseFiles\\" + name + ".txt", "a") as file:
        file.write(exercise + " ---> " + str(getDate()) + "\n\n")


def retrieveDiet(name):
    try:
        with open("T24_DietFiles\\" + name + ".txt", "r") as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(name.capitalize() + " YOU ARE NOT YET REGISTERED")


def retrieveExercise(name):
    try:
        with open("T24_ExerciseFiles\\" + name + ".txt", "r") as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(name.capitalize() + " YOU ARE NOT YET REGISTERED")


def lock():
    name = input("Enter Name for whom you want to Lock ---> ")
    createTextFiles(name)
    choice = input("Enter Diet or Exercise to lock that particular ---> ")

    while True:
        if choice == "Diet" or choice == "diet":
            dietName = input("Enter Your Diet ---> ")
            lockDiet(name, dietName)
            break
        elif choice == "Exercise" or choice == "exercise":
            exerciseName = input("Enter Your Exercise ---> ")
            lockExercise(name, exerciseName)
            break
        print("Error!  Enter valid Input")
        choice = input(">>>> ")


def retrieve():
    name = input("Enter name for whom you want to retrieve ---> ")
    choice = input("Enter Diet or Exercise to Retrieve that particular ---> ")

    while True:
        if choice == "Diet" or choice == "diet":
            retrieveDiet(name)
            break
        elif choice == "Exercise" or choice == "exercise":
            retrieveExercise(name)
            break
        print("Error!  Enter valid Input")
        choice = input(">>>> ")


def main():
    a = input("Enter Lock or Retrieve To do the same ---> ")
    if a == "Lock" or a == "lock":
        lock()
    elif a == "Retrieve" or a == "retrieve":
        retrieve()
    else:
        print("Error!  Enter the valid Input")
        main()


main()
