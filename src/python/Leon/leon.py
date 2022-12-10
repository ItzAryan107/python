import pyautogui
import pyttsx3
from datetime import datetime as dt
import speech_recognition as sr
import wikipedia as wiki
import webbrowser as web
import os
import smtplib as smtp  # is used to send email
import pywhatkit
import time
import keyboard
import youtubeAudio.youtubeAudioDownloader as ytAudio
import youtubeVideo.youtubeVideoDownloader as ytVideo

from pygame import mixer as music
from mutagen.mp3 import MP3 as musicPlayer

assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
"""
My computer have two voices
male and female ---> 

voices at 0 index have male voice and at index 1 have female voice
as my computer have two voices only, at index of 2 voices will throw error

we can add additional voices to our computer if we want
"""
assistant.setProperty('voices', voices[2].id)
assistant.setProperty('rate', 170)


def speak(audio):
    """
    first we will write speak function, as our AI could able to speak
    as an argument it will take audio
    and after reading the audio it will pronounce it
    """
    assistant.say(audio)
    assistant.runAndWait()


def wishMe():
    """
    this function is use to wish
    """
    hour = int(dt.now().hour)  # this will give the hour from 0 to 24
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Leon Sir. Please tell How may I help You?")


def takeCommand():
    """
    it recognise microphone input from the user and returns it in string output

    Recognizer class of thr speech_recognition helps to recognise the speech by tje user
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # here pause_threshold is 1 means, let if user is speaking and
        # user take a break, then Leon should wait for the upcoming speech from the user,
        # Leon won't get operate on th half listened speech
        audio = r.listen(source)  # it will store the speech

        try:
            print("Recognizing ....")
            query = r.recognize_google(audio, language='en-in')
            # in recognize_google class i have commented the line
            # 917 and 918(hold press ctrl button and drag to recognize_google and click,
            # it will directly open that particular class with showing particular function
            # of that class)
            print(f"user said : {query}\n")
        except Exception as Error:
            # print(e)  # this will let you write Exception on the console, which we don't want
            # print("SAY THAT AGAIN PLEASE.....")
            return "NONE"
        return query.lower()


def isSongAvailable(songList, songName):
    if songList in songName:
        return True

    a = songName.split(" ")
    b = songList.split(" ")
    for i in b:
        for j in a:
            if i == j:
                return True
    return False


def playMusicFromLocal(musicName):
    musicDir = "music"
    songs = os.listdir(musicDir)  # this will give all the songs in the playlist
    for i in songs:
        if musicName in i or isSongAvailable(i[0:len(i) - 4], musicName):
            music.init()
            music.music.load(f"music\\{i}")
            speak("I found the song in your local!")
            print(f"Playing..... Song")
            music.music.play()
            return musicPlayer(f"music\\{i}").info.length
    musicName.replace("please", "")
    musicName.replace("music", "")
    musicName.replace("play", "")
    musicName.replace("song", "")
    musicName.replace("leon", "")
    musicName.replace("leone", "")
    musicName.replace(" ", "")
    speak("Launching sir")

    # pywhatkit.playonyt(musicName)
    return 0.0


"""
or "exit music" in command().lower() or "exit" in command().lower() or "close" 
in command().lower() or "close music" in command().lower()
                        
