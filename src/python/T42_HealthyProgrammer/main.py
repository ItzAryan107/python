import Functions as func
func.dailyStamp()
pastTime = func.getCurrentTime()

exerciseStamp = 2700
eyeStamp = 1800

exerciseLowerLimit = pastTime
eyeDropLowerLimit = pastTime
waterDrinkLowerLimit = pastTime
waterDrank = 0


def timeForExercise():
    global exerciseLowerLimit
    if func.getCurrentTime() - exerciseLowerLimit >= 2700:  # 2700
        func.musicLoop("ExerciseReminder.mp3", "ExDone")
        exerciseLowerLimit = func.getCurrentTime()


def timeForEyeDrop():
    global eyeDropLowerLimit
    if waterDrank <= 3.5:
        timeToDrinkWater()
    if func.getCurrentTime() - eyeDropLowerLimit >= 1800:  # 1800
        func.musicLoop("EyeReminder.mp3", "EyDone")
        eyeDropLowerLimit = func.getCurrentTime()


def timeToDrinkWater():
    global waterDrinkLowerLimit
    global waterDrank
    if func.getCurrentTime() - waterDrinkLowerLimit >= 1800:
        waterDrank += 0.45
        func.musicLoop("DrinkWaterReminder.mp3", "Drank")
        waterDrinkLowerLimit = func.getCurrentTime()


while True:
    if func.getCurrentTime() - pastTime >= 28800:
        break

    timeForEyeDrop()
    timeForExercise()

