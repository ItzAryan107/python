from datetime import datetime as dt
import time as t
from pygame import mixer as reminder


def getData():
    return dt.now().date()


def getCurrentTime():
    return t.time()


def dailyStamp():
    with open("MyLogs.txt", "a") as file:
        file.write(f"\n{getData()}\n\n")


def myLogs(logs):
    with open("MyLogs.txt", "a") as file:
        file.write(f"{logs} --at--> {dt.now().time()}\n")


def musicLoop(music, stopper):
    reminder.init()
    reminder.music.load(music)
    reminder.music.play()
    while True:
        a = input("---> ")
        if a == stopper:
            myLogs(stopper)
            reminder.music.stop()
            return
        print("Error! - Enter valid Input")