"""


def sendEmail(to, content, subject):
    """smtp module in python helps you to send email through gmail"""
    from email.mime.multipart import  MIMEMultipart
    from email.mime.text import MIMEText
    msg = MIMEMultipart()
    msg["from"] = "Leon Kennedy"
    msg["to"] = to
    msg["subject"] = subject
    msg.attach(MIMEText(content))

    server = smtp.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    with open("emailPassword.rxt", "r") as file:
        password = file.readline()
    server.login('leon25101007@gmail.com', password)
    server.send_message(msg)
    server.close()


def searchingAtGoogle(topicToSearch):
    pywhatkit.search(topicToSearch)


def searchOnYoutube(query):
    pywhatkit.playonyt(query)


def whatsapp():
    speak("To whom you want to write message")
    name = takeCommand()
    speak("Tell me the message to send")
    msg = takeCommand()

    if "palak" in name:
        sendMessage("+919838135837", msg)
    elif "denash" in name or "dinesh" in name:
        sendMessage("+918303759462", msg)
    elif "chote" in name or "ashmit" in name:
        sendMessage("+919335345044", msg)


def sendMessage(number, msg):
    pywhatkit.sendwhatmsg(number, msg, dt.now().hour, dt.now().minute + 2, 20)


def screenShot():
    speak("Ok sir, What should I name the file")
    ssName = takeCommand()
    ssName = ssName.replace(" ", "")
    ssName = ssName + ".png"
    dir = "screenShot\\" + ssName
    speak("open the particular page on screen of which you want to take screenshot")
    time.sleep(3)
    ss = pyautogui.screenshot()
    ss.save(dir)
    speak("screenshot has been captured")


def toOpenOnChrome(query):
    speak("wait a second sir")

    if "facebook" in query:
        web.open("https://www.facebook.com/")

    elif "instagram" in query:
        web.open("https://www.instagram.com/")

    elif "google" in query:
        web.open("https://www.google.co.in/")


def toOpenApplication(query):
    # let if you want to open VS-code from your local
    if "code" in query:
        os.startfile("C:\\Users\\dhara\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif "spotify" in query:
        try:
            os.startfile("C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.199.878.0_x86__zpdnekdrzrea0"
                     "\\spotify.exe")
        except Exception as error:
            web.open("https://open.spotify.com/")

    elif "intellij" in query:
        os.startfile("C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.3.1\\bin\\idea64.exe")

    elif "chrome" in query:
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")


def toCloseApplication(query):
    speak("Ok sir, wait a second please")

    # for any application, which is app in your computer
    if "spotify" in query:
        os.system("TASKKILL /f /im spotify.exe")

    elif "chrome" in query:
        os.system("TASKKILL /f /im chrome.exe")

    elif "intellij" in query:
        os.system("TASKKILL /f /im idea64.exe")

    elif "code" in query:
        os.system("TASKKILL /f /im Code.exe")

    # to close a particular tab on website <--- yet has to be done


def youtubeAutomation(query):
    if "pause" in query or "stop" in query:
        keyboard.press("space bar")

    elif "restart" in query or "resume" in query or ("play" in query and "beginning" in query):
        keyboard.press("0")

    elif "play" in query:
        keyboard.press("space bar")

    elif "mute" in query:
        keyboard.press("m")

    elif "skip" in query or "10 seconds" in query:
        keyboard.press("l")

    elif "back" in query:
        keyboard.press("j")

    elif "full screen" in query:
        keyboard.press("f")

    elif "film mode" in query:
        keyboard.press("t")


def unlockMe():
    speak("unlock me please")
    password = takeCommand()
    with open("unlockPassword.txt", "r") as file:
        if file.readline().lower() in password:
            wishMe()
            taskExecutor()
        else:
            content = "Hello Aryan,\n" \
                      "This is Leon, Your Personal Assistant\n" \
                      "Some unknown is trying to Access me!\n" \
                      "\n\n" \
                      "Leon Kennedy\nYour Personal Assistant"
            sendEmail(to="aryangithub2017@gmail.com", content=content, subject="Warning\u26A0\uFE0F")
            speak("Access Denied!")


def taskExecutor():
    """Logic to execute task based on query"""
    print()
    songSize = 0.0
    startingTime = 0.0
    while True:
        print("Aryan")
        query = takeCommand()

        if "hello" in query:
            speak("Hello Sir, I am Leon. Your Personal Assistant!"
                  "How may I help you?")

        elif "how are you" in query:
            speak("I am Fine Sir")
            speak("what about you?")

        elif songSize > 0.0:
            if time.time() - startingTime > songSize or "stop" in query:
                music.music.stop()

        elif "whatsapp message" in query:
            whatsapp()

        elif "download" in query and "youtube" in query and "video" in query:
            query = query.replace("download", "")
            query = query.replace("video", "")
            query = query.replace("youtube", "")
            ytVideo.youtubeVideoDownloader(query)

        elif "download" in query and "youtube" in query and "audio" in query:
            query = query.replace("download", "")
            query = query.replace("audio", "")
            query = query.replace("youtube", "")
            ytAudio.youtubeAudioDownloader(query)

        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            result = wiki.summary(query, sentences=2)  # it will return 2 sentences from wikipedia
            # you can also change the number of sentences you want
            speak("According To Wikipedia")
            print(result)
            speak(result)
            speak("Task Completed.")

        # sending email
        elif "send email" in query or "type email" in query or " write an email" in query or "send an email" in query \
                or "type an email" in query or "write email" in query or "write a email" in query or "type a email" in query:
            speak("Tell me the receiver email")
            receiverEmail = takeCommand()
            receiverEmail = receiverEmail.replace(" ", "")
            print(receiverEmail)
            try:
                speak("What subject should I give to the email!")
                subject = takeCommand()
                speak("What should I write")
                content = takeCommand()
                sendEmail(f"{receiverEmail}@gmail.com", content, subject)
                # speak("login successful")
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry Sir, I couldn't able to send the mail, please try again or try after later")

        elif "screenshot" in query or "screen shot" in query:
            screenShot()

        elif "the time" in query:
            strTime = dt.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif "website" in query or "launch" in query:
            query = query.replace("open", "")
            query.replace("website", "")
            query.replace("leon", "")
            query.replace("launch", "")
            if "leon" in query:
                query = query.replace("leon", "")
            elif "leone" in query:
                query = query.replace("leone", "")

            query = "https://www." + query + ".com"
            speak("Ok Sir, Launching!")
            web.open(query)
            speak("Launched!")

        elif ("pause" in query or "stop" in query or "restart" in query or "resume" in query or
              ("play" in query and "beginning" in query) or "skip" in query or "10 seconds" in query or
              "mute" in query or "back" in query or "full screen" in query or "film mode" in query) and "youtube" in query:
            youtubeAutomation(query)

        elif "youtube" in query:
            query = query.replace("search", "")
            query = query.replace("youtube", "")
            query = query.replace("please", "")
            query = query.replace("on", "")
            query = query.replace("leon", "")
            query = query.replace("leone", "")
            speak("Ok sir, This is what I found for you")
            searchOnYoutube(query)

        elif ("song" in query or "music" in query) and "play" in query:  # sentence should be in the form ".....play
            # music {music name}...."
            query = query.replace("music", "")
            query = query.replace("song", "")
            query = query.replace("play", "")
            songSize = playMusicFromLocal(query)
            startingTime = time.time()
            print(startingTime)
            print(songSize)
            # songs = os.listdir("music")
            # os.startfile(os.path.join("music", songs[0]))

        elif ('take me to google' in query) or ('open google' in query):
            toOpenOnChrome(query)

        elif "instagram" in query:
            toOpenOnChrome(query)

        elif "facebook" in query:
            toOpenOnChrome(query)

        elif "search" in query or "search on google" in query or "search about" in query:
            speak("What would you like to search")
            searchingAtGoogle(takeCommand())

        elif "open chrome" in query or "chrome" in query:
            toOpenOnChrome(query)

        elif "app" in query or "open app" in query or "open" in query:  # if query contain open in it, means leon
            # will open the local available application present, like intellij
            toOpenApplication(query)

        elif "close" in query:
            toCloseApplication(query)

        elif "thank you" in query or "thankyou" in query or "exit" in query or "you need a break" in query or "bye" in query:
            speak("ok sir, you can call me any time!")
            if "bye" in query:
                speak("bye sir, have a nice day")
            exit()

        # speak("I have Not that functionality to do yet")


if __name__ == '__main__':
    unlockMe()
