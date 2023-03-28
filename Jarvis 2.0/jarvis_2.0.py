import pyttsx3 # pip install pyttsx3 
import datetime
import speech_recognition as sr #pip install SpeecRegonition


engine = pyttsx3.init()


def speak(audio):
   engine.say(audio)
   engine.runAndWait()