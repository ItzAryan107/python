from pytube import YouTube, Playlist  # playlist will get in use when you have to download all the videos of playlist
from pywhatkit import playonyt
import time
import keyboard
import pyttsx3

assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voices', voices[2].id)
assistant.setProperty('rate', 170)


def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()


def youtubeLink(link):
    link = playonyt(link)
    return link


def youtubeAudioDownloader(link):  # download only audio in video form(black screen)
    link = youtubeLink(link)
    time.sleep(10)
    keyboard.press("space bar")
    youtube1 = YouTube(link)
    speak(f"the title i found, {youtube1.title}")
    audio = youtube1.streams.filter(only_audio=True)
    # aid = list(enumerate(audio))  # this is the list which contain all type of video resolution
    # for i in aid:  # this will show you all typ e of resolution present for that vide
    #     print(i)

    audio[0].download()
    speak("Successfully Downloaded")
    keyboard.press("space bar")


if __name__ == '__main__':
    youtubeAudioDownloader("Nevada song")
