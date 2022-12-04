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


def myLogs(logs, statement):
    with open("MyLogs.txt", "a") as file:
        file.write(f"{statement}\n{logs} --at--> {dt.now().time()}\n")


def musicLoop(music, stopper, statement):
    reminder.init()
    reminder.music.load(music)
    reminder.music.play()
    while True:
        a = input("---> ")
        if a == stopper:
            myLogs(stopper, statement)
            reminder.music.stop()
            return
        print("Error! - Enter valid Input")
