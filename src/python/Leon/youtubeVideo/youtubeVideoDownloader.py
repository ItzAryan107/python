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


def youtubeVideoDownloader(link):  # download video
    link = youtubeLink(link)
    time.sleep(6)
    keyboard.press("space bar")
    youtube1 = YouTube(link)  # it give the all information about the particular video on youtub  e
    speak(f"the title i found, {youtube1.title}")
    videos = youtube1.streams.filter(only_video=True)
    # vid = list(enumerate(videos))
    # for i in vid:
    #     print(i[1])

    videos[0].download()
    speak("Successfully downloaded")
    keyboard.press("space bar")


# def youtubePlaylistDownloader(link):
#     link = youtubeLink("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")
#     playlist = Playlist(link)
#     # speak(f"the title i found, {playlist.title}")
#     for i in playlist.videos:
#         i.streams.first().download()


if __name__ == '__main__':
    youtubeVideoDownloader("Dark side")

