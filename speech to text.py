import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()


def speech_to_text():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Talk now")
            audiot = r.listen(source)
            myt = r.recognize_google(audiot, language="en-IN")
            print(myt)
    except:
        print("Error")


def SpeakText(command):  # Text to speech
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


a = input("Enter text to be converted")
SpeakText(a)
speech_to_text()
