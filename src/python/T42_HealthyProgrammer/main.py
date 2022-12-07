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
    if func.getCurrentTime() - exerciseLowerLimit >= 2700:  # try for 45 seconds
        func.musicLoop("ExerciseReminder.mp3", "ExDone", "\t -------This is the Time to exercise your body ----->")
        exerciseLowerLimit = func.getCurrentTime()


def timeForEyeDrop():
    global eyeDropLowerLimit
    if waterDrank <= 3.5:
        timeToDrinkWater()
    if func.getCurrentTime() - eyeDropLowerLimit >= 1800:  # try for 30 seconds
        func.musicLoop("EyeReminder.mp3", "EyDone", "\t -------This is the Time to give rest to your eyes ----->")
        eyeDropLowerLimit = func.getCurrentTime()


def timeToDrinkWater():
    global waterDrinkLowerLimit
    global waterDrank
    if func.getCurrentTime() - waterDrinkLowerLimit >= 1800:  # try for 30 seconds
        waterDrank += 0.45
        func.musicLoop("test music.mp3", "Drank",
                       "\t -------This is the Time to Drink Water At least OF 0.45 liter ----->")
        waterDrinkLowerLimit = func.getCurrentTime()


if __name__ == '__main__':
    while True:
        if func.getCurrentTime() - pastTime >= 28800:  # try For 300 seconds
            break

        timeForEyeDrop()
        timeForExercise()
